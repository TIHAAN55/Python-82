def greet_customer():
    print("Welcome to our lemonade stand!")
greet_customer()

price = 2
cups = int(input("Enter cups you want."))

def cost():
    print("$", price*cups, "is your cost.")
    print()
    print()
cost()

def reciept():
    print("RECIEPT/BILL")
    print("Total cost: ", "$", price*cups)
    print("Total cups: ", cups)
    print("Thank you for buying from our stand!")
reciept()