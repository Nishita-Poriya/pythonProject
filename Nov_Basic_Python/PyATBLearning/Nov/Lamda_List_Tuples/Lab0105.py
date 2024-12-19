# Find the first non-repeating character in a string using sets.
#swiss ->s -x,w-Answer

def first_non_reapiting(string):
    for char in string:
        if string.count(char)==1:
            return char
    return None

print(first_non_reapiting("swiss"))
print(first_non_reapiting("pepper"))
print(first_non_reapiting("dada"))
print(first_non_reapiting("annusinha"))
