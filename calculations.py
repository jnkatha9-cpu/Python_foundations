#ask user for the first number
num1=float(input("enter the first number:"))
#ask user for the second number
num2=float(input("enter the second number:"))
#ask user for the operation to be performed
operation=input("enter the operation to be performed (+,-,*,/):")
#perform the operation based on user input
if operation=="+":
   print(num1+num2)
elif operation=="-":
   print(num1-num2)
elif operation=="*":
   print(num1*num2)
elif operation=="/" :
   print(num1/num2)
else:
   print("invalid operation")