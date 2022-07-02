# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 07:28:16 2021

@author: sauba
"""
import os
genome_names_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/phylo_species.txt",'r')
genomes = genome_names_file.readlines()
header = "Species,Exon1,Exon2,Exon3,Exon4,Exon5\n"
output_data = header
genome_names_file.close()
extracted_exon_files = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/12.Yellow_Un3")
print(extracted_exon_files)
query_name_list = ["Exon1"]
for genome_name in genomes:
    output_data = output_data + genome_name[:-1] + ","
    for gene_name in query_name_list:
        phylo_name = genome_name[:-1]+"_"+gene_name+".fa"
#        print(phylo_name)
        if phylo_name in extracted_exon_files:
            print(phylo_name)
            output_data = output_data + "Yes,"
        else:
            output_data = output_data + "NO,"
#            print (phylo_name)
        
    output_data =output_data + "\n"
#    print (output_data)
#    break
output_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/1.Tester_files/Yellow_Un3_exonrecord.csv",'w')
output_file.write(output_data)
output_file.close()