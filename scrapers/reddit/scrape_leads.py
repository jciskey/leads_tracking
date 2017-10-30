import os
import praw
import datetime

# Grab relevant values from the environment and stuff them into the constructor
reddit_praw_config = {}
reddit_praw_config['client_id'] = os.environ['LEADS_REDDIT_CLIENT_ID']
reddit_praw_config['client_secret'] = os.environ['LEADS_REDDIT_CLIENT_SECRET']
reddit_praw_config['password'] = os.environ['LEADS_REDDIT_PASSWORD']
reddit_praw_config['user_agent'] = os.environ['LEADS_REDDIT_USER_AGENT']
reddit_praw_config['username'] = os.environ['LEADS_REDDIT_USERNAME']

reddit = praw.Reddit(**reddit_praw_config)

def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

job_query_string = '(title:"[hiring]" OR flair:Hiring) AND (subreddit:forhire OR subreddit:jobbit OR subreddit:jobopenings OR subreddit:b2bforhire) AND (software OR app OR webapp OR developer OR programmer OR program OR app)'

sr_all = reddit.subreddit('all')
results = sr_all.search(job_query_string, limit=100, sort='new')

for x in results:
	print x.fullname, x.subreddit, get_date(x), x.title[:25]
