import praw

reddit = praw.Reddit(client_id='AfTzpfgZkekFVA', \
                     client_secret='HuuUOePi2OTn0SbROWsdX6XDbnc', \
                     user_agent='SpecZo', \
                     username='HTN2019_SpecZo', \
                     password='northstar6')

subreddit = reddit.subreddit('SmashBrosUltimate')

subreddit_list = subreddit.new(limit=5)

for submission in subreddit_list:
    print('Title: {}\nLink: {}\nClicked: {}'.format(submission.title, submission.url, submission.clicked))


C:\Users\Ivan Chow\PycharmProjects\HTN2019\redditCrawl.py
C:\Users\Ivan Chow\PycharmProjects\HTN2019\retrieveURL.py