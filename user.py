import requests
import sys
import json
sys.path.append('data')
import config
import data

#———————————————————————————————
username=config.name
password=config.password

s = requests.Session()

auth={'username':username,'password':password}

def check(username,password):
    try:
        res=s.post(config.server+'/signin',data=auth,timeout=2)
        if res.text=='good':
            return True
        else:
            print('认证失败了')
    except:
        print('与服务器的连接出现问题')

def kiri_sync():
    res=s.post(config.server+'/kiri_sync',data={'username':username,'json':json.dumps(data.kiri,ensure_ascii=False)},timeout=2)
    data.kiri=json.loads(res.text)


if config.online_mode:
    if check(username,password):
        kiri_sync()
    else:
        print('并没有成功登录')
        username=None
else:
    print('在线模式被关闭因此不会和服务器通信。')
    



if __name__=='__main__':
    pass