# write a program to print multiplication table of a given number
num=int(input("enter a number"))
for x in range (1,11):
    product=num*x
    print(num,"*",x,"=",product)