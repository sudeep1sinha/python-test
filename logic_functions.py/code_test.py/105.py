def has_33(num):
    for i in range(0,len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True

        else:
            False

print(has_33([1,2,3,3]))