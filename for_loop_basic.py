for i in range(0, 151):
    print(i)

print("----")

for i in range(5, 1001, 5):
    print(i)

print("----")

for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

print("----")

odd_sum = 0
for i in range(0, 500000, 2):
    odd_sum = odd_sum + i
print("The sum of the odd numbers from 1 to 500000 is", {odd_sum})

print("----")

for i in range(2018, 0, -4):
    print(i)

print("----")

lowNum = 2
highNum = 10
mult = 3
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)
    else:
        print("Not a multiple of 3!")

