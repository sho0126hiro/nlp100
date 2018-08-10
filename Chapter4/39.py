# -*- coding: utf-8 -*-
"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
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
    plt.scatter(range(1,len(frequency)+1),frequency,marker='.')
    plt.xscale('log')
    plt.yscale('log')
    plt.title("39 Zipfの法則")
    plt.xlabel("出現頻度の順位")
    plt.ylabel("出現頻度")
    plt.grid(axis='y')
    plt.savefig('39.png' )
    
if __name__  == '__main__':
    main()