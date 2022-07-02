# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:05:04 2021

@author: sauba
"""

from Bio import SeqIO
from Bio.Seq import Seq
import os

Species= "Pieris_macdunnoughi"
entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
for file_names  in entries:
    if ".nhr" in file_names:
        Genome_name = file_names[:-4]
        break
#print(genome_name)
#Genome_name = "GCA_014332785.1_AM_v1.0_genomic.fna"
Scaff = "CAJOBZ010000035.1"
reverse_c = 1 #1 = yes, 0 = no
# for pasting 3713291	3713431
exon = "idh"
start = 2329338     
end = 2329478                  

frame = 1

if exon == "Exon_1":
    frame = 1
elif exon == "Exon_2":
    frame = 3
elif exon == "Exon_3":
    frame = 2
elif exon == "Exon_4":
    frame = 3
elif exon == "Exon_5":
    frame = 2
elif exon == "Exon_6":
    frame = 2
elif exon == "Exon_7":
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
    print ("\n\n"+out_trans.translate()) 
else:
    print ("too long")
    assert(False)
    
       
#    break
fasta_file.close()
#out_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Species+"_idh.fa"),'w')
#output_sequence = ">"+Species+"_Yellow_"+Scaff+"_"+exon+"_"+str(start)+"-"+str(end)+"\n"+str(out_Seq)+"\n"
#out_file.write(output_sequence)
#out_file.close()


#if "Exon_7" in exon:
#    exon_1_file = (open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_1_yellow-e.fa"),'r')).readlines()
#    exon_2_file = open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_2_yellow-e.fa"),'r').readlines()
#    exon_3_file = open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_3_yellow-e.fa"),'r').readlines()
#    exon_4_file = open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_4_yellow-e.fa"),'r').readlines()
#    exon_5_file = open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_5_yellow-e.fa"),'r').readlines()
#    exon_6_file = open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_6_yellow-e.fa"),'r').readlines()
#    exon_7_file = open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_7_yellow-e.fa"),'r').readlines()
#    
#    #print(exon_1_file)
#    
##    out_comb = exon_1_file[0]+exon_1_file[1][:-1]+exon_2_file[1][:-1]+exon_3_file[1]
#    out_comb = exon_1_file[0]+exon_1_file[1][:-1]+exon_2_file[1][:-1]+exon_3_file[1][:-1]+exon_4_file[1][:-1]+exon_5_file[1][:-1]+exon_6_file[1][:-1]+exon_7_file[1]
#    out_comb_seq = Seq(out_comb.split("\n")[1])
#    print("\n"+out_comb_seq.translate())
#    out_comb_file = open(("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/1.Raw/1.Lepidoptera/5.Yellow-e/2.Extracted/"+Species+".txt"),'w')
#    out_comb_file.write(out_comb)
#    out_comb_file.close()
##    exon_1_file.close()
##    exon_2_file.close()
##    exon_3_file.close()