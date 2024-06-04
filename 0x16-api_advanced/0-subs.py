#!/usr/bin/python3
"""Return the total number of subscribers on a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns
    the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced"}
    response = requests.get(url=url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
