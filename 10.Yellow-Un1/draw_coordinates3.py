# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 07:45:16 2021

@author: sauba
"""

import drawSvg as draw
Species = "Bicyclus_anynana"
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/0.For_making_images/"+Species+".csv", 'r') as species_coordinate_file:
    species_coordinate_file_list = species_coordinate_file.readlines()
print(species_coordinate_file_list)
counter = 1

old_scaffold = ''

gene_list = []
scaffold_list = []
scaff_start_coordinates = 0
scaff_stop_coordinates = 0
number_of_scaffolds = 0
counter = 1
while counter < len(species_coordinate_file_list):
    if species_coordinate_file_list[counter].split(",")[0] not in scaffold_list:
        print(species_coordinate_file_list[counter].split(",")[0])
        scaffold_list.append(species_coordinate_file_list[counter].split(",")[0])
    counter = counter + 1
counter = 1

for scaffold in scaffold_list:
    gene_list = []
    counter_2  = 1
    while counter < len(species_coordinate_file_list):
        print(species_coordinate_file_list[counter].split(",")[0])
        if species_coordinate_file_list[counter].split(",")[0] == scaffold:
            print(species_coordinate_file_list[counter].split(",")[1])
            if species_coordinate_file_list[counter].split(",")[1] not in gene_list:
                print(species_coordinate_file_list[counter].split(","))
                gene_list.append(species_coordinate_file_list[counter].split(",")[1])
        else:
            break
        
        counter_2 += 1
    print(gene_list)
    counter = counter + counter_2

print(len(scaffold_list))    
    
        