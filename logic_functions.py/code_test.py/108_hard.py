def summer(arr):

    total=0
    add=True

    for num in arr:
        if num!=6:
            total+=num
            

        elif num!=9:
            break
            
    return total


print(summer([2,1,6,9,11]))