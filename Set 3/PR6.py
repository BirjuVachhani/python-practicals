sentence = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'
words=sentence.split()
word_count=dict()
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print('word occurances:')
for key,value in word_count.items():
    print('{}\t{}'.format(key,value))
