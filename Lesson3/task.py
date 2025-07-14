# Print Numbers 1 to 10 using both for and while loop
for i in range (1,11,1):
    print(i)

n=int(input("Enter the value of n"))
s=0
for i in range(1,n+1,1):
    s=s+i
print(s)

for i in range(1,11,1):
    print(f"{n} x {i} = {n * i}")
