import math
def square(number):
    return number**2
result=square(4)
print(result)

def sum(a,b):
    return a+b
add=sum(3,4)
print(add)

def circle(radius):
    area=math.pi*radius*radius
    circumference=2*math.pi*radius
    return area,circumference
  
       
circle_area,circle_circumference=circle(6)
print("Area is",circle_area,"circumference is",circle_circumference)

def greet(name="Siddhant"):
    return "Hi"+ name+"!"
print(greet("Ram"))
print(greet())


cube=lambda q,r,t: q+r+t
print(cube(2,3,4))

def sum_all(*args): #takes all arguments
    print(args)
    for i in args: #data types is tuple
        print(i*3)
    return sum(args)
print(sum_all(1,2,3,4,5))

def print_kwargs(name,age):
    print("name:",name,"age:",age)
print_kwargs(name="Siddhant",age="17")
# print_kwargs(name="Siddhant",age="17",height="170") #TypeError: print_kwargs() got an unexpected keyword argument 'height' 

def print_kwargs(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")
print_kwargs(name="Siddhant",age="17",height="170")
print_kwargs(name="Golu",age="21",height="171",sex="male")

def even_generator(limit):
    for i in range(2,limit+1,2):
        return i
print(even_generator(10))


#YIELD VS RETURN

#WITH RETURN
def even_generator(limit):
    for i in range(2,limit+1,2):
        return i
for num in even_generator(10):
    print(num) #TypeError: 'int' object is not iterable

#WITH YIELD
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
for num in even_generator(10):
    print(num)

def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))