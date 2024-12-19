#Tupples
#collection of items
#()
## Immutable

my_tuple = (1,3,5,6,23)
print("my_tuples:",my_tuple)
#my_tuple[3] = 64 # TypeError: 'tuple' object does not support item assignment

shopping_list_wife = ["bread","milk","butter"]
shopping_list_wife[2]= "jam"
print(shopping_list_wife)

# Real of Tuples
my_tuple = ("amazon.com", "sdet.live")
my_api_list = list(my_tuple)
print(my_api_list)
# my_tuple[0] = "abc.com" # TypeError: 'tuple' object does not support item assignment

# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://amazon.com", "https://thetestingacademy.com")
print(API_URLSs[2])