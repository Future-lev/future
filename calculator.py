print("简易计算器")
print("支持加减乘除")
try:
    num1=input("请输入第一个数：")
    num1=float(num1)
    operator=input("请输入运算符：")
    num2=input("请输入第二个数：")
    num2=float(num2)
    result=0
    flag=True
    if operator=="+":
        result=num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":
        if num2==0:
            print("错误，分母不能为0")
            flag=False
        else:
            result=num1/num2
    else:
        flag=False
    if flag:
        print(f"{num1}{operator}{num2}={result}")
    else:
        print("式子错误，请重新输入")
except ValueError:
    print("输入错误！请输入数字")
