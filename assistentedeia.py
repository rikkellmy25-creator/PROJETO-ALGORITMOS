import questionary
from ollama import chat
import re
import bibliotecas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


def assistenteia_pdf(texto, titulo="RELATORIO ASSISTENTE", caminho="RELATORIO_ASSISTENTE.pdf"):
    doc = SimpleDocTemplate(caminho, pagesize=A4)
    estilos = getSampleStyleSheet()
    elementos = [Paragraph(titulo, estilos["Title"]), Spacer(1, 0.5 * cm)]

    for linha in texto.split("\n"):
        linha = linha.strip()
        if not linha:
            elementos.append(Spacer(1, 0.2 * cm))
            continue
        linha = linha.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        linha = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", linha)
        elementos.append(Paragraph(linha, estilos["Normal"]))

    doc.build(elementos)
    print(f"PDF gerado em: {caminho}")
    return caminho

def assistentedeia(rebanho, estoqueadm, financeiro, vacina,retiradas):
    opcao = questionary.select(
        "CONSULTOR IA",
        choices=[
            "ANÁLISE GERAL",
            "ANÁLISE FINANCEIRA",
            "ANÁLISE DO REBANHO",
            "ANÁLISE DE ESTOQUE",
            "PERGUNTA LIVRE",
            "HISTORICO DE MOVIMENTAÇÃO"
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
    elif opcao == "HISTORICO DE MOVIMENTAÇÃO":
        prompt = f"""
        Você é um consultor agropecuário. Com base nos dados abaixo,
        monte um histórico organizado de todas as movimentações da fazenda.

        Organize por categoria (financeiro, rebanho, estoque, vacinas, retiradas).
        Quando os dados tiverem datas, apresente em ordem cronológica.
        Ao final, traga um resumo das principais movimentações do período.

        Rebanho: {rebanho}
        Estoque: {estoqueadm}
        Financeiro: {financeiro}
        Vacinas: {vacina}
        Retiradas: {retiradas}
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
    pdf=questionary.select("Deseja salvar essa análise em PDF?", choices=["SIM","NÃO"]).ask()
    if pdf== "SIM":
        assistenteia_pdf(resposta["message"]["content"])
    elif pdf=="NÃO":
        return



