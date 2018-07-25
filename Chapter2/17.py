# -*- coding: utf-8 -*-
"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはsort, uniqコマンドを用いよ．
"""

def main():
    #file read
    with open("hightemp.txt",mode='r') as f:
        l=f.readlines()
    col=[]
    col1=[]
    for i in range(len(l)):
        col.append(l[i].split('\t'))
        col1.append(col[i][0])
    print(set(col1))

if __name__  == '__main__':
    main()

#UNIX
#cut -f 1 hightemp.txt | sort | uniq
"""
千葉県
和歌山県
埼玉県
大阪府
山形県
山梨県
岐阜県
愛媛県
愛知県
群馬県
静岡県
高知県
"""