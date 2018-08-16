# -*- coding: utf-8 -*-
"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
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

class Chunk:
    def __init__(self,morphs,dst,srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

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
    morph=[]# .surface = 'EOS'の時
    # .base  count=0 0 文目の終了（存在しない）
    # .pos   count=0+1 文目が次から始まる
    # .pos1  'EOS'
    count=0
    morph.append(Morph('EOS',str(count),str(count+1),'EOS'))
    for line in result:
        if line == "EOS\n" or line[0]=='*':
            continue # 処理しない行
        surface=line.split('\t')[0]
        tmp=line.split('\t')[1]
        base=tmp.split(',')[6]
        pos=tmp.split(',')[0]
        pos1=tmp.split(',')[1]
        morph.append(Morph(surface,base,pos,pos1))
        if surface == '。' :
            count+=1
            morph.append(Morph('EOS',str(count),str(count+1),'EOS'))
            # .surface = 'EOS'の時
            # .base  count=num   num   文目の終了（存在しない）
            # .pos   count=num   num+1 文目が次から始まる
            # .pos1  'EOS'
    return morph
def main():
    # dependency_parsing()
    morph=init_list()
    #三文目の形態素列を示す
    for i in range(len(morph)):
        if morph[i].surface == 'EOS' and morph[i].pos == '3' :
            i+=1
            while not(morph[i].surface == 'EOS') :
                morph[i].printMorph()
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