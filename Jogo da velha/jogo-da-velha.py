print("Bem-vindo ao jogo de X e O")

numero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
jogadas = 0

def imprimir_tabuleiro():
    for i in range(0, 9, 3):
        print(numero[i], numero[i+1], numero[i+2])

def verificar_vitoria():
    
    for i in range(0, 9, 3):
        if numero[i] == numero[i+1] == numero[i+2]:
            return True
    
    for i in range(3):
        if numero[i] == numero[i+3] == numero[i+6]:
            return True
    
    if numero[0] == numero[4] == numero[8] or numero[2] == numero[4] == numero[6]:
        return True
    return False

imprimir_tabuleiro()

while jogadas < 9:
    print("JOGADOR X: Agora é a vez do jogador X")
    num = int(input("Digite a posição que pretende para X (1-9): "))
    
    if 1 <= num <= 9 and numero[num - 1] not in ['X', 'O']:
        numero[num - 1] = "X"
    else:
        print("Posição inválida ou já ocupada, tente novamente.")
        continue
    
    imprimir_tabuleiro()
    
    if verificar_vitoria():
        print("JOGADOR X venceu!")
        break
    
    jogadas += 1
    
    if jogadas >= 9:
        break
    
    print("JOGADOR O: Agora é a vez do jogador O")
    n = int(input("Digite a posição que pretende para O (1-9): "))
    
    if 1 <= n <= 9 and numero[n - 1] not in ['X', 'O']:
        numero[n - 1] = "O"
    else:
        print("Posição inválida ou já ocupada, tente novamente.")
        continue
    
    imprimir_tabuleiro()
    
    if verificar_vitoria():
        print("JOGADOR O venceu!")
        break
    
    jogadas += 1

if jogadas == 9:
    print("O jogo terminou em empate!")
