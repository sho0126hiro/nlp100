# -*- coding: utf-8 -*-
"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
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
        print("ERROR (N <= {})".format(len(l)),)
    for i in range(N,0,-1):
        print(l[len(l)-i],end="")
if __name__  == '__main__':
    main()

#UNIX
#tail -n 4 hightemp.txt
#tail -4 hightemp.txt
#cat hightemp.txt | tail -4
"""
大阪府  豊中    39.9    1994-08-08
山梨県  大月    39.9    1990-07-19
山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02
"""
