import socket
import threading
import time

def match(name,password):
    if(name=='Rimo')and(password=='daisuki'):
        return 'good'
    else:
        return 'fuck'
        

def server(address):
    address = (address, 4950)

    def tcplink(sock,addr):
        name=sock.recv(30).decode('utf8').rstrip('\0')
        password=sock.recv(30).decode('utf8').rstrip('\0')
        
        statu=match(name,password)
        print(statu)
        if statu=='good':
            sock.send(b'\0')
        else: 
            sock.send(b'\1')
        sock.close()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    s.listen(True)

    while True:
        time.sleep(0.01)
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock,addr))
        t.start()


if __name__ == "__main__":
    server('127.0.0.1')