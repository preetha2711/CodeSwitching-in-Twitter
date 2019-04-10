# import nltk
# nltk.download('words')
from nltk.corpus import words
f4 = open("hidev_detected.txt", "w")
count = 0
file = open("hidev_words.txt", "r")

for word in file:
    word = word.strip()
    # print word.decode("utf-8") 
    try:
        word.decode('ascii')
    except UnicodeDecodeError:
        # print "it was not a ascii-encoded unicode string"
        print word
        f4.write(word + "\n")
        count +=1
    else:
        pass
        # print "It may have been an ascii-encoded unicode string"
    # if word.decode("utf-8") in words.words() == True:
    #     count += 0 
    # else :
    #     count += 1
print count