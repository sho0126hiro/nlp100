#00. 文字列の逆順
#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

def StrReverse(str1):
    return str1[::-1]
    #str[i:j:k] >> i to j step k
def main():
    str1="stressed"
    print(str1)
    str2=StrReverse(str1)
    print(str2)

if __name__  == '__main__':
    main()