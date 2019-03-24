import tweepy
import csv
import time

auth = tweepy.OAuthHandler("muLJUTtbzimAti4sPkzGi1FCi", "ISwLlpWn7hJ3lwvPADMhlseP9DFRCqxVhJGlPXOQxIBDb3aD0c")
auth.set_access_token("1612765604-VHcRtBok33g2phCJ7LqzXfaW5ETWXbDyQ9ZtOsV", "8NtdR1E4BeBteltxR0aJBey5ntq8WBjvpaH1DnuaXyt8D")

# api = tweepy.API(auth)


#file = open("dalit.txt", "w")

# f = open("jaat.txt", "r")
# for line in f:

#     for tweet in tweepy.Cursor(api.search, q=line, rpp=100).items(1000):
#         file.write(tweet.text.encode('utf-8'))
#         print tweet.text.encode('utf-8')


api = tweepy.API(auth, wait_on_rate_limit= True)

file = open("dalit4withoutRT.txt", "w")
count = 0 

f = open("D_SearchTerms.txt", "r")

try : 
	previous=""
	for line in f:
		print(line)
		for tweet in tweepy.Cursor(api.search,tweet_mode='extended', q=line, rpp=100).items(30000):
			if ("India" in tweet._json["user"]["location"]):   
				print tweet.full_text.encode('utf-8')
				if(tweet!=previous):
					file.write(tweet.full_text.encode('utf-8'))
					count += 1  
				previous = tweet
	print count

except tweepy.TweepError:  

    print "in the except condition"
    time.sleep(60 * 15)    

     

