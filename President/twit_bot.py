import tweepy
from tweepy import OAuthHandler

consumer_key = 'dydwEBqDcNqh5OEcmVkn00CxK'
consumer_secret = 'Zg9OGrG5GJAbv4PBm9NzTUh2UgSrMpJSeTOiY0uKhnV9Qxyv3a'
access_token = '738080022359990272-luiY3IwKMZuPUfeq1ddp2HI2NontZNp'
access_secret = 'YHE9gvPUEOuuGHDpzaPRkUj13NJ0LEIIZCVugHSueGKuX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def testRun():
    for status in tweepy.Cursor(api.home_timeline).items(10):
        print(status.text)

if __name__ == '__main__':
    testRun()