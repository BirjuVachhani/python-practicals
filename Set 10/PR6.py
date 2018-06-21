import matplotlib.pyplot as plt

def occurence(str):
    string = str.lower().split()
    dic = {}
    for word in string:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


fhand = open("input.txt","r")
str = fhand.read()
a = occurence(str)
plt.bar(a.keys(),a.values(), align='center', alpha=0.5,color='g')
plt.xlabel('Word')
plt.ylabel('Occurences')
plt.title('Word Occurences')
plt.show()
