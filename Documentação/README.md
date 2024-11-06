# Documentação do Algoritmo Genético para o Problema do Caixeiro Viajante

## 1. Introdução
Este projeto implementa um algoritmo genético para resolver o Problema do Caixeiro Viajante (TSP). O objetivo é encontrar a rota de menor distância que passe por todos os pontos e retorne ao ponto inicial, utilizando técnicas de seleção, cruzamento, mutação e elitismo. Para o componente Curricular de Sistemas Inteligentes.

## 2. Requisitos
- **Linguagem:** Python 3
- **Bibliotecas:** `random`, `numpy`, `matplotlib.pyplot`

## 3. Estrutura e Funcionamento

O código é dividido em várias funções que executam as operações principais do algoritmo genético, incluindo geração de cromossomos, cálculo de fitness, seleção de pais, cruzamento, mutação e melhoria de caminhos.

### 3.1 Funções principais

- **`distancia(ponto1, ponto2)`**: Calcula a distância euclidiana entre dois pontos.
  - **Parâmetros**: 
    - `ponto1`, `ponto2`: Tuplas `(x, y)` representando as coordenadas dos pontos.
  - **Retorno**: Distância euclidiana entre `ponto1` e `ponto2`.

- **`aptidao(caminho, pontos)`**: Avalia a aptidão de um caminho.
  - **Parâmetros**: 
    - `caminho`: Lista com a ordem dos pontos visitados.
    - `pontos`: Lista de tuplas com as coordenadas dos pontos.
  - **Retorno**: Valor da aptidão (inverso da distância total percorrida).

- **`gerar_caminho(pontos)`**: Gera um caminho aleatório.
  - **Parâmetros**: 
    - `pontos`: Lista de pontos para visitação.
  - **Retorno**: Lista com a ordem de visitação dos pontos.

- **`selecao(populacao, aptidoes)`**: Seleciona um caminho com base no método de torneio.
  - **Parâmetros**: 
    - `populacao`: Lista de caminhos.
    - `aptidoes`: Lista de valores de aptidão correspondentes.
  - **Retorno**: Rota selecionado para cruzamento.

- **`cruzamento(pai1, pai2)`**: Realiza o cruzamento de dois caminhos, gerando um filho.
  - **Parâmetros**: 
    - `pai1`, `pai2`: Listas representando os pais.
  - **Retorno**: Rota resultante do cruzamento.

- **`mutacao(caminho, taxa_mutacao, pontos)`**: Aplica mutação e melhora o caminho por inversão.
  - **Parâmetros**: 
    - `caminho`: Lista com a ordem dos pontos.
    - `taxa_mutacao`: Taxa de mutação aplicada.
    - `pontos`: Lista de pontos.
  - **Retorno**: Rota mutado e otimizado.

- **`nova_geracao_com_elitismo(populacao, fitness_pop, taxa_mutacao, pontos, elitismo=True)`**: Gera uma nova população, preservando o melhor caminho da geração anterior.
  - **Parâmetros**: 
    - `populacao`, `aptidoes`, `taxa_mutacao`, `pontos`, `elitismo`.
  - **Retorno**: Nova população.

- **`algoritmo_genetico(pontos, tamanho_populacao=100, num_geracoes=50, taxa_mutacao=0.08, elitismo=True)`**: Função principal do algoritmo.
  - **Parâmetros**:
    - `pontos`: Lista de pontos.
    - `tamanho_populacao`: Número de caminhos na população inicial.
    - `num_geracoes`: Número de gerações.
    - `taxa_mutacao`: Taxa de mutação.
    - `elitismo`: Habilita/desabilita o elitismo.
  - **Retorno**: Melhor caminho encontrado e histórico de aptidão.

- **`criar_pontos_circulares(quantidade, raio=10)`** e **`gerar_pontos_uniformes(quantidade, limite=10)`**: Geram pontos para o problema.

- **`plotar_caminho(pontos, caminho, titulo="Rota")`**: Plota o caminho final.

### 3.2 Passo a Passo do Funcionamento
1. **Inicialização**: A população inicial é gerada aleatoriamente.
2. **Avaliação de Aptidão**: Cada caminho recebe uma pontuação de aptidão.
3. **Seleção e Cruzamento**: Os caminhos mais aptos são cruzados para formar novos caminhos.
4. **Mutação**: Pequenas mutações são aplicadas para introduzir diversidade.
5. **Elitismo**: O melhor caminho é preservado na nova geração.
6. **Iteração**: O processo se repete para o número de gerações especificado.

## 4. Uso

Para testar o algoritmo:
- Execute o código para ver o desempenho com pontos dispostos em um círculo ou distribuídos aleatoriamente.
- Após as execuções, será exibido o histórico de aptidão e o gráfico do melhor caminho.

### Exemplo de Execução

```python
# Geração de pontos uniformemente distribuídos
pontos_uniformes = gerar_pontos_uniformes(15)
melhor_caminho, historico = algoritmo_genetico(pontos_uniformes)
plotar_caminho(pontos_uniformes, melhor_caminho, "Rota Uniforme")

# Geração de pontos circulares
pontos_circulares = criar_pontos_circulares(15)
melhor_caminho, historico = algoritmo_genetico(pontos_circulares)
plotar_caminho(pontos_circulares, melhor_caminho, "Rota Circular")

