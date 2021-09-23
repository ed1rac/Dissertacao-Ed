#Geração das políticas
"""
Autor  :  Edkallenn Lima
Data   :  18/04/2019 
Função :  Gera automaticamente as políticas de controle     
          de acesso. As políticas são geradas a partir      
          de listas com os valores das mesmas. 
          As instâncias geradas são todas randômicas.
Obs.   :
"""
#Geração das políticas
from random import randint
import pandas as pd
import numpy as np
import time
import random
from time import sleep


def get_aleatorio(max):
  return random.randint(0,max-1)

def gera_uma_politica(num_politica):
  #str = '';
  milisegundos = int(round(time.time() * 1000))
  random.seed(milisegundos)

  data1 = random_date("1/1/2017 1:30 PM", "1/1/2018 4:50 AM", random.random())
  data2 = random_date("1/1/2019 1:30 PM", "1/1/2020 4:50 AM", random.random())
  numero = repr(num_politica+1)
  string = 'Policy' + numero + ', ' \
       + acesso[get_aleatorio(tamAcesso)] + ', ' \
       + org[get_aleatorio(tamOrg)] + ', ' \
       + sujeito[get_aleatorio(tamSujeito)] + ',' \
       + acao[get_aleatorio(tamAcao)] + ', ' \
       + objeto[get_aleatorio(tamObjeto)] + ', ' \
       + data1  + ', ' + data2
  #print(string)
  return string

def exibe_politicas(array_politicas):
  for i in range(0,len(array_politicas)):
    linha = array_politicas[i]
    print(linha)

def gera_politicas(politicas, quant):  
  for i in range(0,quant):    
    politicas.append(gera_uma_politica(i))
    sleep(0.01)

def str_time_prop(data_inicial, data_final, formato, prop):
    """Retorna uma data na proporção de um intervalo de dois tempos formatados:
    - data_inicial e data_final devem ser strings especificando os tempos formatados no formato determinado  (estilo strftime), 
      fornecendo um intervalo [data_inicial, data_final].
    - prop especifica como uma proporção do intervalo a ser tomada após data_inicial. 
      O horário de retorno será no formato especificado.

    Exemplo de uso:
      data1 = random_date("1/1/2017 1:30 PM", "1/1/2018 4:50 AM", random.random())
      data2 = random_date("1/1/2019 1:30 PM", "1/1/2020 4:50 AM", random.random())
      print('Data1 = {}\nData2 = {}'.format(data1, data2))
    """

    stime = time.mktime(time.strptime(data_inicial, formato))
    etime = time.mktime(time.strptime(data_final, formato))

    ptime = stime + prop * (etime - stime)

    return time.strftime(formato, time.localtime(ptime))

def random_date(data_inicial, data_final, prop):
    return str_time_prop(data_inicial, data_final, '%d/%m/%Y %I:%M %p', prop)



#listas com as opções das políticas
acesso = ["Permitted", "Forbidden", "Obliged"] #KP

org = ['UFAC', 'CCET', 'CCSJA', 'Administrative_Unit', 'CFET', 'Uninorte',
       'Comite_Etica_Em_Pesquisa', 'CPA', 'Unidade_Administrativa',
       'FAMETA', 'IFAC', 'UNIMETA', 'Unidade_Gerencial', 'FAAO',
       'UNIASSELVI', 'Estácio', 'Unidade_Executiva', 'Unidade_Financeira',
       'UNOPAR'] #ORG

sujeito = ['Secretario_de_Curso_Academico', 'Daenerys_Targaryen',
       'Outro_Usuario', 'Secretario_de_Centros_Academicos',
       'Tyrion_Lannister', 'Secretarios', 'Grupo_IPTU', 'Arwen_Undomiel',
       'Jaime_Lannister', 'Grupo_Almoxarifado', 'Usuario_Qualquer',
       'Eddard_Stark', 'Secretario_de_Unidade_Administrativa',
       'PROTOCOLIZADOR3', 'PROTOCOLIZADOR1', 'Oberyn_Martell',
       'Carl_Sagan', 'Ada_Lovelace', 'Professor', 'Coordenador',
       'Pro_Reitora_Academica', 'Tyrion Lanniester',
       'Setor_Administrativo', 'Cersei_Lannister', 'Robb_Stark', 'Elrond',
       'Bilbo_Bolseiro', 'Marcos_Ponts',
       'Secretario_e_Unidade_Administrativa', 'Estagiario3',
       'Estagiario1', 'Vanessa_Lima', 'Janaina_Souza',
       'Usuario_Terceirizado', 'Jorge_Jesus', 'Aline_Moreira',
       'Raimundo_Nonato', 'Francisco_Mendes', 'Italo_Calvino',
       'Vanessa_Souza', 'Eliana_Maria_de_Souza', 'Francisco_Carlos',
       'Raimunda_Souza', 'Bilbo_Bolseiros', 'Ana_Ester'] #SR

acao = ['Abertura', 'Solicitar', 'Acessar', 'Gerar', 'Calcular',
       'Matricular', 'Solicitacao', 'Analise', 'Requisitar', 'Criar',
       'Inserir', 'Cadastrar', 'Nova', 'Alterar', 'Efetivar',
       'LancarMedia', 'VoltarLancamento', 'SolicitacaoAbertura',
       'Cancelamento', 'Acess', 'Record', 'Create', 'Generate', 'Open',
       'Close'] #AA

objeto = ['Documentos', 'Produtos', 'Almoxarifado', 'Materiais',
       'Planilhas_de_Calculo', 'IPTU', 'Portal_do_Aluno', 'Aluno',
       'Central_de_Copias', 'Central_de_Copias_Analise', 'Material',
       'Guia_de_Requisicao', 'Convencao', 'MatriculaAluno', 'Notas',
       'Process', 'ProcNURCADesp', 'ProcessDispatch', 'BuildDispatch',
       'FGTS', 'Central_Processo', 'Biblioteca'] #OV   
tamAcesso = len(acesso)
tamOrg = len(org)
tamSujeito = len(sujeito)
tamAcao = len(acao)
tamObjeto = len(objeto)

politicas = []
quantidade_gerada = 200
gera_politicas(politicas, quantidade_gerada)

teste = pd.DataFrame(np.array(politicas), columns=['politica'])
teste.to_csv('politicas_geradas.csv', index=False)

#retira as aspas
with open("politicas_geradas.csv", "rt") as fin:
    with open("politicas_geradas_out.csv", "wt") as fout:
        for line in fin:
            fout.write(line.replace("\"" , ""))

#altera a primeira linha pelas colunas corretas
from io import StringIO
buffer = StringIO()

with open('politicas_geradas_out.csv', 'r') as stream:
    for index, line in enumerate(stream):
        # index == 0 representa a primeira linha do arquivo:
        buffer.write('Politica,Acesso,Organizacao,Sujeito,Acao,Objeto\n' if index == 0 else line)

with open('politicas_geradas_final.csv', 'w') as stream:
    stream.write(buffer.getvalue())