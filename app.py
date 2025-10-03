import os

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

def finalizar_app():
    os.system('cls')
    print('Finalizando o app...\n')
    exit()

def escolher_opcao():
    opcao_usuario = int(input('Escolha uma opção: '))

    if opcao_usuario == 1:
        cadastro_restaurante()
        print('Cadastrar restaurante')
    elif opcao_usuario == 2:
        print('Listar restaurantes')
    elif opcao_usuario == 3:
        print('Ativar restaurante')
    elif opcao_usuario == 4:
        finalizar_app()
    else:
        print('Opção inválida! Tente novamente.\n')
        escolher_opcao()

def main():
    os.system('cls')
    nome_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()