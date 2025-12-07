cars = ["audi", "honda", "bmw", "fiat", "toyota"]
best = "bmw"
winner = 188
age = 17
x = 566
y = 899

# Conditions
if best == "bmw":
    print("Tiene razón")
else:
    print("Está equivado")

if winner != 188:
    print("Perdiste")
else:
    print("Ganaste")

if age >= 21:
    print("Podés pasar")
elif age > 18:
    print("Te falta poco")
elif age < 18:
    print("Te falta mucho")
elif age <= 13:
    print("Te falta muchisimo")

if x == 565 and y == 899:
    print("SI")
else:
    print("NO")

if x == 565 or y == 899:
    print("SI")
else:
    print("NO")

# Condition in loop
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Case sensitive
car = "Audi"
print(car == "audi")
print(car.lower() == "audi")

# List condition
if "fiat" in cars:
    print("Está Fiat")
else:
    print("No está Fiat")

if "ford" not in cars:
    print("No está Ford")
else:
    print("Si está Ford")

toppings = ["pineapple", "mushroom", "onion", "pepper", "bacon", "cheese"]
requested = ["mushroom", "pepper", "cheese"]

for topping in requested:
    if topping == "pepper":
        print(f"Sorry, we are out of {topping.title()}.")
    else:
        print(f"{topping.title()} added.")

requested = ["mushroom", "apple", "cheese", "orange"]
for topping in requested:
    if topping in toppings:
        print(f"{topping.title()} added.")
    else:
        print(f"Sorry, we don't have {topping.title()}.")


requested = []

if requested:
    for topping in requested:
        print(f"{topping.title()} added.")
else:
    print("Please add toppings.")
