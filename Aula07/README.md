# 📚 Exercícios de Listas, Funções e Dicionários em Python

Este repositório contém a resolução de exercícios práticos voltados ao uso de **listas**, **dicionários** e **funções** em Python, com foco em manipulação de dados estruturados — como produtos de e-commerce e personagens de jogos.

---

## 📁 Estrutura do Projeto

```
.
├── README.md
├── exercicio1_produtos.py     # Solução do exercício 1 (produtos de e-commerce)
└── exercicio2_personagens.py  # Solução do exercício 2 (personagens de jogo)
```

---

## 🧩 Exercício 1: Produtos de E-commerce

### Objetivo
Manipular uma lista de dicionários que representam produtos, extraindo e atualizando informações como:
- Número total de produtos
- Nome, número de comentários e nota média de cada produto
- Último comentário de cada produto
- Informações do terceiro produto (por índice)
- Produtos com nota acima da média geral
- Aplicação de desconto de 10% em todos os preços
- Atualização de estoque após uma venda (4º produto)

### Dados de exemplo
```python
Produtos = [
  {
    "nome": "maquina de lavar",
    "valor": 1350.0,
    "quantidade": 12,
    "comentarios": ["bacana", "veio arranhada", ...],
    "notas": [1, 1, 1, 3, 5, ...]
  },
  # ...
]
```

---

## 🎮 Exercício 2: Personagens de Jogo

### Objetivo
Trabalhar com um dicionário de dicionários contendo estatísticas de personagens e uma lista de lutas registradas, para:
- Calcular a soma total das estatísticas de cada personagem e ordená-los
- Calcular as médias das estatísticas entre todos os personagens
- Identificar o personagem **mais escolhido** nas lutas (com desempate alfabético)
- Identificar o personagem que **mais venceu** (com desempate alfabético)

### Dados de exemplo
```python
personagens = {
  "zangief": {"forca": 100, "vida": 150, "velocidade": 0, "magia": 0},
  "ken": {"forca": 50, "vida": 100, "velocidade": 50, "magia": 50},
  # ...
}

lutas = [
  {"p1": "ryu", "p2": "ryu", "venceu": "p1"},
  {"p1": "ken", "p2": "zangief", "venceu": "p2"},
  # ...
]
```

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone ou baixe este repositório.
3. Execute os arquivos individualmente:

```bash
python exercicio1_produtos.py
python exercicio2_personagens.py
```

Cada script exibe no terminal as respostas para os respectivos itens do enunciado.

---

## 🛠️ Requisitos

- Python 3.x
- Nenhuma biblioteca externa é necessária (apenas recursos nativos do Python)

---

## 📝 Observações

- Todas as funções pedidas nos enunciados foram implementadas conforme solicitado.
- Os códigos seguem boas práticas de legibilidade e modularização.
- Em casos de empate (ex: personagem mais escolhido), a solução aplica o desempate por ordem alfabética, conforme instruído.

---

Desenvolvido com ❤️ para fins educacionais.