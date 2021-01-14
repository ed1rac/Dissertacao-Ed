var acesso = ["Permitted", "Forbidden", "Obliged"]; //KP
var org = ['UFAC', 'CCET', 'CCSJA', 'Administrative_Unit', 'CFET', 'Uninorte',
       'Comite_Etica_Em_Pesquisa', 'CPA', 'Unidade_Administrativa',
       'FAMETA', 'IFAC']; //ORG
var sujeito = ['Secretario_de_Curso_Academico', 'Sandra_Maria_Soares_da_Rocha',
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
       'Raimunda_Souza', 'Marcos_Pontes', 'Ana_Ester']; //SR
var acao = ['Abertura', 'Solicitar', 'Acessar', 'Gerar', 'Calcular',
        'Matricular', 'Solicitacao', 'Analise', 'Requisitar', 'Criar',
        'Inserir', 'Cadastrar', 'Nova', 'Alterar', 'Efetivar',
        'LancarMedia', 'VoltarLancamento', 'SolicitacaoAbertura',
        'Cancelamento', 'Acess', 'Record', 'Create', 'Generate', 'Open',
        'Close']; //AA
var objeto = ['Documentos', 'Produtos', 'Almoxarifado', 'Materiais',
        'Planilhas_de_Calculo', 'IPTU', 'Portal_do_Aluno', 'Aluno',
        'Central_de_Copias', 'Central_de_Copias_Analise', 'Material',
        'Guia_de_Requisicao', 'Convencao', 'MatriculaAluno', 'Notas',
        'Process', 'ProcNURCADesp', 'ProcessDispatch', 'BuildDispatch',
        'FGTS', 'entral_de_Copias', 'Biblioteca']; //OV

//tamanhos dos objetos
var tamAcesso = acesso.length;
var tamOrg = org.length;
var tamSujeito = sujeito.length;
var tamAcao = acao.length;
var tamObjeto = objeto.length;

//geração dos números randômicos
function getAleatorio(max){
    return Math.trunc(Math.random() * max);
}

function geraUmaPolitica(num_politica){
    var str = '';
    str = str + 'Policy' + num_politica + ', ';
    str = str + acesso[getAleatorio(tamAcesso)] + ', ' + 
                org[getAleatorio(tamAcesso)] + ', ' + 
                sujeito[getAleatorio(tamAcesso)] + ', ' + 
                acao[getAleatorio(tamAcesso)] + ', ' +  
                objeto[getAleatorio(tamAcesso)];
    //console.log(str);
    return str;
}
//geração das políticas
//quantidade
var quant = 5;
var politicas = [];
for (var i = 1; i <= quant; i++){
    politicas.push(geraUmaPolitica(i));
}

function exibePoliticas(array_politicas){
    for (var i = 0; i < array_politicas.length; i++) {
        const element = array_politicas[i];
        document.writeln(element); 
        document.write('<br>');        
    }
}