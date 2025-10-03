import os

restaurantes = ['Pizza Hut', 'McDonalds', 'Burger King']

def nome_programa():
    print("""
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀

    """)

def exibir_opções():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Ativar restaurante')
    print('4 - Sair\n')

def escolher_opcao():
    opcao_usuario = int(input('Escolha uma opção: '))

    if opcao_usuario == 1:
        cadastro_restaurante()
    elif opcao_usuario == 2:
        listar_restaurantes()
    elif opcao_usuario == 3:
        print('Ativar restaurante')
    elif opcao_usuario == 4:
        finalizar_app()
    else:
        print('Opção inválida! Tente novamente.\n')
        escolher_opcao()

def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    escolher_opcao()

def cadastro_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    input('\nPressione ENTER para voltar ao menu principal...')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes cadastrados...\n')

    for restaurante in restaurantes:
        print(f'- {restaurante}')

    input('\nPressione ENTER para voltar ao menu principal...')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app...\n')
    exit()

def main():
    os.system('cls')
    nome_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()