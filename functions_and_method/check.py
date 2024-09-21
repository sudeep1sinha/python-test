import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    print(alphaset)

    str1 = str1.replace(' ', '')
    str1 = str1.lower()
    print(str1)
    str1 = set(str1)
    print(str1)

    return str1 == alphaset

print(ispangram("the quick brown fox jjjumps over the lazy dog"))