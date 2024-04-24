def mostrarIngredientes():
    print("Ingrediente Quantidade inicial")
    print("Pó de Fênix 100 g")
    print("Essência Celestial 50 ml")
    print("Raiz de Dragão 45g")
    print("Orvalho Lunar 30 ml")
    print("Flores secas 200 g")
    print("Elixir amargo 20 ml")
    print("Lágrimas de unicórnio 15 ml")


def escolhaMenu(opcao):
    if opcao == 3:
        print("Você fechou o programa.")

    elif opcao == 2:
        mostrarIngredientes()

    else:
        print("Lista de poções")
        print("1. Poção de Cura. Ingredientes: Pó de Fênix (30g), Essência Celestial (20 ml), Flores secas (20g), Lágrimas de unicórnio (10 ml)")
        print("2. Poção Força da Floresta. Ingredientes: Orvalho Lunar (20 ml), Raiz de Dragão (30g), Flores secas (30g)")
        print("3. Poção Sabedoria da Riqueza. Ingredientes: Essência Celestial (30 ml), Pó de Fênix (50g)")
        print("4. Poção Sorte no Amor. Ingredientes: Orvalho Lunar (10 ml), Flores secas (50g), Lágrimas deunicórnio (5 ml)")
        print("5. Poção Malvada. Ingredientes: Elixir amargo (10 ml), Raiz de Dragão (15g)")

        opcaoPocao = int(input("Digite o número da poção que deseja preparar: "))
        if opcaoPocao in poções:
            ingredientes_poção = poções[opcaoPocao]
            faltando = []
            for ingrediente, quantidade_necessaria in ingredientes_poção.items():
                if ingrediente in ingredientes and ingredientes[ingrediente] >= quantidade_necessaria:
                    ingredientes[ingrediente] -= quantidade_necessaria
                else:
                    faltando.append(ingrediente)
            if faltando:
                print("Ingredientes faltando para preparar a poção:", ", ".join(faltando))
            else:
                print("Poção criada com sucesso!")
        else:
            print("Número de poção inválido.")



ingredientes = {
    "Pó de Fênix": 100,
    "Essência Celestial": 50,
    "Raiz de Dragão": 45,
    "Orvalho Lunar": 30,
    "Flores secas": 200,
    "Elixir amargo": 20,
    "Lágrimas de unicórnio": 15
}


poções = {
    1: {"Pó de Fênix": 30, "Essência Celestial": 20, "Flores secas": 20, "Lágrimas de unicórnio": 10},
    2: {"Orvalho Lunar": 20, "Raiz de Dragão": 30, "Flores secas": 30},
    3: {"Essência Celestial": 30, "Pó de Fênix": 50},
    4: {"Orvalho Lunar": 10, "Flores secas": 50,"Lágrimas de unicórnio": 5},
    5: {"Elixir amargo": 10, "Raiz de Dragão": 15}
}

while True:
    print("\nMenu")
    print("1. Preparar poção")
    print("2. Consultar os ingredientes disponíveis")
    print("3. Sair")

    opcao = int(input("Digite a opção que deseja: "))

    if opcao == 1 or opcao == 2 or opcao == 3:
        escolhaMenu(opcao)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue

    if opcao == 3:
        break
