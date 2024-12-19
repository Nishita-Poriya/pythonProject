student_infor1 = {
    "name": "Nishita",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}
student_infor2 = {
    "name": "Kaushal",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_infor3 = {
    "name": "purvesh",
    # "age": 65,
    "age": 120,
    "address": {
        "home_address": "PODI",
        "office_address": "vizag"
    }
}

student_list =[student_infor1,student_infor2,student_infor3]
print("\n---------------")

print(student_list)
print("\n---------------")

print(student_list[2])
print("\n---------------")

print(student_list[2]["address"])
print("\n---------------")

print(student_list[2]["address"]["office_address"])

#Alternate way
print(student_infor3["address"]["office_address"])