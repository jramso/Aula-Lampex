# Dados fornecidos no enunciado
personagens = {
    "zangief": {
        "forca": 100, 
        "vida": 150, 
        "velocidade": 0, 
        "magia": 0
    },
    "ken": {"forca": 50, "vida": 100, "velocidade": 50, "magia": 50},
    "ryu": {"forca": 75, "vida": 100, "velocidade": 50, "magia": 25},
    "chun-li": {"forca": 25, "vida": 75, "velocidade": 125, "magia": 50}
}

lutas = [
    {"p1": "ryu", "p2": "ryu", "venceu": "p1"},
    {"p1": "ken", "p2": "zangief", "venceu": "p2"},
    {"p1": "ken", "p2": "chun-li", "venceu": "p1"},
    {"p1": "ken", "p2": "ken", "venceu": "p2"},
    {"p1": "zangief", "p2": "zangief", "venceu": "p2"},
    {"p1": "ryu", "p2": "chun-li", "venceu": "p2"},
    {"p1": "chun-li", "p2": "chun-li", "venceu": "p1"},
]

# Função para calcular a soma das estatísticas de cada personagem


def somar_estatisticas(personagens_dict):
    soma_por_personagem = {}
    for nome, stats in personagens_dict.items():
        total = stats["forca"] + stats["vida"] + stats["velocidade"] + stats["magia"]
        soma_por_personagem[nome] = total
    return soma_por_personagem

# Função para mostrar os personagens em ordem crescente da soma total


def mostrar_soma_ordenada(personagens_dict):
    soma = somar_estatisticas(personagens_dict)
    # Criar lista de (nome, total) e ordenar pelo total (e depois pelo nome, em caso de empate)
    lista_ordenada = sorted(soma.items(), key=lambda x: (x[1], x[0]))
    print("a. Soma das estatísticas (ordem crescente):")
    print("-" * 40)
    for nome, total in lista_ordenada:
        print(f"{nome}: {total}")

# Função para calcular as médias das estatísticas entre todos os personagens


def mostrar_medias(personagens_dict):
    total_forca = total_vida = total_velocidade = total_magia = 0
    num_personagens = len(personagens_dict)

    for stats in personagens_dict.values():
        total_forca += stats["forca"]
        total_vida += stats["vida"]
        total_velocidade += stats["velocidade"]
        total_magia += stats["magia"]

    print("\nb. Médias das estatísticas:")
    print("-" * 40)
    print(f"Força média: {total_forca / num_personagens:.2f}")
    print(f"Vida média: {total_vida / num_personagens:.2f}")
    print(f"Velocidade média: {total_velocidade / num_personagens:.2f}")
    print(f"Magia média: {total_magia / num_personagens:.2f}")

# Função que retorna o personagem mais escolhido nas lutas


def personagem_mais_escolhido(lutas_lista):
    contagem = {}

    for luta in lutas_lista:
        p1 = luta["p1"]
        p2 = luta["p2"]
        # Conta quantas vezes cada personagem foi escolhido
        contagem[p1] = contagem.get(p1, 0) + 1
        contagem[p2] = contagem.get(p2, 0) + 1

    # Encontrar o máximo de escolhas
    max_escolhas = max(contagem.values())
    # Filtrar os que têm esse máximo
    candidatos = [nome for nome, qtd in contagem.items() if qtd == max_escolhas]
    # Em caso de empate, escolher por ordem alfabética
    mais_escolhido = min(candidatos)  # min() dá o primeiro em ordem alfabética
    return mais_escolhido

# Função que retorna o personagem que mais venceu


def personagem_mais_vitorias(lutas_lista):
    vitorias = {}

    for luta in lutas_lista:
        vencedor_key = luta["venceu"]  # "p1" ou "p2"
        if vencedor_key == "p1":
            nome_vencedor = luta["p1"]
        else:
            nome_vencedor = luta["p2"]

        vitorias[nome_vencedor] = vitorias.get(nome_vencedor, 0) + 1

    # Encontrar o máximo de vitórias
    max_vitorias = max(vitorias.values())
    # Filtrar candidatos com máximo de vitórias
    candidatos = [nome for nome, qtd in vitorias.items() if qtd ==
                  max_vitorias]
    # Em caso de empate, ordem alfabética
    mais_vitorioso = min(candidatos)
    return mais_vitorioso

# Função para mostrar os dados de um personagem


def mostrar_dados_personagem(nome, personagens_dict):
    dados = personagens_dict[nome]
    print(f"\nNome: {nome}")
    print(f"Força: {dados['forca']}")
    print(f"Vida: {dados['vida']}")
    print(f"Velocidade: {dados['velocidade']}")
    print(f"Magia: {dados['magia']}")

# --- PROGRAMA PRINCIPAL ---


# a. Soma das estatísticas em ordem crescente
mostrar_soma_ordenada(personagens)

# b. Médias das estatísticas
mostrar_medias(personagens)

# c. Personagem mais escolhido
mais_usado = personagem_mais_escolhido(lutas)
print("\nc. Personagem mais escolhido nas lutas:")
print("-" * 40)
mostrar_dados_personagem(mais_usado, personagens)

# d. Personagem que mais venceu
mais_vitorias = personagem_mais_vitorias(lutas)
print("\nd. Personagem que mais venceu:")
print("-" * 40)
mostrar_dados_personagem(mais_vitorias, personagens)
