# print("hello Sir")

# def chai(n):
#     print(n)

# chai("Want some tea")
#Muutable and Immutable-> Object by reference example.
# x=10;
# y=x;
# print("old x",x)  
# print("old y",y)
# x= 15
# print("new x",x)
# print ("new y after changing x",y) Value is still pointing 10 for y but changed for x. 


# a=[1,2,3]
# b=a
# print(a)
# print(b)
# a[0]=33

# print(a)
# print(b)
# b=[1,2,3]

# print(a)
# print(b)

# string1='123456789'
# print(string1[:-2:3])

# chai="  Masala Tea   "
# print(chai.strip())
# print(chai.capitalize())
# print(chai.upper())
# print(chai.replace('Masala','Ginger'))
# chai= "'Lemon,'Ginger','Mint'"
# print(chai.split())
# print(chai.split(" ,"))
# chai="Masala Tea"
# print(chai.find("Tea"))
# print(chai.find("tea"))
# print(chai.count("a"))

# order="Masala chai"
# quantity=2
# ORDER="I ordered {} cup of {}"
# print(ORDER)
# print(ORDER.format(quantity,order))

# chai_variety=['Lemon','Masala','Ginger']
# print(type(chai_variety))
# print(", ".join(chai_variety))
# print(type(", ".join(chai_variety)))
# name="Siddhant"
# for letter in name:
#     print(letter)
# chai="He said","Tea was fantastic"
# print(chai)
# chai="He said,\"Tea was fantastic\""
# print(chai)

# chai="masala\nchai"
# print(chai)
# chai=r"masala\nchai"  
# print(chai)
LIST
chai_varities=["OOlong","ginger","White"]
print(chai_varities[:2])
print(chai_varities[0:2])

chai_varities[:2]=["Masala","lemon"]
print(chai_varities)
for tea in chai_varities:
    print(tea)
if "Masala" in chai_varities:
    print("I have Masala Tea")

chai_varities.append("Oolong")
print(chai_varities)

squared_nums=[x**2 for x in range(11)]-> List comprehension.
print(squared_nums)