frutas = [
    'uva',
    'banana'
    ]

produto = {
    'nome':'Teclado', 
    'quantidade': 30, 
    'preco': 200.99
    }


estoque = [
    {
        'nome':'teclado', 
        'preco': 45.99
    },
    {
        'nome':'mouse', 
        'preco': 12.99
    },
    {
        'nome':'Monitor', 
        'preco': 1200.99
    },
    {
        'nome':'processador', 
        'preco': 12000.99
    }
]

novo_produto = {
    'nome': 'Placa de vídeo',
    'preco': 7800.00
}

def mostrar_produtos():
    for produto in estoque:
        print (produto)

def adicionar_produto(produto):
    estoque.append(produto)

adicionar_produto(novo_produto)
mostrar_produtos()
