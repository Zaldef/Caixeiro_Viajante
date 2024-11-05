import random
import numpy as np
import matplotlib.pyplot as plt

def gerar_pontos_uniformes(quantidade, limite=15):
    """
    Gera pontos aleatórios uniformemente distribuídos em um quadrado de lado 2 * limite.
    """
    return [(random.uniform(-limite, limite),
             random.uniform(-limite, limite))
             for _ in range(quantidade)]

def gerar_pontos_circulares(quantidade, raio=15):
    """
    Gera pontos igualmente espaçados em um círculo de raio especificado.
    """
    angulos = np.linspace(0, 2 * np.pi, quantidade, endpoint=False)
    return [(raio * np.cos(angulo), raio * np.sin(angulo)) for angulo in angulos]

def plotar_caminho(pontos, caminho, titulo="Caminho"):
    """
    Plota o caminho final que passa por todos os pontos.
    """
    caminho_completo = caminho + [caminho[0]]
    x = [pontos[i][0] for i in caminho_completo]
    y = [pontos[i][1] for i in caminho_completo]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker='o')
    plt.title(titulo)
    plt.show()

def distancia(ponto1, ponto2):
    """
    Calcula a distância euclidiana entre dois pontos.
    """
    return np.sqrt((ponto1[0] - ponto2[0]) ** 2 + (ponto1[1] - ponto2[1]) ** 2)

def aptidao(caminho, pontos):
    """
    Calcula a aptidão de um caminho, que é a inversa da distância total percorrida.
    """
    distancia_total = 0
    for i in range(len(caminho)):
        distancia_total += distancia(pontos[caminho[i]], pontos[caminho[(i + 1) % len(caminho)]])
    return 1 / distancia_total  # Quanto menor a distância, maior o aptidao

def gerar_caminho(pontos):
    """
    Gera um caminho aleatório que passa por todos os pontos.
    """
    caminho = list(range(len(pontos)))
    random.shuffle(caminho)
    return caminho

def selecao(populacao, aptidao_pop):
    """
    Seleciona um indivíduo da população com base em um torneio de 3 indivíduos.
    """
    torneio = random.sample(list(zip(populacao, aptidao_pop)), 3)
    torneio.sort(key=lambda x: x[1], reverse=True)  # Ordena pelo melhor aptidao
    return torneio[0][0]

def cruzamento(pai1, pai2):
    """
    Realiza o cruzamento de dois pais para gerar um filho.
    """
    tamanho = len(pai1)
    filho = [-1] * tamanho
    inicio, fim = sorted(random.sample(range(tamanho), 2))
    filho[inicio:fim] = pai1[inicio:fim]

    for gene in pai2:
        if gene not in filho:
            for i in range(tamanho):
                if filho[i] == -1:
                    filho[i] = gene
                    break
    return filho

def melhorar_caminho_inversao(caminho, pontos):
    """
    Realiza uma melhoria no caminho trocando duas cidades e verificando se a inversão melhora a distância.
    """
    melhorou = False
    for i in range(1, len(caminho) - 1):
        dist_atual = (distancia(pontos[caminho[i-1]], pontos[caminho[i]]) +
                      distancia(pontos[caminho[i]], pontos[caminho[i+1]]))

        dist_invertida = (distancia(pontos[caminho[i-1]], pontos[caminho[i+1]]) +
                          distancia(pontos[caminho[i+1]], pontos[caminho[i]]))

        if dist_invertida < dist_atual:
            caminho[i], caminho[i+1] = caminho[i+1], caminho[i]
            melhorou = True
    return caminho, melhorou

def mutacao(caminho, taxa_mutacao, pontos):
    """
    Realiza uma mutação no caminho trocando duas cidades aleatórias.
    """
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(caminho)), 2)
        caminho[i], caminho[j] = caminho[j], caminho[i]

    caminho = melhorar_caminho_inversao(caminho, pontos)

    return caminho


def nova_geracao_com_elitismo(populacao, aptidao_pop, taxa_mutacao, pontos, elitismo=True):
    """
    Gera uma nova população com base na aptidão dos indivíduos da geração anterior.
    """
    nova_populacao = []
    if elitismo:
        melhor_indice = np.argmax(aptidao_pop)
        melhor_individuo = populacao[melhor_indice]
        nova_populacao.append(melhor_individuo)

    for _ in range(len(populacao) - len(nova_populacao)):
        pai1 = selecao(populacao, aptidao_pop)
        pai2 = selecao(populacao, aptidao_pop)
        filho = cruzamento(pai1, pai2)
        filho = mutacao(filho, taxa_mutacao, pontos)
        nova_populacao.append(filho)

    return nova_populacao


def algoritmo_genetico(pontos, tamanho_populacao=100, num_geracoes=50, taxa_mutacao=0.08, elitismo=True):
    """
    Algoritmo Genético para resolver o Problema do Caixeiro Viajante.
    """
    populacao = [gerar_caminho(pontos) for _ in range(tamanho_populacao)]
    historico_aptidao = []

    melhor_rota = None

    # Configurações do gráfico do caminho
    plt.figure(figsize=(6, 6))
    plt.title("Caminho")
    plt.xlim(-12, 12)  # Ajuste o limite conforme necessário
    plt.ylim(-12, 12)
    plt.ion()  # Ativa o modo interativo
    linha, = plt.plot([], [], 'bo-', marker='o')  # Linha vazia para atualização

    for geracao in range(num_geracoes):
        aptidao_pop = [aptidao(caminho, pontos) for caminho in populacao]
        melhor_aptidao = max(aptidao_pop)
        melhor_rota = populacao[aptidao_pop.index(melhor_aptidao)]
        historico_aptidao.append(1 / melhor_aptidao)

        print(f"Geração {geracao + 1}: Melhor distância: {1 / melhor_aptidao}")

        populacao = nova_geracao_com_elitismo(populacao, aptidao_pop, taxa_mutacao, pontos, elitismo)

        # # Atualizar gráfico do caminho a cada 10 gerações
        # if (geracao + 1) % 10 == 0:
        #     caminho_completo = melhor_rota + [melhor_rota[0]]  # Volta ao ponto inicial
        #     x = [pontos[i][0] for i in caminho_completo]
        #     y = [pontos[i][1] for i in caminho_completo]
        #     linha.set_xdata(x)
        #     linha.set_ydata(y)
        #     plt.draw()
        #     plt.pause(1.0)  # Pausa para atualizar o gráfico

    plt.ioff()  # Desativa o modo interativo
    plt.show()  # Exibe o gráfico final

    return melhor_rota, historico_aptidao



# -------------- MAIN --------------

# Teste Pontos Uniformes - 15 pontos
pontos_uniformes = gerar_pontos_uniformes(15)
melhor_caminho, historico = algoritmo_genetico(pontos_uniformes)
plotar_caminho(pontos_uniformes, melhor_caminho, "Caminho Uniforme")

# Teste Pontos Circulares - 15 pontos
pontos_circulares = gerar_pontos_circulares(15)
melhor_caminho, historico = algoritmo_genetico(pontos_circulares)
plotar_caminho(pontos_circulares, melhor_caminho, "Caminho Circular")



# Plotar histórico de aptidão (melhor distância ao longo das gerações)
plt.plot(historico)
plt.title("Evolução do aptidão ao Longo das Gerações")
plt.xlabel("Geração")
plt.ylabel("Melhor Distância")
plt.show()
