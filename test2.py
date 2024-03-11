# this is a commented line 

name = "Aliff" # this is an inline comment
age = "27"

# ternary operator 

def is_adult(age):
  if age > 18:
    return True
  else:
    return False

def is_adult2(age):
  return True if age > 18 else False

print(name[:7])

# create a constant
from enum import Enum  
class State(Enum):
  INACTIVE = 0
  ACTIVE = 1 

# Functions

def talk (phrase):
  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)

# talk("I am going to buy the milk")

# Classes 

class Animal:
  def walk(self):
    print("Walking...")

class Dog(Animal):
  # add constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # add a method 
  def bark(self):
    print("woof!")

jason = Dog("Jason", 9)

print(jason.name)
print(jason.age)
jason.bark()
jason.walk()

# Modules 

import math 

print(math.sqrt(4))

# lambda function - single liner function 

multiply = lambda a : a*  2 
print(multiply(5)) #10

# map(), filter(), reduce()

numbers = [1, 2, 3, 4, 5, 6]

result = map(lambda a : a * 2 , numbers)
print(list(result))

result = filter(lambda n : n % 2 == 0, numbers)
print(list(result))

# Recursion 

def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5)) 



