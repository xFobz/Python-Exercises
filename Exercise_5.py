sentence = list(input("Type a sentence to find out whether it is a palindrome: "))
length = int(len(sentence))
half = int(length / 2)

if length % 2 > 0:
    sentence.pop(half)

print (half)
list1 = sentence[0:half]
list2 = sentence[half:]
list2 = list2[::-1]
print (list1, list2)
if list1 == list2:
    print ("palindrome")
else:
    print ("not palindrome")


