import funcadm

def compra(estoqueadm,propostas):
    produtos_comprados=[]
    total_geral=0
    continuar="SIM"
    while continuar=="SIM":
        funcadm.listarestoqueadm
        id_compra= int(input("DIGITE O ID DO PRODUTO QUE DESEJA ADQUIRIR: "))
        produto_encontrado= False
        for i in estoqueadm:
            if i["id"]==id_compra:
                produto_encontrado=True
                quant_compra=int(input("DIGITE A QUANTIDADE QUE DESEJA COMPRAR: "))
                valor_unitario=i["valor"]
                if quant_compra<=0:
                    print("QUANTIDADE INVALIDA!")
                elif quant_compra>i["quantidade"]:
                    print("QUANTIDADE INVALIDA!")
                elif quant_compra<=i["quantidade"]:
                    for p in propostas:
                        if p[1]==usuario and p[2]==i[1] and p[6]=="ACEITA":
                            print(f"PROPOSTA ACEITA ENCONTRADA! O VALOR DO PRODUTO {i[1]} FOI ALTERADO PARA R${p[3]}")
                            valor_unitario=p[3]
                            break
                    total_compra=quant_compra*valor_unitario
                    produtos_comprados.append({i[0], i[1], quant_compra, total_compra, "PRODUTO"})
                    total_geral=total_geral+total_compra
                print("PRODUTO ADICIONADO A COMPRA!")
                continuar=input("DESEJA ADICIONAR OUTRO PRODUTO?(SIM/NÃO): ").upper()
                if continuar=="SIM":
                    continue
                if len(produtos_comprados)>0:
                    print('''
=========================
RESUMO DA COMPRA
=========================
''')
                    for produto in produtos_comprados:
                        print(f'''

PRODUTO: {produto[1]}
QUANTIDADE: {produto[2]}
TOTAL: R$ {produto[3]:.2f}
''')
                    print(f"TOTAL GERAL: R$ {total_geral:.2f}")

                confirmar=input("DESEJA CONFIRMAR A COMPRA? SIM/NAO: ").upper()
                if confirmar=="NÃO" or confirmar=="NAO":
                    print("COMPRA CANCELADA!")
                elif confirmar=="SIM":
                    for produto in produtos_comprados:
                        for item in estoqueadm:
                            if item[0] == produto[0]:
                                item[2] -= produto[2]
                    id_compra_cliente=len(estoquecliente)+1
                    estoquecliente.append([id_compra_cliente, "PRODUTOS", produtos_comprados, total_geral, "PENDENTE", "PRODUTO"])
                    financeiro.append([total_geral, "PRODUTO VENDIDO", "ENTRADA"])
                print(F'''

=============================
COMPRA REALIZADA COM SUCESSO!
=============================
''')

                for produto in produtos_comprados:
                    print(f'''

PRODUTO: {produto[1]}
QUANTIDADE COMPRADA: {produto[2]}
VALOR TOTAL: R$ {produto[3]:.2f}
STATUS DE RETIRADA: PENDENTE
''')

                    print(f'''
=============================
TOTAL GERAL: R$ {total_geral:.2f}
=============================
''')
        if not produto_encontrado:
                    print("OPÇÃO INVALIDA! COMPRA CANCELADA")



