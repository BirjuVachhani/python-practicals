print("Enter numbbers separated by space to find average:")
list=[int(n) for n in input().split()]
i=0
sum=0
while i<len(list):
    sum=sum+list[i]
    i+=1
print("\n\nAverage: {}".format(sum/len(list)))
