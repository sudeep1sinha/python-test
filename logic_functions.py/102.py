example=[1,2,3,4,5,6,7,8]

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return(mylist)

result=shuffle_list(example)

print (result)


mylist=['','0','']
shuffle_list(mylist)

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=(input("pick a number : 0,1 or 2 :"))

    return int (guess)

#print(player_guess())

#my_index=player_guess()

#print(my_index)

def check_guess(jelly,beans):
    if jelly[beans]=='0':
        print('correct')
    else:
        print('wrong guess')

        print(jelly)

#INITIAL LIST 
mylist=['','0','']

#SHUFFLE LIST
mixedup_list=shuffle_list(mylist)

#USER GUESS
guess=player_guess()

#CHECK GUESS
check_guess(mixedup_list,guess)