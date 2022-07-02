# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:25:31 2021

@author: sauba
"""

from sequence_extraction_called import *


phylo_species = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/phylo_species.txt",'r')
species_list = phylo_species.readlines()
#species_list = ["Abrostola_tripartita"]
#print(species_list)
query_name_list = ["Exon1"]
#species_to_test = ["Amyelois_transitella","Bicyclus_anynana","Helicoverpa_armigera","Manduca_sexta","Zerene_cesonia",]
#query_length_list = [144,40,75,38,27,37,47]
seq_modi = [[0,0]]
#query_length_list = [90,66,49,61,64,44,35]
#seq_modi = [[0,0,90],[0,0,66],[0,1,49],[2,2,61],[1,2,64],[1,0,44],[0,0,35],]
#try:
for species_name in species_list:
    try:
        print(species_name)
        header = "Species," + "Scaffold," + "Start," + "Stop," + "Complement," + "Error," + "Gene,"+ "Query_start," + "Query_stop,"+ "Query_Length\n" 
        Output_Sequence = header
        scaff = "Intial_value"
        scaff_old = "Intial_value"
        old_end = 0
        for i in range(len(query_name_list)):
            query_name = query_name_list[i]
            Length_switch = "0"
    #        query_length = query_length_list[i]
            tblast_out = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+species_name.split("\n")[0]+"/Yellow-Un3_text.txt",'r')
            lines_in_file = tblast_out.readlines()
            #print(lines_in_file)
            result_section_switch = 0
            start_coor_switch = 0
            query_start_coor_switch = 0
            stop_coor_switch = 0
            error = "N"
            break_switch = 0
    #        scaff = ''
            start = 0
            stop = 0
            start_coor = 0
            stop_coor = 0
            
            for lines in lines_in_file:
                
                if query_name in lines:
                    result_section_switch = 1
                    query_species_split = lines.split(" ")[1].split("_")
                    query_species = str(query_species_split[1]+"_"+query_species_split[2].rstrip())
                    print(query_species)
                    print(query_name)
    #                break
                if result_section_switch == 1 and "Lambda" in lines:
                    result_section_switch == 0
                    break
                    
    #                if result_section_switch == 1 and query_species not in species_to_test:
    #                    print(f"{species_name.rstrip()} has query {query_species}")
    #                    break_switch = 1
    #                    break
                    
                if result_section_switch == 1:
                    if "Length=" in lines and Length_switch == "0":
                        query_length = int(lines.split("=")[1][:-1])
                        Length_switch = 1
    #                    print(query_length)
    #                    break
                    if ("Score" in lines or ">" in lines) and (start_coor_switch == 1):
        #                print (lines)
                        break
                    if ">" in lines:
                        
                        scaff = lines.split(" ")[0][1:]
                        if scaff_old != "Intial_value" and scaff_old != scaff:
                            error = "Y"
                        scaff_old = scaff
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
        #                print (stop_coor)
                    
    #            print(query_name, start_coor, stop_coor, query_start_coor, query_stop_coor)
            if break_switch == 1:
                break
            
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
             
            else:
                error = "Y"
            if length < query_length - 100:
                error = "Y"
    #        translated_sequence = (sequence_extractor(species_name.split("\n")[0], scaff, int(complement), start, stop ))
    #        print (translated_sequence[0])
            old_trans = ''
            print(start, stop)
            start_done, stop_done = 0,0 
            while True and (start != 0 or stop != 0):
                if (query_name == "Exon1" or query_name == query_name_list[-1]):
                    frame = 1
                    translated_sequence = (sequence_extractor(species_name.split("\n")[0], scaff, int(complement), start, stop,frame ))
    #                    print(species_name.split("\n")[0], scaff, int(complement), start, stop,frame, query_name )
                    if translated_sequence == old_trans:
                        break
                    if query_name == "Exon1" and start_done == 0 :
                        if translated_sequence[0] != "M":
                            print(translated_sequence)
                            print(start, stop)
                            if complement == "0":
                                start = int(start) - 3
                            if complement == "1":
                                stop = int(stop) + 3
                            old_trans = translated_sequence
#                        if "*" in translated_sequence:
#                            error = "Y"
#                            break
                        if translated_sequence[0] == "M":
                            start_done = 1
    #                            
                            
    #                    elif query_name == "Exon1" and query_species in species_without_exon1:
    #                        print("Species_without_exon1")
    #                        if complement == "0":
    #                            start = int(start) - 3*(int(query_start_coor)-1)
    #                        if complement == "1":
    #                            stop = int(stop) + 3*(int(query_start_coor)-1)
    #                        break
                            
                    if query_name == query_name_list[-1] and stop_done == 0:
                        if translated_sequence[-1] != "*":
                            print(translated_sequence)
                            print(start, stop)
                            if complement == "0":
                                stop = int(stop) + 3
                            if complement == "1":
                                start = int(start) - 3
                            old_trans = translated_sequence
                        if translated_sequence[-1] == "*":
                            stop_done = 1
                    if start_done == 1 and stop_done == 1:
                        break
                else:
                    break
            
            if (start != 0 or stop != 0):
                start_modifier = seq_modi[i][0]
                stop_modifier = seq_modi[i][1]
            else:
                start_modifier = 0
                stop_modifier = 0            
            seq_length = query_length
            if query_start_coor != "1" and query_name != "Exon1":
                if complement == "0":
                    start = int(start) - 3*(int(query_start_coor)-1)
                if complement == "1":
                    stop = int(stop) + 3*(int(query_start_coor)-1)
    #        print (query_stop_coor, seq_length)
            if query_stop_coor != str(seq_length) and query_name != query_name_list[-1]:
                if complement == "0":
                    stop = int(stop) + 3*(int(seq_length)-int(query_stop_coor))
                if complement == "1":
                    start = int(start) - 3*(int(seq_length)-int(query_stop_coor))
    #        print(start, stop)
            if complement == "0":
                start = int(start) - int(start_modifier)
                stop = int(stop) +  int(stop_modifier)
                if old_end != 0 and old_end > stop:
                    
                    error = "Y"
                old_end = stop
                
            if complement == "1":
                start = int(start) - int(stop_modifier)
                stop = int(stop) +  int(start_modifier)
                if old_end != 0 and old_end < stop:
                    error = "Y"
                old_end = stop
    #        print(start, stop)
            
    #        print(translated_sequence)
    
            
            if start == 0 or stop == 0:
                error = "Y"
            output_format = str(species_name.split("\n")[0])+"," + str(scaff) +"," + str(start)+"," + str(stop)+"," + str(complement)+"," + str(error)+  ","+ str(query_name)+","+ str(query_start_coor)+","+str(query_stop_coor)+","+str(query_length)+ "\n"  
            Output_Sequence = Output_Sequence + output_format
        output_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/12.Yellow_Un3/"+species_name.split("\n")[0]+"_coordinates.csv",'w')
        output_file.write(Output_Sequence)
        output_file.close()
        #        break
    except:
        print(species_name[:-1], scaff, start_coor, stop_coor, complement, error)
##        break
# =============================================================================
# except:
#     
#     print(species_name[:-1], scaff, start_coor, stop_coor, complement, error)
# #    break
# =============================================================================
#print(Output_Sequence)
    









tblast_out.close()
phylo_species.close()