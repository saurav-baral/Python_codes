# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 18:27:43 2021

@author: sauba
"""
from IPython import get_ipython
get_ipython().magic('reset -sf')


import os
import drawSvg as draw




#list of genes
gene_list = ["0.Yellow_c","0.Yellow_c_copy1","0.Yellow_c_copy2",
             "1.Yellow","1.Yellow_copy1","1.Yellow_copy2",
             "2.Yellow_b","2.Yellow_b_copy1","2.Yellow_b_like1","2.Yellow_b_like2","2.Yellow_b_like3","2.Yellow_b_like4",
             "3.Yellow_d","3.Yellow_d_copy1","3.Yellow_d_copy2","3.Yellow_d_copy3","3.Yellow_d_copy4",
             "3.Yellow_d_copy5","3.Yellow_d_copy6","3.Yellow_d_copy7","3.Yellow_d_copy8","3.Yellow_d_copy9","3.Yellow_d_copy10","3.Yellow_d_copy11",
             "4.Yellow_e","4.Yellow_e_Polyommatinae",
             "5.Yellow_f3","5.Yellow_f3_copy1","5.Yellow_f3_copy2",
             "6.Yellow_f4","6.Yellow_f4_copy1","6.Yellow_f4_copy2",
             "7.Yellow_h2",
             "8.Yellow_h3","8.Yellow_h3_copy1","8.Yellow_h3_copy2",
             "10.Yellow_Un1","11.Yellow_Un2","12.Yellow_Un3"] 

#overall list of exons
exon_names = ["Exon1","Exon2","Exon3","Exon4","Exon5","Exon6","Exon7","Exon8","Exon9","Exon10","Exon11","Exon12"]

#initialize dictionary




#reading species list from premade list
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/species_phylo_list.txt", 'r') as species_list_file:
        species_list = species_list_file.readlines()
#temp testing species
#species_list = ["Papilio_polytes"]
#species_list = ["Heliconius_melpomene"]
max_exons = 0    
error = ''

for species_name in species_list: 
        
#    try:
        #individual species name
        gene_location = {}
        draw_area = ''
        Species = species_name.rstrip()
        print(f"{Species}")
            
        #iterating over single genes
        output = 'Scaffold,Gene,Exon,Start,Stop\n'
        for gene in gene_list:
#            print(f"{gene}")
            exon_temp_dictionary = {}
            gene_temp_dictionary = {}
            
            
            #get exons folders
            gene_folder_content = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene)
            exons_folder = []
            for content in gene_folder_content:
                if os.path.isdir("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+content):
                    exons_folder.append(content.split(".")[1])
    #        print(gene,exons_folder)
            
            #search by individual exons
            if len(exons_folder) > max_exons:
                max_exons = len(exons_folder)
            scaffold = ''
            try:
                with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/1.Exon1/"+Species+"_Exon1.fa",'r') as f:
                    scaffold = f.readlines()[0].rstrip().split(Species)[1].split("Exon")[0][1:-1]
            except:
                error = error+"\t"+gene+"\t"+Species+"\tExon1\tError"
            for exon in exons_folder:
#                print(f"{exon}")
                try:
                    with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/"+gene+"/"+exon.split("Exon")[1]+"."+exon+"/"+Species+"_"+exon+".fa",'r') as f:
                        exon_file_content_list = f.readlines()
                        
                        #get the exon detail from exon fasta file
                        exon_detail = exon_file_content_list[0].rstrip()
        #                print(gene,"\n",exon_detail)
                        
                        try:
                            exon_coordinates_extracted =exon_detail.split("Exon")[1].split("_")[1].split("-")
        #                    print(exon_coordinates_extracted)
                            current_scaffold = exon_detail.split(Species)[1].split("Exon")[0][1:-1]
                            if current_scaffold in scaffold:
                                exon_temp_dictionary[exon]= [int(exon_coordinates_extracted[0]), int(exon_coordinates_extracted[1])]
        #                    print("\n\n",test_exon_dictionary)
                        except Exception:
                            print('')
                            error = error+"\t"+gene+"\t"+Species+"\t"+exon+"\tError" 
        #                    input("Error. Continue?")
        #                print(scaffold + ","+gene+","+exon+","+exon_coordinates_extracted[0]+","+exon_coordinates_extracted[1]+"\n")
                except:
                   error = error+"\t"+gene+"\t"+Species+"\t"+exon+"\tError" 
            gene_temp_dictionary[gene] = exon_temp_dictionary
            if scaffold in gene_location:
                gene_temp_dictionary = gene_location[scaffold]
                gene_temp_dictionary[gene] = exon_temp_dictionary
            else:
                gene_location[scaffold]= gene_temp_dictionary
        
        
#        for key, value in gene_location.items():
#            print(key,value)
            
        exon_temp_dictionary_2 = {}
        
        number_of_scaffolds = len(gene_location)
        
        draw_area_switch = 0
        i = 0
        gene_number_max = 0                                
        for scaffold , genes in gene_location.items():
    #        draw_area.append(draw.Lines(-1400, (150*(i+1)-250),500,(150*(i+1)-250),close=False,fill='#eeee00',stroke='black', stroke_width=3))
            gene_number = len(genes)
            if gene_number> gene_number_max:
                gene_number_max = gene_number
        for scaffold , genes in gene_location.items():
#            print(genes)
            gene_number = len(genes)
#            print(gene_number)
#            if len(genes)< 1:
#                break
            if draw_area_switch == 0:
                draw_area = draw.Drawing((500*gene_number_max)+600,300*number_of_scaffolds,origin='center', displayInline=False)
                draw_area.append(draw.Text(Species,30, -(((500*gene_number_max)+600)/2)+100, 150*number_of_scaffolds-100, fill='blue'))
                draw_area_switch= 1
            draw_area.append(draw.Text(scaffold,30, -(((500*gene_number_max)+600)/2)+100, (150*(i+1)-170), fill='blue'))
            
            
    #        print(scaffold, gene_number)
            current_exon_number = 0
            current_gene_number = 0
            gene_pos_list = []
            pos_reference = {}
            for gene, exons in genes.items():
                
#                print(exons)
                exon_number = len(exons)
                if exon_number < 1:
                    break
    #            print(scaffold,gene,gene_number, exon_number)
                blocks = gene_number
                draw_area.append(draw.Lines(-(((500*gene_number_max)+600)/2)+100, (150*(i+1)-250),(((500*gene_number_max)+600)/2)-100,(150*(i+1)-250),close=False,fill='#eeee00',stroke='black', stroke_width=3))
    #            draw_area.append(draw.Text(scaffold,30, -1400, (150*(i+1)-170), fill='blue'))
                
                
                exons_list_after_unpacking = []
                for exon, coordinates in exons.items():
                    exons_list_after_unpacking.append(exon)
                
                
                # if gene_location[scaffold][gene][exons_list_after_unpacking[0]][0] < gene_location[scaffold][gene][exons_list_after_unpacking[-1]][1]:
                if True:
                    # complement = 0
                    counter = -(((500*gene_number_max)+600)/2)+300
                    
                    gene_pos_list.append(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0])
                    
#                    print(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0])
    #                print(gene_pos_list)
                    
                    pos_reference[str(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0])] = (gene.split(".")[1]+":"+str(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0])+"-"+str(gene_location[scaffold][gene][exons_list_after_unpacking[-1]][1]))
#                    print(pos_reference)
    #                draw_area.append(draw.Text(gene.split(".")[1]+":"+str(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0])+"-"+str(gene_location[scaffold][gene][exons_list_after_unpacking[-1]][1]),25, counter+(500*current_gene_number), (150*(i+1)-220), fill='blue'))
                    
                    draw_area.append(draw.Rectangle(counter+(500*current_gene_number),(150*(i+1)-250)-20,450,40,fill ='#1248ff', fill_opacity=0.2 ))
                    
                    arrow1 = draw.Lines(int(counter + 50)+(500*current_gene_number), (150*(i+1)-250) , int(counter + 50 -20)+(500*current_gene_number), (150*(i+1)-250)+20,int(counter + 50 - 20)+(500*current_gene_number), (150*(i+1)-250)-20,close=True,fill='Red',stroke='Red', stroke_width=0, fill_opacity=0.4)
                    arrow2 = draw.Lines(int(counter + 100)+(500*current_gene_number), (150*(i+1)-250) , int(counter + 100 -20)+(500*current_gene_number), (150*(i+1)-250)+20,int(counter + 100 - 20)+(500*current_gene_number), (150*(i+1)-250)-20,close=True,fill='Red',stroke='Red', stroke_width=0, fill_opacity=0.4)
                    arrow3 = draw.Lines(int(counter + 150)+(500*current_gene_number), (150*(i+1)-250) , int(counter + 150 -20)+(500*current_gene_number), (150*(i+1)-250)+20,int(counter + 150 - 20)+(500*current_gene_number), (150*(i+1)-250)-20,close=True,fill='Red',stroke='Red', stroke_width=0, fill_opacity=0.4)
                    draw_area.append(arrow1)
                    draw_area.append(arrow2)
                    draw_area.append(arrow3)
    ##              
    #             if gene_location[scaffold][gene][exons_list_after_unpacking[0]][0] > gene_location[scaffold][gene][exons_list_after_unpacking[-1]][1]:
    #                 complement = 1
                    
    #                 gene_pos_list.append(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0]) 
    #                 pos_reference[str(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0])] = (gene.split(".")[1]+":"+str(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0])+"-"+str(gene_location[scaffold][gene][exons_list_after_unpacking[-1]][1]))
                    
    #                 counter = (((500*gene_number_max)+600)/2)-800
    # #                draw_area.append(draw.Text(gene.split(".")[1]+":"+str(gene_location[scaffold][gene][exons_list_after_unpacking[0]][0])+"-"+str(gene_location[scaffold][gene][exons_list_after_unpacking[-1]][1]),25, counter-(500*current_gene_number), (150*(i+1)-220), fill='blue')) 
    #                 draw_area.append(draw.Rectangle(counter-(500*current_gene_number),(150*(i+1)-250)-20,450,40,fill ='#1248ff', fill_opacity=0.2 ))
    #                 arrow1 = draw.Lines(int(counter + 50)-(500*current_gene_number), (150*(i+1)-250) , int(counter + 50 +20)-(500*current_gene_number), (150*(i+1)-250)+20,int(counter + 50 + 20)-(500*current_gene_number), (150*(i+1)-250)-20,close=True,fill='Red',stroke='Red', stroke_width=0, fill_opacity=0.4)
    #                 arrow2 = draw.Lines(int(counter + 100)-(500*current_gene_number), (150*(i+1)-250) , int(counter + 100 +20)-(500*current_gene_number), (150*(i+1)-250)+20,int(counter + 100 + 20)-(500*current_gene_number), (150*(i+1)-250)-20,close=True,fill='Red',stroke='Red', stroke_width=0, fill_opacity=0.4)
    #                 arrow3 = draw.Lines(int(counter + 150)-(500*current_gene_number), (150*(i+1)-250) , int(counter + 150 +20)-(500*current_gene_number), (150*(i+1)-250)+20,int(counter + 150 + 20)-(500*current_gene_number), (150*(i+1)-250)-20,close=True,fill='Red',stroke='Red', stroke_width=0, fill_opacity=0.4)
    #                 draw_area.append(arrow1)
    #                 draw_area.append(arrow2)
    #                 draw_area.append(arrow3)
    
    #                 j = 0
                current_gene_number += 1
            
            
            
            
#            print(gene_pos_list)
            gene_pos_list_sorted=sorted(gene_pos_list, key = int)
#            print(gene_pos_list)
            for j in range(len(gene_pos_list)):
                gene_string = pos_reference[str(gene_pos_list_sorted[j])]
                draw_area.append(draw.Text(gene_string,25, counter+(500*j), (150*(i+1)-220), fill='blue'))
#                print(gene_string)
                # if complement == 0:
                #     draw_area.append(draw.Text(gene_string,25, counter+(500*j), (150*(i+1)-220), fill='blue'))
                # # if complement == 1:
                #     draw_area.append(draw.Text(gene_string,25, counter-(500*j), (150*(i+1)-220), fill='blue')) 
            i += 1
        draw_area.saveSvg('C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/0.For_making_images/'+Species+"_genes.svg")
        del draw_area
        
#    except Exception:
#        print(species_name)
#        error = error+species_name+"\n"
print(error)
##print(gene_location)
##    break
#
#print(output)        
#        