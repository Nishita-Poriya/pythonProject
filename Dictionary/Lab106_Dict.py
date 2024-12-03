my_Dict ={
    "name":"Nishita",
    "age":28,
    "role":"QA",
    "Experience": 5
}

print(my_Dict)
print(my_Dict["age"])

#change role
my_Dict["role"]="Manual Tester"
print(my_Dict)

#delete age
del my_Dict["age"]
print(my_Dict)

print("--------------")

for key,value in my_Dict.items():
    print(key,"->",value)

print("----------------")
#Now age is already removed and role is available so return boolean values
print("age" in my_Dict)
print("role" in my_Dict)

