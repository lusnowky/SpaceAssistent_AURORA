nome_missao = "Expedição Aurora"
nome_equipe = "Artemis Delta"

# ------------------------------------------------------------------------------------------------------#

dados_missao = [
 [24, 92, 88, 96, 90],
 [27, 80, 72, 94, 85],
 [31, 65, 58, 91, 70],
 [36, 42, 38, 87, 55],
 [39, 28, 19, 78, 35],
 [34, 55, 32, 82, 50]
]

for ciclo in dados_missao:
    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

# ------------------------------------------------------------------------------------------------------#

areas_monitoradas = [
 "Temperatura interna",
 "Comunicação com a base",
 "Sistema de energia",
 "Suporte de oxigênio",
 "Estabilidade operacional"
]

# ------------------------------------------------------------------------------------------------------#

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif 30 > valor >= 18:
        return "NORMAL", 0
    elif 35 > valor >= 30:
        return "ATENÇÃO", 1
    elif valor >= 35:
        return "CRÍTICO", 2

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif 59 > valor >= 30:
        return "ATENÇÃO", 1
    elif valor >= 60:
        return "NORMAL", 0

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif 49 > valor >= 20:
        return "ATENÇÃO", 1
    elif valor >= 50:
        return "NORMAL", 0

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif 89 > valor >= 80:
        return "ATENÇÃO", 1
    elif valor >= 90:
        return "NORMAL", 0

def analisar_estabilidade(valor):
        if valor < 40:
            return "CRÍTICO", 2
        elif 69 > valor >= 40:
            return "ATENÇÃO", 1
        elif valor >= 70:
            return "NORMAL", 0

# ------------------------------------------------------------------------------------------------------#

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def analisar_tendencia(primeiro, ultimo): 
    if ultimo > primeiro: 
        return "A missão apresentou tendência de piora." 
    elif ultimo < primeiro: 
        return "A missão apresentou tendência de melhora." 
    else: 
        return "A missão permaneceu estável." 
    
def gerar_recomendacao(risco): 
    if risco <= 2: 
        return "Manter operação normal." 
    elif risco <= 5: 
        return "Monitorar sistemas em atenção." 
    else: 
        return "Ativar protocolos de emergência."


# ------------------------------------------------------------------------------------------------------#

pontuacao_areas = [0, 0, 0, 0, 0]
riscos_ciclos = []

soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0

maior_risco = -1
ciclo_mais_critico = 0

print("============================================================")
print("MISSION CONTROL AI")
print("============================================================")
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos: {len(dados_missao)}")
print("============================================================")

# ------------------------------------------------------------------------------------------------------#

for i, ciclo in enumerate(dados_missao, start = 1):

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    soma_temp += temperatura
    soma_com += comunicacao
    soma_bat += bateria
    soma_oxi += oxigenio
    soma_est += estabilidade

    temp_status, temp_risco = analisar_temperatura(temperatura)
    com_status, com_risco = analisar_comunicacao(comunicacao)
    bat_status, bat_risco = analisar_bateria(bateria)
    oxi_status, oxi_risco = analisar_oxigenio(oxigenio)
    est_status, est_risco = analisar_estabilidade(estabilidade)

    risco_total = (
        temp_risco +
        com_risco +
        bat_risco +
        oxi_risco +
        est_risco
    )

    riscos_ciclos.append(risco_total)

    pontuacao_areas[0] += temp_risco
    pontuacao_areas[1] += com_risco
    pontuacao_areas[2] += bat_risco
    pontuacao_areas[3] += oxi_risco
    pontuacao_areas[4] += est_risco

    if risco_total > maior_risco:
        maior_risco = risco_total
        ciclo_mais_critico = i

    print(f"\nCICLO {i}")
    print("-" * 60)
    print(f"Temperatura: {temperatura}°C | {temp_status}")
    print(f"Comunicação: {comunicacao}% | {com_status}")
    print(f"Bateria: {bateria}% | {bat_status}")
    print(f"Oxigênio: {oxigenio}% | {oxi_status}")
    print(f"Estabilidade: {estabilidade}% | {est_status}")
    print(f"Pontuação de risco: {risco_total}")
    print(f"Classificação: {classificar_ciclo(risco_total)}")
    print(f"Recomendação: {gerar_recomendacao(risco_total)}")

# ------------------------------------------------------------------------------------------------------#

media_temp = soma_temp / len(dados_missao)
media_com = soma_com / len(dados_missao)
media_bat = soma_bat / len(dados_missao)
media_oxi = soma_oxi / len(dados_missao)
media_est = soma_est / len(dados_missao)

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

area_mais_afetada = areas_monitoradas[
    pontuacao_areas.index(max(pontuacao_areas))
]

ciclos_criticos = 0
for risco in riscos_ciclos:
    if risco >= 6:
        ciclos_criticos += 1

print("\n")
print("============================================================")
print("RELATÓRIO FINAL DA MISSÃO")
print("============================================================")

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")

print(f"Média de temperatura: {media_temp:.2f}°C")
print(f"Média de comunicação: {media_com:.2f}%")
print(f"Média de bateria: {media_bat:.2f}%")
print(f"Média de oxigênio: {media_oxi:.2f}%")
print(f"Média de estabilidade: {media_est:.2f}%")

print(f"Ciclo mais crítico: {ciclo_mais_critico}")
print(f"Maior risco: {maior_risco}")
print(f"Risco médio: {risco_medio:.2f}")

print(f"Ciclos críticos: {ciclos_criticos}")

print(analisar_tendencia(
    riscos_ciclos[0],
    riscos_ciclos[-1]
))

print("\nPontuação por área:")

for i in range(len(areas_monitoradas)):
    print(
        f"{areas_monitoradas[i]}: "
        f"{pontuacao_areas[i]} pontos"
    )

print(f"\nÁrea mais afetada: {area_mais_afetada}")

print("\nConclusão:")
print("A missão deve continuar sendo monitorada para evitar falhas críticas.")