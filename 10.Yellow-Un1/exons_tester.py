# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:53:59 2021

@author: sauba
"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW

errors = ''
gene = "Yellow_Un1"
exon_names = ["Exon1"]
frame = [1,3,3,1,2,1,1,1]
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/species_phylo_list.txt", 'r') as species_list_file:
    species_list = species_list_file.readlines()
#species_list = ["Amphipyra_tragopoginis"]
for species_name in species_list:
    full_sequence = ''
    try:
        Species = species_name.rstrip()
        seq_dna =''
        print(f"\n\n{Species}\n")
        for i in range(len(exon_names)):
            exon = exon_names[i]
            with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/10.Yellow_Un1/1.Exon1/old_exon1/"+Species+"_"+exon+".fa",'r') as f:
                exon_file_content_list = f.readlines()
            sequence = Seq(exon_file_content_list[1].rstrip())
#            print(exon,frame[int(exon.split("Exon")[1])-1]-1,sequence )
            translated_sequence = sequence[frame[int(exon.split("Exon")[1])-1]-1:].translate()
            print(Species,exon)
            print(translated_sequence)
            
            if exon == "Exon1":
                
                counter = 0
                while True:
                    if translated_sequence[0:1] == "M" or translated_sequence[0:1] == "X" :
                        break
                    translated_sequence = translated_sequence[1:]
                    counter += 1
                if counter > 0:
                    print(translated_sequence,"\n")
                    print(sequence,"\n\n",sequence[counter*3:],"\n")
                    sequence = sequence[counter*3:]
                output = ''
                output = (str(Seq(exon_file_content_list[0])+sequence))
                print(output)
                with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/10.Yellow_Un1/"+exon.split("Exon")[1]+".Exon"+exon.split("Exon")[1]+"/"+Species+"_"+exon+".fa",'w') as out_file:
                    out_file.write(output)
            print(exon, )
#            if exon == exon_names[-1]:
#                if "*" in translated_sequence[:-1]:
#                    extra_bits = len(translated_sequence[:-1].split("*")[1])+1
#                    sequence = sequence[:-(extra_bits*3)]
#                    
#            if exon != exon_names[-1]:
#                if "*" in translated_sequence:
#                    print(Species,exon,"\n\n", translated_sequence)
#                    break
#            full_sequence = full_sequence +  sequence
#        print(Species,"\n\n",full_sequence,"\n\n", full_sequence.translate())
        if "*" in full_sequence.translate()[:-1]:
            test = input("Error, Continue?:")
            if test.lower()[0] == "n":
                assert False
#break
    except Exception:
         
        print (species_name.rstrip())
#        break