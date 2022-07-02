# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:01:45 2022

@author: sauba
"""
from Bio import SeqIO

species = "Heliothis_virescens"
gene_folder = "10.Yellow_Un1"
number_of_exons = 8
sequence = ''
for i in range(number_of_exons):
    file_name = "C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene_folder+"/"+species+"_Exon"+str(i+1)+".fa"
    sequence_file = SeqIO.parse(file_name,"fasta")
    for record in sequence_file:
        sequence = sequence + record.seq
#print(sequence,"\n", sequence.translate())

trans = ''
i = 0
while i < len(sequence):

    codon_seq = sequence[i:i+3]+" "
    print(codon_seq, end = '')
    if len(codon_seq[:-1]) == 3:
        translated_codon = str(codon_seq.translate())
        if translated_codon == "M":
            trans += "["+translated_codon+"  "
        else:
            trans += " "+translated_codon+"  "
    else:
        trans += " ?   "
    if i % 45 == 0 and i != 0:
        print ("\n"+trans)
        trans = ''
    i = i + 3
print ("\n"+trans)