""" Desenvolvedor: André Holanda
    Data: 01/07/2025
    - Escrevendo as classes de um jogo -
    
    Objetivo:
        Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:
        
        - nome
        - idade
        - tipo (ex: guerreiro, mago, monge, ninja )
        
        além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:
        - exibir a mensagem: "o {tipo} atacou usando {ataque}"  
        - aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe  
        - e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:  

        se mago -> no ataque exibir (usou magia)  
        se guerreiro -> no ataque exibir (usou espada)  
        se monge -> no ataque exibir (usou artes marciais)  
        se ninja -> no ataque exibir (usou shuriken)  

    Saída:
        Ao final deve se exibir uma mensagem:
        - "o {tipo} atacou usando {ataque}"
        ex: mago atacou usando magia
            guerreiro atacou usando espada
"""

# Classe herói
class hero():
    def __init__(self, name, age, type_character):
        self.name = name
        self.age = age
        self.type = type_character
    
    # Método atacar
    def attack(type):
        match type.lower():
            case "mago":
                attacked = "magia"
            case "guerreiro":
                attacked = "espada"
            case "monge":
                attacked = "artes marciais"
            case "ninja":
                attacked = "shuriken"
        return attacked

name = input("Informe o nome do personagem: ")
age = int(input("Informe a idade do personagem: "))
type_character = input("Informe o tipo do personagem (mago, guerreiro, monge ou ninja): ")

result = hero.attack(type_character)
print(f"O {type_character} atacou usando {result}")