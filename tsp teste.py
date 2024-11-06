import random
import numpy as np
import matplotlib.pyplot as plt

def criar_pontos_uniformes(quantidade, limite=15):
    """
    Cria pontos aleatórios uniformemente distribuídos em um quadrado de lado 2 * limite.
    """

    return [(random.uniform(-limite, limite), random.uniform(-limite, limite)) for _ in range(quantidade)]

def criar_pontos_circulares(quantidade, raio=15):
    """
    Cria pontos igualmente espaçados em um círculo de raio especificado.
    """

    angulos = np.linspace(0, 2 * np.pi, quantidade, endpoint=False)

    return [(raio * np.cos(angulo), raio * np.sin(angulo)) for angulo in angulos]

def criar_rota_aleatoria(pontos):
    """
    Cria uma rota aleatório que passa por todos os pontos.
    """

    rota = list(range(len(pontos)))
    random.shuffle(rota)

    return rota

def plotar_rota(pontos, rota, titulo="Rota"):
    """
    Plota a rota final que passa por todos os pontos.
    """

    rota_completa = rota + [rota[0]]
    x = [pontos[i][0] for i in rota_completa]
    y = [pontos[i][1] for i in rota_completa]

    plt.figure(figsize=(9, 9))
    plt.plot(x, y, marker='o')
    plt.title(titulo)
    plt.show()

def distancia(ponto1, ponto2):
    """
    Calcula a distância euclidiana entre dois pontos.
    """

    return np.sqrt((ponto1[0] - ponto2[0]) ** 2 + (ponto1[1] - ponto2[1]) ** 2)

def aptidao(rota, pontos):
    """
    Calcula a aptidão de um rota, que é a inversa da distância total percorrida.
    """

    distancia_total = 0
    for i in range(len(rota)):
        distancia_total += distancia(pontos[rota[i]], pontos[rota[(i + 1) % len(rota)]])

    return 1 / distancia_total

def selecao(populacao, aptidoes):
    """
    Seleciona um indivíduo da população com base em um torneio de 3 indivíduos.
    """

    torneio = random.sample(list(zip(populacao, aptidoes)), 3)
    torneio.sort(key=lambda x: x[1], reverse=True)

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

# Função para inverter dois pontos adjacentes no rota e verificar se melhora a distância total
def inverter_rota(rota, pontos):
    melhor = False
    for i in range(1, len(rota) - 1):
        dist_atual = (distancia(pontos[rota[i-1]], pontos[rota[i]]) + 
                      distancia(pontos[rota[i]], pontos[rota[i+1]]))
        
        dist_invertida = (distancia(pontos[rota[i-1]], pontos[rota[i+1]]) + 
                          distancia(pontos[rota[i+1]], pontos[rota[i]]))
        
        if dist_invertida < dist_atual:
            rota[i], rota[i+1] = rota[i+1], rota[i]
            melhor = True
    return rota, melhor

# Mutação (Troca de duas cidades e melhoria por inversão)
def mutacao(rota, taxa_mutacao, pontos):
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(rota)), 2)
        rota[i], rota[j] = rota[j], rota[i]
    
    rota, melhor = inverter_rota(rota, pontos)
    
    return rota

# Função para criar uma nova geração, incluindo elitismo
def nova_geracao_com_elitismo(populacao, aptidoes, taxa_mutacao, pontos, elite=True):
    nova_populacao = []
    
    if elite:
        melhor_indice = np.argmax(aptidoes)
        melhor_individuo = populacao[melhor_indice]
        nova_populacao.append(melhor_individuo)
    
    for _ in range(len(populacao) - len(nova_populacao)):
        pai1 = selecao(populacao, aptidoes)
        pai2 = selecao(populacao, aptidoes)
        filho = cruzamento(pai1, pai2)
        filho = mutacao(filho, taxa_mutacao, pontos)
        nova_populacao.append(filho)
    
    return nova_populacao

# Função principal do algoritmo genético com elite
def algoritmo_genetico(pontos, tamanho_populacao=100, num_geracoes=50, taxa_mutacao=0.08, elite=True):
    populacao = [criar_rota_aleatoria(pontos) for _ in range(tamanho_populacao)]
    historico_aptidao = []

    melhor_caminho = None

    # Configurações do gráfico do rota
    plt.figure(figsize=(6, 6))
    plt.title("Rota")
    plt.xlim(-12, 12)  # Ajuste o limite conforme necessário
    plt.ylim(-12, 12)
    plt.ion()  # Ativa o modo interativo
    linha, = plt.plot([], [], 'bo-', marker='o')  # Linha vazia para atualização

    for geracao in range(num_geracoes):
        aptidoes = [aptidao(rota, pontos) for rota in populacao]
        melhor_aptidao = max(aptidoes)
        melhor_caminho = populacao[aptidoes.index(melhor_aptidao)]
        historico_aptidao.append(1 / melhor_aptidao)

        print(f"Geração {geracao + 1}: Melhor distância: {1 / melhor_aptidao}")

        populacao = nova_geracao_com_elitismo(populacao, aptidoes, taxa_mutacao, pontos, elite)

        # Atualizar gráfico do rota a cada 10 gerações
        if (geracao + 1) % 10 == 0:
            caminho_completo = melhor_caminho + [melhor_caminho[0]]  # Volta ao ponto inicial
            x = [pontos[i][0] for i in caminho_completo]
            y = [pontos[i][1] for i in caminho_completo]
            linha.set_xdata(x)
            linha.set_ydata(y)
            plt.draw()
            plt.pause(1.0)  # Pausa para atualizar o gráfico

    plt.ioff()  # Desativa o modo interativo
    plt.show()  # Exibe o gráfico final

    return melhor_caminho, historico_aptidao






# Testando com pontos dispostos em círculo
pontos_circulares = criar_pontos_circulares(25)
melhor_rota, historico = algoritmo_genetico(pontos_circulares)

plotar_rota(pontos_circulares, melhor_rota, "Rota Circular")

# Testando com pontos aleatórios (uniformemente distribuídos)
pontos_uniformes = criar_pontos_uniformes(25)
melhor_rota, historico = algoritmo_genetico(pontos_uniformes)

plotar_rota(pontos_uniformes, melhor_rota, "Rota Uniforme")

# Plotar histórico de aptidao (melhor distância ao longo das gerações)
plt.plot(historico)
plt.title("Evolução do aptidao ao Longo das Gerações")
plt.xlabel("Geração")
plt.ylabel("Melhor Distância")
plt.show()