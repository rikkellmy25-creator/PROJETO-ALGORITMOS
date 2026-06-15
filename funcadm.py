import login
import bibliotecas
from datetime import datetime
import questionary


# ============================================================
#  CONTRATO DE DADOS (mesmas chaves usadas em main.py)
#  rebanho       -> ID, TIPO, PESO, GESTACAO, VALOR, QUANTIDADE
#  estoqueadm    -> ID, PRODUTO, QUANTIDADE, PESO, VALOR, VALIDADE
#  financeiro    -> VALOR, DESCRICAO, TIPO ("ENTRADA"/"SAIDA")
#  vacina        -> ID, VACINA, DATA, PROXIMA
#  retiradas     -> ID, TIPO, DATA, HORA, STATUS
#  propostas     -> ID, USUARIO, PRODUTO, VALOR, DESC, QUANTIDADE, STATUS
# ============================================================



def adicionaranimal(rebanho):
    print("ADICIONAR ANIMAL")
    id_animal= len(rebanho)+1
    tipo=input("TIPO DO ANIMAL: ").upper()
    peso=int(input("PESO DO ANIMAL(KG): "))
    gestacao=input("O ANIMAL É GESTANTE? (SIM) OU (NÃO): ").upper()
    valor=int(input("QUAL O VALOR? (R$) "))
    quantidade=int(input("QUAL A QUANTIDADE DE ANIMAIS? "))
    rebanho.append({"ID": id_animal, "TIPO": tipo, "PESO": peso, "GESTACAO": gestacao, "VALOR": valor, "QUANTIDADE": quantidade})
    
    print()
    print(f'''
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
        print("NENHUM ANIMAL DISPONÍVEL!")
        return
    for i in rebanho:
        print(f'ID: {i["ID"]} | TIPO: {i["TIPO"]} | PESO: {i["PESO"]} | GESTAÇÃO: {i["GESTACAO"]} | VALOR: {i["VALOR"]} | QUANTIDADE: {i["QUANTIDADE"]}')
    print(f'\nTOTAL DE ANIMAIS: {sum(i["QUANTIDADE"] for i in rebanho)}')


def removeranimal(rebanho):
    listarrebanho(rebanho)
    if len(rebanho)==0:
        return
    remv=int(input("QUAL ANIMAL VOCÊ QUER REMOVER? DIGITE O NÚMERO DE INDENTIFICAÇÃO: "))
    existe=False
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
    id_atualizar=int(input("DIGITE QUAL A IDENTIFICAÇÃO DO ANIMAL QUE VOCÊ QUER ATUALIZAR: "))
    animal_encontrado=False
    print()
    for i in rebanho:
        if i["ID"]==id_atualizar:
            i["PESO"]=int(input("DIGITE O PESO ATUALIZADO DO ANIMAL: "))
            i["GESTACAO"]=input("DIGITE SE AINDA ESTÁ PRENHA O ANIMAL (SIM) OU (NÃO): ")
            i["VALOR"]=int(input("DIGITE O VALOR ATUALIZADO DO ANIMAL: "))
            i["QUANTIDADE"]=int(input("DIGITE A QUANTIDADE ATUALIZADA: "))
            animal_encontrado=True
            print("\nATUALIZAÇÃO BEM SUCEDIDA\n")
            print("ID:",i["ID"])
            print("PESO:",i["PESO"])
            print("GESTACAO:",i["GESTACAO"])
            print("VALOR:",i["VALOR"])
            print("QUANTIDADE:",i["QUANTIDADE"])
            break
    if not animal_encontrado:
        print(f"ANIMAL COM ID - {id_atualizar} NÃO ENCONTRADO NO REBANHO.")


def vacinaadd(rebanho,vacina):
    print("VACINAS")
    listarrebanho(rebanho)
    reg_vacinas=int(input("DIGITE O ID DO ANIMAL PARA REGISTRAR A VACINA: "))
    encontrado=False
    for i in rebanho:
        if i["ID"]==reg_vacinas:
            encontrado=True
            id_vacina=i["ID"]
            vacina_nome=input("DIGITE O NOME DA VACINA: ")
            data=input("DIGITE A DATA DA VACINA(AA/MM/YY): ")
            prox_vacina=input("DIGITE A DATA DA PROXIMA VACINA(AA/MM/YY): ")
            vacina.append({"ID":id_vacina, "VACINA":vacina_nome, "DATA":data, "PROXIMA":prox_vacina})
            print("VACINA REGISTRADA COM SUCESSO!")
            print("ID:",id_vacina)
            print("VACINA:",vacina_nome)
            print("DATA:",data)
            print("PROXIMA VACINA:",prox_vacina)
            break
    if not encontrado:
        print("ANIMAL NÃO ENCONTRADO!")
def listarvacina(vacina):
    for i in vacina:
        print(f'ID: {i["ID"]} | VACINA: {i["VACINA"]} | PROXIMA: {i["PROXIMA"]}')
def proxvacina(vacina):
    print("PROXIMAS VACINAS A SEREM APLICADAS")
    print()
    if len(vacina)==0:
        print("NENHUMA VACINA REGISTRADA")
        return
    for i in vacina:
        msg=(f'ID: {i["ID"]} | VACINA: {i["VACINA"]} | PROXIMA: {i["PROXIMA"]}')
        print(msg)


def vacinaapl(vacina):
    print("VACINAS JÁ APLICADAS")
    vacina_aplc=False
    for i in vacina:
        vacina_aplc=True
        print(f'ID: {i["ID"]} | VACINA: {i["VACINA"]} | DATA: {i["DATA"]} | PROXIMA: {i["PROXIMA"]}')
    if not vacina_aplc:
        print("NENHUMA VACINA APLICADA")


def addestoque(estoqueadm):
    id_produto=len(estoqueadm)+1
    produto=input("DIGITE O PRODUTO A SER ADICIONADO: ")
    quantidade=int(input("DIGITE A QUANTIDADE DE ITENS: "))
    peso=int(input("DIGITE O PESO(KG/L): "))
    valor=int(input("DIGITE O VALOR DO PRODUTO(R$): "))
    validade=input("DIGITE A VALIDADE DO PRODUTO(AA/MM/YY): ")
    estoqueadm.append({"ID":id_produto, "PRODUTO":produto, "QUANTIDADE":quantidade, "PESO":peso, "VALOR":valor, "VALIDADE":validade})
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
        return
    for i in estoqueadm:
        print(f'ID: {i["ID"]} | PRODUTO: {i["PRODUTO"]} | QUANTIDADE: {i["QUANTIDADE"]} | VALOR: R$ {i["VALOR"]}')
    print(f'\nTOTAL DE PRODUTOS: {sum(i["QUANTIDADE"] for i in estoqueadm)}')


def remvestoque(estoqueadm):
    print("="*15,"REMOÇÃO DE PRODUTO","="*15)
    listarestoqueadm(estoqueadm)
    existe=False
    remv_produto=int(input("DIGITE O PRODUTO QUE VOCÊ QUER REMOVER(ID): "))
    for i in estoqueadm:
        if i["ID"]==remv_produto:
            estoqueadm.remove(i)
            print("PRODUTO REMOVIDO COM SUCESSO!")
            existe=True
            break
    if not existe:
        print("PRODUTO NÃO ENCONTRADO!")


def atualizarproduto(estoqueadm):
    print("="*15,"ATUALIZAR PRODUTO", "="*15)
    listarestoqueadm(estoqueadm)
    update_estoque=int(input("DIGITE QUAL O PRODUTO VOCÊ QUER ATUALIZAR(ID): "))
    encontrado=False
    for i in estoqueadm:
        if i["ID"]==update_estoque:
            encontrado=True
            i["PRODUTO"]=input("DIGITE QUAL O NOVO PRODUTO: ")
            i["QUANTIDADE"]=int(input("DIGITE A QUANTIDADE ATUALIZADA DO PRODUTO: "))
            i["PESO"]=int(input("DIGITE O PESO/VOLUME DO PRODUTO ATUALIZADO(KG/L): "))
            i["VALOR"]=int(input("DIGITE O VALOR DO PRODUTO ATUALIZADO(R$): "))
            i["VALIDADE"]=input("DIGITE A VALIDADE ATUALIZADA DO PRODUTO(AA/MM/YY): ")
            print('''      
===============================
PRODUTO ATUALIZADO COM SUCESSO!
===============================
''')
            break
    if not encontrado:
        print("PRODUTO NÃO ENCONTRADO!")


def prodiaria(estoqueadm):
    print("="*10,"PRODUÇÃO DIÁRIA")
    listarestoqueadm(estoqueadm)
    prod_diaria=int(input("DIGITE O ID DO PRODUTO PRODUZIDO: "))
    encontrado=False
    for i in estoqueadm:
        if i["ID"]==prod_diaria:
            quant_diaria=int(input("QUAL FOI A PRODUÇÃO DIARIA? "))
            i["QUANTIDADE"]+=quant_diaria
            print("PRODUÇÃO DIARIA CADASTRADA COM SUCESSO")
            encontrado=True
            break
    if not encontrado:
        print("PRODUTO NÃO ENCONTRADO!")


def regentrada(financeiro):
    print("REGISTRAR ENTRADA")
    valor=int(input("VALOR(R$): "))
    desc=input("DESCRIÇÃO: ")
    financeiro.append({"VALOR":valor, "DESCRICAO":desc, "TIPO":"ENTRADA"})
    print("ENTRADA ADICIONADA COM SUCESSO")
    print(f"VALOR: {valor} | DESCRIÇÃO: {desc} | TIPO: ENTRADA")
    print("="*15)


def regsaida(financeiro):
    print("REGISTRAR SAIDA")
    valor=int(input("VALOR(R$): "))
    desc=input("DESCRIÇÃO: ")
    financeiro.append({"VALOR":valor, "DESCRICAO":desc, "TIPO":"SAIDA"})
    print("SAIDA ADICIONADA COM SUCESSO")
    print(f"VALOR: {valor} | DESCRIÇÃO: {desc} | TIPO: SAIDA")
    print("="*15)


def saldo(financeiro):
    print("SALDO")
    saldo=0
    for item in financeiro:
        if item["TIPO"]=="ENTRADA":
            saldo += int(item["VALOR"])
        elif item["TIPO"]=="SAIDA":
            saldo -= int(item["VALOR"])
    print(f"O SALDO ATUAL É R$ {saldo}")


def total_entrada(financeiro):
    total=0
    for i in financeiro:
        if i["TIPO"]=="ENTRADA":
            total+=int(i["VALOR"])
    print("TOTAL DE ENTRADAS:", total)


def total_saida(financeiro):
    total=0
    for i in financeiro:
        if i["TIPO"]=="SAIDA":
            total+=int(i["VALOR"])
    print("TOTAL DE SAIDAS:", total)


def retirada_agendar(retiradas):
    data=input("DIGITE A DATA DA RETIRADA(AA/MM/YY): ")
    tipo_retirada=input("DIGITE O TIPO DA RETIRADA(ANIMAL/PRODUTO): ").upper()
    hora=input("DIGITE A HORA DA RETIRADA(HH:MM:SS): ")
    id_retirada=int(input("DIGITE O ID DO PRODUTO/ANIMAL À SER EFETUADO A RETIRADA: "))
    retiradas.append({"ID":id_retirada, "TIPO":tipo_retirada, "DATA":data, "HORA":hora, "STATUS":"PENDENTE"})
    print(f"RETIRADA AGENDADA COM SUCESSO PARA {data}, às {hora}")


def listar_retirada(retiradas):
    if len(retiradas)==0:
        print("NENHUMA RETIRADA AGENDADA")
        return
    for i in retiradas:
        if i["STATUS"]=="PENDENTE":
            print(f'ID: {i["ID"]} | TIPO: {i["TIPO"]} | HORA: {i["HORA"]} | DATA: {i["DATA"]}')


def confirm_retirada(retiradas):
    if len(retiradas)==0:
        print("NENHUMA RETIRADA AGENDADA")
        return
    listar_retirada(retiradas)
    id_confretirada=int(input("DIGITE O ID DA RETIRADA A SER CONFIRMADA: "))
    existe=False
    for i in retiradas:
        if i["ID"]==id_confretirada:
            i["STATUS"]="CONCLUIDA"
            existe=True
            print("RETIRADA FEITA COM SUCESSO!")
            break
    if not existe:
        print("RETIRADA NÃO ENCONTRADA!")


def pendente(retiradas):
    pendente=[]
    for i in retiradas:
        if i["STATUS"]=="PENDENTE":
            pendente.append(i)
    print(f"AS RETIRADAS PENDENTES SÃO: {pendente}")


def concluida(retiradas):
    concluidas=[]
    for i in retiradas:
        if i["STATUS"]=="CONCLUIDA":
            concluidas.append(i)
    print(f"AS RETIRADAS CONCLUIDAS SÃO: {concluidas}")


def ver_propostas(propostas):
    if len(propostas)==0:
        print("NENHUMA PROPOSTA RECEBIDA!")
        return
    for i in propostas:
        print(f'ID: {i["ID"]} | USUÁRIO: {i["USUARIO"]} | PRODUTO: {i["PRODUTO"]} | VALOR: R$ {i["VALOR"]} | DESCRIÇÃO: {i["DESC"]} | QUANTIDADE: {i["QUANTIDADE"]} | STATUS: {i["STATUS"]}')


def confirm_proposta(propostas):
    if len(propostas)==0:
        print("NENHUMA PROPOSTA RECEBIDA!")
        return
    ver_propostas(propostas)
    id_proposta=int(input("DIGITE O ID DA PROPOSTA QUE DESEJA RESPONDER: "))
    proposta_encontrada=False
    for i in propostas:
        if i["ID"]==id_proposta:
            print(f'PROPOSTA ENCONTRADA! USUÁRIO: {i["USUARIO"]} | PRODUTO: {i["PRODUTO"]} | DESCRIÇÃO: {i["DESC"]} | VALOR PROPOSTO: R$ {i["VALOR"]} | STATUS: {i["STATUS"]}')
            resposta=input("DIGITE SUA RESPOSTA (ACEITAR/REJEITAR): ").upper()
            if resposta=="ACEITAR":
                i["STATUS"]="ACEITA"
                print("PROPOSTA ACEITA COM SUCESSO!")
            elif resposta=="REJEITAR":
                i["STATUS"]="REJEITADA"
                print("PROPOSTA REJEITADA COM SUCESSO!")
            proposta_encontrada=True
            break
    if not proposta_encontrada:
        print("PROPOSTA NÃO ENCONTRADA!")
    

def registrar_historico(historico,acao, item, qtd):
    historico.append({"data": datetime.now().strftime("%d/%m %H:%M"),"acao": acao,"item": item,"qtd": qtd})