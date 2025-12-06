# Basic
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first = numbers[0]
second = numbers[1]
penultimate = numbers[-2]
last = numbers[-1]

print(numbers)
print(first)
print(second)
print(penultimate)
print(last)

# Modify
numbers[0] = 10
numbers[-2] = 100
print(numbers)

# Add
numbers.append(50)
numbers.append(-10)
print(numbers)

numbers.insert(0, 330)
numbers.insert(5, -30)
numbers.insert(400, 2)
print(numbers)

# Delete
del numbers[0]
del numbers[-1]
print(numbers)

last_item = numbers.pop()
third_item = numbers.pop(2)
print(last_item)
print(third_item)
print(numbers)

numbers.remove(10)
print(numbers)

# Sort
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

sorted_list = sorted(numbers)
print(sorted_list)

reverse_sorted_list = sorted(numbers, reverse=True)
print(reverse_sorted_list)

# Reverse
numbers = [1, 3, 10, 50, 200, 12]
print(numbers)

numbers.reverse()
print(numbers)

# Length
numbers_length = len(numbers)
print(numbers_length)

# Loop
for number in numbers:
    print(number)

for value in range(6):
    print(value)

for index, value in enumerate(["Honda", "Suzuki", "Yamaha"]):
    print(value, index)

# Range
numbers = list(range(1, 5))
numbers_2 = list(range(6))
numbers_3 = list(range(2, 10))
numbers_4 = list(range(0, 13, 2))
print(numbers)
print(numbers_2)
print(numbers_3)
print(numbers_4)

numbers = []
for number in range(1, 11):
    numbers.append(number**2)

print(numbers)

# Comprehension list
numbers = [number**2 for number in range(1, 11)]
print(numbers)

# Statistics
lowest = min(numbers)
highest = max(numbers)
total = sum(numbers)

print(lowest)
print(highest)
print(total)

# Slice
print(numbers[0:3])
print(numbers[:])
print(numbers[3:])
print(numbers[:3])
print(numbers[-3:])
print(numbers[:-3])
print(numbers[0:8:2])

for number in numbers[:4]:
    print(number)

# Copy
numbers_ref = numbers
numbers_copy = numbers[:]

numbers.append(222)
numbers_ref.append(333)
numbers_copy.append(444)

print(numbers)
print(numbers_ref)
print(numbers_copy)
