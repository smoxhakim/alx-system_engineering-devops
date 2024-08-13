#!/usr/bin/python3
"""This script"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Method get the number of users subscribed to a subreddit
    """
    try:
        h = {'user-agent': 'Mozilla/5.0', 'allow_redirects': 'false'}
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        req = requests.get(url, headers=h)
        return req.json().get('data').get('subscribers', 0)
    except Exception as e:
        return 0


if __name__ == "__main__":
    pass
