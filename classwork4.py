"""1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.
"""
user_value=int(input("Enter the value: "))
print("Min value is",min([x for x in range(user_value)]))
print("Max value is",max([x for x in range(user_value)]))
"""
2.  В інтервалі від 1 до 10 визначити числа 
•  парні, які діляться на 2,
•  непарні, які діляться на 3, 
•  числа, які не діляться на 2 та 3.
"""
user_input_start,user_input_finish=int(input("Please enter the start value ")),int(input("Please enter the end value "))
print(list([x for x in range(user_input_start,user_input_finish) if x%2==0]))
print(list([x for x in range(user_input_start,user_input_finish) if x%3==0]))
print(list([x for x in range(user_input_start,user_input_finish) if x%3!=0 and x%2!=0]))
"""
3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
num_list = [int(input("Enter int {}: ".format(i+1))) for i in range(3)]
"""
while True:
  user_input=int(input("Enter the value: "))
  if user_input>=0:
    break
if user_input==0:
  "Factorial of 0 is equal to 1"
else:
  result=1
  for i in range(1,user_input+1):
    result*=i
  print("Factorial of {} is equal to {}".format(user_input,result))
"""
4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
Якщо логін вірний (First), то привітайте користувача. 
Якщо ні, то виведіть повідомлення про помилку. 
(використайте цикл while)
"""
while True:
  user_input=input("Please enter the login:\n")
  if user_input=="First":
    break
  else:
    print("Incorrect login. Please try again\n") 
"""
5.  Перший випадок. 
Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).
"""
some_array=[]
while True:
  user_input=int(input("Please enter the >0 value "))
  if user_input >0:
    some_array.append(user_input)
  else:
    break
print(some_array)
"""
6.  Другий випадок. 
На початку на вхід подається кількість елементів послідовності, а потім самі елементи. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).
"""
some_array_2=[]
quantity=int(input("Please enter the quantity of numbers "))
i=0
while i<quantity:
  value_to_add=int(input("Please enter the value to add "))
  if value_to_add>0:
    some_array_2.append(value_to_add)
	i+=1
  else:
    print("<=0 value entered. Termination")
    break
print(some_array_2)
"""
7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
(наприклад 10 equals 2 * 5
                    11 is a prime number
                    12 equals 2 * 6
                    13 is a prime number
                    14 equals 2 * 7
                     ………………….)
"""
list_ex=[x for x in range(10,30)]
for i in list_ex:
  if i%2==0:
    print("{} equals 2*{}".format(str(i),int(i/2)))
  elif i%3==0:
    print("{} equals 3*{}".format(str(i),int(i/3)))
  else:
    print(str(i)+" is primal number")

"""
8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)
"""
sentence="На початку на вхід подається кількість елементів послідовності а потім самі елементи."
print(sorted([x for x in set(sentence.lower().split())],key=len))
