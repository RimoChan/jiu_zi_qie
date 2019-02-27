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

class 山彥(QObject):
    @pyqtSlot(str)
    def rec(self,命令):
        if 命令=='go':
            跑js('set_data(%s);' % json.dumps(data.生成問題()))
            跑js('更新切数(%d)' % len(data.切過的詞))
        if 命令=='初始化':
            跑js('''
                test_mode=%d;
                單詞表名="%s";
                背景=%s;
                准备();
                ''' 
                % 
                (配置['測試模式'],配置['單詞表'],json.dumps(data.生成背景詞()))
                
                )
        if 命令=='可视化':
            圖表.draw([data.單詞表[i]['权'] for i in list(data.緩衝區)])
        if 命令=='切':
            data.前切()
            跑js('更新切数(%d)' % len(data.切過的詞))

def 跑js(x):
    主窗體.page().runJavaScript(x)
        

class 九字切窗體(QWebEngineView):

    def __init__(self):
        super().__init__()
        self.initUI()
        t2 = threading.Thread(target=self.定時存檔)
        t2.setDaemon(True)
        t2.start()

    def initUI(self):
        self.setWindowTitle('九字切')
        self.setWindowIcon(QIcon('資源/九字切.ico'))
        self.頁面=self.page()
        self.頁面.setWebChannel(channel)
        self.load(QUrl('file:///html/index.html'))
        self.全屏=False
        self.resize(1366,768)
        self.show()
            

    def 切換全屏(self):
        self.全屏=not self.全屏
        if self.全屏:
            self.showFullScreen()
        else:
            self.showNormal()

    def 準備快速鍵(self):
        #我也不知道為什麼enter就是綁定不了2333
        QShortcut(QKeySequence('alt+\\'), self).activated.connect(lambda:self.切換全屏())
        
    def resizeEvent(self,ev):
        self.頁面.setZoomFactor(min(self.width()/1366,self.height()/768))
            
    def 定時存檔(self):
        while True:
            data.切詞存檔()
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
    handler = 山彥()
    channel.registerObject('handler', handler)
    
    主窗體 = 九字切窗體()
    
    app.exec_()
    
    data.切詞存檔()
    data.切詞同步()