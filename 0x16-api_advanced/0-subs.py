#!/usr/bin/python3
"""
   use reddit api to print the number of subscribers of a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
       get the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json"
    headers = {"ALX Projecr/1.0: by /u/Musawenkosistar"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
       return 0

    data = response.json().get("data")
    numb_subs = data.get("subscribers")

    return num_subs
