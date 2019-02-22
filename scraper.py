import tweepy
import csv
import time

auth = tweepy.OAuthHandler("sc4FMWdhAxw4GFai3PggJXByF", "Yzdo7d6VLUKKaCW5qrrnOU4THKenLQCfnOjpledcSVq70CZASP")
auth.set_access_token("1612765604-8TyUUWbzxNMCdnzvClUl6GGPmfOvRQNrAjjqSq6", "dIVHFRiJSbR1FKpauN6Ij5ZnFtZh5EEg3yszVGpkh0fsU")

api = tweepy.API(auth)

# def main():
#     users = tweepy.Cursor(api.followers, screen_name = "feminism", count = 100).items()
#     try:
#         user = next(users)
#         print user.screen_name
#         print user.name
#     except tweepy.TweepError:
#         print "there is an error"
#         time.sleep(1)
#         next(users)
# main()
file = open("dalit.txt", "w")

f = open("jaat.txt", "r")
for line in f:

    for tweet in tweepy.Cursor(api.search, q="#"+line, rpp=100).items(1000):
        # print tweet.text.encode('utf-8')
        file.write(tweet.text.encode('utf-8'))
    