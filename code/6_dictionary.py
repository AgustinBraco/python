alien_0 = {"color": "green", "points": 5}

print(alien_0)
print(alien_0["color"])
print(alien_0["points"])

alien_0["x"] = 0
alien_0["y"] = 25

print(alien_0["x"])
print(alien_0["y"])
print(alien_0)

alien_0["x"] = 25
print(alien_0["x"])
print(alien_0)

# Modify
alien_1 = {}
alien_1["color"] = "red"
alien_1["points"] = 30
alien_1["x"] = 25
alien_1["y"] = 25
alien_1["speed"] = "medium"

print(f"Alien 1 current position is: x{alien_1['x']}, y{alien_1['y']}")

if alien_1["speed"] == "slow":
    increment = 1
elif alien_1["speed"] == "medium":
    increment = 2
else:
    increment = 3

alien_1["x"] = alien_1["x"] + increment
print(f"Alien 1 new position is: x{alien_1['x']}, y{alien_1['y']}")


# Delete
del alien_1["color"]
print(alien_1)

# Method: Get
alien_0_speed = alien_0.get("color", "No color assigned")
alien_1_speed = alien_1.get("color", "No color assigned")
print(alien_0_speed)
print(alien_1_speed)

# Loops
user_0 = {
    "id": 0,
    "first_name": "Juan",
    "last_name": "Perez",
    "birthday": "01-01-1999",
}

# Methods: Items, Keys, Values, Set
for key, value in user_0.items():
    print(key, value)

for key in user_0.keys():
    print(key)

for key in user_0:
    print(key)

friends = ["Juan", "Sara", "Daniel", "Maria", "Jose", "Marcos", "Tadeo"]

completed = {
    "Juan": True,
    "Sara": True,
    "Maria": True,
    "Marcos": True,
}

for friend in sorted(friends):
    if friend not in completed:
        print(f"{friend.title()}, please complete the poll")
    else:
        print(f"{friend.title()}, thank for complete the poll")

poll = {
    "Tadeo": False,
    "Juan": True,
    "Sara": True,
    "Daniel": False,
    "Maria": True,
    "Jose": False,
    "Marcos": True,
    "Ciro": False,
    "Juana": False,
}
counter_fill = 0
counter_empty = 0

for status in poll.values():
    if status:
        counter_fill = counter_fill + 1
    else:
        counter_empty = counter_empty + 1

print(f"There're {counter_fill} completed polls and {counter_empty} pending")

languages_set = {
    "Pyhton",
    "Javascript",
    "Typescript",
    "Pyhton",
    "C",
    "Java",
    "Pyhton",
    "Javascript",
    "Javascript",
}

languages = {
    "Tadeo": "Pyhton",
    "Juan": "Javascript",
    "Sara": "Typescript",
    "Daniel": "Pyhton",
    "Maria": "C",
    "Jose": "Java",
    "Marcos": "Pyhton",
    "Ciro": "Javascript",
    "Juana": "Javascript",
}

print(languages)
print(languages_set)

for language in set(languages.values()):
    print(f"Language: {language}")

# Nest
# Dictionary in list
aliens = []

for id in range(1, 31):
    if id >= 1 and id <= 10:
        aliens.append({"id": id, "color": "green", "points": 10})
    elif id >= 11 and id <= 20:
        aliens.append({"id": id, "color": "yellow", "points": 20})
    else:
        aliens.append({"id": id, "color": "red", "points": 30})

print(aliens)

# List in dictionary
languages = {
    "Tadeo": ["Pyhton", "Javascript"],
    "Juan": ["Javascript", "Typescript"],
    "Sara": ["Typescript", "C"],
    "Daniel": ["C", "Pyhton"],
    "Maria": ["C", "Typescript"],
    "Jose": ["Java", "Python"],
    "Marcos": ["Javascript", "Pyhton"],
    "Ciro": ["Typescript", "Javascript"],
    "Juana": ["Javascript", "C"],
}

for key, value in languages.items():
    print(f"{key.title()} favorite languages are:")
    for language in value:
        print(f"\t{language.title()}")

# Dictionary in dictionary
users = {
    0: {"first_name": "Juan", "last_name": "Perez", "location": "San Juan"},
    1: {"first_name": "Maria", "last_name": "Gomez", "location": "Corrientes"},
}

for key, value in users.items():
    print(f"User {key}:")
    print(
        f"Name: {value['first_name']} {value['last_name']}\nLocation: {value['location']}"
    )
