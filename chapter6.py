"""
Write code using find() and string slicing (see section 6.10)
to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475";
semicolon = text.find(":")
print(semicolon)

firstnumber = text.find("0", semicolon)
print(firstnumber)

number = text[int(firstnumber):]
print(float(number))

#----
#Practice
"""
name = 'Adrian'
index = 0
print(len(name))
while index < len(name):
    letter = name[index]
    print(letter)
    index = index + 1
    print(index)


person = 'Jamaica'
length = len(person)-1
print(length)
while length >= 0:
    backward = person[length]
    print(backward)
    length = length - 1

for char in name:
    print(char)

fruit = 'banana'
print(fruit[:])

#Replace the certain letter with other letter
greeting = 'Hello my world!'
new_greeting = 'J'+greeting [1:]
print(new_greeting)
print(greeting)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

def count():
    step = 0
    letter = input('> ')
    for word in letter:
        step = step + 1
    print(step)
count()

word = 'banana'
index = word.find('n')
print(index)
new_word = word.upper()
print(new_word)

data = 'From peter.fever@gmail.com Sat Jan 3 09:12:16 2017'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1: sppos]
print(host)
"""
