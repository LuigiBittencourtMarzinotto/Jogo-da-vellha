import os
import random
matriz = []
modo = ""
linhaChecagem= 0
jogador = 1
def tabuleiro():
    for x in range(3):
        linha =[]
        for y in range(5):
            if y%2 !=0:
                linha.append("|")
            else:
                linha.append(" _ ")
        matriz.append(linha)
    for linha in matriz:
        for coluna in linha:
            print(coluna, end="")
        print("\n")

def validacao():
    colunaVerifica = []
    colunaVerificadois = []
    colunaVerificatres = []
    for linha in matriz:
        linhaVerifica = []
        for coluna in linha:
        #linha
            if coluna !="|":
                linhaVerifica.append(coluna) 
        if linhaVerifica[0]== linhaVerifica[1] and linhaVerifica[0] == linhaVerifica[2] and linhaVerifica[0] != " _ " :
            return "Ganhou"
        #Coluna
        colunaVerifica.append(linha[0])
        colunaVerificadois.append(linha[2])
        colunaVerificatres.append(linha[4])
    if colunaVerifica[0]== colunaVerifica[1] and colunaVerifica[0] == colunaVerifica[2] and colunaVerifica[0] != " _ " :
        return "Ganhou"
    if colunaVerificadois[0]== colunaVerificadois[1] and colunaVerificadois[0] == colunaVerificadois[2] and colunaVerificadois[0] != " _ " :
        return "Ganhou"
    if colunaVerificatres[0]== colunaVerificatres[1] and colunaVerificatres[0] == colunaVerificatres[2] and colunaVerificatres[0] != " _ " :
        return "Ganhou"
    if matriz[0][0]== matriz[1][2] and matriz[0][0]== matriz[2][4] and matriz[0][0]!= " _ ":
        return "Ganhou"
    if matriz[0][4]== matriz[1][2] and matriz[0][4]== matriz[2][0] and matriz[0][4]!= " _ ":
        return "Ganhou"
    else:
        linhaChecagem = 0
        for linhaEmpate in matriz:
            for colunaEmpate in linhaEmpate:
                if colunaEmpate == ' _ ':
                    linhaChecagem +=1
        if linhaChecagem ==0:
            return "Empate"
        
def view ():
    for linha in matriz:
        for coluna in linha:
            print(coluna, end="")
        print("\n")

def play(modo):
    print("A posição são passadas pelo teclado númerico de 1 a 9")
    global jogador
    valor = ""
    while True: 
        if modo == 1:
            print(f"É a vez do jogador N°{jogador}")
            posicao = input("Digite uma posição: ")
            if posicao.isdigit()==False:
                os.system("cls")
                print("Valor invalido")
                print("Tente novamente")
                view()
                play(modo)
        else : 
            if jogador == 1:
                print(f"É a vez do jogador N°{jogador}")
                posicao = input("Digite uma posição: ")
                if posicao.isdigit()==False:
                    os.system("cls")
                    print("Valor invalido")
                    print("Tente novamente")
                    view()
                    play(modo)
            else:
                os.system("cls")
                print(f"É a vez do jogador N°{jogador}")
                posicao = random.randint(1,9)
                print(f"A I.A escolheu a posição {posicao}")


        if  int(posicao)<=9:
            posicao = int(posicao)
            if jogador ==1:
                valor=" X "
            else:
                valor = " O "
            if posicao>0 and posicao<=3:
                if posicao>1 and posicao!=2:
                    posicao=posicao+1
                elif posicao==1:
                    posicao = posicao-1
                else:
                    posicao = 2
                if matriz[2][posicao] == " _ ":
                    matriz[2][posicao]=valor
                else:
                    print("Valor invalido")
                    view()
                    play(modo)
            elif posicao>3 and posicao<=6:
                posicao = posicao -3
                if posicao>1 and posicao!=2:
                    posicao=posicao+1
                elif posicao==1:
                    posicao = posicao-1
                else:
                    posicao = 2
                if matriz[1][posicao] == " _ ":
                    matriz[1][posicao]=valor
                else:
                    print("Valor invalido")
                    view()
                    play(modo)
            else:
                posicao = posicao -6
                if posicao>1 and posicao!=2:
                    posicao=posicao+1
                elif posicao==1:
                    posicao = posicao-1
                else:
                    posicao = 2
                if matriz[0][posicao] == " _ ":
                    matriz[0][posicao]=valor
                else:
                    print("Valor invalido")
                    view()
                    play(modo)
            validacao()
            resultado = validacao()
            if resultado == "Ganhou":
                print (f"O jogador N° {jogador} ganhou")
                view()
                start()
            elif resultado == "Empate":
                os.system("cls")
                view()
                print (f"Empatou")
                start()
            else:

                if jogador==1:
                    jogador+=1
                else:
                    jogador=1
                view()
        else:
            os.system("cls")
            print("Valor invalido")
            play()
        
def switch(case):
    if case == 1:
        global matriz
        print("ESCOLHA UM MODO: ")
        print("1 - Jogador n° 1 x Jogador n° 2")
        print("2 - Jogador n° 1 x I.A")
        modoEscolha= input("Digite o numero: ")
        matriz = []
        modoEscolha = int(modoEscolha)
        global modo
        modo = modoEscolha
        if modo <= 2:
            tabuleiro()
            play(modo)
        else:
            os.system("cls")
            print("Valor invalido")
            start()
def start():
    while True:
        print("ESCOLHA UM E DIGITE O NÚMERO: ")
        print("1 - Jogar jogo da velha")
        print("2 - Sair")
        case = input("Digite o numero: ")
        if int(case)> 2:
            print("valor invalido")
            os.system("cls")
            start()
        if int(case) == 2:
            print("Saindo...")
            exit()
        switch(int(case))
start()
