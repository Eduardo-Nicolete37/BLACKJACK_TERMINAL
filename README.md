<div align="center">
  <h1>🃏 BlackJack Terminal</h1>
  <p>
    <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge" alt="Status"/>
    <img src="https://img.shields.io/badge/Plataforma-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Windows"/>
  </p>
  <p>Jogo de BlackJack (21) interativo rodando diretamente no terminal, com interface premium desenhada em caracteres de caixa Unicode, sistema de saves em JSON e configurações persistentes. <strong>Projeto atualmente em desenvolvimento.</strong></p>
</div>

---

## 🚧 Status do Projeto

### ✅ Implementado

**Interface & Navegação**
- Menu principal com Box Drawing Characters (`╔ ═ ║ ╗ ╚ ╝`)
- Validação de inputs com loops seguros contra entradas inválidas (letras, símbolos, fora do range)
- Função `pad()` personalizada para alinhar bordas corretamente, descontando a largura real de caracteres especiais Unicode (como `║ ♣ ♦ ♠ ♥ —`) que ocupam espaço duplo no terminal
- Retorno suave entre telas via `msvcrt.getch()`
- Limpeza de tela multiplataforma (`cls` / `clear`)

**Sistema de Saves (`data/game_data.json`)**
- 3 slots de salvamento independentes
- Criação automática do arquivo e da pasta `data/` se não existirem
- Exibição dos slots na tela de Novo Jogo e Carregar Jogo, com contagem total de partidas
- Detecção de slot ocupado com prompt de sobrescrita (em refinamento)

**Painel de Estatísticas**
- Exibe por slot: partidas jogadas, vitórias, derrotas, empates, blackjacks e saldo
- Porcentagens calculadas dinamicamente com `f-strings` formatadas

**Configurações Persistentes (`data/settings.json`)**
- **Modo Rápido**: toggle ON/OFF com exibição dinâmica
- **Teto de Buy-In**: valor editável com validação de tipo e limite positivo
- Dados salvos automaticamente no disco após cada alteração

**Outras telas**
- Tela de Regras completa (objetivo, valores das cartas, decisões, pagamentos)
- Tela de Créditos com nome, GitHub, linguagem e versão
- Saída limpa via `sys.exit()`

---

### ⏳ Backlog (próximas etapas)

- [ ] Finalizar lógica de seleção/sobrescrita de slots em `new_game()` e `load_game()`
- [ ] Função de cadastro de novo jogador (nome + buy-in inicial)
- [ ] Lógica de cálculo dinâmico da mão (Ás valendo 1 ou 11)
- [ ] Lógica central de rodadas: distribuição, Hit, Stand, Double Down e IA do Dealer
- [ ] Renderização de cartas grandes (ASCII art, ~10 linhas de altura) lado a lado
- [ ] Animação de flip 3D das cartas com frames em caracteres especiais e `time.sleep()`
- [ ] Descomentar e integrar o módulo `time` (atualmente comentado)

---

## 📁 Estrutura de Arquivos

```
BlackJack_Terminal/
├── main.py
└── data/
    ├── game_data.json   # Saves dos jogadores
    └── settings.json    # Configurações globais
```

### `game_data.json`

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

Slots não utilizados são salvos como `null`. Arquivo sempre lido e escrito com `encoding="utf-8"`.

### `settings.json`

```json
{
    "modo_rapido": false,
    "teto_buyin": 10000
}
```

---

## ▶️ Como executar

**Pré-requisitos:** Python 3.14 instalado no Windows (a navegação por teclas depende do módulo `msvcrt`, exclusivo do Windows).

```bash
# Clone o repositório
git clone https://github.com/Eduardo-Nicolete37/BlackJack_Terminal.git
cd BlackJack_Terminal

# Execute o jogo
python main.py
```

---

## 🛠️ Tecnologias

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/json-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/msvcrt-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/os-Built--in-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/sys-Built--in-blue?style=flat-square"/>
</p>

---

## Autor

**Eduardo Nicolete**

[![GitHub](https://img.shields.io/badge/GitHub-Eduardo--Nicolete37-181717?style=flat-square&logo=github)](https://github.com/Eduardo-Nicolete37)

---

<div align="center">
  <sub>Feito com 🐍 e dedicação para aprender Python na prática.</sub>
</div>