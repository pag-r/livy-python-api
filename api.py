#!/usr/bin/env python
import requests, os, json
from time import sleep
os.system('clear')
# curl localhost:8998/sessions -X POST --data '{"kind":"spark"}'  -H "Content-Type: application/json"
# curl localhost:8998/sessions
# curl localhost:8998/sessions/0/statements -X POST -H 'Content-Type: application/json' -d '{"code":"print(\"asd\")"}'
# curl localhost:8998/sessions/0/statements/0
host = 'http://localhost:8998'
data = { 'kind' : 'spark' }
headers = {
    'Content-Type' : 'application/json',
    'Accept-Encoding' : '',
    'Content-Encoding' : 'identity'
    }

# creates new session shell
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
session_url = host + r.headers['Location']

# returns all active sessions
r = requests.get(session_url, headers=headers)

# runs a statement in a session
statements_url = session_url + '/statements'
print statements_url
data = { 'code' : '1+1' }
headers = {
    'Content-Type' : 'application/json',
    'Accept-Encoding' : '',
    'Content-Encoding' : 'identity'
}
r = requests.post(statements_url, data=json.dumps(data), headers=headers)
print r.headers
# print statements_url, r.json(), r.status_code, r.headers
# for i in range(20):
#         print "[%d]\t%s" % (i, r.status_code)
#         sleep(i)
# returns specific session in a statement
r = requests.get(host + '/sessions/12/statements/0', headers=headers)
print r.json()
# docker restart `docker ps | grep livy | awk '{print $1}'`;docker logs -f `docker ps | grep livy | awk '{print $1}'`
