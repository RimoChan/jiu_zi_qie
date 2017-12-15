import requests
import sys
import json

from 配置 import 配置
from 數據 import data

#———————————————————————————————
username=配置['用戶名']

s = requests.Session()

auth={'username':username,'password':233}

def check(username,password):
    try:
        res=s.post(配置['服務器地址']+'/signin',data=auth,timeout=2)
        if res.text=='good':
            return True
        else:
            print('认证失败了')
    except:
        print('与服务器的连接出现问题')

def 切詞同步(kiri):
    try:
        res=s.post(配置['服務器地址']+'/kiri_sync',data={'username':username,'json':json.dumps(data.kiri,ensure_ascii=False)},timeout=2)
        return json.loads(res.text)
    except:
        return kiri


if 配置['在線的']:
    if check(username,password):
        data.切詞同步()
    else:
        print('并没有成功登录')
        username=None
else:
    print('在线模式被关闭因此不会和服务器通信。')
    username=None
    



if __name__=='__main__':
    pass