# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 23:58:37 2021

@author: sauba
"""

from Bio import SeqIO
import os
import subprocess

query_species_list = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/0.queries/7.Yellow_h2_queries/Just_exon1.txt",'r').readlines()
#print(query_species_list)
for Species_name in query_species_list:
    Species = Species_name.split("\n")[0]
    entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
    for file_names  in entries:
        if ".nhr" in file_names:
            Genome_name = file_names[:-4]
            break
    script = "tblastn -query /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/0.queries/7.Yellow_h2_queries/Yellow_h2_Exon1_query.txt -seg no -db /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name+" -out   /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/yellow_h2_amtra_exon1.htm -html -matrix PAM250"                       
    print(script)
    subprocess.run("wsl "+ script, capture_output=True)