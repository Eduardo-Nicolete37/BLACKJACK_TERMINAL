<div align="center">
  <h1>🃏 BlackJack Terminal</h1>
  <p>
    <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge" alt="Status"/>
  </p>
  <p>Jogo de BlackJack (21) interativo rodando diretamente no terminal, com foco em uma interface premium desenhada em caracteres de caixa. <strong>Projeto atualmente em desenvolvimento.</strong></p>
</div>

---

## 🚧 Status do Projeto e Desenvolvimento

O projeto está sendo desenvolvido de forma colaborativa e por etapas. Abaixo está o progresso do que já está funcional e do que está planejado para as próximas sessões de programação:

### ✅ O que já foi implementado:

* **Menu Principal Interativo**: Tela inicial desenhada com Box Drawings oferecendo opções de jogo, regras, estatísticas, configurações e créditos.
* **Navegação Inteligente**: Validação de inputs no terminal com loops de captura segura contra entradas inválidas de tipo (letras/símbolos) e lógica de opções.
* **Tela de Regras Completa**: Um painel explicativo detalhando o objetivo, valores das cartas, fluxo e pagamentos, com retorno suave ao menu inicial usando a tecla de atalho `msvcrt.getch()`.
* **Gerenciador de Saves**: Bloco `try/except` robusto capaz de ler as informações do arquivo `game_data.json` na subpasta `data/` ou criar um novo arquivo contendo 3 slots de salvamento zerados se o arquivo não existir.
* **Painel de Estatísticas**: Loop que percorre os slots do JSON e exibe partidas, vitórias, derrotas, empates, blackjacks e saldo de cada jogador — com porcentagens calculadas dinamicamente e alinhamento de bordas corrigido via função `pad()` que desconta a largura real de caracteres especiais do terminal.
* **Painel de Configurações**: Tela de configurações persistentes carregadas do arquivo `settings.json` na subpasta `data/`. Conta com exibição dinâmica e possibilita alterar o **Modo Rápido** (toggles ON/OFF) e o **Teto de Buy-In** (com validação completa de tipo e limite positivo), salvando os novos dados no disco e atualizando a tela de forma fluida.
* **Menu de Créditos**: Tela de créditos personalizada contendo as informações do desenvolvedor (nome, GitHub, linguagem Python 3.14 e versão do jogo).
* **Encerramento Seguro**: Opção de sair integrada de forma limpa usando `sys.exit()`.

### ⏳ O que será desenvolvido nas próximas etapas (Backlog):

* **Finalização das Configurações**:

* **Lógica de Cálculo Dinâmico**: Implementação da função que calcula o valor da mão, tratando os Áses de forma inteligente (valendo 1 ou 11) para evitar estouros.
* **Lógica de Rodadas (Jogo Central)**: A mesa de jogo em si, incluindo a distribuição, decisões do jogador (Hit, Stand, Double Down) e a inteligência artificial do Dealer.
* **Cartas Grandes (10 linhas de altura)**: Renderização das cartas lado a lado no terminal.
* **Animação Flip 3D**: Efeito visual de virada das cartas utilizando frames em caracteres especiais e intervalos de tempo.

---

## Estrutura do Arquivo de Salvamento (`game_data.json`)

O jogo gerencia os perfis por slots de gravação organizados no seguinte formato JSON:

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
Slots ainda não utilizados são salvos como `null`. O arquivo é sempre lido e escrito com `encoding="utf-8"`.

### Configurações Globais (`settings.json`)

```json

{

    "modo_rapido": false,

    "teto_buyin": 10000

}

```

---

## Tecnologias utilizadas

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/json-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/msvcrt-Built--in-blue?style=flat-square"/>
</p>

---

## Como executar (Versão de Desenvolvimento)

**Pré-requisitos:** Python 3.14 instalado (Sistema Operacional Windows necessário para navegação por teclas).

```bash
# Clone o repositório
git clone https://github.com/Eduardo-Nicolete37/BlackJack_Terminal.git
cd BlackJack_Terminal

# Execute o menu do jogo
python main.py
```

---

## Autor

**Eduardo Nicolete**

[![GitHub](https://img.shields.io/badge/GitHub-Eduardo--Nicolete37-181717?style=flat-square&logo=github)](https://github.com/Eduardo-Nicolete37)

---

<div align="center">
  <sub>Feito com 🐍 e dedicação para aprender Python na prática.</sub>
</div>
</div>
