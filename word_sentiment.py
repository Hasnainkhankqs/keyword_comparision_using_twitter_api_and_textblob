import tweepy
from textblob import TextBlob
import preprocessor
import statistics
from typing import List
# please create secret_code.py file and add your twitter provided api_key and api_secret_key like this in it
# api_key = "asdfadfasdfa"
# api_secret_key = "asdfadfadfadfasdf"
from secret_code import api_key, api_secret_key 


auth = tweepy.AppAuthHandler(api_key , api_secret_key)
api = tweepy.API(auth)

def get_tweets(keyword : str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search , q=keyword , tweet_mode="extended" , lang="en").items(100) :
        all_tweets.append(tweet.full_text)

    return all_tweets

def clean_tweets(all_tweets : List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(preprocessor.clean(tweet))
    return tweets_clean

def get_sentiments(all_tweets : List[str]) -> List[float]:
    sentiment_score = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_score.append(blob.sentiment.polarity)
    return sentiment_score

def generate_avg_sent_score(keyword : str) -> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    sentiment_score = get_sentiments(tweets_clean)

    average_score = statistics.mean(sentiment_score)

    return average_score

if __name__ == "__main__":

    print("What world likes")
    first_input = input()
    print("--or--")
    second_input = input()
    print("\n")

    first_score = generate_avg_sent_score(first_input)
    second_score = generate_avg_sent_score(second_input)

    if(first_score > second_score) :
        print(f"world like {first_input} over {second_input}")
    else:
        print(f"world like {second_input} over {first_input}")

