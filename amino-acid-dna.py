# strSeqOne = input("Enter Sequence One: ")
# strSeqTwo = input("Enter Sequence Two: ")

seq_one = "--RTIIALETHDVRFPtsreldgsdamnpdpdYSAAYVVLRTDGAedLAGYGLVFTIgRG"
seq_two = "mmPKIIDAKVIITCPG----------------RNFVTLKIMTDEG--VYGLGDATLN-GR"

#Dictionary of amino acid / codon pairs
codon_table = {'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
               'K': ['AAA', 'AAG'], 'N': ['AAT', 'AAC'], 'M': ['ATG'], 'D': ['GAT', 'GAC'], 'F': ['TTT', 'TTC'] ,
               'C': ['TGT', 'TGC'], 'P': ['CCT', 'CCC', 'CCA', 'CCG'], 'Q': ['CAA', 'CAG'],
               'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'E': ['GAA', 'GAG'], 'T': ['ACT', 'ACC', 'ACA', 'ACG'],
               'G': ['GGT', 'GGC', 'GGA', 'GGG'], 'W': ['TGG'], 'H': ['CAT', 'CAC'], 'Y': ['TAT', 'TAC'],
               'I': ['ATT', 'ATC', 'ATA'], 'V': ['GTT', 'GTC', 'GTA', 'GTG'], 'A': ['GCT', 'GCC', 'GCA', 'GCG']}

optcodon_table = {'a': 'GCT', 'c': 'TGT', 'e': 'GAG', 'd': 'GAC', 'g': 'GGT', 'f': 'TTC', 'i': 'ATC', 'h': 'CAC', 'k': 'AAG',
               'm': 'ATG', 'l': 'TTG', 'n': 'AAC', 'q': 'CAA', 'p': 'CCT', 's': 'TCT', 'r': 'CGC', 't': 'ACA', 'w': 'TGG', 
               'v': 'GTG', 'y': 'TAC'}               

def compare(str_one, str_two):
    score = 0
    index = 0
    while index < len(str_one):
        if str_one[index] == str_two[index]:
            if str_one[index] == "G" or str_one[index] == "C":
                score += 1.4
            else: 
                score += 1
        index += 1
    return score


def run_seqences(strA, strB):
    strA_counter = 0
    counter = 0
    list_counter = 0
    top_score = 0
    str_one_letter = ""
    str_two_letter = ""
    str_one_best = ""
    str_two_best = ""
    str_one_final = ""
    str_two_final = ""

    while strA_counter < len(strA):    
        counter = 0
        top_score = 0
        str_one_best = ""
        str_two_best = ""
        str_one_letter = strA[strA_counter]
        str_two_letter = strB[strA_counter]
        check_upper = str_one_letter.isupper()
        check_alpha = str_one_letter.isalpha()
        check_lower_strA = str_one_letter.islower()
        check_lower_strB = str_two_letter.islower()
        if check_upper is True and check_alpha is True:
            while counter < len(codon_table[str_one_letter]): #cycle through the first letters list
                list_counter = 0
                while list_counter < len(codon_table[str_two_letter]): #compare the first list to the second list
                    score = compare(codon_table[str_one_letter][counter], codon_table[str_two_letter][list_counter])
                    if score > top_score:
                        top_score = score
                        str_one_best = codon_table[str_one_letter][counter]
                        str_two_best = codon_table[str_two_letter][list_counter]
                    list_counter += 1
                counter += 1
            if top_score == 0: #if no matches then go to opt table
                str_one_best = optcodon_table.get(str_one_letter.lower())
                str_two_best = optcodon_table.get(str_two_letter.lower())          
        if check_lower_strA is True:
            str_one_best = optcodon_table.get(str_one_letter)
        if check_lower_strB is True:
            str_two_best =  optcodon_table.get(str_two_letter)
        str_one_final += str_one_best
        str_two_final += str_two_best    
        print(str_one_letter + " & " + str_two_letter + " => " + str_one_best + " " + str_two_best + " " + str(top_score))
        strA_counter += 1
    print("\n Sequence One:")    
    print(str_one_final)
    print("\n Sequence Two:")
    print(str_two_final)         
 
if __name__ == "__main__":
    run_seqences(seq_one,seq_two)
