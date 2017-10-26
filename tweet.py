# importing the module
import tweepy
 
# personal information
consumer_key =""
consumer_secret =""
access_token ="@gmail.com"
access_token_secret =""
 
# authentication
auth = tweepy.OAuthHandler(, )
auth.set_access_token(@gmail.com, )
  
api = tweepy.API(auth)
tweet ="Text part of the tweet"
import os
import time
import tweepy


a=1
b=1

while a<15:
	img="fswebcam -F 3 --fps 25 -r 800x600 " + str(b)+".jpg"
	os.system(img)
	time.sleep(10)
	a=a+1
	b=b+1
 
# to attach the media file
status = api.update_with_media(image_path, tweet) 
api.update_status(status = tweet)
