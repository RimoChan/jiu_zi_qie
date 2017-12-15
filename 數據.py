import random
rd= random.randint

import sys
import json
import re
from 配置 import 配置

#加权抽取
def weighting_choice(li,wei):
    total_weight=sum(wei)
    p=random.uniform(0,total_weight)
    for i in range(len(li)):
        p-=wei[i]
        if p<0: 
            return li[i]
        
class Data:
    def __init__(self):
        #————————————————————————————
        #读入单词表
        f=open('data/'+配置['單詞表'],encoding='utf8')
        f.read(1)
        self.word=[] #单词表
        while 1:
            line=f.readline()
            if line:
                l=line.split()
                self.word.append(dict( [(i,l[配置['dict_order'][i]]) for i in 配置['dict_order']] ))
            else:
                break
        f.close()
        
        # self.word=self.word[:配置['缓冲区大小']]
        
        #————————————————————————————
        #读入例句字典
        f=open('data/dictionary.json',encoding='utf8')
        self.mon_dict=json.loads(f.read())
        f.close()
        
        #————————————————————————————
        #打乱单词表
        R=random.Random(配置['隨機種子'])
        for i in self.word:
            i['eigen']=R.random()
        self.word.sort( key=lambda x : x['eigen'] )
        #————————————————————————————
        #读入被切过的单词
        try:
            f=open('data/kiri.json',encoding='utf8')
            self.kiri=json.loads(f.read())
            f.close()
        except:
            self.kiri={}
        #————————————————————————————
        #生成缓冲区
        self.buff=set()
        self.now_word=0
        self.buff_full()
        
        #————————————————————————————
        #填充权
        for item in self.word:
            item['权']=1
            

    #————————————————————————————
    #填满缓冲区
    def buff_full(self):
        while len(self.buff)<配置['缓冲区大小'] and self.now_word<len(self.word):
            if not self.kiried(self.now_word):
                self.buff.add(self.now_word)
            self.now_word+=1

    #————————————————————————————
    #切掉上一个单词
    def to_kiri(self):
        the_word = self.word[self.pre_x]
        self.kiri[the_word['word']+' '+the_word['spell']]=1
        self.buff.remove(self.pre_x)
        self.buff_full()

    #————————————————————————————
    #存档被切过的单词
    def kiri_save(self):
        f=open('data/kiri.json','w',encoding='utf8')
        f.write(json.dumps(self.kiri,ensure_ascii=False))
        f.close()

    #————————————————————————————
    #与服务器同步被切过的单词
    def kiri_sync(self):
        import user
        self.kiri=user.kiri_sync(self.kiri)
    
    #处理例句
    def deal_mon(self,mon):
        if type(mon)==str:
            pattern=re.compile(r'^.*?[^<]/')
            a=pattern.findall(mon)
            if a:
                a=a[0]
            else:
                return
            b=mon[len(a):-1]
            mon=['','']
            mon[0]=a[0:-1]
            mon[1]=b
            
        if type(mon)==list:
            return mon[0] + '<br/><span class="例句中文">'+mon[1]+'</span>'

    #————————————————————————————
    #生成一个题目
    def gen_ques(self):
        gen=dict()
        
        
        try:
            self.pre_x=self.x
        except:
            self.pre_x=-1
        while True:
            li=list(self.buff)
            # self.x=random.choice(li)
            self.x=weighting_choice(li,[self.word[i]['权'] for i in li])    #取buff中的一个下标
            if len(self.buff)==1:  break
            if self.x!=self.pre_x: break
        self.word[self.x]['权']*=配置['確率調整']
        self.word[self.x]['权']=min(max(self.word[self.x]['权'],配置['確率範圍'][0]),配置['確率範圍'][1])
        
        gen['senkai'] = self.word[self.x]
        
        the_spell = gen['senkai']['spell']
        if the_spell in self.mon_dict and self.mon_dict[the_spell]:
            mon=self.deal_mon(random.choice(self.mon_dict[the_spell]))
        else:
            mon='没抓到2333'
        gen['mon']=mon
        
        
        for i in range(3):
            gen[i] = self.word[rd(0,len(self.word)-1)]
        return gen

    #————————————————————————————
    #生成背景用的单词
    def gen_bg(self):
        gen_bg=[]
        s=set()
        for i in range(1,100):
            s.add(rd(0,len(self.word)-1))
        for i in s:
            gen_bg.append({'spell':self.word[i]['spell'],'top':rd(-100,800),'left':rd(-200,1300),'op':rd(5,20)/100,'size':rd(13,30)})
        return gen_bg
    
    def kiried(self,x):
        return self.word[x]['word']+' '+self.word[x]['spell'] in self.kiri

data=Data()

if __name__=='__main__':
    data = Data()
    print(data.word[1])
    for i in range(160):
        q=data.gen_ques()
        if i%100==99:
            print('已经处理%d个。'%i)
        
        
    import numpy as np
    权s=[data.word[i]['权'] for i in list(data.buff)]
    print('方差=%.3f' % np.array(权s).var())
    print('没读过数=%d'% sum([i==1 for i in 权s]))
    
    import 圖表
    圖表.draw(权s)