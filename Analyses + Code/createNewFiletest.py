import shutil
f = open("D_SearchTermsWork.txt", "r+")
#final_line = "\n"
newf = open("D_SearchTermsNew.txt", "r+")
b=1
for line in f:
	#print(line)
	if(b==1):
		newf.write(line)
	# if(line==final_line):
	# 	b=1
	# 	print("here")

shutil.copyfile("D_SearchTermsNew.txt", "D_SearchTermsWork.txt")

