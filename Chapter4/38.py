# -*- coding: utf-8 -*-
"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

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
    for line in data:
        line=line.replace("\n","")
        word.append(line.split("\t")[0])
        frequency.append(int(line.split("\t")[1]))
    frequency_int=[]
    #str >> int
    left=word
    right=frequency
    plt.bar(left,right)
    plt.savefig( '37.png' )

if __name__  == '__main__':
    main()