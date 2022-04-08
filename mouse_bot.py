import tweepy
import time

Consumer_API = 'oCNFimhMBH5F5mqE9mKd9weiY'
Consumer_Secret = 'OU8LQWc7prmLnWfla2sDRfGwWUd4Iv8J6HvcqsXX5mrUZsXYch'
Access_Token = '1412445599056683008-BLDSCNJlZ3Bv9e9m1TzNeE6KqqNrHg'
Access_Secret = '2QJ1K3kAhs1MyaQCzXklhMyb7HHUDGRVmkXV9Z7E8HMYi'

auth = tweepy.OAuthHandler(Consumer_API, Consumer_Secret)
auth.set_access_token(Access_Token, Access_Secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

search_term = "nft"

#Method to retweet found tweets that ignores exceptions (account has already retweeted found tweet)
def Retweet(id):
    try:
        api.retweet(id)
        print("Tweet was retweeted")
    except Exception:
        pass

#Method to "create a friendship" aka follow the person, exception ignored for if we already follow the user
def Follow(scrn_name):
    try:
        print(scrn_name)
        api.create_friendship(screen_name = scrn_name)
        print("User # {0} was followed".format(scrn_name))
    except Exception:
        pass

#Method to fav found tweets that ignores the same exception
def Favorite(id):
    try:
        api.create_favorite(id)
        print("Tweet was favorited")
    except Exception:
        pass


def find_tweets():

    tweets = api.search_tweets(search_term)
    for tweet in tweets:
        curr_text = tweet.text
        if curr_text[0:2] == "RT":
            #print("INVALID BC RETWEET")
            continue
        if curr_text[0] == '@':
            #print("INVALID BC REPLY")
            continue
        else:
            if search_term in tweet.text.lower():
                id = tweet.id
                author = tweet.author
                scrn_name = author.screen_name
                Follow(scrn_name)
                Favorite(id)


                             
def find_tweets_w_cursor():
    print("using cursor")
    tweets = tweepy.Cursor(api.search, q=search_term, count = 1).items()
    print("tweets collected")
    print(tweets)
    for tweet in tweets:
        print(tweet)
        curr_text = tweet.text
        if curr_text[0:2] == "RT":
            #print("INVALID BC RETWEET")
            continue
        if curr_text[0] == '@':
            #print("INVALID BC REPLY")
            continue
        else:
            if search_term in tweet.text.lower():
                id = tweet.id
                author = tweet.author
                scrn_name = author.screen_name
                #Follow(scrn_name)
                Favorite(id)


print("running the program...")

                
while True:
    #print("Running...")
    #find_tweets()
    find_tweets_w_cursor()      #bro this worked I swear it just took a minute
    time.sleep(1)
    
