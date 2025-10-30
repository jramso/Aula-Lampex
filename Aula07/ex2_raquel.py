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

# a. Soma das estatisticas em ordem ascendente de pontuacao
soma_status= {}

for lutador in personagens:
    status = personagens[lutador]
    total = status["forca"] + status["vida"] + status["velocidade"] + status["magia"]
    soma_status[lutador] = total

lista = []
for lutador in soma_status:
    lista.append((soma_status[lutador],lutador))

lista = sorted(lista)

print("a. Soma das estatisticas em ordem ascendente de pontuacao")
print("")

for total,nome in lista:
    print(f"{nome}: {total}")


# B. Mostre na tela os valores médios das estatísticas de todos os personagens.

for lutador in personagens:
    status = personagens[lutador]
    media_forca = status["forca"] / len(personagens)
    media_vida = status["vida"] / len(personagens)
    media_velocidade = status["velocidade"] / len(personagens)
    media_magia = status["magia"] / len(personagens)
    media = (media_forca + media_vida + media_velocidade + media_magia) / 4
    print(f"{lutador}: {media:.2f}")
 

# C. Mostre na tela o nome do personagem mais escolhido para lutar.
def personagem_mais_escolhido(lutas_lista):
    contagem = {}
    for luta in lutas_lista:
        p1 = luta["p1"]
        p2 = luta["p2"]

        if p1 in contagem:
            contagem[p1] += 1
        else:
            contagem[p1] = 1

        if p2 in contagem:
            contagem[p2] = contagem[p2]+1
        else:
            contagem[p2] = 1


    max_escolhas = max(contagem.values())
    candidatos = []
    for nome in contagem:
        if contagem[nome] == max_escolhas:
            candidatos.append(nome)
    
    candidatos.sort()
    mais_escolhido = candidatos[0]
    return mais_escolhido
print(f"O personagem mais escolhido para lutar é: {personagem_mais_escolhido(lutas)}")


def personagem_mais_vencedor(lutas):


return mais_vencedor
