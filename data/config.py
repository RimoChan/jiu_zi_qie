#————————————————————————————
#并没有什么用的用户名和密码233333

name='Rimo'

password='daisuki'

#————————————————————————————
#是否在线，如果是False的话就不会和服务器通信了
#通信的话就可以在不同的设备上同步你切过的词
#但是说不定有什么我不知道的bug然后数据突然就消失，所以没有这个必要的话就不要填True

online_mode=True

server='http://127.0.0.1:4950'

#————————————————————————————
#选择字典文件

word_dict='旧版n3.txt'

dict_order={'spell':0, 'word':1, 'chinese':-1}

#这一行指定字典的阅读顺序
# 比如旧版n3字典是这样的——「合う	あう	①		一致、合适」
# 写法(spell)在第0(注意!)个位置，单词(word)在第1个位置，翻译在最后一个位置
#为什么是是最后一个而不是第三个，如果你的字典排列整齐的话就都可以。但是有些字典的每行的个数并不是确定的。

# 再举一个例子，比如: 
# word_dict = 'n2单词.txt' 
# dict_order = {'spell':-2, 'word':0, 'chinese':-1}
# 这里的spell不一定是1，但一定是-2。
# あいじょう	愛情	爱情，爱慕
# アイスクリーム		冰激凌


#————————————————————————————
#测试用的main，别管
if __name__=='__main__':
    f=open(word_dict,encoding='utf8')
    f.read(1)
    word=[]
    n=0
    while n<50:
        n+=1
        line=f.readline()
        if line:
            l=line.split()
            print(dict( [(i,l[dict_order[i]]) for i in dict_order] ))
        else:
            break
    f.close()