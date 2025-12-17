import os
import datetime
import json

# Funções globais
def mostrar_menu():
    print('-' * 12, 'MENU PRINCIPAL', '-' * 12)
    print('ADD    -  Adicionar novo projeto')
    print('LIST   -  Listar todos os projetos')
    print('UPDATE -  Atualizar um projeto')
    print('DELETE -  Excluir um projeto')
    print('ABOUT  -  Sobre o projeto')
    print('QUIT   -  Sair do programa')
    print('-' * 40)

def adicionar_projeto(lista_projetos):
    print('-' * 10, 'ADICIONAR PROJETOS', '-' * 10)
    try:
        numero_projetos = int(input('Digite o número de projetos que deseja adicionar: \n').strip())  # Recebe o número de projetos do usuário.
    except ValueError:
        print('-' * 45)
        print('ERRO: Por gentileza, digite um NÚMERO válido.')
        print('-' * 45)
        return  # Cria um ponto de saída imediata da função

    if numero_projetos <= 0:  # Verifica se o numero de projetos é menor ou igual a 0.
        print('-' * 54)
        print('ERRO: Verifique o número de projetos a ser cadastrado.')
        print('-' * 54)
    else:
        for n in range(numero_projetos):  # Percorre o numero de projetos adicionados.
            nome_projeto = (input(f'\nDigite o nome do {n + 1}° projeto: \n')).strip().upper()  # Recebe o nome do projeto adicionado.
            while not nome_projeto:  # Enquanto o nome do projeto for vazio continua perguntando o nome ao usuário.
                limpar_tela()
                sem_nome()
                nome_projeto = (input(f'\nDigite o nome do {n + 1}° projeto: \n')).strip().upper()

            cadastro_projeto = {
                'nome': nome_projeto,
                'concluido': False,
                'historico': []
            }

            lista_projetos.append(cadastro_projeto)  # Adiciona o projeto a lista_projetos.
            
            print(f'\nSUCESSO: "{nome_projeto}" foi adicionado a lista de projetos.')

def listar_projetos(lista_projetos):
    print('-' * 11, 'LISTA DE PROJETOS', '-' * 10)
    if not lista_projetos:
        sem_projeto()
        return
    else:
        for indice, projeto in enumerate(lista_projetos, start=1):  # Percorre os elementos da lista de projetos.
            if projeto['concluido']:
                status_txt = 'Concluído'
            else:
                status_txt = 'Pendente'
            print(f'{indice}. {projeto['nome']} - [{status_txt}]')
            if not projeto['historico']:
                pass
            else:
                print('--','HISTÓRICO:', '-' * 26)
                for registro in projeto['historico']:
                    data_mudanca, descricao = registro
                    print(f'Em {data_mudanca}: {descricao}')

def atualizar_projeto(lista_projetos):
    print('-' * 10, 'ATUALIZAR PROJETOS', '-' * 10)
    if not lista_projetos:
        sem_projeto()
        return
    else:
        relistar_projeto(lista_projetos)
        nome_projeto = input('Digite o NOME do projeto para atualizar: \n').strip().upper()
        while not nome_projeto:  # Enquanto o nome do projeto for vazio continua perguntando o nome ao usuário.
            limpar_tela()
            sem_nome()
            relistar_projeto(lista_projetos)
            nome_projeto = input('\nDigite o nome do projeto para atualizar: \n').strip().upper()

        projeto = encontrar_projeto(lista_projetos, nome_projeto)

        if projeto:
            print('-' * 40)
            print(f'PROJETO: {projeto['nome']} em atualização...')
            print('-' * 40)
            print(f'Opções de atualização para "{projeto['nome']}"')
            print('1 - Atualizar o nome')
            print('2 - Atualizar o status')
            print('3 - Voltar ao menu')
            print('-' * 40)
            escolha_update = input('Digite o número da opção: ').strip()
            while not escolha_update:
                limpar_tela()
                sem_numero()
                print(f'Opções de atualização para "{projeto['nome']}"')
                print('1 - Atualizar o nome')
                print('2 - Atualizar o status')
                print('3 - Voltar ao menu')
                print('-' * 41)
                escolha_update = input('Digite o número da opção: ').strip()
            match escolha_update:
                case '1':
                    print('-' * 10, 'ATUALIZAR NOME', '-' * 10)
                    nome_antigo = projeto['nome']  # Captura o nome antigo do projeto.
                    novo_nome = input(f'Digite o novo nome para "{projeto['nome']}": ').strip().upper()  # Captura o nome novo do projeto.
                    while not novo_nome:  # Enquanto o nome do projeto for vazio continua perguntando o nome ao usuário.
                        limpar_tela()
                        sem_nome()
                        novo_nome = input(f'Digite o novo nome para "{projeto['nome']}": ').strip().upper()
                    projeto['nome'] = novo_nome  # Faz a troca do nome antigo pelo nome novo.
                    data_agora = datetime.datetime.now().strftime('%d-%m-%y %H:%M')  # Captura a data e horario.
                    novo_registro = (data_agora, f'Nome alterado de "{nome_antigo}" para "{novo_nome}"')  # Cria o registro de alteração do nome.
                    projeto['historico'].append(novo_registro)  # Adiciona o registro ao historico.
                    print(f'\nSUCESSO: O nome foi alterado para {projeto['nome']}.')

                case '2':
                    print('-' * 10, 'ATUALIZAR STATUS', '-' * 10)
                    print(f'Qual é o novo status para "{projeto['nome']}"?')
                    print('1 - Concluído')
                    print('2 - Pendente')
                    print('3 - Voltar ao menu')
                    print('-' * 41)
                    modificar_status = input('Digite o número da opção: ').strip()
                    while not modificar_status:
                        limpar_tela()
                        sem_numero()
                        print(f'Qual é o novo status para "{projeto['nome']}"?')
                        print('1 - Concluído')
                        print('2 - Pendente')
                        print('3 - Voltar ao menu')
                        print('-' * 41)
                        modificar_status = input('Digite o número da opção: ').strip()
                    match modificar_status:
                        case '1':
                            projeto['concluido'] = True
                            data_agora = datetime.datetime.now().strftime('%d-%m-%y %H:%M')
                            novo_registro = (data_agora, 'Concluído')
                            projeto['historico'].append(novo_registro)
                            print('\nSUCESSO: Status alterado para "CONCLUÍDO".')

                        case '2':
                            projeto['concluido'] = False
                            data_agora = datetime.datetime.now().strftime('%d-%m-%y %H:%M')
                            novo_registro = (data_agora, 'Pendente')
                            projeto['historico'].append(novo_registro)
                            print('\nSUCESSO: Status alterado para "PENDENTE".')

                        case '3':
                            return

                        case _:
                            sem_numero()

                case '3':
                    return

                case _:
                    sem_numero()

        else:
            print('-' * 40)
            print('   ERRO: O projeto não foi encontrado.')
            print('-' * 40)

def deletar_projeto(lista_projetos):
    print('-' * 12, 'EXCLUIR PROJETO', '-' * 11)
    if not lista_projetos:
        sem_projeto()
        return
    else:
        relistar_projeto(lista_projetos)
        delete_projeto = input('\nDigite o NOME do projeto para excluir: \n').strip().upper()
        projeto = encontrar_projeto(lista_projetos, delete_projeto)
        if projeto:
            print('\nATENÇÃO: Esta ação não pode ser desfeita.\n')
            print(f'Prosseguir com a exclusão do projeto "{projeto['nome']}"?')
            excluir_projeto = input('Digite: EXCLUIR O PROJETO\n').strip().upper()
            if excluir_projeto == 'EXCLUIR O PROJETO':
                lista_projetos.remove(projeto)
                print(f'\nSUCESSO: "{projeto['nome']}" foi excluido.')
            else:
                print('\nExclusão cancelada.')
        else:
            print('\nERRO: O projeto não existe, verifique o NOME.')

def mostrar_sobre():
    print('-' * 11, 'SOBRE O PROJETO', '-' * 12)
    print('Projeto referente a disciplina de Raciocínio Computacional - PUCPR 2025')  # Mostra informações sobre o projeto para o usuário.
    print('Autor: Filipe Vaz')  # Mostra informações do autor para o usuário.
    print('-' * 40)

# Funções utilitárias
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def relistar_projeto(lista_projetos):
    for indice, projeto in enumerate(lista_projetos, start=1):
        print(f'{indice}. {projeto['nome']}')

def encontrar_projeto(lista_projetos, nome_projeto):
    for projeto in lista_projetos:
        if projeto['nome'] == nome_projeto:
            return projeto
    return None

def salvar_dados(lista_projetos):
    with open('portfolio.json', 'w') as arquivos:
        json.dump(lista_projetos, arquivos, indent=4)
        print('-' * 40)
        print(f'SUCESSO: Os dados foram salvos.')

def carregar_dados():
    try:
        with open('portfolio.json', 'r') as arquivos:
            return json.load(arquivos)
    except json.JSONDecodeError:
        print('ERRO: Não foi possível ler o arquivo.')
        return []
    except FileNotFoundError:
        return []

# Funções de mensagens de erro
def sem_projeto():
    print('ERRO: Não existem projetos cadastrados.')
    print('-' * 40)

def sem_nome():
    print('-' * 40)
    print('   ERRO: O projeto não possui um nome.')
    print('-' * 40)

def sem_numero():
    print('-' * 40)
    print('  ERRO: O NÚMERO não foi reconhecido.')
    print('-' * 40)

# Função principal
def main():
    lista_projetos = carregar_dados()
    while True:
        limpar_tela()
        mostrar_menu()
        comando = input('\nPor gentileza, informe um dos comandos disponíveis: \n').strip().upper()  # Recebe o comando do usuário.
        match comando:
            case 'ADD':
                adicionar_projeto(lista_projetos)
            case 'LIST':
                listar_projetos(lista_projetos)
            case 'UPDATE':
                atualizar_projeto(lista_projetos)
            case 'DELETE':
                deletar_projeto(lista_projetos)
            case 'ABOUT':
                mostrar_sobre()
            case 'QUIT':
                salvar_dados(lista_projetos)
                print('-' * 40)
                print('Encerrando o programa...até logo!')
                print('-' * 40)
                break  # Encerra o loop e fecha o programa.
            case _:
                print('-' * 40)
                print('  ERRO: O comando não foi reconhecido.')
                print('-' * 40)
        
        input('\nPressione ENTER para voltar ao menu principal...\n')  # Cria uma pausa para o usuário interagir e retornar ao menu.

# Ponto de entrada do script
if __name__ == '__main__':  # Garante que a função main só vá ser executada quando este arquivo for o executado.
    main()
