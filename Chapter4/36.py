# -*- coding: utf-8 -*-
"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""
import MeCab
import collections

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
    words=[]
    i=0
    for line in data:
        if line['pos'] != '記号':
            words.append(line['surface'])
    words_frequency=collections.Counter(words)
    #print(sort_data)
    #sort_data.sort(key=lambda x : x[1])
    #sort_data.reverse()
    """
    with open("36_word_frequency.txt",mode='w') as f:
        for i in range(len(sort_data)) :
            f.write(sort_data[i][0] + "\t" + str(sort_data[i][1]))
            f.write("\n")
    """
if __name__  == '__main__':
    main()