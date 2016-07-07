import praw

r = praw.Reddit('Comment Scraper 1.0 by u/_Daimon_ see '
                'https://praw.readthedocs.org/en/latest/'
                'pages/comment_parsing.html')
f = open("jsonoutput.txt", "w")
submission = r.get_submission(submission_id='4riq0c')
submission.replace_more_comments(limit=None, threshold=0)
flat_comments = praw.helpers.flatten_tree(submission.comments)
count = 0
for x in flat_comments:
    f.write(str(x.__dict__) + '\n')
    count += 1
        
print count