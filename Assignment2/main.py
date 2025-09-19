import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    print("Welcome to the Ham Sandwich Maker!")

    while True:
        order = input("What size sandwich would you like? (small/medium/large) or 'report' to see ingredients, 'off' to quit: ").lower()

        if order == "off":
            print("Shutting down. Goodbye!")
            break
        elif order == "report":
            print(f"Current resources: {sandwich_maker_instance.machine_resources}")
        elif order in recipes:
            if sandwich_maker_instance.check_resources(recipes[order]["ingredients"]):
                print("Ingredients are available.")
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, recipes[order]["cost"]):
                    sandwich_maker_instance.make_sandwich(order, recipes[order]["ingredients"])
                    print(f"Here is your {order} sandwich. Enjoy!")
                else:
                    print("Sorry, not enough money. Money refunded.")
            else:
                print("Sorry, we do not have enough ingredients for that sandwich.")
        else:
            print("Invalid input. Please choose small, medium, large, report, or off.")

if __name__=="__main__":
    main()