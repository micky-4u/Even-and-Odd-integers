# Even and Odd integer detecter 

#getting value from the user
num  = int(input("Please enter an integer Value: "))

# find the remainder when divided by 2
# 0 implies even
# 1 inplies odd
if (num % 2)==0: 
    print(str(num)+ " is an even number")
else:
    print(str(num)+ "  is an odd number")
