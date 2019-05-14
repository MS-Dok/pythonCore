'''
Create a robot that will always win the game. Your robot will always go first. 
The function should take an integer and returns 1, 2, or 3.
'''
def make_move(sticks):
    return sticks%4 if sticks>=3 else sticks
