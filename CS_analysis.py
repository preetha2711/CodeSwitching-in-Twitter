file = open("fem_tweets_fin.txt","r")

en = 0
hi = 0
hi_dev = 0
content = ''
word_count = 0
for line in file:
    if "##" not in line:
        content +=line
        words = line.split(" ")
        print "words", words
        line = line.decode("utf-8")
        maxchar = max(line)
        # print words
        
        for word in words:
            
            # print(word)
            if (("/EN" in word) and ("thisisanewtweet" not in word) and ("fullstop" not in word) and ("questionmark" not in word) and ("exclamationmark" not in word) ):
                en +=1
                word_count +=1
                # print("EN \n \n \n")
            elif "/HI" in word:
                hi +=1
                word_count +=1
                # print("HI \n \n \n")
            elif u'\u0900' <= maxchar <= u'\u097f':
                hi_dev +=1
                word_count +=1
                # print (word)
                # print("HIDEV \n \n \n")
              
         
tweets= content.split("thisisanewtweet/EN") 
Tweet_total = len(tweets)     
sent_hin = 0
sent_eng = 0
sent_hin_dev = 0
CS_tweets = 0
CS_sentences = 0
CS_Fragment_Length = [0]*20
for tweet in tweets:
    print "tweet: ", tweet
    sentences = tweet.split("sentenceender")
    eng_per_tweet = 0
    hi_per_tweet = 0

    for sentence in sentences:
        is_hi_dev = False
        sentence = sentence.decode("utf-8")
        maxchar = max(sentence)
        print sentence
        print "maxchar: ", maxchar
        if(u'\u0900' <= maxchar <= u'\u097f'):
            sent_hin_dev += 1
            
            is_hi_dev = True
            
        else:
            hi_per_sent = 0
            eng_per_sent = 0
            #hidev_per_sent = 0
            sentence = sentence.split(" ")
            # for word in sentence:
            #     if word == "" or word == " ":
            #         pass
            #     else:
            #         word = word.decode("utf-8")
            #         maxchar = max(word)    
            for word in sentence:
                if "/HI" in word:
                    hi_per_sent +=1
                elif "/EN" in word:
                    eng_per_sent +=1
            
            if(hi_per_sent > 0 and eng_per_sent > 0):
                CS_sentences += 1

            eng_per_tweet += eng_per_sent
            hi_per_tweet += hi_per_sent 
            Language = ""
            if(hi_per_sent + eng_per_sent == 0):
                continue
            if(hi_per_sent > eng_per_sent):
                sent_hin +=1
                Language = "/HI"
                Not_Language = "/EN"
            else:
                sent_eng +=1
                Language = "/EN"
                Not_Language = "/HI"
            CS_max_fragment = 0
            n = len(sentence)
            i = 0
            while(i < n):
                CS_fragment = 0
                word = sentence[i]
                # if word == "" or word == " ":
                #     pass
                # else:
                #     word = word.decode("utf-8")
                #     maxchar = max(word)
        
                while(Language not in word and Not_Language in word):
                    CS_fragment += 1
                    i += 1
                    word = sentence[i]
                    print (CS_fragment)
                if(CS_fragment > CS_max_fragment):
                    CS_max_fragment = CS_fragment
                
                i += 1


            CS_Fragment_Length[CS_max_fragment] += 1


    if(eng_per_tweet > 0 and hi_per_tweet > 0):
        CS_tweets += 1



#Also print these variablea into file.
print "Total words: ", word_count
print "English words: ", en
print "Hindi words: ", hi
print "Hindi Devanagari words: ", hi_dev
print "\n"
print "Tweet total", Tweet_total
sentence_total = sent_eng + sent_hin + sent_hin_dev
print "Sentence total: ", sentence_total
print "sent_eng: ", sent_eng
print "sent_hin: ", sent_hin
print "sent_hin_dev", sent_hin_dev
print "CS_sentences: ", CS_sentences
percentage_eng_sentences = float(sent_eng) / float(sentence_total)
percentage_hin_sentences = float(sent_hin) / float(sentence_total)
percentage_hin_dev_sentences = float(sent_hin_dev) / float(sentence_total)
percentage_CS_sentences = float(CS_sentences) / float(sentence_total)
print "CS_tweets: ", CS_tweets
percentage_CS_tweets = float(CS_tweets) / float(Tweet_total)
print "CS_Fragment_Length: ", CS_Fragment_Length
Phrasal_CS = sentence_total - CS_Fragment_Length[0] - CS_Fragment_Length[1] - CS_Fragment_Length[2]
Lexical_CS = CS_Fragment_Length[1]
