# analyze/cds_features.py

from Bio import SeqIO
import os
import csv

# Folder where your GenBank files are saved
input_folder = "data"  # or the correct folder path if different
output_folder = "cds_data"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".gb"):
        species_name = filename.replace(".gb", "")
        gb_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{species_name}_cds.tsv")

        print(f"Processing {filename}...")

        with open(gb_path, "r") as handle, open(output_path, "w", newline="") as out_file:
            writer = csv.writer(out_file, delimiter="\t")
            writer.writerow(["locus_tag", "gene", "product", "protein_translation", "start", "end"])

            for record in SeqIO.parse(handle, "genbank"):
                for feature in record.features:
                    if feature.type == "CDS":
                        locus_tag = feature.qualifiers.get("locus_tag", ["-"])[0]
                        gene = feature.qualifiers.get("gene", ["-"])[0]
                        product = feature.qualifiers.get("product", ["-"])[0]
                        translation = feature.qualifiers.get("translation", ["-"])[0]
                        start = int(feature.location.start) + 1
                        end = int(feature.location.end)

                        writer.writerow([locus_tag, gene, product, translation, start, end])

        print(f"✅ Extracted CDS to {output_path}")
