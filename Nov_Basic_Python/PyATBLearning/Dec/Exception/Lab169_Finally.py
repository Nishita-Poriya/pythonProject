try:
    num1=int(input("Enter a number1\n"))
    num2=int(input("Enter nuber2\n"))

    result=num1/num2

except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print("Output is",result)

else:
    print("Output is ",result)

finally:
    print("This code will be always executed ! ")