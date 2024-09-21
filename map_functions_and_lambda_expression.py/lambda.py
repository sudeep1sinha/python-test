square=lambda num : num ** 2 

result=square(5)

print(result)



#lambda with map function

mynums=[1,2,3,4,5,6]
she=list(map(lambda num : num **2,mynums))
print(she)


#lambda with filter function

he=list(filter(lambda num : num%2==0,mynums))

print(he)