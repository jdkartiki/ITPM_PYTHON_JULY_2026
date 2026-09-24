# Filter : it is used to filter the data based on some condition 
# returns only values that satisfy the condition
# filter(function,iteraable)



# even odd numbers 
# nums=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda n:n%2==0,nums))
# print(even)

# #odd numbers
# nums=[1,2,3,4,5,6]
# odd=list(filter(lambda n:n%2!=0,nums))
# print(odd)

# words=["hi","hello","Python","DS"]
# res=list(filter(lambda n:len(n)>3,words))
# print(res)


# Map : is used to apply something/ some property to each element

# nums=[1,2,3,4,5]
# res=list(map(lambda n:n**2,nums))
# print(res)

# words=["hi","hello","python"]
# res=list(map(lambda n:n.upper(),words))
# print(res)

# nums=[1,2,3]
# res=list(map(lambda x:x+10,nums))
# print(res)

# # reduce :: it is used to reduce the list to one single value
# import functools module 

# # sum of list 
# from functools import reduce 
# nums=[10,20,30,40,50]
# res=reduce(lambda a,b:a+b,nums)
# print(res)

# factorial
# from functools import reduce
# n=5
# res=reduce(lambda x,y:x*y,range(1,n+1))
# print(res)

from functools import reduce 
res=reduce(lambda a,b:a if a>b else b,[3,5,8])
print(res)