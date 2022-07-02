# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 10:54:40 2021

@author: sauba
"""


def blast_and_check(gene,gene_folder, done_species_list, query_exon, frame, Species,scaffold, diff_number ):
    import os
    import subprocess
    from Bio import SeqIO
    
    
    query_difference = 9999
    tblast_details = "Species,Query_length,Query_start,Query_end,Query_difference\n"                                                                                          #tblast output csv header
    
    for done_species in done_species_list:                                                                                                                                    #iterate over species to be used for query
        query_species = done_species.rstrip()   
        print(query_species)                                                                                                                              #species to be queried
        query_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene_folder+"/"+str(query_exon.split("Exon")[1]+"."+query_exon)+"/"+query_species+"_"+query_exon+".fa",'r')                                 #take the species exon as query file
        
        #making the query file
        for record in SeqIO.parse(query_file,"fasta"):
            translated_query_seq = record.seq[frame-1:].translate()
            
            print(record.id, translated_query_seq)
            query_file_trans_name = "C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/query_"+query_exon+".fa"
            with open(query_file_trans_name ,'w') as f:
                f.write(str(">" + record.id + "\n" + translated_query_seq + "\n"))
            
    
    
        #tblastn as a text    
        script2 = "tblastn -query /mnt/c/"+query_file_trans_name[3:]+" -db /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+scaffold+".fna -out /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+gene+"_"+query_exon+"_"+query_species+".txt -seg no"
        subprocess.run("wsl "+ script2, capture_output=True)

        #tblastn as a html for visualization
        script3 = "tblastn -query /mnt/c/"+query_file_trans_name[3:]+" -db /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+scaffold+".fna -out /mnt/c/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+gene+"_"+query_exon+"_"+query_species+".htm -html -seg no"
        subprocess.run("wsl "+ script3, capture_output=True)
        
        #read the tblastn output and store the lines as a list
        with open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+gene+"_"+query_exon+"_"+query_species+".txt") as t:
            tblast_out = t.readlines()
        
        query_length = 0                                                                 #query length variable to check against the aligned result
        start_coor_switch = 0                                                            #switch for capturing the blast aligned start site of scaffold
        query_start_coor_switch = 0                                                      #switch for capturing the blast aligned start site of query
        stop_coor_switch = 0                                                             #switch for capturing the blast aligned start site
        query_stop_coor = 0                                                              #switch for capturing the blast aligned start site
        query_start_coor = 0
        start = 0
        stop = 0
        complement = 0
        start_coor = 0
        stop_coor = 0
        
        for lines in tblast_out:
            
            #storing the length of the query once query length is assigned, this condition is always false
            if "Length" in lines and query_length == 0:
                query_length = lines.split("=")[1].rstrip()
            
            #sbjct line of blast result stores the information on the aligned scaffold
            if "Sbjct" in lines:
                
                if start_coor_switch == 0:
                    start_coor = int(lines.split(" ")[2])                                                            #switch for capturing the blast aligned start site of scaffold
                    start_coor_switch = 1                                                                            #switch off after capturing the blast aligned start site of scaffold
                
                stop_coor =int(lines.split(" ")[-1][:-1])                                                            #as the aligned results may be multiple lines long, the final stop coordinate is taken
            
            #Query line of blast result stores the information on the aligned scaffold
            if "Query" in lines and "=" not in lines:                                                                #selecting the proper query line
                
                if query_start_coor_switch == 0:                                                                     #checking for start switch
        
                    query_start_coor = int(lines.split(" ")[2])                                                      #switch for capturing the blast aligned start site of query
                    query_start_coor_switch = 1                                                                      #switch off after capturing the blast aligned start site of query
                query_stop_coor =int(lines.split(" ")[-1][:-1])                                                      #as the aligned results may be multiple lines long, the final stop coordinate is taken
            
            #end loop conditions
            if "Score" in lines and query_stop_coor != 0:
                break
            
            if "Lambda" in lines:
                break
        
        query_difference = int(query_length) -(int(query_stop_coor)-int(query_start_coor))                            #calculating the coverage of the query
                    
        tblast_details = tblast_details + query_species+","+str(query_length)+","+str(query_start_coor)+","+str(query_stop_coor)+","+str(query_difference)+"\n"                             #keeping the tblast details
        
        
        print(f"Length of query: {query_length}, Query_start = {query_start_coor}, Query_stop = {query_stop_coor}, {query_difference}, scaf_start = {start_coor}, scaf_end = {stop_coor}")
        
        if query_difference < diff_number and query_difference != 0:
            
            if input("Use? (Y/N) :").lower()[0] == "y":
                #fixing the complement
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
                
                #writing tblast output to file
                with open("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/0.tblast_details.csv",'w') as f:
                    f.write(tblast_details)
                
                break
        
            
    return(query_difference,start, stop, query_length, query_start_coor, query_stop_coor, complement, tblast_details)