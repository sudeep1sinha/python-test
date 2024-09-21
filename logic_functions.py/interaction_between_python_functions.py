example=[1,2,3,3,4,5,6,7]

from random import shuffle
#shuffle(example)
#print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result=shuffle_list(example)

print(result)


mylist=['',0,'']
result1=shuffle_list(mylist)
print(result1)
