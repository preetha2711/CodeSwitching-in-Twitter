# file = open("Dalit_Collated_Cleaned.txt", "r")
# f2 = open("Dalit_col_fin.txt", "w")

# for line in file:
# 	line = line.decode("utf-8")
# 	words = line.split(" ")
# 	for word in words:
# 		if(word == " " or word == ""):
# 			continue
# 		count_sent = 0
# 		#word = word.decode('utf-8')
# 		f2.write(word.encode("utf-8").strip())

# 		if word == "sentenceender":
# 			f2.write("\n")
# 			count_sent += 1
# 		else:
# 			f2.write(" ")


# file.close()
# f2.close()

file = open("Dalit_tagged.txt", "r")
f3 = open("final_dal.txt", "w")
count_sent = 0
count_word = 0
tweet = "thisisanewtweet "
for line in file:
	if "##" not in line:
		words = line.split(" ")
		for word in words: 
			f3.write(word + " ")
			count_word +=1
			if ("sentenceender" in word):
				count_sent +=1	
			if count_sent == 3:
				f3.write("\n"+"thisisanewtweet" + "\n")
				count_sent = 0

				
