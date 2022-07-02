# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 15:39:43 2022

@author: sauba
"""
from Bio import SeqIO

gene_names = ["cad.fas","cat.fas","ddc.fas","ef1.fas","gapdh.fas","hcl.fas","idh.fas","mdh.fas","rps2.fas","rps5.fas","wg.fas"]

for gene in gene_names:
    fasta_file = SeqIO.parse("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/4.Aligned/"+gene,"fasta")
    translated_output = ''
    for sequences in fasta_file:
    # print(sequences.id,sequences.seq)
        translated_output = translated_output +">"+ str(sequences.id)+"\n"+str((sequences.seq).translate())+"\n\n"
    with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/4.Aligned/"+gene.split(".")[0]+"_translated.fas",'w') as out_file:
        out_file.write(str(translated_output))
    