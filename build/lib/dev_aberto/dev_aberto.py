import errno
from warnings import catch_warnings
import requests


def hello():
    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    try:
        commit_info = info[0]['commit']['author']
        return commit_info['date'], commit_info['name']
    except:
        print(info)
        return "0000-00-00T00:00:00Z", "-"