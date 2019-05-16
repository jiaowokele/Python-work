favorate_languages = {
    'jen': 'python',
    'sarah': 'c' ,
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorate language is " + favorate_languages['sarah'].title() + ".")

old_friend = {
    'first_name': 'mei' ,
    'last_name' : 'yuchao' ,
    'age' : 23 ,
    'city': 'wuhan' ,

}
print(str(old_friend)  + '\n')

favorate_number = {
    'caven' : 4 ,
    'kele'  : 6 ,
    'jobs'  : 9 ,
    'taylor': 13,
    'alice' : 2 ,
 }
print("Caven's favorate number is " + str(favorate_number['caven']) + '.')
print("Kele's favorate number is " + str(favorate_number['kele']) + '.')
print("Job's favorate number is " + str(favorate_number['jobs']) + '.')
print("Taylor's favorate number is " + str(favorate_number['taylor']) + '.')
print("Alice's favorate number is " + str(favorate_number['alice']) + '.\n')


for name , language in favorate_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')
friends = ['phil' , 'sarah']
for name in favorate_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorate_languages[name].title() + "!")


if 'erin' not in favorate_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorate_languages.keys()):
    print(name.title() + ", thank you for taking the poll.\n")

print("The following languages have been mentioned:")
for language in favorate_languages.values():
    print(language.title())

for language in set(favorate_languages.values()):
    print(language.title())

print("\n")

favorate_languages = {
    'jen': 'python',
    'sarah': 'c' ,
    'edward': 'ruby',
    'phil': 'python',
}

people = ['kele' , 'caven' , 'edward', 'xiaoqi', 'jen']

for name in favorate_languages.keys():
    if name in people:
        print(name.title() + ", thank you!")
    else:
        print(name.title() + ", I am glad to invite you for investigation!")


favorate_languages = {
    'jen': ['python','c'],
    'sarah': ['c' ,'c++'],
    'edward': ['ruby'],
    'phil': ['python','R']
}

for name,languages in favorate_languages.items():
    print("\n" + name.title() + "'s favorate languages is:")
    for language in languages:
        print("\t" + language.title())