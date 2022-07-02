# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:08:51 2021

@author: sauba
"""
import os

list_of_files_file = open("F:/2021-04-22_Genomes/4.Lepidoptera/0.fetch_2_1/ncbi_dataset/data/names", 'r')
list_of_files = list_of_files_file.readlines()
for i in range(len(list_of_files)):
#    print (list_of_files[i])
    entries = os.listdir("F:/2021-04-22_Genomes/4.Lepidoptera/0.fetch_2_1/ncbi_dataset/data/"+list_of_files[i][:-1])
    for genome_name in entries:
        if ".fna" in genome_name:
#            print (genome_name)
            genome_file = open("F:/2021-04-22_Genomes/4.Lepidoptera/0.fetch_2_1/ncbi_dataset/data/"+list_of_files[i][:-1]+"/"+genome_name, 'r')
            last_line = genome_file.readlines()[-1]
            if "\n" not in last_line:
                print(list_of_files[i][:-1], genome_name, last_line)
            
            genome_file.close()
#            break
        
#    break
    
#    
#    if "chr1.fna" in entries:
#        print (entries[1])
#        break
#    for file_names  in entries:
#    if ".nhr" in file_names:
#        Genome_name = file_names[:-4]
#        break
list_of_files_file.close()