import praw
import json
threadid = raw_input("Enter ID of thread to collect comments from: ")

#DO NOT SET THIS TO ANYTHING UNDER 10
total = 10
threadname = ""

p = praw.Reddit(user_agent='DisasterFinder')
p.config.store_json_result = True
comments = praw.helpers.comment_stream(p, 'news', total)
f = open("jsonoutput.txt", 'w')
for x in comments:
    if threadid == x.link_id:
        f.write(json.dumps(x.json_dict) + '\n')