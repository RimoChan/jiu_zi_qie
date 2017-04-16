from random import randint as rd

import sys
import json
sys.path.append('data')
import config

#————————————————————————————
#读入单词表
f=open('data/'+config.word_dict,encoding='utf8')
f.read(1)
word=[] #单词表
while 1:
    line=f.readline()
    if line:
        l=line.split()
        word.append(dict( [(i,l[config.dict_order[i]]) for i in config.dict_order] ))
    else:
        break
f.close()

#————————————————————————————
#读入被切过的单词
f=open('data/kiri.json',encoding='utf8')
kiri=json.loads(f.read())
f.close()


#————————————————————————————
#存档被切过的单词
def kiri_save():
    f=open('data/kiri.json','w',encoding='utf8')
    f.write(json.dumps(kiri,ensure_ascii=False))
    f.close()

#————————————————————————————
#生成一个题目
def gen_ques():
    gen=[]
    while True: 
        x=rd(0,len(word)-1)
        if word[x]['word']+' '+word[x]['spell'] not in kiri: 
            print(word[x]['word']+' '+word[x]['spell'])
            break
    seikai=rd(1,4)
    gen.append(word[x]['word'])
    for i in range(1,5):
        if i==seikai:
            gen.append(word[x]['chinese'])
        else:
            gen.append(word[rd(0,len(word)-1)]['chinese'])
    gen.append(seikai)
    gen.append(word[x]['spell'])
    return tuple(gen)
    
#————————————————————————————
#生成背景用的单词
def gen_bg():
    gen_bg=[]
    s=set()
    for i in range(1,100):
        s.add(rd(0,len(word)-1))
    for i in s:
        gen_bg.append({'spell':word[i]['spell'],'top':rd(-100,800),'left':rd(-200,1300),'op':rd(5,20)/100,'size':rd(13,30)})
    return gen_bg
'nya'
'nya'
'nya'
'nya'
'nya'
'nya'
'nya'
if __name__=='__main__':
    print(kiri)