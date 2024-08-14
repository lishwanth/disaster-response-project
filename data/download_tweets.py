import tweepy
import json
from kafka import KafkaProducer

class TwitterStreamer:
    def __init__(self, api_key, api_secret, access_token, access_token_secret, kafka_topic):
        self.kafka_topic = kafka_topic
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.auth = tweepy.OAuthHandler(api_key, api_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def stream_tweets(self, track_keywords):
        stream_listener = self.StreamListener(self.producer, self.kafka_topic)
        stream = tweepy.Stream(auth=self.api.auth, listener=stream_listener)
        stream.filter(track=track_keywords, languages=['en'])

    class StreamListener(tweepy.StreamListener):
        def __init__(self, producer, topic):
            super().__init__()
            self.producer = producer
            self.topic = topic

        def on_status(self, status):
            tweet = {
                'text': status.text,
                'user': status.user.screen_name,
                'created_at': str(status.created_at)
            }
            self.producer.send(self.topic, tweet)

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
    kafka_topic = "disaster_tweets"

    twitter_streamer = TwitterStreamer(api_key, api_secret, access_token, access_token_secret, kafka_topic)
    twitter_streamer.stream_tweets(['earthquake', 'flood', 'hurricane', 'fire'])
