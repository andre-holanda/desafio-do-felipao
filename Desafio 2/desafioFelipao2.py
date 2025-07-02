""" Desenvolvedor: André Holanda
    Data: 01/07/2025
    - Calculadora de partidas Rankeadas -
    
    Resumo:
        Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador, depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

        Se vitórias for menor do que 10 = Ferro
        Se vitórias for entre 11 e 20 = Bronze
        Se vitórias for entre 21 e 50 = Prata
        Se vitórias for entre 51 e 80 = Ouro
        Se vitórias for entre 81 e 90 = Diamante
        Se vitórias for entre 91 e 100= Lendário
        Se vitórias for maior ou igual a 101 = Imortal

    ## Saída
        Ao final deve se exibir uma mensagem:
        "O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"
"""

def menu():    
    menu = """
    ### Opções ###

    1 - Iniciar partida
    2 - Encerra jogo

    Informe o número:
"""
    return int(input(f"{menu}    -> "))

def calcularVitorias(vitorias, derrotas):
    resultado = vitorias - derrotas
    if resultado < 0:
        resultado = 0

    rank = ranking(resultado)

    return resultado, rank

def ranking(pontos):
    match pontos:
        case _ if pontos <= 10:
            ranking = "Ferro"
        case _ if 11 <= pontos <= 20:
            ranking = "Bronze"
        case _ if 21 <= pontos <= 50:
            ranking = "Prata"
        case _ if 51 <= pontos <= 80:
            ranking = "Ouro"
        case _ if 81 <= pontos <= 90:
            ranking = "Diamante"
        case _ if 91 <= pontos <= 100:
            ranking = "Lendário"
        case _:
            ranking = "Imortal"
        
    return ranking

def main():

    while True:
        opcao = menu()

        match opcao:
            case 1:
                print("\nJogo iniciado")
                jogador = input("Informe o nome do seu Personagem: ")
                vitorias = int(input("Informe a quantidade de Vitórias: "))
                derrotas = int(input("Informe a quantidade de Derrotas: "))

                resultado, ranking = calcularVitorias(vitorias, derrotas)

                print(f"O Herói {jogador}, tem saldo de {resultado}, e está no nível de {ranking} ")
            case 2:
                print("\nEncerrando jogo")
                break
            case _:
                print("\nEscolha uma opção válida !")

main()