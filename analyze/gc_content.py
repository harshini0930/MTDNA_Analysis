import os
import csv
from Bio import SeqIO

# Folder where FASTA files are located
DATA_FOLDER = "data/"
OUTPUT_FILE = "results/gc_content_analysis.csv"

# Ensure results folder exists
os.makedirs("results", exist_ok=True)

# Initialize results list
results = []

# Loop through each FASTA file in data folder
for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".fasta") or filename.endswith(".fa"):
        path = os.path.join(DATA_FOLDER, filename)
        record = SeqIO.read(path, "fasta")
        sequence = str(record.seq).upper()

        species = os.path.splitext(filename)[0]
        length = len(sequence)

        # Count nucleotides
        a = sequence.count("A")
        t = sequence.count("T")
        g = sequence.count("G")
        c = sequence.count("C")
        at_total = a + t
        gc_total = g + c

        # Calculate percentages and skew
        at_percent = round((at_total / length) * 100, 2)
        gc_percent = round((gc_total / length) * 100, 2)
        at_skew = round((a - t) / (a + t), 4) if (a + t) != 0 else 0
        gc_skew = round((g - c) / (g + c), 4) if (g + c) != 0 else 0

        # Store result
        results.append([
            species, length, a, t, g, c, at_percent, gc_percent, at_skew, gc_skew
        ])

# Write results to CSV
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Species", "Length", "A_Count", "T_Count", "G_Count", "C_Count",
        "AT_Content(%)", "GC_Content(%)", "AT_Skew", "GC_Skew"
    ])
    writer.writerows(results)

print(f"GC content analysis saved to: {OUTPUT_FILE}")
