# -*- coding: utf-8 -*-
"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

style manual       : https://ja.wikipedia.org/wiki/Wikipedia:%E3%82%B9%E3%82%BF%E3%82%A4%E3%83%AB%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB
mark up quick help : https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8

[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]

"""
import gzip
import json
import re

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
    data=UK_data.split('\n')
    for line in range(len(data)):
        m=re.search(r"(ファイル:|File:)(?P<fname>.+?)\|",data[line])
        if m:
            print(m.group("fname"))

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