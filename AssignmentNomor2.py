def translate_codon(cod):
    tc = {
        "TTT": "Phe - (F)", "TTC": "Phe - (F)", "TTA": "Leu - (L)", "TTG": "Leu - (L)",
        "TCT": "Ser - (S)", "TCC": "Ser - (S)", "TCA": "Ser - (S)", "TCG": "Ser - (S)",
        "TAT": "Tyr - (Y)", "TAC": "Tyr - (Y)", "TAA": "_", "TAG": "_",
        "TGT": "Cys - (C)", "TGC": "Cys - (C)", "TGA": "_", "TGG": "Trp - (W)",

        "CTT": "Leu - (L)", "CTC": "Leu - (L)", "CTA": "Leu - (L)", "CTG": "Leu - (L)",
        "CCT": "Pro - (P)", "CCC": "Pro - (P)", "CCA": "Pro - (P)", "CCG": "Pro - (P)",
        "CAT": "His - (H)", "CAC": "His - (H)", "CAA": "Gln - (Q)", "CAG": "Gln - (Q)",
        "CGT": "Arg - (R)", "CGC": "Arg - (R)", "CGA": "Arg - (R)", "CGG": "Arg - (R)",

        "ATT": "Ile - (I)", "ATC": "Ile - (I)", "ATA": "Ile - (I)", "ATG": "Met - (M)",
        "ACT": "Thr - (T)", "ACC": "Thr - (T)", "ACA": "Thr - (T)", "ACG": "Thr - (T)",
        "AAT": "Asn - (N)", "AAC": "Asn - (N)", "AAA": "Lys - (K)", "AAG": "Lys - (K)",
        "AGT": "Ser - (S)", "AGC": "Ser - (S)", "AGA": "Arg - (R)", "AGG": "Arg - (R)",

        "GTT": "Val - (V)", "GTC": "Val - (V)", "GTA": "Val - (V)", "GTG": "Val - (V)",
        "GCT": "Ala - (A)", "GCC": "Ala - (A)", "GCA": "Ala - (A)", "GCG": "Ala - (A)",
        "GAT": "Asp - (D)", "GAC": "Asp - (D)", "GAA": "Glu - (E)", "GAG": "Glu - (E)",
        "GGT": "Gly - (G)", "GGC": "Gly - (G)", "GGA": "Gly - (G)", "GGG": "Gly - (G)",
    }

    if cod in tc:
        return tc[cod]
    else:
        return None

def find_codon_frequency(dna_sequence, amino_acid,aau,gcu):
    codon_count = {}
    dna_sequence = dna_sequence.upper()

    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        # print(dna_sequence)
        if(codon == "AAU"):
            aau += 1
        elif (codon == "GCU"):
            gcu += 1
    

    print("AAU: " + str(aau),"\nGCU: " + str(gcu))

dna = "AAUGCUAAU"

#Pseudocode line 1

amino = "NAN"

#Pseudocode line 2
print("mRNA: " + dna)

#Pseudocode line 3,4
find_codon_frequency(dna,amino,0,0)