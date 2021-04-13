#Basic Calculator

#This function returns a sum
def add(x, y):
    return x + y

#This function returns a subtract
def subtract(x, y):
    return x - y

#This function returns a multiply
def multiply(x, y):
    return x * y

#This function returns a divide
def divide(x, y):
    return x / y

#This function returns the division of an integer
def integer_division(x, y):
    return x // y 

#This function returns a power
def power(x, y):
    return x ** y

#This function returns the module of a division
def module(x, y):
    return x % y

print('Operations available:\n 1.Add\n 2.Subtract\n 3.Multiply\n 4.Divide\n 5.Integer division\n 6.Power\n 7.Module\n')
 
calculator = input('What operation do you want to do (1,2,3,4,5,6,7)? ')

if calculator in ('1','2','3','4','5','6', '7'):
    num1 = float(input('Enter a number:'))
    num2 = float(input('Enter a number:'))

    if calculator == '1':
        print(add(num1, num2))
  
    elif calculator == '2':
        print(subtract(num1, num2))

    elif calculator == '3':
        print(multiply(num1, num2))

    elif calculator == '4':
        print(divide(num1, num2))

    elif calculator == '5':
        print(integer_division(num1, num2))

    elif calculator == '6':
        print(power(num1, num2))

    elif calculator == '7':
        print(module(num1, num2))
    
else:
    print('Invalid input')