#def user_choice():

#    choice=int(input("please enter the number :"))

#    if type(choice)==int:
#        print(f"{choice} is a number")
#    else:
#        print(f"{choice} is not a number")

#    return int(choice)

#print(user_choice())


def user_input():

    choice='wrong'
    acceptable_range=range(0,11)
    within_range=False

    while choice.isdigit()==False or within_range==False:
       
        choice=input("enter a number :")
        if choice.isdigit()==False:
            print("sorry dis is not a digit")
        
        elif choice.isdigit()==True:
            if int(choice) in acceptable_range:
                    within_range=True
            else:
                print('choice not in acceptable range')

    return int(choice)

print(user_input())