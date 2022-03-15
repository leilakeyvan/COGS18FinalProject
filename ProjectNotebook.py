#!/usr/bin/env python
# coding: utf-8

# # Project Description

# ##### Write a brief description of your project here. 
# 
# ##### Note that projects should be self-sufficient, so make sure to provide enough information and context here for someone to understand what you are doing in your project, and why. 
# 
# This code will execute a vending machine concept where an input is received by the machine after the human interacts with the keypad (enters a certain number/letter code). The desired item will be specified by the human inputting a column and row (columns indicated by number, row indicated by letter) into the machine. When the input is received, the machine will check the stock/inventory of the specified item and will check to make sure the human has inserted enough cash. If both checks go through, the human will receive their item. The machine will keep track of item inventory/stock, name, price, and the total amount of money the machine has collected from purchases made.

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


from my_module.functions import buy_snack, restock, get_total_money
from my_module.classes import Vend


# In[2]:


# Do a bunch of things.
item_0 = {'name' : 'gummy bears', 'price' : 1.75, 'how many available' : 10}
item_1 = {'name' : 'skittles', 'price' : 1.50, 'how many available' : 7}
item_2 = {'name' : 'granola bar', 'price' : 2.00, 'how many available' : 14}
item_3 = {'name' : 'doritos', 'price' : 1.75, 'how many available' : 4}
item_4 = {'name' : 'gum', 'price' : 1.00, 'how many available' : 9}
item_5 = {'name' : 'gatorade', 'price' : 2.50, 'how many available' : 6}
item_6 = {'name' : 'water', 'price' : 1.65, 'how many available' : 10}
item_7 = {'name' : 'pop-tarts', 'price' : 2.15, 'how many available' : 11}
item_8 = {'name' : 'coca-cola', 'price' : 1.05, 'how many available' : 13}
item_9 = {'name' : 'sprite', 'price' : 1.05, 'how many available' : 15}
                
def dispense(userinput):

    if userinput == '1A':
        return 0

    if userinput == '1B':
        return 1

    if userinput == '2A':
        return 2

    if userinput == '2B':
        return 3

    if userinput == '3A':
        return 4

    if userinput == '3B':
        return 5

    if userinput == '4A':
        return 6

    if userinput == '4B':
        return 7

    if userinput == '5A':
        return 8

    if userinput == '5B':
        return 9
            
class Vend():
    
    def __init__(self):
        self.inventory = [item_0, item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9]
        self.money_in_machine = 0

    def buy_snack(self, cash):    
        select_item = input('item position: ')

        index = dispense(select_item)
        
        if self.inventory[index]['how many available'] >= 0 and self.inventory[index]['price'] <= cash:
            change = cash - self.inventory[index]['price']
            self.money_in_machine += self.inventory[index]['price']
            self.inventory[index]['how many available'] -= 1
            return change
            
        else:
            print('not available or need more cash')    
            
    def restock(self, inventory):

        if 'how many available' == 0 in self.inventory:
            print('restock needed-item not available at this time')
        else:
            print('in stock')
    
    def get_total_money(self):
        return self.money_in_machine
    


# In[3]:


# test it out
test = Vend()
print(test.buy_snack(5))
print(test.buy_snack(10))
print(test.get_total_money())


# In[5]:


def test_buy_snack():

    assert callable (buy_snack)
    assert buy_snack(5) >= 1


# In[8]:


def test_restock():

    assert callable (restock)
    assert restock() == str
    assert restock(0) == 'restock needed-item not available at this time'


# In[10]:


def test_get_total_money():

    assert callable (get_total_money)
    assert get_total_money() == int


# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. I had no experience at all with coding coming into this class. I was interested in learning about a coding language, and this class provided such a positive learning environment for me to explore something I had interest in. Thank you for being an amazing teacher with such a upbeat attitude, Professor Ellis! Also, thank you to all of the TAs in this course, they were very helpful and encouraging.
# 2. I thought it was very difficult to come up with my own concept and implement different functions and classes that would allow for my idea to come to life. I started out with a much larger idea that became way too complicated, so I had to restart the project about 5 times. Luckily, I was able to find a way to execute one of the ideas I had (coded above). Although it may be short, I am proud of what my brain was able to figure out through this whole process. I realize there are probably several projects involving programming a vending machine out in the world since I think it is a fun concept to work with! However, I wanted to be able to come up with the ideas for the functions on my own and did not want to be tempted to duplicate someone else's code, so I ended up not using any resources outside of class notes to aid in my function and method building.
