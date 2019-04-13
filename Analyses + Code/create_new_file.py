f1 = open("fem_tweets_tagged.txt","r")
f2 = open("fem_tweets_fin.txt", "w")

def count_upper_case(string):
    count1=0
    count2=0
    for j in string:
        if(j.isupper()):
                count2=count2+1
    return count2

def count_digits(string):
    count = 0
    for j in string:
        if ((j == '0') or (j == '1') or (j == '2') or (j == '3') or (j == '4') or (j == '5') or (j == '6') or (j == '7') or (j == '8') or (j == '9')):
            count +=1
    return count

# if word=='!'replace w/ [n] & increment n; else append same word to     
# file2
count = 0
for line in f1:
    words = line.split(" ")
    reconstructed_line = ""
    for i in range(len(words)):
        if ((words[i] == "exclamationmark/EN") or (words[i] == "questionmark/EN") or (words[i] == "fullstop/EN")):
            words[i] = 'sentenceender'
        if ((count_upper_case(words[i])>=3) and (count_digits(words[i])==2)):
            print words[i]
            count +=1
            words[i] = ""
            # print line.replace(word, 'sentenceender') + " "
    #     elif ((len(words[i]) == 13) and (('0' in words[i]) or ('1' in words[i]) or ('2' in words[i]) or ('3' in words[i]) or ('4' in words[i]) or ('5' in words[i]) or ('6' in words[i]) or ('7' in words[i]) or ('8' in words[i]) or ('9' in words[i])) and (count_upper_case(words[i])>=3)):
    #         print words[i]
    #         count +=1
    #         words[i] = ""
    #     elif ((len(words[i]) == 11) and (('0' in words[i]) or ('1' in words[i]) or ('2' in words[i]) or ('3' in words[i]) or ('4' in words[i]) or ('5' in words[i]) or ('6' in words[i]) or ('7' in words[i]) or ('8' in words[i]) or ('9' in words[i])) and (count_upper_case(words[i])>=3)):
    #         print words[i]
    #         count +=1
    #         words[i] = ""
        reconstructed_line += words[i] + " "
    f2.write(reconstructed_line + '\n')

f1.close()
f2.close()


# word = "Dfa0VwWJwR/EN"

# if len(word) == 13 and (('0' in word) or ('1' in word) or ('2' in word) or ('3' in word) or ('4' in word) or ('5' in word) or ('6' in word) or ('7' in word) or ('8' in word) or ('9' in word)):
#     print "yes"

print count