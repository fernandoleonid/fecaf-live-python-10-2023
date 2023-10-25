def escrever_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(conteudo + '\n')
    arquivo.close

def apagar_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write('')
    arquivo.close



def ler_aquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    conteudo = arquivo.read()
    arquivo.close
    return conteudo

def mostar(tarefas):
    numero = 0
    for tarefa in tarefas.splitlines():
        print(f'{numero} - {tarefa}')
        numero += 1

def exibir_menu():
    print('#### MENU ####')
    print('1 - Adicionar tarefa')
    print('2 - Mostrar tarefas')
    print('3 - Atualizar tarefa')
    print('4 - Excluir tarefa')
    print('0 - Sair')

def selecionar_menu(opcao):
    if opcao == '1':
        tarefa = input('Digite uma nova tarefa: ')
        escrever_arquivo('controle_tarefas.txt', tarefa)
    elif opcao == '2':
        tarefas = ler_aquivo('controle_tarefas.txt')
        print(tarefas)
        input('Aperte qualquer tecla para continuar!')
    elif opcao == '3':
        tarefas = ler_aquivo('controle_tarefas.txt')
        mostar(tarefas)
        tarefas = tarefas.splitlines()
        numero_tarefa = int(input('Digite o número da tarefa para atualizar: '))
        nova_tarefa = input('Digite a nova tarefa')
        tarefas[numero_tarefa] = nova_tarefa
        tarefas = '\n'.join(tarefas)
        apagar_arquivo('controle_tarefas.txt')
        escrever_arquivo('controle_tarefas.txt', tarefas)

    elif opcao == '4':
        tarefas = ler_aquivo('controle_tarefas.txt')
        mostar(tarefas)
        tarefas = tarefas.splitlines()
        numero_tarefa = int(input('Digite o número da tarefa para atualizar: '))
        del tarefas[numero_tarefa]
        tarefas = '\n'.join(tarefas)
        apagar_arquivo('controle_tarefas.txt')
        escrever_arquivo('controle_tarefas.txt', tarefas)
    elif opcao == '0':
        print('Saindo do programa...')
        exit(0)

    else:
        print('Opção incorreta, tente novamente!')



def executar_sistema():
    exibir_menu()
    opcao = input('Escolha uma opção: ')
    selecionar_menu(opcao)
    executar_sistema()


executar_sistema()