# 3-1
names=["a","b","c","d"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2
print(f"{names[-1]} is a bitch")
print(f"{names[-4]} is good")

# 3-3
a= "I love to ride motorcycle"
b= "I love to ride car"
c= "I don't like to ride the helecopter"
d= 5665
example=[a,b,c,d]
print(example[0])
print(f"{example[-1]} is my car number")


# 3-4
people= ['A','B','C','D']
print(f'Please come to my dinner {people[0]}')
print(f'Please come to my dinner {people[1]}')
print(f'Please come to my dinner {people[2]}')
print(f'Please come to my dinner {people[3]}')

# 3-5
print(f'Ohho! {people[2]} will not be able to come')
people[2]= 'E'
print(people)

# 3-6
people.insert(0,'X') # Beginning
print(people)
people.insert(3, 'Y') # Middle
print(people)
people.append('Z') # At the end
print(people)

for i in people:
 print(f'Please come to dinner {i}')


# 3-7
people.pop() # Just delete the last component of the list
print(people)
people.pop()
print(people)
del people[0] # The del function should be at first
print(people)

while len(people) > 2:
    people.pop()

print(people)

# 3-8
locations= ["Japan", "Newzealand", "Switzerland", "US", "Madagaskar"]
print(locations)
print(sorted(locations)) # sorted function prevents the list to sort permanently
print(sorted(locations, reverse=True)) # Reverse using sorted function
print(locations)
locations.reverse() # Changing to the reverse of the original order
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# 3-9
people= ['A','B','C','D']
print(len(people))

# 3-10
rivers=["Atrai", "Gorai", "Padma", "Meghna", "Surma"]

print(f"{rivers[3]} is the biggest river") # Index position

rivers.insert(2,"Jamnuna") # Insert at specific position
rivers.append("Kumar") # Insert at last
print(rivers)

del rivers[1] # Delete from specific position
print(rivers)

print(rivers.pop()) # showing the last one which has been deleted ; if I give any position inside the pop it will delete from the specific position
print(rivers) # the list after the pop

print(sorted(rivers)) # Temporarily sort alphabetically the rivers list
print(sorted(rivers, reverse= True)) # Temporarily sort alphabetically in a reverse manner of the rivers
print(len(rivers))

print(rivers)
rivers.reverse() # Permanently reverse the actual order of the list (not alphabetically)
print(rivers)

rivers.sort()
print(rivers) # Permanently sort the list alphabetically

# 3-11
y=[]
print(y[-1]) # Error because there is no item in the list

x=[1,2,3]
print(x[2])
print(x[3]) # Error because in the list there are 3 positions 0,1,2
