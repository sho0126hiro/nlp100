# -*- coding: utf-8 -*-
"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""
import numpy as np
import matplotlib
matplotlib.use('Agg') # error除去のため
import matplotlib.pylab as plt

def main():
    with open("36_word_frequency.txt",mode='r') as f:
        data=f.readlines()
    word=[]
    frequency=[]
    for line in data:
        line=line.replace("\n","")
        word.append(line.split("\t")[0])
        frequency.append(int(line.split("\t")[1]))
    plt.hist(frequency,bins=20,range=(1,20))
    plt.xlim(xmin=1,xmax=20)
    plt.xticks([i for i in range(1,21) if i % 5 == 0 ])
    plt.title("38 単語の出現頻度")
    plt.xlabel("出現頻度")
    plt.ylabel("出現頻度をとる単語数")
    plt.grid(axis='y')
    plt.savefig('38.png' )
    
if __name__  == '__main__':
    main()