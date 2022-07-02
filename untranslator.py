# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:36:00 2022

@author: sauba
"""
from Bio import SeqIO

gene_folder = ["cad.fas","cat.fas","ddc.fas","ef1.fas","gapdh.fas","hcl.fas","idh.fas","mdh.fas","rps2.fas","rps5.fas","wg.fas"]

for gene_name in gene_folder:

    translated_file_list = SeqIO.parse("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/4.Aligned/"+gene_name.split(".")[0]+"_aligned_translated_translated.fas","fasta")
        
    untranslated_file_list = SeqIO.parse("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/4.Aligned/"+gene_name.split(".")[0]+".fas","fasta")
    untranslated_dictionary = {}
    for untranslated_gene_sequence in untranslated_file_list:
        untranslated_dictionary[str(untranslated_gene_sequence.id)]=untranslated_gene_sequence.seq
    header_switch = 0
    output = ''
    sequence = ''
    
    for gene_sequences in translated_file_list:
        sequence_id = gene_sequences.id
        sequence = gene_sequences.seq
        untranslated_gene_sequence_output = ''
        if sequence_id in untranslated_dictionary:
            untranslated_sequence = untranslated_dictionary[str(sequence_id)]
        else:
            breaker = input(f"ERROR: {sequence_id} \n untranslated = {untranslated_sequence} \n translated = {sequence}")
            if breaker.lower()[0] == "y":
                assert False
                
        untranslated_sequence_counter = 0
        translated_sequence_counter = 0
        codon = ''
        while translated_sequence_counter < len(sequence):
            if sequence[translated_sequence_counter] != "-":
                
                codon = untranslated_sequence[untranslated_sequence_counter:untranslated_sequence_counter+3]
                untranslated_sequence_counter += 3
                if codon.translate() == sequence[translated_sequence_counter]:
                    untranslated_gene_sequence_output = untranslated_gene_sequence_output + codon
                else:
                    breaker = ''
                    
                    breaker = input(f"ERROR: {sequence_id} \n untranslated = {untranslated_sequence} \n translated = {sequence}\n codon = {codon}, residue = {sequence[translated_sequence_counter]}, residue_number = {translated_sequence_counter} ")
                    breaker = input(f"ERROR: codon = {codon}, residue = {sequence[translated_sequence_counter]}")
                    if breaker.lower()[0] == "y":
                        assert False
            elif sequence[translated_sequence_counter] == "-":
                untranslated_gene_sequence_output = untranslated_gene_sequence_output + "---"
            
            else:
                breaker = ''
                breaker = input(f"ERROR: codon = {codon}, residue = {sequence[translated_sequence_counter]}")
                if breaker.lower()[0] == "y":
                    assert False
            translated_sequence_counter += 1
        output = output+">"+sequence_id+"\n"+untranslated_gene_sequence_output+"\n\n"
        
        
        
        
        
        # print(sequence_id,"\n",sequence,"\n",untranslated_sequence,"\n",untranslated_gene_sequence_output )
        # break  
    with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/6.Phylo_final_22-04-01/4.Aligned/"+gene_name.split(".")[0]+"_aligned_untranslated.fa",'w') as output_file:
        output_file.write(str(output))
    # print(output)
        