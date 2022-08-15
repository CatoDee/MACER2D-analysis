'''
this script is to smooth the data
'''
import numpy as np
def smooth(x,M): #x为一维数组
    K=round(M/2-0.1) #M应为奇数
    lenX=len(x)
    if lenX<2*K+1:
        print('数据长度小于平滑点数')
    else:
        y = np.zeros(lenX)
        for NN in range(0,lenX,1):
            startInd = max([0,NN-K])
            endInd = min(NN+K+1,lenX)
            y[NN] = np.mean(x[startInd:endInd])
    return(y)