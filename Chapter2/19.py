# -*- coding: utf-8 -*-
"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""
import collections

def main():
    #file read
    with open("hightemp.txt",mode='r') as f:
        l=f.readlines()
    data=[]
    for i in range(len(l)):
        data.append(l[i].split('\t'))
    col=[]
    col1=[]
    for i in range(len(l)):
        col.append(l[i].split('\t'))
        col1.append(col[i][0])
    data=collections.Counter(col1)
    printdata=data.most_common()
    for i in range(len(printdata)):
        print(str(printdata[i][1])+" "+printdata[i][0])
    
if __name__  == '__main__':
    main()

#UNIX
#cut -f 1 hightemp.txt | sort | uniq -c | sort r | cut -c 6-
"""
 3 群馬県
 3 山梨県
 3 山形県
 3 埼玉県
 2 静岡県
 2 愛知県
 2 岐阜県
 2 千葉県
 1 高知県
 1 愛媛県
 1 大阪府
 1 和歌山県
"""