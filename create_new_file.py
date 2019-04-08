f1 = open("fem_tweets_tagged.txt","r")
f2 = open("fem_tweets_fin.txt", "w")


# if word=='!'replace w/ [n] & increment n; else append same word to     
# file2

for line in f1:
    for word in line:
        if word == "exclamationmark/EN" or word == "questionmark/EN" or word == "fullstop/EN":
            f2.write(line.replace(word, 'sentenceender'))
        else:
            f2.write(word)
f1.close()
f2.close()


