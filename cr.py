import csv

def calcular_cr(csv_reader):  # Calcula o CR
    soma_nota_creditos = 0
    soma_creditos = 0

    for line in csv_reader:
        creditos = int(line[1])
        nota = float(line[2])

        if nota is not None:  # Desconsidera as cadeiras que ainda não têm nota
            soma_nota_creditos += nota * creditos
            soma_creditos += creditos

    if soma_creditos == 0:  # Evita divisões por 0
        return 0

    cr = soma_nota_creditos / soma_creditos

    return cr

def ver_disciplinas(csv_reader):
    print("\nDisciplinas Cadastradas:")
    for disciplina in csv_reader:
        print(f"{disciplina[0]} - Créditos: {disciplina[1]}, Média Final: {disciplina[2]}")

def cadastrar_disciplina():
    nome = input("Digite o nome da disciplina: ")
    creditos = int(input("Digite a quantidade de créditos da disciplina: "))
    media_final = float(input("Digite a média final da disciplina: "))

    disciplina = [nome, creditos, media_final]

    with open('notas.csv', mode='a', newline='\n') as file:
        writer = csv.writer(file)

        # Se o arquivo estiver vazio, escreve o cabeçalho
        if file.tell() == 0:
            writer.writerow(['Disciplina', 'Créditos', 'Média Final'])

        # Escreve a nova disciplina
        writer.writerow(disciplina)

def pesquisar_disciplina(nome):
    nome = nome.lower()
    with open('notas.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        for row in reader:
            if row[0].lower() == nome:
                print(f"\nDisciplina encontrada: {row[0]} - Créditos: {row[1]}, Média Final: {row[2]}")
                return
        print("\nDisciplina não encontrada.")


def remover_disciplina(nome):
    linhas = []
    with open('notas.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        for row in reader:
            if row[0].lower() != nome.lower():
                linhas.append(row)

    with open('notas.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(['Disciplina', 'Créditos', 'Média Final'])
        writer.writerows(linhas)

    print("\nDisciplina removida com sucesso.")

def editar_disciplina(nome):
    linhas = []
    disciplina_encontrada = False
    with open('notas.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        for row in reader:
            if row[0].lower() == nome.lower():
                disciplina_encontrada = True
                novo_nome = input("Digite o novo nome da disciplina: ")
                novos_creditos = int(input("Digite a nova quantidade de créditos: "))
                nova_media_final = float(input("Digite a nova média final: "))
                linhas.append([novo_nome, novos_creditos, nova_media_final])
            else:
                linhas.append(row)

    if not disciplina_encontrada:
        print("\nDisciplina não encontrada.")
        return

    with open('notas.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(['Disciplina', 'Créditos', 'Média Final'])
        writer.writerows(linhas)

    print("\nDisciplina editada com sucesso.")

def menu():
    while True:
        print("\nEscolha uma Opção")
        print("1 - Ver Disciplinas")
        print("2 - Cadastrar nova Disciplina")
        print("3 - Calcular CR")
        print("4 - Pesquisar Disciplina")
        print("5 - Remover Disciplina")
        print("6 - Editar Disciplina")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            with open('notas.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Pula o cabeçalho
                ver_disciplinas(csv_reader)
        elif opcao == '2':
            cadastrar_disciplina()
        elif opcao == '3':
            with open('notas.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Pula o cabeçalho
                cr = calcular_cr(csv_reader)
                print(f"O Coeficiente de Rendimento (CR) é: {cr:.4f}")
        elif opcao == '4':
            nome = input("Digite o nome da disciplina a ser pesquisada: ")
            pesquisar_disciplina(nome)
        elif opcao == '5':
            nome = input("Digite o nome da disciplina a ser removida: ")
            remover_disciplina(nome)
        elif opcao == '6':
            nome = input("Digite o nome da disciplina a ser editada: ")
            editar_disciplina(nome)
        elif opcao == '7':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
