# Enunciado

Criar e explorar o uso de um algoritmo genético para solucionar (localmente) o problema do caixeiro viajante.

## Objetivo:
Desenvolver um algoritmo genético completo que minimize a distância percorrida em um problema do Caixeiro Viajante, considerando pontos em duas dimensões e caminhos cíclicos.

---

## Tarefas

### 1. Desenvolvimento do Algoritmo Genético
- [ ] Criar o algoritmo genético completo:
  - [ ] Definir a população inicial
  - [ ] Implementar a seleção
  - [ ] Definir a taxa de mutação e a operação de mutação
  - [ ] Implementar o cruzamento
  - [ ] Definir a função de aptidão (distância euclidiana)
  - [ ] Implementar o critério de parada

### 2. Cenários a serem analisados
- [ ] Implementar e testar o cenário com pontos uniformemente distribuídos
- [ ] Implementar e testar o cenário com pontos distribuídos em um círculo (benchmark)

### 3. Acompanhamento da evolução do algoritmo
- [ ] Mostrar a solução encontrada a cada época para o caso com pontos aleatórios
- [ ] Mostrar a solução encontrada a cada época para o caso circular

### 4. Explicações e Justificativas
- [ ] Explicar as escolhas de população e critério de parada
- [ ] Explicar a escolha da taxa de mutação
- [ ] Explicar a escolha da representação do gene e do cruzamento
- [ ] Explicar a função de aptidão

### 5. Testes e Avaliação
- [ ] Criar um caso simples para testar o algoritmo
- [ ] Criar um caso extremo para testar o algoritmo (cenário com maior quantidade de pontos)
- [ ] Anotar o tempo gasto para convergência e soluções intermediárias para o modelo circular
- [ ] Realizar uma avaliação do desempenho da solução encontrada (com gráficos e métricas)

### 6. Bônus
- [ ] Realizar um teste com uma quantidade alta de pontos para o modelo circular
- [ ] Anotar o tempo gasto para convergência e algumas soluções intermediárias

---

## Pontuação

- **Algoritmo Genético e Parametrização:**  
  - Definição clara da população, cruzamento, seleção, mutação e critério de parada.

- **Soluções para Cenários Aleatório e Circular:**  
  - Acompanhamento da evolução da solução a cada época para os dois cenários.

- **Explicações Técnicas:**  
  - Justificativas para as escolhas de parâmetros e operações no algoritmo.

- **Testes e Avaliação de Desempenho:**  
  - Realização de testes para verificar o funcionamento do algoritmo em diferentes cenários e quantidades de pontos.

- **Bônus:**  
  - Teste com grande quantidade de pontos no cenário circular.
