def myfunc(letter):
    new_letter=""

    for i,j in enumerate(letter):
        if i%2==0:
            new_letter+=j.upper()

        else:
            new_letter+=j.lower()

    return new_letter

letter_string=myfunc("hey how u doing")
print(letter_string)



def myfunc(input_string):
    result = ""
    is_even = True  # Start with uppercase

    for char in input_string:
        if is_even:
            result += char.upper()
        else:
            result += char.lower()

        # Toggle the is_even flag
        is_even = not is_even

    return result

input_string = "heyhowudoing"
output_string = myfunc(input_string)
print(output_string)