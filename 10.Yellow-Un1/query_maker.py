# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 01:29:10 2021

@author: sauba
"""
import os
from sequence_extraction_called import *

species_name = "Pieris_rapae"
gene_name = "XM_022263887.1"

files = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+species_name)
for file_names  in files:
        if ".gff" in file_names:
            gff_file_name = file_names
            break
gff_file_opener = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+species_name+"/"+gff_file_name,'r')
gff_file = gff_file_opener.readlines()
gff_file_opener.close()
query_switch = 0
cds_lines = []
for lines in gff_file:
    if gene_name in lines and "CDS" in lines.split("\t"):
        cds_lines.append(lines.split("\t"))
        query_switch = 1
    if "CDS" not in lines and query_switch == 1:
        break
scaff = cds_lines[0][0]
if cds_lines[0][6] == "-":
    complement = 1
else:
    complement = 0
output = ''
extra_output = ''
for i in range(len(cds_lines)):
    Exon_name = "Exon"+str(i+1)+"_"+species_name
    start = int(cds_lines[i][3])
    stop = int(cds_lines[i][4])
    frame = int(cds_lines[i][7])+1
    translated_sequence = (sequence_extractor(species_name, scaff, int(complement), start, stop,frame ))
    print(species_name, scaff, int(complement), start, stop,frame )
    output= output + ">"+Exon_name+"\n"+translated_sequence+"\n"
    extra_output = extra_output + Exon_name+":"+str(frame)+"\n"+ (sequence_extractor(species_name, scaff, int(complement), start, stop,frame,0 ))+"\n\n"
query_file = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/0.queries/10.Yellow_Un1_queries/yellow_Un1_"+species_name+"_query.txt",'w')
query_file.write(str(output))
query_file.close()
print(output)
print(extra_output)    
#print (cds_lines)
    

    