person=('Birju Vachhani',21) #tuple packing
(name, age)=person #tuple unpacking
print(name)
print(age)

a=(5,6)
b=(5,7)
#tuple comparison
if a>b:
    print('a is bigger')
else:
    print('b is bigger')

c=(1,2,3,4,5,6,7)
print(c[1:5]) #tuple slicing

#tuple as dictionary key
d={('birju','vachhani'):1403701160655}
print(d[('birju','vachhani')])