my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorate food are:")
print(my_foods)

print("\nMy friend's favorate foods are:")
print(friend_foods)

print("The first three items in the list are:\n" + str(my_foods[0:3]))
print("The first three items in the list are:" )
for item in my_foods[0:3]:
    print(item)
print(my_foods)
print(friend_foods)
my_foods.append("kele")
friend_foods.append("kele")
print("My favorate food are:")
for food in my_foods:
    print(food)

print("My friend's favorate are:")
for food in friend_foods:
    print(food)
