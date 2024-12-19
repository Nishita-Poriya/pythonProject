student_inforr={
        "name":"Nishita",
        "age": 65,
       # "age": 67,
        "address": "KA"
}


print(student_inforr["name"])
print(student_inforr["age"])
print(student_inforr["address"])
student_inforr["age"]=100
print(student_inforr)

print("-----------------------------")

student_infor2 = dict(name="Kaushal", age=67, address="KA")
print(student_infor2)

print("-----------------------------")

student_info1={

     "name":"Nishita",
    # "age": 65,
    "age": 67,

        #dictionary under dictionary
            "address":{
                "home_address": "ND",
                "office_address": "DK"
            }
    }
print(student_info1)

print("-----------------------------")

# dictionary under dictionary

student_infor2 = {
    "name": "Kaushal",
    # "age": 65,
    "age": 30,

            "address": {
                "home_address": "GOA",
                "office_address": "MH"
            }
}
print(student_infor2)

