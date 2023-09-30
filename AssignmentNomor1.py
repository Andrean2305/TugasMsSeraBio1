def complement_dna(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna_sequence)

def translate_mrna_to_protein(mrna_sequence):
    # Define the genetic code (codon to amino acid mapping)
    genetic_code = {
        "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
        "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
        "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
        "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
        "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    }
    
    protein_sequence = []

    codons = [mrna_sequence[i:i+3] for i in range(0, len(mrna_sequence), 3)]

    for codon in codons:
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            if amino_acid == "Stop":
                break 
            protein_sequence.append(amino_acid)
        else:
            protein_sequence.append("X") 
    
    return " ".join(protein_sequence)

# Input DNA sequence Pseudo code line 1
dna_sequence = "TTACGA"

# Printing the complement Pseudo code line 2
complement_sequence = complement_dna(dna_sequence)
print("Complement:", complement_sequence)

# Printing mRNA Pseudo code line 3
mrna_sequence = dna_sequence.replace('T', 'U')
print("mRNA Sequence:", mrna_sequence)

# Printing AminoAcid Pseudo code line 4
protein_sequence = translate_mrna_to_protein(mrna_sequence)
print("Amino Acid Sequence:", protein_sequence)
