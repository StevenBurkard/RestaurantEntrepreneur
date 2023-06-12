from order_factory import OrderFactory
from logger import *

class Franchise:
    def __init__(self, name):
        self.name = name
    
    def place_order(self):
        choice = input("\nWhat would you like to order? >")
        order = OrderFactory.create_order(choice)
        
        if order is None:
            print("***Sorry there was an error with your order..***")
        else:
            logger = Logger.get_instance()
            logger.log_transaction(order)
    
    
        
        