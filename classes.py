"""Classes used throughout project"""
class Vend():
# the entire vending process: from number/letter input to checking the stock status of an item
# to the cash exchange with the human to the machine's counting of money collected overall
    
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
    