import requests
import re
import json
import argparse


def login_in(user, password):
    headers = { 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':  'en-us,en;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection':  'keep-alive',
        'Content-Type':	'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':	'www.renren.com',
        'Pragma': 'no-cache',
        'Referer': 'http://www.renren.com/SysHome.do',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:11.0) Gecko/20100101 Firefox/11.0'
        }
    payload = {'email': user, 'password': password}

    login_url = 'http://www.renren.com/ajaxLogin/login'
    r = requests.post(login_url, data=payload, headers=headers)
    return r.cookies

def get_friends(user, password):
    cookies = login_in(user, password)
    friends_url = 'http://friend.renren.com/myfriendlistx.do#item_0'
    res = requests.get(friends_url, cookies=cookies)
    #print res.status_code, res.text
    m = re.search(r'var friends=(.*);', res.text)
    friends_list = m.group(1)    

    friends = json.loads(friends_list)
    print "total friends: %s" % len(friends)
    with open('friends.json', 'w') as outfile:
        json.dump(friends, outfile)

    with open('friends.csv', 'w') as f:
        for friend in friends:
            f.write(str(friend['id']))
            f.write(', ')
            f.write(friend['name'].encode('utf-8'))
            f.write(', ')
            f.write(friend['head'])
            f.write('\n')

parser = argparse.ArgumentParser(description='Friends collections command line tool for Renren')
parser.add_argument("user", help="your Renren username")
parser.add_argument("password", help="your Renren password")
args = parser.parse_args()

user = args.user
password = args.password    
get_friends(user, password)
delete this gist
Comments are parsed with GitHub Flavored Markdown
