#!/usr/bin/env python3
#redditvotebot v2.0 by sped

import praw
import os
import threading

reddit = praw.Reddit(
    client_id=os.environ.get("PRAW_CLIENT_ID"),
    client_secret=os.environ.get("PRAW_CLIENT_SECRET"),
    user_agent=os.environ.get("PRAW_USER_AGENT"),
    username=os.environ.get("PRAW_USERNAME"),
    password=os.environ.get("PRAW_PASSWORD")
)

def vote_on_comments(user, vote_type, already_done):
    for comment in user.comments.new(limit=None):
        if comment.id not in already_done:
            if vote_type == 'upvote':
                comment.upvote()
            elif vote_type == 'downvote':
                comment.downvote()
            already_done.add(comment.id)
            print(comment.permalink)

def run_bot():
    username = input('Enter the username of the target: ')
    vote_type = input('Would you like to (U)pvote or (D)ownvote the target? (U|D). ')
    run_continuously = input('Would you like the bot to run continuously? (Y|N) ')
    upvote = {'u', 'U'}
    downvote = {'d', 'D'}
    yes = {'y', 'Y'}

    already_done = set()
    user = reddit.redditor(username)
    while True:
        if vote_type in downvote:
            print('Beginning to downvote. The permalink to the comment will be printed when a comment is downvoted.')
            t = threading.Thread(target=vote_on_comments, args=(user, 'downvote', already_done))
            t.start()
        elif vote_type in upvote:
            print('Beginning to upvote. The permalink to the comment will be printed when a comment is upvoted.')
            t = threading.Thread(target=vote_on_comments, args=(user, 'upvote', already_done))
            t.start()
        else:
            print('Invalid vote type.')
            break

        if run_continuously in yes:
            t.join()
        else:
            break

if __name__ == '__main__':
    run_bot()