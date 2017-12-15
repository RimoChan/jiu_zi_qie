import matplotlib.pyplot as plt  
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

def draw(height):
    plt.title('緩衝狀態')
    plt.xlabel('緩衝區')
    plt.ylabel('確率')
    
    left=range(len(height))
    
    plt.bar(left = left,height = height,color='#000',width = 1,yerr=0.000001)
    plt.show()