import praw

x = 1 
r = praw.Reddit('sped')
r.login('spedbot', 'stthom83')
input = raw_input('Enter the username of the target: ')
input2 = str(raw_input('Type upvote to mass upvote or type downvote to mass downvote. '))
upvote = 'upvote' or 'Upvote'
downvote = 'downvote' or 'Downvote'

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
       x +=1 

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
       x +=1  
