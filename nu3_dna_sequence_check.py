#Check the GC content of the nu3 gene sequence from sequence.gb file 
#and compare it to the GC content of the nu3 gene sequence from the lambda_cds_results.csv file.

nu3_dna_sequence = """ atggacgca acccgccaga tgtttgcgca
      gaaggtgtcg gcatataccg gcctgtccgt gcaggttgtg ctggataccg aggctgcagt
      gtacagcggt caggaggcca ttgatgccgg actggctgat gaacttgtta acagcaccga
      tgcgatcacc gtcatgcgtg atgcactgga tgcacgtaaa tcccgtctct caggagggcg
      aatgaccaaa gagactcaat caacaactgt ttcagccact gcttcgcagg ctgacgttac
      tgacgtggtg ccagcgacgg agggcgagaa cgccagcgcg gcgcagccgg acgtgaacgc
      gcagatcacc gcagcggttg cggcagaaaa cagccgcatt atggggatcc tcaactgtga
      ggaggctcac ggacgcgaag aacaggcacg cgtgctggca gaaacccccg gtatgaccgt
      gaaaacggcc cgccgcattc tggccgcagc accacagagt gcacaggcgc gcagtgacac
      tgcgctggat cgtctgatgc agggggcacc ggcaccgctg gctgcaggta acccggcatc
      tgatgccgtt aacgatttgc tgaacacacc agtgtaa """

print(nu3_dna_sequence.count("g") + nu3_dna_sequence.count("c"))