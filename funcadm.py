import login
def selecadm(usuario):
    print(f"""
\nSEJA BEM VINDO!
{usuario}!\n
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
    for i in rebanho:
        print(f"ID={i["ID"]}")
        print(f"TIPO={i["TIPO"]}")
        print(f"PESO={i["PESO"]}")
        print(f"GESTACÃO={i["GESTACAO"]}")
        print(f"VALOR={i["VALOR"]}")
        print(f"QUANTIDADE={i["QUANTIDADE"]}")
        print("="*15)
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