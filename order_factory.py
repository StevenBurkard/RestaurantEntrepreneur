from order import *

class OrderFactory:
    @staticmethod
    def create_order(order_type):
        order_type = order_type.lower()
        if order_type == "pizza":
            return Pizza()
        elif order_type == "pasta":
            return Pasta()
        elif order_type == "salad":
            return Salad()
        else:
            print("\n***Sorry, we only have Pizza, Pasta, or Salad***")
            return None