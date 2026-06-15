import questionary
from ollama import chat


def assistentedeia(rebanho, estoqueadm, financeiro, vacina,retiradas):
    opcao = questionary.select(
        "CONSULTOR IA",
        choices=[
            "ANÁLISE GERAL",
            "ANÁLISE FINANCEIRA",
            "ANÁLISE DO REBANHO",
            "ANÁLISE DE ESTOQUE",
            "PERGUNTA LIVRE",
            "VOLTAR"
        ]
    ).ask()

    if opcao == "ANÁLISE GERAL":
        prompt = f"""
        Você é um consultor agropecuário. Analise os dados abaixo e gere:
        1. Situação geral da fazenda
        2. Possíveis problemas
        3. Recomendações de melhoria
        4. Alertas importantes

        Rebanho: {rebanho}
        Estoque: {estoqueadm}
        Financeiro: {financeiro}
        Vacinas: {vacina}
        Retiradas:{retiradas}
        """
    elif opcao == "ANÁLISE FINANCEIRA":
        prompt = f"""
        Analise exclusivamente o financeiro da fazenda:
        {financeiro}
        Gere recomendações para aumentar o lucro e reduzir custos.
        """
    elif opcao == "ANÁLISE DO REBANHO":
        prompt = f"""
        Analise exclusivamente o rebanho da fazenda:
        Rebanho: {rebanho}
        Vacinas: {vacina}
        Gere recomendações sobre saúde, manejo e produtividade.
        """
    elif opcao == "ANÁLISE DE ESTOQUE":
        prompt = f"""
        Analise exclusivamente o estoque da fazenda:
        Estoque: {estoqueadm}
        Gere recomendações sobre reposição, itens em falta e em excesso.
        """
    elif opcao == "PERGUNTA LIVRE":
        pergunta = input("Digite sua pergunta: ")
        prompt = f"""
        Dados da fazenda:
        Rebanho: {rebanho}
        Estoque: {estoqueadm}
        Financeiro: {financeiro}
        Vacinas: {vacina}
        Retiradas:{retiradas}

        Pergunta: {pergunta}
        """
    else:
        return

    resposta = chat(
        model="gemma4:e4b-it-qat",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\n=== RESPOSTA DA IA ===\n")
    print(resposta["message"]["content"])