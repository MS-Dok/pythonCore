"""Задано чотирицифрове натуральне число. 
Знайти добуток цифр цього числа.
Записати число в реверсному порядку.
Посортувати цифри, що входять в дане число
"""

value_example=4552
multipl=1
for i in str(value_example):
	multipl*=int(i)
print(multipl)
print(str(value_example)[::-1])
print(''.join(sorted(str(value_example))))