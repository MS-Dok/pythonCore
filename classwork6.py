'''
1. Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання.
(для виконання завдання необхідно імпортувати модуль random, а з нього функцію randint())
'''

from random import randint
val=randint(1,100)
while True:
    user_value=int(input("Please enter the value "))
    if user_value > val:
        print("The value is lower")
    elif user_value < val:
        print("The value is higher")
    else:
        print("EXACTLY!")
        break
		
'''2. Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2.
(для виконання завдання необхідно імпортувати модуль math, а з нього функцію pow() та значення змінної пі).'''

from math import pi
from math import pow

def square_calc():

  user_input=int(input("Please enter \'1\' for triangle square calculation. \'2\' - for circle square and \'3\' for calculating a rectangle square: "))
  if user_input==1:
    triangle_square()
  elif user_input==2:
    circle_square()
  elif user_input==3:
    rectangle_square()
  else:
    print("Unsupported operation")


def triangle_square():
  h,a=float(input("Please enter the height: ")),float(input("Please enter the length: "))
  print("The square of triange is {}".format(0.5*h*a))

def circle_square():
  r=float(input("Please enter the radius: "))
  print("The square of circle is {}".format(pi*pow(r,2)))

def rectangle_square():
  a,b=float(input("Please enter a: ")),float(input("Please enter b: "))
  print("The square of rectange is {}".format(a*b))


square_calc()