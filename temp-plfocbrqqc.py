dna_string = str(raw_input("Insert dna string"))
nu_c = dna_string.count('c')
nu_g = dna_string.count('g')
lenght_dna =  len(dna_string)
percent = (nu_c+nu_g)*100.0/lenght_dna
print(percent)