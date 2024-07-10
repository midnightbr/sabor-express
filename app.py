import os

restaurantes = [{'nome':'Pizza', 'categoria':'Italiana', 'ativo':False},
                {'nome':'Lazanha', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Lamen', 'categoria':'Japonesa', 'ativo':False}]

def exibir_nome_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      ''')

def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def opcao_selecionada():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        # Opção para python < 3.10
        # if opcao_escolhida == 1:
        #     print('Cadastrar restaurante')
        # elif opcao_escolhida == 2:
        #     print('Listar restaurantes')
        # elif opcao_escolhida == 3:
        #     print('Ativar restaurante')
        # else:
        #     finalizar_app()

        # Opção disponivel a partir do python >= 3.10
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
                voltar_menu_principal()
            case 3:
                ativar_desativar_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_restaurante():
    '''Esta função cadastra um novo restaurante

        Inputs:
        - Nome do restaurante
        - Categoria

        Outputs:
        - Adicionar um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    restaurantes.append({'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False})
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    '''Esta função lista todos os restaurantes do dicionario
    
        Outputs:
        - Escreve na tela todos os restaurantes do dicionario

    '''
    exibir_subtitulo('Listando os restaurantes cadastrados:')
    print(f'  {'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    print('--------------------------------------------------------------')
    for restaurante in restaurantes:
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {'Ativado' if restaurante['ativo'] else 'Desativado'}')

def ativar_desativar_restaurante():
    '''Está função altera o status do restaurate para ativado e desativado
    
        Inputs:
        - Nome do restaurante

        Outputs:
        - Altera o status do restaurante para o inverso que está cadastrado

    '''
    exibir_subtitulo('Alterando estado do restaurante')
    print('\nRestaurantes cadastrados:')
    print(f'  {'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    print('--------------------------------------------------------------')
    for restaurante in restaurantes:
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {'Ativado' if restaurante['ativo'] else 'Desativado'}')
    print()
    nome_restaurante = input('\nDigite o nome do restaurante que deseja alterar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            # Usando operação ternaria
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restauraante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado')

    voltar_menu_principal()

# Função Finalizar App
def finalizar_app():
    exibir_subtitulo('Finalizando o app.\n')

def exibir_subtitulo(texto):
    linha = '*' * (len(texto) + 8)
    os.system('cls')
    print(linha)
    print(f'*   {texto}   *')
    print(linha)

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu. ')
    os.system('cls')
    main()

def main():
    exibir_nome_programa()
    exibir_menu()
    opcao_selecionada()
    
if __name__ == '__main__':
    main()