# -*- coding: utf-8 -*-
"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

CaboChaのインストールへの流れはここを見た：https://qiita.com/segavvy/items/2f686cfb0065c8cbe698 (ipadicはMeCabの時にインストール済み) 
フォーマット
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形(基本形),読み,発音
"""
import CaboCha
import re

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def printMorph(self):
        print("surface = {0} / base = {1} / pos = {2} / pos1 = {3}".format(self.surface,self.base,self.pos,self.pos1))

def dependency_parsing():
    #係り受け解析 >> ファイル出力
    with open("neko.txt",mode='r') as f:
        text=f.read()
    c = CaboCha.Parser()
    tree=c.parse(text)
    result=tree.toString(CaboCha.FORMAT_LATTICE)
    data=result.split('\n')
    with open("40_neko.txt.cabocha",mode='w') as c:
        for i in range(len(data)):
            c.write("".join(data[i]))
            c.write("\n")

def init_list():
    with open("40_neko.txt.cabocha",mode='r') as f:
        result=f.readlines()
    morph=[]
    for line in result:
        if line == "EOS\n" or line[0]=='*':
            continue
        if len(line.split('\t')) > 1 :
            surface=line.split('\t')[0]
            tmp=line.split('\t')[1]
            base=tmp.split(',')[6]
            pos=tmp.split(',')[0]
            pos1=tmp.split(',')[1]
            morph.append(Morph(surface,base,pos,pos1))
    morph[2].printMorph()
def main():
    #dependency_parsing()
    init_list()

if __name__  == '__main__':
    main()