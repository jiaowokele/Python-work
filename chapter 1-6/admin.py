users = ['kele','xiaoqi','liumao','susu','admin']
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a staus report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")
print("\n\n")

current_users = ['kele','xiaoqi','liumao','kangkang','admin']
new_users = ['Kele','AAA','BBB','admin','CCC']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You need to log in another name!")
    else:
        print("It is not used before")



numbers = list(range(1,10))
for number in numbers:
    if number < 2:
        print("1st\n")
    elif number < 2:
        print("2nd\n")
    elif number < 4:
        print("3rd\n")
    elif number < 5:
        print("4th\n")
    elif number < 6:
        print("5th\n")
    elif number < 7:
        print("6th\n")
    elif number < 8:
        print("7th\n")
    elif number < 9:
        print("8th\n")
    else:
        print("9t\n")
