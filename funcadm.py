import login
def selecadm(usuario):
    print(f"""
SEJA BEM VINDO!
{usuario}!
===============================
        MENU ADM
01-GERENCIAR REBANHO
02-GERENCIAR PRODUÇÃO/ESTOQUE 
03-FINANCEIRO
04-RETIRADAS
05-RELATÓRIOS
06-GESTÃO DE PROPOSTAS
07-SAIR
===============================\n
""")
    return

def adicionaranimal(rebanho):
    print("ADICIONAR ANIMAL")
    id_animal= len(rebanho)+1
    tipo=input("TIPO DO ANIMAL:").upper()
    peso=int(input("PESO DO ANIMAL(KG):"))
    gestacao=input("O ANIMAL É GESTANTE? (SIM) OU (NÃO)").upper()
    valor=int(input("QUAL O VALOR? (R$) "))
    quantidade=int(input("QUAL A QUANTIDADE DE ANIMAIS? "))
    rebanho.append({"ID": id_animal, "TIPO": tipo, "PESO": peso, "GESTACAO": gestacao, "VALOR": valor, "QUANTIDADE": quantidade})
    print()
    print(F'''
ANIMAL ADICIONADO COM SUCESSO!
ID:{id_animal} 
TIPO:{tipo} 
PESO:{peso}
GESTANTE:{gestacao} 
VALOR:{valor}
QUANTIDADE:{quantidade}
''')
    return


def listarrebanho(rebanho):
    if len(rebanho)==0:
        print("NENHUM PRODUTO DISPONÍVEL!")
    for i in rebanho:
        print(f'ID: {i["ID"]} | TIPO: {i["TIPO"]} | PESO: {i["PESO"]}| GESTAÇÃO: {i["GESTACAO"]}| VALOR: {i["VALOR"]}| QUANTIDADE: {i["QUANTIDADE"]}')
    print(f'\nTOTAL DE ANIMAIS: {sum(i["QUANTIDADE"] for i in rebanho)}')

def removeranimal(rebanho):
    listarrebanho(rebanho)
    for i in rebanho:
        print(f"ID={i["ID"]}")
        print(f"TIPO={i["TIPO"]}")
        print(f"PESO={i["PESO"]}")
        print(f"GESTAÇÃO={i["GESTACAO"]}")
        print(f"VALOR={i["VALOR"]}")
        print(f"QUANTIDADE={i["QUANTIDADE"]}")
        existe=False
        print()
        remv=int((input("QUAL ANIMAL VOCÊ QUER REMOVER? DIGITE O NÚMERO DE INDENTIFICAÇÃO:")))
        print()
        for i in rebanho:
            if i["ID"]==remv:
                rebanho.remove(i)
                existe=True
            print("\nANIMAL REMOVIDO COM SUCESSO!\n")
            break

        if not existe:
            print("\nANIMAL NÃO ENCONTRADO!\n")


def atualizaranimal(rebanho):
    listarrebanho(rebanho)
    id_atualizar=int(input("DIGITE QUAL A IDENTIFICAÇÃO DO ANIMAL QUE VOCÊ QUER ATUALIZAR:"))
    animal_encontrado=False
    print()
    for i in rebanho:
        if i["ID"]==id_atualizar:
            i["PESO"]=int(input("DIGITE O PESO ATUALIZADO DO ANIMAL: "))
            i["GESTACAO"]=(input("DIGITE SE AINDA ESTÁ PRENHA O ANIMAL (SIM) OU (NÃO): "))
            i["VALOR"]=int(input("DIGITE O VALOR ATUALIZADO DO ANIMAL: "))
            i["QUANTIDADE"]=int(input("DIGITE A QUANTIDADE ATUALIZADA"))
            animal_encontrado=True
            print("\nATUALIZAÇÃO BEM SUCEDIDA\n")
            print("ID:",i["ID"])
            print("PESO:",i["PESO"])
            print("GESTACAO:",i["GESTACAO"])
            print("VALOR:",i["VALOR"])
            print("QUANTIDADE:",i["QUANTIDADE"])    
    if not animal_encontrado:
        print(f"ANIMAL COM ID - {id_atualizar} NÃO ENCONTRADO NO REBANHO.")




def vacinaadd(rebanho,vacina):
    print("VACINAS")
    listarrebanho()
    reg_vacinas=int(input("DIGITE O ID DO ANIMAL PARA REGISTRAR A VACINA:"))
    for i in rebanho:
        if i["ID"]==reg_vacinas:
            id_vacina=i["ID"]
            vacina_nome=input("DIGITE O NOME DA VACINA:")
            data=input("DIGITE A DATA DA VACINA(AA/MM/YY): ")
            prox_vacina=input("DIGITE A DATA DA PROXIMA VACINA(AA/MM/YY):")
            vacina.append({"ID":id_vacina, "VACINA":vacina_nome, "DATA":data, "PROXIMA VACINA":prox_vacina})
            print("VACINA REGISTRADO COM SUCESSO!")
            print("ID:",id_vacina)
            print("VACINA:",vacina_nome)
            print("DATA:",data)
            print("PROXIMA VACINA:",prox_vacina)


def proxvacina(vacina):
    print("PROXIMAS VACINAS A SEREM APLICADAS")
    print()
    for i in vacina:
        print(i["PROXIMA VACINAS"])




def vacinaapl(vacina):
    print("VACINAS JÁ APLICADAS")
    vacina_aplc=False
    for i in vacina:
            if i[2]:
                vacina_aplc=True
            print(i[0],i[1],i[2],i[3])
    if not vacina_aplc:
            print("NENHUMA VACINA APLICADA")




def addestoque(estoqueadm):
    id_produto=len(estoqueadm)+1
    produto=input("DIGITE O PRODUTO A SER ADICIONADO:  ")
    quantidade=int(input("DIGITE A QUANTIDADE DE ITENS: "))
    peso=int(input("DIGITE O PESO(KG/L): "))
    valor=int(input("DIGITE O VALOR DO PRODUTO(R$): "))
    validade=(input("DIGITE A VALIDADE DO PRODUTO(AA/MM/YY): "))
    estoqueadm.append({"ID":id_produto, "PRODUTO":produto, "QUANTIDADE":quantidade,"PESO":peso,"VALOR":valor,"VALIDADE":validade})
    print(f'''      
===============================
Produto adicionado com sucesso!
===============================
ID: {id_produto}
PRODUTO: {produto}
QUANTIDADE: {quantidade}
PESO(KG/L): {peso}
VALOR(R$): {valor}
VALIDADE(AA/MM/YY): {validade}
===============================
                        ''')
    


def listarestoqueadm(estoqueadm):
    if len(estoqueadm)==0:
        print("NENHUM PRODUTO DISPONÍVEL!")
    for i in estoqueadm:
        print(f'ID: {i["ID"]} | PRODUTO: {i["PRODUTO"]} | QUANTIDADE: {i["QUANTIDADE"]}')
    print(f'\nTOTAL DE PRODUTOS: {sum(i["QUANTIDADE"] for i in estoqueadm)}')


def remvestoque(estoqueadm):
    print("="*15,"REMOÇÃO DE PRODUTO","="*15)
    listarestoqueadm(estoqueadm)
    existe=False
    remv_produto=int(input("DIGITE O PRODUTO QUE VOCÊ QUER REMOVER(ID):"))
    for i in estoqueadm:
        if i[0]==remv_produto:
            estoqueadm.remove(i)
            print("PRODUTO REMOVIDO COM SUCESSO!")
            existe=True
    if not existe:
        print("PRODUTO NÃO ENCONTRADO!")


def atualizarproduto(estoqueadm):
    print("="*15,"ATUALIZAR PRODUTO", "="*15)
    listarestoqueadm
    update_estoque=int(input("DIGITE QUAL O PRODUTO VOCÊ QUER ATUALIZAR(ID): "))
    for i in estoqueadm:
        if i["ID"]==update_estoque:
                i["ID"]=int(input("DIGITE O ID ATUALIZADO: "))
                i["PRODUTO"]=input("DIGITE QUAL O NOVO PRODUTO:")
                i["QUANTIDADE"]=int(input("DIGITE A QUANTIDADE ATUALIZADA DO PRODUTO: "))
                i["PESO"]=int(input("DIGITE O PESO/VOLUME DO PRODUTO ATUALIZADO(KG/L): "))
                i["VALOR"]=int(input("DIGITE O VALOR DO PRODUTO ATUALIZADO(R$): "))
                i["VALIDADE"]=input("DIGITE A VALIDADE ATUALIZADA DO PRODUTO(AA/MM/YY):")
                print(f'''      
===============================
PRODUTO ATUALIZADO COM SUCESSO!
===============================
''')

def prodiaria(estoqueadm):
    print("="*10,"PRODUÇÃO DIÁRIA",)
    encontrado=False
    listarestoqueadm()
    prod_diaria=int(input("DIGITE O ID DO PRODUTO PRODUZIDO:"))
    for i in estoqueadm:
        if i["ID"]==prod_diaria:
            quant_diaria=int(input("QUAL FOI A PRODUÇÃO DIARIA?"))
            i["QUANTIDADE"]+=quant_diaria
            print("PRODUÇÃO DIARIA CADASTRADA COM SUCESSO")
            encontrado=True
        if not encontrado:
            print("PRODUTO NÃO ENCONTRADO!")
        for i in estoqueadm:
            if i["QUANTIDADE"]<5:
             print(f"ALERTA!!!!!! O {i[1]} ESTÁ COM ESTOQUE BAIXO!")


def regentrada(financeiro):
    print("REGISTRAR ENTRADA")
    valor=int(input("VALOR(R$): "))
    desc=input("DESCRIÇÃO: ")
    tipo="ENTRADA"
    financeiro.append({"VALOR":valor,"DESCRIÇÃO":desc, "ENTRADA":tipo})
    print(F"ENTRADA ADICIONADA COM SUCESSO")
    print(f"VALOR:{valor} | DESCRIÇÃO:{desc}  | TIPO: {tipo}")
    print("="*15)


def regsaida(financeiro):
    print("REGISTRAR saida")
    valor=int(input("VALOR(R$): "))
    desc=input("DESCRIÇÃO: ")
    tipo="SAIDA"
    financeiro.append({"VALOR":valor,"DESCRIÇÃO":desc, "SAIDA":tipo})
    print(F"ENTRADA ADICIONADA COM SUCESSO")
    print(f"VALOR:{valor} | DESCRIÇÃO:{desc}  | TIPO: {tipo}")
    print("="*15)



def saldo(financeiro):
    print("SALDO")
    saldo=0
    for item in financeiro:
        if item["ENTRADA"]=="ENTRADA":
            saldo += int(item["VALOR"])
        elif item["SAIDA"]=="SAIDA":
            saldo -= int(item["VALOR"])
    print(F"O SALDO ATUAL É {saldo} R$")




def total_entrada(financeiro):
    total=0
    for i in financeiro:
        if i["ENTRADA"]:
            total+=int(i["VALOR"])
    print("TOTAL DE ENTRADAS:", total)


def total_saida(financeiro):
    total=0
    for i in financeiro:
        if i["SAIDA"]:
            total-=int(i["VALOR"])
    print("TOTAL DE ENTRADAS:", total)