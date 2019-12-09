
x = 0
for i in range(10, 100):
    for j in range(10, 100):
        x = i * j
        print(i,'*',j,'=',x)

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