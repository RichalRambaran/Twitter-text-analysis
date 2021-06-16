import json
import credentials as crd
import tweepy as tp


class TwitterClient:
    def __init__(self, twitter_user=None):
        self.auth = crd.authenticate_twitter_app()
        self.twitter_client = tp.API(self.auth)

        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, max_num_tweets):
        tweets = []
        for tweet in tp.Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(max_num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, max_num_friends):
        friend_list = []
        for friend in tp.Cursor(self.twitter_client.friends, id=self.twitter_user).items(max_num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, max_num_tweets):
        home_timeline_tweets = []
        for tweet in tp.Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(max_num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


class TwitterListener(tp.StreamListener):

    def __init__(self, fetched_tweets_filename_param):
        super().__init__()
        self.fetched_tweets_filename = fetched_tweets_filename_param

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, "a") as tf:
                tf.write(data)
            return True
        except BaseException as error_message:
            print(f"Error on_data: {str(error_message)}")
        return True

    def on_error(self, status):
        if status == 420:
            return False
        print(status)


def stream_tweets(fetched_tweets_filename_param, filter_list):
    # streams tweets that contain the filtering words
    listener = TwitterListener(fetched_tweets_filename_param)

    auth = tp.OAuthHandler(crd.api_key, crd.api_key_secret)
    auth.set_access_token(crd.access_token, crd.access_token_secret)

    stream = tp.Stream(auth, listener)
    stream.filter(track=filter_list)


if __name__ == "__main__":
    # streams tweets from specific user
    user = "Space_Station"
    twitter_client = TwitterClient(user)
    user_tweets = twitter_client.get_user_timeline_tweets(5)

    print(user_tweets)
    with open("data/user_tweets.json", "w", encoding="utf8") as file:
        for item in user_tweets:
            json.dump(item._json, file, sort_keys=True, indent=4)

    # streams tweets with specific hashtags
    hashtag_list = ["#Crypto"]
    fetched_tweets_filename = "data/hashtag_tweets.json"
    stream_tweets(fetched_tweets_filename, hashtag_list)
