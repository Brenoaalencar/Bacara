#EP - Design Software
#Dupla: Breno Alencar e Nívea Abreu
#Data:

#Bacará

print("            ")
print("Bacará V0.01")
print("                                          ___")
print(" ____                                    /__/")
print("| __ )    __ _    ___    __ _   _ __    __ _ ") 
print("|  _ \   / _` |  / __|  / _` | | '__|  / _` |")
print("| |_) | | (_| | | (__  | (_| | | |    | (_| |")
print("|____/   \__,_|  \___|  \__,_| |_|     \__,_|")

#Recolhendo dados dos jogadores
print("   ")
print("Bem-vindo(a) ao Bacará!")
print("   ")

#Dados jogador 1
jogador1=input("Qual o seu nome? ")
print("   ")
print(jogador1,",", "você tem 100 fichas!")
#Fichas iniciais
ficha1=100
print("   ")

#Definindo outros jogadores
jogadores=int(input("Quantos jogadores na partida? Máximo de 3 jogadores. "))

if jogadores == 0:
    print("   ")
    print ("Até logo!")
else :
    while jogadores < 0 or jogadores > 3:
        print("Digite 1, 2 ou 3 jogadores")
        jogadores=int(input("Quantos jogadores na partida? Máximo de 3 jogadores : "))

    if jogadores == 2 :
        jogador2=input("Qual o seu nome, jogador 2? ")
        print("   ")
        ficha2=100
        print(jogador2,",", "você tem 100 fichas!")

    elif jogadores == 3 :
        jogador2=input("Qual o seu nome, jogador 2? ")
        print("   ")
        ficha2=100
        print(jogador2,",", "você tem 100 fichas!")

        jogador3=input("Qual o seu nome, jogador 3? ")
        ficha3=100
        print("   ")
        print(jogador3,",", "você tem 100 fichas!")

    else :
        print(" ")

    #Definindo número de baralhos
    print("   ")
    baralhos=int(input("Quantos baralhos utilizar? 1, 6 ou 8? "))
    
    
          
    #Randomizando cartas
    import random
    from random import randint
    Às = 1
    Q = 0
    J = 0
    K = 0
    cartas = [Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K,Às,2,3,4,5,6,7,8,9,10,Q,J,K]
   
          
    if baralhos == 1:
        random.shuffle(cartas)
            
    elif baralhos == 6 :
        cartas = cartas*6
        random.shuffle(cartas)
            
    elif baralhos == 8 :
        cartas = cartas*6
        random.shuffle(cartas)

    print("Vamos às apostas?!")
    print("Vamos começar a embaralhar as cartas!")
    #Apostas dos jogadores
    if jogadores == 1:
        aposta_jog1 = int(input("Quanto quer apostar, jogador 1? "))
    
    elif jogadores == 2:
        aposta_jog1 = int(input("Quanto quer apostar, jogador 1? "))
        aposta_jog2 = int(input("Quanto quer apostar, jogador 2? "))
    
    elif jogadores == 3:
        aposta_jog1 = int(input("Quanto quer apostar, jogador 1? "))
        aposta_jog2 = int(input("Quanto quer apostar, jogador 2? "))
        aposta_jog3 = int(input("Quanto quer apostar, jogador 3? "))
    else :
        print ("  ")

    #Distribuindo cartas para os jogadores
    c1=randint(0,len(cartas))
    if jogadores == 1 :
        carta1_1 = cartas [c1]
        del cartas [c1]
        c2=randint(0,len(cartas))
        cartas1_2 = cartas [c2]
        del cartas [c2]       
    
    








