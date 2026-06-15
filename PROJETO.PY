import cadastro
import login
import funcadm
import funcusuario
import bibliotecas
import questionary
import assistentedeia
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
historico=[]


while iniciar!=0:
    menu=questionary.select("MENU", choices=[
        "CADASTRO",
        "LOGIN",
        "SAIR",
    ]).ask()
    if menu=="SAIR":
        break
    if menu=="CADASTRO":
        cadastrar=questionary.select("CADASTRO",choices=[
            "ADM",
            "CLIENTE",
            "VOLTAR"
        ]).ask()
        if cadastrar=="ADM":
            cadastro.cadastro_adm(adm)
        elif cadastrar=="CLIENTE":
            cadastro.cadastro_cliente(cliente)
        elif cadastrar=="VOLTAR":
            continue
    if menu=="LOGIN":
        perm_login=questionary.select("MENU LOGIN", choices=[
            "ADM",
            "CLIENTE",
            "VOLTAR"
        ]).ask()
        if perm_login=="VOLTAR":
            continue
        elif perm_login=="ADM":
            logadoadm,usuario=login.login_adm(adm)
            if logadoadm==True: 
                while True:
                    menuadm = questionary.select(
                    "MENU ADM",
                    choices=[
                    "Gerenciar Rebanho",
                    "Produção/Estoque",
                    "Financeiro",
                    "Retiradas",
                    "Relatórios",
                    "Propostas",
                    "ASSISTENTE DE IA",
                    "Sair"]).ask()
                    if menuadm=="Sair":
                        break
                    if menuadm=="Gerenciar Rebanho":
                        opadm=questionary.select(
                        "GERENCIAR REBANHO",
                        choices=[
                        "ADICIONAR ANIMAL",
                        "REMOVER ANIMAL",
                        "EDITAR ANIMAL",
                        "LISTAR ANIMAIS DO REBANHO",
                        "VACINAS",
                        "RELATÓRIO EM PDF REBANHO",
                        "VOLTAR"]).ask()
                        print()
                        if opadm=="ADICIONAR ANIMAL":
                            funcadm.adicionaranimal(rebanho)
                        elif opadm=="REMOVER ANIMAL":
                            funcadm.removeranimal(rebanho)
                        elif opadm=="EDITAR ANIMAL":
                            funcadm.atualizaranimal(rebanho)
                        elif opadm=="LISTAR ANIMAIS DO REBANHO":
                            funcadm.listarrebanho(rebanho)
                        elif opadm=="RELATÓRIO EM PDF REBANHO":
                            bibliotecas.pdf_relatorio_rebanho(rebanho)
                        elif opadm=="VOLTAR":
                                continue
                        elif opadm=="VACINAS":
                            op_vacinas=questionary.select("VACINAS", choices=["REGISTRAR VACINA", "PROXIMAS VACINAS","LISTAR VACINAS","RELATORIO EM PDF VACINA","VOLTAR"]).ask()
                            if op_vacinas=="REGISTRAR VACINA":
                                funcadm.vacinaadd(rebanho,vacina)
                            elif op_vacinas=="PROXIMAS VACINAS":
                                funcadm.proxvacina(vacina)
                            elif op_vacinas=="LISTAR VACINAS":
                                funcadm.listarvacina(vacina)
                            elif op_vacinas=="RELATÓRIO EM PDF VACINA":
                                bibliotecas.pdf_relatorio_vacina(vacina)
                            elif op_vacinas=="VOLTAR":
                                continue
                    elif menuadm=="Produção/Estoque":
                            bibliotecas.alertaestoquebaixo(estoqueadm)
                            opestoque=questionary.select("GESTÃO PRODUÇÃO", choices=[
                                "ADICIONAR AO ESTOQUE",
                                "REMOVER DO ESTOQUE",
                                "ATUALIZAR QUANTIDADE DE ITENS",
                                "ADICIONAR PRODUÇÃO DIÁRIA",
                                "RELATORIO PDF ESTOQUE",
                                "LISTAR PRODUTOS",
                                "GRAFICO ESTOQUE",
                                "RELATORIO EM PDF DO ESTOQUE",
                                "VOLTAR"
                            ]).ask()

                            print()
                            if opestoque=="ADICIONAR AO ESTOQUE":
                                funcadm.addestoque(estoqueadm)
                            elif opestoque=="REMOVER DO ESTQOUE":
                                funcadm.remvestoque(estoqueadm)
                            elif opestoque=="ATUALIZAR QUANTIDADE DE ITENS":
                                funcadm.atualizarproduto(estoqueadm)
                            elif opestoque=="LISTAR PRODUTOS":
                                funcadm.listarestoqueadm(estoqueadm)
                            elif opestoque=="ADICIONAR PRODUÇÃO DIÁRIA":
                                funcadm.prodiaria(estoqueadm)
                            elif opestoque=="RELATORIO EM PDF DO ESTOQUE":
                                bibliotecas.pdf_relatorio_estoque(estoqueadm)
                            elif opestoque=="GRAFICO ESTOQUE":
                                bibliotecas.grafico_estoque(estoqueadm)
                            elif opestoque=="VOLTAR":
                                continue
                    elif menuadm== "Financeiro":
                            op_fin=questionary.select("MENU FINANCEIRO", choices=[
                                "REGISTRAR ENTRADA",
                                "REGISTRAR SAIDA",
                                "VER SALDO",
                                "VER TOTAL DE ENTRADAS",
                                "VER TOTAL DE SAIDAS",
                                "GRAFICO FINANCEIRO",
                                "RELATORIO FINANCEIRO PDF",
                                "SAIR"
                            ]).ask()
                            if op_fin=="REGISTRAR ENTRADA":
                                funcadm.regentrada(financeiro)
                            elif op_fin=="REGISTRAR SAIDA":
                                funcadm.regsaida(financeiro)
                            elif op_fin=="VER SALDO":
                                funcadm.saldo(financeiro)
                            elif op_fin=="VER TOTAL DE ENTRADAS":
                                funcadm.total_entrada(financeiro)
                            elif op_fin=="VER TOTAL DE SAIDAS":
                                funcadm.total_saida(financeiro)
                            elif op_fin=="GRAFICO FINANCEIRO":
                                bibliotecas.grafico_financeiro(financeiro)
                            elif op_fin=="RELATORIO FINANCEIRO PDF":
                                bibliotecas.pdf_relatorio_financeiro
                            elif op_fin=="SAIR":
                                continue
                    elif menuadm=="Retiradas":
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
                        op_retirada=questionary.select("RETIRADAS", choices=[
                            "AGENDAR RETIRADA",
                            "CONFIRMAR RETIRADA",
                            "RETIRADAS PENDENTES",
                            "RETIRADAS FEITAS",
                            "SAIR"
                        ]).ask()
                        if op_retirada=="AGENDAR RETIRADA":
                            funcadm.retirada_agendar(retiradas)
                        elif op_retirada=="CONFIRMAR RETIRADA":
                            funcadm.confirm_retirada(retiradas)
                        elif op_retirada=="RETIRADAS PENDENTES":
                            funcadm.pendente(retiradas)
                        elif op_retirada=="RETIRADAS FEITAS":
                            funcadm.concluida(retiradas)
                        elif op_retirada=="SAIR":
                            continue

                    elif menuadm=="Relatórios":
                        op_relatorio=questionary.select("RELATORIO", choices=[
                            "RELATORIO REBANHO",
                            "RELATORIO ESTOQUE",
                            "RELATORIO FINANCEIRO",
                            "RELATORIO RETIRADAS",
                            "RELATORIO VACINAS"
                            "VOLTAR"
                        ]).ask()
                        if op_relatorio=="RELATORIO REBANHO":
                           funcadm.listarrebanho(rebanho)
                        elif op_relatorio=="RELATORIO ESTOQUE":
                            funcadm.listarestoqueadm(estoqueadm)
                        elif op_relatorio=="RELATORIO FINANCEIRO":
                            bibliotecas.pdf_relatorio_financeiro(financeiro)
                        elif op_relatorio=="RELATORIO RETIRADA":
                            funcadm.listar_retirada(retiradas)
                        elif op_relatorio=="RELATORIO VACINAS":
                            bibliotecas.pdf_relatorio_vacina(vacina)
                        elif op_relatorio=="VOLTAR":
                            continue
                    elif menuadm=="Propostas":
                        op_proposta=questionary.select("PROPOSTAS", choices=[
                            "VER PROPOSTAS",
                            "RESPONDER PROPOSTA",
                            "VOLTAR"
                        ]).ask()
                        if op_proposta=="VER PROPOSTAS":
                            funcadm.ver_propostas(propostas)
                        elif op_proposta=="RESPONDER PROPOSTA":
                            funcadm.confirm_proposta(propostas)
                        elif op_proposta=="VOLTAR":
                            continue
                    elif menuadm=="ASSISTENTE DE IA":
                        assistentedeia.assistentedeia(rebanho, estoqueadm, financeiro, vacina,retiradas)
                    elif menuadm=="SAIR":
                        break

                            
                

        elif perm_login=="CLIENTE":
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
                            funcusuario.comprar_animais(rebanho, estoquecliente, financeiro, propostas, cliente)
                    elif menu_user==2:
                        funcusuario.agendar_retirada(estoquecliente, retiradas)
                    if menu_user==3:
                        funcusuario.propostas_negociacao(estoqueadm, propostas, usuario)
                    elif menu_user==5:
                        break
                      
        else:
            print("USUÁRIO OU SENHA INVALIDO! ")
            continue