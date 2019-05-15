user_0 = {
    'username' : 'kele' ,
    'first' : 'ke' ,
    'last'  : 'le' ,
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


rivers = {
    'nile' : 'egypt' ,
    'changjiang' : 'china' ,
    'hanjiang': 'wuhan',
}

for river , location in rivers.items():
    print(river.title() + " run through " + location + ".")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)

