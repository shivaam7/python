#!/usr/bin/env python
# coding: utf-8

# # Random Passsword Generator

# In[ ]:


import random
print('Welcome to your password generator')
chars='abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ!@#$%^&*().,'
number = input('Amount of passwords you want to generate: ')
number = int(number)
length = input('Input your password length: ')
length = int(length)

print('\n here are your passwords:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)


# In[ ]:





# In[ ]:





# In[ ]:




