# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:18:11 2022

@author: sauba
"""
from Bio import SeqIO

files_list = ["cad_aligned_untranslated.fa","cat_aligned_untranslated.fa","ddc_aligned_untranslated.fa","ef1_aligned_untranslated.fa","gapdh_aligned_untranslated.fa","hcl_aligned_untranslated.fa","idh_aligned_untranslated.fa","mdh_aligned_untranslated.fa","rps2_aligned_untranslated.fa","rps5_aligned_untranslated.fa","wg_aligned_untranslated.fa"]

final_output = ''
gene_details = {}
gene_name_list = []
gene_length = {}
species_list = []
for gene_files in files_list:
    gene_name = gene_files.split("_")[0]
    gene_name_list.append(gene_name)
    
    with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/5.Aligned/"+gene_files,'r') as gene:
            
        gene_records = SeqIO.parse(gene,'fasta')
        for records in gene_records:
            species_name = str(records.id).split("_")[0]+"_"+str(records.id).split("_")[1]
            gene_details[str(gene_name+"_"+species_name)] = str(records.seq)
            
            if species_name not in species_list:
                species_list.append(species_name)
            if gene_name not in gene_length:
                gene_length[gene_name] = len(records.seq)
            if len(records.seq) != gene_length[gene_name]:
                input(f"Error! gene = {gene_name} , len(record.seq), gene_length[gene_name]")

# print(gene_name_list)
print(gene_length)
# print(gene_details)
# print(species_list)
final_gene_sequences = {}
for gene in gene_name_list:
    for species in species_list:
        if species not in final_gene_sequences:
            final_gene_sequences[species] = ''
        
        if str(gene+"_"+species) not in gene_details:
            sequence = gene_length[gene]*"-"
            # print(str(gene+"_"+species))
        else:
            sequence = gene_details[str(gene+"_"+species)]
        
        final_gene_sequences[species] = final_gene_sequences[species] + sequence

for key,value in final_gene_sequences.items():
    final_output = final_output + ">"+key+"\n"+value+"\n"

cfg_out = ''
current_length = 0
for key,value in gene_length.items():
    gene_name = key
    gene_length = value
    cfg_out = cfg_out + gene_name+"_pos1 = "+ str(current_length+1) + "-" + str(current_length+gene_length)+"\\3;\n"+gene_name+"_pos2 = "+ str(current_length+2) + "-" + str(current_length+gene_length)+"\\3;\n"+gene_name+"_pos3 = "+ str(current_length+3) + "-" + str(current_length+gene_length)+"\\3;\n"
    current_length = current_length+gene_length
print(cfg_out)
                

# with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/5.Aligned/combined.fa",'w') as output_file:
#     output_file.write(final_output)