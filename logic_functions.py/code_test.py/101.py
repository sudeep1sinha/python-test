def myfunc(a,b):

    if a%2==0 and b%2==0:
        if a<b:
            result= a
        else:
            result= b

    else:
        if a > b:
            result= a
        else:
            result= b
    return result

num=myfunc(9,6)

print(num)


# more short and clean
if a%2==0 and b%2==0:
    return min(a,b)

else:
    return max(a,b)