"""
Write a program to read through the mbox-short.txt and figure out who has the
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail. The
program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to
find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

largest = None
counts = dict()

for line in handle:
    if line.startswith('From: '):
        words = line.split()
       # print(words[1])
        for word in words:
        	counts[word] = counts.get(word,0) + 1

            #if largest is None or counts[word]
            #	largest = counts[word]
    		#print(counts[word])
 			#if largest is None or counts[word]
        #print(line)
        #print(line.split())
    	#print(words)
    #for word in words:
     #   counts[word] = counts.get(word,0)+1
	#print(counts[word])
#		if largest is None or counts[word] > largest:
#       		largest = counts[word]

#print(word)
print(words[1], counts[word])

"""
word = 'photosynthesis'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print(d)


counts = {'chuck':1, 'anne':43, 'jan':1000}
print(counts.get('jan',3))
print(counts.get('tim',2))

word = 'photosynthesis'
d = dict()
for c in word:
    d[c] = d.get(c,0)+1
print(d)


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)
"""
