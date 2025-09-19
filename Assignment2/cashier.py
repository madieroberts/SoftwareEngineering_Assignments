class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Insert coins:")
        total = 0
        total += int(input("Quarters: ")) * 0.25
        total += int(input("Dimes: ")) * 0.10
        total += int(input("Nickels: ")) * 0.05
        total += int(input("Pennies: ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        else:
            return False