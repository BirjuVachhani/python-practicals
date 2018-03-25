n=int(input('Enter a numer to print fibonacci series:'))
print(n)
first=1
second=0
fibonacci_series = list() 
for _ in range (0,n):
    x=first+second
    fibonacci_series.append(x)
    first=second
    second=x

print(fibonacci_series)
