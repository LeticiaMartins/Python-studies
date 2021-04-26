# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:03:26 2021

@author: leticia Martins
"""

num = int(input("Digite n: "))

while(num > 0):
    digito = num // 1 % 10
    num_novo = num - digito
print(num_novo)


'''
teste = num // 100 % 10
t = num // 10 % 10
tt = num // 1 % 10
print(teste, t, tt)

'''
'''
dv1 = soma1 % 11

dv2 = soma2 % 11 

print(dv1, dv2)





soma = 0
numero = 123
while(numero > 0):
    soma += numero % 10
    numero = int(numero /10)
print(soma)
'''