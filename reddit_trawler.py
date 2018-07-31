import praw


def reddit(sub, term):
    file = open("../tokens/reddit_trawler.txt").read()
    codes = []
    for x in file.splitlines():
        codes.append(x)

    reddit = praw.Reddit(client_id=codes[0],
                         client_secret=codes[1],
                         user_agent='reddit trawler for discord',
                         username=codes[2],
                         password=codes[3])

    subreddit = reddit.subreddit(sub)

    if term == "top":
        top_subreddit = subreddit.top()
    else:
        top_subreddit = subreddit.search(term, limit=5)

    topics_dict = {"title": [],
                   "body": []}

    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["body"].append(submission.selftext)

    title = topics_dict["title"][0]
    body = topics_dict["body"][0].splitlines()
    text = "***" + title + "*** \n "
    for lines in body:
        text = text + lines + " \n "

    return(text)
