#!/usr/bin/python3
"""
    Uses reddit API to get 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Print the title of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "ALX Project/1.0 (by /u/Musawenkosistar)"
            }
    params = {
            "limit": 10
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
