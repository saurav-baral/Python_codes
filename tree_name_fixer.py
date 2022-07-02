# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 02:00:52 2022

@author: sauba
"""
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/8.Nexus/3.Yellow_c/Yellow_c/infile.nex.con.tre",'r') as tree_file:
    tree_file_list = tree_file.readlines()

with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/6.Phylip/Yellow_c_aligned_untranslated_header_info.txt",'r') as header_info_file:
    header_info_file_list = header_info_file.readlines()
new_line = "aa"
tree_file_output = ''
for lines in tree_file_list:
    for headers in header_info_file_list:
        fasta_original, fasta_rand_head  = headers.split("\t")
        i = 0
        while i < len(lines):
            # print(lines[i:i+5])
            # print(fasta)
            if lines[i:i+5] in fasta_rand_head.rstrip():
                new_line = lines[:i]+fasta_original.rstrip()+lines[i+5:]
                # print(f"new_line = {new_line}")
                lines = new_line
                # print(lines, new_line)
                # input("wait1")
                # print(lines[i:i+5], fasta_rand_head)
                # print(lines)
                # input("wait")
            i = i+1
    # print(lines, new_line)
    # input("wait2")
    tree_file_output = tree_file_output + lines
        
    #     # print(fasta_original,fasta_rand_head)
    #     # if fasta_rand_head in lines:
    #         # print(lines, fasta_rand_head, lines.replace(fasta_rand_head,fasta_original))
    #         # assert False
    #     if fasta_rand_head in lines:
    #         new_line = lines.replace(fasta_rand_head,(fasta_original+"\n"))
    #     # new_line = lines.replace("ZdvBm","aa")
    #     # print(lines, new_line)
    # if new_line != "aa":    
    #     print(lines, new_line)
    #     # input("wait")
    #     tree_file_output = tree_file_output + new_line
    #     new_line = "aa"
    # else:
    #     print(lines, new_line)
    #     # input("wait")
    #     tree_file_output = tree_file_output + lines
    # print(f"tree:\n\n{tree_file_output}\n")
        
with open("C:/Users/sauba/Desktop/Work_Stuff/MRJP/Genes/8.Nexus/3.Yellow_c/Yellow_c.tre",'w') as tree_file_out:
    tree_file_out.write(tree_file_output)