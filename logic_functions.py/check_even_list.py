#def even_check_list(num_list):
 #   for number in num_list:
 #       if number %2==0:
 #           return True
 #       else:
 #           pass

#print(even_check_list([1,3,5]))


def even_check_list(num_list):

    even_number=[]

    for number in num_list:
        if number%2==0:
            even_number.append(number)

        else:
            pass
        
    return even_number

print(even_check_list([1,2,3,4,5]))