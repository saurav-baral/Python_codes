# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:05:04 2021

@author: sauba
"""

from Bio import SeqIO
from Bio.Seq import Seq
import os
import csv
#coordinate_files = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/6.Yellow_f4")
#coordinate_files = ["Blastobasis_adustella_coordinates.csv","Blastobasis_lacticolella_coordinates.csv","Chilo_suppressalis_coordinates.csv","Diatraea_saccharalis_coordinates.csv","Chrysoteuchia_culmella_coordinates.csv","Parapoynx_stratiotata_coordinates.csv","Ostrinia_furnacalis_coordinates.csv","Ostrinia_nubilalis_coordinates.csv","Leucinodes_orbonalis_coordinates.csv","Cnaphalocrocis_exigua_coordinates.csv","Cnaphalocrocis_medinalis_coordinates.csv","Antheraea_mylitta_coordinates.csv","Antheraea_pernyi_coordinates.csv","Samia_ricini_coordinates.csv","Actias_luna_coordinates.csv","Dendrolimus_punctatus_coordinates.csv","Bombyx_huttoni_coordinates.csv","Bombyx_mandarina_coordinates.csv","Bombyx_mori_coordinates.csv","Biston_betularia_coordinates.csv","Erannis_defoliaria_coordinates.csv","Peribatodes_rhomboidaria_coordinates.csv","Ectropis_grisescens_coordinates.csv","Hylaea_fasciaria_coordinates.csv","Crocallis_elinguaria_coordinates.csv","Ennomos_fuscantarius_coordinates.csv","Ennomos_quercinarius_coordinates.csv","Operophtera_brumata_coordinates.csv","Idaea_aversata_coordinates.csv","Carcina_quercana_coordinates.csv","Tuta_absoluta_coordinates.csv","Adela_reaumurella_coordinates.csv","Plutella_xylostella_coordinates.csv","Ypsolopha_scabrella_coordinates.csv","Adoxophyes_honmai_coordinates.csv","Apotomis_turbidana_coordinates.csv","Hedya_salicella_coordinates.csv","Notocelia_uddmanniana_coordinates.csv","Pammene_fasciana_coordinates.csv","Cydia_pomonella_coordinates.csv","Cydia_splendana_coordinates.csv"]
#this block is just for missing species
#
#
#coordinate_files_temp = []
#species_left = ["Antheraea_mylitta","Cyaniris_semiargus","Erynnis_tages","Heliconius_hermathena","Hesperia_comma","Zeuzera_pyrina","Zygaena_filipendulae"]
#for names_species in coordinate_files:
#    if (names_species[:-16]) in species_left:
#        coordinate_files_temp.append(names_species)
#coordinate_files = coordinate_files_temp
#     
#
#
coor_species = "Plodia_interpunctella"
coordinate_files = [coor_species+"_coordinates.csv"]
errors = ''
for coordinate_file_names in coordinate_files:
#    try:    
    coordinates_detail_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/6.Yellow_f4/"+coordinate_file_names,'r')
    coordinates_dict = csv.DictReader(coordinates_detail_file)
    coordinates_list = []
    for records in coordinates_dict:
        if records["Error"] == "N":
            Species= records["Species"]
#            
            Scaff = records["Scaffold"]
            reverse_c = int(records["Complement"])
            exon = records["Gene"]
            start = int(records["Start"])   
            end = int(records["Stop"])   
            frame = 1
            coordinate_detail = [Scaff,reverse_c,exon,start,end]
#            print(coordinate_detail)
            coordinates_list.append(coordinate_detail)
    print(Species)
            
    entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
    for file_names  in entries:
        if ".nhr" in file_names:
            Genome_name = file_names[:-4]
            break
    old_scaffold = ''
    
    fasta_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name),'r')
    for i in range(len(coordinates_list)):  
        out_Seq = ''
        scaffold = coordinates_list[i][0]
        reverse_c = coordinates_list[i][1]
        exon = coordinates_list[i][2]
        start = coordinates_list[i][3]   
        end = coordinates_list[i][4]
        
        if scaffold != old_scaffold:
            for record in SeqIO.parse(fasta_file,"fasta"):
            #    print (record.id)
                if record.id == Scaff:
                    sequence = str(record.seq)
        old_scaffold = scaffold
        out_Seq = Seq(sequence[start-1:end])
        if reverse_c == 1:
            out_Seq = str(out_Seq)
            dna_seq = Seq(out_Seq)
            out_Seq = dna_seq.reverse_complement()
        
        
        out_file = open(("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/6.Yellow_f4/"+Species+"_"+exon+".fa"),'w')
        output_sequence = ">"+Species+"_"+Scaff+"_"+exon+"_"+str(start)+"-"+str(end)+"\n"+str(out_Seq)+"\n"
        print(output_sequence)
        out_file.write(output_sequence)
        out_file.close()
    fasta_file.close()
#    except:
#        errors = errors + coordinate_file_names
#        print(coordinate_file_names)
#print(errors)
            