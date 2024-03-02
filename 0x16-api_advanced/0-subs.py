#!/usr/bin/python3
"""
    this module contains the function number_of_subscribers
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
        returns the number of subscribers for a given subreddit
    """
    user = {'User-Agent': 'ALX Project'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0
