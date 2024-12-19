# Sorting by values in descending order

my_dict={"a":3,"b":2,"c":1}

sorted_dict= dict(sorted(my_dict.items(),key = lambda item: item[1],reverse=True))

print(sorted_dict)