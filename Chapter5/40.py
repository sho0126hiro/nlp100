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
        # .surface = 'EOS'の時
        # .base  count=num   num   文目の終了（存在しない）
        # .pos   count=num   num+1 文目が次から始まる
        # .pos1  'EOS'
    def printMorph(self):
        print("surface = {0} / base = {1} / pos = {2} / pos1 = {3}".format(self.surface,self.base,self.pos,self.pos1))

def dependency_parsing():
    #係り受け解析 >> ファイル出力
    with open("neko.txt",mode='r') as f:
        text=f.read()
    c = CaboCha.Parser()
    tree=c.parse(text)
    result=tree.toString(CaboCha.FORMAT_LATTICE)
    with open("40_neko.txt.cabocha",mode='w') as c:
        c.write(result)

def init_list():
    with open("40_neko.txt.cabocha",mode='r') as f:
        result=f.readlines()
    morphs=[]
    # .surface = 'EOS'の時
    # .base  count=0 0 文目の終了（存在しない）
    # .pos   count=0+1 文目が次から始まる
    # .pos1  'EOS'
    count=0
    morphs.append(Morph('EOS',str(count),str(count+1),'EOS'))
    for line in result:
        if line == "EOS\n" or line[0]=='*':
            continue # 処理しない行
        surface=line.split('\t')[0]
        tmp=line.split('\t')[1]
        base=tmp.split(',')[6]
        pos=tmp.split(',')[0]
        pos1=tmp.split(',')[1]
        morphs.append(Morph(surface,base,pos,pos1))
        if surface == '。' :
            count+=1
            morphs.append(Morph('EOS',str(count),str(count+1),'EOS'))
            # .surface = 'EOS'の時
            # .base  count=num   num   文目の終了（存在しない）
            # .pos   count=num   num+1 文目が次から始まる
            # .pos1  'EOS'
    return morphs
def main():
    # dependency_parsing()
    morphs=init_list()
    #三文目の形態素列を示す
    for i in range(len(morphs)):
        if morphs[i].surface == 'EOS' and morphs[i].pos == '3' :
            i+=1
            while not(morphs[i].surface == 'EOS') :
                morphs[i].printMorph()
                i+=1

if __name__  == '__main__':
    main()

"""
surface = 　 / base = 　 / pos = 記号 / pos1 = 空白
surface = どこ / base = どこ / pos = 名詞 / pos1 = 代名詞
surface = で / base = で / pos = 助詞 / pos1 = 格助詞
surface = 生れ / base = 生れる / pos = 動詞 / pos1 = 自立
surface = た / base = た / pos = 助動詞 / pos1 = *
surface = かとん / base = 火遁 / pos = 名詞 / pos1 = 一般
surface = と / base = と / pos = 助詞 / pos1 = 格助詞
surface = 見当 / base = 見当 / pos = 名詞 / pos1 = サ変接続
surface = が / base = が / pos = 助詞 / pos1 = 格助詞
surface = つか / base = つく / pos = 動詞 / pos1 = 自立
surface = ぬ / base = ぬ / pos = 助動詞 / pos1 = *
surface = 。 / base = 。 / pos = 記号 / pos1 = 句点
"""