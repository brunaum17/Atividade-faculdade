from Funcoes import *


while True:
    print("\nMenu:")
    print("1. Buscar na lista de 1 Milhão")
    print("2. Buscar na lista de 1 Bilhão")
    print("3. Buscar na lista de 1 Trilhão")
    print("4. Sair\n")

    escolha = input("Escolha uma opção (1-4): ")
    print("\n")

    if escolha == '1':

        resultado = procuraMI("1Milhao.txt",1000000)
        
        print("--"*16)
        print(f"Número {resultado['resultado_funcao']['numero_procurado']} {'encontrado' if resultado['resultado_funcao']['encontrado'] else 'não encontrado'}")
        print(f"Tempo total: {resultado['tempo_total']} segundos")
        print(f"Uso de CPU: {resultado['uso_cpu']}%")
        print(f"Uso de Memória: {resultado['uso_memoria']/ (1024 * 1024):.2f} MB")
        print("--"*16)

    elif escolha == '2':

        resultado = carregaBI("1Bilhao.txt",1000000000)
        print("--"*16)
        print(f"Número {resultado['resultado_funcao']['numero_procurado']} {'encontrado' if resultado['resultado_funcao']['encontrado'] else 'não encontrado'}")
        print(f"Tempo total: {resultado['tempo_total']} segundos")
        print(f"Uso de CPU: {resultado['uso_cpu']}%")
        print(f"Uso de Memória: {resultado['uso_memoria']/ (1024 * 1024):.2f} MB")
        print("--"*16)

    elif escolha == '3':

        resultado = carregaTRI("1Trilhao.txt",1000000000000 )
        print("--"*16)
        print(f"Número {resultado['resultado_funcao']['numero_procurado']} {'encontrado' if resultado['resultado_funcao']['encontrado'] else 'não encontrado'}")
        print(f"Tempo total: {resultado['tempo_total']} segundos")
        print(f"Uso de CPU: {resultado['uso_cpu']}%")
        print(f"Uso de Memória: {resultado['uso_memoria']/ (1024 * 1024):.2f} MB")
        print("--"*16)

    elif escolha == '4':

        print("Saindo...")
        break

    else:

        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

