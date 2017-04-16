import socket
import sys
sys.path.append('data')
import config

#长度不超过30，因为是utf8所以中文算3倍
name=config.name
password=config.password

address=('localhost',4950)

def check(name,password):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(address)
        s.send(name.encode('utf8').ljust(30,b'\0'))
        s.send(password.encode('utf8').ljust(30,b'\0'))
        r=s.recv(1)
        if r==b'\0':
            return True
        else:
            return False
        s.close()
    except:
        return False

#服务器根本没开23333
# if not check(name,password):
    # name=None
    
if __name__=='__main__':
    if check(name,password):
        print('成')
    else:
        print('败')