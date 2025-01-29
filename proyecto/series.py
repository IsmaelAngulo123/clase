#Serie resta de N
def resta_acumulativa(n):
    resta = n
    for i in range(n - 1, 0, -1):
        resta -= i
    return resta

print(resta_acumulativa(5))  

#Ismael Angulo
