print("Hello, my name is Raya your virtual assistant. I will help you order a pizza!")
print("I will ask you a few questions about your pizza preferences press enter after you type your choice")
userName = input("\nEnter your name:  ")
if userName.lower() == "brenda dixon":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
print(f"\nHello, {userName}. Nice to meet you!")

size = input("\nWhat size do you want?  Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
toppings = input("\nEnter your toppings:  ")
crustType = input("\nWhat type of crust do you:  ")
quantity = input("\nHow many of these do you want to order?  Enter a numeric value:  ")
quantity = int(quantity)
method = input("\nIs this for carry out or delivery:  ")
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0

salesTax = 1.1
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
total = (pizzaCost * quantity) * salesTax + deliveryFee
print(f" Thank you, {userName}, for you order.")
print(f"Your {quantity} {size} {flavor} {toppings} pizza(s) with {crustType} crust costs ${total:,.2f}.")
print("-" * 10)
print(f"Thank you, {userName}, for you order.")
print("Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
if total >= 50:
    print("\nCongratulations! You've been awarded a $10 Off coupon for your next order.")
else:
    print("\nOrder over $50 will receive a free $10 Off coupon!")
print("-" * 10)
