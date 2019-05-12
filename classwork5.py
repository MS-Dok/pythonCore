#1. Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.
def average(*args):
  return sum(args)/len(args)
print(average(1,2,3))

#2. Написати функцію, яка повертає абсолютне значення числа
def absolute(a):
  return (a if a>=0 else a*-1)
print(absolute(5))

#3. Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.

def max_min_ident(a,b):
  """
  Function returns the max value from both numbers
  """
  return (max(a,b))

print(max_min_ident(9,-5))

# 4. Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
def square_round():
  radius=int(input("Enter the radius: "))
  return 3.14*(radius**2)

def square_triangle():
  height,side=int(input("Enter the height: ")),int(input("Enter the side: "))
  return(0.5*height*side)

def square_square():
  a,b=int(input("Enter the first side: ")),int(input("Enter the second side: "))
  return a*b

def square_calc(choise):
  """
  Enter 1 for round square, 2 for triangle square, 3 for rectangle square calculation
  """
  if choise==1:
    print(square_round())
  elif choise==2:
    print(square_triangle())
  else:
    print(square_square)

square_calc(int(input("Enter the choise from 1 to 3: ")))

#5. Написати функцію, яка обчислює суму цифр введеного числа.
def calculate_number_amount():
  value=input("Enter the value: ")
  print(sum([int(x) for x in value]))

calculate_number_amount()

#6. Написати програму калькулятор, яка складається з наступних функцій:

#головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!
def calc_prog():
  operations=['-','+','/','*','%','exit']
  while True:
    oper=input('Please enter the operation or print \'exit\' to quit: ')
    if oper not in operations: 
      print("Unsopported operation, please use one of the available ones: {}".format(list(oper)))
    elif oper=='exit':
      print('Thank you for using this product')
      exit()
    else:
      break
  a,b=float(input('Please enter the first value: ')),float(input('Please enter the second value: '))
  operation_dictionary={
  "+": a+b,
  "-": a-b,
  "/": a/b,
  "*": a*b,
  "%": a%b
  }
  if b==0 and oper=="/":
    print('Division by 0')
    exit()
  else:
    print("A %s B = %s" % (oper,operation_dictionary.get(oper)))
  calc_prog()

calc_prog()

