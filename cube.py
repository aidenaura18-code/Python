def cube(number):
   return number*number*number
def three_times(number):
   if number%3==0:
      return cube(number)
   else:
    return False
print(three_times(9))
print(three_times(4))

def add():
   """USE THIS FUNCTION LATER"""
print(add.__doc__)


def count(n):
   if n>0:
      print(n)
      count(n-1)
count(5)