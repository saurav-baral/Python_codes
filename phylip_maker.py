# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:24:01 2022

@author: sauba
"""
from Bio import SeqIO
import string
import random

# gene = "Yellow_Un3"

output = ''
fasta_head_info = ''
sequence_counter = 0
sequence_length = 0
sequence_length_old = 0
sequence_file  = SeqIO.parse("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/5.Aligned/Partition_finder/combined_removed.fa", 'fasta')
for sequence in sequence_file:
    header_old = sequence.id
    header_new = ''.join(random.choice(string.ascii_letters) for x in range(5))
    fasta_head_info = fasta_head_info + header_old + "\t"+header_new + "\n"
    
    sequence_counter += 1
    
    sequence_length = len(sequence.seq)
    if sequence_length_old != 0 and sequence_length != sequence_length_old:
        breaker = input(f"sequence_length_old = {sequence_length_old},sequence_length = {sequence_length} \n Error. Continue?")
        if breaker.lower()[0] == 'n':
            assert False
    sequence_length_old = len(sequence.seq)
    output = output + header_new + "     " + sequence.seq + "\n"

with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/5.Aligned/Partition_finder/combined_removed_header_info.txt",'w') as header_file:
    header_file.write(fasta_head_info)

with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/5.Aligned/Partition_finder/combined_removed.phy",'w') as phylip_file:
    output = str(sequence_counter)+" "+str(sequence_length)+"\n"+output
    phylip_file.write(str(output))