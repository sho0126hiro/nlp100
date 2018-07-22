str1 = "aa"
str2 = 3
str3 = [2]

if type(str1) != str : print("true1")
if type(str2) == int : print("true2")
if type(str3) == list : print("true3")
str2=str(str2)
if type(str2) == str : print("true4")