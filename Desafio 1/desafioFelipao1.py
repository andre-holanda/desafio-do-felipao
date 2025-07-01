"""_summary_
    Desenvolvedor: André Holanda
    Data: 30/06/2025
    - Classificação de nível de Herói -
    Resumo: Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:
        Se XP for menor do que 1.000 = Ferro
        Se XP for entre 1.001 e 2.000 = Bronze
        Se XP for entre 2.001 e 5.000 = Prata
        Se XP for entre 6.001 e 7.000 = Ouro
        Se XP for entre 7.001 e 8.000 = Platina
        Se XP for entre 8.001 e 9.000 = Ascendente
        Se XP for entre 9.001 e 10.000 = imortal
        Se XP for maior ou igual a 10.001 = Radiante
    Saída:
        Ao final deve se exibir uma mensagem:
        "O Herói de nome **{nome}** está no nível de **{nivel}**"
"""
while True:
    nome = input("Informe o nome do seu Personagem: ")
    xp = int(input("Informe a quantidade de XP do seu Personagem: "))

    match xp:
        case _ if xp <= 1_000:
            nivel = "Ferro"
        case _ if 1_000 <= xp <= 2_000:
            nivel = "Bronze"
        case _ if 2_001 <= xp <= 3_000:
            nivel = "Prata"
        case _ if 3_001 <= xp <= 4_000:
            nivel = "Ouro"
        case _ if 4_001 <= xp <= 5_000:
            nivel = "Platina"
        case _ if 5_001 <= xp <= 6_000:
            nivel = "Ascendente"
        case _ if 6_001 <= xp <= 7_000:
            nivel = "Imortal"
        case _:
            nivel = "Radiante"
    
    print(f"\nO Herói de nome ** {nome} ** está no nível ** {nivel} **")
    
    nova_execucao = input("\nDeseja executar novamente (s ou n): ")
    if nova_execucao.lower() == "s":
        continue
    elif nova_execucao.lower() == "n":
        break
    else:
        print("Vocês escolheu uma opção inválida, execução encerrada!")
        break