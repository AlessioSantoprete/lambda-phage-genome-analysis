# Lambda Phage Genome Analysis

My first bioinformatics project, using Python to explore the coding sequences (CDSs) of a lambda phage genome.

## What it does

- Reads a GenBank file using Biopython.
- Extracts annotated CDS sequences.
- Calculates each CDS's length and GC percentage.
- Calculates the combined GC percentage across extracted CDSs.
- Exports a CSV table and saves a histogram.

## Files

- `sequence.gb`: genome sequence and annotations.
- `analysis.py`: main analysis.
- `lambda_cds_results.csv`: CDS measurements.
- `lambda_gc_histogram.png`: distribution of CDS GC percentages.
- `nu3_dna_sequence_check.py`: independent check of the nu3 GC count.

## How to run

Requires Python, Biopython, pandas and Matplotlib.

Install dependencies:
    pip install biopython pandas matplotlib

Run from the project folder:
    python analysis.py

## Verification

I checked two CDS lengths against the GenBank annotations.

For nu3, I independently counted 363 G and C nucleotides
in a 606-nucleotide CDS, giving approximately 59.90% GC.
This matched the analysis output.

## Limitations

This project describes sequence composition. GC percentage
alone cannot explain gene function or expression.

The combined CDS GC percentage is not the whole-genome GC
percentage. Overlapping regions, if present, are counted
within each extracted CDS.

## Skills practised

Python functions, loops, lists and dictionaries; Biopython;
pandas; Matplotlib; weighted percentages; verification;
and Git/GitHub.

## Genome reference

The analysis uses the lambda phage reference genome in NCBI RefSeq.

- Accession: NC_001416
- Version: NC_001416.1
- Record: https://www.ncbi.nlm.nih.gov/nuccore/NC_001416.1

The input sequence and annotations are stored in `sequence.gb`.