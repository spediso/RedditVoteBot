#redditvotebot v1.2 by sped

import praw

x = 1 
r = praw.Reddit('redditvotebot v1.2 by sped')
r.login()
input = raw_input('Enter the username of the target: ')
input2 = str(raw_input('Would you like to (U)pvote or (D)ownvote the target? (U|D). '))
input3 = str(raw_input('Would you like the bot to run continuously? (Y|N) '))
upvote = 'u' or 'U'
downvote = 'd' or 'D'
yes = 'y' or 'Y'
no = 'n' or 'N'

if input2 in downvote:
   print('Begining to downvote.  The permalink to the comment will be printed when a comment is downvoted.')
   already_done = set()

   user = r.get_redditor(input)
   while True:
       for comment in user.get_comments(limit=None):
           if comment.id not in already_done:
              comment.downvote()
              already_done.add(comment.id)
              print(comment.permalink)
       if input3 in yes:
           x +=1
       if input3 in no:
           exit()

if input2 in upvote:
   print('Begining to upvote.  The permalink to the comment will be printed when a comment is upvoted.')
   already_done = set()

   user = r.get_redditor(input)
   while True:
       for comment in user.get_comments(limit=None):
           if comment.id not in already_done:
              comment.upvote()
              already_done.add(comment.id)
              print(comment.permalink)
       if input3 in yes:
           x +=1
       if input3 in no:
           exit()
