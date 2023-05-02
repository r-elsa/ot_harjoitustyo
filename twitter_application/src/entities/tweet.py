import uuid


class Tweet:
    """_summary_

    Args:
        comment_id (_type_, optional): _description_. Defaults to None.
        user (_type_, optional): _description_. Defaults to None.
        tweet_id (_type_, optional): _description_. Defaults to None.
        send_time (_type_, optional): _description_. Defaults to None.
        message (_type_, optional): _description_. Defaults to None.
    """  
    def __init__(self, tweet_id=None, user=None, send_time=None,  \
        message=None, picture_url=None):
        """_summary_

        Args:
            comment_id (_type_, optional): _description_. Defaults to None.
            user (_type_, optional): _description_. Defaults to None.
            tweet_id (_type_, optional): _description_. Defaults to None.
            send_time (_type_, optional): _description_. Defaults to None.
            message (_type_, optional): _description_. Defaults to None.
        """  
        self.id = tweet_id or str(uuid.uuid4())
        self.user = user
        self.send_time = send_time
        self.message = message
        self.picture_url = picture_url
    
