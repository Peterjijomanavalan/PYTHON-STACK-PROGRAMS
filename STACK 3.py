print('\n>>>')
print('\nGIVEN MENUE FOR ADDING AND DISPLAYING EMPOLOYEE ')
print()
#menue card
print(" 1) <<< ADD RECORD >>>")
print(" 2) <<< DELETE RECORD >>>")
print(" 3) <<< DISPLAY RECORD >>>")
print(" 4) <<< EXIT >>>")

p  = []
def push(p):
    #push function
    ct=0
    n=int(input(' \nENTER THE LIMIT : '))
    for i in range(n):
        ct+=1
        print()
        print(ct,end='.')
        emp_id   = int(input(' \nENTER THE EMP_ID : '))
        emp_name = input('\nENTER THE EMP_NAME : ')
        emp_salary = int(input(' \nENTER THE EMP_SALARY : '))
        dat = [emp_id,emp_name,emp_salary]
        p.append(dat)

def pop():
    #pop function
    if p == []:
        print('UNDERFLOW')
    else:
        print('\nREST OF THE EMPOLOYEE AFTER POPING ARE')
        print()
        print('EMP_ID','\t\t','EMP_NAME','\t','EMP_SALARY')
        a=p.pop()
        print(a[0],"\t\t",a[1],"\t\t",a[2])

def display(p):
    #display function
    l=len(p)
    if p==[]:
        print("\nSTACK EMPTY")
    else:
        print('EMP_ID','\t\t','EMP_NAME','\t','EMP_SALARY')
        for i in range(l-1,-1,-1):
            print(p[i][0],"\t\t",p[i][1],"\t\t",p[i][2])
    
while True:
    ch = int(input(' \nENTER YOUR CHOICE : '))
    if ch==1:
        print(' \nYOUR SELECTED CHOICE IS ADD RECORD')
        push(p)#calling push function
        continue
    elif ch==2:
        print(' \nYOUR SELECTED CHOICE IS DELETE RECORD\n')
        pop()#calling pop function
        continue
    elif ch==3:
        print(' \nYOUR SELECTED CHOICE IS DISPLAY RECORD\n')
        display(p)#calling display function
        continue
    elif ch==4:
        print(' \nEXITING')
        exit()
    else:
        print('\n -> -> INVALID CHOICE <- <-')
