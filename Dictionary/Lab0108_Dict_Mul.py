from Dictionary.Lab107_Dict_P2 import student_infor2

student_infor1 ={
    "name":"Nishita",
    "age":28,
        "address":{
            "home_address":"Divine Residency",
            "office address":"UK"
        }
}

print(student_infor1)
print("--------------------------------")

student_info2 ={
    "name":"Kaushal",
    "age":30,
        "address":{
            "home_address": "Ahmedabad",
            "office_address":"GJ"
        }
}

print(student_info2)
print("----------------------------------")

student_list = [student_infor1,student_infor2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["home_address"]["office_address"])

# print(student_list[1])
# print(student_list[2])

