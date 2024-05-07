#Input palavra
palavra = input("Insira uma palavra: ")

#converter para minúsculas
palavra = palavra.lower()


#[] operador de fatiamento de sequência, pode ser usado para acessar partes de uma lista ou string. 
#Quando usado com um terceiro argumeno -1, indica que estamos acessando a sequência de trás para frente, invertendo-a.
#palavra[::1] acessa a sequência original do início ao fim.
#palavra[::-1] acessa a sequência de trás para frente, ou seja, a sequência invertida.

#verifica se é um palíndromo ou não
if palavra == palavra[::-1]:
    print(f"{palavra} é um palíndromo!")
else:
    print(f"{palavra} não é um palíndromo.")