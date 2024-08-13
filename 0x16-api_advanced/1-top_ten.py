#!/usr/bin/python3
"""task 1"""


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux x86_64) Ama45'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()['data']['children']
    for post in data:
        print(post['data']['title'])
