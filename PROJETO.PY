import cadastro
import login
import funcadm
import funcusuario
#import questionary
print("-"*50)
print("Sistema de Gestão Agropecuária (Fazenda Sertão)".upper())



iniciar=1
adm=[]
cliente=[]
rebanho=[]
estoqueadm=[]
estoquecliente=[]
financeiro=[]
vacina=[]
retiradas=[]
carac_especiais= "!@#$%&*()-_=+[]{}|;:,.<>?/"
propostas=[]
compras_cliente=[]


while iniciar!=0:
    print('''
====================
      MENU
====================      
01-CADASTRAR       
02-LOGIN           
====================               
''')
    menu=int(input("Digite a opção desejada: "))
    print()
            
    if menu==1:
        print(f'''
====================
        MENU
==================== 
01-ADM
02-CLIENTE
03-VOLTAR
====================
''')
        print()
        cadastrar=int(input("Digite a opção desejada: "))
        print()
        if cadastrar==1:
            cadastro.cadastro_adm(adm)
        elif cadastrar==2:
            cadastro.cadastro_cliente(cliente)
        elif cadastrar==3:
            continue
    if menu==2:
        print(f'''
====================
        MENU
==================== 
01-ADM
02-CLIENTE
03-VOLTAR
====================
''')
        perm_login=int(input("DIGITE A OPÇÃO DESEJADA: "))
        if perm_login==3:
            continue
        elif perm_login==1:
            logadoadm,usuario=login.login_adm(adm)
            if logadoadm==True: 
                while True:
                    funcadm.selecadm(usuario)
                    menuadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                    print()
                    #if menuadm==7:
                    if menuadm==1:
                        print("="*30)
                        print("01-ADICIONAR ANIMAL")
                        print("02-REMOVER ANIMAL")
                        print("03-EDITAR ANIMAL")
                        print("04-LISTAR ANIMAIS DO REBANHO")
                        print("05-VACINAS")
                        print("06-VOLTAR")
                        print()
                        opadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                        print()
                        if opadm==1:
                            funcadm.adicionaranimal(rebanho)
                        elif opadm==2:
                            funcadm.removeranimal(rebanho)
                        elif opadm==3:
                            funcadm.atualizaranimal(rebanho)
                        elif opadm==4:
                            funcadm.listarrebanho(rebanho)
                        elif opadm==5:
                            print()
                            print("="*10,"VACINAS","="*10)
                            print("01-REGISTRAR VACINA")
                            print("02-PROXIMAS VACINAS")
                            print("03-LISTAR VACINAS")
                            print("04-Voltar")
                            print()
                            op_vacinas=int(input("DIGITE A OPÇÃO DESEJADA: "))
                            print()
                            if op_vacinas==1:
                                funcadm.vacinaadd()
                            elif op_vacinas==2:
                                funcadm.proxvacina()
                            elif op_vacinas==3:
                                funcadm.vacinaapl()
                            elif op_vacinas==4:
                                continue
                        elif opadm==7:
                                continue
                    elif menuadm==2:
                            print("="*15,"GESTÃO PRODUÇÃO", "="*15)
                            print("01-ADICIONAR AO ESTOQUE")
                            print("02-REMOVER DO ESTOQUE")
                            print("03-ATUALIZAR QUANTIDADE DE ITENS")
                            print("04-LISTAR ESTOQUE")
                            print("05-ADICIONAR PRODUÇÃO DIÁRIA")
                            print("06-LISTAR UM PRODUTO ESPECIFICO")
                            print("07-VOLTAR")
                            print()
                            opadm=int(input("DIGITE A OPÇÃO DESEJADA:"))
                            print()
                            if opadm==1:
                                funcadm.addestoque(estoqueadm)
                            elif opadm==2:
                                funcadm.remvestoque(estoqueadm)
                            elif opadm==3:
                                funcadm.atualizarproduto(estoqueadm)
                            elif opadm==4:
                                funcadm.listarestoqueadm(estoqueadm)
                            elif opadm==5:
                                funcadm.prodiaria(estoqueadm)
                    elif menuadm==3:
                            print("MENU FINANCEIRO")
                            print("01-REGISTRAR ENTRADA")
                            print("02-REGISTRAR SAIDA")
                            print("03-VER SALDO")
                            print("04-VER TOTAL DE ENTRADAS")
                            print("05-VER TOTAL DE SAIDAS")
                            print("06-VOLTAR")
                            op_fin=int(input("DIGITE A OPÇÃO DESEJADA: "))
                            if op_fin==1:
                                funcadm.regentrada(financeiro)
                            elif op_fin==2:
                                funcadm.regsaida(financeiro)
                            elif op_fin==3:
                                funcadm.saldo(financeiro)
                            elif op_fin==4:
                                funcadm.total_entrada(financeiro)
                            elif op_fin==5:
                                funcadm.total_saida(financeiro)
                            elif op_fin==6:
                                continue
                    elif menuadm==4:
                        print('''
=================
RETIRADAS
=================
01-AGENDAR RETIRADA
02-CONFIRMAR RETIRADA
03-RETIRADAS PENDENTES
04-RETIRADAS FEITAS
05-VOLTAR
            ''')
                        op_retirada=int(input("DIGITE A OPÇÃO DESEJADA: "))
                        if op_retirada==1:
                            funcadm.retirada_agendar(retiradas)
                        elif op_retirada==2:
                            funcadm.confirm_retirada(retiradas)
                        elif op_retirada==3:
                            funcadm.pendente(retiradas)
                        elif op_retirada==4:
                            funcadm.concluida(retiradas)
                        elif op_retirada==5:
                            continue

                    elif menuadm==5:
                        print("-"*30)
                        print("RELATORIOS")
                        print("-"*30)
                        print("01-RELATÓRIO REBANHO")
                        print("02-RELATÓRIO DO ESTOQUE")
                        print("03-RELATÓRIO FINANCEIRO")
                        print("04-RELÁTORIO RETIRADAS")
                        print("05-RELATÓRIOS VACINAS")
                        print("06-VOLTAR")
                        print("-"*30)
                        op_relatorio=int(input("DIGITE A OPÇÃO DESEJADA:"))
                        if op_relatorio==1:
                           funcadm.listarrebanho
                        elif op_relatorio==2:
                            funcadm.listarestoqueadm
                        elif op_relatorio==3:
                            print("RELATÓRIO FINANCEIRO")
                            print("-"*30)
                            print("-"*30)
                            total_saida=0
                            total_entrada=0
                            for i in financeiro:
                                if i["tipo"] == "ENTRADA":
                                    total_entrada += int(i[0])
                                elif i["tipo"] == "SAIDA":
                                    total_saida += int(i[0])
                            saldo=(total_entrada-total_saida)
                            print(F"TOTAL DE ENTRADAS: {total_entrada}")
                            print(f"TOTAL DE SAIDAS: {total_saida}")
                            print(F"O SALDO ATUAL É: {saldo}")
                        elif op_relatorio==4:
                            funcadm.listar_retirada(retiradas)
                        elif op_relatorio==5:
                            print("-"*30)
                            print("RELATÓRIO VACINA")
                            print("-"*30)
                            print(f"O TOTAL DE VACINAS APLICADAS É:{len(vacina)}")
                            for i in vacina:
                                print(i)
                        elif op_relatorio==6:
                            continue
                    elif menuadm==6:
                        print("-"*30)
                        print("GESTÃO DE PROPOSTAS")
                        print("-"*30)
                        print("01-VER PROPOSTAS RECEBIDAS")
                        print("02-RESPONDER PROPOSTA")
                        print("03-VOLTAR")
                        op_proposta=int(input("DIGITE A OPÇÃO DESEJADA: "))
                        if op_proposta==1:
                            funcadm.ver_propostas(propostas)
                        elif op_proposta==2:
                            funcadm.confirm_proposta(propostas)
                        elif op_proposta==3:
                            continue
                    elif menuadm==7:
                        break

                            
                

        elif perm_login==2:
            logadocliente = login.login_cliente(cliente)
            op_user=0
            while op_user>=0:
                    print(f'''
SEJA BEM VINDO {usuario}!

===============================
        MENU
===============================      
1-EFETUAR COMPRA
2-AGENDAR RETIRADA
3-FAZER PROPOSTA DE NEGOCIAÇÃO
4-VER MINHAS PROPOSTAS
5-SAIR
==============================
        ''')
                    print()
                    menu_user=int(input("DIGITE A OPÇÃO DESEJADA: "))
                    if menu_user==6:
                         continue
                    if menu_user==1:
                        print('''
=======================
01-COMPRAR PRODUTO
02-COMPRAR ANIMAL      
=======================
                               ''')   
                        op_compracliente=int(input("DIGITE A OPÇÃO DESEJADA: "))              
                        if op_compracliente==1:
                            funcusuario.comprar_produtos(estoqueadm, estoquecliente, financeiro, propostas, cliente)
                        elif op_compracliente==2:
                            funcusuario.comprar_produtos(rebanho, estoquecliente, financeiro, propostas, cliente)
                    elif menu_user==2:
                        funcusuario.agendar_retirada(estoquecliente, retiradas)
                    if menu_user==3:
                        funcusuario.propostas_negociacao(estoqueadm, propostas, usuario)
                    elif menu_user==5:
                        break
                      
        else:
            print("USUÁRIO OU SENHA INVALIDO! ")
            continue