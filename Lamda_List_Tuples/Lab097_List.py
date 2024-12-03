
my_list = [1,2,3,4]

print("Element of index 0: \n",my_list[0])
print("Element of index 1: \n",my_list[1])
print("Element of index 2: \n",my_list[2])
print("-----------")

# append() - # Append object to the end of the list.
my_list.append(4)
my_list.append(5)
print(my_list)

# extend() - Append a new list
my_list.extend([7,8,9,10])
print(my_list)

# insert()
my_list.insert(1,"Nishita")
print(my_list)

my_list.insert(0,0)
print(my_list)

my_list[1]="Nishita"
print(my_list)

#remove
my_list.remove("Nishita")
print(my_list)


print(" --------------------------")
print(" --------------------------")

my_copy_list=my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Nishita")
my_list.remove(10)

my_copy_list.sort()

print(my_list)

print("--------")

print(my_copy_list)