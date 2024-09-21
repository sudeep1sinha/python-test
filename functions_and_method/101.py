def check(num,low,high):
    return num in range(low,high+1)

print(check(5,2,5)) 


def check_num(num,low,high):
    if num in range(low , high+1):
        print(f"{num} is in {low} and {high}")

    else:
        print("shessh not in range")

print(check_num(5,2,5))