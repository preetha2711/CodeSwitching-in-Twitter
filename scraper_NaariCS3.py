import tweepy
import csv
import time

auth = tweepy.OAuthHandler("3K2hfNVMWkaRVsMwtSzfHSgLe", "zB9R0q6YFqW1ALoFX5HiypLe0eBnHJC7tHop37NpBDWqyrNrbB")
auth.set_access_token("1612765604-E9AaB0QiQglYmTUkiZnuQ21rCo34FtLV5LXxdcf", "o8QIzfIdNkRs3OTYOSWfQ1eCWdYWDW8EzohfOSLapdxEo")

# api = tweepy.API(auth)


#file = open("dalit.txt", "w")

# f = open("jaat.txt", "r")
# for line in f:

#     for tweet in tweepy.Cursor(api.search, q=line, rpp=100).items(1000):
#         file.write(tweet.text.encode('utf-8'))
#         print tweet.text.encode('utf-8')


api = tweepy.API(auth, wait_on_rate_limit= True)

file = open("Feminism_File_9.txt", "a")
count = 0 

f = open("F_SearchTermsWorkCS3.txt", "r+")
f_write = open("F_SearchTermsCoveredCS3.txt", "a")

try : 
	for line in f:
		print(line)
		f_write.write(line)
		for tweet in tweepy.Cursor(api.search,tweet_mode='extended', q=line, rpp=100).items(30000):
			if ("India" in tweet._json["user"]["location"]):   
				text = tweet.full_text.encode('utf-8')
				if("RT @" not in text):
					print tweet.full_text.encode('utf-8')
					file.write(tweet.full_text.encode('utf-8'))
					file.write("\n" + "!!!!$$$EOT$$$!!!!" +"\n")
					count += 1  
	print count

except tweepy.TweepError:  

    print "in the except condition"
    time.sleep(60)
	


     

