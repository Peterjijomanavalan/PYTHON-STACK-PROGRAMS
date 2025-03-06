print('\n>>>')
print('\nGIVEN MENU FOR ADDING AND DISPLAYING NUMBERS ')
print()
#menue card
print('1) <<< ADD >>>')
print('2) <<< DELETE THE LAST NUMBER >>>')
print('3) <<< PEEK  >>>')
print('4) <<< DISPLAY THE NUMBERS >>>')
print('5) <<< EXIT >>>')
print()
p=[]
def push():
    #push function
    ct=0
    n=int(input('\nENTER THE NO. OF NUMBERS : '))
    for i in range(n):
        ct+=1
        print()
        print(ct,end='.')
        a=int(input('\nENTER THE NUMBER  : '))
        p.append(a)
def pop():
    #pop function
    if p==[]:
        print('\nUNDERFLOW')
    else:
        print('\nPOPED ELEMENT IS',p.pop())
def peek():
    #peek function
    if p==[]:
        print('\nUNDERFLOW')
    else:
        print('\nPEEK ELEMENT IS',p[-1])

def display():
    #display function
    for i in range(len(p)-1,-1,-1):
        print()
        print(p[i])
    if p==[]:
        print("\nSTACK EMPTY")
while True:
    ch=int(input('\nENTER YOUR CHOICE : '))
    if ch==1:
        print('\nYOUR SELECTED CHOICE IS ADD ')
        push()#calling push function
    elif ch==2:
        print('\nYOUR SELECTED CHOICE IS DELETE THE LAST NUMBER')
        pop()#calling pop function
    elif ch==3:
        print('\nYOUR SELECTED CHOICE IS ACCESS THE FIRST NUMBER')
        peek()#calling peek function
    elif ch==4:
        print('\nYOUR SELECTED CHOICE IS DISPLAY THE NUMBERS')
        display()#calling display function
    elif ch==5:
        print('\nYOUR SELECTED CHOICE IS EXIT')
        print('\n>>>')
        exit()
    else:
        print('\n-> -> INVALID CHOICE <- <-')
