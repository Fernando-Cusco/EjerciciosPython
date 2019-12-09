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

# i = 1
# c = 0
# while i < 7:
#     if(i%2 == 0 and i%1 == 0):
#         i+=1
#         c+=1
#     if c  == 10001:
#         print(i)
#         break    
        

