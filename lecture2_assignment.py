"""
Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.
"""
a=int(input('Enter first number:\n'))
b=int(input('Enter second number:\n'))
if a>b:
  print("A is bigger than B")
elif a==b:
  print("A equals B")
else:
  print("A is less than B")

"""
Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення. 
"""
a=int(input("Please enter the value:\n"))
print("The number is odd" if(a%2!=0) else "The number is even")

"""
Написати скрипт, який обчислить факторіал введеного числа.
"""
value=int(input("Please enter the value:\n"))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(value))

value=int(input("Please enter the value:\n"))
def fact(n):
    return(1 if n==0 else n*fact(n-1))
print(fact(value))
"""
Написати скрипт, який знайде найбільший спільний дільник НСД та найменше спільне кратне НСК двох чисел.
"""
first_value=int(input('Enter the value A:'))
second_value=int(input('Enter the value B:'))
user_values=(first_value,second_value)
for i in range(1,user_values[0]+1)[::-1]:
  if user_values[0]%i==0 and user_values[1]%i==0:
    print("The greatest common divisor for values %s and %s is %s"%(user_values[0],user_values[1],i))
    break
i=1
while i*max(user_values)<=first_value*second_value:
  if i*max(user_values)%min(user_values)==0:
    print("The least common multiple for values %s and %s is %s"%(user_values[0],user_values[1],i*max(user_values)))
    break
  i+=1
