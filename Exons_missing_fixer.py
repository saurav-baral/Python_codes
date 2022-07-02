# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:57:48 2022

@author: sauba
"""


import os
gene_list = ["3.Yellow_d_copy4"]
Exon_names = ["Exon1","Exon2","Exon3","Exon4","Exon5","Exon6","Exon7","Exon8","Exon9","Exon10","Exon11","Exon12"]

with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/4.Complete_details/Exon_details.tsv",'r') as species_exon_list_file:
    species_exon_list = species_exon_list_file.readlines()
    
for lines in species_exon_list[1:]:
    gene,species,exons = lines.split("\t")[0],lines.split("\t")[1],lines.split("\t")[2:-1]
    
    if gene in gene_list:
        if "NO" in exons:
            for i in range(len(exons)):
                if exons[i] == "NO" and i != 0:
                    file_name = species+"_"+Exon_names[i-1]+".fa"
                    location = "C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene_list[0]+"/"+str(i)+"."+Exon_names[i-1]+"/"+file_name
                    with open(location,'r') as exon_file:
                        header = exon_file.readlines()[0]
                        # print(header)
                        # break
                        # print(exons[i],Exon_names[i],i)
                    new_header = header.replace(Exon_names[i-1],Exon_names[i])
                    print(f"Old_head = {header} \nNew_head = {new_header}")
                    sequence_placeholder = int(input("Enter Extra Sequence:"))
                    output = new_header+"NNN"+"N"*sequence_placeholder+"\n"
                    print(output)
                    
                    new_file_name = species+"_"+Exon_names[i]+".fa"
                    # new_file_name = "Agrotis_ipsilon_Exon3.fa"
                    new_location = "C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene_list[0]+"/"+str(i+1)+"."+Exon_names[i]+"/"+new_file_name
                    files_in_new_location = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene_list[0]+"/"+str(i+1)+"."+Exon_names[i])
                    if new_file_name in files_in_new_location:
                        print (f"{new_file_name} is already present")
                    prompt = input(f"Write {new_file_name}:")
                    if prompt.lower() == "y":
                        with open(new_location,'w') as exon_file_write:
                            exon_file_write.write(output)
                        
                    # new_location = 
            # print(gene,species,exons)
            # break