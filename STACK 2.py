print('\n>>>')
print('\nGIVEN MENUE FOR ADDING AND DISPLAYING NAME ')
print()
#menue card
print('1) <<< ADD >>>')
print('2) <<< REVERSING THE NAME >>>')
print('3) <<< EXIT >>>')
print()
p1=[]
def add():
    #add function
    n=input('\nENTER THE NAME : ')
    for i in n:
        p1.append(i)
def reverse():
    #reverse function
    if p1==[]:
        print('\nUNDERFLOW')
    else:
        print('\nREVERSED NAME => ')
        print()
        for i in range(len(p1)):
            print(p1.pop(),end='')
        print()
    
while True:
    ch=int(input('\nENTER YOUR CHOICE : '))
    if ch==1:
        print('\nYOUR SELECTED CHOICE IS ADD')
        add()#calling add function
    elif ch==2:
        print('\nYOUR SELECTED CHOICE IS REVERSE')
        reverse()#calling reverse function
    elif ch==3:
        print('\nYOUR SELECTED CHOPICE IS EXIT')
        print('\nEXITING...')
        print('\n>>>')
        exit()
    else:
        print('\n-> -> INVALID CHOICE <- <-')
