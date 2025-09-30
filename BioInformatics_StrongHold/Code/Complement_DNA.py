with open("BioInformatics_StrongHold/Example_Data/rosalind_revc.txt", "r") as file:
    string = file.read().strip()
    
def ComplementDNA(string):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in string)
result=(ComplementDNA(string)[::-1]) # Reverse the complemented string


with open("BioInformatics_StrongHold/Output/Complement_DNA_Output.txt", "w") as file:
    file.write(result)
