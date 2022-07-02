# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:05:04 2021

@author: sauba
"""
def sequence_extract(Species,Scaff,start,end,reverse_c,frame = 1, to_trans = 0, scaff_area = 0, scaffold_name = '', scaff_length = 0):
    from Bio import SeqIO
    from Bio.Seq import Seq
    import os
#    print(f"scaff_area = {scaff_area}, scaffold_name = {scaffold_name}, complement = {reverse_c}")
    entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
    for file_names  in entries:
        if ".nhr" in file_names:
            Genome_name = file_names[:-4]
            break
    
    out_Seq = ''
    if scaff_area == 1:
        fasta_file = open(str(scaffold_name),'r')
    else:
        fasta_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name),'r')
    for record in SeqIO.parse(fasta_file,"fasta"):
#        print("\n\n"+record.id+"\n\n")
        if record.id == Scaff:
            sequence = str(record.seq)
            if scaff_length == 1:
                return(len(sequence))
            out_Seq = Seq(sequence[start-1:end])
            
            if reverse_c == 1:
                out_Seq = str(out_Seq)
                dna_seq = Seq(out_Seq)
                out_Seq = dna_seq.reverse_complement()
#    if len(out_Seq) < 100000: #fixing error due to mistake in typing the coordinate, change this for longer sequence
##        print (out_Seq)
#        if frame == 1 :
#            out_trans = out_Seq[0:]
#        if frame == 2 :
#            out_trans = out_Seq[1:]
#        if frame == 3 :
#            out_trans = out_Seq[2:]
##        print ("\n\n"+out_trans.translate()+"\n\n") 
#    else:
#        print ("too long")
#        assert(False)
        
        
    #    break
    fasta_file.close()
    i = 0
    trans = ''
    gene_Seq = out_Seq
    if to_trans == 1:
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
    if to_trans == 1:
        
        return (gene_Seq[frame-1:].translate())
    else:
        
        return(gene_Seq)