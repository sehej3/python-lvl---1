num = int(input("Enter Number : "))
#print(num%3)
#print(num%5)
#print(num%15)

if(num%15==0):
    print("fizzbuzz")

elif(num%5==0):
    print("buzz")

elif(num%3==0):
    print("fizz")

else:
    print("This is not divisible by 3 or 5")
