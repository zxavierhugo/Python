"""
Open the file mbox-short.txt and read it line by line. When you find a line
that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second
word in the line (i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From: '):
        words = line.split()
        print(words[1])
        count = count+1

print("There were", count, "lines in the file with From as the first word")





"""
Open the file romeo.txt and read it line by line. For each line, split the
line into a list of words using the split() method. The program should build
a list of words. For each word on each line check to see if the word is
already in the list and if not append it to the list. When the program
completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt

"""
fh = open(fname)
lst = list()
for line in fh:
    word= line.rstrip().split()
    for element in word:
        if element in lst:
            continue
        else :
            lst.append(element)
lst.sort()
print (lst)


"""
Open the file mbox-short.txt and read it line by line. When you find a line
that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the
line (i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""



"""
Write a function called chop that takes a list and modifies it, removing the
first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list
that contains all but the first and last elements.
"""

def chop(t):
    t = t[1:-2] #using the same list

test = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
phrase = chop(test)
print(test)
print(phrase) # should return none cos there is no new list

"""
Then write a function called middle that takes a list and returns a new list
that takes a list and returns a new list that contains all but the first
and the last elements.
"""

def tail(t):
    return t[1:-2] #must put in return in order to provide new list

letters = ['c', 'd', 'e', 'f', 'g', 'i', 'j']
rest = tail(letters)
print(letters) #original list
print(rest) #new list because u use return


"""
t1 = ['a','b','c']
t2 = ['d','e']
t1.extend(t2)
print(t1)
print(t2)

numlist = list()
while(True):
    inp = input('Enter a number: \n')
    if inp == 'done':
        break:
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average: ',average)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

a = [1, 2, 3]
b = a
print(b is a)
"""
