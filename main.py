##READING A FILE

##f=open('myfile.txt','r')##
##text=f.read()
#print(text)
#f.closed()


## WRITING A FILE
##f=open('myfile.txt','a')
##f.write('\n hello world!')
#f.close()



##another writing method
with open('myfile.txt','a') as f:
    f.write('hey i am batman')