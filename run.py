import twitter
import requests
import random
import time
from thesaurus import Word

from environment import TwitterEnv


def setup_twitter_api():
    api = twitter.Api(consumer_key=TwitterEnv['CONSUMER_KEY'],
                  consumer_secret=TwitterEnv['CONSUMER_SECRET'],
                  access_token_key=TwitterEnv['ACCESS_TOKEN_KEY'],
                  access_token_secret=TwitterEnv['ACCESS_TOKEN_SECRET'])
    return api


def fetch_news():

    print('Fetching latest from FOX News...')
    
    fox_news_api_key = TwitterEnv['FOX_NEWS_API_KEY']
    url = """https://newsapi.org/v2/top-headlines?country=us&apiKey={}""".format(fox_news_api_key)
       
    response = requests.get(url).json()

    return [{'title': item['title'], 'url': item['url']} for item in response['articles']]


def post_tweet(api, obj):
    
    print('Posting...')

    tweet = """ {}, {} """.format(obj['altered_title'], obj['url'])
    api.PostUpdate(tweet)


def run_news_through_filter(news):

    print('Filtering news...')

    filtered = []

    news = [random.choice(news)]

    for item in news:
        headline = item['title'].split()
        
        altered_sentence = []
        
        for word in headline:
            w = Word(word)
            synonym = w.synonyms(relevance=1)
            
            if len(synonym) == 0:
                word_to_use = word
            else:
                word_to_use = random.choice(synonym)
            
            altered_sentence.append(word_to_use)  
         
        altered_headline = ' '.join(word for word in altered_sentence)
        tmp = {'altered_title': altered_headline, 'url': item['url']}
        filtered.append(tmp)

    return filtered[0]

api = setup_twitter_api()

start_time=time.time()
while True:
    print('Starting...')
    time.sleep(60.0 - ((time.time() - start_time) % 60.0))

    news = fetch_news()
    filtered_news = run_news_through_filter(news)
    post_tweet(api, filtered_news)
