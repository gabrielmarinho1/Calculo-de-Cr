import csv

def calcular_cr(csv_reader): # Calcula o Cr
    soma_nota_creditos = 0
    soma_creditos = 0

    for line in csv_reader:
        creditos = int(line[1])
        nota = float(line[2])

        if nota is not None: # Desconsidera as cadeiras que ainda não têm nota
             soma_nota_creditos += nota * creditos
             soma_creditos += creditos

    if soma_creditos == 0: # Evita divisões por 0
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
                writer.writeheader()

            # Escreve a nova disciplina
            writer.writerow(disciplina)

def menu():
     while True:
        with open('notas.csv', 'r',) as csv_file: # Abre o arquivo CSV
         csv_reader = csv.reader(csv_file)

         next(csv_reader) # Pula a primeira linha que tem "cadeira, creditos, media_final"
         print("\nEscolha uma Opção")
         print("1 - Ver Disciplinas")
         print("2 - Cadastrar nova Disciplina")
         print("3 - Calcular CR")
         print("4 - Sair")
 
         opcao = input("Escolha uma opção: ")
 
         if opcao == '1':
             ver_disciplinas(csv_reader)
         elif opcao == '2':
             cadastrar_disciplina()
         elif opcao == '3':
             cr = calcular_cr(csv_reader)
             print(f"O Coeficiente de Rendimento (CR) é: {cr:.4f}")
         elif opcao == '4':
             break
         else:
             print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()