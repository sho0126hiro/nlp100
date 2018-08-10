# -*- coding: utf-8 -*-
"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

棒グラフの出力例 : https://pythondatascience.plavox.info/matplotlib/%E6%A3%92%E3%82%B0%E3%83%A9%E3%83%95
Hou to use 'numpy' : https://qiita.com/jyori112/items/a15658d1dd17c421e1e2
numpyとは : https://www.sejuku.net/blog/42550
Ububtu上のMatplotlibで日本語出力できない問題の解決方法 : fc-list | grep Takao
"""
import numpy as np
import matplotlib
matplotlib.use('Agg') # error除去のため
import matplotlib.pylab as plt
from matplotlib.font_manager import FontProperties
# グラフで使うフォント情報(デフォルトのままでは日本語が表示できない)

def main():
    with open("36_word_frequency.txt",mode='r') as f:
        data=f.readlines()
    word=[]
    frequency=[]
    for i in range(10):
        data[i]=data[i].replace("\n","")
        word.append(data[i].split("\t")[0])
        frequency.append(data[i].split("\t")[1])
    print(word)
    print(frequency)
    frequency_int=[]
    #str >> int
    for num in frequency:
        frequency_int.append(int(num))
    fp = FontProperties(fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=14)
    left=word
    right=frequency_int
    plt.bar(left,right)
    plt.savefig( '37.png' )
    print(matplotlib.matplotlib_fname())
    # /home/sho0126hiro/.local/lib/python3.5/site-packages/matplotlib/mpl-data/matplotlibrc
    print(matplotlib.get_configdir())
    # /home/sho0126hiro/.config/matplotlib
    print(matplotlib.rcParams['font.family'])


if __name__  == '__main__':
    main()