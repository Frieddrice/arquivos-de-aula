#Aqui, o algoritmo entende que os números devem ser repetidos um por um
lista = [1,2,3,4,5]
for x in lista:
    print(x)

#Aqui, o algoritmo entende que as letras devem ser repetidas uma por uma
nome = "Melyssa" 
for letras in nome:
    print(letras)

#Range(inicio,fim) ----> Contador nativo
for x in range(5):
    print(x)

#While ----> Sempre executará a função enquanto for verdadeira
opcao = "Sophia"
for x in range(3) :
    print("Menu de opções")
    print("1- Repete: olá")
    print("2 - Repete: tudo bem")
    print("3 - Encerra")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        print("Olá")
    elif opcao == 2:#Elif (Else if) ----> "Senão se"
        print("tudo bem")
    elif opcao == 3:
        print("Encerrando o programa")
        break
    else:
        print("Opção inválida") 
        

    #Condicionais da repetição:
    #Break - encerrar repetição
    #continue - continuar
    #else - limita a repetição

    #(Se a repetição precisa executar várias vezes e ela só irá parar em um valor específico, utilizamos o while opcao (menor ou maior) variável)
    #(While é utilizado quando eu quero que o meu programa repita várias vezes (enquanto a opção for verdadeira, ele continuará rodando, mas quando ela for falsa, irá encerrar o programa); enquanto for é utilizado quando eu tenho uma variável de repetição definida. Ex: Quero que o meu programa repita x vezes - utilizar o for)