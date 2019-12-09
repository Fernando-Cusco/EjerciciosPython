x = 600851475143
for i in range(1, 600851475143):
    if x%i == 0 and x%1 == 0:
        print(True, i)