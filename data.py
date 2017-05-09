import random
rd= random.randint

import sys
import json
import re
sys.path.append('data')
import config
import user

def chocolate():
    x=config.chocolate
    while True:
        x=x*4.3451%3.5836
        yield x

class Data:

    def __init__(self):
        #————————————————————————————
        #读入单词表
        f=open('data/'+config.word_dict,encoding='utf8')
        f.read(1)
        self.word=[] #单词表
        while 1:
            line=f.readline()
            if line:
                l=line.split()
                self.word.append(dict( [(i,l[config.dict_order[i]]) for i in config.dict_order] ))
            else:
                break
        f.close()
        #————————————————————————————
        #读入例句字典
        f=open('data/dictionary.json',encoding='utf8')
        self.mon_dict=json.loads(f.read())
        f.close()
        
        #————————————————————————————
        #打乱单词表
        a=chocolate()
        for i in self.word:
            i['eigen']=next(a)
        self.word.sort( key=lambda x : x['eigen'] )
        #————————————————————————————
        #读入被切过的单词
        f=open('data/kiri.json',encoding='utf8')
        self.kiri=json.loads(f.read())
        f.close()
        #————————————————————————————
        #生成缓冲区
        self.buff=set()
        self.now_word=0
        self.buff_full()
        print(self.buff)

    #————————————————————————————
    #填满缓冲区
    def buff_full(self):
        while len(self.buff)<config.buff_size and self.now_word<len(self.word):
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
        self.kiri=user.kiri_sync(self.kiri)
    
    #处理例句
    def deal_mon(self,mon):
        if type(mon)==str:
            pattern=re.compile(r'^.*?[^<]/')
            a=pattern.findall(mon)[0]
            b=mon[len(a):-1]
            mon=['','']
            mon[0]=a[0:-1]
            mon[1]=b
            
        if type(mon)==list:
            return mon[0] + '<br/><span class="例句中文">'+mon[1]+'</span>'

    #————————————————————————————
    #生成一个题目
    def gen_ques(self):
        gen=[]
        try:
            self.pre_x=self.x
        except:
            self.pre_x=-1
        while True:
            self.x=random.choice(list(self.buff)) #取buff中的一个下标，python好像没法从集合里选出随机元素？？
            if len(self.buff)==1:  break
            if self.x!=self.pre_x: break
        the_word=self.word[self.x]
        
        the_spell=the_word['spell']
        
        if the_spell in self.mon_dict and self.mon_dict[the_spell]:
            print(self.mon_dict[the_spell])
            mon=self.deal_mon(random.choice(self.mon_dict[the_spell]))
            print(mon)
        else:
            mon='没抓到2333'
        
        seikai=rd(1,4)
        gen.append(the_word['word'])
        for i in range(1,5):
            if i==seikai:
                gen.append(the_word['chinese'])
            else:
                gen.append(self.word[rd(0,len(self.word)-1)]['chinese'])
        gen.append(seikai)
        gen.append(the_spell)
        gen.append(mon)
        return tuple(gen)

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
    print(
    data.deal_mon('学校を出てすぐこの会社に<b><b>就職</b></b>した/一出校门马上就到这家公司来<b>工作</b>了。'))