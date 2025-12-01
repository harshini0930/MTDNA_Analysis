# MTDNA_Analysis
Comparative Analysis of Mitochondrial  Genomes to Understand Patterns in  Healthy Aging across Species

## Introduction
Mitochondrial function is central to aging and healthspan in animals. This project explores mitochondrial genome features of diverse species to uncover potential genomic patterns associated with healthy and extended lifespans.

## Objective
To compare mitochondrial genome features—such as gene presence/absence, CDS count, and total gene length—across species with varying lifespans, aiming to identify genetic signatures linked to healthy aging.

## Species List
Human (Homo sapiens)
House Mouse (Mus musculus)
Bowhead Whale (Balaena mysticetus)
Naked Mole Rat (Heterocephalus glaber)
Fruit Fly (Drosophila melanogaster)
Roundworm (Caenorhabditis elegans)

## Data
Note: Raw mtDNA sequences and metadata (.fasta, .gb, and .tsv files) are not included in this repository due to large file sizes.
Users can download mitochondrial genome sequences from publicly available databases such as NCBI GenBank
Example scripts in analyze/ can be used with your own sequence files to reproduce the analysis.
The repository includes results and plots (results/) to showcase outputs.

## Methods
Analysis Tools: Custom Python scripts for feature extraction; Pandas and Matplotlib for data handling and plotting.
Steps:
Download annotated mitochondrial genome files for all species.
Extract coding DNA sequence (CDS) features and gene lengths.
Calculate CDS counts and total coding region lengths for each species.
Generate gene presence/absence matrix.
Visualize data using heatmaps and barplots.

## Results
Gene Presence/Absence Matrix:
Bowhead whale and naked mole rat show greater mitochondrial gene diversity.
Human, house mouse, fruit fly, and roundworm share a more compact gene set.

CDS Count per Species:
Bowhead whale and naked mole rat have higher mitochondrial CDS feature counts.

Total CDS Gene Length per Species:
Bowhead whale and naked mole rat have significantly longer mitochondrial coding regions than other species.

## Interpretation:
Most animals maintain a highly conserved and compact mitochondrial genome.
Long-lived species like the bowhead whale and naked mole rat exhibit expanded mitochondrial gene repertoires and coding lengths, which may be linked to their longevity.
Mitochondrial genome features alone do not determine lifespan; nuclear genes, environment, and physiology also play roles.

## Conclusion
This project demonstrates that comparative mitochondrial genomics can reveal evolutionary patterns linked to healthy aging. The workflow highlights the potential of bioinformatics tools to bridge molecular biology with aging research.

## How to Run
Clone the repo.
Open the notebook in Jupyter: analyze/mtDNA_analysis.ipynb
Use your own mtDNA sequence files (FASTA/GB) or download them from NCBI GenBank.
Follow the notebook steps to reproduce the analysis.
Output plots and tables will appear in results/.


This project demonstrates that comparative mitochondrial genomics can reveal evolutionary patterns linked to healthy aging. The workflow highlights the potential of bioinformatics tools to bridge molecular biology with aging research.
