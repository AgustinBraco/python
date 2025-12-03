# Basic
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first = list[0]
second = list[1]
penultimate = list[-2]
last = list[-1]

print(list)
print(first)
print(second)
print(penultimate)
print(last)

# Modify
list[0] = 10
list[-2] = 100
print(list)

# Add
list.append(50)
list.append(-10)
print(list)

list.insert(0, 330)
list.insert(5, -30)
list.insert(400, 2)
print(list)

# Delete
del list[0]
del list[-1]
print(list)

last_item = list.pop()
third_item = list.pop(2)
print(last_item)
print(third_item)
print(list)

list.remove(10)
print(list)

# Sort
list.sort()
print(list)

list.sort(reverse=True)
print(list)

sorted_list = sorted(list)
print(sorted_list)

reverse_sorted_list = sorted(list, reverse=True)
print(reverse_sorted_list)

# Reverse
list = [1, 3, 10, 50, 200, 12]
print(list)

list.reverse()
print(list)

# Length
list_length = len(list)
print(list_length)
