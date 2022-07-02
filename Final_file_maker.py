# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:26:33 2022

@author: sauba
"""
%reset
import os

def list_to_str(list_to_be_converted):
    s = ''
    for i in list_to_be_converted:
        s = s + i
    return s


gene_list = ["12.Yellow_Un3"]

Exon_names = ["Exon1","Exon2","Exon3","Exon4","Exon5","Exon6","Exon7","Exon8","Exon9","Exon10","Exon11","Exon12"]
output = ''
for gene in gene_list:
    gene_folder_content_all = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene)
    gene_folder_content = []
    for i in gene_folder_content_all:
        if os.path.isdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+i):
            gene_folder_content.append(i)
    gene_folder_content_sorted = sorted(gene_folder_content, key=lambda x: int(x.split('.')[0]))  
    gene_folder_content = gene_folder_content_sorted   
    species_exon_detail = {}
    for content in gene_folder_content:
        
        sequence_files_all = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+content)
        
        for sequence_files_names in sequence_files_all:
            if "0.e" not in sequence_files_names and "names" not in sequence_files_names and "old" not in sequence_files_names and "0.combined" not in sequence_files_names and "0.Exon" not in sequence_files_names and "1.Exon" not in sequence_files_names:
                species = sequence_files_names.split("Exon")[0][:-1]
        
                if species not in species_exon_detail:
                    species_exon_detail[species]= ["NO"]*(int(gene_folder_content[-1].split("Exon")[1]))
                species_exon_detail[species][int(sequence_files_names.split("Exon")[1].split(".")[0])-1] = "Yes"
    for key, value in species_exon_detail.items():
        sequence = ''
        for i in range(len(value)):
            with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+str(Exon_names[i].split("Exon")[1]+"."+Exon_names[i])+"/"+key+"_"+Exon_names[i]+".fa",'r') as sequence_file:
                # print(Exon_names[i],sequence_file.readlines())
                sequence = sequence+ list_to_str(sequence_file.readlines()[1:]).rstrip()


        output = output+">"+key+"___"+gene.split(".")[1]+"\n"+sequence+"\n\n"
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/4.Complete_details/Yellow_Un3.fa",'w') as out_file:
    out_file.write(str(output))
                    