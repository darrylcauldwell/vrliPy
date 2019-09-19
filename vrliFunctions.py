import requests
import logging

def _url(path):
    return 'https://192.168.1.206:9543/api/v1' + path

def sessions():
    return requests.post(_url('/sessions'), headers={'Accept':'application/json','Content-Type':'application/json'}, json={"username":"admin","password":"VMware1!VMware1!","provider":"Local"})

def getUsers(bearerToken):
    return requests.get(_url('/users'), headers={'Accept':'application/json','Content-Type':'application/json', 'Authorization':'Bearer ' + bearerToken})
