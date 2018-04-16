#programs calculates the sum of all numbers of list except 5 and breaks loop if 0
print("Enter numbers seperated by space:")
list=[int(x) for x in input().split()]
sum=0
for i in list:
    if i==5: continue
    if i==0: break
    sum+=i
print("\nSum: ",sum)
