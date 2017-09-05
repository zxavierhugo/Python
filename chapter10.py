"""
Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the
hour out from the 'From ' line by finding the time and then splitting the
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
"""


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

largest = None
counts = dict()
delimiter = ':'

for line in handle:
    if line.startswith('From '):
        words = line.split()
        hours = words[5].split(delimiter)
        h = hours[0]
        #print(hours[0])
        h = list(hours[0:1])
        #print(h)
        for h in hours[0:1]:
            if h not in counts:
                counts[h] = 1
            else:
            	counts[h] +=1

#print(counts)

t = list(counts.items())
q = t
q.sort()
#print(q)


lst = list()
for key, val in q:
    lst.append((val, key))
    print(key, val)
