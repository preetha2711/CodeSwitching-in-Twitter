import tweepy
import csv
import time
import shutil

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

file = open("DalitDaarakshantest.txt", "a")
count = 0 

final_line=""
f = open("D_SearchTermsWork.txt", "r+")
#all_lines = f.readlines()
try : 
	for line in f:
		final_line=line
		print("CHANGING TERMS: \n \n \n \n")
		print(line)
		#f.remove(line)
		for tweet in tweepy.Cursor(api.search,tweet_mode='extended', q=line, rpp=100).items(5000):
			if ("India" in tweet._json["user"]["location"]):   
				if(tweet.full_text.encode('utf-8').startswith("RT @") ==False): #and "RT  @" not in tweet.full_text.encode('utf-8'))
					print tweet.full_text.encode('utf-8')
					file.write(tweet.full_text.encode('utf-8'))
					count += 1  
	print count

except tweepy.TweepError:  
	print "in the except condition"
	old_list = open("D_SearchTermsWork.txt", "r+")
	newfile = open("D_SearchTermsNew.txt", "r+")
	b=0
	for line in old_list:
		if(b==1):
			newfile.write(line)
		if(line==final_line):
			b=1
			print("here")
	shutil.copyfile("D_SearchTermsNew.txt", "D_SearchTermsWork.txt")
	time.sleep(60)