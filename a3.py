# 3. Write a Python program to test whether a number is within 100 of 1000 or 2000.

a=int(input("give the numner"))
if(a>=900 and a<=1100):
    print("given no is within 100 of 1000 number is",a)
elif(a>=1900 and a<=2100):
    print("the given no is within 100 of 2000 number is ",a )
else:
    print("the given value is not in range of 100 of 1000 or 2000 ",a)


    