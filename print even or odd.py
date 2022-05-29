# print all even and odd numbers from 1 upto a given input
a=int(input("enter a number"))
for i in range (1,a+1):
    if i%2==0:
        print("even number=",i)
    else:
        print("odd number=",i)    