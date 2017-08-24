#!/usr/bin/env python
import requests
import os
# set spark as kind
url = "http://localhost:8998/sessions"
payload = "{\"kind\":\"spark\"}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text, response.headers, url)
location = response.headers['Location']

# list all sessions
url = "http://localhost:8998/sessions"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
response = requests.request("GET", url, headers=headers)
print(response.text, response.headers, url)

#send statement to process
url = "http://localhost:8998" + location + "/statements"
payload = "{\"code\":\"print(\\\"asd\\\")\"}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

statement_location = None
while True:
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 201:
        print(response.text, response.headers, url)
        statement_location = response.headers['Location']
        os.system('sleep 5')
        break
    else:
        os.system('sleep 0.5')

# get results of a task
if statement_location is not None:
    url = "http://localhost:8998" + statement_location
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
else:
    print 'Error'
