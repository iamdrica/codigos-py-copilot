# testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação 
# de strings para inverter a palavra e comparar com a original.

#Palindromo é uma palavra que se lê da mesma forma de trás para frente.

palavra = input("Digite uma palavra: ")
if palavra == palavra[::-1]: # [::-1] é um slice que inverte a string
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")