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

def mostrar_produtos(lista):
    for produto in lista:
        print(f"Nome: {produto['nome']}")
        