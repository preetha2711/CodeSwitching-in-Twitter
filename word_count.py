file = open("fem_tweets_fin.txt","r")

en = 0
hi = 0
hi_dev = 0
content = ''
for line in file:
    if "##" not in line:
        content +=line
        words = line.split(" ")
        line = line.decode("utf-8")
        maxchar = max(line)
        # print words

        for word in words:
            print(word)
            if (("/EN" in word) and ("thisisanewtweet" not in word) and ("fullstop" not in word) and ("questionmark" not in word) and ("exclamationmark" not in word) ):
                en +=1
                print("EN \n \n \n")
            elif "/HI" in word:
                hi +=1
                print("HI \n \n \n")
            elif u'\u0900' <= maxchar <= u'\u097f':
                hi_dev +=1
                print("HIDEV \n \n \n")
            
        
            
         
tweets= content.split("thisisanewtweet/EN")      
sent_hin = 0
sent_eng = 0
for tweet in tweets:
    sentences = tweet.split("sentenceender")
    for sentence in sentences:
        hi_per_sent = 0
        eng_per_sent = 0
        hidev_per_sent = 0
        sentence = sentence.split(" ")
        for word in sentence:
            if word == "" or word == " ":
                pass
            else:
                word = word.decode("utf-8")
                maxchar = max(word)
            
            if "/HI" in word:
                hi_per_sent +=1
            elif "/EN" in word:
                eng_per_sent +=1
            elif u'\u0900' <= maxchar <= u'\u097f':
                    hidev_per_sent +=1

        print(sentence) 
        if(hi_per_sent + hi_per_sent + eng_per_sent != 0):
            if(hi_per_sent + hi_per_sent > eng_per_sent):
                sent_hin +=1
                #print("HI \n \n \n")
            else:
                sent_eng +=1
                #print("EN \n \n \n")


        # if hidev_per_sent == max(hidev_per_sent,hi_per_sent,eng_per_sent):
        #     sent_hin +=1
        #     print("HI \n \n \n")
        # elif hi_per_sent == max(hidev_per_sent,hi_per_sent,eng_per_sent):
        #     sent_hin +=1
        #     print("HI \n \n \n")
        # else:
        #     sent_eng +=1
        #     print("EN \n \n \n")

    

print en
print hi
print hi_dev
print "\n"
print sent_eng
print sent_hin

'''
Results : 
280754
57928
205867

27684
15085
'''

'''
Alternate results with all zero sentences removed:
280754
57928
205867


32254
4352
'''
