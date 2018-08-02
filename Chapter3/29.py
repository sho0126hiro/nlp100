# -*- coding: utf-8 -*-
"""
::未完成
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

MediaWiki API:https://www.mediawiki.org/wiki/API:Main_page/ja
API:Clien code/ja : https://www.mediawiki.org/wiki/API:Client_code/ja
MediaWiki API : https://www.mediawiki.org/w/api.php
Request Quicstart : http://requests-docs-ja.readthedocs.io/en/latest/user/quickstart/#url
How to use Mwdiawiki api : https://qiita.com/yubessy/items/16d2a074be84ee67c01f
"""
import gzip,json,re,pprint
import requests

def extract_text(text):
    #gzip file open >> json
    with gzip.open("jawiki-country.json.gz","rt") as f:
        for line in f:
            obj = json.loads(line)
            #type(obj) : class 'dict
            if obj["title"] == text :
                return obj["text"]

def delete_markup(text):
    #見出し == == === === ==== ====
    text=re.sub(r"=+\s(.+?)\s=+",lambda m : m.group(1),text)
        #スタブ {{ }}
    text=re.sub(r"{{(.+?)}}",lambda m : m.group(1),text)
    #強調 '' '' ''' ''' '''' ''''
    text=re.sub(r"\'{2,}","",text)
    #内部リンク [[]]
    text=re.sub(r"\[\[(.+?)\]\]",lambda m : m.group(1).split('|')[-1],text)
    #m.group(1) : (.+?)を取得し、|で分割後、[-1]で一番最後の要素（表示文字）を取得
    #外部リンク []
    text=re.sub(r"\[(.+?)\]",lambda m : m.group(1).split('|')[-1],text)
    #リダイレクト
    text=re.sub(r"#REDIRECT\[\[(.+?)\]\]",lambda m : m.group(1),text)
    #コメントアウト
    text=re.sub(r"<!--(.+?)-->",lambda m : m.group(1),text)
    #箇条書き
    text=re.sub(r"^\*+\s","",text)
    #定義の箇条書き
    text=re.sub(r"^(;|:)\s","",text)
    # 水平線
    text=re.sub(r"^-+","",text)
    #署名
    text=re.sub(r"^~+","",text)

    return text

def main():
    UK_data=extract_text('イギリス')
    #UK_data : str
    #re.DOTALL : 改行にもマッチさせる
    m=re.search(r"{{基礎情報\s国(?P<info>.+?)\n}}",UK_data,re.DOTALL)
    if m :
        info = m.group("info")
    #m.group("info"):基礎情報が入ってる
    info_list=info.split('\n|')
    info_dict={}
    sortlist=[] #ソート用
    for i in range(len(info_list)): 
        #マークアップ除去
        info_list[i]=delete_markup(info_list[i])
        m2=re.split(r"\s+=\s+",info_list[i])
        #re.split : "\s+=\s+"で区切ってm2リストに格納する
        if len(m2) == 2 :
            info_dict[m2[0]]=m2[1]
            sortlist.append(m2[0])
    
    #出現順にソートして表示
    info=sorted(info_dict.items(),key=lambda m2 : sortlist.index(m2[0]))
    #info_dict.items() ; 辞書のタプル型リストを取得
    #pprint.pprint(info)
    #http://ja.wikipedia.org/w/api.php?パラメータ1=値1&パラメータ2=値2&...&パラメータn=値n

    endpoint = "https://commons.wikimedia.org/w/api.php"
    payload = {"actions": "query",
               "title"  : "Image:{}".format(info_dict[u"国旗画像"]),
               "prop"   : "imageinfo",
               "format" : "json",
               "iiprop" : "endpoint"}
    r = requests.get(endpoint,params=payload)
    flagurl=json.loads(r.text)
    print(flagurl)
    
if __name__  == '__main__':
    main()

"""
 *** GIVE UP ***
"""