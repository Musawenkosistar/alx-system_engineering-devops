#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for fetching subreddit information
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid Too Many Requests error
    headers = {"ALX Project/1.0 by /u/Musawenkosistar"}
    
    # Send GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response is successful (status code 200) and not a redirect
    if response.status_code == 200 and not response.is_redirect:
        # Parse JSON response
        data = response.json()
        # Extract number of subscribers from response
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        # Return 0 if subreddit is invalid or there's an error
        return 0
