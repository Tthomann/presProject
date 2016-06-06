import re
import pandas as pd
import matplotlib.pyplot as plt
import json

twit_path = "c:\\users\Tyler\desktop\presProject\president\twit_bot.json"
twit_data = []

all_tweets = open(twit_path,'r')
class graph_data():

    def grab_data(self):
        for line in all_tweets:
            try:
                tweet = json.loads(line)
                twit_data.append(tweet)
            except:
                continue

    def plot_data(self):

        tweets = pd.DataFrame()
        tweets["trump"] = map(lambda tweet:tweet["trump"].twit_data)
        tweets["hillary"] = map(lambda tweet:tweet["hillary"].twit_data)
        tweets["bernie"] = map(lambda tweet:tweet["bernie"].twit_data)

        tweets_by_trump = tweets["trump"].value_counts()

    fig.ax = plt.subplots()
    ax.tick_params(axis = 'x',labelsize=15)
    ax.tick_params(axis = 'y',labelsize=10)
    ax.set_xlabel("Trump",fontsize=15)
    ax.set_ylabel("Number of Tweets",fontsize=15)
    ax.set_title("Presidential Statistics")
    tweets_by_trump[:5].plot(ax=ax,kind="bar",color="green")
    plt.show()

if __name__ == '__main__':
    graph_data()