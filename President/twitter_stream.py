import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
consumer_key = 'dydwEBqDcNqh5OEcmVkn00CxK'
consumer_secret = 'Zg9OGrG5GJAbv4PBm9NzTUh2UgSrMpJSeTOiY0uKhnV9Qxyv3a'
access_token = '738080022359990272-luiY3IwKMZuPUfeq1ddp2HI2NontZNp'
access_secret = 'YHE9gvPUEOuuGHDpzaPRkUj13NJ0LEIIZCVugHSueGKuX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])