# Calcular a média de três notas fornecidas na entrada do usuário

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

#Formatacao de string para notacao de ponto flutuante, duas casas apos a virgula
print(f"A média das notas é {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

