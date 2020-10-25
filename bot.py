import tweepy #import the twitter python package
import config as cfg #import a config.py file with your tokens (YOU MUST MAKE THIS YOURSELF)
import time #import the package that lets us wait a few seconds in the code
import datetime #import the datetime package that lets us get the current time

auth = tweepy.OAuthHandler(cfg.ck, cfg.cs) #try to connect to the twitter api using your consumer key and consumer secret
auth.set_access_token(cfg.at, cfg.ats) #authenticate to twitter using your access key and access token


api = tweepy.API(auth) #use the twitter connection to log into your twitter account

with open('wordlist.txt') as f: #open the wordlist.txt file
    for line in f: #for each line in the file
        try:
            api.update_status(f"{line.strip()} is cringe") #post a tweet to twitter with the word
            print(f'"{line}" sent successfully at {datetime.datetime.now()}.') #print out in console that it was sent
        except Exception as e: #if something failed
            print("Could not send line '" + line + "'") #say what the line is
            print(str(e)) #print the error
        time.sleep(60) #wait 60 seconds

print("NGL WE KINDA DONE 🎉😳")
print(f"Finished at {datetime.datetime.now()}.")


