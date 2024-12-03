# Dictionary from Two Lists
from sockshandler import merge_dict

keys=["name","role","experience"]
values = ["Nishita","QA",5]

my_Dict = dict(zip(keys,values))
print(my_Dict)

dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}

merge_dict = dict1 | dict2
print(merge_dict)

print(merge_dict.get("a"))
