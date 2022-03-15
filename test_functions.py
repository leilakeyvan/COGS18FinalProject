"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import buy_snack, restock, get_total_money
##
##

def test_buy_snack():

    assert callable (buy_snack)
    assert buy_snack(5) >= 1

def test_restock():

    assert callable (restock)
    assert restock() == str
    assert restock(0) == 'restock needed-item not available at this time'
    
def test_get_total_money():

    assert callable (get_total_money)
    assert get_total_money() == int



                 
    