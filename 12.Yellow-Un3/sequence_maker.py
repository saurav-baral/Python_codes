def sequence_maker(query_exon, last_exon, Species, scaffold, complement, start, stop, query_start_coor, query_stop_coor, seq_length, start_modifier, stop_modifier,query_length,query_difference,frame, scaff_area, scaffold_name):
    from sequence_extraction_called_2 import sequence_extract
    from Bio import SeqIO
    from Bio.Seq import Seq
    import os
    
    
    entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
    for file_names  in entries:
        if ".nhr" in file_names:
            Genome_name = file_names[:-4]
            break
    error = ''
    old_trans = ''
    out_Seq = ''
    if scaff_area == 1:
        fasta_file = open(str(scaffold_name),'r')
    else:
        fasta_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name),'r')
    for record in SeqIO.parse(fasta_file,"fasta"):
#        print("\n\n"+record.id+"\n\n")
        if record.id == scaffold:
            sequence = str(record.seq)
            
    
    while True:
        if (query_exon == "Exon1" or last_exon == 1):
            
            out_Seq = Seq(sequence[start-1:stop])
            if complement == "1":
                out_Seq = str(out_Seq)
                dna_seq = Seq(out_Seq)
                out_Seq = dna_seq.reverse_complement()
            translated_sequence = out_Seq.translate()
#            print("\n\n"+scaffold_name+","+str(scaff_area)+"\n\n")
#            print(f"first pass translated_sequence, from sequence maker : {translated_sequence}\n")
            
            # Make sure not stuck in a loop
            if translated_sequence == old_trans:
                break
            #
            
#            print(translated_sequence)
            if query_exon == "Exon1":
                if translated_sequence[0] != "M":

                    if complement == "0":
                        start = int(start) - 3
                    if complement == "1":
                        stop = int(stop) + 3
                    old_trans = translated_sequence
                    print(translated_sequence)
                    print(start, stop,"\n\n")                    
                    if "*" in translated_sequence:
                        error = "Y"
                        break
                
                if translated_sequence[0] == "M":
            #                            print(translated_sequence)
            #                            print(start, stop)
                    break
                
            if last_exon == 1:
                
                if translated_sequence[-1] != "*":

                    if complement == "0":
                        stop = int(stop) + 3
                    if complement == "1":
                        start = int(start) - 3
                    old_trans = translated_sequence
                    print(translated_sequence)
                    print(start, stop)                    
                if translated_sequence[-1] == "*":
#                            print(translated_sequence)
#                            print(start, stop)
                    break
            if "*" in translated_sequence:
                break
               
                
        else:
            break
        
    
    
    if query_start_coor != "1" and query_exon != "Exon1":
        if complement == "0":
            start = int(start) - 3*(int(query_start_coor)-1)
        if complement == "1":
            stop = int(stop) + 3*(int(query_start_coor)-1)
        #        print (query_stop_coor, seq_length)
    if query_stop_coor != str(seq_length) and last_exon != 1:
        if complement == "0":
            stop = int(stop) + 3*(int(seq_length)-int(query_stop_coor))
        if complement == "1":
            start = int(start) - 3*(int(seq_length)-int(query_stop_coor))
    
    print((sequence_extract(Species,scaffold,start,stop,int(complement),1, 1, scaff_area, scaffold_name)) )
    if complement == "0":
        start = int(start) - int(start_modifier)
        stop = int(stop) +  int(stop_modifier)
                   
    if complement == "1":
        start = int(start) - int(stop_modifier)
        stop = int(stop) +  int(start_modifier)
    print(f"Length of query: {query_length}, Query_start = {query_start_coor}, Query_stop = {query_stop_coor}, {query_difference},\nScaffold  = {scaffold},\n scaf_start = {start},\n scaf_end = {stop},\n frame = {frame}, complement = {complement}")
    
    
    

    
    return(start, stop)
    

