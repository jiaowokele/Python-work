motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(0)
print("The last motocycle I owned was a " + last_owned.title() + ".")
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.\n")

friends = ['Fred winston', 'Steve jobs', 'Kobe Bryant','Li Hua']
print(friends)

print("It is a pity that " + friends[0] + " can not come to th party!")
friends[0] = 'Jerry'
print(friends)
message = "Dear " + friends[3] +", welcome to the party!\n-"
print(message)

print(friends)
print("\nDear friends! I find a big table!")
friends.insert(0,'xiaoqi')
friends.insert(2,'sixmao')
friends.append('kangkang')
print(friends)
print("\nI am sorry to inform that I can only invite two people to dinner!")
popped_friends = friends.pop(2)
message = "Dear " + popped_friends.title() + ", I am sorry that you can't come."
print(message)
popped_friends = friends.pop(2)
message = "Dear " + popped_friends.title() + ", I am sorry that you can't come."
print(message)
popped_friends = friends.pop(2)
message = "Dear " + popped_friends.title() + ", I am sorry that you can't come."
print(message)
popped_friends = friends.pop(2)
message = "Dear " + popped_friends.title() + ", I am sorry that you can't come."
print(message)
popped_friends = friends.pop(2)
message = "Dear " + popped_friends.title() + ", I am sorry that you can't come."
print(message)
print(friends)
message = "Dear " + friends[0].title() + ", you can come to the party!"
print(message)
message = "Dear " + friends[1].title() + ", you can come to the party!"
print(message)
del friends[0]
del friends[0]
print(friends)















