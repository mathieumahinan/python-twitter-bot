from bs4 import BeautifulSoup
import requests
import tweepy
import time

#Twitter API keys/tokens
consumer_key = 'KTwIOegG32OuQuA62AAdbNQDe'
consumer_secret = '4YICrglq7DH9CWm8YYUxIsCpU3esS56vNloImXdmy93zPSuSmH'

key = '1334399834812342272-EYNyxUM6pBQZA4mhCmfApFGTNFoGao'
secret = 'hcrRsCQyNNuc9YRewSm13xYoZcyBmNdPjkjFhzu5FcfKs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


response = requests.get("https://www.basketball-reference.com/players/j/jamesle01/gamelog/2021/")
basketball_reference = response.text

soup = BeautifulSoup(basketball_reference, "html.parser")

# Using soup.find to retrieve data from the basketball reference table. Stats are taken and added to an empty list.
def find_stats():
    table = soup.find(id="pgl_basic.1305")
    data_in_row = table.find_all(name="td", class_="right")
    data_class_left = table.find_all(name="td", class_="left")
    stats = []
    for data in data_in_row:
        stats += data
    pts = stats[-3]
    reb = stats[-9]
    ast = stats[-8]
    stl = stats[-7]
    blk = stats[-6]
    tov = stats[-5]
    minutes = data_in_row[3].getText()
    opponent = data_class_left[2].getText()
    date = data_class_left[0].getText()
  
    api.update_status(f"{date}: Lebron James vs. {opponent}. {pts} PTS, {reb} REB, {ast} AST, {stl} STL, {blk} BLK, {tov} TOV in {minutes} minutes played. #lebron #lakers")
    
# Below is used to favorite key words.
hashtag = "lebron"
lakers = "lakers"
tweetNumber = 20

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)
def searchBot():
    for tweet in tweets:
        try:
            tweet.favorite()
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

find_stats()
searchBot()




