# Exibe boas vindas
print("Bem-vindo(a) à Loja da Sarah Marques!")

# Perguta de valor e quantidade de produtos
preco = int(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade de produto: "))

# Cálculo do valor total
total = preco * quantidade

# Cálculo de porcentagem de desconto
desconto4 = ((total * 4) / 100)
desconto7 = ((total * 7) / 100)
desconto11 = ((total * 11) / 100)

# Condições
if total <= 0:
 print('Valor inválido!')

elif total < 2500: # 0% de desconto
 print(f"O valor SEM desconto: R${total: }")

elif total < 6000: # 4% de desconto
 print(f"O valor SEM desconto: R${total: }")
 print(f"O valor COM desconto: R${total - desconto4: }")

elif total < 10000: # 7% de desconto
 print(f"O valor SEM desconto: R${total: }")
 print(f"O valor COM desconto: R${total - desconto7: }")

else: # 11% de desconto
 print(f"O valor SEM desconto: R${total: }")
 print(f"O valor COM desconto: R${total - desconto11: }")