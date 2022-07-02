# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:05:15 2021

@author: sauba
"""

import os
import subprocess

entries = os.listdir("C:/Users/sauba/Desktop/temp")
counter = 0
for names in entries:
    if "Exon12" in names:
        counter += 1
        code = "mv  /mnt/c/Users/sauba/Desktop/temp/"+names+" /mnt/c/Users/sauba/Desktop/temp/"+names.split(".")[0].split("Exon")[0]+"Exon11.fa"
        subprocess.run("wsl "+ code, capture_output=True)
#        print(code)
print (counter)
