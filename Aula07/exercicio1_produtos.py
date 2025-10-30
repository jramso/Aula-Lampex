# Lista de produtos fornecida no enunciado
Produtos = [
    {
        "nome": "maquina de lavar",
        "valor": 1350.0,
        "quantidade": 12,
        "comentarios": ["bacana", "veio arranhada", "gasta muita energia"],
        "notas": [1, 1, 1, 3, 5, 1, 1, 2, 1, 1],
    },
    {
        "nome": "placa de video",
        "valor": 15732.99,
        "quantidade": 3,
        "comentarios": ["top", "tem raytracing", "muito rapida", "barulhenta", "esquenta bastante"],
        "notas": [5, 5, 5, 5, 5, 4, 5, 4, 4, 5, 5],
    },
    {
        "nome": "biografia- ozzy osbourne",
        "valor": 9.99,
        "quantidade": 30,
        "comentarios": ["bem maluco", "um monstro sagrado do rock"],
        "notas": [5, 1, 3, 4, 5, 5],
    },
    {
        "nome": "geladeira frost free",
        "valor": 2469.50,
        "quantidade": 4,
        "comentarios": ["gostei", "maior do que esperava", "linda", "nao produz gelo:O"],
        "notas": [4, 4, 5, 3, 3, 3, 4, 5, 1, 0],
    },
]

# Função para mostrar nome, número de comentários e nota média de cada produto

# Função da letra B
def info_produtos(lista):

    for produto in lista:
        nome = produto["nome"]
        num_comentarios = len(produto["comentarios"])
        media = sum(produto["notas"]) / len(produto["notas"]) 
        print(f"{nome} | {num_comentarios} | {media:.2f}")

# Função para mostrar o último comentário de cada produto


def ultimo_comentario(lista):
    print("\nc. Último comentário de cada produto:")
    print("-" * 50)
    for produto in lista:
        nome = produto["nome"]
        comentarios = produto["comentarios"]
        if comentarios:
            ultimo = comentarios[-1]
        else:
            ultimo = "Sem comentários"
        print(f"{nome}: {ultimo}")

# Função para mostrar os produtos com nota acima da média geral


def produtos_acima_da_media(lista):
    # Juntar todas as notas
    todas_notas = []
    for produto in lista:
        todas_notas.extend(produto["notas"])

    media_geral = sum(todas_notas) / len(todas_notas)
    print(f"\ne. Média geral das notas: {media_geral:.2f}")
    print("Produtos com nota acima da média:")

    for produto in lista:
        media_produto = sum(produto["notas"]) / len(produto["notas"])
        if media_produto > media_geral:
            print(f"- {produto['nome']}")

# Função para aplicar 10% de desconto em todos os preços


def aplicar_desconto(lista):
    for produto in lista:
        produto["valor"] = produto["valor"] * 0.9

# Função para registrar a venda do 4º produto (índice 3)


def vender_quarto_produto(lista):
    lista[3]["quantidade"] = lista[3]["quantidade"] - 1

# Função para mostrar a lista de produtos (nome, preço e estoque)


def mostrar_produtos(lista):
    print("\nLista atualizada:")
    print("-" * 50)
    for i, p in enumerate(lista):
        print(
            f"{i+1}. {p['nome']} - R${p['valor']:.2f} - Estoque: {p['quantidade']}")

# --- PROGRAMA PRINCIPAL ---


# a. Número de produtos
print("a. Número de produtos:", len(Produtos))

# b. Informações por produto
info_produtos(Produtos)

# c. Último comentário
ultimo_comentario(Produtos)

# d. Terceiro produto (índice 2)
terceiro = Produtos[2]
print(
    f"\nd. Terceiro produto: {terceiro['nome']} - Estoque: {terceiro['quantidade']}")

# e. Produtos com nota acima da média
produtos_acima_da_media(Produtos)

# f. Aplicar desconto de 10%
print("\nf. Aplicando 10% de desconto em todos os preços...")
aplicar_desconto(Produtos)
mostrar_produtos(Produtos)

# g. Venda do 4º produto
print("\ng. Vendendo uma unidade do 4º produto...")
vender_quarto_produto(Produtos)
mostrar_produtos(Produtos)
