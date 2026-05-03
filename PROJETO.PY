print("-"*50)
print("Sistema de Gestão Agropecuária (Fazenda Sertão)".upper())

op=1

adm=[]
cliente=[]
rebanho=[]
estoque=[]
financeiro=[]
vacina=[]
retiradas=[]

while op!=0:
    print("MENU")
    print("01-CADASTRAR")
    print("02-LOGIN")
    print("03-SAIR")

    menu=int(input("Digite a opção desejada: "))

    if menu==1:
        print("01-ADM")
        print("02-CLIENTE")
        perm=int(input("Digite a opção desejada: "))
        if perm==1:
            usuario=input("DIGITE O USUARIO: ")
            senha= input("DIGITE A SUA SENHA: ")
            cadastrado=False
            for i in adm:
                if i[0]==usuario and i[1] == senha:
                    print("USUARIO JÁ CADASTRADO")
                    cadastrado=True
                    continue
            if not cadastrado:
                    adm.append([usuario,senha])
                    print("USUARIO CADASTRADO COM SUCESSO!" )
        if perm==2:
            usuario=input("DIGITE O USUARIO: ")
            senha= input("DIGITE A SUA SENHA: ")
            cadastrado=False
            for i in cliente:
                if i[0]==usuario and i[1] == senha:
                    print("USUARIO JÁ CADASTRADO")
                    cadastrado=True
                    continue
            if not cadastrado:
                    cliente.append([usuario,senha])
                    print("USUARIO CADASTRADO COM SUCESSO!" )
    if menu==2:
        print("="*50)
        print("LOGIN")
        print("01-ADM")
        print("02-CLIENTE")
        print("="*50)
        perm_login=int(input("DIGITE A OPÇÃO DESEJADA: "))
        if perm_login==1:
            login=False
            usuario=input("DIGITE SEU USUÁRIO: ")
            senha=input("DIGITE SUA SENHA: ")
            for i in adm:
                if i[0]==usuario and i[1]==senha:
                    print("LOGIN REALIZADO COM SUCESSO! ")
                    login=True
            if login:
                opadm=0
                while opadm>=0:
                        print(f"SEJA BEM VINDO {usuario}!")
                        print("="*30)
                        print("MENU ADM")
                        print("01-GERENCIAR REBANHO")
                        print("02-GERENCIAR PRODUÇÃO/ESTOQUE") 
                        print("03-FINANCEIRO")
                        #print("04-RELATÓRIOS") não sei como adicionar essa opção ainda
                        print("04-RETIRADAS")
                        menuadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                        if menuadm==1: #opção 1 do menu
                            print("="*30)
                            print("01-ADICIONAR ANIMAL")
                            print("02-REMOVER ANIMAL")
                            print("03-EDITAR ANIMAL")
                            print("04-LISTAR ANIMAIS DO REBANHO")
                            print("05-VACINAS")
                            print("06-VOLTAR")
                            opadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                            if opadm==1:
                                print("ADICIONAR ANIMAL")
                                id_animal= len(rebanho)+1
                                tipo=input("TIPO DO ANIMAL:").upper()
                                peso=input("PESO DO ANIMAL(KG):").upper()
                                gestaçao=input("O ANIMAL É GESTANTE? (SIM) OU (NÃO)").upper()
                                rebanho.append({"IDENTIFICAÇÃO DO ANIMAL":id_animal,"TIPO:":tipo,"PESO(KG)":peso,"GESTAÇÃO:":gestaçao})
                                print(F"ANIMAL ADICIONADO COM SUCESSO!")
                                print(f"ID:{id_animal}, TIPO:{tipo}, PESO:{peso},GESTANTE:{gestaçao}")
                            elif opadm==2:
                                print("REMOVER REBANHO")
                                print(rebanho)
                                existe=False
                                remv=int((input("QUAL ANIMAL VOCÊ QUER REMOVER? DIGITE O NÚMERO DE INDENTIFICAÇÃO:")))
                                for i in rebanho:
                                       if i["IDENTIFICAÇÃO DO ANIMAL"]==remv:
                                            rebanho.remove(i)
                                            existe=True
                                            print("ANIMAL REMOVIDO COM SUCESSO!")
                                            
                                if not existe:
                                     print("ANIMAL NÃO ENCONTRADO!")
                            elif opadm==3:
                                print("="*30)
                                print("EDITAR ANIMAL")
                                print(rebanho)
                                id_atualizar=int(input("DIGITE QUAL A IDENTIFICAÇÃO DO ANIMAL QUE VOCÊ QUER ATUALIZAR:"))
                                for i in rebanho:
                                     if i["IDENTIFICAÇÃO DO ANIMAL"]==id_atualizar:
                                          i["PESO(KG)"]=int(input("DIGITE O PESO ATUALIZADO DO ANIMAL: "))
                                          i["GESTAÇÃO"]=(input("DIGITE SE AINDA ESTÁ PRENHA O ANIMAL (SIM) OU (NÃO): "))
                                          print(F"ATUALIZAÇÃO BEM SUCEDIDADE{rebanho}")
                            elif opadm==4:
                                 print("="*30)
                                 print("RELATORIO DO REBANHO")
                                 print("EXISTEM",len(rebanho),"ANIMAIS NO REBANHO")
                            elif opadm==5:
                                print("="*10,"VACINAS","="*10)
                                print("01-REGISTRAR VACINA")
                                print("02-PROXIMAS VACINAS")
                                print("03-LISTAR VACINAS")
                                print("04-Voltar")
                                op_vacinas=int(input("DIGITE A OPÇÃO DESEJADA: "))
                                if op_vacinas==1:
                                    print("VACINAS")
                                    print(rebanho)
                                    reg_vacinas=int(input("DIGITE O ID DO ANIMAL PARA REGISTRAR A VACINA:"))
                                    for i in rebanho:
                                        if i["ID"]==reg_vacinas:
                                            id_animal=i["ID"]
                                            animal=input("DIGITE O TIPO DO ANIMAL:")
                                            vacina=input("DIGITE O NOME DA VACINA:")
                                            data=input("DIGITE A DATA DA VACINA(AA/MM/YY): ")
                                            prox_vacina=input("DIGITE A DATA DA PROXIMA VACINA(AA/MM/YY):")
                                        vacina.append({"ID:":id_animal,"ANIMAL:":animal,"VACINA:":vacina,"DATA":data,"PROXIMAS VACINA:":prox_vacina})
                                        print(({"ID:":id_animal,"ANIMAL:":animal,"VACINA:":vacina,"DATA":data,"PROXIMAS VACINA:":prox_vacina}))
                                elif op_vacinas==2:
                                    print("PROXIMAS VACINAS A SEREM APLICADAS")
                                    for i in vacina:
                                        if i["PROXIMAS VACINAS"]:
                                            print(F"AS PROXÍMAS VACINAS SÃO{i}")
                                elif op_vacinas==3:
                                    print("VACINAS JÁ APLICADAS")
                                    for i in vacina:
                                         if i["VACINA"]:
                                              print(i["ID"])
                                              print(i["ANIMAL"])
                                              print(i["Vacina"])
                                              print(i["DATA"])
                                elif op_vacinas==4:
                                     continue
                            elif opadm==6:
                                 continue
                        if menuadm==2:  #opção 2 do menu
                                print("="*30)
                                print("="*15,"GESTÃO PRODUÇÃO", "="*15)
                                print("01-ADICIONAR AO ESTOQUE")
                                print("02-REMOVER DO ESTOQUE")
                                print("03-ATUALIZAR QUANTIDADE DE ITENS")
                                print("04-LISTAR ESTOQUE")
                                print("05-ADICIONAR PRODUÇÃO DIÁRIA")
                                print("05-VOLTAR")
                                opadm=int(input("DIGITE A OPÇÃO DESEJADA:"))
                                if opadm==1:
                                    id_produto=len(estoque)+1
                                    produto=input("DIGITE O PRODUTO A SER ADICIONADO:  ")
                                    quantidade=int(input("DIGITE A QUANTIDADE DE ITENS: "))
                                    peso=int(input("DIGITE O PESO(KG): "))
                                    valor=int(input("DIGITE O VALOR DO PRODUTO(R$): "))
                                    validade=(input("DIGITE A VALIDADE DO PRODUTO(AA/MM/YY): "))
                                    estoque.append({F"ID:":id_produto, f"PRODUTO:":produto, f"QUANTIDADE:":quantidade,f"PESO(KG):":peso,f"VALOR(R$):":valor,f"VALIDADE(AA/MM/YY):":validade})
                                    print("Produto adicionado com sucesso:",{F"ID:":id_produto, f"PRODUTO:":produto, f"QUANTIDADE:":quantidade,f"PESO(KG):":peso,f"VALOR(R$):":valor,f"VALIDADE(AA/MM/YY):":validade})
                                elif opadm==2:
                                    print("="*15,"REMOÇÃO DE PRODUTO","="*15)
                                    print(estoque)
                                    existe=False
                                    remv_produto=int(input("DIGITE O PRODUTO QUE VOCÊ QUER REMOVER(ID):"))
                                    for i in estoque:
                                        if i["ID":id_produto]==remv_produto:
                                            estoque.remove(i)
                                            print("PRODUTO REMOVIDO COM SUCESSO!")
                                        if not existe:
                                            print("PRODUTO NÃO ENCONTRADO!")
                                elif opadm==3:
                                     print("="*15,"ATUALIZAR PRODUTO", "="*15)
                                     print(estoque)
                                     update_estoque=int(input("DIGITE QUAL O PRODUTO VOCÊ QUER ATUALIZAR(ID): "))
                                     for i in estoque:
                                        if i["ID":id_produto]==update_estoque:
                                             i["ID"]==int(input("DIGITE O ID ATUALIZADO: "))
                                             i["PRODUTO"]=input("DIGITE QUAL O PRODUTO VOCÊ QUER ATUALIZAR:")
                                             i["QUANTIDADE"]=int(input("DIGITE A QUANTIDADE ATUALIZADA DO PRODUTO: "))
                                             i["PESO"]=int(input("DIGITE O PESO DO PRODUTO ATUALIZADO(KG): "))
                                             i["VALOR"]=int(input("DIGITE O VALOR DO PRODUTO ATUALIZADO(R$): "))
                                             i["VALIDADE"]=input("DIGITE A VALIDADE ATUALIZADA DO PRODUTO(AA/MM/YY):")
                                elif opadm==4:
                                     print("="*15,"ESTOQUE","="*15)
                                     print(print(("O ESTOQUE ATUAL É:",{F"ID:":id_produto, f"PRODUTO:":produto, f"QUANTIDADE:":quantidade,f"PESO:":peso,f"VALOR:":valor})))
                                elif opadm==5:
                                     print("="*10,"PRODUÇÃO DIÁRIA",)
                                     prod_diaria=input("DIGITE O ID DO PRODUTO PRODUZIDO:")
                                     print(estoque)
                                     for i in estoque:
                                          if i[id]==prod_diaria:
                                            i["QUANTIDADE"]=int(input(f"QUAL FOI A PRODUÇÃO DIÁRIA DO {produto}? "))
                                for i in estoque:
                                    if i["PRODUTO"] in estoque<5:
                                        print(f"ALERTA!!!!!! O {i["PRODUTO"]} ESTÁ COM ESTOQUE BAIXO!")
                        if menuadm==3:
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
                                    valor=int(input("VALOR(R$):"))
                                    desc=input("DESCRIÇÃO:")
                                    tipo="ENTRADA"
                                    financeiro.append({"VALOR:":valor,"DESCRIÇÃO:":desc,"ENTRADA:":tipo})
                                    print(F"VALOR:{valor}",f"DESCRIÇÃO:{desc}", "ADICIONADOS COM SUCESSO")
                                if op_fin==2:
                                    print("REGISTRAR SAIDA")
                                    valor=int(input("VALOR(R$):"))
                                    desc=input("DESCRIÇÃO:")
                                    tipo="SAIDA"
                                    financeiro.append({"VALOR:":valor,"DESCRIÇÃO:":desc,"SAIDA":tipo})
                                    print(F"VALOR:{valor}",f"DESCRIÇÃO:{desc}", "ADICIONADOS COM SUCESSO")
                                if op_fin==3:
                                    print("SALDO")
                                    saldo=0
                                    for valor in financeiro:
                                        if valor[tipo]=="ENTRADA":
                                            saldo+=valor[tipo]
                                        elif valor[tipo]=="SAIDA":
                                            saldo-=valor[tipo]
                                    print(F"O SALDO ATUAL É {saldo}")
                                if op_fin==4:
                                    print("FILTRO POR TIPO(ENTRADA/SAIDA)")
                                    tipo=input("DIGITE QUAL O FILTRO(ENTRADA/SAIDA): ")

                                    for tipo in financeiro:
                                        if tipo["tipo"]==tipo:
                                            print(tipo)
                                if op_fin==5:
                                    total=0
                                    for i in financeiro:
                                        if i["tipo"]=="entrada":
                                            total+=i["valor"]
                                    print("TOTAL DE ENTRADAS:", total)
                                if op_fin==6:
                                    total=0
                                    for i in financeiro:
                                        if i["tipo"]=="saida":
                                            total+=i["valor"]
                                    print("TOTAL DE SAIDAS:", total)
                                if op_fin==7:
                                    continue
                            #TENHO QUE FAZER AGENDAMENTO DE RETIRADA, o menu do cliente, e ainda da uma melhorada na parte de relatorio


                                     
                                          



                                     
                                        

                                


                                      


                                      
                                                                     
                            
                            
                                       

                            
                            

                            





            if not login:
                    print("USUARIO OU SENHA INVALIDO! ")
            
                
            

    
            

