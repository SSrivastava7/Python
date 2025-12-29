# adding this to github
import random


x=4**2
y=random.choice([1,2,3])
print(x,y)

a=10
b=a
a=15
print(a,b) #15 10
l1=[1,2,3]
l2=l1
l1[0]=44
print(l1,l2)
# [44, 2, 3] [44, 2, 3]
l1=[1,2,3]
l2=l1
l1[0]=44
l2=[1,2,3]
print(l1,l2) 
# [44, 2, 3] [1, 2, 3]