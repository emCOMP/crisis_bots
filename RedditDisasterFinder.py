""" Prints information about the top ten links in /r/news """
import praw

#gets the top scoring links in the worldnews subreddit from the reddit api using praw
p = praw.Reddit(user_agent='DisasterFinder')
submissions = p.get_subreddit('news').get_hot(limit=10)

#prints each post's position on the subreddit, score title, id, and creation value
print "index, score, title, id, created"
count = 1
for x in submissions:
    print str(count) + ", " + str(x.score) +", " + x.title + ", " + x.id + ", " + str(x.created)
    count += 1