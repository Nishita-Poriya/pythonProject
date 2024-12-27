import os

file_name="nishita.txt"
content="This is a nishita's File ABC"

with open(file_name,"w") as file:
    file.write(content)

with open(file_name,"r") as file:
    content2=file.read()
    print(content2)

    