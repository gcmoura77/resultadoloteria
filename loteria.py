import requests

# Documentação da API: https://conectalot.com.br/api/documentation#/Resultados%20Jogos/get_megasena

link = "https://conectalot.com.br/api/megasena"
# megasena = requests.get(link)

# # buscar a última mega-sena
# resultado = megasena.json() # transforma a resposta em um dicionário
# ultimo_concurso = resultado['id']

# atualiza com o resultado do último concurso
# dezenas = resultado['dezenas_sorteadas']
# dezenas.sort()

# ultimo_concurso
# resultado['data_apuracao']
# dezenas[0]
# dezenas[1]
# dezenas[2]
# dezenas[3]
# dezenas[4]
# dezenas[5]
# resultado['acumulado']
# resultado['f1_ganhadores']


# print(dezenas)

def get_ultimo_concurso():
    megasena = requests.get(link)

    # buscar a última mega-sena
    resultado = megasena.json() # transforma a resposta em um dicionário
    return resultado


