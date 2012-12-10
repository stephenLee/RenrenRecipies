#!/usr/bin/env python
#-*- coding: utf-8 -*-
from oauth2 import OAuth2

import webbrowser
import requests
import json
import time
import hashlib  #md5

# your client id
client_id = ''
# your client secret
client_secret=''
# base url
BASE_URL = 'http://api.renren.com/restserver.do?'

oauth2_handler = OAuth2(client_id, client_secret, "https://graph.renren.com/", 
		"http://stephenlee.github.com", "oauth/authorize", "oauth/token")

authorization_url = oauth2_handler.authorize_url(response_type='code',scope='read_user_status read_user_blog read_user_album')

#print authorization_url
webbrowser.open(authorization_url)
code = raw_input('please input the code ')
response = oauth2_handler.get_token(code,grant_type='authorization_code')
access_token=response['access_token']
#print response
#print 'access_token is: ',response['access_token']
oauth2_client = requests.session(params={'access_token': response['access_token']})

# get session_key

#SESSION_URL='https://graph.renren.com/renren_api/session_key?oauth_token='
#key_response= requests.get(SESSION_URL+access_token)
# print key_response.headers['content-type'] #json
#text=json.loads(key_response.text)
#session_key=text["renren_token"]["session_key"]

#print 'session_key is: ',session_key

#Detect if a string is unicode and encode as utf-8 if necessary
def unicode_encode(str):
    return isinstance(str,unicode) and str.encode('utf-8') or str

def get_sig(params):
    message =''.join(['%s=%s' % (unicode_encode(k),unicode_encode(v)) for (k,v) in sorted(params.iteritems())])
    m=hashlib.md5(message+client_secret)
    sig=m.hexdigest()
    return sig

def concat_url(params):
    url ='&'.join(['%s=%s' % (unicode_encode(k),unicode_encode(v)) for (k,v) in params.iteritems()])
    return BASE_URL+url

def getUsersInfo(access_token,method='users.getInfo',v='1.0',format='json'):
    # invoke users.getinfo
    call_id=str(int(time.time()*1000))
    # compute sig
    params={
        'access_token': access_token,
        'v':v,
        'method': method,
        'call_id': call_id,
        'format': format
        }
    sig=get_sig(params)
    params.update({'sig':sig})
    url=concat_url(params)
    r=oauth2_client.post(url)
    user_info=json.loads(r.text)[0]
    return r.text

def getFriendsList(access_token,method='friends.getFriends',v='1.0',format='json'):
    call_id=str(int(time.time()*1000))
    # compute sig
    params={
        'access_token': access_token,
        'v':v,
        'method': method,
        'call_id': call_id,
        'format': format
        }
    sig=get_sig(params)
    params.update({'sig':sig})
    url=concat_url(params)
    r=oauth2_client.post(url)
    return r.text

# need scope parameter to control authorization, scope=read_user_status
def getStatus(access_token,method='status.gets',v='1.0',format='json',uid=''):

    call_id=str(int(time.time()*1000))
    # compute sig
    params={
        'access_token': access_token,
        'v':v,
        'method': method,
        'call_id': call_id,
        'format': format,
        'uid': uid
        }
    sig=get_sig(params)
    params.update({'sig':sig})
    url=concat_url(params)
    r=oauth2_client.post(url)
    return r.text

def getProfileInfo(access_token,method='users.getProfileInfo',v='1.0',format='json',uid='',fields='base_info,status,visitors_count,blogs_count,albums_count,friends_count,gustbook_count,status_count'):

    call_id=str(int(time.time()*1000))
    # compute sig
    params={
        'access_token': access_token,
        'v':v,
        'method': method,
        'call_id': call_id,
        'format': format,
        'uid': uid,
        'fields': fields
        }
    sig=get_sig(params)
    params.update({'sig':sig})
    url=concat_url(params)
    r=oauth2_client.post(url)
    return r.text

# search somebody based name
def search(access_token,method='friends.search',v='1.0',format='json',name='',page='',count='20'):

    call_id=str(int(time.time()*1000))
    # compute sig
    params={
        'access_token': access_token,
        'v':v,
        'method': method,
        'call_id': call_id,
        'format': format,
        'name': name,
        'page': page,
        'count': count
        }
    sig=get_sig(params)
    params.update({'sig':sig})
    url=concat_url(params)
    r=oauth2_client.post(url)
    return r.text

# get somebody's blog, need read_user_blog authentication
def getBlogs(access_token,method='blog.gets',v='1.0',
             format='json',uid=''):
    call_id=str(int(time.time()*1000))
    # compute sig
    params={
        'access_token': access_token,
        'v':v,
        'method': method,
        'call_id': call_id,
        'format': format,
        'uid': uid,
        }
    sig=get_sig(params)
    params.update({'sig':sig})
    url=concat_url(params)
    r=oauth2_client.post(url)
    return r.text

# need scope parameter to control authorization, scope=read_user_album
def getAlbums(access_token,method='photos.getAlbums',v='1.0',format='json',uid=''):

    call_id=str(int(time.time()*1000))
    # compute sig
    params={
        'access_token': access_token,
        'v':v,
        'method': method,
        'call_id': call_id,
        'format': format,
        'uid': uid
        }
    sig=get_sig(params)
    params.update({'sig':sig})
    url=concat_url(params)
    r=oauth2_client.post(url)
    return r.text

def main():
	print 'users info is: ',getUsersInfo(access_token)
	print 'friendList is: ',getFriendsList(access_token)
if __name__ == "__main__":
    main()





