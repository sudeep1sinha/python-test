def animal_crackers(word1,word2):
    if word1[0]==word2[0]:
        return True

    else:
        return False


word=animal_crackers('hello','they')

print(word)



def animal_crackers(word):

    wordlist=word.split()
    first=wordlist[0]
    second=wordlist[1]

    return first[0]==second[1]


def animal(word):
    text=word.lower().split()
    print(text)
    return word[0][0]==word[1][0]
