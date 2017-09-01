
"""
Write a program that prompts for a file name, then opens that file and
reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""

fname = input("Enter file name: ")
fh = open(fname)
text = fh.read()
text2 = text.rstrip()
uppertxt = text2.upper()
print(uppertxt)

"""
Write a program that prompts for a file name,
then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from
each of the lines and compute the average of those values and
produce an output as shown below. Do not use the sum() function or
a variable named sum in your solution.
You can download the sample data at
http://www.py4e.com/code3/mbox-short.txt when you are testing
below enter mbox-short.txt as the file name.
"""

# Use the file name mbox-short.txt as the file name
number = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    count = count + 1
    line1 = line.find(":")
    #print(line1)
    line2 = line.find("0", line1)
    #print(line2)
    line3 = line.rstrip()
    line4 = float(line3[20:])
    #print(line4)
    number = number + line4
    #print(number)
    average = number/count


print("Average spam confidence: " + str(average))



"""
fhand = open('mbox.txt')
print(fhand)

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opeed:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
"""
