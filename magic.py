import random
number = [random.randint (0,10), random.randint(0,10)]
def magic_number():
    num = int(input('enter your lucky number :'))
    if num in number:
        return 'you are a lucky '
    else:
        return 'better luck next time '
     
def input_number(attempt):
       for chance in range(1,attempt+1):
        print( 'this is your {} attempt'.format(chance))
        print(magic_number())

attempt = int(input("enter the number of attempt : "))
input_number(attempt)