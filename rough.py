# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 01:38:39 2021

@author: sauba
"""

from Bio import SeqIO
from Bio.Seq import Seq
Species= "Leptidea_sinapis"
exon_1_file = (open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_1.fa"),'r')).readlines()
exon_2_file = open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_2.fa"),'r').readlines()
exon_3_file = open(("F:/2021-04-22_Genomes/1.Lepidoptera/ncbi_dataset/data/"+Species+"/Exon_3.fa"),'r').readlines()
#print(exon_1_file)

out_comb = exon_1_file[0]+exon_1_file[1][:-1]+exon_2_file[1][:-1]+exon_3_file[1]
out_comb_seq = Seq(out_comb.split("\n")[1])
print(out_comb_seq.translate())
#print(out_comb_file)