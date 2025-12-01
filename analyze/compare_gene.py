# analyze/compare_gene.py

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path to the folder containing all .tsv files
CDS_FOLDER = "cds_data"
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

gene_data = {}

# Read each CDS .tsv file
for filename in os.listdir(CDS_FOLDER):
    if filename.endswith(".tsv"):
        species = filename.replace(".tsv", "")
        file_path = os.path.join(CDS_FOLDER, filename)
        
        try:
            df = pd.read_csv(file_path, sep="\t")
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")
            continue
        
        if "gene" not in df.columns:
            print(f"⚠️ Skipping {filename} — no 'gene' column found.")
            continue

        gene_data[species] = df["gene"].dropna().str.strip().unique().tolist()

# Create gene presence matrix
all_genes = sorted(set(g for genes in gene_data.values() for g in genes))
matrix = pd.DataFrame(0, index=gene_data.keys(), columns=all_genes)

for species, genes in gene_data.items():
    for gene in genes:
        if gene in matrix.columns:
            matrix.at[species, gene] = 1

# Save CSVs
matrix.to_csv(os.path.join(OUTPUT_FOLDER, "gene_presence_matrix_binary.csv"))
matrix.T.to_csv(os.path.join(OUTPUT_FOLDER, "gene_presence_matrix_visual.csv"))

# Plot heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(matrix, cmap="Greens", cbar=True, linewidths=0.5, linecolor='gray')
plt.title("Gene Presence/Absence Matrix")
plt.xlabel("Genes")
plt.ylabel("Species")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_FOLDER, "gene_presence_matrix_heatmap.png"))
plt.show()

print("\n✅ Gene presence matrix and heatmap saved in 'output/' folder.")
