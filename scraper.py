import tweepy
import csv
import time

auth = tweepy.OAuthHandler("cXv12CchrguyxKpfFA6uBr8z0", "hWX26AU8hVwNAWcQYmrPQ7xGzW99VYoPm0g7vic2VyVV31kOhO")
auth.set_access_token("1612765604-VHcRtBok33g2phCJ7LqzXfaW5ETWXbDyQ9ZtOsV", "8NtdR1E4BeBteltxR0aJBey5ntq8WBjvpaH1DnuaXyt8D")

api = tweepy.API(auth)

file = open("dalit.txt", "w")

file = open("dalit.txt", "w")

f = open("jaat.txt", "r")
for line in f:

    for tweet in tweepy.Cursor(api.search, q="#"+line, rpp=100).items(1000):
        # print tweet.text.encode('utf-8')
        # if (tweet.location == "India"):
        if ("India" in tweet._json["user"]["location"]):    
            file.write(tweet.text.encode('utf-8'))
    