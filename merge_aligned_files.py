# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:56:53 2021

@author: sauba
"""

import os

# getting a list of files to be aligned

aligned_files_list = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/5.phylo_21_08-31/4.Aligned")

# iterating through the list
for aligned_file_name in aligned_files_list:
    # opening the file
    aligned_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/5.phylo_21_08-31/4.Aligned/" + aligned_file_name, 'r')
#    print(aligned_file_name.type())
    
    # creating names of variables where the lines of file are stored as a list
    file_name =  (aligned_file_name[:-4])
#    exec("str(aligned_file_name)" + " = []")
    
    # storing the lines of file as individual list with names same as the file
    exec(file_name + " = aligned_file.readlines()")
#    exec("print("+file_name+")")
    aligned_file.close()
#initializing empty containers
gene_name_list = []
gene_length_dict = {}
species_name_list = []

#iterating through the filenames
for list_name in aligned_files_list:
    #creating a new variable data_list which will contain all the lines of an individual file in one iteration
    #this will iterate once for each gene
    exec("data_list =" + list_name[:-4])
    #getting the gene name file name
    gene_name = list_name.split("_")[0]
    #getting the gene length from the second line
    gene_length = len(data_list[1][:-1])
    #storing gene length in a dictionary to use later
    gene_length_dict[gene_name] = gene_length
    #keeping the list of genes for later iteration
    gene_name_list.append(gene_name)
    #initiating dictonary for each gene
    exec(gene_name + "={}")
    for data_counter in range(len(data_list)):
#        print (data_counter%2)
#        print (data_list[data_counter])
        #every even line is fasta header
        if (data_counter%2 == 0) and (">" in data_list[data_counter]):
            #key is the species name
            key = (data_list[data_counter].split("_")[0][1:]+"_"+data_list[data_counter].split("_")[1])
            #making a list of species
            if key not in species_name_list:
                species_name_list.append(key)
#            print (key)
        #odd line is sequence
        else:
            #adding gene sequence to the species
            exec(gene_name+"[key] = data_list[data_counter]")
#    exec("print("+gene_name+")")
#    break
#        print (data)
#print (gene_name_list)

##total length test
gene_length_counter=0
for key, items in gene_length_dict.items():
    gene_length_counter += int(items)
print (gene_length_counter)
##print (len(species_name_list))
print(gene_name_list)
output_sequence = ''
sequence = ''
for species in species_name_list:    
    output_sequence = output_sequence + ">" + species + "\n"
    for gene_names in gene_name_list:
        sequence = ''
#        print(gene_names, species)
#        exec("print("+gene_names+"[species])")
#        print(species, gene_names)
        try:
            exec("sequence = ("+gene_names+"[species])[:-1]")
        except:
#             exec("sequence_length = ("+gene_length_dict+"[gene_names])")
            sequence_length = gene_length_dict[gene_names]
            sequence = sequence_length * "-"
#            print (sequence_length, sequence)
#            print(species, gene_names)
#            break
        output_sequence += sequence
            
#        break
    output_sequence += "\n"
#    print (output_sequence)
#    break
#        try:
#            exec("print(Species\n"+gene_names+"[species])")
#            break
#        except:
#            print(gene_names, species)
#        break
#    break
            
#print(gene_length_dict)
combined_output_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/5.phylo_21_08-31/0.combined.fa",'w')
combined_output_file.write(output_sequence)
combined_output_file.close()