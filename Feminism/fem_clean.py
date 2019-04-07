file = open("Feminism_Collated.txt", "r")
f = open("Final_Fem_Collated_Clean.txt", "w")
count =0
for line in file:
    if line == "\n":
        pass
    else:
        f.write(line)


    

    