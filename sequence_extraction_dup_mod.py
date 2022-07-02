# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:05:04 2021

@author: sauba
"""

from Bio import SeqIO
from Bio.Seq import Seq
import os

Species= "Danaus_plexippus"
entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
for file_names  in entries:
    if ".nhr" in file_names:
        Genome_name = file_names[:-4]
        break
Scaff = "NC_045809.1"
reverse_c = 0 #1 = yes, 0 = no
coordinates_list = [[9422261,9422480],[9427382,9427705]]
for i in range(len(coordinates_list)):
    
    
    start =  coordinates_list[i][0]
    end =   coordinates_list[i][1]
                
    
    frame = 1
    
    out_Seq = ''
    fasta_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name),'r')
    for record in SeqIO.parse(fasta_file,"fasta"):
    #    print (record.id)
        if record.id == Scaff:
            sequence = str(record.seq)
            out_Seq = Seq(sequence[start-1:end])
            if reverse_c == 1:
                out_Seq = str(out_Seq)
                dna_seq = Seq(out_Seq)
                out_Seq = dna_seq.reverse_complement()
    if len(out_Seq) < 10000: #fixing error due to mistake in typing the coordinate, change this for longer sequence
        print (out_Seq)
        if frame == 1 :
            out_trans = out_Seq[0:]
        if frame == 2 :
            out_trans = out_Seq[1:]
        if frame == 3 :
            out_trans = out_Seq[2:]
        print ("\n"+out_trans.translate()+"\n\n") 
    else:
        print ("too long")
        assert(False)
        
           
    #    break
    fasta_file.close()
