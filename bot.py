import tweepy
import config as cfg
import time

auth = tweepy.OAuthHandler(cfg.ck, cfg.cs)
auth.set_access_token(cfg.at, cfg.ats)


api = tweepy.API(auth)

with open('script.txt') as f:
   for line in f:
       api.update_status(line)
       time.sleep(60)


