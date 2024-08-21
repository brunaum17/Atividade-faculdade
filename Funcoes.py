import random
import time
#Primeiro copiar o codigo a baixo e colar no CMD para instalar a biblioteca psutil
#pip install psutil
import psutil

def medir_performance(func):
    def wrapper(*args, **kwargs):
        processo = psutil.Process()

        uso_inicial_cpu = processo.cpu_percent(interval=None)
        uso_inicial_memoria = processo.memory_info().rss

        inicio_tempo = time.time()
        resultado = func(*args, **kwargs)
        fim_tempo = time.time()

        tempo_total = fim_tempo - inicio_tempo
        uso_final_cpu = processo.cpu_percent(interval=None)
        uso_final_memoria = processo.memory_info().rss

        uso_cpu = uso_final_cpu - uso_inicial_cpu
        uso_memoria = uso_final_memoria - uso_inicial_memoria

        return {
            "resultado_funcao": resultado,
            "tempo_total": round(tempo_total, 2),
            "uso_cpu": uso_cpu,
            "uso_memoria": uso_memoria
        }

    return wrapper

@medir_performance
def procuraMI(NomeArquivo,numero):

    carregaMI(NomeArquivo,numero)
    numero_procurado = random.randint(1, numero)  # Escolhe um número aleatório para procurar
    resultado = busca_numero_aleatorio(NomeArquivo, numero_procurado)
    
    resultado['numero_procurado'] = numero_procurado
    
    return resultado



@medir_performance
def carregaMI(NomeArquivo,numero):  
    arquivo = open(NomeArquivo, 'w')
    for i in range(1000000):
        numero_aleatorio = random.randint(1, numero) 
        arquivo.write(f"{numero_aleatorio}\n")
    arquivo.close()

@medir_performance
def carregaBI(NomeArquivo,numero):
    numero_procurado = random.randint(1, numero)  # Escolhe um número aleatório para procurar
    for i in range(1000):
        carregaMI(NomeArquivo,numero)
        resultado = busca_numero_aleatorio(NomeArquivo, numero_procurado)
        if resultado['encontrado']:
            return resultado

    return resultado

@medir_performance
def carregaTRI(NomeArquivo,numero):
    numero_procurado = random.randint(1, numero)  # Escolhe um número aleatório para procurar
    for i in range(1000000):
        carregaMI(NomeArquivo,numero)
        resultado = busca_numero_aleatorio(NomeArquivo, numero_procurado)
        if resultado['encontrado']:
            return resultado

    return resultado


def busca_numero_aleatorio(arquivo_nome, numero_procurado):
    encontrado = False
    with open(arquivo_nome, 'r') as arquivo:
        for linha in arquivo:
            if int(linha.strip()) == numero_procurado:
                encontrado = True
                break

    return {"encontrado": encontrado, "numero_procurado": numero_procurado}