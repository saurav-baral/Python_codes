# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:38:45 2021

@author: sauba
"""
from sequence_extraction_called_2 import sequence_extract

Species = "Noctua_pronuba"
exon = "Exon1"
frame = 1
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/6.Yellow_f4/"+Species+"_coordinates.csv",'r') as f:
    coordinates_list = f.readlines()
coordinate_line = coordinates_list[int(exon[4:])].split(",")
print(coordinate_line)
species,scaffold,start,stop,complement = coordinate_line[0],coordinate_line[1],int(coordinate_line[2]),int(coordinate_line[3]),int(coordinate_line[4])
sequence_extract(species,scaffold,start,stop,complement,frame,1)