# -*- coding: utf-8 -*-
"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

def main():
    #file read
    with open("col1.txt",mode='r') as c1:
        col1=c1.readlines()
    with open("col2.txt",mode='r') as c2:
        col2=c2.readlines()
    #marge
    x=[]
    for i in range(len(col1)):
        x.append(col1[i].strip('\n'))
        x.append(col2[i].strip('\n'))
    #print(x[0:2])#['高知県\n', '江川崎\n']
    m=[]
    for i in range(0,len(x),2):
        m.append(x[i:i+2])
    print(m)
    marge=[]
    for i in range(len(m)):
        marge.append("\t".join(m[i]))
    print(marge)
    #file write
    with open("col12_marge.txt",mode='w') as margedata:
        margedata.write('\n'.join(marge))

if __name__  == '__main__':
    main()

#UNIX
#paste col1.txt col2.txt > col12_marge.txt
