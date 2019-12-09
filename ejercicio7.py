def esPalindromico(x):
    flag = False
    cont = 0
    j = len(x)-1
    for i in range(len(x)):
        if x[i] == x[j]:
            if(cont == len(x)-1):
                flag = True
            cont += 1
        j -= 1
    return flag

print(esPalindromico('anitalavalatina'))

ls = 1
mx = 10
ec = 100

print(la, mx, ec)
        

