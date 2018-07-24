# -*- coding: utf-8 -*-
"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

def main():
    #file read
    with open("hightemp.txt",mode='r') as f:
        l=f.readlines()
    length=len(l)
    while True :
        print("N (N <= {}) = ".format(len(l)),end="")
        N=int(input())
        if N <= len(l) :
            break
        print("ERROR (N <= {})".format(len(l)))
    #整数除算+あまりを出す(rem)
    # n分割の要素のうち、rem個が、あまりのため1増加
    div=length//N
    rem=length%N
    s=[]
    for i in range(N):
        if(i<rem) : s.append(div+1)
        else      : s.append(div)
    sum=0
    for i in range(N):
        print("-----------")
        splitdata=open("split_"+str(i+1)+".txt",mode='w')
        for j in range(s[i]):
            print(l[sum+j],end="")
            splitdata.write("".join(l[sum+j]))
        splitdata.close()
        sum+=s[i]
if __name__  == '__main__':
    main()

#UNIX
#split -l 5 hightemp.txt

"""
N (N <= 24) = 5
-----------
高知県  江川崎  41      2013-08-12
埼玉県  熊谷    40.9    2007-08-16
岐阜県  多治見  40.9    2007-08-16
山形県  山形    40.8    1933-07-25
山梨県  甲府    40.7    2013-08-10
-----------
和歌山県        かつらぎ        40.6    1994-08-08
静岡県  天竜    40.6    1994-08-04
山梨県  勝沼    40.5    2013-08-10
埼玉県  越谷    40.4    2007-08-16
群馬県  館林    40.3    2007-08-16
-----------
群馬県  上里見  40.3    1998-07-04
愛知県  愛西    40.3    1994-08-05
千葉県  牛久    40.2    2004-07-20
静岡県  佐久間  40.2    2001-07-24
愛媛県  宇和島  40.2    1927-07-22
-----------
山形県  酒田    40.1    1978-08-03
岐阜県  美濃    40      2007-08-16
群馬県  前橋    40      2001-07-24
千葉県  茂原    39.9    2013-08-11
埼玉県  鳩山    39.9    1997-07-05
-----------
大阪府  豊中    39.9    1994-08-08
山梨県  大月    39.9    1990-07-19
山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02
"""
