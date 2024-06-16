# Exibe boas vindas e o cardápio
cardapio = '''
    Bem vindo(a) á Açaíteria da Sarah!
---------------- Cárdapio ------------------
--------------------------------------------
--| Tamanho |  Cupuaçu (CP) |  Açai (AC) |--
--|    P    |    R$ 9,00    |  R$ 11,00  |--
--|    M    |    R$ 14,00   |  R$ 16,00  |--
--|    G    |    R$ 18,00   |  R$ 20,00  |--
--------------------------------------------
'''
print(cardapio)

# Inicia o acumulador
valor = 0
acumulador = 0

while True:
     # Solicita o sabor
     sabor = input("Entre com o sabor desejado ( CP / AC ): ").upper()
     if sabor != "CP" and sabor != "AC":
       print("Sabor inválido. Tente novamente.")
       continue

     # Solicita o tamanho
     tamanho = input("Entre com o tamanho desejado ( P / M / G ): ").upper()
     if tamanho != "P" and tamanho != "M" and tamanho != "G":
       print("Tamanho inválido. Tente novamente.")
       continue

     # Condições de tamanhos e sabores
     if sabor == "CP":
        if tamanho == "P":
         valor = 9.00
         
         print("Você pediu um Cupuaçu no tamanho P: R$ 9.00")
        elif tamanho == "M":
         valor = 14.00
         print("Você pediu um Cupuaçu no tamanho M: R$ 14.00")
        elif tamanho == "G":
         valor = 18.00
         print("Você pediu um Cupuaçu no tamanho G: R$ 18.00")
     else:
        if sabor == "AC":
          if tamanho == "P":
           valor = 11.00
           print("Você pediu um Açaí no tamanho P: R$ 11.00")
          elif tamanho == "M":
           valor = 16.00
           print("Você pediu um Açaí no tamanho M: R$ 16.00")
          elif tamanho == "G":
           valor = 20.00
           print("Você pediu um Açaí no tamanho G: R$ 20.00")
          else:
            print("Inválido")

     # Soma o valor total
     acumulador += valor

     # Pergunta se deseja continuar
     continuar = input("Deseja mais alguma coisa? ( S / N ): ").upper()
     if continuar != 'S':
       break

# Mostra o total do valor final
print(f"O total do seu pedido é: R$ {acumulador}")