# Reddit/Twitter Capture Tools

These are a series of python scripts that aid with various functions involving event detection on both Twitter and Reddit, as well as capture on Reddit.

## DisasterFinder.py

Checks to see if the top 10 trending Hashtags on twitter match the disaster terms in twitterterms.txt. Prints any that match to console.

### API Key

This program requires you to store your private twitter API information in a separate file called `keys.json` (placed in the TwitterDisasterFinder directory) in the following format:
```
{"api_key":  "*********************",
"api_secret": "*************************************************",
"token_key": "***************************************************",
"token_secret": "***************************************"}
```

## RedditDisasterFinder.py

Looks for trending reddit posts whose titles match the disaster terms in redditterms.txt in the subreddit of your choice, and prints the post's information to console.

To select a subreddit, change `news` on this line to the subreddit of your choice:
```
submissions = p.get_subreddit('news').get_hot(limit=10)
```
You can also change the number of posts checked by altering the `limit=10` value.

## RedditCollector3.py

Prints flattened json data for every comment in a given submission
select the submission by altering the submission ID on this line
```
submission = r.get_submission(submission_id='4riq0c')
```
A submission's ID can be found in the URL when you visit its comment section. RedditDisasterFinder also returns thread IDs when it spots a relevant thread.
