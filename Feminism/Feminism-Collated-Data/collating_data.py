import os
f = open("Feminism_Collated.txt", "a")
for filename in os.listdir(os.getcwd()):
    if filename == ".DS_Store":
        continue
    else :
        fname = filename 
        file = open(fname, "r")
        content  = file.read()
        f.write(content)
        f.write("\n" + "!!!!$$$EOT$$$!!!!" + "\n")

        