def user_input():
    choice = 'wrong'
    acceptable_range = range(0, 11)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Enter a number: ")

        if choice.isdigit() == False:
            print("Sorry, this is not a digit")
        elif int(choice) in acceptable_range:
            within_range = True
        else:
            print('Choice not in acceptable range')

    return int(choice)

print(user_input())