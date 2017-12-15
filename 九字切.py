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

from 數據 import data
import user, 圖表

from 配置 import 配置

#————————————————————————————
#接受gui回传的信息
class CallHandler(QObject):
    @pyqtSlot(str)
    def rec(self,命令):
        if 命令=='go':
            run_js('set_data(%s);' % json.dumps(data.gen_ques()))
            run_js('更新切数(%d)' % len(data.kiri))
        if 命令=='初始化':
            run_js('''
                test_mode=%d;
                單詞表名="%s";
                背景=%s;
                准备();
                ''' 
                % 
                (配置['測試模式'],配置['單詞表'],json.dumps(data.gen_bg()))
                
                )
        if 命令=='可视化':
            圖表.draw([data.word[i]['权'] for i in list(data.buff)])
        if 命令=='切':
            data.to_kiri()
            run_js('更新切数(%d)' % len(data.kiri))

def run_js(x):
    view.page().runJavaScript(x)
        

class 九字切窗體(QWebEngineView):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('九字切')
        self.setWindowIcon(QIcon('資源/九字切.ico'))
        self.p=self.page()
        self.p.setWebChannel(channel)
        self.load(QUrl('file:///html/index.html'))
        self.resize(1366,768)
        self.show()
        # self.showFullScreen()
        t = threading.Thread(target=self.修正縮放)
        t.setDaemon(True)
        t.start()
        t2 = threading.Thread(target=self.定時存檔)
        t2.setDaemon(True)
        t2.start()
        
    def 修正縮放(self):
        while True:
            self.p.setZoomFactor(self.width()/1366)
            time.sleep(0.15)
            
    def 定時存檔(self):
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
    
    view = 九字切窗體()
    
    app.exec_()
    
    data.kiri_save()
    data.kiri_sync()