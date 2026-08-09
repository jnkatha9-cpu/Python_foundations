#ask the user for a number
number=int(input("enter a number:"))
#start total at 0
total=0
#add numbers from 1 to the given number
for i in range(1,number + 1):
    total = total + i
#diplay the result
print("the sum is:", total)
