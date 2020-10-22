import tweepy
import config as cfg
import time

auth = tweepy.OAuthHandler(cfg.ck, cfg.cs)
auth.set_access_token(cfg.at, cfg.ats)


api = tweepy.API(auth)

with open('script.txt') as f:
    for line in f:
        try:
            api.update_status(line)
            print(f"Sent {line} successfully")
        except Exception as e:
            print("Could not send line '" + line + "'")
            print(str(e))
        time.sleep(60)

print("")
print("")
print("")
print("NGL WE KINDA DONE 🎉😳")


