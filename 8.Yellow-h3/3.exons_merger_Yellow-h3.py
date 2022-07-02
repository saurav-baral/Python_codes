# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:06:21 2021

@author: sauba
"""
from Bio import SeqIO
species_list_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/0.Temp_use_files/Yellow-h3_species_selected.txt",'r')
species_list = species_list_file.readlines()
species_list_file.close()
output = ''
exons_list = ["Exon1","Exon2","Exon3"]
for i in range(len(species_list)):
    species = species_list[i][:-1]
    full_sequence = ''
    for j in range(len(exons_list)):
        exon = exons_list[j]
        file_name = "C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/8.Yellow_h3/"+str(j+1)+"."+exon+"/"+species+"_"+exon+".fa"
        exon_file = SeqIO.parse(file_name,"fasta")
        for records in exon_file:
#            print(records.seq)
            full_sequence = full_sequence+str(records.seq)
    output = output + ">"+species+"_Yellow_H3\n"+full_sequence+"\n\n"
output_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/8.Yellow_h3/Yellow_h3.fa",'w')
output_file.write(output)
output_file.close()
        
#        break
#    break
    