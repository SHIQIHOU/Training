import numpy as np
import pyhht    #pyhht库，进行hht变换的主要库，可使用pip install pyhht安装
import matplotlib.pyplot as plt
from pyhht.visualization import plot_imfs    #同pyhht库，可视化操作
import tftb.processing    #用来计算瞬时频率的包
from scipy.signal import hilbert    #hilbert变换需要使用的包
from scipy import signal
from PyEMD import EMD, Visualisation
import math


def ar_least_square(sample, p):
    matrix_x = np.zeros((sample.size - p, p))
    matrix_x = np.matrix(matrix_x)
    array = sample.reshape(sample.size)
    j = 0
    for i in range(sample.size - p):
        matrix_x[i, 0:p] = array[j:j + p]
        j = j + 1
    matrix_y = np.array(array[p:sample.size])
    matrix_y = matrix_y.reshape(sample.size - p, 1)
    matrix_y = np.matrix(matrix_y)
    # cofe为AR系数
    cofe = np.dot(np.dot((np.dot(matrix_x.T, matrix_x)).I, matrix_x.T), matrix_y)
    return np.array(cofe)

def cal(DataRaw):
    DataRaw = DataRaw  # 原信号
    decomposer = pyhht.emd.EMD(DataRaw)
    imfs = decomposer.decompose()
    ReImf0 = hilbert(imfs[0])
    ReImf1 = hilbert(imfs[1])
    ReImf2 = hilbert(imfs[2])
    ReImf3 = hilbert(imfs[3])
    ReImf4 = hilbert(imfs[4])
    instf0, timestamps0 = tftb.processing.inst_freq(ReImf0)
    instf1, timestamps1 = tftb.processing.inst_freq(ReImf1)
    instf2, timestamps2 = tftb.processing.inst_freq(ReImf2)
    instf3, timestamps3 = tftb.processing.inst_freq(ReImf3)
    instf4, timestamps4 = tftb.processing.inst_freq(ReImf4)
    IA0 = abs(ReImf0)
    IA1 = abs(ReImf1)
    instf = np.array([instf0, instf1, instf2])  # 频率均值
    AR0 = ar_least_square(IA0, 4)
    AR1 = ar_least_square(IA1, 4)
    f1 = instf.mean()
    return np.vstack((AR0, AR1, f1))    #纵向拼接

path = 'F:\\BaiduNetdiskDownload\\超声波数据\\1mm\\50.txt'
with open(path,'r',encoding='utf-8') as f:
    for line in f:
        a=line.split(',')
        a=np.array(a).astype(float)
        x,y=signal.butter(1,0.4,'highpass')
        a=signal.filtfilt(x,y,a)
"""decomposer = pyhht.emd.EMD(a[5000:6000])
imfs = decomposer.decompose()      #获取到imfs数据。
plot_imfs(a[5000:6000], imfs) 
ReImf0 = hilbert(imfs[0])
ReImf1 = hilbert(imfs[1])
ReImf2 = hilbert(imfs[2])
ReImf3 = hilbert(imfs[3])
ReImf4 = hilbert(imfs[4])
ReImf = np.array([ReImf0, ReImf1, ReImf2, ReImf3, ReImf4])
amplitude = abs(ReImf0)     #计算幅值
instf, timestamps = tftb.processing.inst_freq(ReImf0)    #计算瞬时频率
plt.plot(timestamps, instf)     #画图看看效果
plt.show()"""
x=(cal(a[6000:7000]))
