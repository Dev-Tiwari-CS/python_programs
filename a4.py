# 4. Write a Python program to calculate the sum of three given numbers. If the values are equal,
#  return three times their sum.

a=int(input("enter the 1st valuse"))
b=int(input("enter the 2nd valuse"))
c=int(input("enter the 3rd valuse"))
if(a==b==c):
    print("values are equal, three times their sum.",(a+b+c)*3)
else:
    print(("the sum of three no is ",a+b+c))
