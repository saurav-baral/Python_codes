# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:53:59 2021

@author: sauba
"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW

errors = ''
gene = "Yellow_Un1"
exon_names = ["Exon1","Exon2","Exon3","Exon4","Exon5","Exon6","Exon7","Exon8"]
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/species_phylo_list.txt", 'r') as species_list_file:
    species_list = species_list_file.readlines()
#species_list = ["Apamea_monoglypha"]
for species_name in species_list:
    try:
        Species = species_name.rstrip()
        seq_dna =''
        print(f"\n\n{Species}\n")
        for i in range(len(exon_names)):
            exon = exon_names[i]
            with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/10.Yellow_Un1/"+Species+"_"+exon+".fa",'r') as f:
                exon_file_content_list = f.readlines()
            sequence = Seq(exon_file_content_list[1].rstrip())
            seq_dna = seq_dna + sequence