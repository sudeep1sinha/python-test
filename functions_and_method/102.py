def up_low(she):
    d={'upper':0,'lower':0}
    #uppercase=0
    #lowercase=0

    for char in she:
        if char.isupper():
            d['upper']+=1

        elif char.islower():
            d['lower']+=1
        else:
            pass

        print(f"original string : {she}")
        print(f'lower count : {d["lower"]}')
        print(f'uppercase : {d["upper"]}')

print(up_low("cmom DIS iS a HEALTHcode violatioN"))