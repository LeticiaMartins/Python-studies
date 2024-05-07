#Input número inteiro positivo
try:
  num = int(input("Insira um número inteiro positivo: "))
  if num < 0:
    print("Insira um número inteiro positivo: ")
except ValueError:
        print("Insira um número inteiro positivo: ")
        
#Calcular fatorial
#produto de todos os números inteiros positivos de 1 até o próprio número
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de {num} é {fatorial}")