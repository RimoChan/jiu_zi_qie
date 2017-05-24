from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import QIcon
import time 
import threading
import os
import sys
import json

sys.path.append('data')
from data import data 
import moban, user, config

#————————————————————————————
#接受gui回传的信息
class CallHandler(QObject):
    @pyqtSlot(str)
    def rec(self):
        view.page().runJavaScript(
            '''
            data=%s;
            set_data();
            '''     %
            json.dumps(data.gen_ques()) +
            '''
            all_kiri=%d;
            更新切数()
            '''     %
            len(data.kiri)
        )
        
    @pyqtSlot(str)
    def kiri(self):
        data.to_kiri()
        view.page().runJavaScript(
            '''
            all_kiri=%d;
            更新切数()
            '''
            %
            len(data.kiri)
        )
        
#————————————————————————————
#窗口界面
class my_view(QWebEngineView):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('9Kiri!')
        self.setWindowIcon(QIcon('icon.ico'))
        moban.tp('index.html','final.html',bg=data.gen_bg(),user=user.username,word_dict=config.word_dict)
        self.p=self.page()
        self.p.setWebChannel(channel)
        self.load(QUrl('file:///html/final.html'))
        self.resize(1366,768)
        self.show()
        # self.showFullScreen()
        t = threading.Thread(target=self.size_fix)
        t.setDaemon(True)
        t.start()
        t2 = threading.Thread(target=self.time_save)
        t2.setDaemon(True)
        t2.start()
        
    def size_fix(self):
        while True:
            self.p.setZoomFactor(self.width()/1366)
            time.sleep(0.15)
            
    def time_save(self):
        while True:
            data.kiri_save()
            time.sleep(30)
            
pass
pass
pass
pass
'nya'
pass

if __name__=='__main__':
    app = QApplication([])
    
    channel = QWebChannel()
    handler = CallHandler()
    channel.registerObject('handler', handler)
    
    view = my_view()
    
    app.exec_()
    
    data.kiri_save()
    data.kiri_sync()