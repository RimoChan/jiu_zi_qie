import random
rd = random.randint

import json
import re
from 配置 import 配置

def 加权抽取(li,wei):
    total_weight=sum(wei)
    p=random.uniform(0,total_weight)
    for i in range(len(li)):
        p-=wei[i]
        if p<0: 
            return li[i]
        
class Data():
    def __init__(self):
        #————————————————————————————
        #读入单词表
        self.單詞表=[]
        with open('data/'+配置['單詞表'],encoding='utf8') as f:
            while 1:
                line=f.readline()
                if line:
                    l=line.split()
                    self.單詞表.append(dict( [(i,l[配置['dict_order'][i]]) for i in 配置['dict_order']] ))
                else:
                    break
        
        
        #————————————————————————————
        #读入例句字典
        with open('data/例句.json',encoding='utf8') as f:
            self.例句字典=json.loads(f.read())
        
        #————————————————————————————
        #打乱单词表
        R=random.Random(配置['隨機種子'])
        for i in self.單詞表:
            i['特徵']=R.random()
        self.單詞表.sort( key=lambda x : x['特徵'] )
        #————————————————————————————
        #读入被切过的单词
        try:
            with open('data/kiri.json',encoding='utf8') as f:
                self.切過的詞=json.loads(f.read())
        except:
            print('存檔沒了……')
            self.切過的詞={}
        #————————————————————————————
        #生成缓冲区
        self.緩衝區=set()
        self.緩衝區尾=0
        self.填滿緩衝區()
        
        #————————————————————————————
        #填充权
        for i in self.單詞表:
            i['权']=1
            

    def 填滿緩衝區(self):
        while len(self.緩衝區)<配置['缓冲区大小'] and self.緩衝區尾<len(self.單詞表):
            if not self.切過了(self.緩衝區尾):
                self.緩衝區.add(self.緩衝區尾)
            self.緩衝區尾+=1

    #切掉上一个单词
    def 前切(self):
        前詞 = self.單詞表[self.之前詞位置]
        self.切過的詞[前詞['假名']+' '+前詞['寫法']]=1
        self.緩衝區.remove(self.之前詞位置)
        self.填滿緩衝區()

    def 切詞存檔(self):
        with open('data/kiri.json','w',encoding='utf8') as f:
            f.write(json.dumps(self.切過的詞,ensure_ascii=False))
       
    def 切詞同步(self):
        import user
        self.切過的詞=user.切詞同步(self.切過的詞)
    
    def 处理例句(self,句):
        if type(句)==str:
            pattern=re.compile(r'^.*?[^<]/')
            a=pattern.findall(句)
            if a:
                a=a[0]
            else:
                return
            b=句[len(a):-1]
            句=['','']
            句[0]=a[0:-1]
            句[1]=b
            
        if type(句)==list:
            return 句[0] + '<br/><span class="例句中文">'+句[1]+'</span>'

    def 生成問題(self):
        組={}
        
        try:
            self.之前詞位置=self.當前詞位置
        except:
            self.之前詞位置=-1
        while True:
            li=list(self.緩衝區)
            self.當前詞位置=加权抽取(li,[self.單詞表[i]['权'] for i in li])    #取buff中的一个下标
            if len(self.緩衝區)==1:  break
            if self.當前詞位置!=self.之前詞位置: break
        self.單詞表[self.當前詞位置]['权']*=配置['確率調整']
        self.單詞表[self.當前詞位置]['权']=min(max(self.單詞表[self.當前詞位置]['权'],配置['確率範圍'][0]),配置['確率範圍'][1])
        
        組['正解'] = self.單詞表[self.當前詞位置]
        
        the_spell = 組['正解']['寫法']
        if the_spell in self.例句字典 and self.例句字典[the_spell]:
            例句=self.处理例句(random.choice(self.例句字典[the_spell]))
        else:
            例句='没抓到2333'
        組['例句']=例句
        
        for i in range(3):
            組[i] = self.單詞表[rd(0,len(self.單詞表)-1)]
        return 組

    def 生成背景詞(self):
        詞列=[]
        s=set()
        for i in range(1,100):
            s.add(rd(0,len(self.單詞表)-1))
        for i in s:
            詞列.append({'字':self.單詞表[i]['寫法'],'top':rd(-100,800),'left':rd(-100,1400),'透明度':rd(5,20)/100,'字號':rd(13,30)})
        return 詞列
    
    def 切過了(self,x):
        return self.單詞表[x]['假名']+' '+self.單詞表[x]['寫法'] in self.切過的詞

data=Data()

if __name__=='__main__':
    data = Data()
    t = data.單詞表
    for i in t:
        del i['特徵']
        del i['权']
    with open('n1.js','w',encoding='utf8') as f:
        f.write(json.dumps(t, ensure_ascii=False))
    
    # data = Data()
    # print(data.單詞表[1])
    # for i in range(160):
    #     q=data.生成問題()
    #     if i%100==99:
    #         print('已经处理%d个。'%i)
    # 
    # import numpy as np
    # 权s=[data.單詞表[i]['权'] for i in list(data.緩衝區)]
    # print('方差=%.3f' % np.array(权s).var())
    # print('没读过数=%d'% sum([i==1 for i in 权s]))
    # 
    # import 圖表
    # 圖表.draw(权s)