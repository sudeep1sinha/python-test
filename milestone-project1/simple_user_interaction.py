game_list=[0,1,2]

def display_game(game_list):
    print("here is the current game list")
    print(game_list)
    #return game_list

print(display_game(game_list))


def position_choice():
    choice='wrong'

    while choice not in ['0','1','2']:
        choice=input("enter the choice :")

        if choice not in ['0','1','2']:
            print("hey u enter the wrong choice number")

    return int(choice)

position=position_choice()
print(position)

def replacement_choice(game_list,position):

    user_placement=input("type a string to replace :")

    game_list[position]=user_placement

    return game_list

print(replacement_choice(game_list,position))

def gameon_choice():

    choice='wrong'

    while choice not in ['Y','N']:
        choice=input("keep playing ? (Y or N)")

        if choice not in ['Y','N']:
            print("sorry i dont understand plss try again")

    if choice == 'Y':
        return True

    else:
        return False

print(gameon_choice())

game_on=True
game_list=[0,1,2]

while game_on:
    display_game(game_list)

    position=position_choice()

    game_list=replacement_choice(game_list,position)

    #display_game(game_list)

    game_on=gameon_choice()

