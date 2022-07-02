def sequence_maker(query_exon, last_exon, Species, scaffold, complement, start, stop, query_start_coor, query_stop_coor, seq_length, start_modifier, stop_modifier,query_length,query_difference,frame, scaff_area, scaffold_name):
    from Bio.Seq import Seq
    from sequence_extraction_called_2 import sequence_extract
    
    error = ''
    old_trans = ''
    
    sequen_length = sequence_extract(Species,scaffold,start,stop,int(complement),1, 0, scaff_area, scaffold_name,1)
    original_start = start
    original_stop = stop
#    if scaff_area == 0:
    if start-10000 > 0:
        start_reducer = 10000
    else:
        start_reducer = start
    if stop + 10000 < sequen_length:
        stop_reducer = 10000
    else:
        stop_reducer = sequen_length-stop
#        if complement == 0:
#        
#            
#        if complement == 1:
#            if start-10000 > 0:
#                start_reducer = 10000
#            else:
#                start_reducer = start
#            if stop + 10000 < sequen_length:
#                stop_reducer = 10000
#            else:
#                stop_reducer = sequen_length-stop
#    else:
#        start_reducer = 0
#        stop_reducer = 0
#        original_start = 0
#        original_stop = 0
    temp_seq = (sequence_extract(Species,scaffold,start-start_reducer,stop+stop_reducer,int(complement),1, 0, scaff_area, scaffold_name)).reverse_complement()
    while True:
        if (query_exon == "Exon1" or last_exon == 1):
#            if int(complement) == 1:
#                current_seq = Seq(str(temp_seq[int(start+start_reducer-original_start):int(stop-stop_reducer-original_stop)]))
#            else:
            current_seq = Seq(str(temp_seq[int(start+start_reducer-original_start):int(stop-stop_reducer-original_stop)]))

            
            
            
            
#            if int(complement) == 0:
#                if scaff_area == 0:
#                    print(int(start+start_reducer-original_start),int(stop-stop_reducer-original_stop))
#                    current_seq = Seq(str(temp_seq[int(start+start_reducer-original_start):int(stop-stop_reducer-original_stop)]))
#                else:
#                    current_seq = (sequence_extract(Species,scaffold,start-start_reducer,stop+stop_reducer,int(complement),1, 0, scaff_area, scaffold_name))
#            if int(complement) == 1:
#                if scaff_area == 0:
#                    print(int(start+start_reducer-original_start),int(start_reducer+(stop-start)))
#                    current_seq = Seq(str(temp_seq[int(start+start_reducer-original_start):int(start_reducer+(stop-start))]))
#                else:
#                    current_seq = (sequence_extract(Species,scaffold,start-start_reducer,stop+stop_reducer,int(complement),1, 0, scaff_area, scaffold_name))
            translated_sequence = current_seq.translate()
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
                    print(start, stop)                    
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
    print((sequence_extract(Species,scaffold,start,stop,int(complement),1, 1, scaff_area, scaffold_name)) )
    
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
    
    
    if complement == "0":
        start = int(start) - int(start_modifier)
        stop = int(stop) +  int(stop_modifier)
                   
    if complement == "1":
        start = int(start) - int(stop_modifier)
        stop = int(stop) +  int(start_modifier)
    print(f"Length of query: {query_length}, Query_start = {query_start_coor}, Query_stop = {query_stop_coor}, {query_difference},\nScaffold  = {scaffold},\n scaf_start = {start},\n scaf_end = {stop},\n frame = {frame}, complement = {complement}")
    
    
    

    
    return(start, stop)
    

