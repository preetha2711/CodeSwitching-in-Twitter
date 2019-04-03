import random

file = open("Collated.txt", "r")
f = open("Seg_Collated.txt","w")
count = 0
non_RT_arr = []
for line in file: 
    f.write(line)
    if line == "\n":
        f.write("!!!!!!!!!EOT!!!!!!!!!")
    if "RT @" in line:
        f.write("\n"+"!!!!!!!!!EOT!!!!!!!!!!!")
    f.write(line + "\n"+"!!!!!!!!!EOT!!!!!!!!!!!")




    


