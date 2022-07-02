# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 12:55:26 2017

@author: Bhrigu
"""
from Bio import SeqIO
import os, errno
import csv

def all_comparison(location,sequence_length):
    print sequence_length
    comparison_file_list = open(str(location+"comparison\\comparison_list.txt"), "r")
    average_comparison_file= open(str(location+"avg_comp.txt"), 'w')
    average_comparison_file.write("POS\tS\tNS\tGap\n")
    nonsynonymous_mutation=open(str(location+"ns.txt"),'w')
    nonsynonymous_mutation.write("POS\tNS\n")
    synonymous_mutation_counter={}
    nonsynonymous_mutation_counter={}
    gap_counter={}

    for i in range(1,sequence_length+1):
#        print i
        synonymous_mutation_counter[str(i)]=0.0
        nonsynonymous_mutation_counter[str(i)]=0.0
        gap_counter[str(i)]=0.0
    No_of_comparisons = 0
    for files in comparison_file_list.readlines():
        No_of_comparisons+=1
        individual_comparison_file = open(files[:-1],"r")
        individual_comparison_file_table = csv.DictReader(individual_comparison_file, delimiter = "\t")
        
        for lines in individual_comparison_file_table:
            synonymous_mutation_counter[lines["POS"]] = float(synonymous_mutation_counter[lines["POS"]]) + float(lines["Sbase"] )
            nonsynonymous_mutation_counter[lines["POS"]] = float(nonsynonymous_mutation_counter[lines["POS"]]) + float(lines["NSbase"] )
            gap_counter[lines["POS"]] = float(gap_counter[lines["POS"]]) + float(lines["Gapbase"])
    for i in range(1,sequence_length+1):
        average_comparison_file.write(str(i)+"\t"+str(synonymous_mutation_counter[str(i)]/No_of_comparisons)+"\t"+str(nonsynonymous_mutation_counter[str(i)]/No_of_comparisons)+"\t"+str(gap_counter[str(i)]/No_of_comparisons)+"\n")
        
    counter = 1
    while counter < sequence_length:
        synonymous_substitutions = synonymous_mutation_counter[str(counter)] + synonymous_mutation_counter[str(counter+1)] + synonymous_mutation_counter[str(counter+2)]
        nonsynonymous_substitutions = nonsynonymous_mutation_counter[str(counter)] + nonsynonymous_mutation_counter[str(counter+1)] + nonsynonymous_mutation_counter[str(counter+2)]
        total_mutation = synonymous_substitutions+nonsynonymous_substitutions
        if total_mutation == 0.0:
            nonsynonymous_mutation.write(str(counter)+"\t"+str(nonsynonymous_substitutions)+"\n"+str(counter+1)+"\t"+str(nonsynonymous_substitutions)+"\n"+str(counter+2)+"\t"+str(nonsynonymous_substitutions)+"\n")
        else:
            nonsynonymous_mutation.write(str(counter)+"\t"+str(nonsynonymous_substitutions/total_mutation)+"\n"+str(counter+1)+"\t"+str(nonsynonymous_substitutions/total_mutation)+"\n"+str(counter+2)+"\t"+str(nonsynonymous_substitutions/total_mutation)+"\n")
        counter = counter + 3
    nonsynonymous_mutation.close()
    average_comparison_file.close()
    comparison_file_list.close()

def aligner(location, sequence_file_1, sequence_file_2):

    file1_for_comparison = SeqIO.parse(location+"temporary_exon_folder\\"+sequence_file_1,'fasta')
    file2_for_comparison = SeqIO.parse(str(location+"temporary_exon_folder\\"+sequence_file_2), 'fasta')
    for record1, record2 in zip(file1_for_comparison, file2_for_comparison):
        "test_script"

    comparison_file_name = (location+"comparison\\"+sequence_file_1[:-4] + "vs"+ sequence_file_2[:-4]+".txt")
    output_file = open( comparison_file_name,"w")
    comparison_file_name_list.write(comparison_file_name+"\n")
    print comparison_file_name
    
    out_header = "POS\tBase1\tAA1\tBase2\tAA2\tNS\tS\tBaseChange\tNSbase\tSbase\tGapbase\t" +sequence_file_1[:-4] + "vs"+ sequence_file_2[:-4]+"\n"
    output_file.write(out_header)    
    
    
    
    sequence_length = len(str(record1.seq))
    counter = 0
    while counter <= (len(str(record1.seq))-3):
        codon_sequence1 = record1.seq[counter:counter+3]
        codon_sequence2 = record2.seq[counter:counter+3]
        output = ""
        ns = '0'
        s ='0'
        pos1_change = '0'
        pos2_change = '0'
        pos3_change = '0'
        if ("-" in codon_sequence1) or ("-" in codon_sequence2):
#            print codon_sequence1, codon_sequence2
            output =  str(counter+1)+"\t"+record1.seq[counter]+'\t'+"-"+'\t'+record2.seq[counter]+'\t'+"-"+'\t'+"-"+"\t"+"-"+"\t"+"-"+"\t"+"0"+"\t"+"0"+"\t"+"1"+"\n"+str(counter+2)+"\t"+record1.seq[counter+1]+'\t'+"-"+'\t'+record2.seq[counter+1]+'\t'+"-"+'\t'+"-"+"\t"+"-"+"\t"+"-"+"\t"+"0"+"\t"+"0"+"\t"+"1"+"\n"+str(counter+3)+"\t"+record1.seq[counter+2]+'\t'+"-"+'\t'+record2.seq[counter+2]+'\t'+"-"+'\t'+"-"+"\t"+"-"+"\t"+"-"+"\t"+"0"+"\t"+"0"+"\t"+"1"+"\n"
        else:
            amino_acid_seq1 = codon_sequence1.translate()
            amino_acid_seq2 = codon_sequence2.translate()
            if codon_sequence1 != codon_sequence2:
                if amino_acid_seq1 == amino_acid_seq2: 
                    s = "1"
                else:
                    ns = "1"
                if record1.seq[counter] != record2.seq[counter]:
                    pos1_change = '1'
                elif record1.seq[counter+1] != record2.seq[counter+1]:
                    pos2_change = '1'
                if record1.seq[counter+2] != record2.seq[counter+2]:
                    pos3_change = '1'
            output = str(counter+1)+"\t"+record1.seq[counter]+'\t'+amino_acid_seq1+'\t'+record2.seq[counter]+'\t'+amino_acid_seq2+'\t'+ns+"\t"+s+"\t"+pos1_change+"\t"+str(int(ns)*int(pos1_change))+"\t"+str(int(s)*int(pos1_change))+"\t"+"0"+"\n"+str(counter+2)+"\t"+record1.seq[counter+1]+'\t'+"-"+'\t'+record2.seq[counter+1]+'\t'+"-"+'\t'+ns+"\t"+s+"\t"+pos2_change+"\t"+str(int(ns)*int(pos2_change))+"\t"+str(int(s)*int(pos2_change))+"\t"+"0"+"\n"+str(counter+3)+"\t"+record1.seq[counter+2]+'\t'+"-"+'\t'+record2.seq[counter+2]+'\t'+"-"+'\t'+ns+"\t"+s+"\t"+pos3_change+"\t"+str(int(ns)*int(pos3_change))+"\t"+str(int(s)*int(pos3_change))+"\t"+"0"+"\n"
                
            
                        
        output_file.write(str(output))
        counter = counter + 3
#        print base1, base2
        
    output_file.close()
    return sequence_length    



def align_prep(location,output_names_file):
    exon_file_name = open(output_names_file,'r')
    name_tuple =[]
    for file_names in exon_file_name:
        name_tuple.append(file_names.replace("\n","")) 
    print len(name_tuple)
    for tuple_item_number in range(0,len(name_tuple)):
        sequence_file_1 = name_tuple[tuple_item_number]
        for tuple_item_number2 in range(tuple_item_number+1,len(name_tuple)):
            sequence_file_2 = name_tuple[tuple_item_number2]
            y=( aligner(location, sequence_file_1, sequence_file_2))
    return y
            





location = "D:/1.Work/2018-09-14_dsx_reanalyzed/2.dsx_gene/4.hymenoptera/2.wasps/4.exon4/1.dn_ds_analysis/"
temporary_exon_storage = location + "temporary_exon_folder"
final_output = location + "comparison"


try:
    os.makedirs(temporary_exon_storage)
    os.makedirs(final_output)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
comparison_file_name_list = open(str(location+"comparison/comparison_list.txt"), "w")    
input_file_exons = location +"exon4_modified_aligned.best.fas"
output_names_file = location + "names.txt"

sequences = SeqIO.parse(input_file_exons, 'fasta') 
output_name = open(output_names_file, "w")
for record in sequences:
    sequence_name = str(record.id)
    counter = 0
    species_name = sequence_name.replace("|",'')
#    for letters in sequence_name:
#       if letters == ":":
#            species_name = sequence_name[:counter-6]
#            break
#       counter = counter + 1
##    print exon[:-1],species_name
    individual_sequence_file_name = location + "temporary_exon_folder\\"+species_name+".fas"
    output_name.write(str(species_name+".fas\n"))
    output_temporary_exon_file = open(individual_sequence_file_name, 'w')
    output = str(">"+record.id+"\n"+record.seq)
    output_temporary_exon_file.write(output)
    output_temporary_exon_file.close()
    








output_name.close()
y = align_prep(location,output_names_file)
#print y
comparison_file_name_list.close()
all_comparison(location,y)
