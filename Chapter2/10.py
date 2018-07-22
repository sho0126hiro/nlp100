# -*- coding: utf-8 -*-
"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

def main():
    data=open("hightemp.txt","r")
    count=0
    for i in data:
        count+=1
    print(count)

if __name__  == '__main__':
    main()

#UNIX
#wc --line hightemp.txt
