#input the first number from the user
num1=float(input("enter the first number:"))
#input the second number from the user
num2=float(input("enter the second number:"))
#input the operation to be performed
operation=input("enter the operation to be performed (+,-,*,/):")
#perform the operation based on user input
if operation=="+":
    print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
else:print("invalid operation")
