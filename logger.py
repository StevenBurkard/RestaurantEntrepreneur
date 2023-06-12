class Logger():
    instance = None
    transaction_count = 0
    daily_sales = 0

    @staticmethod
    def get_instance():
        if Logger.instance is None:
            Logger.instance = Logger()
        return Logger.instance
    
    def log_transaction(self, order):
        self.transaction_count += 1
        self.daily_sales += order.price

        with open("log.txt", "a") as file:
            file.write(f"Transaction: {self.transaction_count}, Dish: {order.name}, Restaurant: {order.store}, Price: ${format(order.price)}, Total Sales: ${self.daily_sales}\n")
            file.close()