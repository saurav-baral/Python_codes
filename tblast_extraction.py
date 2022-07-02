# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:25:31 2021

@author: sauba
"""
phylo_species = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/2.for_automation/phylo_species.txt",'r')
species_list = phylo_species.readlines()
#print(species_list)
query_name = "wg_query"
query_length = 175
scaff = "Intial_value"
header = "Species," + "Scaffold," + "Start," + "Stop," + "Complement," + "Error," + "Gene\n" 
Output_Sequence = header
for species_name in species_list:
#    print(species_name)
    tblast_out = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+species_name.split("\n")[0]+"/phylo_text.txt",'r')
    lines_in_file = tblast_out.readlines()
    #print(lines_in_file)
    result_section_switch = 0
    start_coor_switch = 0
    stop_coor_switch = 0
    error = "N"
    for lines in lines_in_file:
        if query_name in lines:
            result_section_switch = 1
        if result_section_switch == 1:
            if ("Score" in lines or ">" in lines) and (start_coor_switch == 1):
#                print (lines)
                break
            if ">" in lines:
                scaff = lines.split(" ")[0][1:]
            if "Sbjct" in lines:
                if start_coor_switch == 0:
                    start_coor = int(lines.split(" ")[2])
                    start_coor_switch = 1
                stop_coor =int(lines.split(" ")[-1][:-1])
#                print (stop_coor)
            
    #print(scaff, start_coor, stop_coor)
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
    if length < query_length - 0.05*query_length:
        error = "Y"
                    
    
    output_format = str(species_name.split("\n")[0])+"," + str(scaff) +"," + str(start)+"," + str(stop)+"," + str(complement)+"," + str(error)+  ","+ str(query_name[:-6])+"\n"  
    Output_Sequence = Output_Sequence + output_format
    #print(species_name[:-1], scaff, start_coor, stop_coor, complement, error)
#    break
#print(Output_Sequence)
output_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/2.for_automation/coordinates.csv",'w')
output_file.write(Output_Sequence)
output_file.close()
    









tblast_out.close()
phylo_species.close()