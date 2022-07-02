# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:06:21 2021

@author: sauba
"""
from Bio import SeqIO
species_list_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/0.Temp_use_files/Yellow-f4_species_selected.txt",'r')
species_list = species_list_file.readlines()
species_list_file.close()
output = ''
exons_list = ["Exon1","Exon2","Exon3","Exon4","Exon5","Exon6","Exon7","Exon8","Exon9"]
for i in range(len(species_list)):
    species = species_list[i].rstrip()
    full_sequence = ''
    for j in range(len(exons_list)):
        exon = exons_list[j]
        if exon == "Exon3" or exon == "Exon2":
            try:
                file_name = "C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/6.Yellow_f4/"+str(j+1)+"."+exon+"/"+species+"_"+exon+".fa"
                exon_file = SeqIO.parse(file_name,"fasta")
                for records in exon_file:
    #            print(records.seq)
                    full_sequence = full_sequence+str(records.seq)
            except:
                full_sequence = full_sequence+("N"*39)
            
        else:    
            file_name = "C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/6.Yellow_f4/"+str(j+1)+"."+exon+"/"+species+"_"+exon+".fa"
            exon_file = SeqIO.parse(file_name,"fasta")
            for records in exon_file:
    #            print(records.seq)
                full_sequence = full_sequence+str(records.seq)
    output = output + ">"+species+"_Yellow_F4\n"+full_sequence+"\n\n"
    print(">"+species+"_Yellow_F4\n"+full_sequence+"\n\n")
output_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/6.Yellow_f4/Yellow_f4.fa",'w')
output_file.write(output)
output_file.close()
        
#        break
#    break
    