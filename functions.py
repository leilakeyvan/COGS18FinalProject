"""A collection of function for doing my project."""

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
# number/letter combination assignments to snacks

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
    
def __init__(self):
    self.inventory = [item_0, item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9]
    self.money_in_machine = 0

def buy_snack(self, cash):

    """Check and alter the inventory of an item after purchase as well as make
    sure enough cash has been received bu the human for the item selected. 

Parameters
----------
cash : int
    The amount of money given to the machine by the human.

Returns
-------
change : int
    The result of the 'price' of the item being subtracted from the cash gien by the human.
'not available or need more cash' : str
    The result of not enough money being given by the human or stock equaling zero. 
"""

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

    """Check the stock of an item. 

Parameters
----------
inventory : int
    The amount of a particular item in the machine.

Returns
-------
'in stock' : str
    The result of the stock being above 0.
'restock needed-item not available at this time' : str
    The result of the stock being equal to 0. 
"""

    if 'how many available' == 0 in self.inventory:
        print('restock needed-item not available at this time')
    else:
        print('in stock')
    
def get_total_money(self):

    """Show the total amount of money in the machine. 

Returns
-------
self.money_in_machine : int
    The amount of money that has been collected by the machine from humans buying snacks. 
"""

    return self.money_in_machine
