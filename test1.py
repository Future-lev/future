# print("请输入一个任意大的自然数")
# n=input()
# s=0
# for i in n:
#     s+=int(i)
# print(s)
print("--------------------")
# A=input("请输入集合A")
# B=input("请输入集合B")
# listA=eval(A) #把字符串当成 Python 代码直接执行
# listB=eval(B)
# setA=set(listA) #set在 Python 里叫集合，是一种容器类型。set(xxx)就是把 xxx 转换成集合。
# setB=set(listB)
# print("交集：",setA&setB)
# print("并集：",setA|setB)
# print("差集：",setA-setB)
# print("--------------------")
# n=int(input("请输入一个自然数；"))
# print("二进制：",bin(n))
# print("八进制：",oct(n))
# print("十六进制：",hex(n))
# n=2.34
# print(type(n))
# print("hello"+" world")
# print("a"*3)
# name="彭于晏"
# face="真帅"
# print("我的名字是："+name)
# print(name+face)
# name = "小明"
# age,number,high= 18,2,1.826
# print(f"姓名：{name}，年龄：{age},身高：{high:.2f}")
# print(f"小明今年{age}岁了，有{number}个妹妹")
# s = "python"
# print(s[1:4])
# print(s[::-1])
# print(s[5:2:-1])
# score = 85
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 60:
#     print("C")
# else:
#     print("D")
age = 20
has_id = True
if age >= 18:
    print("成年")
    if has_id:
        print("可以进入")
    else:
        print("成年但无证件，不能进")
else:
    print("未成年")