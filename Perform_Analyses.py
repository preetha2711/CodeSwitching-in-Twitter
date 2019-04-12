file = open("final_dal.txt","r")
#file = open("Dalit_tagged.txt","r")

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
              
         
tweets= content.split("thisisanewtweet") 
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
            
            if(hi_per_sent > 1 and eng_per_sent > 1):
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



Results = open("Results_Dalit.txt", "a")
A_different_total = 0
sizeCSFL = len(CS_Fragment_Length)
for i in range (2, sizeCSFL):
    A_different_total += CS_Fragment_Length[i]
print "Just like that:", A_different_total
#Also print these variablea into file.
Results.write("\nTotal words: " + str(word_count))
Results.write("\nEnglish words: "+ str(en))
Results.write("\nHindi words: "+ str(hi))
Results.write("\nHindi Devanagari words: "+ str(hi_dev))
percentage_eng_words = (float(en) / float(word_count))*100
percentage_hin_words = (float(hi) / float(word_count))*100
percentage_hin_dev_words = (float(hi_dev) / float(word_count))*100
Results.write("\nPercentage of English words: "+ str(percentage_eng_words))
Results.write("\nPercentage of Hindi words: "+ str(percentage_hin_words))
Results.write("\nPercentage of Hindi Devanagari words: "+ str(percentage_hin_dev_words))
#Results.write("\n")
Results.write("\nTweet total: "+ str(Tweet_total))
#sentence_total = sent_eng + sent_hin + sent_hin_dev
Results.write("\nSentence total: "+ str(sentence_total))
Results.write("\nsent_eng: "+ str(sent_eng))
Results.write("\nsent_hin: "+ str(sent_hin))
Results.write("\nsent_hin_dev: "+ str(sent_hin_dev))
#Results.write("\nCS_sentences: "+ str(CS_sentences))
print "Just like that:", A_different_total
Results.write("\nCS_sentences: "+ str(A_different_total))
percentage_eng_sentences = (float(sent_eng) / float(sentence_total))*100
Results.write("\npercentage_eng_sentences: "+ str(percentage_eng_sentences))
percentage_hin_sentences = (float(sent_hin) / float(sentence_total))*100
Results.write("\npercentage_hin_sentences: "+ str(percentage_hin_sentences))
percentage_hin_dev_sentences = (float(sent_hin_dev) / float(sentence_total))*100
Results.write("\npercentage_hin_dev_sentences: "+ str(percentage_hin_dev_sentences))
percentage_CS_sentences = (float(A_different_total) / float(sentence_total))*100
Results.write("\npercentage_CS_sentences: "+ str(percentage_CS_sentences))
Results.write("\nCS_tweets: "+ str(CS_tweets))
percentage_CS_tweets = (float(CS_tweets) / float(Tweet_total))*100
Results.write("\npercentage_CS_tweets: "+ str(percentage_CS_tweets))
Results.write("\nCS_Fragment_Length: "+ str(CS_Fragment_Length))
Phrasal_CS = A_different_total - CS_Fragment_Length[2]
Results.write("\nPhrasal_CS: "+ str(Phrasal_CS))
percentage_PCS = (float(Phrasal_CS) / float(A_different_total))*100
Results.write("\npercentage_Phrasal CS: "+ str(percentage_PCS))
Lexical_CS = CS_Fragment_Length[1]
Results.write("\nLexical_CS: "+ str(Lexical_CS))

