sentence = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'
words=sentence.split()
unique_words=set(words)#creating set from list
print('creating set from list')
print(unique_words)

a = {1,3} #defining set
print(a)

#adding item in set
print('adding item in set')
a.add('hello')
print(a)

#adding multiple items in set
print('adding multiple items in set')
a.update([1,2,3])
print(a)

#removing item from set
print('removing item from set')
a.discard(4)
print(a)

#poping item from set
print('poping item from set')
print(a.pop())

#clearing set
print('clearing set')
a.clear()
print(a)


s1 = {1,2,3,4}
s2 = {3,4,5,6}

#set union
print('Set Union')
print(s1 | s2)
print(s1.union(s2))

#set intersection
print('Set Intersection')
print(s1 & s2)
print(s1.intersection(s2))

#set difference
print('Set Difference')
print(s1 - s2)
print(s1.difference(s2))

#set symmetric difference
print('Set Symmetric Difference')
print(s1 ^ s2)
print(s1.symmetric_difference(s2))