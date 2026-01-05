chai_types={"Masala":"Kadak","Lemon":"Khataa","Green":"Paniwala"}
print(chai_types)
print(chai_types["Masala"])
print(chai_types.get("Masala"))
#print(chai_types["Masalaa"]) 
#will give this error when not found KeyError: 'Masalaa'
#print(chai_types.get("Masalaa"))
#  # will give output as None when not found
chai_types["Masala"]="Chatak"
print(chai_types)

for chai in chai_types:
    print(chai,chai_types[chai])
#"Using key value in dictionary",
for key,value in chai_types.items():
    print(key,value)
if "White" in chai_types:
    print("I have White tea")
else:
    print("I don't have White tea chose from this list",chai_types)

chai_types["Citrus"]="Khatta"
print(chai_types)
chai_types.pop("Masala")
print(chai_types)
chai_types.popitem() #removes last items added
print(chai_types)
del chai_types["Green"]
print(chai_types)

chai_types_copy=chai_types.copy()
print(chai_types,chai_types_copy)
chai_types_copy["Ginger"]="Kadak"
print(chai_types,chai_types_copy)

tea_shop={
    'chai':{"Ginger":"Kadak","Lemon":"khatta"},
    'Tea':{"Black":"Strong"}
    }
print(tea_shop["chai"]["Ginger"])

squared_num={x:x**2 for x in range(6)}
print(squared_num)

tea={"Masala","Ginger","lemon"}
default_values="Delicious"
new_dict=dict.fromkeys(tea,default_values)
print(new_dict)