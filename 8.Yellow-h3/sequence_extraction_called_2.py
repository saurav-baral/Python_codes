# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:05:04 2021

@author: sauba
"""
def sequence_extract(Species,Scaff,start,end,reverse_c,frame = 1):
    from Bio import SeqIO
    from Bio.Seq import Seq
    import os
    
#    Species= "Dendrolimus_punctatus"
    entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
    for file_names  in entries:
        if ".nhr" in file_names:
            Genome_name = file_names[:-4]
            break
    #print(genome_name)
    #Genome_name = "GCA_014332785.1_AM_v1.0_genomic.fna"
#    Scaff = "CM022539.1"
#    reverse_c = 0 #1 = yes, 0 = no
    # for pasting 3713291	3713431
    exon = "idh"
#    start =   11830143                                       
#    end =     11830306                   
    
#    frame = 1
    
    if exon == "Exon_1":
        frame = 1
    elif exon == "Exon_2":
        frame = 3
    elif exon == "Exon_3":
        frame = 2
    elif exon == "Exon_4":
        frame = 3
    elif exon == "Exon_5":
        frame = 2
    elif exon == "Exon_6":
        frame = 2
    elif exon == "Exon_7":
        frame = 1
    
    out_Seq = ''
    fasta_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name),'r')
    for record in SeqIO.parse(fasta_file,"fasta"):
    #    print (record.id)
        if record.id == Scaff:
            sequence = str(record.seq)
            out_Seq = Seq(sequence[start-1:end])
            if reverse_c == 1:
                out_Seq = str(out_Seq)
                dna_seq = Seq(out_Seq)
                out_Seq = dna_seq.reverse_complement()
    if len(out_Seq) < 10000: #fixing error due to mistake in typing the coordinate, change this for longer sequence
        print (out_Seq)
        if frame == 1 :
            out_trans = out_Seq[0:]
        if frame == 2 :
            out_trans = out_Seq[1:]
        if frame == 3 :
            out_trans = out_Seq[2:]
        print ("\n\n"+out_trans.translate()+"\n\n") 
    else:
        print ("too long")
        assert(False)
        
           
    #    break
    fasta_file.close()
    i = 0
    trans = ''
    
    if frame == 2 :
        codon_seq = out_Seq[i:i+1]+" "
        print(codon_seq, end = '')
        out_Seq = out_Seq[1:]
        trans = "  "
    if frame == 3 :
        codon_seq = out_Seq[i:i+2]+" "
        print(codon_seq, end = '')
        out_Seq = out_Seq[2:]
        trans = "   "
    while i < len(out_Seq):
    
        codon_seq = out_Seq[i:i+3]+" "
        print(codon_seq, end = '')
        if len(codon_seq[:-1]) == 3:
            translated_codon = str(codon_seq.translate())
            if translated_codon == "M":
                trans += "["+translated_codon+"  "
            else:
                trans += " "+translated_codon+"  "
        else:
            trans += " ?   "
        if i % 45 == 0 and i != 0:
            print ("\n"+trans)
            trans = ''
        i = i + 3
    print ("\n"+trans)