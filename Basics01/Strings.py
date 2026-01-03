chai="masala chai"
sliced=chai[0:6]
print(sliced)
number="0123456789"
twospace=number[0:8:2]
print(twospace)
threespaces=number[0:9:3]
print(threespaces)
playing=number[0:-1:2]
print(playing)

spaces="    Siddhant   "
print(spaces)
print(spaces.strip())

chai="Masala tea"
nayi_chai=(chai.replace("Masala","Ginger"))
print(chai)
print(nayi_chai)
splited="lemon,Ginger,adrak,masala"
print(splited.split())
print(splited.split("," ))

chai="masala"
quantity=2
order=("I odered {} cups of {} tea")
print(order)
print(order.format(quantity,chai))

List=["Masala","Ginger","lemon"]
listToString=(", ".join(List))
print(listToString)

name="siddhant"
for letter in name:
    print(letter)