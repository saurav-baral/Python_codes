from Bio import SeqIO
import os
import subprocess
from sequence_extraction_called import sequence_extractor
import random

from scaffold_preparer import scaffold_preparer
from blast_and_check import blast_and_check
from sequence_extraction_called_2 import sequence_extract
from sequence_maker import sequence_maker
not_use_species = ''
#not_use_species = ["Lysandra_bellargus","Endotricha_flammealis","Carposina_sasakii"]

scaffold = "OU342964.1"                                            #Scaffold where the gene is present, narrows the search space
Species = "Ypsolopha_scabrella"                                      #Species to search                  
exon_numbers = "358"
scaff_area, start_area, end_area = 0,0, 440324                  #if a small exon, and the area for the exon is known, use this to first search in the small area to make blast results easier first parameter - initialize the subsearch, start and end for the coordinates start and end
done_species_temp_switch, temp_species =0, ["Celastrina_argiolus"] 

exon_names = ["Exon1","Exon2","Exon3","Exon4","Exon5","Exon6","Exon7","Exon8"]
for i in range(len(exon_numbers)):
#    print
    query_exon = (exon_names[int(exon_numbers[i])-1])                                               #Exon to search    
  
    gene = "yellow_Un1"                                                 #Gene to search    
    if query_exon == "Exon8": 
        frame = 1                                                          #open reading frame of the exon
        start_modifier = frame-1                                           #bases to be added at the beginning to maintain frame    
        stop_modifier = 0                                                 #bases to be added at the end to maintain the frame    
        last_exon = 1
        diff_number = 41                                                  #check if this is the last exon for searching stop codon 0 - not last exon 1 - last exon
    elif query_exon == "Exon1":
        frame = 1                                                          #open reading frame of the exon
        start_modifier = frame-1                                           #bases to be added at the beginning to maintain frame    
        stop_modifier = 1                                                 #bases to be added at the end to maintain the frame    
        last_exon = 0                                                     #check if this is the last exon for searching stop codon 0 - not last exon 1 - last exon
        diff_number = 27
    elif query_exon == "Exon2":
        frame = 3                                                          #open reading frame of the exon
        start_modifier = frame-1                                           #bases to be added at the beginning to maintain frame    
        stop_modifier = 1                                                 #bases to be added at the end to maintain the frame    
        last_exon = 0                                                     #check if this is the last exon for searching stop codon 0 - not last exon 1 - last exon
        diff_number = 10
    elif query_exon == "Exon3":
        frame = 3                                                          #open reading frame of the exon
        start_modifier = frame-1                                           #bases to be added at the beginning to maintain frame    
        stop_modifier = 0                                                 #bases to be added at the end to maintain the frame    
        last_exon = 0                                                     #check if this is the last exon for searching stop codon 0 - not last exon 1 - last exon
        diff_number = 16
    elif query_exon == "Exon4":
        frame = 1                                                          #open reading frame of the exon
        start_modifier = frame-1                                           #bases to be added at the beginning to maintain frame    
        stop_modifier = 2                                                 #bases to be added at the end to maintain the frame    
        last_exon = 0                                                     #check if this is the last exon for searching stop codon 0 - not last exon 1 - last exon
        diff_number = 27
    elif query_exon == "Exon5":
        frame = 2                                                          #open reading frame of the exon
        start_modifier = frame-1                                           #bases to be added at the beginning to maintain frame    
        stop_modifier = 0                                                 #bases to be added at the end to maintain the frame    
        last_exon = 0                                                     #check if this is the last exon for searching stop codon 0 - not last exon 1 - last exon
        diff_number = 15
    else:
        frame = 1                                                         #open reading frame of the exon
        start_modifier = frame-1                                           #bases to be added at the beginning to maintain frame    
        stop_modifier = 0                                                 #bases to be added at the end to maintain the frame    
        last_exon = 0                                                     #check if this is the last exon for searching stop codon 0 - not last exon 1 - last exon
        diff_number = 15
                                                        #difference threshold between query length and aligned query
    
    
    with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/species_phylo_list.txt", 'r') as f:
        phylo_species_list = f.readlines()
    
    done_species_list_temp = []                                        #placeholder for species to be used for making query
    
    
    #make a list of queries by checking if our query exon is present for other species
    
    entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/10.Yellow_Un1")            #get a list of files present in exon output directory
    
    
    for file_names  in entries :
        file_names_list = file_names.split("_")
        species_name_temp = file_names.split("Exon")[0][:-1]                                       #get species name from the file
        exon_name_in_file = file_names_list[-1].split(".")[0]                                               #get exon name from the file
    
        if (query_exon == exon_name_in_file) and (Species not in species_name_temp) and (species_name_temp not in not_use_species):                        #check if appropriate exon is present while preventing search within the species
            done_species_list_temp.append(species_name_temp)                                                #list of appropriate species
    
    #use this piece if there are species to be skipped, this code ends the program when such species is encountered
    
    #    elif (Species in not_use_species):                                            
    #        assert False
    #        break
    #
    
    done_species_list = random.sample(done_species_list_temp, len(done_species_list_temp))                  #randomize the species list to prevent errors
                                                                                   
    #print(done_species_list)                                                                               #Testing Testing
    done_species_list_temp = []
    list_top_switch = 0
    list_bot_switch = 0
    for i in range(len(phylo_species_list)):
        if Species == phylo_species_list[i].rstrip():
            print(Species)
            counter = 0
            while True:
                counter = counter + 1
                if i-counter <= 0:
                    list_top_switch = 1
                    
                if i+counter >= len(phylo_species_list)-1:
                    list_bot_switch = 1
                
                if list_top_switch == 1 and list_bot_switch == 1:
                    break
    
                if (list_top_switch == 0) and (phylo_species_list[i-counter].rstrip() in done_species_list) :
                    done_species_list_temp.append(phylo_species_list[i-counter].rstrip())
    #                print(i+counter, len(phylo_species_list), list_bot_switch)
                if (list_bot_switch == 0) and phylo_species_list[i+counter].rstrip() in done_species_list :
                    done_species_list_temp.append(phylo_species_list[i+counter].rstrip())
            
    
        if list_top_switch == 1 and list_bot_switch == 1:
            break
    done_species_list = done_species_list_temp
    if done_species_temp_switch == 1:
        done_species_list = temp_species  
#    print(done_species_list_temp)
    print("\n\n"+str(query_exon))
    
    #assert False
        
        
        
    scaffold_name = scaffold_preparer(Species, scaffold, scaff_area, start_area, end_area, gene)                            #Given species, scaffold, sub-scaffold details and gene, this prepares the blast database (makeblastdb)                   
    
    #does blast until an appropriate alignment is found
    query_difference, start, stop, query_length, query_start_coor, query_stop_coor, complement, tblast_details = blast_and_check(gene, done_species_list, query_exon, frame, Species,scaffold, diff_number)
    
    
    if query_difference < diff_number and query_difference != 0:
    
        start, stop = sequence_maker(query_exon, last_exon, Species, scaffold, complement, start, stop, query_start_coor, query_stop_coor, query_length, start_modifier, stop_modifier,query_length,query_difference,frame,  scaff_area, scaffold_name)
        
        gene_sequence = sequence_extract(Species,scaffold,start,stop,int(complement),frame, 0, scaff_area, scaffold_name)
        
        exon_output = ">"+Species+"_"+scaffold+"_"+query_exon+"_"+str(start)+"-"+str(stop)+"\n"+str(gene_sequence)+"\n"
        write_prompt = input("Write? :")
        if write_prompt.lower()[0] == "y":
            with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/10.Yellow_Un1/"+Species+"_"+query_exon+".fa",'w') as f:
                f.write(str(exon_output))
        
    else:
        print("no appropriate query found")
    print(f"\n\nLength of query: {query_length}, Query_start = {query_start_coor}, Query_stop = {query_stop_coor}, {query_difference}, scaf_start = {start}, scaf_end = {stop}")
    


