## credits: https://www.youtube.com/watch?v=jtIMnmbnOFo&ab_channel=AISpectrum for snscrape library
## credits: https://realpython.com/introduction-to-mongodb-and-python/ for pymongo
## pip install snscrape
import pandas as pd

import collectionTW
import twitter  # ## taken from snscape.twitter
from databaseConnection import client

userlist = [
    'twigcard',
    'gericupi',
    'elonmusk'
    # note: userID
]
for tw_user in userlist:
    query = f"(from:{tw_user}) until:2023-01-01 since:2010-01-01"
    limit = 500
    tweets = []

    for tweet in twitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content])

    df = pd.DataFrame(tweets, columns=["Date", "UserName", "Tweets"])
    print (df)

    collectionTW.fill_collection(df, client)

    # # save tweets to csv
    # df.to_csv(f'Tweets-{tw_user}.csv', index=False, encoding='utf-8')
client.close()
