# 1. CRUD de Treinos e Competições: Pedro deve poder adicionar, visualizar,
# atualizar e excluir os registros de seus treinos e competições através de um menu
# interativo.
# 2. Cadastro de Treinos e Competições: O sistema deve permitir que Pedro registre
# informações sobre cada treino ou competição, incluindo data, distância percorrida,
# tempo, localização, e condições climáticas.
# 3. Filtragem por Distância ou Tempo: O sistema deve permitir que Pedro filtre
# seus treinos com base na distância percorrida ou no tempo, ajudando-o a analisar
# seu desempenho em diferentes distâncias.
# 4. Armazenamento de Dados: Todas as informações dos treinos e competições
# devem ser armazenadas em um banco de dados para que possam ser acessadas a
# qualquer momento (arquivo .txt ou .csv).
# 5. Metas e Desafios: O sistema deve permitir que Pedro defina metas pessoais
# (como correr 100 km por mês ou melhorar o tempo em 5 km), e o acompanhe no
# cumprimento dessas metas.
# 6. Sugestões de Treinos Aleatórios: O sistema deve sugerir treinos aleatórios, com
# base no histórico de Pedro, para que ele possa variar sua rotina e melhorar seu
# desempenho.
# 7. Funcionalidade Extra: Ter pelo menos uma outra funcionalidade a mais que não
# está descrita aqui neste documento. Sejam criativos e divirtam-se!




import os

def formatacao(variavel):
    return variavel.replace("/", "")


def limparTela():
    input("Digite qualquer tecla para voltar ao menu: ")
    os.system("cls")

treinos = {"Data":[], "DistanciaPercorrida":[], "Tempo":[], "Localizacao":[], "CondicoesClimaticas":[]}

os.system("cls")
while True:
    print("""
Digite 1 para adicionar um registro de treino e competição
Digite 2 para visualizar um registro de treino e competição
Digite 3 para atualizar um registro de treino e competição
Digite 4 para excluir um registro de treino e competição
Digite 6 para vê sugestões de treinos aleatorios
Digite 0 para encerrar o programa""")
    opcao = int(input("Digite sua opção: "))

    match opcao:
        case 0:
            print("Saindo...")
            break
        
        case 1:
            data = input("Digite a data do seu treino/competição (DD/MM/YYYY): ") # LEMBRAR DA TRATAÇÃO DO USUARIO EX: DATA > 10
            treinos["Data"] = data
            distanciaPercorrida = float(input("Digite a distancia percorrida (KM): "))
            treinos["DistanciaPercorrida"] = distanciaPercorrida
            tempo = int(input("Digite o tempo em minutos que você levou para concluir esse treino/competição: "))
            treinos["Tempo"] = tempo
            localizacao = input("Digite a localizacao do seu treino/competição: ")
            treinos["Localizacao"] = localizacao
            condicoesClimaticas = input("Digite as condições climaticas na hora do treino/competição: ")
            treinos["CondicoesClimaticas"] = condicoesClimaticas

            # data = data.replace("/", "")
            dataFormatada = formatacao(data)
            with open(f"Treino{dataFormatada}.txt", "w", encoding="utf-8") as file:
                file.write(f"""Data: {data}
Distancia percorrida: {distanciaPercorrida}km
Tempo: {tempo}min
Localização: {localizacao}
Condições climaticas: {condicoesClimaticas}
""")
                file.close()
            
            limparTela()

        case 2:
            #Filtragem por Distância ou Tempo: O sistema deve permitir que Pedro filtre
            # seus treinos com base na distância percorrida ou no tempo, ajudando-o a analisar
            # seu desempenho em diferentes distâncias.
            os.system("cls")
            filtro = input("Você deseja filtrar na hora da visualização de seus treinos (Sim/Nao)? ").lower()

            arquivosTreinos = []
            for arquivo in os.listdir("."):
                if arquivo.startswith("Treino") and arquivo.endswith(".txt"): #and os.path.isfile(arquivo):
                    arquivosTreinos.append(arquivo)

            if filtro == "nao" or filtro == "não":
                for arquivo in arquivosTreinos:
                    with open(arquivo, "r", encoding="utf-8") as file:
                        print(f"\nArquivo: {arquivo}")
                        print(file.read())
                        print("-" * 30)
                        file.close()

                # for data, distancia, tempo, localizacao, clima in zip(treinos["Data"], str(treinos["DistanciaPercorrida"]), str(treinos["Tempo"]), 
                #                                                       treinos["Localizacao"], treinos["CondicoesClimaticas"]):
                #     print(f"Data: {data}")
                #     print(f"DistanciaPercorrida: {distancia}km")
                #     print(f"Tempo: {tempo}min")
                #     print(f"Localizacao: {localizacao}")
                #     print(f"CondicoesClimaticas: {clima}")
                #     print("-" * 30)
            
            elif filtro == "sim":
                criterio = int(input("Você deseja filtrar por distancia ou tempo? Digite 1 ou 2, respectivamente: "))
                
                if criterio == 1:
                    distanciaFiltro = float(input("Digite a distancia mínima para filtrar (em km): "))

                    for arquivo in arquivosTreinos:
                        with open(arquivo, "r", encoding="utf-8") as file:
                            conteudo = file.read()
                            if "Distancia percorrida:" in conteudo:
                                distanciaStr = conteudo[conteudo.index("Distancia percorrida:"):]
                                distanciaStr = distanciaStr.split(":")[1].strip()
                                distanciaStr = distanciaStr.split()[0]
                                distancia = float(distanciaStr.replace("km", "").strip())
                                
                            if distancia >= distanciaFiltro:
                                print(f"\nArquivo: {arquivo}") 
                                print(conteudo)
                                print("-" * 30)
                                file.close()   

                elif criterio == 2:
                    tempoFiltro = int(input("Digite a o tempo mínimo para filtrar (em min): "))

                    for arquivo in arquivosTreinos:
                        with open(arquivo, "r", encoding="utf-8") as file:
                            conteudo = file.read()
                            if "Tempo:" in conteudo:
                                tempoStr = conteudo[conteudo.index("Tempo:"):]
                                tempoStr = tempoStr.split(":")[1].strip()
                                tempoStr = tempoStr.split()[0]
                                tempoExibir = int(tempoStr.replace("min", "").strip())
                                
                            if tempoExibir >= tempoFiltro:
                                print(f"\nArquivo: {arquivo}") 
                                print(conteudo)
                                print("-" * 30)
                                file.close()   

                else:
                    print("Opção invalida, por favor digite novamente!!")
                
            limparTela()

        case 3:
            os.system("cls")
            dataArquivo = input("Digite a data do treino que você deseja alterar: ")

            dataArquivo = formatacao(dataArquivo)
            nomeArquivo = f"Treino{dataArquivo}.txt"
            if os.path.isfile(nomeArquivo):

                print("""
Digite 1 para alterar a data
Digite 2 para alterar a distancia percorrida
Digite 3 para alterar o tempo
Digite 4 para alterar a localização
Digite 5 para alterar as condições climaticas""")
                opcaoUpdate = int(input("Digite a opção que você deseja alterar: "))

                with open(nomeArquivo, "r", encoding="utf-8") as file:
                    conteudo = file.readlines()

                match opcaoUpdate:
                    case 1:
                        novaData = input("Digite a nova data: ")

                        # novaDataFormatada = formatacao(novaData)
                        for i in range(len(conteudo)):
                            if "Data: " in conteudo[i]:
                                conteudo[i] = f"Data: {novaData}\n"

                    case 2: 
                        novaDistanciaPercorrida = float(input("Digite a nova distancia percorrida: "))
                        
                        for i in range(len(conteudo)):
                            if "Distancia percorrida: " in conteudo[i]:
                                conteudo[i] = f"Distancia percorrida: {novaDistanciaPercorrida}km\n"                      

                    case 3: 
                        novoTempo = int(input("Digite o novo tempo: "))

                        for i in range(len(conteudo)):
                            if "Tempo: " in conteudo[i]:
                                conteudo[i] = f"Tempo: {novoTempo}min\n"
                    
                    case 4:
                        novaLocalizacao = input("Digite a nova localização: ")
                        
                        for i in range(len(conteudo)):
                            if "Localização: " in conteudo[i]:
                                conteudo[i] = f"Localização: {novaLocalizacao}\n"

                    
                    case 5:
                        novaCondicaoClimatica = input("Digite uma nova condição climatica: ")
                        
                        for i in range(len(conteudo)):
                            if "Condições climaticas: " in conteudo[i]:
                                conteudo[i] = f"Condições climaticas: {novaCondicaoClimatica}\n"
                

                with open(nomeArquivo, "w", encoding="utf-8") as file:
                    file.writelines(conteudo)

                if opcaoUpdate == 1:
                    os.rename(nomeArquivo, f"Treino{formatacao(novaData)}.txt")

                print("Alteração realizada com sucesso!")
            
            else:
                print("Arquivo não localizado, por favor tente novamente")
        
            limparTela()

        case 4:
            os.system("cls")
            dataNomeArquivo = input("Digite a data do treino que você deseja excluir: ")

            dataNomeArquivo = formatacao(dataNomeArquivo)
            if os.path.exists(f"Treino{dataNomeArquivo}.txt"):
                os.remove(f"Treino{dataNomeArquivo}.txt")
                print("Arquivo excluido com sucesso!")
            else:
                print("Arquivo não encontrado! por favor tente novamente")
            
            limparTela()
        
        
        case 6:
            os.system("cls")
            
            listaAleatorios = []
            
            caminhoDaPasta = "treinosAleatorios"
            for arquivo in os.listdir(caminhoDaPasta):
                if arquivo.startswith("treinoAleatorio") and arquivo.endswith(".txt"): #and os.path.isfile(arquivo):
                    listaAleatorios.append(arquivo)
            
            for treinosAleatorios in listaAleatorios:
                caminhoArquivo = os.path.join(caminhoDaPasta, treinosAleatorios) #caminhoDaPasta + "/" + treinoAleatorio
                with open(caminhoArquivo, "r", encoding="UTF-8") as file:
                    print(f"\nArquivo: {treinosAleatorios}")
                    print(file.read())
                    print("-" * 30)
                    file.close() 
            
            while True:
                print("Você fez algum dos treinos aleatorios?")
                fazer = int(input("Se sim, digite o número de 1 a 5 para marcar como feito, se nao, digite 0: "))
                
                if 1 <= fazer <= 5:
                    treinoFeito = "treinoAleatorio" + str(fazer) + ".txt"
                    arquivoCaminho = os.path.join(caminhoDaPasta, treinoFeito)
                    
                    with open(arquivoCaminho, "r", encoding="UTF-8") as file:
                        conteudo = file.readlines()
                        
                        for i in range(len(conteudo)):
                            if "Status: " in conteudo[i]:
                                conteudo[i] = f"Status: feito✔️\n"
                    
                        file.close()
                    
                    with open(arquivoCaminho, "w", encoding="UTF-8") as file:
                        file.writelines(conteudo)
                        file.close()
                    
                    print(f"{treinoFeito} foi atualizado como feito!!")
                    
                    
                    break
                elif fazer == 0:
                    break
                else:
                    print("Opção incorreta, por favor digite novamente!")
            
            limparTela()
            
        case _:
            print("Opção invalido, por favor digite novamente!")