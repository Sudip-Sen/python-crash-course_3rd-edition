# 4-1
pizzas= ["a", "b", "c"]
for pizza in pizzas:
    print(pizza)

pizzas.append("pepperoni") # adding another item in the list
for pizza in pizzas:
    print(f'I like {pizza} pizza') # showing in the sentence
    print(f'I often eat {pizza}')
print('I really love pizza') # Outside the loop it is the final sentence

# 4-2
animals= ["Cow", "Goat", "Deer"]
for animal in animals:
    print(f'{animal} eat grass')
print('They all eat grass')

# 4-3
for value in range(1,21):
    print(value) # Just printing 1-20 number

# 4-4 (Doing 500 instead of one million)
num=[]
for value in range (1,501):
    num.append(value)
print(num)

# 4-5
print(min(num)) # Minimum value of the list
print(max(num)) # Max value of the list
print(sum(num)) # Sum of the total list

# 4-6
for value in range(1,21,2):
    print(value)

# 4-7
threes=[]
for value in range (1,11):
    threes.append(value*3)
print(threes)

# 4-8
cubes=[]
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

# 4-9
cubes=[value**3 for value in range(1,11)] # List comprehension
print(cubes)