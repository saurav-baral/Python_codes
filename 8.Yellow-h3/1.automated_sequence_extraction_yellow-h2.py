# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:05:04 2021

@author: sauba
"""

from Bio import SeqIO
from Bio.Seq import Seq
import os
import csv
coordinate_files = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/8.Yellow_h3")

#this block is just for missing species
#
#
coordinate_files_temp = []
species_left = ["Antheraea_mylitta","Cyaniris_semiargus","Erynnis_tages","Heliconius_hermathena","Hesperia_comma","Zeuzera_pyrina","Zygaena_filipendulae"]
for names_species in coordinate_files:
    if (names_species[:-16]) in species_left:
        coordinate_files_temp.append(names_species)
coordinate_files = coordinate_files_temp
#     
#
#
    
#coordinate_files = ["Conopomorpha_cramerella_coordinates.csv"]
errors = ''
for coordinate_file_names in coordinate_files:
    try:    
        coordinates_detail_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/8.Yellow_h3/"+coordinate_file_names,'r')
        coordinates_dict = csv.DictReader(coordinates_detail_file)
        for records in coordinates_dict:
            if records["Error"] == "N":
                Species= records["Species"]
                print(Species)
                entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
                for file_names  in entries:
                    if ".nhr" in file_names:
                        Genome_name = file_names[:-4]
                        break
                #print(genome_name)
                #Genome_name = "GCA_014332785.1_AM_v1.0_genomic.fna"
                Scaff = records["Scaffold"]
                reverse_c = int(records["Complement"])  #1 = yes, 0 = no
                # for pasting 3535676	3535945
                exon = records["Gene"]
                start = int(records["Start"])   
                end = int(records["Stop"])   
                
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
#                    print (out_Seq)
                    if frame == 1 :
                        out_trans = out_Seq[0:]
                    if frame == 2 :
                        out_trans = out_Seq[1:]
                    if frame == 3 :
                        out_trans = out_Seq[2:]
#                    print ("\n\n"+out_trans.translate()) 
                else:
                    print ("too long")
                    assert(False)
                    
                       
                #    break
                fasta_file.close()
                out_file = open(("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/8.Yellow_h3/"+Species+"_"+exon+".fa"),'w')
        #        out_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/test/"+Species+"_idh.fa"),'w')
                output_sequence = ">"+Species+"_"+Scaff+"_"+exon+"_"+str(start)+"-"+str(end)+"\n"+str(out_Seq)+"\n"
                print(output_sequence)
                out_file.write(output_sequence)
                out_file.close()
    except:
        errors = errors + coordinate_file_names
        print(coordinate_file_names)
print(errors)
            