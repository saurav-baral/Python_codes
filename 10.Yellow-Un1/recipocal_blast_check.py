# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:01:58 2021

@author: sauba
"""

import os

with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/species_phylo_list.txt", 'r') as species_list_file:
    species_list = species_list_file.readlines()
output = 'Species,Gene\n'
Reci_blast_files = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/0.recipocal_blast_Yellow_Un1")
for species in species_list:
    reci_blast_species = species.rstrip()+"_Yellow_Un1_recipocal_blast.txt"
    if reci_blast_species in Reci_blast_files:
#        print(reci_blast_species)
        with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/0.recipocal_blast_Yellow_Un1/"+reci_blast_species, "r") as recipocal_blast_file:
            recipocal_blast_file_lines = recipocal_blast_file.readlines()
        
        result_switch = 0
        for lines in recipocal_blast_file_lines:
            if "ALIGNMENTS" in lines:
                result_switch = 1
            if result_switch == 1 and ">" in lines:
#                print(lines)
                gene = ''
                gene = lines.split("(")[1].split(")")[0]
                output = output + species.rstrip() + "," + gene+"\n"
                gene = ''
                break
    else:
        output = output + species.rstrip() + ",Not present in Data\n"
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/0.recipocal_blast_Yellow_Un1/0.Final_list.csv", 'w') as f:
    f.write(output)
    
    
import pandas as pd

read_file = pd.read_csv (r'C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/0.recipocal_blast_Yellow_Un1/0.Final_list.csv')
read_file.to_excel (r'C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/0.recipocal_blast_Yellow_Un1/0.Final_list.xlsx', index = None, header=True)