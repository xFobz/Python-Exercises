name = input("What is your name? ")
age = input("How old are you? ");
age = int(age)
cent = 2017 - age + 100
line = ('Hi %s, you are %s which means you will turn 100 in %s' % (name, age, cent))
print (line)
repeat = input("Would you like to print that line again? Y/N: ")
if repeat == 'Y' or repeat == 'y':
    times = input("how many times would you like to print it? ")
    times = int(times)
else:
    print ("Bye")
for x in range(0, times):
    print (line)
