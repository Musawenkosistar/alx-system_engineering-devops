#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
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

subreddit = "python"
print(f"Number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")
