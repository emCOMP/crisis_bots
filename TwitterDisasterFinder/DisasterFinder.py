#
#Requires twitterterms.txt and tweepy to work, runs indefinitely
#
import tweepy
import time
import os
import json

#Establish variables for keys taken off twitter dev website
with open("keys.json", "r") as f:
    auth_details = json.loads(f.read())

#Set up OAuth with above keys
auth = tweepy.OAuthHandler(auth_details["api_key"], auth_details["api_secret"])
auth.set_access_token(auth_details["token_key"], auth_details["token_secret"])

#Executes the following every ~5 minutes
while True:
    #Use tweepy to get top 10 trending hashtags for USA
    api = tweepy.API(auth)
    trends_response = api.trends_place(23424977)
    trends = trends_response[0]["trends"]
    
    #Open list of keywords we're interested in
    keywords = open("twitterterms.txt", 'r').readlines()
    
    #Iterate over trending hashtags; printing hashtags that have words from our keyword
    #list in them
    for x in trends:
        name = x["name"]
        if name[0] == "#":
            name = name[1:]
            for y in keywords:
                if y.rstrip() in name.lower():
                    print name
    time.sleep(300)
    

