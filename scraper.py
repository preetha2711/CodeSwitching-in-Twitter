import tweepy
import csv
import time

auth = tweepy.OAuthHandler("OjNUlb0H895evrer3ewqdOjZj", "XfBi1g9y7ukRMo2ncUW91BuB0PM14BtfHuFiO7VKWWEbSMTW5E")
auth.set_access_token("1612765604-u0NNqcQHJM2thk0OBQd2dojTZiaOj8mv4x6YUs0", "Gg1KkEi6iP4yUtt7DIqN2F0YPfzQ8mV1TE6JzADzVejCN")

# api = tweepy.API(auth)


#file = open("dalit.txt", "w")

# f = open("jaat.txt", "r")
# for line in f:

#     for tweet in tweepy.Cursor(api.search, q=line, rpp=100).items(1000):
#         file.write(tweet.text.encode('utf-8'))
#         print tweet.text.encode('utf-8')


api = tweepy.API(auth, wait_on_rate_limit= True)

file = open("Feminism_File_6.txt", "a")
count = 0 

f = open("F_SearchTermsWork.txt", "r+")
f_write = open("F_SearchTermsCovered.txt", "a")

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
	


     

