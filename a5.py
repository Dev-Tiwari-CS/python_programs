# 5. Write a Python program to get a newly-generated string from a given string where "Is" has been added to 
# the front. Return the string unchanged if the given string already begins with "Is".
a=input("give the string")
if(a[0]=="i" and a[1]=="s"):
    print(a)
else:
    print("is " + a)