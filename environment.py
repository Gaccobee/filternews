import os

from dotenv import (load_dotenv, find_dotenv)

load_dotenv(find_dotenv())

variables = {
    'CONSUMER_KEY': os.getenv('CONSUMER_KEY'),
    'CONSUMER_SECRET': os.getenv('CONSUMER_SECRET'),
    'ACCESS_TOKEN_KEY': os.getenv('ACCESS_TOKEN_KEY'),
    'ACCESS_TOKEN_SECRET': os.getenv('ACCESS_TOKEN_SECRET'),
    'FOX_NEWS_API_KEY': os.getenv('FOX_NEWS_API_KEY')
}

TwitterEnv = variables
