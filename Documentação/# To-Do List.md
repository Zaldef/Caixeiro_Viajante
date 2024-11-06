# To-Do List

## Análise e Documentação
- [x] Analisar/documentar o problema do Caixeiro Viajante
- [x] Analisar/documentar a criação dos pontos (cidades) e a representação da rota
- [x] Analisar/documentar a função de aptidão
- [x] Analisar/documentar a função de seleção
- [x] Analisar/documentar a função de cruzamento
- [x] Analisar/documentar a função de mutação
- [x] Analisar/documentar a função de inversão de rota
- [ ] Analisar/documentar a função Elitismo
- [ ] Analisar/documentar a função Algoritmo Genético
- [ ] Ajustar funções de cruzamento e mutação para melhorar eficiência
- [ ] Verificar o comportamento de elitismo com diferentes configurações (com e sem elite)
- [ ] Testar a robustez do algoritmo para diferentes configurações de entrada (diferentes tipos de distribuição de pontos)
- [x] Implementar uma estratégia para evitar ciclos de melhoria local durante o algoritmo genético
- [x] Ajustar a lógica de cruzamento para garantir que a rota gerada seja válida
- [ ] Documentar escolha de variáveis
- [ ] Criar documentação do código geral
- [ ] Documentar a escolha dos parâmetros (taxa de mutação, tamanho da população, etc.)
- [ ] Incluir exemplos de entrada e saída no README e na documentação

## Testes
- [x] Testar a criação de pontos e a representação da rota
- [x] Testar a função de aptidão para diferentes rotas
- [x] Testar a função de seleção para diferentes configurações de população
- [x] Validar se a troca de cidades dentro da função `inverter_rota` realmente melhora a distância (teste de melhoria)
- [x] Testar a função `inverter_rota` para diferentes tamanhos de rota
- [ ] Montar caso simples e caso extremo para testes
- [ ] Validar a performance do algoritmo com diferentes configurações de parâmetros (população, gerações, taxa de mutação)
- [ ] Criar um teste para avaliar o comportamento do algoritmo em diferentes distribuições de pontos (uniforme, circular, etc.)
- [ ] Testar a robustez do algoritmo para um grande número de cidades (pontos)


## Gráficos e Visualização
- [ ] Mudar o tipo de visualização dos gráficos
- [ ] Melhorar a atualização gráfica durante as gerações
- [ ] Implementar gráficos para diferentes métricas (aptidão, distância total)
- [ ] Ajustar a visualização para casos extremos (muitas cidades, visualização de grandes distâncias)
- [ ] Verificar a escalabilidade gráfica quando o número de pontos/cidades for muito grande
- [ ] Implementar a visualização do histórico de aptidão ao longo das gerações

## Bibliotecas e Funcionalidades
- [x] Ler documentação matplotlib
- [ ] Investigar e testar outras bibliotecas para visualização (ex: seaborn, plotly)



## Performance e Otimização
- [ ] Testar a eficiência do algoritmo com grandes quantidades de pontos
- [ ] Analisar a complexidade do algoritmo genético e otimizar, se necessário
- [ ] Implementar um critério de parada para evitar execuções desnecessárias quando a solução estabilizar
- [ ] Avaliar e otimizar o tempo de execução do algoritmo em diferentes tamanhos de população e número de gerações
