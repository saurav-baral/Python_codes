# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:57:42 2021

@author: sauba
"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW

errors = ''
gene = "Yellow_Un2"
exon_names = ["Exon1","Exon2","Exon3","Exon4","Exon5"]
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
            with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/11.Yellow_Un2/"+exon.split("Exon")[1]+"."+exon+"/"+Species+"_"+exon+".fa",'r') as f:
                exon_file_content_list = f.readlines()
            sequence = Seq(exon_file_content_list[1].rstrip())
            seq_dna = seq_dna + sequence
        my_query  = seq_dna
        print(my_query)
        result_handle = NCBIWWW.qblast("tblastn", "nt", my_query.translate(), entrez_query='"Papilio polytes"[organism]', format_type = "Text", alignments = 1)
        with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/0.recipocal_blast_yellow_Un2/"+Species+"_"+gene+"_recipocal_blast.txt", "w") as f:
            f.write(result_handle.read())
        result_handle.close()
    except Exception:
        errors = errors+(("\nThe error species is "+ Species))
        print(("\nThe error species is "+ Species))
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/0.recipocal_blast_yellow_Un2/00.errors.txt", "w") as error_file:
    error_file.write(errors)
        