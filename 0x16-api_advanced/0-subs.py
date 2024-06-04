#!/usr/bin/python3
"""
Function queries Reddit API and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """Returns the total number of subscribers
    for a given subreddit.
    """
    # Set the Default URL strings
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)

    # Set a custom User-Agent
    user_agent = {'User-Agent': 'Custom User Agent'}

    # Get the Response of the Reddit API
    res = requests.get(api_uri, headers=user_agent,
                       allow_redirects=False)

    # Checks if the subreddit is invalid
    if res.status_code == 404:
        return 0

    # Handle redirects if necessary
    if res.status_code == 302:
        # Redirects are not followed, hence an invalid subreddit
        return 0

    # Returns the total subscribers of the subreddit
    return res.json().get('data', {}).get('subscribers', 0)

