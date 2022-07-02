# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:28:42 2021

@author: sauba
"""
import os

new_genomes_list_file = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/1.Temp_files/genome.txt", 'r')
new_genomes_list = new_genomes_list_file.readlines()
new_genomes_list_file.close()

output = ''
list_of_genome_files = []
genome_list = ''

for i in range(len(new_genomes_list)):
    genome_folder_files_list = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+new_genomes_list[i][:-1])
#    print(new_genomes_list[i][:-1],"aa")
    concat_switch = 0
    for files in genome_folder_files_list:
#        print(new_genomes_list[i][:-1],"aa")
        if "chr" in files:
#            print(new_genomes_list[i][:-1],"aa")
#            print(new_genomes_list[i][:-1]) 
#            output = output + "cd /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+ new_genomes_list[i][:-1] + "\ncat *.fna > genome.fna\nmakeblastdb -dbtype nucl -in genome.fna\n"
            list_of_genome_files.append([new_genomes_list[i][:-1],"genome.fna"])
            concat_switch = 1
            break
    if concat_switch == 0:
        for files in genome_folder_files_list:
            if ".fna" in files:
#                output = output + "cd /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+ new_genomes_list[i][:-1] + "\nmakeblastdb -dbtype nucl -in "+files+"\n"
                list_of_genome_files.append([new_genomes_list[i][:-1],files])
                break
#output_file = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/1.Temp_files/genome_prepare.txt",'w')
#output_file.write(output)
#output_file.close()
for entries in list_of_genome_files:
    genome_list = genome_list+ entries[0]+"\t"+entries[1]+"\n"
output_file_genome_list = open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/1.Temp_files/genome_list_all.txt",'w')
output_file_genome_list.write(genome_list)
output_file_genome_list.close()
#    break