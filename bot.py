import tweepy
import config as cfg
import time
import datetime

auth = tweepy.OAuthHandler(cfg.ck, cfg.cs)
auth.set_access_token(cfg.at, cfg.ats)


api = tweepy.API(auth)

with open('wordlist.txt') as f:
    for line in f:
        try:
            api.update_status(f"{line.strip()} is cringe")
            print(f'"{line}" sent successfully at {datetime.datetime.now()}.')
        except Exception as e:
            print("Could not send line '" + line + "'")
            print(str(e))
        time.sleep(60)

print("NGL WE KINDA DONE 🎉😳")
print(f"Finished at {datetime.datetime.now()}.")


