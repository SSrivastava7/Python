tea_varities=["Masala","Black","Oolong"]
print(tea_varities[1:3])
tea_varities[2]="White"
print(tea_varities)
tea_varities[1:3]=["Herbal","Lemon"]
print(tea_varities)
tea_varities[1:1]=["test","test"]
print(tea_varities)
tea_varities[1:3]=[]  
# insert nothing
print(tea_varities)

for tea in tea_varities:
     print(tea)
  
for tea in tea_varities:
      print(tea,end="-")
if "Oolong" in tea_varities:
      print("I have Oolong tea")
else:
      print("i dont have oolong tea")
tea_varities.append("Oolong")
if "Oolong" in tea_varities:
      print("I have Oolong tea")

print(tea_varities)
tea_varities.remove("Lemon")
print(tea_varities)
tea_varities.insert(1,'Lemon')
print(tea_varities)
tea_varities_copy=tea_varities
print(tea_varities_copy,tea_varities)
tea_varities.append("Ginger")
# now both of them have been changed as tey share the same reference. Its mutable.
print(tea_varities_copy,tea_varities)
tea_varities_copy_reference=tea_varities.copy()
# creating different references in memory using .copy() otherwise it would have shared refrences
print(tea_varities,tea_varities_copy_reference)
tea_varities_copy_reference.append("Elaichi")
# elaichi is added only to tea_varities_copy_reference because of different reference
print(tea_varities,tea_varities_copy_reference)

# List Comprehension
squared_nums=[x**2 for x in range(10)]
print(squared_nums)
