# -*- coding: utf-8 -*-
"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""
import MeCab

def Morphological_Analysis():
    with open("neko.txt",mode='r') as f:
        text=f.read()
    #type(text) : str
    mt = MeCab.Tagger("-Ochasen")
    r = mt.parse(text)
    data=r.split("\n")
    with open("neko.txt.mecab",mode='w') as c:
        for i in range(len(data)):
            c.write("".join(data[i]))
            c.write("\n")
def init_dict():
    with open("neko.txt.mecab",mode='r') as f:
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
    return neko_dict

def main():
    Morphological_Analysis()
    data = init_dict()
    nouns=[]
    for i in range(len(data)):
        if data[i]['surface'] == 'の' :
            if data[i-1]['pos'] == '名詞' and data[i+1]['pos'] == '名詞' :
                nouns.append(data[i-1]['surface'] + 'の' + data[i+1]['surface'])
    with open("34_noun_phrase.txt",mode='w') as f:
        for line in nouns :
            f.write(line)
            f.write("\n")

if __name__  == '__main__':
    main()