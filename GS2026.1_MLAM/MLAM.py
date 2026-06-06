# =================================================== AVISO =======================================================
# É NECESSÁRIO TER O ARQUIVO "baseDadosORIGINAL.csv" NA MESMA PASTA DESTE CÓDIGO PARA QUE ELE FUNCIONE CORRETAMENTE.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# LEITURA DA BASE DE DADOS
# =========================

df = pd.read_csv("baseDadosORIGINAL.csv")

print("=" * 60)
print("BASE DE DADOS CARREGADA COM SUCESSO")
print("=" * 60)

print("\nColunas encontradas na base:")
print(df.columns.tolist())

# ======================================================
# TABELA DE FREQUÊNCIA - VARIÁVEL QUANTITATIVA DISCRETA
# ======================================================

df["vento_discreto"] = df["windspeed_10m_max_kmh"].round().astype(int)

freq_discreta = (
    df["vento_discreto"]
    .value_counts()
    .sort_index()
    .reset_index()
)

freq_discreta.columns = ["Velocidade_Vento", "Frequencia"]

freq_discreta["Freq_Relativa_%"] = (
    freq_discreta["Frequencia"] / len(df) * 100
).round(2)

print("\n")
print("=" * 60)
print("TABELA DE FREQUÊNCIA - VARIÁVEL DISCRETA")
print("=" * 60)
print(freq_discreta)

# ======================================================
# TABELA DE FREQUÊNCIA - VARIÁVEL QUANTITATIVA CONTÍNUA
# ======================================================

classes = 8

freq_continua = pd.cut(
    df["temp_mean_c_approx"],
    bins=classes
)

tabela_continua = (
    freq_continua
    .value_counts()
    .sort_index()
    .reset_index()
)

tabela_continua.columns = ["Classe_Temperatura", "Frequencia"]

tabela_continua["Freq_Relativa_%"] = (
    tabela_continua["Frequencia"] / len(df) * 100
).round(2)

print("\n")
print("=" * 60)
print("TABELA DE FREQUÊNCIA - VARIÁVEL CONTÍNUA")
print("=" * 60)
print(tabela_continua)

# =========================
# GRÁFICO 1 - HISTOGRAMA
# =========================

plt.figure(figsize=(8, 5))

plt.hist(
    df["temp_mean_c_approx"],
    bins=8,
    edgecolor="black"
)

plt.title("Distribuição da Temperatura Média")
plt.xlabel("Temperatura Média (°C)")
plt.ylabel("Frequência")
plt.grid(True)

plt.savefig("grafico_temperatura.png")
plt.close()

# =========================
# GRÁFICO 2 - BARRAS
# =========================

faixas_chuva = pd.cut(
    df["precip_mm"],
    bins=[-0.1, 0, 5, 10, 20, 50, float("inf")]
)

chuva_freq = faixas_chuva.value_counts().sort_index()

plt.figure(figsize=(8, 5))

chuva_freq.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Distribuição da Precipitação")
plt.xlabel("Faixas de Precipitação (mm)")
plt.ylabel("Quantidade de Capitais")

plt.tight_layout()

plt.savefig("grafico_precipitacao.png")
plt.close()

# ====================================
# ANÁLISE UNIVARIADA - TEMPERATURA
# ====================================

temperatura = df["temp_mean_c_approx"]

media = temperatura.mean()
mediana = temperatura.median()
moda = temperatura.mode().iloc[0]

maximo = temperatura.max()
minimo = temperatura.min()
amplitude = maximo - minimo

variancia = temperatura.var()
desvio_padrao = temperatura.std()

coef_variacao = (desvio_padrao / media) * 100

quartis = temperatura.quantile([0.25, 0.50, 0.75])

print("\n")
print("=" * 60)
print("ANÁLISE UNIVARIADA - TEMPERATURA MÉDIA")
print("=" * 60)

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Máximo: {maximo:.2f}")
print(f"Mínimo: {minimo:.2f}")
print(f"Amplitude: {amplitude:.2f}")
print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Coeficiente de Variação: {coef_variacao:.2f}%")

print("\nQuartis:")
print(quartis)

print("\nInterpretação da Variabilidade:")

if coef_variacao < 15:
    print("Baixa variabilidade dos dados.")
elif coef_variacao < 30:
    print("Variabilidade moderada dos dados.")
else:
    print("Alta variabilidade dos dados.")

# ====================================
# ANÁLISE UNIVARIADA - VENTO
# ====================================

vento = df["windspeed_10m_max_kmh"]

media_v = vento.mean()
mediana_v = vento.median()
moda_v = vento.mode().iloc[0]

maximo_v = vento.max()
minimo_v = vento.min()
amplitude_v = maximo_v - minimo_v

variancia_v = vento.var()
desvio_padrao_v = vento.std()

coef_variacao_v = (desvio_padrao_v / media_v) * 100

quartis_v = vento.quantile([0.25, 0.50, 0.75])

print("\n")
print("=" * 60)
print("ANÁLISE UNIVARIADA - VELOCIDADE DO VENTO")
print("=" * 60)

print(f"Média: {media_v:.2f}")
print(f"Mediana: {mediana_v:.2f}")
print(f"Moda: {moda_v:.2f}")
print(f"Máximo: {maximo_v:.2f}")
print(f"Mínimo: {minimo_v:.2f}")
print(f"Amplitude: {amplitude_v:.2f}")
print(f"Variância: {variancia_v:.2f}")
print(f"Desvio Padrão: {desvio_padrao_v:.2f}")
print(f"Coeficiente de Variação: {coef_variacao_v:.2f}%")

print("\nQuartis:")
print(quartis_v)

print("\nInterpretação da Variabilidade:")

if coef_variacao_v < 15:
    print("Baixa variabilidade dos dados.")
elif coef_variacao_v < 30:
    print("Variabilidade moderada dos dados.")
else:
    print("Alta variabilidade dos dados.")

print("\n")
print("=" * 60)
print("ARQUIVOS GERADOS")
print("=" * 60)
print("grafico_temperatura.png")
print("grafico_precipitacao.png")