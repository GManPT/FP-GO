# Projeto 2: Jogo de Go - IST

## Descrição

Neste projeto de Jogo de Go, parte integrante do curso de Engenharia Informática no Instituto Superior Técnico (IST) de Lisboa, os alunos desenvolverão um programa em Python para implementar um jogo de Go. O Go é um jogo de tabuleiro estratégico para dois jogadores, no qual o objetivo é controlar o território do tabuleiro.

### Regras do Jogo de Go

O Go é jogado em um tabuleiro quadriculado, onde os jogadores alternam entre colocar pedras pretas e brancas. O objetivo é conquistar território, cercar grupos de pedras do oponente e capturar pedras do oponente.

## Funcionalidades Implementadas

O projeto consiste na implementação de várias funcionalidades essenciais para o jogo de Go. Algumas das principais funcionalidades incluem:

### Representação do Tabuleiro

O tabuleiro é representado internamente como uma estrutura de dados específica em Python. A posição das pedras no tabuleiro é atualizada após cada jogada.

### Regras de Colocação de Pedras

Funções são implementadas para verificar a validade de uma jogada, garantindo que as regras de colocação de pedras sejam seguidas.

### Verificação de Capturas

Mecanismos para verificar e processar capturas de pedras, removendo as pedras capturadas do tabuleiro.

### Fim do Jogo

O jogo termina quando ambos os jogadores concordam ou quando não há mais movimentos válidos. O programa determina o vencedor com base na contagem de território controlado por cada jogador.

## Como Executar o Jogo

Para jogar o jogo de Go implementado, siga as instruções abaixo:

1. Clone o repositório para o seu ambiente local.
2. Execute o programa principal em um ambiente Python:

```bash
python FP2324P2.py
