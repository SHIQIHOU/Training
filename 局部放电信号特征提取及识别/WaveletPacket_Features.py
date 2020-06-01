import csv
import random
import numpy as np
from scipy import sparse
import math
from scipy import signal
import pywt
import numpy as np
import pandas as pd
import pyhht    #pyhht库，进行hht变换的主要库，可使用pip install pyhht安装
from pyhht.visualization import plot_imfs    #同pyhht库，可视化操作
import tftb.processing    #用来计算瞬时频率的包
from scipy.signal import hilbert    #hilbert变换需要使用的包

num = 6
result = [0 for x in range(199*num)]
def getFeature(path):
    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            a=line.split(',')
            a=np.array(a).astype(float)
            x,y=signal.butter(1,0.4,'highpass')
            a=signal.filtfilt(x,y,a)
        u=[0 for i in range(8)]
        for i in range(100):
            wp = pywt.WaveletPacket(a[10000*i:10000*(i+1)], wavelet='db3', mode='symmetric', maxlevel=3)
            u[0] += np.linalg.norm(wp['aaa'].data,ord=None)
            u[1] += np.linalg.norm(wp['aad'].data,ord=None)
            u[2] += np.linalg.norm(wp['ada'].data,ord=None)
            u[3] += np.linalg.norm(wp['add'].data,ord=None)
            u[4] += np.linalg.norm(wp['daa'].data,ord=None)
            u[5] += np.linalg.norm(wp['dad'].data,ord=None)
            u[6] += np.linalg.norm(wp['dda'].data,ord=None)
            u[7] += np.linalg.norm(wp['ddd'].data,ord=None)
        u[0] /= 100
        u[1] /= 100
        u[2] /= 100
        u[3] /= 100
        u[4] /= 100
        u[5] /= 100
        u[6] /= 100
        u[7] /= 100
    return u

for x in range(num):
    for i in range(199):
        path = 'F:\\BaiduNetdiskDownload\\小波去噪后数据\\' +str(x+1) + 'mmrec4\\' + str(i+1) + '.txt'
        u=getFeature(path)
        result[i+x*199] = u + [x]
        print(x, i)
#random.shuffle(result)
"""with open(r"/home/guest/hsq/Data/1mm/data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for i in range(199*6):
        writer.writerow(result[i])"""
