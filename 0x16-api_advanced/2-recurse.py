#!/usr/bin/python3
"""Recursive function"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux x86_64) Bio/34'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list.extend(post['data']['title'] for post in data['children'])
    if data['after'] is None:
        return hot_list

    return recurse(subreddit, hot_list, data['after'])
