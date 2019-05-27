"""1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні."""

try:
  print("Odd" if int(input("Please enter the integer: "))%2!=0 else "Even")
except ValueError:
  print("It is not integer value")
  
"""
2.  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом. Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію. Головний код має викликати функцію, яка обробляє введену інформацію.
"""
class CustomError(Exception): 
  def __init__(self, data): 
      self.data = data
  def __str__(self):
      return repr(self.data)


while True:
  try:
    a=int(input("Please enter the age: "))
    if a<0:
      raise CustomError("Age cannot be less than 0")
  except CustomError as e:
    print("The error: ", e.data)
  else:
    print("Odd" if a%2!=0 else "Even")
    break

'''
3. Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та finaly.
'''
while True:
  try:
    a,b=eval(input("Please enter the two numbers separated by \",\":\n"))
  except TypeError:
    print("Incorrect format. Entered float instead of 2 numbers separated by comma")  
  except SyntaxError:
    print("Incorrect format. No values or values are not separated by \",\"")
  except Exception:
    print("Da hell is this?")
  else:
    try:
      print("{}/{} equals {}".format(a,b,a/b))
    except ZeroDivisionError:
      print("devision by 0 is not acceptable")
    else:
      break
  finally:
    print("The program has been completed")
'''
4. Написати програму, яка аналізує введене число та в залежності від числа видає день тижня, який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.
'''
class CustomError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)
days=["Monday","Tuesday","Wednesday",'Thursday',"Friday","Saturday","Sunday"]
while True:
  try:
    print (days[int(input("Please enter the number of the week's day from 1 to 7: \n"))-1])
  except TypeError:
    print('Please enter the number')
  except IndexError:
    print("Enter the value from 1 to 8")
  except ValueError:
    print("You have not entered anything")
  else:
    break