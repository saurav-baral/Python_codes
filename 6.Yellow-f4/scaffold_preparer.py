def scaffold_preparer(Species, scaffold, scaff_area, start_area, end_area, gene):
    import os
    import subprocess
    from Bio import SeqIO
    
    entries = os.listdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species)
    for file_names  in entries:
        if ".nhr" in file_names:
            Genome_name = file_names[:-4]
            break
    output = ''
    fasta_file = open(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/"+Genome_name),'r')
    for record in SeqIO.parse(fasta_file,"fasta"):
        if record.id == scaffold:
            if scaff_area == 1:
                output = ">" + record.id + "\n"+ str(record.seq)[start_area:end_area] + "\n"
            else:
                output = ">" + record.id + "\n"+ str(record.seq) + "\n"
            break
    if "0.for_"+ gene not in entries:
        os.mkdir("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene)
    output_file_name = "C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+scaffold+".fna"
    scaffold_output_file = open(output_file_name,'w')
    scaffold_output_file.write(str(output))
    scaffold_output_file.close()
    fasta_file.close()
    script1 = "makeblastdb -dbtype nucl -in /mnt/c/"+ output_file_name[3:]
    #
    subprocess.run("wsl "+ script1 , capture_output=True)
    return(("C:/Users/sauba/Desktop/Work_Stuff/3.Genomes/data/"+Species+"/0.for_"+gene+"/"+scaffold+".fna"))
