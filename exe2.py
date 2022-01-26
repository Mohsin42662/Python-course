var1=int(input("Enter first number ="))
sign=input("operation")
var2=int(input("Enter secound number ="))
sum=int(var1)+int(var2)
mul=int(var1)*int(var2)
sub=int(var1)-int(var2)
div=int(var1)/int(var2)
if(var1==45 and sign=="*" and var2==3 ):
    print("555")
elif(var1==56 and sign=="+" and var2==9 ):
    print("77")
elif (var1 == 56 and sign == "/" and var2 == 6):
        print("4")
elif(sign=="+"):
    print(sum)
elif(sign=="-"):
    print(sub)
elif(sign=="*"):
    print(mul)
elif(sign=="/"):
    print(div)
else:
    print("Sorry incorrect values")

