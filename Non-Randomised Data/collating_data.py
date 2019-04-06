import os
os.chdir("Desktop/CodeSwitching-in-Twitter/Feminism/Feminism-Collated-Data")

for root, dirs, files in os.walk("Desktop/CodeSwitching-in-Twitter/Feminism/Feminism-Collated-Data"):  
    for filename in files:
        if filename == ".DS_Store":
            continue
        else:
            fname = filename 
            file = open(fname, "r")
            for line in file:
                print line

            print "END OF FILEEEEEEEEEEEEEEEEE "
            