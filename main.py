import requests
import random
import json
import os
def send(push_token,title,text):
    #http://pushplus.hxtrip.com/send?token=XXXXX&title=XXX&content=XXX&template=html
    requests.get('http://pushplus.hxtrip.com/send?token='+push_token+'&title='+title+'&content='+text+'&template=html')
def create_user():
    string = '0123456789abcdefghijklmnopqrstuvwxyz'
    times = random.randint(8,12)
    user = ''
    for i in range(times):
        user += string[random.randint(0,35)]
    return (user)
def signup(user):
    data = {
        "contact": "qq",
        "email": user,
        "emailcode": "1234",
        "name": user,
        "passwd": user,
        "qq": "123456",
        "repasswd": user
    }
    response = requests.post('https://j01.space/signup',data=data )
    return (response.text.encode('utf-8').decode('unicode-escape'))
def get_link(user):
    data = {
        "email":user,
        "passwd":user
    }
    response = requests.post('https://j01.space/signin',data=data )
    headers = {
        'cookie': '__cfduid='+response.cookies['__cfduid']+'; uid='+response.cookies['uid']+'; email='+response.cookies['email']+'; key='+response.cookies['key']+'; ip='+response.cookies['ip']+'; expire_in='+response.cookies['expire_in']+'; PHPSESSID='+response.cookies['PHPSESSID']
    }
    response = requests.get('https://j01.space/xiaoma/get_user', headers=headers)
    return (json.loads(response.text).get('data')['link'])

while True:
    user = create_user()
    if('注册成功' in signup(user)):
        push_token = os.environ.get('PUSH_TOKEN')
        link = get_link(user)+'?sub=1'
        send(push_token,'几鸡订阅地址',link)
        print(link,user)
        break
