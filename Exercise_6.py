sentence = list(input("Type a sentence to find out whether it is a palindrome: "))
length = int(len(sentence))
half = int(length / 2)

print (half)
list1 = sentence[0:half]
list2 = sentence[half:]

print (list1, list2[::-1])


