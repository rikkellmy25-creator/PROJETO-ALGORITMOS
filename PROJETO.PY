print("-"*50)
print("Sistema de Gestão Agropecuária (Fazenda Sertão)".upper())

op=1

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

while op!=0:
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
            usuario=input("DIGITE O USUARIO: ")
            senha= input("DIGITE A SUA SENHA(8 DÍGITOS, 1 LETRA MAISCULA E 01 CARACTERE ESPECIAL): ")
            cadastrado=False
            maiuscula_user=False
            maiuscula_senha=False
            senha_espec=False
            user_espec=False
            for i in usuario:
                 if i.isupper():
                      maiuscula_user=True
                 continue
            if len(usuario)<5:
                 print()
                 print("USUARIO INVALIDO, MÍNIMO 5 DÍGITOS")
                 print()
                 continue
            for i in senha:
                if i.isupper():
                      maiuscula_senha=True
                if i in carac_especiais:
                     senha_espec=True
            if len(senha)<8 or not maiuscula_senha or not senha_espec:
                 print()
                 print("SENHA INVALIDA!!")
                 print()
                 continue
                     
            
            for i in adm:
                if i[0]==usuario and i[1] == senha:
                    print()
                    print("USUARIO JÁ CADASTRADO")
                    print()
                    cadastrado=True
                    continue
            if not cadastrado:
                    adm.append([usuario,senha])
                    print()
                    print("USUARIO CADASTRADO COM SUCESSO!" )
                    print()
        elif cadastrar==2:
            print()
            usuario=input("DIGITE O USUARIO: ")
            senha= input("DIGITE A SUA SENHA(8 DÍGITOS, 1 LETRA MAISCULA E 01 CARACTERE ESPECIAL): ")
            print()
            cadastrado=False
            maiuscula_user=False
            maiuscula_senha=False
            senha_espec=False
            user_espec=False
            for i in usuario:
                 if i.isupper():
                      maiuscula_user=True
                 continue
            if len(usuario)<5:
                 print()
                 print("USUARIO INVALIDO, MÍNIMO 5 DÍGITOS")
                 print()
                 continue
            for i in senha:
                if i.isupper():
                      maiuscula_senha=True
                if i in carac_especiais:
                     senha_espec=True
            if len(senha)<8 or not maiuscula_senha or not senha_espec:
                 print("SENHA INVALIDA")
                 continue
            for i in cliente:
                if i[0]==usuario and i[1] == senha:
                    print("USUARIO JÁ CADASTRADO")
                    cadastrado=True
                    continue
            if not cadastrado:
                    cliente.append([usuario,senha])
                    print("USUARIO CADASTRADO COM SUCESSO!") 
        elif cadastrar==3:
             continue
            
    if menu==2:
        loginadm = False
        loginusuario = False
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
            usuario=input("DIGITE SEU USUÁRIO: ")
            senha=input("DIGITE SUA SENHA: ")
            for i in adm:
                if i[0]==usuario and i[1]==senha:
                    print("LOGIN REALIZADO COM SUCESSO! ")
                    loginadm=True
        if perm_login==2:
            usuario=input("DIGITE SEU USUÁRIO: ")
            senha=input("DIGITE SUA SENHA: ")
            for i in cliente:
                if i[0]==usuario and i[1]==senha:
                    print("LOGIN REALIZADO COM SUCESSO! ")
                    loginusuario=True
        if loginadm==True:
                opadm=0
                while opadm>=0:
                        print()
                        print(f"SEJA BEM VINDO {usuario}!")
                        print("="*30)
                        print("MENU ADM")
                        print("01-GERENCIAR REBANHO")
                        print("02-GERENCIAR PRODUÇÃO/ESTOQUE") 
                        print("03-FINANCEIRO")
                        print("04-RETIRADAS")
                        print("05-RELATÓRIOS")
                        print("05-SAIR")
                        print()
                        menuadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                        print()
                        if menuadm==6:
                            break
                        elif menuadm==1: #opção 1 do menu
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
                                print("ADICIONAR ANIMAL")
                                id_animal= len(rebanho)+1
                                tipo=input("TIPO DO ANIMAL:").upper()
                                peso=input("PESO DO ANIMAL(KG):")
                                gestaçao=input("O ANIMAL É GESTANTE? (SIM) OU (NÃO)").upper()
                                valor=int(input("QUAL O VALOR? (R$) "))
                                rebanho.append([id_animal,tipo,peso,gestaçao, valor])
                                print()
                                print(F"ANIMAL ADICIONADO COM SUCESSO!")
                                print(f"ID:{id_animal}, TIPO:{tipo}, PESO:{peso},GESTANTE:{gestaçao}, VALOR:{valor}")
                                print()
                            elif opadm==2:
                                print("REMOVER REBANHO")
                                for i in rebanho:
                                            print(f'''
ID={i[0]}
TIPO={i[1]}
PESO={i[2]}
GESTAÇÃO={i[3]}
VALOR={i[4]}  
                ''')
                                existe=False
                                print()
                                remv=int((input("QUAL ANIMAL VOCÊ QUER REMOVER? DIGITE O NÚMERO DE INDENTIFICAÇÃO:")))
                                print()
                                for i in rebanho:
                                       if i[0]==remv:
                                            rebanho.remove(i)
                                            existe=True
                                            print()
                                            print("ANIMAL REMOVIDO COM SUCESSO!")
                                            print()
                                            
                                if not existe:
                                     print()
                                     print("ANIMAL NÃO ENCONTRADO!")
                                     print()
                            elif opadm==3:
                                print("="*30)
                                print("EDITAR ANIMAL")
                                for i in rebanho:
                                            print(f'''
ID={i[0]}
TIPO={i[1]}
PESO={i[2]}
GESTAÇÃO={i[3]}  
''')
                                print()
                                id_atualizar=int(input("DIGITE QUAL A IDENTIFICAÇÃO DO ANIMAL QUE VOCÊ QUER ATUALIZAR:"))
                                animal_encontrado=False
                                print()
                                for i in rebanho:
                                     if i[0]==id_atualizar:
                                          i[2]=int(input("DIGITE O PESO ATUALIZADO DO ANIMAL: "))
                                          i[3]=(input("DIGITE SE AINDA ESTÁ PRENHA O ANIMAL (SIM) OU (NÃO): "))
                                          i[4]=int(input("DIGITE O VALOR ATUALIZADO DO ANIMAL: "))
                                          animal_encontrado=True
                                          print(f'''
ATUALIZAÇÃO BEM SUCEDIDA!
ID:{i[0]}
PESO:{i[2]}
GESTANTE:{i[3]}                                            
''')
                                if not animal_encontrado:
                                       print(f"ANIMAL COM ID {id_atualizar} NÃO ENCONTRADO NO REBANHO.")
                            elif opadm==4:
                                 print('''
==================
RELATÓRIO REBANHO
==================                                       
                                       ''')
                                 
                                 for i in rebanho:
                                    print(f'''
ID={i[0]}
TIPO={i[1]}
PESO={i[2]}
GESTAÇÃO={i[3]} 
EXISTEM {len(rebanho)} ANIMAIS NO REBANHO! 
''')
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
                                    print("VACINAS")
                                    for i in rebanho:
                                        print(f'''
ID={i[0]}
TIPO={i[1]}
''')
                                    reg_vacinas=int(input("DIGITE O ID DO ANIMAL PARA REGISTRAR A VACINA:"))
                                    for i in rebanho:
                                        if i[0]==reg_vacinas:
                                            id_animal=i[0]
                                            vacina_nome=input("DIGITE O NOME DA VACINA:")
                                            data=input("DIGITE A DATA DA VACINA(AA/MM/YY): ")
                                            prox_vacina=input("DIGITE A DATA DA PROXIMA VACINA(AA/MM/YY):")
                                            vacina.append([id_animal, vacina_nome, data, prox_vacina])
                                    print("VACINA REGISTRADO COM SUCESSO!")
                                elif op_vacinas==2:
                                    print("PROXIMAS VACINAS A SEREM APLICADAS")
                                    print()
                                    for i in vacina:
                                        if i[3]:
                                            print(F"AS PROXÍMAS VACINAS SÃO: {i[3]}")
                                elif op_vacinas==3:
                                    print("VACINAS JÁ APLICADAS")
                                    vacina_aplc=False
                                    for i in vacina:
                                         if i[2]:
                                            vacina_aplc=True
                                            print(i[0],i[1],i[2],i[3])
                                    if not vacina_aplc:
                                         print("NENHUMA VACINA APLICADA")
                                elif op_vacinas==4:
                                     continue
                            elif opadm==6:
                                 continue
                        elif menuadm==2:
                                print("="*15,"GESTÃO PRODUÇÃO", "="*15)
                                print("01-ADICIONAR AO ESTOQUE")
                                print("02-REMOVER DO ESTOQUE")
                                print("03-ATUALIZAR QUANTIDADE DE ITENS")
                                print("04-LISTAR ESTOQUE")
                                print("05-ADICIONAR PRODUÇÃO DIÁRIA")
                                print("05-VOLTAR")
                                print()
                                opadm=int(input("DIGITE A OPÇÃO DESEJADA:"))
                                print()
                                if opadm==1:
                                    id_produto=len(estoqueadm)+1
                                    produto=input("DIGITE O PRODUTO A SER ADICIONADO:  ")
                                    quantidade=int(input("DIGITE A QUANTIDADE DE ITENS: "))
                                    peso=int(input("DIGITE O PESO(KG/L): "))
                                    valor=int(input("DIGITE O VALOR DO PRODUTO(R$): "))
                                    validade=(input("DIGITE A VALIDADE DO PRODUTO(AA/MM/YY): "))
                                    estoqueadm.append([id_produto, produto, quantidade,peso,valor,validade])
                                    print(f'''      
===============================
Produto adicionado com sucesso!
===============================
ID:{id_produto}
PRODUTO:{produto}
QUANTIDADE:{quantidade}
PESO(KG/L):{peso}
VALOR(R$):{valor}
VALIDADE(AA/MM/YY):{validade}
===============================
                            ''')
                                elif opadm==2:
                                    print("="*15,"REMOÇÃO DE PRODUTO","="*15)
                                    for i in estoqueadm:
                                            print(f'''
ID: {i[0]}
PRODUTO: {i[1]}
QUANTIDADE:{i[2]}
PESO(KG/L): {i[3]}
VALOR(R$): R$ {i[4]}
VALIDADE: {i[5]})
TOTAL DE PRODUTOS: {len(estoqueadm)}     
''')
                                    existe=False
                                    remv_produto=int(input("DIGITE O PRODUTO QUE VOCÊ QUER REMOVER(ID):"))
                                    for i in estoqueadm:
                                        if i[0]==remv_produto:
                                            estoqueadm.remove(i)
                                            print("PRODUTO REMOVIDO COM SUCESSO!")
                                            existe=True
                                        if not existe:
                                            print("PRODUTO NÃO ENCONTRADO!")
                                elif opadm==3:
                                    print("="*15,"ATUALIZAR PRODUTO", "="*15)
                                    for i in estoqueadm:
                                            print(f'''
ID: {i[0]}
PRODUTO: {i[1]}
QUANTIDADE:{i[2]}
PESO(KG/L): {i[3]}
VALOR(R$): R$ {i[4]}
VALIDADE: {i[5]})
TOTAL DE PRODUTOS: {len(estoqueadm)}     
''')
                                    update_estoque=int(input("DIGITE QUAL O PRODUTO VOCÊ QUER ATUALIZAR(ID): "))
                                    for i in estoqueadm:
                                        if i[0]==update_estoque:
                                             i[0]=int(input("DIGITE O ID ATUALIZADO: "))
                                             i[1]=input("DIGITE QUAL O NOVO PRODUTO:")
                                             i[2]=int(input("DIGITE A QUANTIDADE ATUALIZADA DO PRODUTO: "))
                                             i[3]=int(input("DIGITE O PESO/VOLUME DO PRODUTO ATUALIZADO(KG/L): "))
                                             i[4]=int(input("DIGITE O VALOR DO PRODUTO ATUALIZADO(R$): "))
                                             i[5]=input("DIGITE A VALIDADE ATUALIZADA DO PRODUTO(AA/MM/YY):")
                                             print(f'''      
===============================
PRODUTO ATUALIZADO COM SUCESSO!
===============================
''')
                                elif opadm==4:
                                    print("="*15,"ESTOQUE","="*15)
                                    if len(estoqueadm)==0:
                                        print("NENHUM PRODUTO DISPONÍVEL!")
                                    else:
                                        for i in estoqueadm:
                                            print(f'''
ID: {i[0]}
PRODUTO: {i[1]}
QUANTIDADE:{i[2]}
PESO(KG/L): {i[3]}
VALOR(R$): R$ {i[4]}
VALIDADE: {i[5]}
TOTAL DE PRODUTOS: {len(estoqueadm)}     
''')
                                elif opadm==5:
                                    print("="*10,"PRODUÇÃO DIÁRIA",)
                                    encontrado=False
                                    for i in estoqueadm:
                                            print(f'''
ID: {i[0]}
PRODUTO: {i[1]}
QUANTIDADE:{i[2]}
PESO(KG/L): {i[3]}
VALOR(R$): R$ {i[4]}
VALIDADE: {i[5]}
TOTAL DE PRODUTOS: {len(estoqueadm)}     
                                            ''')
                                    prod_diaria=int(input("DIGITE O ID DO PRODUTO PRODUZIDO:"))
                                    for i in estoqueadm:
                                        if i[0]==prod_diaria:
                                            quant_diaria=int(input("QUAL FOI A PRODUÇÃO DIARIA?"))
                                            i[2]+=quant_diaria
                                            print("PRODUÇÃO DIARIA CADASTRADA COM SUCESSO")
                                            encontrado=True
                                    if not encontrado:
                                            print("PRODUTO NÃO ENCONTRADO!")
                                for i in estoqueadm:
                                    if i[2]<5:
                                        print(f"ALERTA!!!!!! O {i[1]} ESTÁ COM ESTOQUE BAIXO!")
                        elif menuadm==3:
                                print("MENU FINANCEIRO")
                                print("01-REGISTRAR ENTRADA")
                                print("02-REGISTRAR SAIDA")
                                print("03-VER SALDO")
                                print("04-FILTRAR POR TIPO(ENTRADA/SAIDA)")
                                print("05-VER TOTAL DE ENTRADAS")
                                print("06-VER TOTAL DE SAIDAS")
                                print("07-VOLTAR")
                                op_fin=int(input("DIGITE A OPÇÃO DESEJADA: "))

                                if op_fin==1:
                                    print("REGISTRAR ENTRADA")
                                    valor=int(input("VALOR(R$): "))
                                    desc=input("DESCRIÇÃO: ")
                                    financeiro.append([valor,desc, "ENTRADA"])
                                    print(F"ENTRADA ADICIONADA COM SUCESSO")
                                elif op_fin==2:
                                    print("REGISTRAR SAIDA")
                                    valor=int(input("VALOR(R$):"))
                                    desc=input("DESCRIÇÃO:")
                                    tipo="SAIDA"
                                    financeiro.append([valor,desc,"SAIDA"])
                                    print("SAIDA ADICIONADA COM SUCESSO")
                                elif op_fin==3:
                                    print("SALDO")
                                    saldo=0
                                    for item in financeiro:
                                        if item[2]=="ENTRADA":
                                            saldo += int(item[0])
                                        elif item[2]=="SAIDA":
                                            saldo -= int(item[0])
                                    print(F"O SALDO ATUAL É {saldo} R$")
                                if op_fin==4:
                                    print("FILTRO POR TIPO(ENTRADA/SAIDA)")
                                    tipo=input("DIGITE QUAL O FILTRO(ENTRADA/SAIDA): ").upper()
                                    existe=False
                                    for i in financeiro:
                                        if i[2]==tipo:
                                            print(f"VALOR: R${i[0]} | DESCRIÇÃO: {i[1]} | TIPO: {i[2]}")
                                            existe=True
                                    if not existe:
                                        print(f"NENHUM REGISTRO DO TIPO {tipo} ENCONTRADO!")
                                if op_fin==5:
                                    total=0
                                    for i in financeiro:
                                        if i[2]=="ENTRADA":
                                            total+=int(i[0])
                                    print("TOTAL DE ENTRADAS:", total)
                                if op_fin==6:
                                    total=0
                                    for i in financeiro:
                                        if i[2]=="SAIDA":
                                            total+=int(i[0])
                                    print("TOTAL DE SAIDAS:", total)
                                if op_fin==7:
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
                                data=input("DIGITE A DATA DA RETIRADA(AA/MM/YY): ")
                                tipo_retirada=input("DIGITE O TIPO DA RETIRADA(ANIMAL/PRODUTO): ")
                                hora=input("DIGITE A HORA DA RETIRADA(HH:MM:SS):")
                                id_retirada=int(input("DIGITE O ID DO PRODUTO/ANIMAL À SER EFETUADO A RETIRADA:"))
                                status="PENDENTE"
                                retiradas.append([data,tipo_retirada,hora, id_retirada,status])
                                print(F"RETIRADA AGENDADA COM SUCESSO PARA {data}, às {hora}")
                            elif op_retirada==2:
                                if len(retiradas)==0:
                                    print("NENHUMA RETIRADA AGENDADA")
                                elif len(retiradas)>=1:
                                    for i in retiradas:
                                        if i[3]=="PENDENTE":
                                            print(f"ID:{i[3]}| TIPO:{i[1]}|HORA:{i[2]}|DATA:{i[0]}")
                                id_confretirada=int(input("DIGITE O ID DA RETIRADA A SER CONFIRMADA:"))
                                existe=False
                                for i in retiradas:
                                    if i[2]==id_confretirada:
                                        i[4]="CONCLUIDA"
                                        existe=True
                                        print("RETIRADA FEITA COM SUCESSO!")
                                        continue
                                    if not existe:
                                        print("RETIRADA NÃO ENCONTRADA!")
                                        continue
                            elif op_retirada==3:
                                pendente=[]
                                for i in retiradas:
                                    if i[4]=="PENDENTE":
                                        pendente.append(i)
                                print(f"AS RETIRADAS PENDENTE SÃO {pendente}")
                            elif op_retirada==4:
                                concluidas=[]
                                for i in retiradas:
                                    if i[4]=="CONCLUIDA":
                                        concluidas.append(i)
                                print(f"AS RETIRADAS CONCLUIDAS SÃO {concluidas}")

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
                                print("-"*30)
                                print("RELATÓRIO REBANHO")
                                print("-"*30)
                                print(f"O TOTAL DE ANIMAIS É:{len(rebanho)}")
                                for i in rebanho:
                                    print(i)
                            elif op_relatorio==2:
                                print("-"*30)
                                print("RELATÓRIO ESTOQUE")
                                print("-"*30)
                                print(f"O TOTAL DE PRODUTOS É:{len(estoqueadm)}")
                                for i in estoqueadm:
                                    print(i)
                            elif op_relatorio==3:
                                print("-"*30)
                                print("RELATÓRIO FINANCEIRO")
                                print("-"*30)
                                total_saida=0
                                total_entrada=0
                                for i in financeiro:
                                    if i[2] == "ENTRADA":
                                        total_entrada += int(i[0])
                                    elif i[2] == "SAIDA":
                                        total_saida += int(i[0])
                                saldo=(total_entrada-total_saida)
                                print(F"TOTAL DE ENTRADAS: {total_entrada}")
                                print(f"TOTAL DE SAIDAS: {total_saida}")
                                print(F"O SALDO ATUAL É: {saldo}")
                            elif op_relatorio==4:
                                print("-"*30)
                                print("RELATÓRIO DE RETIRADA")
                                print("-"*30)

                                pendente=[]
                                for i in retiradas:
                                    if i[4]=="PENDENTE":
                                        pendente.append(i)
                                    print(f"AS RETIRADAS PENDENTE SÃO {pendente}")
                                concluidas=[]
                                for i in retiradas:
                                    if i[4]=="CONCLUIDA":
                                        concluidas.append(i)
                                        print("-"*30)
                                        print(f"AS RETIRADAS CONCLUIDAS SÃO {concluidas}")
                                        print("-"*30)
                                print(F"RETIRADAS CONCLUIDAS: {len(concluidas)}")
                                print(F"RETIRADAS PENDENTES: {len(pendente)}")
                            elif op_relatorio==5:
                                print("-"*30)
                                print("RELATÓRIO VACINA")
                                print("-"*30)
                                print(f"O TOTAL DE VACINAS APLICADAS É:{len(vacina)}")
                                for i in vacina:
                                    print(i)
                            elif op_relatorio==6:
                                continue

        elif loginusuario==True:
                op_user=0
                while op_user>=0:
                    print(f'''
SEJA BEM VINDO {usuario}

====================
        MENU
====================      
1-EFETUAR COMPRA
2-AGENDAR RETIRADA
3-SIMULADOR DE PREÇO
4-FAZER PROPOSTA DE NEGOCIAÇÃO
5-VER MINHAS PROPOSTAS
6-PAINEL DO CLIENTE
7-SAIR
==================
        ''')
                    print()
                    menu_user=int(input("DIGITE A OPÇÃO DESEJADA: "))
                    if menu_user==3:
                         continue
                    if menu_user==1:
                        print('''
01-COMPRAR PRODUTO
02-COMPRAR ANIMAL      
                               ''')  
                        op_compracliente=int(input("DIGITE A OPÇÃO DESEJADA: "))              
                        if op_compracliente==1:
                            produtos_comprados=[]
                            total_geral=0
                            continuar="SIM"
                            while continuar=="SIM":
                                    print('''
=========================
ESTOQUE DISPONÍVEL   
=========================
    ''')
                                    if len(estoqueadm)==0:
                                        print("NENHUM PRODUTO DISPONÍVEL")
                                        continuar=="NÃO"
                                    elif len(estoqueadm)>=1:
                                        for i in estoqueadm:
                                                    print(f'''
ID: {i[0]})
PRODUTO: {i[1]})
QUANTIDADE:{i[2]})
PESO(KG): {i[3]})
VALOR(R$): R$ {i[4]})
VALIDADE: {i[5]}) 
TOTAL DE PRODUTOS: {len(estoqueadm)}     
                                                    ''')
                                    id_compra= int(input("DIGITE O ID DO PRODUTO QUE DESEJA ADQUIRIR: "))
                                    produto_existe= False
                                    for i in estoqueadm:
                                        if i[0]==id_compra:
                                            produto_encontrado=True
                                            quant_compra=int(input("DIGITE A QUANTIDADE QUE DESEJA COMPRAR: "))
                                        if quant_compra<=0:
                                            print("QUANTIDADE INVALIDA!")
                                        elif quant_compra>i[2]:
                                            print("QUANTIDADE INVALIDA!")
                                        elif quant_compra<=i[2]:
                                            total_compra=quant_compra*i[4]
                                            produtos_comprados.append([i[0], i[1], quant_compra, total_compra, "PRODUTO"])
                                            total_geral=total_geral+total_compra
                                            print("PRODUTO ADICIONADO A COMPRA!")
                                        if produto_encontrado==False:
                                            print("PRODUTO NÃO ENCONTRADO!")
                                        continuar=input("DESEJA ADICIONAR OUTRO PRODUTO?(SIM/NÃO): ").upper()
                                        if len(produtos_comprados)>0:
                                            print(f'''
=========================
    RESUMO DA COMPRA
=========================
PRODUTO: {i[1]}
QUANTIDADE: {quant_compra}
VALOR UNITÁRIO: R$ {i[4]}
TOTAL: R$ {total_compra}
    ''')
                                            confirmar=input("DESEJA CONFIRMAR A COMPRA? SIM/NAO: ").upper()
                                            if confirmar=="SIM":
                                                id_compra_cliente=len(estoquecliente)+1
                                                estoquecliente.append([id_compra_cliente, usuario, "PRODUTOS", produtos_comprados, total_geral, "PENDENTE", "PRODUTO"])
                                                for produto in produtos_comprados:
                                                    for i in estoqueadm:
                                                        if i[0]==produto[0]:
                                                            i[2]=i[2]-produto[2]
                                                i[2]=i[2]-quant_compra
                                                financeiro.append([total_compra, "PRODUTO VENDIDO", "ENTRADA"])
                                            print(F'''
=========================
COMPRA REALIZADA COM SUCESSO!
=========================
PRODUTO: {i[1]}")
QUANTIDADE COMPRADA: {quant_compra}")
VALOR TOTAL: R$ {total_compra}")
STATUS DE RETIRADA: PENDENTE")                                  
        ''')
                                        elif confirmar=="NÃO":
                                                print("COMPRA CANCELADA!")
                                        else:
                                                print("OPÇÃO INVALIDA! COMPRA CANCELADA")
                                        if produto_encontrado==False:
                                                print("PRODUTO/ANIMAL NÃO ENCONTRADO!")
                            if op_compracliente==2:
                                print('''
    =========================
    ESTOQUE DISPONÍVEL   
    =========================
        ''')
                                if len(rebanho)==0:
                                    print("NENHUM PRODUTO DISPONÍVEL")
                                elif len(rebanho)>=1:
                                    for i in rebanho:
                                                    print(f'''
    ID: {i[0]})
    ANIMAL: {i[1]})
    PESO(KG): {i[2]})
    GESTANTE: {i[3]}) 
    VALOR(R$): R$ {i[4]})
    TOTAL DE PRODUTOS: {len(rebanho)}     
                                                    ''')
                                id_compra= int(input("DIGITE O ID DO PRODUTO QUE DESEJA ADQUIRIR: "))
                                produto_existe= False
                                for i in rebanho:
                                    if i[0]==id_compra:
                                        produto_existe=True
                                        quant_compra=int("DIGITE A QUANTIDADE QUE DESEJA COMPRAR: ")
                                        if quant_compra<=0:
                                            print("QUANTIDADE INVALIDA!")
                                        elif quant_compra>i[2]:
                                            print("QUANTIDADE ")
                                        elif quant_compra<=i[2]:
                                            total_compra=quant_compra*i[4]
                                            print(f'''
    =========================
        RESUMO DA COMPRA
    =========================
    ANIMAL: {i[1]}
    QUANTIDADE: {quant_compra}
    VALOR UNITÁRIO: R$ {i[4]}
    TOTAL: R$ {total_compra}
        ''')
                                            confirmar=input("DESEJA CONFIRMAR A COMPRA? SIM/NAO: ").upper()
                                            if confirmar=="SIM":
                                                estoquecliente.append([i[0],i[1],quant_compra,total_compra,"PENDENTE"])
                                                i[2]=i[2]-quant_compra
                                                financeiro.append([total_compra, "PRODUTO VENDIDO", "ENTRADA"])
                                                print(F'''
    =========================
    COMPRA REALIZADA COM SUCESSO!
    =========================
    PRODUTO: {i[1]}")
    QUANTIDADE COMPRADA: {quant_compra}")
    VALOR TOTAL: R$ {total_compra}")
    STATUS DE RETIRADA: PENDENTE")                                  
        ''')
                                            elif confirmar=="NÃO":
                                                print("COMPRA CANCELADA!")
                                            else:
                                                print("OPÇÃO INVALIDA! COMPRA CANCELADA")
                                            if produto_encontrado==False:
                                                print("PRODUTO/ANIMAL NÃO ENCONTRADO!")
                                print('''
        =========================
            AGENDAR RETIRADA
        =========================
        ''')
                                retirada_pendente=False
                                print("RETIRADAS PENDENTES: ")
                                for i in estoquecliente:
                                    if i[5]=="ABERTO":
                                        retirada_pendente:True
                                        print(f'''
    ID DO PRODUTO/ANIMAL: {i[1]}
    PRODUTO: {i[2]}
    QUANTIDADE: {i[3]}
    TOTAL PAGO: R$ {i[4]}
    STATUS: {i[5]}
                    ''')
                                    if retirada_pendente==False:
                                        print("NÃO POSSUI RETIRADAS PENDENTE!")
                                    if retirada_pendente==True:
                                        for i in estoquecliente:
                                            if i[1]==id_retirada and i[5]=="ABERTO":
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

                        #if menu_user==3:
                                                                                


                                
                                        
                                        


                                            
                                                



                                            
                                                

                                        


                                            


                                            
                                                                            
                                    
                                    
                                            

                                    
                                    

                                    



    elif not loginadm:
        print("USUARIO OU SENHA INVALIDO! ")
        continue
    elif not loginusuario:
        print("USUARIO OU SENHA INVALIDO! ")
        continue

                    
                        
                    

            
                    

