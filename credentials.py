import tweepy as tp


api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""


def authenticate_twitter_app():
    # authentication and connection to Twitter's API
    auth = tp.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth
