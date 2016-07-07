""" Prints information about the top ten links in /r/news """
import praw
from datetime import datetime


#gets the top scoring links in the news subreddit from the reddit api using praw
p = praw.Reddit(user_agent='DisasterFinder')
submissions = p.get_subreddit('news').get_hot(limit=10)

#prints each post's position on the subreddit, score title, id, and creation value
dt = datetime.now()
print "current date, index, score, title, id, date created"
count = 1
f = open("redditterms.txt", 'r')
f = f.readlines()
f = [x.rstrip('\n') for x in f]
for x in submissions:
    title = x.title.replace('"', '\\\"')
    titleL = title.lower()
    for y in f:
        if y in titleL:
            print "%s, %d, %d, \"%s\", %s, %s" %(
                dt, 
                count, 
                x.score, 
                title, 
                x.id, 
                str(datetime.fromtimestamp(x.created)))
            title = "Nothing to see here"
    count += 1