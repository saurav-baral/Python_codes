from Bio.Seq import Seq
Species = "Spodoptera_frugiperda"
exon_names = ["Exon1","Exon2","Exon3","Exon4","Exon5","Exon6","Exon7","Exon8"]
seq_dna =''
trans_seq = ''
frames_list = [[0,1],[2,1],[2,0],[0,2],[1,0],[0,0],[0,0],[0,0]]
for i in range(len(exon_names)):
    exon = exon_names[i]
    frame = frames_list[i][0]+1

    with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/3.Extracted/10.Yellow_Un1/"+Species+"_"+exon+".fa",'r') as f:
        exon_file_content_list = f.readlines()
    sequence = Seq(exon_file_content_list[1].rstrip())
    print(exon_file_content_list[0], sequence, sequence.translate())
    seq_dna = seq_dna + sequence
print("\n\n",Species,"\n\n", seq_dna,"\n\n", seq_dna.translate())