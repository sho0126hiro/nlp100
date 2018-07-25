# -*- coding: utf-8 -*-
"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さ
らに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

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
