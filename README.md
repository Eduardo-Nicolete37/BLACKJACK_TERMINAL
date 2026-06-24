<div align="center">
  <h1>🃏 BlackJack Terminal</h1>
  <p>
    <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Vers%C3%A3o-v0.9-blueviolet?style=for-the-badge" alt="Versão"/>
    <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge" alt="Status"/>
    <img src="https://img.shields.io/badge/Plataforma-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Windows"/>
  </p>
  <p>Jogo de BlackJack (21) interativo rodando diretamente no terminal, com interface premium desenhada em caracteres de caixa Unicode, sistema de saves em JSON e configurações persistentes. <strong>Projeto atualmente em desenvolvimento.</strong></p>
</div>

---

## 1. Introdução

BlackJack Terminal é um projeto de desenvolvimento de software individual com o objetivo de implementar o jogo de cartas BlackJack (21) em ambiente de terminal Windows. O sistema é desenvolvido inteiramente em Python 3.14, utilizando exclusivamente bibliotecas nativas, e prioriza uma interface de usuário rica construída com caracteres Unicode de Box Drawing. O projeto serve como veículo prático de aprendizado em lógica de programação, manipulação de arquivos JSON, estruturas de controle de fluxo e design de interfaces CLI.

---

## 2. Descrição do Sistema

O sistema é composto por um único módulo principal (`main.py`) que gerencia todas as telas, fluxos de navegação e persistência de dados. A interface é renderizada inteiramente via `print()` com caracteres especiais, e a navegação entre telas ocorre por meio de leitura de tecla com `msvcrt.getch()`. Os dados do jogador e as configurações globais são persistidos em arquivos `.json` na subpasta `data/`.

### 2.1 Estrutura de Arquivos

```
BlackJack_Terminal/
├── main.py
└── data/
    ├── game_data.json   # Saves dos jogadores (3 slots)
    └── settings.json    # Configurações globais
```

### 2.2 Formato dos Dados

**`game_data.json`** — perfis de jogador por slot:

```json
{
    "1": {
        "nome": "Jogador",
        "vitorias": 15,
        "derrotas": 8,
        "empates": 3,
        "blackjacks": 4,
        "saldo": 1250
    },
    "2": null,
    "3": null
}
```

Slots não utilizados são armazenados como `null`. O arquivo é criado automaticamente junto com a pasta `data/` caso não exista.

**`settings.json`** — configurações globais:

```json
{
    "modo_rapido": false,
    "teto_buyin": 10000
}
```

---

## 3. Funcionalidades Implementadas

### 3.1 Interface e Navegação

O sistema utiliza caracteres Unicode de Box Drawing (`╔ ═ ║ ╗ ╚ ╝ ╠ ╣`) para compor painéis de texto alinhados. A função `pad()` foi desenvolvida para corrigir o desalinhamento causado por caracteres de largura dupla (como `║ ♣ ♦ ♠ ♥ —`), que o terminal contabiliza como dois caracteres de espaço. A validação de inputs ocorre em loops `while True` com tratamento de `ValueError`, garantindo que entradas inválidas não interrompam o fluxo. A limpeza de tela é feita de forma multiplataforma via `os.system('cls' if os.name == 'nt' else 'clear')`.

### 3.2 Sistema de Saves

O sistema gerencia três slots de salvamento independentes. Ao iniciar um novo jogo, o slot selecionado é exibido com suas estatísticas (se ocupado) ou indicado como vazio. Caso o slot já possua dados, o sistema solicita confirmação de sobrescrita (S/N) com loop de revalidação. Na tela de Carregar Jogo, a seleção de um slot vazio é bloqueada e exibe aviso orientando o jogador a criar um novo save.

### 3.3 Painel de Estatísticas

Percorre os três slots do arquivo `game_data.json` e exibe, para cada perfil ativo: total de partidas, vitórias, derrotas, empates, blackjacks e saldo atual. As porcentagens de vitória, derrota e empate são calculadas dinamicamente e formatadas com uma casa decimal.

### 3.4 Configurações Persistentes

A tela de configurações carrega e salva o arquivo `settings.json` a cada interação. O **Modo Rápido** é alternado por negação booleana (`not`). O **Teto de Buy-In** aceita apenas inteiros positivos, com validação de tipo e intervalo. Ambas as configurações são exibidas de forma dinâmica na tela, refletindo o estado atual do arquivo.

### 3.5 Demais Telas

- **Regras**: painel explicativo com objetivo, valores das cartas, decisões (Hit, Stand, Double Down) e tabela de pagamentos.
- **Créditos**: informações do desenvolvedor, link GitHub e versão do jogo.
- **Saída**: encerramento limpo via `sys.exit()`.

---

## 4. Backlog

| # | Funcionalidade | Status | Descrição |
|---|---|---|---|
| 1 | Cadastro de jogador | ✅ Concluído | Tela para inserir nome e buy-in inicial ao criar um novo save |
| 2 | Cálculo dinâmico da mão | 🔄 Pendente | Função que trata o Ás valendo 1 ou 11 para evitar estouro |
| 3 | Lógica de rodadas | 🔄 Pendente | Distribuição de cartas, decisões do jogador (Hit, Stand, Double) e IA do Dealer (compra até 17) |
| 4 | Renderização de cartas | 🔄 Pendente | ASCII art de cartas (~10 linhas de altura) exibidas lado a lado |
| 5 | Animação de flip 3D | 🔄 Pendente | Frames em caracteres especiais com `time.sleep()` simulando virada de carta |
| 6 | Integração do módulo `time` | 🔄 Pendente | Descomentar e integrar delays nas animações |

---

## 5. Histórico de Atualizações

| Versão | Data | Commits | Principais alterações |
|---|---|---|---|
| v0.1 | 28/05/2026 | `196e7e5` | Início do projeto — estrutura base e definição do baralho |
| v0.2 | 29/05/2026 | `0873dcb` `91465a1` `470228c` | Adição dos naipes, início da estrutura de menus |
| v0.3 | 31/05/2026 | `2443527` `4b4d805` `495c4f9` `f6171c` `2580354` | Começo do menu principal, correção de tratamento de erros, mesclagem das funções de avaliação do tipo de mão |
| v0.4 | 02/06/2026 | `9375f04` `0ec1ca2f` `ba52d7a` | Features iniciais de estatísticas, adição do README e .gitignore |
| v0.5 | 03/06/2026 | `840fb75` `2c3d484` `79fba65` | Visualização de estatísticas do player, correção de atribuição de slot, atualização do README |
| v0.6 | 06/06/2026 | `759893a` `25b21f3b` | Início da tela de configurações |
| v0.7 | 07/06/2026 | `f11098fa` `c282e4b` `6491be1` `b9e8be1` | Finalização das funções 4, 5 e 6 (estatísticas, configurações, créditos), correções e documentação |
| v0.8 | 16/06/2026 | `3c4552a` | Início da lógica do jogo principal |
| v0.8.1 | 20/06/2026 | `7886e57` `6d7898d` `5f7895d` | Início da lógica de carregamento de saves, configuração do load_game, atualização do README |
| v0.9 | 23/06/2026 | `9ff7cdb` `5e8511d` | Correção do `break` incorreto nas confirmações de sobrescrita de slot; sistema de menus, saves, estatísticas e configurações considerado estável |

---

## 6. Como Executar

**Pré-requisitos:** Python 3.14 instalado no Windows. A navegação por teclas depende do módulo `msvcrt`, exclusivo do Windows.

```bash
# Clone o repositório
git clone https://github.com/Eduardo-Nicolete37/BlackJack_Terminal.git
cd BlackJack_Terminal

# Execute o jogo
python main.py
```

---

## 7. Tecnologias Utilizadas

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/json-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/msvcrt-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/os-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/sys-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/random-Built--in-blue?style=flat-square"/>
</p>

---

## Autor

**Eduardo Nicolete**

[![GitHub](https://img.shields.io/badge/GitHub-Eduardo--Nicolete37-181717?style=flat-square&logo=github)](https://github.com/Eduardo-Nicolete37)

---

<div align="center">
  <sub>Feito com 🐍 e dedicação para aprender Python na prática.</sub>
</div>
