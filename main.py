# Escritório de Projeto - Lógica e Programação de Computadores
# Desenvolvido por Bê Wartchow

###############################################################################
#------------------- CÓDIGOS DAS FASES 01 E 02 D0 PROJETO ---------------------

import statistics
import matplotlib.pyplot as plt

data = "" # inicializa data como string vazia

#--------------------------- Funções gerais: ----------------------------------
def carregaDados(nome):
    """Carrega os dados de um arquivo em uma lista"""
    dados = []
    arq = open(nome, 'r', encoding='utf-8')
    for linha in arq:
        linha1 = linha[:-1] # retira o \n
        dados.append(linha1)
    arq.close()
    return dados


def listaSemCabecalho(lista):
    """Exibe os dados em uma lista de listas, sem cabeçalho"""
    nova = []
    indice = 1
    while indice < len(lista):
        nova.append(lista[indice].split(';'))
        indice += 1
    return nova


def gravaArquivo(conteudo):
    """Grava os dados em lista em um arquivo txt"""
    lista = list(conteudo)
    arq = open('listaDeDados.txt', "w")
    nova = []
    indice = 0
    while indice < len(lista):
        nova.append(lista[indice].split(';'))
        indice += 1
    arq.write(str(nova))
    print(nova) # exibe no console o que foi gerado
    arq.close()


#-------------------------- CABEÇALHO DO PROGRAMA -----------------------------
def exibeMenu():
    """Exibe menu com opções disponíveis"""
    txt = "Informações climáticas de Porto Alegre, entre os anos 1961 e 2016."
    print("\n")
    print("*"*100)
    print(f"{txt:^100}")
    print("*"*100)
    b = "" # para alinhamento do texto nos prints
    print(f"{b:>7}","\nOpções de dados para visualização:")
    print(f"{b:>10}","[1] - GRAVAR DADOS - gravar todos os dados em arquivo txt")
    print(f"{b:>10}","[2] - PRECIPITAÇÃO - exibir volume de chuva em mm por m²")
    print(f"{b:>10}","[3] - TEMPERATURA - exibir amostra da temperatura em ºC")
    print(f"{b:>10}","[4] - ANÁLISE DE DADOS - exibir breve análise de dados")
    print(f"{b:>10}","[0] - SAIR DO PROGRAMA")


#----------------------- Funções precipitação:---------------------------------
def exibeAmostraPrecip(lista):
    """Exibe a amostra de precipitação do período solicitado pelo usuário"""
    amostra = []
    for item in lista:
        if data in item[0]:
            amostra.append(item[0:2])
    if len(amostra) == 0:
        return print(f'Dados em {data}: Não há dados para o período informado')
    else:
        return print(f'Dados em {data}: ', amostra)


def exibeCabecalhoPrecip(arquivo):
    """Gera o cabeçalho da precipitação"""
    dados = carregaDados(arquivo)
    cabecalho = dados[0]
    exibe = []
    coluna = cabecalho.split(';')
    exibe.append(str(coluna[0])) # data
    exibe.append(str(coluna[1])) # precip
    return print('Legenda: ', exibe)


#----------------------- Funções temperatura:----------------------------------
def exibeAmostraTemp(lista, ano):
    """Exibe temperatura máxima dentre 7 dias dos meses do ano solicitado"""
    amostra = []
    maior = 0
    meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",]
    for mes in meses:
        data = f"/{mes}/{ano}"
        total = 0
        for item in lista:
            if data in item[0]:
                amostra.append(item[0]) # data
                amostra.append(float(item[2])) # temp max
                if float(item[2]) > maior:
                    maior = float(item[2])
                total += 1
                if total == 7:
                    print(f'07 primeiros dias do mês {mes}: ', amostra,
                    f'\n A maior temperatura foi {maior}ºC \n')
                    maior = 0
                    amostra = []
                    break


def exibeCabecalhoTemp(arquivo):
    """Gera o cabeçalho da temperatura"""
    dados = carregaDados(arquivo)
    cabecalho = dados[0]
    exibe = []
    coluna = cabecalho.split(';')
    exibe.append(str(coluna[0])) # data
    exibe.append(str(coluna[2])) # temp max
    # exibe.append(str(coluna[3])) # temp min
    return print('Legenda: ', exibe)


#---------------------------- Novas Funções -----------------------------------

#---------------------- Função Principal - Dicionário -------------------------

def geraListaDeDicionarios(lista):
    """Converte dados pra lista de dicionários"""
    mega_lista = []
    decada = 0
    for item in lista:
        if int(item[0][6:10]) < (1971):
            decada = 1960
        elif int(item[0][6:10]) < (1981):
            decada = 1970
        elif int(item[0][6:10]) < (1991):
            decada = 1980
        elif int(item[0][6:10]) < (2001):
            decada = 1990
        elif int(item[0][6:10]) < (2011):
            decada = 2000
        elif int(item[0][6:10]) < (2021):
            decada = 2010
        mega_lista.append({
            "decada": decada,
             "ano": int(item[0][6:10]),
             "mes": int(item[0][3:5]),
             "dia": int(item[0][0:2]),
             "precip": float(item[1]),
             "maxima": float(item[2]),
             "minima": float(item[3]),
             "horas_insol": float(item[4]),
             "temp_media": float(item[5]),
             "um_relativa": float(item[6]),
             "vel_vento": float(item[7])
             })
    return mega_lista


#------------------------ Funções Precipitação por Década ---------------------

def chuva_decada(lista, decada):
    """Retorna a média de chuvas por ano de cada década"""
    soma = 0
    for item in lista:
        if item["decada"] == decada:
            soma += item["precip"]
    if decada == 2010: # os dados vão até metade do ano de 2016
        media = soma/5.5
    else:
        media = soma/10 # obtém média por ano de década inteira
    return media


def decadaMaisChuvosa():
    """Compara as décadas e retorna a mais chuvosa"""
    precipitacao = []
    decadas = ["1960", "1970", "1980", "1990", "2000", "2010"]
    dados = carregaDados('dados.csv')
    chuvaDecada = listaSemCabecalho(dados)
    chuva = geraListaDeDicionarios(chuvaDecada)
    chuva1960 = chuva_decada(chuva, 1960)
    chuva1970 = chuva_decada(chuva, 1970)
    chuva1980 = chuva_decada(chuva, 1980)
    chuva1990 = chuva_decada(chuva, 1990)
    chuva2000 = chuva_decada(chuva, 2000)
    chuva2010 = chuva_decada(chuva, 2010)
    precipitacao.append(chuva1960)
    precipitacao.append(chuva1970)
    precipitacao.append(chuva1980)
    precipitacao.append(chuva1990)
    precipitacao.append(chuva2000)
    precipitacao.append(chuva2010)
    print("A precipitação acumulada nas décadas ", decadas, " é, respectivamente: \n", precipitacao, "\n")
    plt.title("Precipitação (mm/m²) acumulada por década") # título do gráfico
    plt.bar(decadas, precipitacao) # plota o gráfico de barras
    plt.show() # exibe o gráfico
    for i in range(0,len(precipitacao)-1): # Vai ordenar as listas
        for j in range(0,len(precipitacao)-1-i):
            if precipitacao[j]<precipitacao[j+1]:  #decrescente
                aux = precipitacao[j]
                precipitacao[j] = precipitacao[j+1]
                precipitacao[j+1] = aux
                aux = decadas[j]
                decadas[j] = decadas[j+1]
                decadas[j+1] = aux
    print("A década que possui maior média de chuva acumulada por ano é: ")
    print(decadas[0], " com ", precipitacao[0], " milímetros por m² de chuva")


#------------------------ Funções Análises Mês de Agosto ----------------------

def dadosTempAgosto(ano):
    """Retorna média e moda da temperatura mínima do mês de agosto"""
    dados = carregaDados('dados.csv')
    amostra = listaSemCabecalho(dados)
    agostos = geraListaDeDicionarios(amostra)
    temperatura = 0
    dias = 0
    minimas = []
    for item in agostos:
        if item["ano"] == ano:
            if item["mes"] == 8: # agosto
                temperatura += item["minima"]
                dias += 1
                minimas.append(item["minima"])
    moda = statistics.mode(minimas) # verifica a moda
    media = temperatura/dias # calcula a média
    #print(minimas)
    print(f"A média das temperaturas mínimas em agosto de {ano} é {media} °C e a moda é {moda} °C")


def dadosVentoAgosto(ano):
    """Retorna média e moda da velocidade do vento do mês de agosto"""
    dados = carregaDados('dados.csv')
    amostra = listaSemCabecalho(dados)
    agostos = geraListaDeDicionarios(amostra)
    vento = 0
    dias = 0
    velocidadeVento = []
    for item in agostos:
        if item["ano"] == ano:
            if item["mes"] == 8: # agosro
                vento += item["vel_vento"]
                dias += 1
                velocidadeVento.append(item["vel_vento"])
    moda = statistics.mode(velocidadeVento) # verifica a moda
    media = vento/dias # calcula a média
    #print(velocidadeVento)
    print(f"A média da velocidade do vento em agosto de {ano} é {media} m/s e a moda é {moda} m/s")


def dadosUmidadeAgosto(ano):
    """Retorna média e moda da umidade relativa do ar do mês de agosto"""
    dados = carregaDados('dados.csv')
    amostra = listaSemCabecalho(dados)
    agostos = geraListaDeDicionarios(amostra)
    umid = 0
    dias = 0
    umidadeRelativa = []
    for item in agostos:
        if item["ano"] == ano:
            if item["mes"] == 8: # agosto
                umid += item["um_relativa"]
                dias += 1
                umidadeRelativa.append(item["um_relativa"])
    moda = statistics.mode(umidadeRelativa) # verifica a moda
    media = umid/dias # calcula a média
    #print(velocidadeVento)
    print(f"A média da umidade relativa do ar em agosto de {ano} é {media} % e a moda é {moda} %")


def exibeDadosAgostos():
    """Exibe análise de temperatura, vento e umidade de agostos 2006 a 2016"""
    for ano in range(2006,2016): # exibe até 2015
        dadosTempAgosto(ano)
        dadosUmidadeAgosto(ano)
        dadosVentoAgosto(ano)
        print("\n")
    print("Sem dados para o mês de agosto de 2016")

#------------------------ Funções Precipitação por Mês ------------------------

def chuva_mes(lista, mes, ano):
    """Retorna o acumulado de chuvas por mês de cada ano"""
    soma = 0
    for item in lista:
        if item["ano"] == ano:
            if item["mes"] == mes:
                soma += item["precip"]
    return soma


def mesMaisChuvoso():
    """Compara os meses e retorna o mais chuvoso"""
    precipitacao = []
    meses = []
    dados = carregaDados('dados.csv')
    dadosChuva = listaSemCabecalho(dados)
    chuva = geraListaDeDicionarios(dadosChuva)
    for ano in range(1961,2017): # até 2016
        for mes in range(1,13): # até dezembro
            chuvaMes = chuva_mes(chuva, mes, ano)
            precipitacao.append(chuvaMes)
            meses.append((mes,ano))
    for mes in range(1,8): # até julho, mês máximo dos dados de 2017
        chuva2017 = chuva_mes(chuva, mes, 2017) # ano com dados faltantes
        precipitacao.append(chuva2017)
        meses.append((mes, 2017))
    #print(meses)
    #print(precipitacao)
    for i in range(0,len(precipitacao)-1): # Vai ordenar as listas
        for j in range(0,len(precipitacao)-1-i):
            if precipitacao[j]<precipitacao[j+1]:  #decrescente
                aux = precipitacao[j]
                precipitacao[j] = precipitacao[j+1]
                precipitacao[j+1] = aux
                aux = meses[j]
                meses[j] = meses[j+1]
                meses[j+1] = aux
    print("O mês que possui maior valor acumulado de chuva é: ")
    print(meses[0], " com ", precipitacao[0], " milímetros por m² de chuva")



#-------------------------PROGRAMA PRINCIPAL ----------------------------------

while True:
#------------------------- MENU com Opções disponíveis ------------------------
    exibeMenu()
    try:
        opcao = input("\nQual sua escolha? ").strip()
        if opcao not in "12340":
            msg = "Informe uma opção válida\n"
            raise Exception(msg)
        else:
#-------------------------- Opção 0 - Sair do Programa ------------------------
            if opcao == "0":
                print('\n Programa encerrado!!')
                break

#-------------------------- Opção 1 - Gravar os dados -------------------------
# Esta opção também exibe em tela a lista de listas gerada com todos os dados,
# porém são muitos dados para serem impressos no console. Por isso o .txt
            if opcao == "1":
                try:
                    dados = carregaDados('dados.csv')
                    gravaArquivo(dados)
                    print("-"*70)
                    print('>'*10, 'Dados gravados com sucesso\n')
                except FileNotFoundError:
                        print('Arquivo base para exibição de dados não encontrado\n')

#-------------------------- Opção 2 - PRECIPITAÇÃO ----------------------------
            if opcao == "2":
                print("-"*70)
                print('>'*10, 'PRECIPITAÇÃO - volume de chuva em mm por m²\n')
                while True:
                    try:
                        ano_precip = input("Informe o ano (AAAA) desejado para visualização: ")
                        if not ano_precip.isnumeric():
                            msg = "Informe um ano válido"
                            raise Exception(msg)
                        else:
                            if len(ano_precip) != 4:
                                msg = "Necessário 4 números (AAAA)"
                                raise Exception(msg)
                            elif int(ano_precip) < 1961 or int(ano_precip) > 2016:
                                msg = "Escolha um ano entre 1961 e 2016"
                                raise Exception(msg)
                            else:
                                break
                    except Exception as erro:
                        print(erro)
                while True:
                    try:
                        mes_precip = input(f"Informe o mês (MM) desejado em {ano_precip}: ")
                        if not mes_precip.isnumeric():
                            msg = "Informe um mês válido"
                            raise Exception(msg)
                        else:
                            if len(mes_precip) != 2:
                                msg = "Necessário 2 números (MM)"
                                raise Exception(msg)
                            elif int(mes_precip) > 12 or int(mes_precip[1]) < 1:
                                msg = "Informe um mês válido"
                                raise Exception(msg)
                            else:
                                break
                    except Exception as erro:
                        print(erro)
                data = f"{mes_precip}/{ano_precip}"
                try:
                    dados = carregaDados('dados.csv')
                    resultadoPrecip = listaSemCabecalho(dados)
                    print('-'*70)
                    print('\nEXIBINDO PRECIPITAÇÃO (mm/m²) PARA O PERÍODO ESCOLHIDO:')
                    exibeCabecalhoPrecip('dados.csv')
                    exibeAmostraPrecip(resultadoPrecip)
                except FileNotFoundError:
                        print('\nArquivo base para exibição de dados não encontrado')

#------------------------- Opção 3 - TEMPERATURA ------------------------------
            if opcao == "3":
                print("-"*70)
                print('>'*10, 'TEMPERATURA - em graus celsius')
                while True:
                    try:
                        ano_temp = input("Informe o ano (AAAA) desejado para visualização: ")
                        if not ano_temp.isnumeric():
                            msg = "Informe um ano válido"
                            raise Exception(msg)
                        else:
                            if len(ano_temp) != 4:
                                msg = "Necessário 4 números (AAAA)"
                                raise Exception(msg)
                            elif int(ano_temp) < 1961 or int(ano_temp) > 2016:
                                msg = "Escolha um ano entre 1961 e 2016"
                                raise Exception(msg)
                            else:
                                break
                    except Exception as erro:
                        print(erro)
                try:
                    dados = carregaDados('dados.csv')
                    resultadoTemp = listaSemCabecalho(dados)
                    print('-'*70)
                    print('\nEXIBINDO AMOSTRA DE TEMPERATURA (°C) PARA O ANO ESCOLHIDO:')
                    exibeCabecalhoTemp('dados.csv')
                    exibeAmostraTemp(resultadoTemp, ano_temp)
                except FileNotFoundError:
                        print('\nArquivo base para exibição de dados não encontrado')

#------------------------- Opção 4 - DADOS FASE 02 ----------------------------
#-------------------------- Exibe análise de Dados ----------------------------
            if opcao == "4":
                try:
                    print('-'*100)
                    print('\nEXIBINDO PRECIPITAÇÃO (mm/m²) ACUMULADA POR DÉCADA:\n')
                    decadaMaisChuvosa()
                    print('-'*100)
                    print('\nEXIBINDO MAIOR PRECIPITAÇÃO (mm/m²) ACUMULADA POR MÊS:\n')
                    mesMaisChuvoso()
                    print('-'*100)
                    print('\nEXIBINDO DADOS DO MÊS DE AGOSTO - INVERNO - DE 2006 A 2016:\n')
                    exibeDadosAgostos()
                except FileNotFoundError:
                        print('\nArquivo base para exibição de dados não encontrado')


    except Exception as erro:
        print(erro)
