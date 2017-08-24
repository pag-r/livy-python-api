#!/bin/bash
curl localhost:8998/sessions -X POST --data '{"kind":"spark"}'  -H "Content-Type: application/json"
curl localhost:8998/sessions
curl localhost:8998/sessions/0/statements -X POST -H 'Content-Type: application/json' -d '{"code":"1+1"}'
curl localhost:8998/sessions/0/statements/4
