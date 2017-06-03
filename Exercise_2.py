number = int(input("Input a number: "))
divide = number % 2
divide4 = number % 4
if divide == 0 and divide4 == 0:
    print ("Number is even and is a multiple of 4")
elif divide == 0:
    print ("Number is even")   
else:
    print ("Number is odd")

num = int(input("To check if a number divides evenly into another number input first number: "))
num2 = int(input("Input second number: "))

res = num2 % num

if res == 0:
    print ("It divides evenly")
else:
    print ("It does not divide evenly")
