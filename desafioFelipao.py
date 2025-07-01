while True:
    nome = input("Informe o nome do seu Personagem: ")
    xp = int(input("Informe a quantidade de XP do seu Personagem: "))

    if xp <= 1_000:
        nivel = "Ferro"
        print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    elif (xp >= 1_001) and (xp <= 2_000):
        nivel = "Bronza"
        print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    elif (xp >= 2_001) and (xp <= 5_000):
        nivel = "Prata"
        print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    elif (xp >= 6_001) and (xp <= 7_000):
        nivel = "Ouro"
        print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    elif (xp >= 7_001) and (xp <= 8_000):
        nivel = "Platina"
        print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    elif (xp >= 8_001) and (xp <= 9_000):
        nivel = "Ascendente"
        print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    elif (xp >= 9_001) and (xp <= 10_000):
        nivel = "Imortal"
        print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    else:
        nivel = "Radiante"
        print(f"O Herói de nome ** {nome} ** está no nível de ** {nivel} **")
    
    nova_execucao = input("Deseja executar novamente (s ou n): ")
    if nova_execucao.lower() == "s":
        continue
    elif nova_execucao.lower() == "n":
        break
    else:
        print("Vocês escolheu uma opção inválida, execução encerrada!")
        break