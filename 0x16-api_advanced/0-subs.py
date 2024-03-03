#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribera(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = { 'User-Agent': 'ALX Project/1.0' }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get('data')
    return results.get('subscribers')
    
