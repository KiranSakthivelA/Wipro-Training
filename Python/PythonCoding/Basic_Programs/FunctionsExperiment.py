'''
#function
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

#driver
num1 = int(input('Enter a number : '))
num2 = int(input('Enter another number : '))

print('Add : ',  add(num1,num2))
res = add(n2=num1, n1=num2)
print('Sub : ',  sub(num1,num2))
print('Mul : ',  mul(num1,num2))
'''

'''
#Arbitary
def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


numbers = list()
count = int(input('How many ? '))

for _ in range(1, count + 1):
    numbers.append(int(input('No : ')))


#print(add(numbers))
print(add( *nums: 1,2))
print(add( *nums:1,2,3))
print(add( *nums:1,2,3,4))
'''

'''
#lambda
num1 = int(input('Enter a Number : '))
num2 = int(input('Enter another Number : '))
add = lambda n1, n2 : n1+n2
print(add(num1, num2))
'''

numbers = [1,2,3,4,5,6,7,8,9,10]
sq = lambda nums : [num * num for num in nums if num%2==0]
print(sq(numbers))
