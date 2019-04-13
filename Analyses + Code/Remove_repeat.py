
f1 = open("Dalit_col_fin.txt", "r")
f2 = open("Dalit_No_Repeat.txt", "w")
sentence = ""
sentences = []
sent_len = 0
for line in f1:
	
	line = line.decode("utf-8")
	words = line.split(" ")
	for word in words:
		if(word == " " or word == ""):
			continue
		word = word.strip()
		sentence = sentence + word.encode("utf-8")
		sent_len += 1
		if(sent_len > 60):
			sentence = sentence + " sentenceender"

		if(word == "sentenceender" or sent_len > 60):
			sentence = sentence + "\n"
			if(sentence not in sentences):
				sentences.append(sentence)
				f2.write(sentence)
				print sentence
				print "\n"
			sentence = ""	
			sent_len = 0
		else:
			sentence = sentence + " "
