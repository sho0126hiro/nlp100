# -*- coding: utf-8 -*-
"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""

def main():
    #file read
    with open("hightemp.txt",mode='r') as f:
        l=f.readlines()
    while True :
        print("N (N <= {}) = ".format(len(l)),end="")
        N=int(input())
        if N <= len(l) :
            break
        print("ERROR (N <= {})".format(len(l)))
    for i in range(N):
        print(l[i],end="")
if __name__  == '__main__':
    main()

#UNIX
#head -n 4 hightemp.txt
#head -4 hightemp.txt
#cat hightemp.txt | head -4
"""
高知県  江川崎  41      2013-08-12
埼玉県  熊谷    40.9    2007-08-16
岐阜県  多治見  40.9    2007-08-16
山形県  山形    40.8    1933-07-25
"""
