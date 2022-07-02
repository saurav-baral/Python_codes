# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:05:04 2021

@author: sauba
"""
def sequence_extractor(Species, Scaff, reverse_c, start, end, frame = 1, trans = 1 ):
    from Bio import SeqIO
    from Bio.Seq import Seq
    import os
    
    
    entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
    for file_names  in entries:
        if ".nhr" in file_names:
            Genome_name = file_names[:-4]
            break
    #print(genome_name)
    #Genome_name = "GCA_014332785.1_AM_v1.0_genomic.fna"
    
#    reverse_c = 0 #1 = yes, 0 = no
    # for pasting 3713291	3713431
#    exon = "idh"
#    start = 3713291
         
#    end = 3713434                  
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
#        print (out_Seq)
        if frame == 1 :
            out_trans = out_Seq[0:]
        if frame == 2 :
            out_trans = out_Seq[1:]
        if frame == 3 :
            out_trans = out_Seq[2:]
#        return (out_trans.translate()) 
    else:
        print ("too long")
        assert(False)
        
        
    #    break
    fasta_file.close()
    if trans == 1:
        return (out_trans.translate())
    else:
        return(out_Seq)
#print(sequence_extractor("Carposina_sasakii", "CP053153.1", 1, 10055832, 10056257 ))
