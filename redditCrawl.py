import praw

reddit = praw.Reddit(client_id='AfTzpfgZkekFVA', \
                     client_secret='HuuUOePi2OTn0SbROWsdX6XDbnc', \
                     user_agent='SpecZo', \
                     username='HTN2019_SpecZo', \
                     password='northstar6')

def getInstance(site):
    try:
        return reddit.submission(url=site)
    except:
        print("Invalid URL")

def filter_domain(domain):
    return not("self" in domain or "redd" in domain or "imgur" in domain)


#self, redd, i.imgur.com

#subreddit = reddit.subreddit('SmashBrosUltimate')

#subreddit_list = subreddit.new(limit=5)

#for submission in subreddit_list:
#    print('Title: {}\nLink: {}\nClicked: {}'.format(submission.title, submission.url, submission.clicked))

