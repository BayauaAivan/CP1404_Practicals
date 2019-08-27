for i in range(1, 21, 2):
    print(i, end=' ')
print()

for a in range(0, 101, 10):
    print(a, end=' ')
print()

for b in range(20, 0, -1):
    print(b, end=' ')
print()

number = int(input("Enter number of stars: "))


for n in range(number):
    print((n+1)*"*")