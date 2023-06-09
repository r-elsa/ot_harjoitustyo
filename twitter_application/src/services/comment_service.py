import uuid
import time
from entities.comment import Comment
from db_connection import get_db_connection


def get_comment_by_row(row):
    return (Comment(row[0], row[1], row[2], row[3], row[4]), row[5]) if row else None


class CommentService:
    """Class, which adds and returns comments.
    """

    def __init__(self, connection):
        """ The constructor of the class, which creates a new instance of CommentService.
        """
        self.connection = connection

    def comment(self, tweet_id, user_id, message):
        """ Function to add a comment.

        Args:
            tweet_id (string): Id of the tweet to which the comment belongs.
            user_id (string): Id of the user to which the comment belongs.
            message(string): The content of the comment
        """

        new_comment = Comment(str(uuid.uuid4()), user_id,
                              tweet_id, time.time(), message)

        cursor = self.connection.cursor()
        cursor.execute(
            "insert into comment (comment_id, user_id, tweet_id, send_time,"\
            "message) values (?, ?, ?, ?, ?)",
            (new_comment.comment_id, new_comment.user_id, new_comment.tweet_id,
             new_comment.send_time, new_comment.message,)
        )

        self.connection.commit()

    def return_comments_for_tweet(self, tweet_id):
        """ Function to return all comments.

        Returns:
            array: of comment-objects as well as username
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "select comment.comment_id, comment.user_id, comment.tweet_id, comment.send_time,"\
            "comment.message, user.username from comment LEFT JOIN user WHERE" \
            " user.user_id = comment.user_id and comment.tweet_id = ? ORDER BY send_time LIMIT 10",
            (tweet_id,)
        )
        rows = cursor.fetchall()
        return list(map(get_comment_by_row, rows))


comment_service = CommentService(get_db_connection())
