def fill_collection(dataframe, client):
    # convert to dictionary for uploading to MongoDB
    tweet_dict = dataframe.to_dict('records')
    # point to dbtwitter collection 
    db_ = client.dbtwitter
    # emtpy tweet collection before inserting new records
    # db.tweets.drop()
    # insert new tweets
    db_.tweets.insert_many(tweet_dict)
