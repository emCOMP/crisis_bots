import praw
import json

#DO NOT SET THIS TO ANYTHING UNDER 10
total = 10
threadname = ""

p = praw.Reddit(user_agent='DisasterFinder')
comments = praw.helpers.comment_stream(p, 'news', total)
for x in comments:
    print x