## -*- coding: utf-8 -*-
#"""
#Created on Mon May 31 15:30:07 2021
#
##@author: sauba
##"""
##
##import subprocess
##import sys
##
##def install(package):
##    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
##    
##install("biopython")
#
#
##import os
##Species= "Antheraea_mylitta"
#import csv
##
##coordinates_detail_file = open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/3.Phylo/2.for_automation/coordinates.csv",'r')
##coordinates_dict = csv.DictReader(coordinates_detail_file)
###print (coordinates_dict(0))
##for i in coordinates_dict:
###    print (i["Species"])
##foo = ["bar","test"]
##for i in foo:
###    foo = "bar"
##    exec(i + " = 'something else'")
##    print (bar)
#    
##
##print (1 % 2)
#
#from Bio import SeqIO
#from Bio.Seq import Seq
#import os
##sequence_extractor(Species, Scaff, reverse_c, start, end, frame = 1 ):
#Species,Scaff,reverse_c,start,end,frame = "Carposina_sasakii", "CP053153.1", 0, 10055832, 10056257, 1
#
#entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
#for file_names  in entries:
#    if ".nhr" in file_names:
#        Genome_name = file_names[:-4]
#        break
##print(genome_name)
##Genome_name = "GCA_014332785.1_AM_v1.0_genomic.fna"
#
##    reverse_c = 0 #1 = yes, 0 = no
## for pasting 3713291	3713431
##    exon = "idh"
###    start = 3713291
##     
###end = 3713434                  
##out_Seq = ''
##fasta_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name),'r')
##for record in SeqIO.parse(fasta_file,"fasta"):
###    print (record.id)
##    if record.id == Scaff:
##        sequence = str(record.seq)
##        out_Seq = Seq(sequence[start-1:end])
##        if reverse_c == 1:
##            out_Seq = str(out_Seq)
##            dna_seq = Seq(out_Seq)
##            out_Seq = dna_seq.reverse_complement()
##if len(out_Seq) < 10000: #fixing error due to mistake in typing the coordinate, change this for longer sequence
##    print (out_Seq)
##    if frame == 1 :
##        out_trans = out_Seq[0:]
##    if frame == 2 :
##        out_trans = out_Seq[1:]
##    if frame == 3 :
##        out_trans = out_Seq[2:]
##    print ("\n\n"+out_trans.translate()) 
###    return (out_trans.translate()) 
##else:
##    print ("too long")
##    assert(False)
##    
##    
###    break
##fasta_file.close()
##return (out_trans.translate())

#import os
#
#cmd = "git --version"
#
##returned_value = os.system(cmd)
##
##print(returned_value)
#
#import subprocess
#file = "/mnt/c/Users/sauba/Desktop/Work_Stuff/MRJP/0.for_automation_temp_files/00.Temp/test.sh"
#print(subprocess.run("wsl sh "+ file, shell=True))


#class bcolors:
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKCYAN = '\033[96m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
#    
#print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

#from graphics import *
#win = GraphWin()
#
#
#
#pt = Point(100, 50)
#pt.draw(win)
#
#win.close()

#from graphics import *
#
#
#def main():
#    win = GraphWin('Face', 200, 150) # give title and dimensions
##    win.yUp() # make right side up coordinates!
#
#    head = Circle(Point(40,100), 25) # set center and radius
#    head.setFill("yellow")
#    head.draw(win)
#
#    eye1 = Circle(Point(30, 105), 5)
#    eye1.setFill('blue')
#    eye1.draw(win)
#
#    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
#    eye2.setWidth(3)
#    eye2.draw(win)
#
#    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
#    mouth.setFill("red")
#    mouth.draw(win)
#
#    label = Text(Point(100, 120), 'A face')
#    label.draw(win)
#
#    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
#    message.draw(win)
#    win.getMouse()
#    win.close()
#
#main()
#
#assert False
#


from Bio import SeqIO
from Bio.Seq import Seq

sequence = Seq("AACAATATGTATTGGAAATATTTCATGTTAAGCCTCGTAGTGATCGAAAATTCTATAGGGTACCCAAAAAATTTAGCTTGGAACGGTGGACCGATACATTTGGGTTGTGAACATGGAACTGATTTGTGGATGAAAAGTGAACAGCACATAAGANNTAATGTTATAGTCATCAAAGCCGTGACTTACATGGATGATATCTACGTTATATCTCCG")
print(sequence.translate())