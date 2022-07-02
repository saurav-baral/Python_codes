# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:06:21 2021

@author: sauba
"""
from Bio import SeqIO
from Bio.Seq import Seq
species_list_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/0.Temp_use_files/Yellow-Un2_species_selected.txt",'r')
species_list = species_list_file.readlines()
species_list_file.close()
frame = [1,3,3,1,2,1,1,1]
output = ''
exons_list = ["Exon1","Exon2","Exon3","Exon4","Exon5"]
full_sequence = ''
for i in range(len(species_list)):
    species = species_list[i].rstrip()
    full_sequence = ''
    for j in range(len(exons_list)):
        exon = exons_list[j]
        file_name = "C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/10.Yellow_Un1/"+str(j+1)+"."+exon+"/"+species+"_"+exon+".fa"
        exon_file = SeqIO.parse(file_name,"fasta")
        for records in exon_file:
#            print(records.seq)
            translated_seq= records.seq[frame[j]-1:].translate()
            if exon != exons_list[-1]:
                if "*" in translated_seq:
                    print(species, "\n", exon, "\n",records.seq, "\n", translated_seq)
                    input("Continue?")
            full_sequence = full_sequence+str(records.seq)
            
    
    
    if "*" in Seq(full_sequence).translate()[:-1]:
        print(species, "\n", exon, "\n",records.seq, "\n", Seq(full_sequence).translate())
        input("Continue?")
    output = output + ">"+species+"_Yellow_Un1\n"+full_sequence+"\n\n"
    print(">"+species+"_Yellow_Un1\n"+full_sequence+"\n\n")
output_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/10.Yellow_Un1/Yellow_Un1.fa",'w')
output_file.write(output)
output_file.close()
        
#        break
#    break
    