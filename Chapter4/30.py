# -*- coding: utf-8 -*-
"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
MeCabの使い方（参考）：http://aidiary.hatenablog.com/entry/20101121/1290339360

## 30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""
import MeCab

def Morphological_Analysis():
    with open("neko.txt",mode='r') as f:
        text=f.read()
    #type(text) : str
    mt = MeCab.Tagger("-Ochasen")
    r = mt.parse(text)
    data=r.split("\n")
    with open("30_neko.txt.mecab",mode='w') as c:
        for i in range(len(data)):
            c.write("".join(data[i]))
            c.write("\n")
def init_dict():
    with open("30_neko.txt.mecab",mode='r') as f:
        result=f.readlines()
    data=[]
    neko_dict=[]
    for i in range(len(result)):
        data.append(result[i].split("\t"))
        if len(data[i]) > 2 :
            if len(data[i][3].split("-")) > 1 :
                line_dict={
                    'surface' : data[i][0],
                    'base'    : data[i][2],
                    'pos'     : data[i][3].split("-")[0],
                    'pos1'    : data[i][3].split("-")[1],
                }
                neko_dict.append(line_dict)
            else :
                line_dict={
                    'surface' : data[i][0],
                    'base'    : data[i][2],
                    'pos'     : data[i][3].split("-")[0],
                    'pos1'    : data[i][3].split("-")[-1],
                }
                neko_dict.append(line_dict)
    #print(neko_dict)
    # for line in neko_dict:
        # print(str(line))
    with open("30_neko_dict.txt",mode='w') as c:
        for line in neko_dict:
            c.write(str(line))
            c.write("\n")
def main():
    Morphological_Analysis()
    init_dict()
        
if __name__  == '__main__':
    main()