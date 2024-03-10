import numpy as np

msg = "Roll a dice"
print(msg)

print(np.random.randint(1,9))

print('What is your name?')
myName = input()
print('It is good to meet you, {}'.format(myName))
