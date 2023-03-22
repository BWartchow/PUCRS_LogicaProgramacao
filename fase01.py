# Escritório de Projeto - Lógica e Programação de Computadores
# Desenvolvido por Bê Wartchow

###############################################################################
#----------------------CÓDIGO DA FASE 01 D0 PROJETO ---------------------------

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


#-------------------------PROGRAMA PRINCIPAL ----------------------------------

while True:
#------------------------- MENU com Opções disponíveis ------------------------
    exibeMenu()
    try:
        opcao = input("\nQual sua escolha? ").strip()
        if opcao not in "1230":
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

    except Exception as erro:
        print(erro)
