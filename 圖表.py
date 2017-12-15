import matplotlib.pyplot as plt  
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

def draw(height):
    plt.title('缓冲状态')
    plt.xlabel('缓冲区')
    plt.ylabel('确率')
    
    left=range(len(height))
    
    plt.bar(left = left,height = height,color='#000000',width = 1,yerr=0.000001)
    plt.show()