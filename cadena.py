# -*- coding: utf-8 -*-
print("Bienvenido, este programa compara dos cadenas y muestra si son iguales o no")
primera = raw_input("Ingrese la primera cadena: ")
segunda = raw_input("Ingrese la segunda cadena: ")

if len(primera) != len(segunda):
    print("No son iguales")
else: 
    for i in range(len(primera)):
        if primera[i] != segunda[i]:
            print("No son iguales")
            break
    print("Son iguales")