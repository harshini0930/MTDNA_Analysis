import os
import pandas as pd
import matplotlib.pyplot as plt

# Folder where your CDS .tsv files are stored
CDS_FOLDER = "cds_data"

cds_counts = {}

# Loop through each file in cds_data folder
for file in os.listdir(CDS_FOLDER):
    if file.endswith("_cds.tsv"):
        species = file.replace("_cds.tsv", "")
        file_path = os.path.join(CDS_FOLDER, file)

        # Count the number of rows (CDS features)
        df = pd.read_csv(file_path, sep="\t")
        cds_counts[species] = len(df)

# Sort by count
cds_counts = dict(sorted(cds_counts.items(), key=lambda x: x[1], reverse=True))

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(cds_counts.keys(), cds_counts.values(), color='skyblue')
plt.xlabel("Species")
plt.ylabel("Number of CDS features")
plt.title("CDS Count per Species")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
os.makedirs("results", exist_ok=True)
plt.savefig("results/cds_counts_plot.png")
plt.show()
