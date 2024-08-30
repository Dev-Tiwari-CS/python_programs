# 8. Write a Python program to count the number 4 in a given list.
# a=[1,23,4,5,6,4,8]
# count=0
# n=0

# if(a[n]==4):
#     count+1
# elif(a[n]==4):
#     n=n+1
# else:
#     print("4 is not found in given list")

numbers = [1, 4, 6, 4, 4, 7, 4]

count = 0
for number in numbers:
    if number == 4:
        count += 1
print('no 4  ocure in list ', count ,"time")
