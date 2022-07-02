# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 07:45:12 2022

@author: sauba
"""





import os
from Bio import SeqIO
from Bio.Seq import Seq

def list_to_str(list_to_be_converted):
    s = ''
    for i in list_to_be_converted:
        s = s + i
    return s

def sequence_printer(out_Seq):
    trans = ''
    i = 0
    while i < len(out_Seq):

        codon_seq = out_Seq[i:i+3]+" "
        print(codon_seq, end = '')
        if len(codon_seq[:-1]) == 3:
            translated_codon = str(codon_seq.translate())
            if translated_codon == "M":
                trans += "["+translated_codon+"  "
            else:
                trans += " "+translated_codon+"  "
        else:
            trans += " ?   "
        if i % 45 == 0 and i != 0:
            print ("\n"+trans)
            trans = ''
        i = i + 3
    print ("\n"+trans)
gene_list = ["0.Yellow_c","0.Yellow_c_copy1","0.Yellow_c_copy2",
             "1.Yellow","1.Yellow_copy1","1.Yellow_copy2",
             "2.Yellow_b","2.Yellow_b_copy1","2.Yellow_b_like1","2.Yellow_b_like2","2.Yellow_b_like3","2.Yellow_b_like4",
             "3.Yellow_d","3.Yellow_d_copy1","3.Yellow_d_copy2","3.Yellow_d_copy3","3.Yellow_d_copy4",
             "3.Yellow_d_copy5","3.Yellow_d_copy6","3.Yellow_d_copy7","3.Yellow_d_copy8","3.Yellow_d_copy9","3.Yellow_d_copy10","3.Yellow_d_copy11",
             "4.Yellow_e","4.Yellow_e_Polyommatinae",
             "5.Yellow_f3","5.Yellow_f3_copy1","5.Yellow_f3_copy2",
             "6.Yellow_f4","6.Yellow_f4_copy1","6.Yellow_f4_copy2",
             "7.Yellow_h2",
             "8.Yellow_h3","8.Yellow_h3_copy1","8.Yellow_h3_copy2",
             "10.Yellow_Un1","11.Yellow_Un2","12.Yellow_Un3"] 
# gene_list = ["5.Yellow_f3"]
Exon_names = ["Exon1","Exon2","Exon3","Exon4","Exon5","Exon6","Exon7","Exon8","Exon9","Exon10","Exon11","Exon12"]
output = "Gene\tSpecies\tExon1\tExon2\tExon3\tExon4\tExon5\tExon6\tExon7\tExon8\tExon9\tExon10\tExon11\tExon12"

species_list = []

for gene in gene_list:
    gene_folder_content_all = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene)
    gene_folder_content = []
    for i in gene_folder_content_all:
        # print(os.path.isdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+i))
        if os.path.isdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+i):
            gene_folder_content.append(i)
    gene_folder_content_sorted = sorted(gene_folder_content, key=lambda x: int(x.split('.')[0]))  
    gene_folder_content = gene_folder_content_sorted     

    species_exon_detail = {}
    
    for content in gene_folder_content:
        
        sequence_files_all = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+content)
        
        for sequence_files_names in sequence_files_all:
            if "0.e" not in sequence_files_names and "names" not in sequence_files_names and "old" not in sequence_files_names and "0.combined" not in sequence_files_names and "0.Exon" not in sequence_files_names and "1.Exon" not in sequence_files_names:
                species = sequence_files_names.split("Exon")[0][:-1]
        
                if species not in species_exon_detail:
                    species_exon_detail[species]= ["NO"]*(int(gene_folder_content[-1].split("Exon")[1]))
                species_exon_detail[species][int(sequence_files_names.split("Exon")[1].split(".")[0])-1] = "Yes"
                
    
    for key, value in species_exon_detail.items():
        sequence = ''
        if (str(key)+"\n") not in species_list:
            species_list.append(str(key)+"\n")
        for i in range(len(value)):
            with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+str(Exon_names[i].split("Exon")[1]+"."+Exon_names[i])+"/"+key+"_"+Exon_names[i]+".fa",'r') as sequence_file:
                # print(Exon_names[i],sequence_file.readlines())
                sequence = sequence+ list_to_str(sequence_file.readlines()[1:]).rstrip()
                if "ACTCAAGTAAAACAGCCAGCCATTGTss" in sequence:
                    print(f"Gene : {gene}, Species : {key} {Exon_names[i]}")
                    assert(False)
        
        
        translated_sequence = Seq(sequence).translate()
        if "*" in translated_sequence[:-1]:
            print(f"Gene : {gene}, Species : {key}\n{sequence}")
            sequence_printer(Seq(sequence))    
            assert(False)
        # break
    # break
        # output = output +"\n"+ str(gene+"\t"+key+"\t")
        # for i in value:
        #     output = output+str(i+"\t")
        # # print(output)
        # # break


with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/4.Complete_details/Species_list.txt",'w') as output_file:
    output_file.write(list_to_str(sorted(species_list)))
    # break