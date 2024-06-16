# Boas vindas
print("Bem vindo(a) á copiadora da Sarah Marques!")

# Menu
def escolha_servico():
    print('''
Serviços:
  DIG - Digitalização
  ICO - Impressão Colorida
  IPB - Impressão Preto e Branco
  FOT - Fotocópia
''')
    # Pergunta o tipo de serviço desejado:
    servico = input("Digite o tipo de serviço desejado: ").upper()

    # Loop para serviço inválido
    while servico not in ["DIG", "ICO", "IPB", "FOT"]:
        print("Escolha inválida, entre com o tipo de serviço novamente.")
        servico = input("Escolha um serviço: ").upper()

    # Condições de preços
    if servico == "DIG":
        preco_servico = 1.1
    elif servico == "ICO":
        preco_servico = 1
    elif servico == "IPB":
        preco_servico = 0.4
    elif servico == "FOT":
        preco_servico = 0.2
    else:
        print("Serviço indisponível.")
        return None, None  # Essa linha é apenas para garantir que a função retorne algo válido se cair no else

    return preco_servico, servico

# Pergunta a quantidade de páginas
def num_paginas():
    while True:
        try:
            paginas = int(input("Digite o número de páginas desejado: "))
            if paginas < 0:
                print("Valor inválido, tente novamente")
                continue

            # Condições de quantidade de páginas
            desconto = ""
            if paginas < 20:
                paginas_desconto = paginas * 1
            elif paginas >= 20 and paginas < 200:
                paginas_desconto = paginas * 0.85
                desconto = "(15% de desconto)"
            elif paginas >= 200 and paginas < 2000:
                paginas_desconto = paginas * 0.8
                desconto = "(20% de desconto)"
            elif paginas >= 2000 and paginas < 20000:
                paginas_desconto = paginas * 0.75
                desconto = "(25% de desconto)"
            elif paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                continue
            return paginas_desconto, paginas, desconto
        except ValueError:
            print("Valor inválido, tente novamente")

# Menu de serviços extras
def servico_extra():
    print('''
Serviços adicionais:
   1 - Encadernação simples - R$ 15.00
   2 - Encadernação de capa dura - R$ 40.00
   0 - Não desejo mais nada
''')
    try:
        # Pergunta se deseja mais algum serviço
        servico_extra = int(input("Deseja adicionar algum serviço?: "))
        while servico_extra not in [0, 1, 2]:
            print("Número inválido.")
            servico_extra = int(input("Deseja adicionar algum serviço?: "))

        # Condições de preços de serviços extras
        if servico_extra == 1:
            extra = 15.00
        elif servico_extra == 2:
            extra = 40.00
        elif servico_extra == 0:
            extra = 0
        return extra
    except ValueError:
        print("Número inválido.")
        return 0

# Executa as funções e calcula o preço total
preco_servico, servico = escolha_servico()
if preco_servico and servico:
    paginas_desconto, paginas, desconto = num_paginas()
    extra = servico_extra()

    # Calculo do preço total do serviço (com ou sem extras)
    total = (preco_servico * paginas_desconto) + extra

    print(f"Total do pedido: R$ {total:.2f} {desconto} / Serviço: R$ {preco_servico:.2f} / Páginas: {paginas} / Extra: R$ {extra:.2f}.")