# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:50:08 2022

@author: sauba
"""
from Bio import SeqIO
from textwrap import wrap

# gene_folders = ["10.Yellow_Un1","11.Yellow_Un2","12.Yellow_Un3","1.Yellow","2.Yellow_b","3.Yellow_c","4.Yellow_d","5.Yellow_e","6.Yellow_f3","7.Yellow_f4","8.Yellow_h2","9.Yellow_h3"]
# for gene in gene_folders:
#     gene_name = gene.split(".")[1]
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/5.Aligned/Partition_finder/combined_removed.phy",'r') as phylip_file:
    phylip_file_list = phylip_file.readlines()

species_number = phylip_file_list[0].split(" ")[0]
sequence_length = phylip_file_list[0].split(" ")[1]     
species_dictionary = {}
i = 1
species_names_list = ""
while i < len(phylip_file_list):
    sequence_name,sequence = phylip_file_list[i].split("     ")[0],phylip_file_list[i].split("     ")[1]
    species_names_list = species_names_list+"             "+sequence_name+"\n"
    species_dictionary[sequence_name] = sequence
    i = i+1

nexus_file = (f"#NEXUS\n[ Title ]\nbegin taxa;\n       dimensions ntax={species_number};\n       taxlabels\n{species_names_list}\n;\nend;\nbegin characters;\n       dimensions nchar={sequence_length[:-1]};\n       format missing=? gap=- datatype= DNA;\n       matrix\n")

for key, value in species_dictionary.items():
    counter = 0
    each_gene_sequence = ''
    for seqs in value:
        
        if counter == 60:
            each_gene_sequence = each_gene_sequence + "\n"
            counter = 0
        each_gene_sequence = each_gene_sequence + seqs 
        counter = counter + 1
    nexus_file = nexus_file + key + "\n"+each_gene_sequence+"\n"
nexus_file = nexus_file + ";\nend;\n"
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/5.Aligned/Partition_finder/infile.nex",'w') as nex_file:
    nex_file.write(nexus_file)