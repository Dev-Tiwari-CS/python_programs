# 9. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given
#  string. Return n copies of the whole string if the length is less than 2.

string=input("enter the string ")
str=string[0:1]
a=int(input("ente the no of copies you want "))

c=a*str
print(c)
# if(len(string)<2):
#     copy=int(input("enter the no of copies"))
#     print(string[0:1]*copy)

