"""
Створити батьківський клас Figure з методами __init__: ініціалізується колір,
__get_color__: повертає колір фігури,
__info__: надає інформацію про фігуру та колір,
від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.
"""


class Figure:
  def __init__(self,figure_color):
    self.color=figure_color
  
  def get_sides(self,sides_quantity):
    self.s=sides_quantity
    self.sides=[float(input("Enter side "+str(i+1)+" : ")) for i in range(self.s)] 

  def get_color(self):
    return self.color

  def square(self):
    return (self.sides[0]**2 if isinstance(self,Square) else self.sides[0]*self.sides[1])

  def info(self):
    print ("This is a Rectangle. The length is {}. The height is {}. The color is {}".format(self.sides[0],self.sides[1],self.color) if isinstance(self,Rectangle) else "This is a Square. The side is {}. The color is {}".format(self.sides[0],self.color))


class Rectangle(Figure):
  def __init__(self,color):
    Figure.__init__(self,color)


class Square(Figure):
  def __init__(self,color):
    Figure.__init__(self,color)
