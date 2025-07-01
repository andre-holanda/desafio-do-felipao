""" Desenvolvedor: André Holanda
    Data: 01/07/2025
    - Calculadora de partidas Rankeadas -
    Resumo: Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador, depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)
"""

def menu():

    menu = """
    ### Opções ###

    1 - Iniciar partida
    2 - Encerra jogo

    Informe o número:
"""

    return int(input(f"{menu} -> "))

def main():

    while True:
        opcao = menu()

        match opcao:
            case 1:
                print("\nJogo iniciado")
            case 2:
                print("\nEncerrando jogo")
                break
            case _:
                print("\nEscolha uma opção válida !")

main()

#     jogador = input("Informe o nome do seu Personagem: ")
#     vitorias = int(input("Informe a quantidade de Vitórias: "))
#     derrotas = int(input("Informe a quantidade de Derrotas: "))

    

# while True:
    
#     if xp <= 1_000:
#         nivel = "Ferro"
#         print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
#     elif (xp >= 1_001) and (xp <= 2_000):
#         nivel = "Bronza"
#         print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
#     elif (xp >= 2_001) and (xp <= 5_000):
#         nivel = "Prata"
#         print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
#     elif (xp >= 6_001) and (xp <= 7_000):
#         nivel = "Ouro"
#         print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
#     elif (xp >= 7_001) and (xp <= 8_000):
#         nivel = "Platina"
#         print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
#     elif (xp >= 8_001) and (xp <= 9_000):
#         nivel = "Ascendente"
#         print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
#     elif (xp >= 9_001) and (xp <= 10_000):
#         nivel = "Imortal"
#         print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
#     else:
#         nivel = "Radiante"
#         print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    
#     nova_execucao = input("Deseja executar novamente (s ou n): ")
#     if nova_execucao.lower() == "s":
#         continue
#     elif nova_execucao.lower() == "n":
#         break
#     else:
#         print("Vocês escolheu uma opção inválida, execução encerrada!")
#         break