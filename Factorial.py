def fact(n):#user defined fuction
    fact=1
    for i in range(n):
        if(n-i)!=0:
            fact*=(n-i)
    return fact

ch='y'
k = ['N','n']
while ch.lower()=='y':
    print('\nENTER YOUR NUMBER [1 - N]')
    n=int(input('\tN => '))
    print('\nYOUR ENTERED NUMBER SERIES IS 1 -',n)
    if n == 1:#checking condition
        print("\nFACTORIAL OF 1 IS 1")
    if n < 0:
        print("\nFACTORIAL IS NOT DEFINED FOR NEGATIVE NUMBERS")
    elif n == 0:
        print("\nFACTORIAL OF 0 IS 1")
    else:
        print("\nTHE FACTORIAL OF",n,"IS",fact(n))  
    ch=input('\nPRESS [Y|N] TO CONTINUE : ')
    if ch in k:
        quit()



