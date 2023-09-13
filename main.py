# https://www.kaggle.com/datasets/joaoavf/enade-microdados-2016-2017-2018

import pandas
from fpdf import FPDF

df = pandas.read_csv("./dados_enade.csv")
print(df.head(n=10))

df = df \
    .rename(columns={'NT_GER': 'Nota Geral', 'TP_SEXO': 'Sexo', 'NU_IDADE': 'Idade', 'CO_UF_CURSO': 'Estado',
                     'ANO_FIM_EM': 'Ano Conclusão'}) \
    .replace({"Estado": {11: "RO", 12: "AC", 13: "AM", 14: "RR", 15: "PA", 16: "AP", 17: "TO", 21: "MA", 22: "PI",
                         23: "CE", 24: "RN", 25: "PB", 26: "PE", 27: "AL", 28: "SE", 29: "BA", 31: "MG", 32: "ES",
                         33: "RJ", 35: "SP", 41: "PR", 42: "SC", 43: "RS", 50: "MS", 51: "MT", 52: "GO", 53: "DF", }})

aplicantes_sexo = \
    df.groupby(["Sexo"])["Sexo"].count().reset_index(name="Aplicantes")
print(aplicantes_sexo.head())
aplicantes_sexo_figure = aplicantes_sexo \
    .plot(x="Sexo", y="Aplicantes", kind="bar", title="Total de aplicantes por sexo") \
    .get_figure()
aplicantes_sexo_figure.show()

nota_sexo = \
    df[["Sexo", "Nota Geral"]] \
        .groupby(["Sexo"])["Nota Geral"].mean().reset_index(name="Média Geral")
print(nota_sexo.head())
nota_sexo_figure = nota_sexo \
    .plot(x="Sexo", y="Média Geral", kind="bar", title="Distribuição de nota geral por sexo (média)") \
    .get_figure()
nota_sexo_figure.show()

aplicantes_estado = \
    df.groupby(["Estado"])["Estado"].count().reset_index(name="Aplicantes") \
        .sort_values(by="Aplicantes", ascending=False)
print(aplicantes_estado.head())
aplicantes_estado_figure = aplicantes_estado \
    .plot(x="Estado", y="Aplicantes", kind="bar", title="Total de aplicantes por estado") \
    .get_figure()
aplicantes_estado_figure.show()

nota_estados = \
    df[["Estado", "Nota Geral"]] \
        .groupby(["Estado"])["Nota Geral"].mean().reset_index(name="Média Geral") \
        .sort_values(by="Média Geral", ascending=True)
print(nota_estados.head())
nota_estados_figure = nota_estados \
    .plot(x="Estado", y="Média Geral", kind="barh", title="Distibuição de nota geral por estado (média)",
          legend=False) \
    .get_figure()
nota_estados_figure.show()

aplicantes_idade = \
    df.groupby(["Idade"])["Idade"].count().reset_index(name="Aplicantes") \
        .query("Aplicantes > 50") \
        .sort_values(by="Aplicantes", ascending=False)
print(aplicantes_idade.tail())
aplicantes_idade_figure = aplicantes_idade \
    .plot(x="Idade", y="Aplicantes", kind="bar", title="Total de aplicantes por idade\nAcima de 50 participantes") \
    .get_figure()
aplicantes_idade_figure.show()

nota_idade = \
    df[["Idade", "Nota Geral"]] \
        .rename(columns={'Idade': 'Idade', 'Nota Geral': 'Nota Geral'}) \
        .groupby(["Idade"])["Nota Geral"].mean().reset_index(name="Média Geral") \
        .query("Idade < 60 and Idade > 14") \
        .sort_values(by="Média Geral", ascending=False)
print(nota_idade.head())
nota_idade_figure = nota_idade \
    .plot(x="Idade", y="Média Geral", kind="bar",
          title="Distibuição de nota geral por idade (média)\nEntre 14 e 60 anos") \
    .get_figure()
nota_idade_figure.show()

nota_idade_evolucao = \
    df[["Idade", "Nota Geral"]] \
        .groupby(["Idade"])["Nota Geral"].mean().reset_index(name="Média Geral") \
        .query("Idade > 14") \
        .sort_values(by="Idade", ascending=True)
print(nota_idade_evolucao.head())
nota_idade_evolucao_figure = nota_idade_evolucao \
    .plot(x="Idade", y="Média Geral", kind="line",
          title="Evolução de nota geral por idade (média)\nAcima de 14 anos") \
    .get_figure()
nota_idade_evolucao_figure.show()

aplicantes_ano_concl = \
    df.groupby(["Ano Conclusão"])["Ano Conclusão"].count().reset_index(name="Aplicantes") \
        .query("`Ano Conclusão` > 1940 and `Ano Conclusão` < 2029") \
        .sort_values(by="Ano Conclusão", ascending=False)
print(aplicantes_ano_concl.tail())
aplicantes_ano_concl_figure = aplicantes_ano_concl \
    .plot(x="Ano Conclusão", y="Aplicantes", kind="line", title="Total de aplicantes por ano de conclusão") \
    .get_figure()
aplicantes_ano_concl_figure.show()

nota_ano_fim_ensino_medio_evolucao = \
    df[["Ano Conclusão", "Nota Geral"]] \
        .groupby(["Ano Conclusão"])["Nota Geral"].mean().reset_index(name="Média Geral") \
        .query("`Ano Conclusão` > 1940 and `Ano Conclusão` < 2029")
print(nota_ano_fim_ensino_medio_evolucao.head())
fim_ensino_medio_plot = nota_ano_fim_ensino_medio_evolucao.plot(x="Ano Conclusão", y="Média Geral", kind="line")
fim_ensino_medio_plot.set_title("Evolução da nota geral por ano de finalização do ensino médio (média)")
nota_ano_fim_ensino_medio_evolucao_figure = fim_ensino_medio_plot.get_figure()
nota_ano_fim_ensino_medio_evolucao_figure.show()

# figure.savefig('./data/figure.png', bbox_inches='tight')

aplicantes_sexo_figure.savefig('./imagens/aplicantes_sexo.png')
nota_sexo_figure.savefig('./imagens/nota_sexo.png')
aplicantes_estado_figure.savefig('./imagens/aplicantes_estado.png')
nota_estados_figure.savefig('./imagens/nota_estados.png')
aplicantes_idade_figure.savefig('./imagens/aplicantes_idade.png')
nota_idade_figure.savefig('./imagens/nota_idade.png')
nota_idade_evolucao_figure.savefig('./imagens/nota_idade_evolucao.png')
aplicantes_ano_concl_figure.savefig('./imagens/aplicantes_ano_concl.png')
nota_ano_fim_ensino_medio_evolucao_figure.savefig('./imagens/nota_ano_fim_ensino_medio_evolucao.png')

pdf = FPDF()
pdf.add_page(orientation='L')
pdf.set_font('helvetica', size=12)
pdf.cell(txt="Desigualdade na Educação")
pdf.image('./imagens/aplicantes_sexo.png', h=150, keep_aspect_ratio=True)
pdf.image('./imagens/nota_sexo.png', h=150, keep_aspect_ratio=True)
pdf.image('./imagens/aplicantes_estado.png', h=150, keep_aspect_ratio=True)
pdf.image('./imagens/nota_estados.png', h=150, keep_aspect_ratio=True)
pdf.image('./imagens/aplicantes_idade.png', h=150, keep_aspect_ratio=True)
pdf.image('./imagens/nota_idade.png', h=150, keep_aspect_ratio=True)
pdf.image('./imagens/nota_idade_evolucao.png', h=150, keep_aspect_ratio=True)
pdf.image('./imagens/aplicantes_ano_concl.png', h=150, keep_aspect_ratio=True)
pdf.image('./imagens/nota_ano_fim_ensino_medio_evolucao.png', h=150, keep_aspect_ratio=True)
pdf.output("desigualdade_educacao.pdf")
