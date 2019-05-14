
'''
Bob is working as a bus driver. 
However, he has become extremely popular amongst the city's residents. 
With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! 
He wants you to write a simple program telling him if he will be able to fit all the passengers. 
'''
def enough(cap, on, wait):
   return (0 if cap-on-wait>=0 else -cap+on+wait)
