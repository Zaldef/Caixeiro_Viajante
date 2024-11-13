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

def plotar_rota(pontos, rota, titulo):
    """
    Plota a rota final que passa por todos os pontos.
    """

    rota_completa = rota + [rota[0]]
    x = [pontos[i][0] for i in rota_completa]
    y = [pontos[i][1] for i in rota_completa]

    plt.figure(figsize=(9, 9))
    plt.plot(x, y, marker='o')
    plt.title(f"{titulo}: Melhor distância = {1/ aptidao(rota, pontos)}")
    plt.savefig(titulo, dpi=300)

def plotar_aptidao(historico_aptidao, gen, titulo):
    """
    Plota a evolução da aptidão ao longo das gerações.
    """
    plt.clf()
    plt.plot(historico_aptidao)
    plt.title(f"{titulo}: Melhor geração = {gen}")
    plt.xlabel("Geração")
    plt.ylabel("Melhor Distância")
    plt.savefig(titulo, dpi=300)

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
    Seleciona um indivíduo da população com base em um torneio de 5 indivíduos.
    """

    torneio = random.sample(list(zip(populacao, aptidoes)), 5)
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

def inverter_rota(rota, pontos):
    """
    Realiza uma melhoria no rota trocando duas cidades e verificando se a inversão melhora a distância.
    """

    for i in range(1, len(rota) - 1):
        distancia_atual = (distancia(pontos[rota[i-1]], pontos[rota[i]]) + distancia(pontos[rota[i]], pontos[rota[i+1]]))
        distancia_invertida = (distancia(pontos[rota[i-1]], pontos[rota[i+1]]) + distancia(pontos[rota[i+1]], pontos[rota[i]]))

        if distancia_invertida < distancia_atual:
            rota[i], rota[i+1] = rota[i+1], rota[i]

    return rota

def mutacao(rota, taxa_mutacao, pontos):
    """
    Realiza uma mutação no rota trocando duas cidades aleatórias.
    """

    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(rota)), 2)
        rota[i], rota[j] = rota[j], rota[i]

    return inverter_rota(rota, pontos)

def elitismo(populacao, aptidoes, taxa_mutacao, pontos, elite=True):
    """
    Gera uma nova população com base na aptidão dos indivíduos da geração anterior.
    """

    nova_populacao = []

    if elite:
        num_elite = max(1, int(0.05 * len(populacao)))
        melhores_indices_5 = np.argsort(aptidoes)[-num_elite:]
        
        for indice in melhores_indices_5:
            nova_populacao.append(populacao[indice])

    for _ in range(len(populacao) - len(nova_populacao)):
        pai1 = selecao(populacao, aptidoes)
        pai2 = selecao(populacao, aptidoes)
        filho = cruzamento(pai1, pai2)
        filho = mutacao(filho, taxa_mutacao, pontos)
        nova_populacao.append(filho)

    return nova_populacao

def algoritmo_genetico(pontos, teste, tamanho_populacao, num_geracoes, taxa_mutacao, elite):
    """
    Algoritmo Genético para resolver o Problema do Caixeiro Viajante.
    """

    populacao = [criar_rota_aleatoria(pontos) for _ in range(tamanho_populacao)]
    historico_aptidao = []

    melhor_rota_ = None
    melhor_geracao_ = None
    melhor_aptidao = None

    for geracao in range(num_geracoes):
        aptidoes = [aptidao(rota, pontos) for rota in populacao]
        if melhor_aptidao is None or max(aptidoes) > melhor_aptidao:
            melhor_geracao_ = geracao + 1
        melhor_aptidao = max(aptidoes)
        melhor_rota_ = populacao[aptidoes.index(melhor_aptidao)]
        historico_aptidao.append(1 / melhor_aptidao)

        # print(f"Geração {geracao + 1} /  Melhor distância: {1 / melhor_aptidao} / melhor geração: {melhor_geracao_}")

        populacao = elitismo(populacao, aptidoes, taxa_mutacao, pontos, elite)

        # if (geracao + 1) % 10 == 0 or geracao == 0:
        #     rota_completo = melhor_rota_ + [melhor_rota_[0]] 
        #     x = [pontos[i][0] for i in rota_completo]
        #     y = [pontos[i][1] for i in rota_completo]
        #     plt.clf()
        #     plt.scatter([p[0] for p in pontos], [p[1] for p in pontos], color='red')
        #     plt.plot(x, y, 'b-', marker='o', markersize=5)
        #     plt.title(f"Geração {geracao + 1}: Melhor distância = {1 / melhor_aptidao}")
        #     plt.xlim(-16, 16) 
        #     plt.ylim(-16, 16)
        #     plt.savefig(f'{teste}_gen_{geracao + 1}.png', dpi=300)

    return melhor_rota_, historico_aptidao, melhor_geracao_



# -------------- MAIN --------------

matriz_resultados= np.zeros((10,3,4,4,4,2))
testes = [1,2,3,4,5,6,7,8,9,10]
pontos_ = [criar_pontos_circulares(20), criar_pontos_uniformes(20), criar_pontos_circulares(200)]
populacoes = [50, 100, 150, 200]
geracoes = [50, 100, 150, 200]
taxas_mutacao = [0.025, 0.05, 0.075, 0.1]
elite_ = [True, False]

for i in range(10):
    np.save("matriz_resultados.npy", matriz_resultados)
    for j in range(3):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    for n in range(2):
                        melhor_rota, historico, melhor_gen = algoritmo_genetico(pontos_[j],
                                                                            teste = f"Teste {i+1}. {j+1}. {k+1}. {l+1}. {m+1}. {n+1}",
                                                                            tamanho_populacao=populacoes[k],
                                                                            num_geracoes=geracoes[l],
                                                                            taxa_mutacao=taxas_mutacao[m],
                                                                            elite=elite_[n])
                        plotar_aptidao(historico, melhor_gen, f"Teste {i+1}. {j+1}. {k+1}. {l+1}. {m+1}. {n+1}")
                        matriz_resultados[i,j,k,l,m,n] = 1 / aptidao(melhor_rota, pontos_[j])




# # Teste Pontos Circulares - 20 pontos
# pontos_circulares = criar_pontos_circulares(20)
# plotar_rota(pontos_circulares, criar_rota_aleatoria(pontos_circulares), "Pontos Circulares Aleatórios")
# melhor_rota, historico, melhor_gen = algoritmo_genetico(pontos = pontos_circulares,
#                                             teste = "Pontos Circulares Simples",
#                                             tamanho_populacao=100,
#                                             num_geracoes=30,
#                                             taxa_mutacao=0.02,
#                                             elite=True)
# plotar_rota(pontos_circulares, melhor_rota, "Rota Circular Simples Otimizada")
# plotar_aptidao(historico, melhor_gen, "Evolução da Aptidão Pontos Circulares Simples")

# # Teste Pontos Uniformes - 20 pontos
# pontos_uniformes = criar_pontos_uniformes(20)
# plotar_rota(pontos_uniformes, criar_rota_aleatoria(pontos_uniformes), "Pontos Uniformes Aleatórios")
# melhor_rota, historico, melhor_gen = algoritmo_genetico(pontos = pontos_uniformes,
#                                             teste = "Pontos Uniformes Simples",
#                                             tamanho_populacao=100,
#                                             num_geracoes=200,
#                                             taxa_mutacao=0.02,
#                                             elite=True)
# plotar_rota(pontos_uniformes, melhor_rota, "Rota Uniforme Simples Otimizada")
# plotar_aptidao(historico, melhor_gen, "Evolução da Aptidão Pontos Uniformes Simples")

# # Teste Pontos Circulares - 200 pontos
# pontos_circulares = criar_pontos_circulares(200)
# plotar_rota(pontos_circulares, criar_rota_aleatoria(pontos_circulares), "Pontos Circulares Aleatórios")
# melhor_rota, historico, melhor_gen = algoritmo_genetico(pontos = pontos_circulares,
#                                             teste = "Pontos Circulares Complexos",
#                                             tamanho_populacao=200,
#                                             num_geracoes=200,
#                                             taxa_mutacao=0.1,
#                                             elite=False)
# plotar_rota(pontos_circulares, melhor_rota, "Rota Circular Complexa Otimizada")
# plotar_aptidao(historico, melhor_gen, "Evolução da Aptidão Pontos Circulares Complexos")
