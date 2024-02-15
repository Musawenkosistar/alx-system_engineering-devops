#!/usr/bin/python3
"""
Write a Python script that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "ALX Project/1.0 by /u/Musawenkosistar"  
    headers = {'User-Agent': user_agent}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)  
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            print("Error occurred while fetching data from Reddit API.")
            return 0
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0
