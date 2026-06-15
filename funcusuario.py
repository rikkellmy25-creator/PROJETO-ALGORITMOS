# -*- coding: utf-8 -*-
"""
Menu de usuário (cliente) - versão refatorada com DICIONÁRIOS.

Usa exatamente as mesmas estruturas do menu ADM (funcadm), para que os dois
módulos compartilhem as mesmas listas de dados sem conflito:

rebanho        -> {"ID", "TIPO", "PESO", "GESTACAO", "VALOR", "QUANTIDADE"}
estoqueadm     -> {"ID", "PRODUTO", "QUANTIDADE", "PESO", "VALOR", "VALIDADE"}
financeiro     -> {"VALOR", "DESCRICAO", "TIPO"}  (TIPO: "ENTRADA"/"SAIDA")
retiradas      -> {"ID", "TIPO", "DATA", "HORA", "STATUS"}
propostas      -> {"ID", "USUARIO", "PRODUTO", "VALOR", "DESC", "QUANTIDADE", "STATUS"}

Estruturas internas do lado do cliente:
estoquecliente -> {"ID", "TIPO", "ITENS", "TOTAL", "STATUS", "CATEGORIA"}
item comprado  -> {"ID", "NOME", "QUANTIDADE", "TOTAL", "CATEGORIA"}
"""
import funcadm
def buscar_proposta_aceita(propostas, usuario, nome_item):
    for p in propostas:
        if (p["USUARIO"] == usuario and p["PRODUTO"] == nome_item and p["STATUS"] == "ACEITA"):
            return p["VALOR"]
    return None

def comprar_produtos(estoqueadm, estoquecliente, financeiro, propostas, usuario):
    produtos_comprados = []
    total_geral = 0
    continuar = "SIM"

    while continuar == "SIM":
        funcadm.listarestoqueadm(estoqueadm)
        if len(estoqueadm) == 0:
            break

        id_compra = int(input(("DIGITE O ID DO PRODUTO QUE DESEJA ADQUIRIR: ")))
        produto_encontrado = False

        for produto in estoqueadm:
            if produto["ID"] == id_compra:
                produto_encontrado = True
                quant_compra = int((input("DIGITE A QUANTIDADE QUE DESEJA COMPRAR: ")))

                if quant_compra <= 0 or quant_compra > produto["QUANTIDADE"]:
                    print("QUANTIDADE INVALIDA!")
                    break

                valor_unitario = produto["VALOR"]
                valor_proposta = buscar_proposta_aceita(propostas, usuario, produto["PRODUTO"])
                if valor_proposta is not None:
                    print(f"PROPOSTA ACEITA ENCONTRADA! O VALOR DO PRODUTO "
                          f"{produto['PRODUTO']} FOI ALTERADO PARA R${valor_proposta}")
                    valor_unitario = valor_proposta

                total_compra = quant_compra * valor_unitario
                produtos_comprados.append({"ID": produto["ID"],"NOME": produto["PRODUTO"],"QUANTIDADE": quant_compra,"TOTAL": total_compra,"CATEGORIA": "PRODUTO",})
                total_geral += total_compra
                print("PRODUTO ADICIONADO A COMPRA!")
                break

        if not produto_encontrado:
            print("PRODUTO NÃO ENCONTRADO!")

        continuar = input("DESEJA ADICIONAR OUTRO PRODUTO?(SIM/NÃO): ").upper()

    if len(produtos_comprados) == 0:
        print("NENHUM PRODUTO ADICIONADO. COMPRA CANCELADA!")
        return

    # Resumo da compra (fora do laço)
    print('''
=========================
     RESUMO DA COMPRA
=========================''')
    for produto in produtos_comprados:
        print(f'''
PRODUTO: {produto["NOME"]}
QUANTIDADE: {produto["QUANTIDADE"]}
TOTAL: R$ {produto["TOTAL"]:.2f}''')
    print(f"\nTOTAL GERAL: R$ {total_geral:.2f}")

    confirmar = input("\nDESEJA CONFIRMAR A COMPRA? SIM/NAO: ").upper()
    if confirmar in ("NÃO", "NAO"):
        print("COMPRA CANCELADA!")
        return

    # Baixa no estoque
    for produto in produtos_comprados:
        for item in estoqueadm:
            if item["ID"] == produto["ID"]:
                item["QUANTIDADE"] -= produto["QUANTIDADE"]

    id_compra_cliente = len(estoquecliente) + 1
    estoquecliente.append({"ID": id_compra_cliente,"TIPO": "PRODUTOS","ITENS": produtos_comprados,"TOTAL": total_geral,"STATUS": "PENDENTE","CATEGORIA": "PRODUTO",})
    financeiro.append({"VALOR": total_geral, "DESCRICAO": "PRODUTO VENDIDO", "TIPO": "ENTRADA"})

    print('''
=============================
COMPRA REALIZADA COM SUCESSO!
=============================''')
    for produto in produtos_comprados:
        print(f'''
PRODUTO: {produto["NOME"]}
QUANTIDADE COMPRADA: {produto["QUANTIDADE"]}
VALOR TOTAL: R$ {produto["TOTAL"]:.2f}
STATUS DE RETIRADA: PENDENTE''')
    print(f'''
=============================
TOTAL GERAL: R$ {total_geral:.2f}
=============================''')

def comprar_animais(rebanho, estoquecliente, financeiro, propostas, usuario):
    animais_comprados = []
    total_geral = 0
    continuar = "SIM"

    while continuar == "SIM":
        funcadm.listarrebanho(rebanho)
        if len(rebanho) == 0:
            break

        id_compra = int(input("DIGITE O ID DO ANIMAL QUE DESEJA ADQUIRIR: "))
        animal_encontrado = False

        for animal in rebanho:
            if animal["ID"] == id_compra:
                animal_encontrado = True
                quant_compra = int(("DIGITE A QUANTIDADE QUE DESEJA COMPRAR: "))

                if quant_compra <= 0 or quant_compra > animal["QUANTIDADE"]:
                    print("QUANTIDADE INVALIDA!")
                    break

                valor_unitario = animal["VALOR"]
                valor_proposta = buscar_proposta_aceita(propostas, usuario, animal["TIPO"])
                if valor_proposta is not None:
                    print(f"PROPOSTA ACEITA ENCONTRADA! O VALOR DO ANIMAL "
                          f"{animal['TIPO']} FOI ALTERADO PARA R${valor_proposta}")
                    valor_unitario = valor_proposta

                total_compra = quant_compra * valor_unitario
                animais_comprados.append({
                    "ID": animal["ID"],
                    "NOME": animal["TIPO"],
                    "QUANTIDADE": quant_compra,
                    "TOTAL": total_compra,
                    "CATEGORIA": "ANIMAL",
                })
                total_geral += total_compra
                print("ANIMAL ADICIONADO A COMPRA!")
                break

        if not animal_encontrado:
            print("ANIMAL NÃO ENCONTRADO!")

        continuar = input("DESEJA ADICIONAR OUTRO ANIMAL?(SIM/NÃO): ").upper()

    if len(animais_comprados) == 0:
        print("NENHUM ANIMAL ADICIONADO. COMPRA CANCELADA!")
        return

    print('''
=========================
     RESUMO DA COMPRA
=========================''')
    for animal in animais_comprados:
        print(f'''
ANIMAL: {animal["NOME"]}
QUANTIDADE: {animal["QUANTIDADE"]}
TOTAL: R$ {animal["TOTAL"]:.2f}''')
    print(f"\nTOTAL GERAL: R$ {total_geral:.2f}")

    confirmar = input("\nDESEJA CONFIRMAR A COMPRA? SIM/NAO: ").upper()
    if confirmar in ("NÃO", "NAO"):
        print("COMPRA CANCELADA!")
        return
    for animal in animais_comprados:
        for item in rebanho:
            if item["ID"] == animal["ID"]:
                item["QUANTIDADE"] -= animal["QUANTIDADE"]

    id_compra_cliente = len(estoquecliente) + 1
    estoquecliente.append({
        "ID": id_compra_cliente,
        "TIPO": "ANIMAL",
        "ITENS": animais_comprados,
        "TOTAL": total_geral,
        "STATUS": "PENDENTE",
        "CATEGORIA": "ANIMAL",
    })
    financeiro.append({"VALOR": total_geral, "DESCRICAO": "ANIMAL VENDIDO", "TIPO": "ENTRADA"})

    print('''
=============================
COMPRA REALIZADA COM SUCESSO!
=============================''')
    for animal in animais_comprados:
        print(f'''
ANIMAL: {animal["NOME"]}
QUANTIDADE COMPRADA: {animal["QUANTIDADE"]}
VALOR TOTAL: R$ {animal["TOTAL"]:.2f}
STATUS DE RETIRADA: PENDENTE''')
    print(f'''
=============================
TOTAL GERAL: R$ {total_geral:.2f}
=============================''')

def agendar_retirada(estoquecliente, retiradas):
    print('''
=========================
     AGENDAR RETIRADA
=========================''')

    retirada_pendente = False
    print("RETIRADAS PENDENTES: ")
    for i in estoquecliente:
        if i["STATUS"] == "PENDENTE":
            retirada_pendente = True
            print(f'''
ID DA COMPRA: {i["ID"]}
TIPO: {i["TIPO"]}
TOTAL PAGO: R$ {i["TOTAL"]:.2f}
STATUS: {i["STATUS"]}''')

    if not retirada_pendente:
        print("NÃO POSSUI RETIRADAS PENDENTES!")
        return

    id_retirada = int(input("DIGITE O ID DA COMPRA QUE DESEJA AGENDAR A RETIRADA: "))
    for i in estoquecliente:
        if i["ID"] == id_retirada and i["STATUS"] == "PENDENTE":
            data = input("DIGITE A DATA DA RETIRADA(AA/MM/YY): ")
            hora = input("DIGITE A HORA DA RETIRADA(HH:MM): ")
            retiradas.append({"ID": i["ID"],"TIPO": i["CATEGORIA"],"DATA": data,"HORA": hora,"STATUS": "PENDENTE",})
            i["STATUS"] = "RETIRADA AGENDADA"
            print(f'''
==============================
RETIRADA AGENDADA COM SUCESSO!
==============================
ID DA COMPRA: {i["ID"]}
TIPO: {i["CATEGORIA"]}
TOTAL PAGO: R$ {i["TOTAL"]:.2f}
DATA: {data}
HORA: {hora}
STATUS: PENDENTE''')
            return
    print("ID NÃO ENCONTRADO OU RETIRADA JÁ AGENDADA!")



def enviar_proposta(estoqueadm, propostas, usuario):
    funcadm.listarestoqueadm(estoqueadm)
    if len(estoqueadm) == 0:
        return
    id_produto = int(input("DIGITE O ID DO PRODUTO QUE DESEJA ENVIAR A PROPOSTA: "))
    produto_encontrado = False

    for i in estoqueadm:
        if i["ID"] == id_produto:
            produto_encontrado = True
            valor_proposta = int(input("DIGITE O VALOR DA PROPOSTA: "))
            desc_proposta = input("DIGITE UMA DESCRIÇÃO PARA A PROPOSTA: ")
            qtd_proposta = int(input("DIGITE A QUANTIDADE QUE DESEJA PROPOR: "))

            if qtd_proposta <= 0:
                print("QUANTIDADE INVALIDA!")
                return
            id_proposta = len(propostas) + 1
            propostas.append({"ID": id_proposta,"USUARIO": usuario,"PRODUTO": i["PRODUTO"],"VALOR": valor_proposta,"DESC": desc_proposta,"QUANTIDADE": qtd_proposta,"STATUS": "PENDENTE",})
            print("PROPOSTA ENVIADA!")
            print("AGUARDANDO RESPOSTA DO ADMINISTRADOR...")
            return

    if not produto_encontrado:
        print("PRODUTO NÃO ENCONTRADO!")


def ver_propostas(propostas, usuario):
    propostas_usuario = False
    for i in propostas:
        if i["USUARIO"] == usuario:
            propostas_usuario = True
            print(f'''
ID: {i["ID"]}
PRODUTO: {i["PRODUTO"]}
VALOR PROPOSTO: R$ {i["VALOR"]}
DESCRIÇÃO: {i["DESC"]}
QUANTIDADE: {i["QUANTIDADE"]}
STATUS: {i["STATUS"]}''')
    if not propostas_usuario:
        print("VOCÊ NÃO POSSUI PROPOSTAS!")


def propostas_negociacao(estoqueadm, propostas, usuario):
    print('''
===========================
   PROPOSTA DE NEGOCIAÇÃO
===========================
01 - ENVIAR PROPOSTA
02 - VER MINHAS PROPOSTAS''')
    op_proposta = int(input("DIGITE A OPÇÃO DESEJADA: "))
    print()
    if op_proposta == 1:
        enviar_proposta(estoqueadm, propostas, usuario)
    elif op_proposta == 2:
        ver_propostas(propostas, usuario)
    else:
        print("OPÇÃO INVÁLIDA!")
