fileold = open("Collated_copy.txt", "a")
filenew = open("DalitDaarakshantest.txt")
for line in filenew:
	fileold.write(line)
	
