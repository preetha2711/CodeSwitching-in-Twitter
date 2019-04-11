f1 = open("Dalit_col_fin.txt", "r")
f2 = open("Dalit_No_Repeat.txt", "r")

linecount1 = 0
for line in f1:

	linecount1 += 1
linecount2 = 0
for line in f2:
	linecount2 += 1
print linecount1
print linecount2
sent_count = 0
for line in f2:
	line = line.decode("utf-8")
	words = line.split(" ")
	for word in words:
		if(word == "sentenceender"):
			sent_count += 1

print sent_count