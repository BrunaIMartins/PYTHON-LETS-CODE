
######################AULA 03##################################

from PIL import Image
from IPython.display import display
import datetime as dt
import requests as r
import requests as r  # r é só o apelido
import requests
import csv  # importar biblioteca
import csv
print("hello world")
x = 5
print(x)  # vai printar a variável
print(type(x))  # class int significa inteiro

preço = 19.99  # variavel
print(preço, type(preço))  # class float significa decimal
cidade = "são paulo"
print(cidade, type(cidade))  # class str significa string
disponivel = True  # variavel do tipo booleana
print(disponivel)
print(disponivel, type(disponivel))  # booleano, true ou false


######################AULA 04##################################

x = 50
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)  # exponencial
print(x//y)  # divisão inteira, output nunca vai ser decimal
print(x % y)  # resto, o output vai ser o resto da divisão

tem_cafe = True  # booleano
tem_pao = False
print(not tem_cafe)  # o not faz o booleano inverter. No caso, o cafe vira false
# o resultado é sempre verdadeiro, a nao ser que ambos sejam falsos.
print(tem_cafe or tem_pao)
print(tem_cafe and tem_pao)  # só retorna verdadeiro se ambas forem verdadeiros

# operadores relacionais
dolar = 5.3
real = 1
print(dolar > real)  # maior
print(dolar < real)  # menor
print(dolar == real)  # igual
print(dolar <= real)  # menor ou igual
print(dolar >= real)  # maior ou igual
print(dolar != real)  # diferente


######################AULA 05##################################

input  # função de entrada permite que o usuário possa interagir, retorna o que ele usar
print  # é uma função de output, ou seja, saída
type  # descobre o tipo do valor que armazenado em uma variável
idade = input("Informe a sua idade:")
print(idade, type(idade))
# ao colocar um numero, irá sair uma string. se for necessário fazer uma operação com o
# valor que saiu como string, é necessário realizar um casting, que muda o tipo
idade = int(idade)
print(idade, type(idade))
# casting só funciona se o valor for passível de converter

print(float("123.25"))
print(str("123.25"))
print(bool(""))
print(bool("abc"))
print(bool(0))  # só esse vai retornar false
print(bool(-2))

salario_mensal = input("Digite o valor do seu salário mensal")
salario_mensal = float(salario_mensal)
gasto_mensal = input("Digite o valor médio do seu gasto mensal")
gasto_mensal = float(gasto_mensal)
salario_total = salario_mensal*12
gasto_total = gasto_mensal * 12
montante_economizado = salario_total - gasto_total
print("O montante economizado ao fim do ano é de", montante_economizado)


######################AULA 06##################################

valor_passagem = 4.30
valor_corrida = input('Qual o valor da corrida?')
# o espaço é a indentação, ela vai "blocar" os códigos
if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
if float(valor_corrida) > valor_passagem * 5:
    print("Pegue o ônibus")
# ou
valor_passagem = 4.30
valor_corrida = input('Qual o valor da corrida?')
# o espaço é a indentação, ela vai "blocar" os códigos
if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
# else é como um "se não", ele substitui toda a linha  #if float(valor_corrida) > valor_passagem * 5:
else:
    print("Pegue o ônibus")

valor_passagem = 4.30
valor_corrida = input('Qual o valor da corrida?')
# o espaço é a indentação, ela vai "blocar" os códigos
if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
else:
    if float(valor_corrida) <= valor_passagem * 6:
        print("Aguarde, o valor da corrida pode abaixar")
    else:
        print("Pegue o ônibus")

valor_passagem = 4.30
valor_corrida = input('Qual o valor da corrida?')
# o espaço é a indentação, ela vai "blocar" os códigos
if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
elif float(valor_corrida) <= valor_passagem * 6:  # elif substitui o else mais o if
    print("Aguarde, o valor da corrida pode abaixar")
else:
    print("Pegue o ônibus")


######################AULA 07##################################

# while, que significa enquanto. Uma tarefa que vai ser executada enquanto outra condição é verdadeira
 # sem o incremento, o contador é sempre zero e o cod não sai do lugar
contador = 0
while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, "item limpo")
    else:
        print(contador, "itens limpos")
print("fim da repetição do bloco while")


contador = 0
while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, "item limpo")
        else:
            print(contador, "itens limpos")
    else:
        break
print("fim da repetição do bloco while")

texto = input("digite a sua senha")
while texto != "letscode":
    texto = input("senha invalida")
    print("acesso permitido")

contador = 0
while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue
    print(contador, "itens limpos")
print("fim da repetição do bloco while")


######################AULA 08##################################

# listas e tuplas, estrutura de dados é a compilação de dados em uma variavel
# listas e tuplas juntam itens de diferentes classes
# lista é uma coleção ou sequencia ordenada de valores. a ordenação é feita por indexação com base zero,vai ser o tamanho menos 1

nomes_paises = ["Brasil", "Argentina", "China", "canada", "Japão"]
print(nomes_paises)
print("tamanho da lista", len(nomes_paises))  # len mostra o tamanho
print("país", nomes_paises[4])
print("país", nomes_paises[-1])
nomes_paises[4] = "colombia"
print("país:", nomes_paises[4])
print(nomes_paises)
# slicing, ou fatiamento, acessar mais de um item de uma vez

print(nomes_paises[1:3])
print(nomes_paises[1:-1])
print(nomes_paises[0:3])
print(nomes_paises[2:])  # assim vai até o fim da lista
print(nomes_paises[:3])
print(nomes_paises[:])
print(nomes_paises[::2])
print(nomes_paises[::-1])
print("Brasil" in nomes_paises)
print("canada" not in nomes_paises)
lista_capitais = []
lista_capitais.append("Brasília")
lista_capitais.append("Buenos aires")
lista_capitais.append("Pequim")
lista_capitais.append("Bogota")
print(lista_capitais)
lista_capitais.insert(2, "paris")
print(lista_capitais)
lista_capitais.remove("Buenos aires")
print(lista_capitais)
lista_capitais.pop(2)
print(lista_capitais)
removido = lista_capitais.pop(2)
# nas tuplas não da pra mudar os itens, mais rigida
print(lista_capitais, removido)

nomes_paises = "brasil", 'argentina', 'canada', 'japao'
print(nomes_paises, type(nomes_paises))
nome_estado = 'sao paulo',
print(nome_estado, type(nome_estado))
len(nomes_paises)
b, a, c, j = nomes_paises
print(b, c, j)
print(*nomes_paises)  # string


######################AULA 09##################################

empresa = "google"
print(empresa)
empresa = "let's code"  # se usar aspas simples nas duas,o python não reconhece
frase = " O prof Pietro dá let's code disse: 'hj a pizza é por minha conta'"
# nesse caso, usar o caractere de escape pra alterar o sentido padrão como um caractere é lido. é só usar contrabarra antes das aspas duplas
frase = " O prof Pietro dá let's code disse: \"hj a pizza é por minha conta\""
frase = " O prof Pietro dá let's code disse: \"hj a pizza é por minha conta\""
# strings possuem nós, podem ser acessados separadamente. Na tupla você acessa um elemento, na string você acessa um caractere
empresa = "google"
print(empresa[0])  # o slicing de tuplas funciona da mesma forma
nomes_cidades = "são paulo, belo horizonte, rio de janeiro, brasilia"
nomes_cidades = nomes_cidades.split(", ")
# split quebra a string em varios valores. nesse caso separou por virgula e espaço
print(nomes_cidades)
# strip tira espaços excessivos nos dados
cabeçalho = "                         MENU PRINCIPAL"
print(cabeçalho.strip())
nome_cidade = "RiO dE jAnEiRo"
# Rio De Janeiro, todas primeiras letras em maíusculo
print(nome_cidade.title())
print(nome_cidade.capitalize())  # Rio de Janeiro
print(nome_cidade.lower())  # rio de janeiro
print(nome_cidade.upper())  # RIO DE JANEIRO
nome_cidade = input(
    "Que cidade do Brasil é conhecida como cidade maravilhosa?")
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'rio de janeiro':
    print("tente novamente")
    nome_cidade = input(
        "Que cidade do Brasil é conhecida como cidade maravilhosa?")
print("correto")
mensagem = "você viu o que o pietro disse na sala ontem?"
fui_citado = "pietro" in mensagem
print(fui_citado)


######################AULA 10##################################

cumprimento = "Olá, "
nome = "Felipe"
print(cumprimento + nome)
print(nome*5)
nome = "Felipe"
idade = 35
n_filhos = 2
print(nome + " tem " + str(idade) + " anos e " + str(n_filhos) + " filhos. ")
print("{} tem {} anos e {} filhos".format(nome, idade, n_filhos))

preco_gasolina = 3.476
print(' o prçeo da gasolina hoje subiu e está em R$ {:.2f}'.format(
    preco_gasolina))
print(f'{nome} tem {idade} anos e {n_filhos} filhos.')


######################AULA 11##################################

dados_cidade = {
    "nome": "são paulo",
    "estado": "são paulo",
    "area": 1521,
    "população_milhoes": 12.18
}
print(type(dados_cidade))
dados_cidade["país"] = "Brasil"
print(dados_cidade)
print(dados_cidade["nome"])
dados_cidade['area'] = 1500
print(dados_cidade)
dados_cidade_2 = dados_cidade
dados_cidade_2['nome'] = 'santos'
print(dados_cidade_2)
dados_cidade_3 = dados_cidade.copy()
dados_cidade_3['estado'] = 'rio de janeiro'
print(dados_cidade_3)
print(dados_cidade)
novos_dados = {
    'população_milhões': 15,
    'fundação': '25/01/1554'

}

dados_cidade.update(novos_dados)
print(dados_cidade)
print(dados_cidade.get('prefeito'))
print(dados_cidade.keys())  # retorna lista de chaves
print("----")
print(dados_cidade.values())  # retorna lista de valores
print("----")
print(dados_cidade.items())  # retorna lista de tuplas
print("----")


######################AULA 12###################################
# for loop
nomes_cidades = ['são paulo', 'londres', 'toquio', 'paris']
for nome in nomes_cidades:
    print(nome)

# usando while
contador = 0
nomes_cidades = ['são paulo', 'londres', 'toquio', 'paris']
# enquanto o contador for menor que a estrutura de dados
while contador < len(nomes_cidades):
    print(nomes_cidades[contador])
    contador = contador + 1

nomes_cidades = 'são paulo', 'londres', 'toquio', 'paris'
for nome in nomes_cidades:
    print(nome)

cidade = {
    'nome': 'são paulo',
    'estado': 'são paulo',
    'população_milhoes': 12.2
}
for chave in cidade:
    print(f'{chave}: {cidade[chave]}')

nomes_cidades = ['são paulo', 'londres', 'toquio', 'paris']
for nome in nomes_cidades:
    print(nome)

for posicao in range(len(nomes_cidades)):
    print(posicao)

for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'rio de janeiro'
print(nomes_cidades)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))


######################AULA 13##################################
# funções
def hello():  # aqui recebe os dados
    print('olá mundo')


hello()  # chamou a função e imprimiu


def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma/3
    return media


# pode chamar como calcula_media ou outro nome
resultado = calcula_media(10, 10, 10)
print(resultado)
resultado2 = calcula_media(valor1=10, valor2=10, valor3=9)
print(resultado2)

print('ola')
print('bruna')
# ou
print('ola', end=" ")
print('bruna')


def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma/3
    return media


resultado = calcula_media()
print(resultado)

######################AULA 14##################################


def calcula_media(valor1, valor2, valor3):
    soma = valor1+valor2+valor3
    media = soma/3
    return media


def calcula_media(*args):
    print(args, type(args))


calcula_media(10, 8, 9)


def calcula_media(*args):
    soma = sum(args)
    media = soma / len(args)
    return media


calcula_media(10, 8, 9)


def print_info(**kwargs):
    print(kwargs, type(kwargs))


print_info(nome='bruna', sobrenome='martins')

######################AULA 15##################################
# primeiro o diretorio com o nome do arquivo e depois a forma de abertura, r de read
arquivo = open('don_casmurro_cap_1.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()

arquivo = open('don_casmurro_cap_1.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
while linha! = ' ':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()  # vai imprimir todo o texto

arquivo = open('don_casmurro_cap_1.txt', 'r', encoding='utf-8')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

with open('don_casmurro_cap_1.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)

# criar arquivo do zero
with open('teste.txt', 'w') as arquivo:
    arquivo.write('linha teste\n')  # utf 8 não precisa no vscode
    arquivo.write('linha 2\n')
with open('teste.txt', 'r') as arquivo:
    print(arquivo.read(), end='')

######################AULA 16##################################
# csv
with open('brasil_covid', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        if float(linha[2]) > 1:
        print(linha)

# ou sem a biblioteca
with open('brasil_covid', 'r') as arquivo_csv:
    linhas = csv.file.read{}
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split('.')
        print(linha)

# escrita arquivo csv
with open('users.csv', 'w') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome'])
    escritor.writerow(['bruna', 'martins'])

header = ['nome', 'sobrenome']
dados = []
opt = input('o q quer fazer?\n1 - cadastrar\n0-sair\n')
while opt != '0':
    nome = input('nome')
    sobrenome = input('sobrenome')
    dados.append([nome, sobrenome])
    opt = input('o q quer fazer?\n1 - cadastrar\n0-sair\n')

print(dados)

with open('users.csv', 'w', newline='') as arquivo_users:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerow(dados)

with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

######################AULA 17##################################
# API interface que permite comunicação de dados
pip install requests  # instalando biblioteca
url = 'https: //api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)
dados = req.json()
print(dados)
url = 'https: //api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)
dados = req.json()
print(dados)
valor_reais = float(input('informe o valor em R$ a ser convertido\n'))
cotação = dados['rates']['BRL']
print(f'R$ {valor_reais:} em dólar valem US$ {valor_reais/cotacao:.2f}')

#####################AULA 18##################################
url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
resp.status_code
raw_data = resp.json()
raw_data[0]
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'],
                      obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0, ['confirmados', 'obitos',
                  'recuperados', 'ativos', 'data'])
final_data = []
confirmados = 0
obitos = 1
recuperados = 2
ativos = 3
data = 4
for i in range(1, len(final_data)):
    final_data[1][data] = final_data[1][data]
print(dt.time(12, 6, 21, 7), 'hora:minuto:segundo:microsegundo')
print('----')
print(dt.date(2020, 4, 25), 'ano-mes-dia')
print('----')
print(dt.datetime(2020, 4, 25, 12, 6, 21,),
      'ano-mes-dia hora:minuto:segundo:microsegundo')


def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets: []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data': y
            }
        ]


def set_title(title=''):
    if title != ' ':
        display = 'true'
    else:
        display = 'false'
    return {'title': title,
            'display': y
            }


def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_datasets(y, labels)
    options = set_title(title)
    chart = {

        'type': kind,
        'data': {
            'labels': x,
            'datasets': get_datasets
        },
        'options': options
    }
    return chart

    def get_api_chart(chart):
        url_base = 'https://quickchart;io/chart'
        resp = r.get(f'(url_base)?c={str(chart)}')
        return resp.content

        def save_image(path, content):
            with open(path, 'wb') as image:
                image.write(content)


def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[confirmados])
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[recuperados])
labels = ['confirmados', 'recuperados']
x = []
for obs in final_data[1::10]:
    x.append(obs[data].strftime('%d/%m/%y'))

chart = create_chart(x, [y_data_1, y_data_2], labels,
                     title="Casos confirmados x Casos recuperados")
charr_content = get_api_chart(chart)
save_image('grafico.png', chart_content)
display_image('grafico.png')
