# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 12:33:10 2021

@author: sauba
"""
import drawSvg as draw

gene = "Yellow"
exon_names = ["Exon1","Exon2","Exon3"]
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/species_phylo_list.txt", 'r') as species_list_file:
    species_list = species_list_file.readlines()
species_list = ["Bicyclus_anynana"]

#species_list = ["Apamea_monoglypha"]
# Initialize variables
Exon_coordinates = {}
Exon_coordinates_for_figure = {}

Exon_scaffold = {}
scaffolds_list = []

for species_name in species_list:
#    try:
        Species = species_name.rstrip()
        seq_dna =''
        
        
        print(f"\n\n{Species}\n")
        
        
        draw_area = draw.Drawing(2500,500,origin='center', displayInline=False)
        
        for i in range(len(exon_names)):
            exon = exon_names[i]
            with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/1.Yellow/"+exon.split("Exon")[1]+"."+exon+"/"+Species+"_"+exon+".fa",'r') as f:
                exon_file_content_list = f.readlines()
            exon_detail = exon_file_content_list[0].rstrip()
            exon_coordinates_extracted =exon_detail.split("_")[-1].split("-")
            try:
                Exon_coordinates[exon] = [int(exon_coordinates_extracted[0]), int(exon_coordinates_extracted[1])]
                current_scaffold = exon_detail.split(Species)[1].split("Exon")[0][1:-1] 
                Exon_scaffold [exon]  = current_scaffold
                if current_scaffold not in scaffolds_list:
                    scaffolds_list.append(current_scaffold)
            except:
                print(exon_detail)
                input("Error. Continue?")
        print(Exon_coordinates, Exon_scaffold)
        for scaffold in scaffolds_list:
            number_of_scaffolds = len(scaffolds_list)
            
            draw_area.append(draw.Lines(-1200, (100*number_of_scaffolds)-100,500,0,close=False,fill='#eeee00',stroke='black', stroke_width=5))
            draw_area.append(draw.Text(Species, 18, -1000, 200, fill='blue'))    
            draw_area.append(draw.Text(gene, 18, -1000, 160, fill='blue'))
    
            scaffold = scaffolds_list[0]
            draw_area.append(draw.Text(scaffold, 18, -1000, 100, fill='blue'))
            if (Exon_coordinates[exon_names[1]][0] > Exon_coordinates[exon_names[0]][0]):
                complement = 0
            else:
                complement = 1
    #        print(complement)
            if complement == 0:
                
                start_position = Exon_coordinates[exon_names[0]][0]
                counter = -1000
                
                for exon in exon_names:
                    Exon_coordinates_for_figure[exon] = [int((Exon_coordinates[exon][0]-start_position+2000)/10), int((Exon_coordinates[exon][1]-start_position+2000)/10)]
                    print(Exon_coordinates_for_figure)
                    print(counter,-10, Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0],20)
                    exon_area = draw.Rectangle(counter,-10, Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0],20,fill ='#1248ff' )
                    draw_area.append(exon_area)
    #                    break
                    if exon != exon_names[-1]:
                        arrow = draw.Lines(counter+(Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0])+10, 0, counter+(Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0])+5, 5,counter+(Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0])+5, -5,close=True,fill='#eeee00',stroke='Red', stroke_width=2)
                        draw_area.append(arrow)
                        arrow = draw.Lines(counter+(Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0])+100, 0, counter+(Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0])+95, 5,counter+(Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0])+95, -5,close=True,fill='#eeee00',stroke='Red', stroke_width=2)
                        draw_area.append(arrow)
                    draw_area.append(draw.Text((exon+":"+str(Exon_coordinates[exon][0])+"-"+str(Exon_coordinates[exon][1])), 18, counter, 25, fill='blue'))
                    counter = counter + 250
                print(Exon_coordinates_for_figure[exon_names[0]][0]-1000,-10,Exon_coordinates_for_figure[exon_names[0]][1]-Exon_coordinates_for_figure[exon_names[0]][0],20)
    
            elif complement == 1:
                start_position = Exon_coordinates[exon_names[-1]][0]
                counter = 100
                
                for exon in exon_names:
                    Exon_coordinates_for_figure[exon] = [int((Exon_coordinates[exon][0]-start_position+2000)/10), int((Exon_coordinates[exon][1]-start_position+2000)/10)]
    #            print(Exon_coordinates_for_figure)
                    exon_area = draw.Rectangle(counter,-10,Exon_coordinates_for_figure[exon][1]-Exon_coordinates_for_figure[exon][0],20,fill ='#1248ff' )
                    draw_area.append(exon_area)
                    if exon != exon_names[-1]:
                        arrow = draw.Lines(counter - 10, 0, counter -5, 5,counter - 5, -5,close=True,fill='#eeee00',stroke='Red', stroke_width=2)
                        draw_area.append(arrow)
                        arrow = draw.Lines(counter - 100, 0, counter -95, 5,counter - 95, -5,close=True,fill='#eeee00',stroke='Red', stroke_width=2)
                        draw_area.append(arrow)
                    draw_area.append(draw.Text((exon+":"+str(Exon_coordinates[exon][1])+"-"+str(Exon_coordinates[exon][0])), 18, counter, 25, fill='blue'))
                    counter = counter - 250
                print(Exon_coordinates_for_figure[exon_names[0]][0]-1000,-10,Exon_coordinates_for_figure[exon_names[0]][1]-Exon_coordinates_for_figure[exon_names[0]][0],20)
    
            else:
                print(Exon_coordinates, Exon_scaffold)
                input("Error. Continue?")
            
        

            
#            break
#    except:
#        print(species_name.rstrip())

#
#draw_area.append(draw.Lines(-250, -250,
#                    70, -49,
#                    95, 49,
#
#                    close=False,
#            fill='#eeee00',
#            stroke='black', stroke_width=2))


#
#d = draw.Drawing(500, 500, origin='center', displayInline=False)
#
## Draw an irregular polygon
#draw_area.append(draw.Lines(-80, -45,
#                    70, -49,
#                    95, 49,
#                    -90, 40,
#                    close=False,
#            fill='#eeee00',
#            stroke='black'))
#
## Draw a rectangle
#r = draw.Rectangle(-525,-10,22,20, fill='#1248ff')
#r.appendTitle("Our first rectangle")  # Add a tooltip
#draw_area.append(r)

## Draw a circle
#d.append(draw.Circle(-40, -10, 30,
#            fill='red', stroke_width=2, stroke='black'))
#
## Draw an arbitrary path (a triangle in this case)
#p = draw.Path(stroke_width=2, stroke='lime',
#              fill='black', fill_opacity=0.2)
#p.M(-10, 20)  # Start path at point (-10, 20)
#p.C(30, -10, 30, 50, 70, 20)  # Draw a curve to (70, 20)
#d.append(p)
#
## Draw text
#d.append(draw.Text('Basic text', 8, -10, 35, fill='blue'))  # Text with font size 8
#d.append(draw.Text('Path text', 8, path=p, text_anchor='start', valign='middle'))
#d.append(draw.Text(['Multi-line', 'text'], 8, path=p, text_anchor='end'))
#
## Draw multiple circular arcs
#d.append(draw.ArcLine(60,-20,20,60,270,
#            stroke='red', stroke_width=5, fill='red', fill_opacity=0.2))
#d.append(draw.Arc(60,-20,20,60,270,cw=False,
#            stroke='green', stroke_width=3, fill='none'))
#d.append(draw.Arc(60,-20,20,270,60,cw=True,
#            stroke='blue', stroke_width=1, fill='black', fill_opacity=0.3))
#
# Draw arrows
#arrow = draw.Marker(-100, -0.5, 0.9, 0.5, scale=4, orient='auto')
#arrow.append(draw.Lines(-10, -0.5, -0.1, 0.5, 0.9, 0, fill='red', close=True))
#p = draw.Path(stroke='red', stroke_width=2, fill='none',
#              marker_end=arrow)  # Add an arrow to the end of a path
#p.M(20, -40).L(20, -27).L(0, -20)  # Chain multiple path operations
#draw_area.append(arrow)
#draw_area.append(p)
#draw_area.append(draw.Line(30, -20, 0, -10,
#            stroke='red', stroke_width=2, fill='none',
#            marker_end=arrow))  # Add an arrow to the end of a line

#d.setPixelScale(2)  # Set number of pixels per geometry unit
####d.setRenderSize(400,200)  # Alternative to setPixelScale
draw_area.saveSvg('C:/Users/sauba/Desktop/example1.svg')
###d.savePng('example.png')
##
### Display in Jupyter notebook
##d.rasterize()  # Display as PNG
#print(d)  # Display as SVG