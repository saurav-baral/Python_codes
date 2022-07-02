# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 07:28:16 2021

@author: sauba
"""
import os
genome_names_file = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/names",'r')
genomes = genome_names_file.readlines()
header = "Species,CAD,CAT,DDC,Ef1,GAPDH,HCL,IDH,MDH,RPS2,RPS5,WG\n"
output_data = header
genome_names_file.close()
extracted_phylo_files = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/5.phylo_21_08-31/2.Extracted")
query_name_list = ["cad_query","cat_query","ddc_query","ef1_query","gapdh_query","hcl_query","idh_query","mdh_query","rps2_query","rps5_query","wg_query"]
for genome_name in genomes:
    output_data = output_data + genome_name[:-1] + ","
    for gene_name in query_name_list:
        phylo_name = genome_name[:-1]+"_"+gene_name+".fa"
        if phylo_name in extracted_phylo_files:
            output_data = output_data + "Yes,"
        else:
            output_data = output_data + "NO,"
#            print (phylo_name)
        
    output_data =output_data + "\n"
#    print (output_data)
#    break
output_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/5.phylo_21_08-31/phylorecord.csv",'w')
output_file.write(output_data)
output_file.close()