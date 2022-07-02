# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:45:25 2021

@author: sauba
"""
from Bio import SeqIO
import os
import subprocess
from sequence_extraction_called import *
import random
not_use_species = ["Abrostola_tripartita","Acronicta_aceris","Agrotis_ipsilon","Amphipyra_berbera","Amphipyra_tragopoginis","Apamea_monoglypha","Arctia_plantaginis","Atethmia_centrago","Autographa_gamma","Autographa_pulchrina","Busseola_fusca","Clostera_curtula","Craniophora_ligustri","Euproctis_similis","Furcula_furcula","Hecatera_dysodea","Helicoverpa_armigera","Helicoverpa_zea","Heliothis_virescens","Hypena_proboscidalis","Hyphantria_cunea","Laspeyria_flexula","Lymantria_dispar","Lymantria_monacha","Mamestra_brassicae","Mamestra_configurata","Mythimna_ferrago","Mythimna_impura","Noctua_fimbriata","Noctua_janthe","Noctua_pronuba","Notodonta_dromedarius","Ochropleura_plecta","Phalera_bucephala","Pheosia_gnoma","Pheosia_tremula","Phlogophora_meticulosa","Schrankia_costaestrigalis","Sesamia_nonagrioides","Spilosoma_lubricipeda","Spodoptera_exigua","Spodoptera_frugiperda","Spodoptera_litura","Thaumetopoea_pityocampa","Trichoplusia_ni","Xestia_xanthographa","Anthocharis_cardamines","Colias_croceus","Delias_pasithoe","Eurema_mandarina","Leptidea_juvernica","Leptidea_reali","Leptidea_sinapis","Pieris_brassicae","Pieris_macdunnoughi","Pieris_napi","Pieris_rapae","Zerene_cesonia"]
#not_use_species = ''
scaffold = "LQNK01000664.1"
Species = "Phoebis_sennae"
query_exon = "Exon2"
done_species_list_temp = []
entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/8.Yellow_h3")
for file_names  in entries :
    species_name_temp = file_names[:-9]
#    print (species_name_temp)
#    assert False
    if (query_exon in file_names) and (Species not in species_name_temp) and (species_name_temp not in not_use_species):
        done_species_list_temp.append(file_names[:-9])
    elif (Species in not_use_species):
        assert False
#        break
done_species_list = random.sample(done_species_list_temp, len(done_species_list_temp))
#done_species_list = ["Heliconius_himera"]
print(done_species_list)
#query_exon = "Exon1"
gene = "yellow_h3"
frame = 2
start_modifier = 1
stop_modifier = 1
#start = int(127689 -  .1* 127689)
#end = int(127689 +  .1* 127689)
#print(start,end)
entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
for file_names  in entries:
    if ".nhr" in file_names:
        Genome_name = file_names[:-4]
        break
output = ''
fasta_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name),'r')
for record in SeqIO.parse(fasta_file,"fasta"):
    if record.id == scaffold:
        output = ">" + record.id + "\n"+ str(record.seq) + "\n"
        break
if "0.for_"+gene not in entries:
    os.mkdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene)
output_file_name = "C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+scaffold+".fna"
scaffold_output_file = open(output_file_name,'w')
scaffold_output_file.write(str(output))
scaffold_output_file.close()
fasta_file.close()
script1 = "makeblastdb -dbtype nucl -in /mnt/c/"+ output_file_name[3:]
#
subprocess.run("wsl "+ script1 , capture_output=True)

genes_folder_list = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted")
for file_names  in genes_folder_list:
    print(file_names)
    if gene[1:] in file_names:
        gene_folder = file_names
        break
tblast_details = "Species,Query_length,Query_start,Query_end,Query_difference\n"
for done_species in done_species_list:
    query_species = done_species.rstrip()
    query_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene_folder+"/"+query_species+"_"+query_exon+".fa",'r')
    for record in SeqIO.parse(query_file,"fasta"):
        print(record.id, record.seq[frame-1:].translate())
        query_file_trans_name = "C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/query_"+query_exon+".fa"
        query_file_trans = open(query_file_trans_name ,'w')
        translated_query = ">" + record.id + "\n" + record.seq[frame-1:].translate() + "\n"
        query_file_trans.write(str(translated_query))
        query_file_trans.close()
#

    
    script2 = "tblastn -query /mnt/c/"+query_file_trans_name[3:]+" -db /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+scaffold+".fna -out /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+gene+"_"+query_exon+"_"+query_species+".txt -seg no"
#print (script2)
    subprocess.run("wsl "+ script2, capture_output=True)
    script3 = "tblastn -query /mnt/c/"+query_file_trans_name[3:]+" -db /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+scaffold+".fna -out /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+gene+"_"+query_exon+"_"+query_species+".htm -html -seg no"
#print (script2)
    subprocess.run("wsl "+ script3, capture_output=True)
    
    with open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+gene+"_"+query_exon+"_"+query_species+".txt") as t:
        tblast_out = t.readlines()
    query_length = 0
    start_coor_switch = 0
    query_start_coor_switch = 0
    stop_coor_switch = 0
    query_stop_coor = 0
    for lines in tblast_out:
        if "Length" in lines and query_length == 0:
            query_length = lines.split("=")[1].rstrip()
        if "Sbjct" in lines:
            if start_coor_switch == 0:
                start_coor = int(lines.split(" ")[2])
                start_coor_switch = 1
            stop_coor =int(lines.split(" ")[-1][:-1])
        if "Query" in lines and "=" not in lines:
            if query_start_coor_switch == 0:
    #                        print(lines)
                query_start_coor = int(lines.split(" ")[2])
                query_start_coor_switch = 1
            query_stop_coor =int(lines.split(" ")[-1][:-1])
        if "Score" in lines and query_stop_coor != 0:
            break
    query_difference = int(query_length) -(int(query_stop_coor)-int(query_start_coor))
        #               
    tblast_details = tblast_details + query_species+","+str(query_length)+","+str(query_start_coor)+","+str(query_stop_coor)+","+str(query_difference)+"\n"
    print(f"Length of query: {query_length}, Query_start = {query_start_coor}, Query_stop = {query_stop_coor}, {query_difference}, scaf_start = {start_coor}, scaf_end = {stop_coor}")
#    break
    if query_difference < 5:
        break
if query_difference < 5:
    if start_coor < stop_coor:
        complement = "0"
        length = (stop_coor-start_coor)/3
        start = start_coor
        stop = stop_coor
                 
    elif start_coor > stop_coor:
        complement = "1"
        length = (-stop_coor+start_coor)/3
        start = stop_coor
        stop = start_coor
    seq_length = query_length
    
    while True:
        translated_sequence = (sequence_extractor(Species, scaffold, int(complement), start, stop,frame,1))    
        print(translated_sequence)
        if query_exon == "Exon1":
            if translated_sequence[0] != "M":
                print(translated_sequence)
                print(start, stop)
                if complement == "0":
                    start = int(start) - 3
                if complement == "1":
                    stop = int(stop) + 3
                old_trans = translated_sequence
                if "*" in translated_sequence:
                    error = "Y"
                    break
            if translated_sequence[0] == "M":
        #                            print(translated_sequence)
        #                            print(start, stop)
                break
    
    
    if query_start_coor != "1" and query_exon != "Exon1":
        if complement == "0":
            start = int(start) - 3*(int(query_start_coor)-1)
        if complement == "1":
            stop = int(stop) + 3*(int(query_start_coor)-1)
        #        print (query_stop_coor, seq_length)
    if query_stop_coor != str(seq_length):
        if complement == "0":
            stop = int(stop) + 3*(int(seq_length)-int(query_stop_coor))
        if complement == "1":
            start = int(start) - 3*(int(seq_length)-int(query_stop_coor))
    
    
    if complement == "0":
        start = int(start) - int(start_modifier)
        stop = int(stop) +  int(stop_modifier)
                   
    if complement == "1":
        start = int(start) - int(stop_modifier)
        stop = int(stop) +  int(start_modifier)
    translated_sequence = (sequence_extractor(Species, scaffold, int(complement), start, stop,frame,1)) 
    gene_sequence = (sequence_extractor(Species, scaffold, int(complement), start, stop,frame,0))    
    
    print(gene_sequence, translated_sequence)
    tblast_recorder = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/0.tblast_details.csv",'w')    
    tblast_recorder.write(tblast_details)
    tblast_recorder.close()
    
    exon_output = ">"+Species+"_"+scaffold+"_"+query_exon+"_"+str(start)+"-"+str(stop)+"\n"+str(gene_sequence)+"\n"
    
#    with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/8.Yellow_h3/"+Species+"_"+query_exon+".fa",'w') as f:
#        f.write(str(exon_output))
    
else:
    print("no appropriate query found")
print(f"Length of query: {query_length}, Query_start = {query_start_coor}, Query_stop = {query_stop_coor}, {query_difference}, scaf_start = {start}, scaf_end = {stop}")