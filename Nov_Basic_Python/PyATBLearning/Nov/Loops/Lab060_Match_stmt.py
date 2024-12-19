# Write a program to ask the user which browser he want to run automation.
# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block

# Match Statement -> # Switch in Java
# match the op and execute
# Python > 3.10


# Write a program to ask the user which browser he want to run automation.

browser =input("Enter the browser\n")
match browser:

    case "firefox":
        print("Firefox")
    case "chrome":
        print("Chrome !")
    case "edge":
        print("edge !")
    case "safari ":
        print(("safari !"))
