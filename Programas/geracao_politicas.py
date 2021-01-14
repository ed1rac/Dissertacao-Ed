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
from random import randint
import pandas as pd
import numpy as np

def get_aleatorio(max):
  return randint(0,max-1)

def gera_uma_politica(num_politica):
  #str = '';
  numero = repr(num_politica+1)
  string = 'Policy' + numero + ', ' \
       + acesso[get_aleatorio(tamAcesso)] + ', ' \
       + org[get_aleatorio(tamAcesso)] + ', ' \
       + sujeito[get_aleatorio(tamAcesso)] + ',' \
       + acao[get_aleatorio(tamAcesso)] + ', ' \
       +  objeto[get_aleatorio(tamAcesso)]
  #print(string)
  return string

def exibe_politicas(array_politicas):
  for i in range(0,len(array_politicas)):
    linha = array_politicas[i]
    print(linha)

def gera_politicas(politicas, quant):  
  for i in range(0,quant):
    politicas.append(gera_uma_politica(i))

#listas com as opções das políticas
acesso = ["Permitted", "Forbidden", "Obliged"] #KP
org = ['UFAC', 'CCET', 'CCSJA', 'Administrative_Unit', 'CFET', 'Uninorte',
       'Comite_Etica_Em_Pesquisa', 'CPA', 'Unidade_Administrativa',
       'FAMETA', 'IFAC'] #ORG
sujeito = ['Secretario_de_Curso_Academico', 'Sandra_Maria_Soares_da_Rocha',
       'Outro_Usuario', 'Secretario_de_Centros_Academicos',
       'Jaider_Moreira_de_Almeida', 'Secretarios', 'Grupo_IPTU',
       'Socorro_Pontes', 'Jose_Rodrigues_Bardalles', 'Grupo_Almoxarifado',
       'Usuario_Qualquer', 'Joao_Josino',
       'Secretario_de_Unidade_Administrativa', 'PROTOCOLIZADOR3',
       'PROTOCOLIZADOR1', 'Joao_Paulo', 'Joao_Calvino', 'Maria_Das_Dores',
       'Professor', 'Coordenador', 'Pro_Reitora_Academica',
       'Setor_Administrativo', 'Joana_Siqueira', 'Francisco_Jose_Souza',
       'FranciscoJose_Souza', 'Marcos_Ponte', 'Marcos_Ponts',
       'Secretario_e_Unidade_Administrativa', 'Estagiario3',
       'Estagiario1', 'Vanessa_Lima', 'Janaina_Souza',
       'Usuario_Terceirizado', 'Jorge_Jesus', 'Aline_Moreira',
       'Raimundo_Nonato', 'Francisco_Mendes', 'Italo_Calvino',
       'Vanessa_Souza', 'Eliana_Maria_de_Souza', 'Francisco_Carlos',
       'Raimunda_Souza', 'Marcos_Pontes', 'Ana_Ester'] #SR
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
        'FGTS', 'entral_de_Copias', 'Biblioteca'] #OV   

tamAcesso = len(acesso)
tamOrg = len(org)
tamSujeito = len(sujeito)
tamAcao = len(acao)
tamObjeto = len(objeto)

politicas = []
quantidade_gerada = 100
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