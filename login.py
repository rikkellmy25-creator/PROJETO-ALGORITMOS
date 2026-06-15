def login_adm(adm):
    usuario=input("DIGITE SEU USUÁRIO: ")
    senha=input("DIGITE SUA SENHA: ")
    logado=False
    for i in adm:
        if i.get("usuario") == usuario and i.get("senha") == senha:
            logado=True
    if logado:
        print("LOGIN REALIZADO COM SUCESSO")
    else:
        print("USUÁRIO OU SENHA INCORRETOS!")
    return logado, usuario


def login_cliente(cliente):
    usuario=input("DIGITE SEU USUÁRIO: ")
    senha=input("DIGITE SUA SENHA: ")
    logado=False
    for i in cliente:
        if i.get("usuario") == usuario and i.get("senha") == senha:
            logado=True
    if logado:
        print("LOGIN REALIZADO COM SUCESSO")
    else:
        print("USUÁRIO OU SENHA INCORRETOS!")
    return logado, usuario