#!/usr/bin/python3
"""
Script to query the number of subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers on the subreddit, or 0 if the subreddit is invalid
             or the request fails.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

# Example usage:
# print(number_of_subscribers("programming"))
# print(number_of_subscribers("this_is_a_fake_subreddit"))

