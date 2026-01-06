codons = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": None, "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": None, "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": None, "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

#############################################################################################################

def read_file_into_lines(file_path):
    """
    A simple function to read a file into
    a list of lines, removing the newline
    character at the end.

    Arguments:
    ==========
    file_path: str
        The location of a text file to read.

    Returns:
    ========
    list[str]
        A list that contains all stripped lines
        of the input text file.
    """
    lines = []
    with open(file_path, 'r') as infile:
        for line in infile.readlines():
            cleaned = line.rstrip()
            lines.append(cleaned)
    return lines

#############################################################################################################

def parse_fasta(lines_list):
    current_sequence = ''
    current_id = ''
    sequences = {}

    for line in lines_list:
        # if line.startswith('>'):
        if line[0] == '>':
            sequences[current_id] = current_sequence
            current_id = line[1:]
            current_sequence = ''
        else:
            current_sequence = current_sequence + line

    sequences[current_id] = current_sequence
    del sequences['']
    return sequences

#############################################################################################################

def triplets(seq):
    split_seq = []
    for i in range(0, len(seq), 3):
        split_seq.append(seq[i:i+3])
    return(split_seq)
# Remove numbers 0 and 3 to get all possibilities. Starting at position 0, for length, in steps of three.

#############################################################################################################

def rev_comp(DNA):
    comp = '' 
    for nucleotide in DNA:
        if nucleotide == 'A':
            comp += 'T'
        elif nucleotide == 'T':
            comp += 'A'
        elif nucleotide == 'G':
            comp += 'C'  
        elif nucleotide == 'C':
            comp += 'G'
    # print(comp)
    rev_comp = ''
    
    for letter in comp:
        rev_comp = letter + rev_comp
    
    return(rev_comp)

#############################################################################################################

def add_quotes_to_lines(input_path, output_path):
    with open(input_path, "r") as infile, \
         open(output_path, "w") as outfile:
        for line in infile:
            outfile.write(f'"{line.rstrip()}"\n')


