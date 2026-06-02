# Bibliotecas que vou usar
import os # Para os.system
import random # Embaralar as cartas
import time # Pausa entre entrega de cartas
import msvcrt # Criar as telas de "Aperte qualquerte tecla para continuar"
import json # Salvar as estátisticas

baralho = ["2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As"]
valor_face_cards = {
    "J": 10,
    "Q": 10,
    "K": 10,
}

naipe = {
    "h": "♥",
    "c": "♣",
    "s": "♠",
    "d": "♦"
}

random.shuffle(baralho) # Embaralhamento das cartas

def jogo_central(baralho):
    print # print como placeholder por agora

def menu():
    while True:
        os.system('cls')
        print("╔══════════════════════════════════════╗")
        print("║           ♣ ♦ BLACKJACK ♠ ♥          ║")
        print("╠══════════════════════════════════════╣")
        print("║                                      ║")
        print("║   Selecione uma opção:               ║")
        print("║     1. Começar jogo                  ║")
        print("║     2. Regras                        ║")
        print("║     3. Estátisticas                  ║")
        print("║     4. Configurações                 ║")
        print("║     5. Créditos                      ║")
        print("║     6. Sair                          ║")
        print("║                                      ║")
        print("╚══════════════════════════════════════╝")
        print("")
        while True:
            try:
                choose = int(input("Digite a opção desejada (1-6): "))
                break
            except ValueError:
                print("Valor Inválido! Tente novamente...")
        if choose == 1:
            jogo_central(baralho)
        elif choose == 2:
            os.system('cls')
            print("╔═════════════════════════════════════════════════════════╗")
            print("║                      ♣ ♦ REGRAS ♠ ♥                     ║")
            print("╠═════════════════════════════════════════════════════════╣")
            print("║                                                         ║")
            print("║   1. OBJETIVO                                           ║")
            print("║    - Chegar o mais próximo de 21 sem ultrapassar        ║")
            print("║    - Ganhe do Dealer tendo a maior pontuação.           ║")
            print("║                                                         ║")
            print("║   2. VALOR DAS CARTAS                                   ║")
            print("║     - 2 a 9: Valor nominal | 10, J, Q, K: 10 pts        ║")
            print("║     - Ás (A): Vale 1 ou 11 (dinâmico).                  ║")
            print("║                                                         ║")
            print("║   3. DECISÕES & FLUXO                                   ║")
            print("║     - Pedir (Hit): Solicita mais uma carta.             ║")
            print("║     - Parar (Stand): Mantém a soma e passa a vez.       ║")
            print("║     - Dobrar (Double): Dobra a aposta inicial, recebe   ║")
            print("║        exatamente mais 1 carta e encerra o turno.       ║")
            print("║     - O Dealer DEVE comprar cartas até somar 17.        ║")
            print("║                                                         ║")
            print("║   4. PAGAMENTOS                                         ║")
            print("║     - Vitória Comum paga 1:1 (dobra a aposta).          ║")
            print("║     - Blackjack Natural (Ás + 10 nas 2 primeiras)       ║")
            print("║        paga 1.5:1.                                      ║")
            print("║                                                         ║")
            print("║         Aperte qualquer botão para sair da tela         ║")
            print("║                                                         ║")
            print("╚═════════════════════════════════════════════════════════╝")
            print("")
            msvcrt.getch()
        elif choose == 3:
            try:
                with open("game_data.json", "r") as f:
                    stats = json.load(f)
            except FileNotFoundError:
                game_data= {
                    "1": None,
                    "2": None,
                    "3": None
                }
                with open("game_data.json", "w") as f:
                    json.dump(game_data, f, indent=4)
                stats = game_data
            os.system('cls')
            
            print("╔═══════════════════════════════════════════════╗")
            print("║              ♣ ♦ ESTÁTISTICAS ♠ ♥             ║")
            print("╚═══════════════════════════════════════════════╝")
            print(" ")
            for num_slot in ["1", "2", "3"]:
                if stats[num_slot] is None:
                    print("╔═══════════════════════════════════════════════╗")
                    print(f"║   Slot {num_slot:<39}║")
                    print("║   - SLOT VAZIO -                              ║")
                    print("╚═══════════════════════════════════════════════╝")
                    print("")
            print("")
            msvcrt.getch()

menu() # Para debugging