
#Biggest of two numbers
'''
num1 = int(input('Enter a number : '))
num2 = int(input('Enter another number : '))

if num1==num2:
    print ('Both numbers are same')
elif num1 > num2:
    print (num1 , 'is greater than' , num2)
else:
    print (num2 , 'is greater than' , num1)

'''

#Biggest of three numbers

"""
num1 = int(input('Enter a number : '))
num2 = int(input('Enter a second number : '))
num3 = int(input('Enter a third number : '))

if num1==num2 and num2==num3:
    print ('All numbers are same')
elif num1 > num2 and num1 > num3:
    print (num1 , 'is greater than' , num2, '&' , num3)
elif num2 > num1 and num2 > num3:
    print (num2 , 'is greater than' , num1, '&' , num3)
elif num3 > num2 and num3 > num1:
    print (num3 , 'is greater than' , num1, '&' , num2)

"""

choice = int(input('Enter a Number : '))

match choice:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('invalid Entry')

