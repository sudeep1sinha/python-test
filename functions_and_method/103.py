def palindrome(stringname):

    stringname=stringname.replace(' ','')

    return stringname==stringname[::-1]

print(palindrome("sudusp"))