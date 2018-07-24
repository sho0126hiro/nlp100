# -*- coding: utf-8 -*-
"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ
"""

def main():
    #file read
    with open("hightemp.txt",mode='r') as f:
        l=f.readlines()
    col=[]
    col1=[]
    col2=[]
    for i in range(len(l)):
        col.append(l[i].split('\t'))
        col1.append(col[i][0])
        col2.append(col[i][1])
    #print("col1={}".format(col1))
    #print("col2={}".format(col2))
    
    #file write
    with open("col1.txt",mode='w') as c1:
        c1.write('\n'.join(col1))
    with open("col2.txt",mode='w') as c2:
        c2.write('\n'.join(col2))
    
if __name__  == '__main__':
    main()

#UNIX
#cut -f 1 hightemp.txt
#cut -f 2 hightemp.txt
#cut -f 1-2 hightemp.txt

#file1出力
#cut -f 1 hightemp.txt > col2.txt
#cut -f 2 hightemp.txt > col2.txt