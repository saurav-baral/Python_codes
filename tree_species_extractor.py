# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:22:02 2021

@author: sauba
"""

with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/5.phylo_21_08-31/phylo_tree.nwk",'r') as f:
    tree_sequence = f.readlines()[0]
#print(tree_sequence)
pos_counter = 0
start_switch = 0
start_position = 0
start_found_switch = 0
stop_found_switch = 0
stop_switch = 0
underscore_switch = 0
species_list = ''
while pos_counter < len(tree_sequence):
#    print(tree_sequence[pos_counter])
    if tree_sequence[pos_counter] == "_" and underscore_switch == 0:
        start_switch = 1
        underscore_position = pos_counter
        underscore_switch = 1
    elif start_switch == 1:
        pos_counter = pos_counter - 1
        if tree_sequence[pos_counter] == "(" or tree_sequence[pos_counter] == ",":
            start_position = pos_counter +1 
            start_found_switch = 1
            start_switch = 0
            stop_switch = 1
    elif stop_switch == 1:
        if underscore_switch == 1:
            pos_counter = underscore_position 
            underscore_switch = 0
        pos_counter = pos_counter + 1
        if tree_sequence[pos_counter] == ":" :
            stop_position = pos_counter 
            stop_found_switch = 1
            stop_switch = 0
    elif start_found_switch == 1 and stop_found_switch == 1:
        species = tree_sequence[start_position:stop_position]
        start_found_switch, stop_found_switch = 0,0 
        species_list=species_list+species+ "\n"
#        break
    
    else:
        pos_counter = pos_counter + 1
    
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/species_phylo_list.txt", 'w') as f:
    f.write(species_list)
    