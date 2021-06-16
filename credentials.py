import tweepy as tp


api_key = "G00md0vbqktfjaUepz8iflhvW"
api_key_secret = "bD9GroaUoYGOmYWVajE4yDUs5AgXD6fohe4Jiip6epghOhBCb0"
access_token = "1397224977489924109-LPsZvz4V4xdCyn2Fpj7ymCI5lE1hLV"
access_token_secret = "54wo9X3sHR3ss3tKTg34ayEMfgJhCgiQKCzVvYKgRiaML"
bearer_token = "AAAAAAAAAAAAAAAAAAAAACz7QAEAAAAAcMgIlMydYwFABz66yOQ9IgthhEQ%3DB81RXNhwpLZazQZEevQAY7S0PxpEyxjNmWBpkmw7KyeSr2bxXI"


def authenticate_twitter_app():
    # authentication and connection to Twitter's API
    auth = tp.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth
