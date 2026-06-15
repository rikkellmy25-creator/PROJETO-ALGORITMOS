
# pip install pandas plotly reportlab pyttsx3 ollama

import pandas as pd
import plotly.express as px
import pyttsx3
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


def falar(texto):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    for voz in engine.getProperty("voices"):
        nome = (voz.name + voz.id).lower()
        if "portug" in nome or "brazil" in nome or "brasil" in nome:
            engine.setProperty("voice", voz.id)
            break
    engine.say(texto)
    engine.runAndWait()

def alertaestoquebaixo(estoqueadm, limite=5):
    estoque_baixo = [i["PRODUTO"] for i in estoqueadm if i["QUANTIDADE"] < limite]
    if not estoque_baixo:
        print("Nenhum produto com estoque baixo.")
        return
    msg = "Atenção! Estoque baixo de: " + ", ".join(estoque_baixo)
    print(msg)
    falar(msg)


def df_financeiro(financeiro):
    if not financeiro:
        return pd.DataFrame(columns=["VALOR", "DESCRICAO", "TIPO"])
    return pd.DataFrame(financeiro)


def resumo_financeiro(financeiro):
    df = df_financeiro(financeiro)
    if df.empty:
        return 0, 0, 0
    total_entrada = df.loc[df["TIPO"] == "ENTRADA", "VALOR"].sum()
    total_saida = df.loc[df["TIPO"] == "SAIDA", "VALOR"].sum()
    return total_entrada, total_saida, total_entrada - total_saida


def grafico_financeiro(financeiro, salvar="grafico_financeiro.html"):
    df = df_financeiro(financeiro)
    if df.empty:
        print("Sem dados financeiros para o gráfico.")
        return
    resumo = df.groupby("TIPO", as_index=False)["VALOR"].sum()
    fig = px.bar(resumo, x="TIPO", y="VALOR", color="TIPO",
                 title="Entradas x Saídas (R$)", text_auto=True)
    fig.write_html(salvar)
    print(f"Gráfico salvo em: {salvar}")

def grafico_estoque(estoqueadm, salvar="grafico_estoque.html"):
    if not estoqueadm:
        print("Estoque vazio.")
        return
    df = pd.DataFrame(estoqueadm)
    fig = px.bar(df, x="PRODUTO", y="QUANTIDADE",
                 title="Quantidade por produto", text_auto=True)
    fig.write_html(salvar)
    print(f"Gráfico salvo em: {salvar}")

def pdf_relatorio_financeiro(financeiro, caminho="relatorio_financeiro.pdf"):
    df = df_financeiro(financeiro)
    total_entrada, total_saida, saldo = resumo_financeiro(financeiro)

    doc = SimpleDocTemplate(caminho, pagesize=A4)
    estilos = getSampleStyleSheet()
    elementos = [Paragraph("Relatório Financeiro - Fazenda Sertão", estilos["Title"]),
                 Spacer(1, 0.5 * cm)]

    dados = [["Valor (R$)", "Descrição", "Tipo"]]
    for linha in df.iterrows():
        dados.append([f'{linha["VALOR"]:.2f}', str(linha["DESCRICAO"]), str(linha["TIPO"])])

    if len(dados) == 1:
        dados.append(["-", "Nenhum lançamento", "-"])

    tabela = Table(dados, hAlign="LEFT")
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2e7d32")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f0f0")]),
    ]))
    elementos.append(tabela)
    elementos.append(Spacer(1, 0.5 * cm))
    elementos.append(Paragraph(f"Total de entradas: R$ {total_entrada:.2f}", estilos["Normal"]))
    elementos.append(Paragraph(f"Total de saídas: R$ {total_saida:.2f}", estilos["Normal"]))
    elementos.append(Paragraph(f"<b>Saldo atual: R$ {saldo:.2f}</b>", estilos["Normal"]))

    doc.build(elementos)
    print(f"PDF gerado em: {caminho}")
    return caminho


def pdf_relatorio_estoque(estoqueadm, caminho="relatorio_estoque.pdf"):
    doc = SimpleDocTemplate(caminho, pagesize=A4)
    estilos = getSampleStyleSheet()
    elementos = [Paragraph("Relatório de Estoque - Fazenda Sertão", estilos["Title"]),
                 Spacer(1, 0.5 * cm)]

    dados = [["ID", "Produto", "Qtd", "Valor (R$)", "Validade"]]
    for item in estoqueadm:
        dados.append([str(item["ID"]), item["PRODUTO"], str(item["QUANTIDADE"]),f'{item["VALOR"]:.2f}', item["VALIDADE"]])
    if len(dados) == 1:
        dados.append(["-", "Estoque vazio", "-", "-", "-"])

    tabela = Table(dados, hAlign="LEFT")
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565c0")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f0f0")]),
    ]))
    elementos.append(tabela)
    doc.build(elementos)
    print(f"PDF gerado em: {caminho}")
    return caminho


def pdf_relatorio_vacina(vacina, caminho="vacina.pdf"):
    doc = SimpleDocTemplate(caminho, pagesize=A4)
    estilos = getSampleStyleSheet()
    elementos = [Paragraph("Relatório de VACINA - Fazenda Sertão", estilos["Title"]),
                 Spacer(1, 0.5 * cm)]

    dados = [["ID", "VACINA", "Qtd", "DATA(AA/MM/YY):", "PROXIMA(AA/MM/YY):"]]
    for item in vacina:
        dados.append([str(item["ID"]), item["VACINA"], str(item["DATA"]),f'{item["PROXIMA"]:.2f}'])
    if len(dados) == 1:
        dados.append(["-", "NENHUMA VACINA APLICADA", "-", "-", "-"])

    tabela = Table(dados, hAlign="LEFT")
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565c0")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f0f0")]),
    ]))
    elementos.append(tabela)
    doc.build(elementos)
    print(f"PDF gerado em: {caminho}")
    return caminho

def pdf_relatorio_rebanho(rebanho, caminho="rebanho.pdf"):
    doc = SimpleDocTemplate(caminho, pagesize=A4)
    estilos = getSampleStyleSheet()
    elementos = [Paragraph("Relatório de REBANHO - Fazenda Sertão", estilos["Title"]),
                 Spacer(1, 0.5 * cm)]

    dados = [["ID", "TIPO", "PESO", "GESTAÇÃO", "QUANTIDADE"]]
    for item in rebanho:
        dados.append([str(item["ID"]), item["TIPO"], str(item["PESO"]), str(item["GESTACAO"]), item["QUANTIDADE"]])
    if len(dados) == 1:
        dados.append(["-", "NENHUM ANIMAL ADICIONADO", "-", "-", "-"])

    tabela = Table(dados, hAlign="LEFT")
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565c0")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f0f0")]),
    ]))
    elementos.append(tabela)
    doc.build(elementos)
    print(f"PDF gerado em: {caminho}")
    return caminho

def pdf_relatorio_retiradas(retiradas, caminho="rebanho.pdf"):
    doc = SimpleDocTemplate(caminho, pagesize=A4)
    estilos = getSampleStyleSheet()
    elementos = [Paragraph("Relatório de RETIRADAS - Fazenda Sertão", estilos["Title"]),
                 Spacer(1, 0.5 * cm)]

    dados = [["ID", "TIPO", "DATA", "HORA", "STATUS"]]
    for item in retiradas:
        dados.append([str(item["ID"]), item["TIPO"], str(item["DATA"]),f'{item["HORA"]:.2f}', item["STATUS"]])
    if len(dados) == 1:
        dados.append(["-", "NENHUMA RETIRADA PENDENTE", "-", "-", "-"])

    tabela = Table(dados, hAlign="LEFT")
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565c0")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f0f0")]),
    ]))
    elementos.append(tabela)
    doc.build(elementos)
    print(f"PDF gerado em: {caminho}")
    return caminho