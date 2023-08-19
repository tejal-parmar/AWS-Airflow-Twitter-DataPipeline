import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twiiter_etl():
    access_key = "" 
    access_secret = "" 
    consumer_key = ""
    consumer_secret = ""

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # Creating an API object 
    api = tweepy.API(auth)
  
    screen_names = ['elonmusk','billgates']
    list_tweet_info = []

    for screen_name in screen_names:
        user = api.get_user(screen_name = screen_name)
        tweet_dict = {
            "user_id" : user.id,
            "user_description" : user.description,
            "user_followers_count" : user.followers_count
        }
        list_tweet_info.append(tweet_dict)

    df = pd.DataFrame(list_tweet_info)
    df.to_csv('s3://tz-airflow-bucket/tweets_info.csv')
  
