from tkinter import Tk, ttk, W
from tkinter import *
from datetime import datetime


def show_comment_view(self, tweet_id, user_id):
    """ Viewing comments

    Args:
        tweet_id (string): id of tweet, to which comment belongs
        user_id (string): user id of comment writer
    """    
    self.hide_current_grid()
    tweet = self.tweet_service.get_tweet_message(tweet_id)
    heading = ttk.Label(master=self._root, text=f"Comments for tweet: {tweet}",
                        foreground="white",  background="black")
    heading.grid(row=2, column=1, columnspan=10, rowspan=10, sticky=W)

    self.display_comments(tweet_id, user_id)
    self.comment = ttk.Entry(master=self._root)
    self.comment.grid(row=500, column=1)

    self.comment_error_variable = StringVar()

    self.comment_error_label = ttk.Label(
        master=self._root,
        textvariable=self.comment_error_variable,
        foreground="red"
    )

    self.comment_error_label.grid(row=501, column=1)

    post_comment_button = ttk.Button(master=self._root, text="Post comment",
                                     command=lambda t=tweet_id: self.comment_button_clicked(t, user_id))
    post_comment_button.grid(row=500, column=2)

    return_button = ttk.Button(
        master=self._root, text="Back to tweet wall", command=self.show_dashboard)
    return_button.grid(row=5, column=10)


def display_comments(self, tweet_id, user_id):
    """ function for displaying comments

    Args:
        tweet_id (string): id of tweet, to which comment belongs
        user_id (string): user id of comment writer
    """    

    comments = self.comment_service.return_comments_for_tweet(tweet_id)
    if not comments:
            nocomments_message =  StringVar()
            nocomments_message.set("No comment yet.")
            nocomments_message_label = Label(master=self._root, textvariable=nocomments_message)
            nocomments_message_label.grid(row=5, column=4)

    for i in range(0, len(comments)):

        user = StringVar()
        user.set(f"@{comments[i][1]}")

        message = StringVar()
        message.set(comments[i][0].message)

        send_time = StringVar()
        send_time.set(datetime.fromtimestamp(comments[i][0].send_time))
     

        user_label = Label(master=self._root, textvariable=user)
        user_label.grid(row=i*2+100, column=0)
        
        send_time_label = Label(master=self._root, textvariable=send_time)
        send_time_label.grid(row=i*2+100, column=1)

        message_label = Label(master=self._root, textvariable=message)
        message_label.grid(row=i*2+100, column=2)

       
