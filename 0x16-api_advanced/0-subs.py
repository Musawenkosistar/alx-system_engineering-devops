#!/usr/bin/python3
"""
   use reddit api to print the number of subscribers of a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "ALX Project/1.0"  # Set your own user-agent string here
    }
    params = {
        'raw_json': 1
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        elif response.status_code != 200:
            print(f"Error fetching data: Status code {response.status_code}")
            return 0
        
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
