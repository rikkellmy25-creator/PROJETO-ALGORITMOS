import cadastro
import login
import funcadm
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
                    if menuadm==6:
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

                            
                

        elif perm_login==2:
            logadocliente = login.login_cliente(cliente)
            op_user=0
            while op_user>=0:
                    print(f'''
print(f"SEJA BEM VINDO!")

===============================
        MENU
===============================      
1-EFETUAR COMPRA
2-AGENDAR RETIRADA
3-FAZER PROPOSTA DE NEGOCIAÇÃO
4-VER MINHAS PROPOSTAS
6-SAIR
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
                    
                        elif op_compracliente==2:
                            animais_comprados=[]
                            total_geral=0
                            continuar="SIM"
                            while continuar=="SIM":
                                    print('''
=========================
ESTOQUE DISPONÍVEL   
=========================
    ''')
                                    if len(rebanho)==0:
                                        print("NENHUM ANIMAL DISPONÍVEL")
                                        continuar="NÃO"
                                    elif len(rebanho)>=1:
                                        for i in rebanho:
                                                    print(f'''
ID: {i[0]}
ANIMAL: {i[1]}
PESO(KG): {i[2]}
VALOR(R$): R$ {i[4]}     
                                                   ''')
                                    id_compra= int(input("DIGITE O ID DO ANIMAL QUE DESEJA ADQUIRIR: "))
                                    animal_encontrado= False
                                    for i in rebanho:
                                        if i[0]==id_compra:
                                            valor_unitario=i[4]
                                            animal_encontrado=True
                                            quant_compra=int(input("DIGITE A QUANTIDADE QUE DESEJA COMPRAR: "))
                                            if quant_compra<=0:
                                                print("QUANTIDADE INVALIDA!")
                                            elif quant_compra>i[5]:
                                                print("QUANTIDADE INVALIDA!")
                                            elif quant_compra<=i[5]:
                                                for p in propostas:
                                                    #if p[1]==usuario and p[2]==i[1] and p[6]=="ACEITA":
                                                        print(f"PROPOSTA ACEITA ENCONTRADA! O VALOR DO ANIMAL {i[1]} FOI ALTERADO PARA R${p[4]}")
                                                        valor_unitario=p[3]
                                                        break
                                                total_compra=quant_compra*valor_unitario
                                                animais_comprados.append([i[0], i[1], quant_compra, total_compra, "ANIMAL"])
                                                i[5] -= quant_compra
                                                total_geral=total_geral+total_compra
                                            print("ANIMAL ADICIONADO A COMPRA!")
                                            break
                                    if animal_encontrado==False:
                                                print("ANIMAL NÃO ENCONTRADO!")
                                    if len(animais_comprados)>0:
                                                print('''
=========================
    RESUMO DA COMPRA
=========================
''')

                                                for animal in animais_comprados:
                                                    print(f'''
ANIMAL: {animal[1]}
QUANTIDADE: {animal[2]}
TOTAL: R$ {animal[3]:.2f}
''')
                                                print(f"TOTAL GERAL: R$ {total_geral:.2f}")
                                    continuar=input("DESEJA ADICIONAR OUTRO ANIMAL?(SIM/NÃO): ").upper()
                                    if continuar=="não" or continuar=="NÃO":
                                        break


                                    if animal_encontrado==False:
                                            print("ANIMAL NÃO ENCONTRADO!")
                                            continue
                            confirmar=input("DESEJA CONFIRMAR A COMPRA? SIM/NAO: ").upper()
                            if confirmar=="SIM":
                                            id_compra_cliente=len(estoquecliente)+1
                                            estoquecliente.append([id_compra_cliente, "ANIMAL", animais_comprados, total_geral, "PENDENTE", "ANIMAL"])
                                            financeiro.append([total_geral, "PRODUTO VENDIDO", "ENTRADA"])
                                            print('''
=============================
COMPRA REALIZADA COM SUCESSO!
=============================
''')

                                            for animal in animais_comprados:
                                                print(f'''

ANIMAL: {animal[1]}
QUANTIDADE COMPRADA: {animal[2]}
VALOR TOTAL: R$ {animal[3]:.2f}
STATUS DE RETIRADA: PENDENTE
''')

                                            print(f'''
=============================
TOTAL GERAL: R$ {total_geral:.2f}
=============================
''')
                            elif confirmar=="NÃO" or confirmar=="NAO":
                                    print("COMPRA CANCELADA!")
                                    for animal in animais_comprados:
                                        for item in rebanho:
                                            if item[0] == animal[0]:
                                                item[5] += animal[2]
                    elif menu_user==2:
                        print('''
=========================
    AGENDAR RETIRADA
=========================
         ''')
                        retirada_pendente=False
                        print("RETIRADAS PENDENTES: ")
                        for i in estoquecliente:
                            if i[4]=="PENDENTE":
                                retirada_pendente=True
                                print(f'''
     ID DO PRODUTO/ANIMAL: {i[1]}
     PRODUTO: {i[2]}
     QUANTIDADE: {i[3]}
     TOTAL PAGO: R$ {i[5]}
     STATUS: {i[4]}
                    ''')
                            if retirada_pendente==False:
                                         print("NÃO POSSUI RETIRADAS !")
                            if retirada_pendente==True:
                                id_retirada=int(input("DIGITE O ID DO PRODUTO/ANIMAL QUE DESEJA AGENDAR A RETIRADA: "))
                                for i in estoquecliente:
                                    if i[0]==id_retirada and i[4]=="PENDENTE":
                                        data=input("DIGITE A DATA DA RETIRADA(AA/MM/YY): ")
                                        hora=input("DIGITE A HORA DA RETIRADA(HH:MM): ")
                                        status="PENDENTE"
                                        retiradas.append([i[1], i[2], i[3], data, hora, status])
                                        i[5]="RETIRADA AGENDADA"
                                        print(F'''
 =========================
 RETIRADA AGENDADA COM SUCESSO!
 =========================
 PRODUTO: {i[2]}
 QUANTIDADE: {i[3]}
 DATA: {data}
 HORA: {hora}
 STATUS: {status}
         ''')

                    if menu_user==3:
                            print('''
===========================
  PROPOSTA DE NEGOCIAÇÃO
===========================
01 - ENVIAR PROPOSTA
02 - VER MINHAS PROPOSTAS                                                 
                                   ''')
                            op_proposta=int(input("DIGITE A OPÇÃO DESEJADA: "))
                            print()
                            if op_proposta==1:
                                for i in estoqueadm:
                                    print(f'''
ID: {i[0]}
PRODUTO: {i[1]}
VALOR ATUAL: {i[4]}
QUANTIDADE: {i[2]}
                                ''')
                                id_proposta=int(input("DIGITE O ID DO PRODUTO QUE DESEJA ENVIAR A PROPOSTA: "))
                                produto_encontrado=False
                                for i in estoqueadm:
                                    if i[0]==id_proposta:
                                        produto_encontrado=True
                                        valor_proposta=int(input("DIGITE O VALOR DA PROPOSTA: "))
                                        desc_proposta=input("DIGITE UMA DESCRIÇÃO PARA A PROPOSTA: ")
                                        qtd_proposta=int(input("DIGITE A QUANTIDADE QUE DESEJA PROPOR: "))
                                        id_proposta=len(propostas)+1
                                    if qtd_proposta<=0:
                                        print("QUANTIDADE INVALIDA!")
                                        continue
                                    id_proposta = len(propostas)+1
                                    #propostas.append([id_proposta, usuario, i[1], valor_proposta, desc_proposta, qtd_proposta, "PENDENTE"])
                                    print("PROPOSTA ENVIADA!")
                                    print("AGUARDANDO RESPOSTA DO ADMINISTRADOR...")
                            if not produto_encontrado:
                                        print("PRODUTO NÃO ENCONTRADO!")
                            if op_proposta==2:
                                propostas_usuario=False
                                for i in propostas:
                                    #if i[1]==usuario:
                                        propostas_usuario=True
                                        print(f'''
ID: {i[0]}
PRODUTO: {i[2]}
VALOR PROPOSTO: R$ {i[3]}
DESCRIÇÃO: {i[4]}
QUANTIDADE: {i[5]}
STATUS: {i[6]}
''')                  
                                                                            


                            
                                    
                                    


                                        
                                            



                                        
        else:
            print("USUÁRIO OU SENHA INVALIDO! ")
            continue
                                            

                                    


                                        


                                        
                                                                        
                                
                                
                                        

                                
                                

                                





                
                    
                

        
                

