import uuid


class Like:
    """_summary_

    Args:
        comment_id (_type_, optional): _description_. Defaults to None.
        user (_type_, optional): _description_. Defaults to None.
        tweet_id (_type_, optional): _description_. Defaults to None.
        send_time (_type_, optional): _description_. Defaults to None.
        message (_type_, optional): _description_. Defaults to None.
    """
    def __init__(self, like_id=None, user_id=None, tweet_id=None, send_time=None):
        """_summary_

        Args:
            comment_id (_type_, optional): _description_. Defaults to None.
            user_id (_type_, optional): _description_. Defaults to None.
            tweet_id (_type_, optional): _description_. Defaults to None.
            send_time (_type_, optional): _description_. Defaults to None.
            message (_type_, optional): _description_. Defaults to None.
        """
        self.id = like_id or str(uuid.uuid4())
        self.user_id = user_id
        self.tweet_id = tweet_id
        self.send_time = send_time
