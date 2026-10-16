from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd


#Read the sequence file
file = SeqIO.read("sequence.gb", "genbank") # reads sequence/gb file and stores it into file variable
nucleotide_seq = file.seq #Stores the complete genome's DNA seuqence

print("ID: ", file.id)
#print("Sequence: ", nucleotide_seq)
print("ORGANISM: ", file.annotations["organism"])

# prints the keys in the dictionary
#print("DICTIONARY_KEYS: " , file.annotations.keys()) 

'''
#print the CDS (coding sequences) from the file.seq file only
for feature in file.features:
    if feature.type == "CDS":
        if feature.qualifiers.get("gene") ==  ["Q"]:
            q_dna = feature.extract(file.seq)
            print("Gene Q DNA: ", q_dna)

# Calculate GC content of the Q gene sequence
gc_content = gc_fraction(q_dna) * 100
print(f"GC Content: {gc_content:.2f}%")
'''

#Function
def calculate_gc_content(dna_sequence):
    return gc_fraction(dna_sequence)* 100

results = [] 

#Collect gene names, DNA lengths, and GC content for all CDS features.
for feature in file.features:
    if feature.type == "CDS":
        cds_dna = feature.extract(file.seq)
        gene_name = feature.qualifiers.get("gene", ["unknown"])[0] #get the gene name list, use unkown if missing, then select first item.
        cds_length = len(cds_dna)
        cds_gc_content = calculate_gc_content(cds_dna)


        row = {
            "Gene": gene_name,
            "DNA_Length": cds_length,
            "GC_percent": cds_gc_content
        }

        results.append(row)


df = pd.DataFrame(results)
df['GC_count'] = df['DNA_Length'] * df['GC_percent'] / 100
print(df)

#Save the CDS results without the DataFrame index
df.to_csv("lambda_cds_results.csv", index=False)

GC_count_sum = df["GC_count"].sum()
DNA_Length_sum = df["DNA_Length"].sum()
overall_GC_percentage = GC_count_sum / DNA_Length_sum * 100
print(overall_GC_percentage)

'''
#Test whether the function is working properly
sequence = "ATGC" 
print(f"The GC content of sequence is: ", calculate_gc_content(sequence),"%")
'''





