""""""
#5.2 Write a program that repeatedly prompts a user for integer numbers
#until the user enters 'done'. Once 'done' is entered, print out the
#largest and smallest of the numbers. If the user enters anything other
#than a valid number catch it with a try/except and put out an appropriate
#message and ignore the number.
#Enter the numbers from the book for problem 5.1 and
#Match the sample output below.
""""""

def calculator():
    total = 0
    count = 0
    while True:
        num = input('> ')
        if num == 'done':
            print (total, count, (total / count))
            break
        else:
            try:
                total += float(num)
            except:
                print ('Invalid input')
                continue
        count += 1
calculator()

#-----
"""
#Practise
friends = ['Adrian', 'Peter']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

count = 0
for it in [3,2,1,4,2,53, 54]:
    count = count + it
print ('Count:', count)

largest = None
print('Before:', largest)
for itv in [3, 19, 2, 10, 52, 4]:
    if largest is None or itv > largest:
        largest = itv
    print('Loop', itv, largest)
print('Largest', largest)

smallest = None
print('Before:', smallest)
for itv in [32, 19, 2, 10, 52, 4, 39]:
    if smallest is None or itv < smallest:
        smallest = itv
    print('Loop', itv, smallest)
print('Smallest', smallest)
""""
