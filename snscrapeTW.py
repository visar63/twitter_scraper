## credits: https://www.youtube.com/watch?v=jtIMnmbnOFo&ab_channel=AISpectrum
## pip install snscrape
import pandas as pd

import twitter

# query = "python"
userlist = [
    'twigcard',
    'gericupi',
    # note: userID
]
for tw_user in userlist:
    query = f"(from:{tw_user}) until:2023-01-01 since:2010-01-01"
    limit = 100
    tweets = []

    for tweet in twitter.TwitterSearchScraper(query).get_items():
        # print(vars(tweet))
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content])

    df = pd.DataFrame(tweets, columns=["Date", "UserName", "Tweets"])
    print (df)
    df.to_csv(f'Tweets-{tw_user}.csv', index=False, encoding='utf-8')

# twitter.TwitterSearchScraper()
