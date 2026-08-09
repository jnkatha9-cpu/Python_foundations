#ask user for the a number
num=float(input("enter the a number:"))
#ask user how many times to multiply the number
times=int(input("enter how many times to mutiply the number:"))
#calculate the result of mutiplication
for i in range(1,times+1):
    print(num,"x",i,"=",num*i)