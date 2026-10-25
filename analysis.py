from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd
import matplotlib.pyplot as plt



#Read the sequence file
file = SeqIO.read("sequence.gb", "genbank") # reads sequence/gb file and stores it into file variable
nucleotide_seq = file.seq #Stores the complete genome's DNA seuqence

print("ID: ", file.id)
print("ORGANISM: ", file.annotations["organism"])


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
df.to_csv("lambda_cds_results.csv", index=False, float_format="%.2f")

GC_count_sum = df["GC_count"].sum()
DNA_Length_sum = df["DNA_Length"].sum()
overall_GC_percentage = GC_count_sum / DNA_Length_sum * 100
print(f"Combined CDS GC content: {overall_GC_percentage:.2f}%")


#Test whether the function is working properly
sequence = "ATGC" 
print(f"The GC content of sequence is: ", calculate_gc_content(sequence),"%")



#Graph to show the distribution of GC content in the lambda phage CDS sequences
values = df['GC_percent']
plt.hist(values, color="steelblue", edgecolor="black")

plt.title('Distribution of GC Content in Lambda Phage CDS')
plt.xlabel('GC Content (%)')
plt.ylabel('Number of CDS')

plt.savefig("lambda_gc_histogram.png", dpi=300, bbox_inches="tight")
plt.show()




