print("Hello, my name is Raya your virtual assistant. I will help you order a pizza!")
print("I will ask you a few questions about your pizza preferences press enter after you type your choice")
userName = input("\nEnter your name:  ")
print(f"\nHello, {userName}. Nice to meet you!")

size = input("\nWhat size do you want?  Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
toppings = input("\nEnter your toppings:  ")
crustType = input("\nWhat type of crust do you:  ")
quantity = input("\nHow many of these do you want to order?  Enter a numeric value:  ")
quantity = int(quantity)
method = input("\nIs this for carry out or delivery:  ")

salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax
print(f" Thank you, {userName}, for you order.")
print(f"Your {quantity} {size} {flavor} {toppings} pizza(s) with {crustType} crust costs ${total:,.2f}.")
print("-" * 10)
