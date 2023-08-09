#!/usr/bin/python3
"""
Function that queries the REDDIT API
returns number of Subscribers for given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns number of subscribers """
    if subreddit is None or type(subreddit) != str:
        return 0

    # set up a customer header to avoid too many requests
    headers = {'User-Agent': '0-subs (Ubuntu; Python:3.8)'}

    # set url then make GET request to the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    # structure: response = requests.get(url, params=None,
    # headers=None, cookies=None, timeout=None)
    response = requests.get(url, headers=headers, allow_redirects=False)

    subs = response.get("data", {}).get("subscribers", 0)
    return subs
