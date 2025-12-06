# Basic
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Loop
for dimension in dimensions:
    print(dimension)

# Re-assign
print(dimensions)
dimensions = (400, 200, 500, 200)
print(dimensions)

# Methods
print(dimensions.count(200))
print(dimensions.index(200))
