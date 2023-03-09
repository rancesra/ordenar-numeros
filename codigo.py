
# input


valor1 = int(input("Digite valor 1: "))
valor2 = int(input("Digite valor 2: "))
valor3 = int(input("Digite valor 3: "))

# codicion

if(valor1<valor2<valor3):
    print(valor1,valor2,valor3)
else:
    if(valor3<valor2<valor1):
        print(valor3,valor2,valor1)
    else:
        if(valor1<valor3<valor2):
            print(valor1,valor3,valor2)
        else:
            print("codigo mal :C")