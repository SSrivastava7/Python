tea_types=("Green","Black","Lemon")
print(tea_types)
#tea_types[0]="Oolong" TypeError: 'tuple' object does not support item assignment
new_tea_types=("Oolong","Masala")
total_tea_types=tea_types+new_tea_types
print(total_tea_types)
if "Green" in total_tea_types:
    print("Tea is presnnt")
new_tea_types=("Oolong","Masala","Oolong")
print(new_tea_types)
print(new_tea_types.count("Oolong"))
print(type(tea_types))
(black,green,oolong)=tea_types
print(tea_types)