
#Natural Number Printing
'''
num = int(input('Enter a Number : '))

value = 1

while value <= num:
    print(value)
    value += 1
'''

# Armstrong Number

num = input('Enter a number : ')
count = len(num)
sum = 0
ni = int (num)
comp = ni
while ni > 0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni//10


if comp == sum:
    print('It is Armstrong Number')
else:
    print('It is not Armstrong Number')


