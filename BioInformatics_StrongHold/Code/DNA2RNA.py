with open("BioInformatics_StrongHold/Example_Data/rosalind_rna.txt", "r") as file:
    string = file.read().strip()

def DNA2RNA(string):
    return string.replace("T","U")
result=DNA2RNA(string)
with open("BioInformatics_StrongHold/Output/DNA2RNA_Output.txt", "w") as file:
    file.write(result)
