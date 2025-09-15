### Data ###


recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}


resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}




### Complete functions ###


class SandwichMachine:


    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources


    def check_resources(self, ingredients):
        """Checks if there are enough resources for the sandwich"""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True


    def process_coins(self):
        """Calculates total money from coins inserted"""
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: ")) * 1.0
        half_dollars = int(input("how many half dollars?: ")) * 0.5
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        return dollars + half_dollars + quarters + nickels


    def transaction_result(self, coins, cost):
        """Check if inserted coins cover the sandwich cost"""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, not enough money. Money refunded.")
            return False


    def make_sandwich(self, sandwich_size, ingredients):
        """Deduct resources and make the sandwich"""
        for item in ingredients:
            self.machine_resources[item] -= ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


    def report(self):
        # Show resources
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounce(s)")


### Make an instance of SandwichMachine class and write the rest of the codes ###


#Instance of SandwichMachine
machine = SandwichMachine(resources)


running = True
while running:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()


    if choice == "off":
        running = False
    elif choice == "report":
        machine.report()
    elif choice in recipes:
        sandwich = recipes[choice]
        # checking resources
        if machine.check_resources(sandwich["ingredients"]):
            # processing coins
            money = machine.process_coins()
            # check transaction
            if machine.transaction_result(money, sandwich["cost"]):
                # make sandwich
                machine.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid option.")
