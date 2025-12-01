import os
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt

# Folder containing GenBank files
data_dir = "data"

# Dictionary to store total CDS gene lengths
species_lengths = {}

for filename in os.listdir(data_dir):
    if filename.endswith(".gb") or filename.endswith(".gbff"):
        species = os.path.splitext(filename)[0]
        total_length = 0

        filepath = os.path.join(data_dir, filename)
        for record in SeqIO.parse(filepath, "genbank"):
            for feature in record.features:
                if feature.type == "CDS":
                    total_length += len(feature.location)

        species_lengths[species] = total_length

# Convert to DataFrame
df = pd.DataFrame(list(species_lengths.items()), columns=["Species", "Total_CDS_Length"])
df = df.sort_values(by="Total_CDS_Length", ascending=False)

# Save result
os.makedirs("results", exist_ok=True)
df.to_csv("results/total_gene_lengths.csv", index=False)

# Plot bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df["Species"], df["Total_CDS_Length"], color='teal')
plt.title("Total CDS Gene Length per Species")
plt.xlabel("Species")
plt.ylabel("Total Gene Length (bp)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save and show
plt.savefig("results/total_gene_lengths_barplot.png")
plt.show()
