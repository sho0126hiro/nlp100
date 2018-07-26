# -*- coding: utf-8 -*-
"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．

基礎情報template：https://ja.wikipedia.org/wiki/Category:%E5%9F%BA%E7%A4%8E%E6%83%85%E5%A0%B1%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88
基礎情報template>>地理の基礎情報template>>国の基礎情報template>>template：基礎情報　国
template：基礎情報　国：https://ja.wikipedia.org/wiki/Template:%E5%9F%BA%E7%A4%8E%E6%83%85%E5%A0%B1_%E5%9B%BD


|フィールド名 = [値]

"""
import gzip
import json
import re
from pprint import pprint 

def extract_text(text):
    #gzip file open >> json
    with gzip.open("jawiki-country.json.gz","rt") as f:
        for line in f:
            obj = json.loads(line)
            #type(obj) : class 'dict
            if obj["title"] == text :
                return obj["text"]
def main():
    UK_data=extract_text('イギリス')
    #UK_data : str
    #re.DOTALL : 改行にもマッチさせる
    m=re.search(r"{{基礎情報\s国(?P<info>.+?)\n}}",UK_data,re.DOTALL)
    if m :
        info = m.group("info")
    #m.group("info"):基礎情報が入ってる
    info_list=info.split('\n|')
    #print(info_list)
    info_dict={}
    for i in range(len(info_list)): 
        m2=re.split(r"\s+=\s+",info_list[i])
        #re.split : "\s+=\s+"で区切ってm2リストに格納する
        if len(m2) == 2 :
            info_dict[m2[0]]=m2[1]
    print(info_dict)

if __name__  == '__main__':
    main()

"""
Royal Coat of Arms of the United Kingdom.svg
Battle of Waterloo 1815.PNG
The British Empire.png
Uk topo en.jpg
BenNevis2005.jpg
Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg
Palace of Westminster, London - Feb 2007.jpg
David Cameron and Barack Obama at the G20 Summit in Toronto.jpg
Soldiers Trooping the Colour, 16th June 2007.jpg
Scotland Parliament Holyrood.jpg
London.bankofengland.arp.jpg
City of London skyline from London City Hall - Oct 2008.jpg
Oil platform in the North SeaPros.jpg
Eurostar at St Pancras Jan 2008.jpg
Heathrow T5.jpg
Anglospeak.svg
CHANDOS3.jpg
The Fabs.JPG
PalaceOfWestminsterAtNight.jpg
Westminster Abbey - West Door.jpg
Edinburgh Cockburn St dsc06789.jpg
Canterbury Cathedral - Portal Nave Cross-spire.jpeg
Kew Gardens Palm House, London - July 2009.jpg
2005-06-27 - United Kingdom - England - London - Greenwich.jpg
Stonehenge2007 07 30.jpg
Yard2.jpg
Durham Kathedrale Nahaufnahme.jpg
Roman Baths in Bath Spa, England - July 2006.jpg
Fountains Abbey view02 2005-08-27.jpg
Blenheim Palace IMG 3673.JPG
Liverpool Pier Head by night.jpg
Hadrian's Wall view near Greenhead.jpg
London Tower (1).JPG
Wembley Stadium, illuminated.jpg
"""