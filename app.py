import pandas as pd
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime as dt

app = dash.Dash(__name__, title='Painel da Inclusão Produtiva', update_title='Carregando...', external_stylesheets=[dbc.themes.BOOTSTRAP,
                                                                                                          'https://use.fontawesome.com/releases/v5.12.1/css/all.css',
                                                                                                          '//fonts.googleapis.com/css?family=Roboto|Lato',
                                                                                                          'https://fonts.googleapis.com/css2?family=Open+Sans&display=swap'],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}],
                suppress_callback_exceptions=True)
server = app.server

# CARREGAR DADOS#
data = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/base_painel_inclus%C3%A3o_produtiva.csv'
df1 = pd.read_csv(data, sep=';', encoding='latin1', low_memory=False)
uf = df1.groupby('uf').agg({'populacao': 'sum', 'pessoas_cad':'sum', 'pes_cad_urbano':'sum', 'pes_cad_rural':'sum', 'cad_feminino':'sum', 'cad_masculino':'sum',
                                        'pessoas_pbf':'sum','pobreza_extremapob_cad':'sum','bpc_ben':'sum','bpc_pcd_ben':'sum','bpc_idoso_ben':'sum','familias_catadores_cad':'sum',
                                        'sabe_ler_escrever':'sum', 'não_sabe_ler_escrever':'sum', 'cad_ensino_fundamental_completo':'sum', 'cad_ensino_fundamental_incompleto':'sum',
                                        'cad_sem_instrucao':'sum', 'cad_ensino_medio_incompleto':'sum', 'cad_superior_completo_incompleto':'sum', 'trab_12_meses':'sum', 'não_trab_12_meses':'sum',
                                        'trab_semana_passada':'sum', 'não_trab_semana_passada':'sum', 'trab_autonomo':'sum', 'trab_temp_area_rura':'sum', 'emprego_sem_carteira':'sum',
                                        'emprego_com_carteira':'sum', 'trab_domestico_sem_carteira':'sum', 'trab_domestico_com_carteira':'sum', 'trabalhador_não_remunerado':'sum',
                                        'militar_servidor_publico':'sum', 'empregador':'sum', 'estagiario':'sum', 'aprendiz':'sum', 'pib_total':'sum', 'pib_agropecuaria':'sum',
                                        'pib_industria':'sum', 'pib_servicos':'sum', 'pib_admpublica':'sum', 'pessoas_deficiencia':'sum', 'faixa_etaria_pessoas_16_17_anos':'sum',
                                        'faixa_etaria_pessoas_18_24_anos':'sum', 'faixa_etaria_pessoas_25_34_anos':'sum', 'faixa_etaria_pessoas_35_39_anos':'sum', 'faixa_etaria_pessoas_40_44_anos':'sum',
                                        'faixa_etaria_pessoas_45_49_anos':'sum', 'faixa_etaria_pessoas_50_54_anos':'sum', 'faixa_etaria_pessoas_55_59_anos':'sum', 'faixa_etaria_pessoas_60_64_anos':'sum',
                                        'vagas_sine':'sum', 'saldo_empregos2021':'sum', 'saldo_empregos_12meses':'sum', 'estoque_empregos_abr2021':'sum', 'saldo_empregos2002':'sum',
                                        'saldo_empregos2003':'sum', 'saldo_empregos2004':'sum', 'saldo_empregos2005':'sum', 'saldo_empregos2006':'sum', 'saldo_empregos2007':'sum',
                                        'saldo_empregos2008':'sum', 'saldo_empregos2009':'sum', 'saldo_empregos2010':'sum', 'saldo_empregos2011':'sum', 'saldo_empregos2012':'sum',
                                        'saldo_empregos2013':'sum', 'saldo_empregos2014':'sum', 'saldo_empregos2015':'sum', 'saldo_empregos2016':'sum', 'saldo_empregos2017':'sum',
                                        'saldo_empregos2018':'sum', 'saldo_empregos2019':'sum', 'empresas_total':'sum', 'empresas_agropecuaria':'sum', 'empresas_ind_extrativas':'sum',
                                        'empresas_ind_transf':'sum', 'empresas_eletric_gas':'sum', 'empresas_saneamento':'sum', 'empresas_construcao':'sum', 'empresas_comercio':'sum',
                                        'empresas_transporte':'sum', 'empresas_alojamento_alimentacao':'sum', 'empresas_info_comunic':'sum', 'empresas_financeiro':'sum',
                                        'empresas_imobiliarias':'sum', 'empresas_ativ_profissionais_cient_tecnicas':'sum', 'empresas_ativ_administrativas':'sum', 'empresas_admpublica':'sum',
                                        'empresas_educacao':'sum', 'empresas_saude_servicosocial':'sum', 'empresas_arte_cultura':'sum', 'empresas_outras_ativ_servicos':'sum',
                                        'mei_cadunico':'sum', 'mei_pbf':'sum','cad_ensino_medio_completo':'sum', 'distorcao_idade_serie': 'mean', 'taxa_evasao_abandono': 'mean', 'remuneracao_docente_edbasica':'mean',
                                        'idhm':'mean', 'var_saldo_empregos_12meses':'mean', 'ivs':'mean', 'taxa_homicidios ':'mean', 'familias_cad':'sum', 'familias_pbf':'sum'
                                        }).reset_index()
uf['municipio'] = ' Todos os Municípios'
regiao = df1.groupby(by=['regiao']).agg({'populacao': 'sum', 'pessoas_cad':'sum', 'pes_cad_urbano':'sum', 'pes_cad_rural':'sum', 'cad_feminino':'sum', 'cad_masculino':'sum',
                                        'pessoas_pbf':'sum','pobreza_extremapob_cad':'sum','bpc_ben':'sum','bpc_pcd_ben':'sum','bpc_idoso_ben':'sum','familias_catadores_cad':'sum',
                                        'sabe_ler_escrever':'sum', 'não_sabe_ler_escrever':'sum', 'cad_ensino_fundamental_completo':'sum', 'cad_ensino_fundamental_incompleto':'sum',
                                        'cad_sem_instrucao':'sum', 'cad_ensino_medio_incompleto':'sum', 'cad_superior_completo_incompleto':'sum', 'trab_12_meses':'sum', 'não_trab_12_meses':'sum',
                                        'trab_semana_passada':'sum', 'não_trab_semana_passada':'sum', 'trab_autonomo':'sum', 'trab_temp_area_rura':'sum', 'emprego_sem_carteira':'sum',
                                        'emprego_com_carteira':'sum', 'trab_domestico_sem_carteira':'sum', 'trab_domestico_com_carteira':'sum', 'trabalhador_não_remunerado':'sum',
                                        'militar_servidor_publico':'sum', 'empregador':'sum', 'estagiario':'sum', 'aprendiz':'sum', 'pib_total':'sum', 'pib_agropecuaria':'sum',
                                        'pib_industria':'sum', 'pib_servicos':'sum', 'pib_admpublica':'sum', 'pessoas_deficiencia':'sum', 'faixa_etaria_pessoas_16_17_anos':'sum',
                                        'faixa_etaria_pessoas_18_24_anos':'sum', 'faixa_etaria_pessoas_25_34_anos':'sum', 'faixa_etaria_pessoas_35_39_anos':'sum', 'faixa_etaria_pessoas_40_44_anos':'sum',
                                        'faixa_etaria_pessoas_45_49_anos':'sum', 'faixa_etaria_pessoas_50_54_anos':'sum', 'faixa_etaria_pessoas_55_59_anos':'sum', 'faixa_etaria_pessoas_60_64_anos':'sum',
                                        'vagas_sine':'sum', 'saldo_empregos2021':'sum', 'saldo_empregos_12meses':'sum', 'estoque_empregos_abr2021':'sum', 'saldo_empregos2002':'sum',
                                        'saldo_empregos2003':'sum', 'saldo_empregos2004':'sum', 'saldo_empregos2005':'sum', 'saldo_empregos2006':'sum', 'saldo_empregos2007':'sum',
                                        'saldo_empregos2008':'sum', 'saldo_empregos2009':'sum', 'saldo_empregos2010':'sum', 'saldo_empregos2011':'sum', 'saldo_empregos2012':'sum',
                                        'saldo_empregos2013':'sum', 'saldo_empregos2014':'sum', 'saldo_empregos2015':'sum', 'saldo_empregos2016':'sum', 'saldo_empregos2017':'sum',
                                        'saldo_empregos2018':'sum', 'saldo_empregos2019':'sum', 'empresas_total':'sum', 'empresas_agropecuaria':'sum', 'empresas_ind_extrativas':'sum',
                                        'empresas_ind_transf':'sum', 'empresas_eletric_gas':'sum', 'empresas_saneamento':'sum', 'empresas_construcao':'sum', 'empresas_comercio':'sum',
                                        'empresas_transporte':'sum', 'empresas_alojamento_alimentacao':'sum', 'empresas_info_comunic':'sum', 'empresas_financeiro':'sum',
                                        'empresas_imobiliarias':'sum', 'empresas_ativ_profissionais_cient_tecnicas':'sum', 'empresas_ativ_administrativas':'sum', 'empresas_admpublica':'sum',
                                        'empresas_educacao':'sum', 'empresas_saude_servicosocial':'sum', 'empresas_arte_cultura':'sum', 'empresas_outras_ativ_servicos':'sum',
                                        'mei_cadunico':'sum', 'mei_pbf':'sum','cad_ensino_medio_completo':'sum', 'distorcao_idade_serie': 'mean', 'taxa_evasao_abandono': 'mean', 'remuneracao_docente_edbasica':'mean',
                                        'idhm':'mean', 'var_saldo_empregos_12meses':'mean', 'ivs':'mean', 'taxa_homicidios ':'mean', 'familias_cad':'sum', 'familias_pbf':'sum'
                                        }).reset_index()
regiao['municipio'] = ' Todos os Municípios'
regiao['uf'] = regiao['regiao']
pais = df1.groupby(by=["pais"]).agg({'populacao': 'sum', 'pessoas_cad':'sum', 'pes_cad_urbano':'sum', 'pes_cad_rural':'sum', 'cad_feminino':'sum', 'cad_masculino':'sum',
                                        'pessoas_pbf':'sum','pobreza_extremapob_cad':'sum','bpc_ben':'sum','bpc_pcd_ben':'sum','bpc_idoso_ben':'sum','familias_catadores_cad':'sum',
                                        'sabe_ler_escrever':'sum', 'não_sabe_ler_escrever':'sum', 'cad_ensino_fundamental_completo':'sum', 'cad_ensino_fundamental_incompleto':'sum',
                                        'cad_sem_instrucao':'sum', 'cad_ensino_medio_incompleto':'sum', 'cad_superior_completo_incompleto':'sum', 'trab_12_meses':'sum', 'não_trab_12_meses':'sum',
                                        'trab_semana_passada':'sum', 'não_trab_semana_passada':'sum', 'trab_autonomo':'sum', 'trab_temp_area_rura':'sum', 'emprego_sem_carteira':'sum',
                                        'emprego_com_carteira':'sum', 'trab_domestico_sem_carteira':'sum', 'trab_domestico_com_carteira':'sum', 'trabalhador_não_remunerado':'sum',
                                        'militar_servidor_publico':'sum', 'empregador':'sum', 'estagiario':'sum', 'aprendiz':'sum', 'pib_total':'sum', 'pib_agropecuaria':'sum',
                                        'pib_industria':'sum', 'pib_servicos':'sum', 'pib_admpublica':'sum', 'pessoas_deficiencia':'sum', 'faixa_etaria_pessoas_16_17_anos':'sum',
                                        'faixa_etaria_pessoas_18_24_anos':'sum', 'faixa_etaria_pessoas_25_34_anos':'sum', 'faixa_etaria_pessoas_35_39_anos':'sum', 'faixa_etaria_pessoas_40_44_anos':'sum',
                                        'faixa_etaria_pessoas_45_49_anos':'sum', 'faixa_etaria_pessoas_50_54_anos':'sum', 'faixa_etaria_pessoas_55_59_anos':'sum', 'faixa_etaria_pessoas_60_64_anos':'sum',
                                        'vagas_sine':'sum', 'saldo_empregos2021':'sum', 'saldo_empregos_12meses':'sum', 'estoque_empregos_abr2021':'sum', 'saldo_empregos2002':'sum',
                                        'saldo_empregos2003':'sum', 'saldo_empregos2004':'sum', 'saldo_empregos2005':'sum', 'saldo_empregos2006':'sum', 'saldo_empregos2007':'sum',
                                        'saldo_empregos2008':'sum', 'saldo_empregos2009':'sum', 'saldo_empregos2010':'sum', 'saldo_empregos2011':'sum', 'saldo_empregos2012':'sum',
                                        'saldo_empregos2013':'sum', 'saldo_empregos2014':'sum', 'saldo_empregos2015':'sum', 'saldo_empregos2016':'sum', 'saldo_empregos2017':'sum',
                                        'saldo_empregos2018':'sum', 'saldo_empregos2019':'sum', 'empresas_total':'sum', 'empresas_agropecuaria':'sum', 'empresas_ind_extrativas':'sum',
                                        'empresas_ind_transf':'sum', 'empresas_eletric_gas':'sum', 'empresas_saneamento':'sum', 'empresas_construcao':'sum', 'empresas_comercio':'sum',
                                        'empresas_transporte':'sum', 'empresas_alojamento_alimentacao':'sum', 'empresas_info_comunic':'sum', 'empresas_financeiro':'sum',
                                        'empresas_imobiliarias':'sum', 'empresas_ativ_profissionais_cient_tecnicas':'sum', 'empresas_ativ_administrativas':'sum', 'empresas_admpublica':'sum',
                                        'empresas_educacao':'sum', 'empresas_saude_servicosocial':'sum', 'empresas_arte_cultura':'sum', 'empresas_outras_ativ_servicos':'sum',
                                        'mei_cadunico':'sum', 'mei_pbf':'sum','cad_ensino_medio_completo':'sum', 'distorcao_idade_serie': 'mean', 'taxa_evasao_abandono': 'mean', 'remuneracao_docente_edbasica':'mean',
                                        'idhm':'mean', 'var_saldo_empregos_12meses':'mean', 'ivs':'mean', 'taxa_homicidios ':'mean', 'familias_cad':'sum', 'familias_pbf':'sum'
                                        }).reset_index()
pais['municipio'] = ' Todos os Municípios'
pais['uf'] = pais['pais']
df = df1.append([uf, regiao, pais], ignore_index=True)

data1 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/vinculos_ativos_ocupacao_subgruposprincipais_2019.csv'
df_caged = pd.read_csv(data1, sep=';', encoding='latin1', low_memory=False)

data2 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/evolucao_pessoas_cad_pbf.csv'
df_cad = pd.read_csv(data2, sep=';', encoding='latin1', low_memory=False)

data3 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/remuneracao_SM_ocupacao_subgruposprincipais_2015_2019.csv'
df_remuneracao = pd.read_csv(data3, sep=';', encoding='latin1', low_memory=False)

data4 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/saldo_empregos_ocupacao_subgruposprincipais_2019.csv'
df_saldo = pd.read_csv(data4, sep=';', encoding='latin1', low_memory=False)

data6 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/vinculos_ativos_subsetor_IBGE_2019_RAIS.csv'
df_vinculos_subsetor_ibge = pd.read_csv(data6, sep=';', encoding='latin1', low_memory=False)
df_vinculos_subsetor_ibge = df_vinculos_subsetor_ibge.drop(['Município'], axis=1)

data7 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/saldo_empregos_subsetor_IBGE_2019_RAIS.csv'
df_saldo_subsetor_ibge = pd.read_csv(data7, sep=';', encoding='latin1', low_memory=False)
df_saldo_subsetor_ibge = df_saldo_subsetor_ibge.drop(['Município'], axis=1)

df_data = pd.read_csv('https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/tabela_bases_dados.csv', sep=';', encoding='latin1')
table = dbc.Table.from_dataframe(df_data, bordered=True, hover=True, style={'fontSize':14})

# --------------------------------------------------------------------------------------------------------------------------------------------
# NAVBAR
logo_progredir = "https://github.com/vitorlsantana/progredir_dashboard/blob/main/Marca_Progredir.png?raw=true"
logo_ministerio = 'http://www.mds.gov.br/webarquivos/cidadania/marca_gov/horizontal/ASSINATURA_CIDADANIA_216X64px.png'

app.layout = dbc.Container([
    # HEADER
    dbc.Row(
        [
            dbc.Col([], className='col-3'),
            dbc.Col(html.H1('Painel da Inclusão Produtiva Urbana', style={'color':'white', 'textAlign':'center', 'fontWeight': 'bold', 'fontSize':45}),
                    className='col-6', style={'align':'center', 'padding':'40px'}, xs=12, sm=12, md=12, lg=12, xl=12),
            dbc.Col([], className='col-3'),
        ], className='row', align='center', style={'backgroundColor':'#071D41'}
    ),
    # GRID
    dbc.Row([
        # SIDEBAR
        dbc.Col([
            html.Div(html.A(html.Img(
                src='https://github.com/vitorlsantana/progredir_dashboard/blob/main/assets/Marca_Progredir.png?raw=true',
                style={'height': '10%', 'width': '75%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
                href='https://www.gov.br/cidadania/pt-br/acoes-e-programas/progredir', target="_blank")),
            html.Label('Consulta', style={'fontSize':20, "width": "100%", 'color': 'white', 'fontWeight': 'bold'},
                   className='mt-3'),
            html.Label('Selecione a Região', style={'fontSize':15, "width": "100%", 'color': 'white', 'fontWeight': 'bold'},
                   className='mt-1'),
            dcc.Dropdown(
                id='w_municipios',
                options=[{'label': i, 'value': i} for i in sorted(df['uf'].unique())],
                value='Brasil',
                placeholder= "Selecione a região",
                style={'display': True, "width": "100%", 'height': '40px', 'outline':True}
            ),
            html.Label('Selecione o Município', style={'color': 'white', 'fontSize':15, 'fontWeight': 'bold', 'margin-top':'15px'}),
            dcc.Dropdown(
                id='w_municipios1',
                value=' Todos os Municípios',
                placeholder ='Selecione o município',
                options=[],
                style={'display': True, "width": "100%", 'height': '40px'}
            ),
            html.Br(),
            html.P(
                'O painel é parte da estratégia do Plano Progredir, e visa disponibilizar acesso a dados importantes para o diagnóstico '
                'e o desenho de estratégias de inclusão produtiva mais efetivas em seu território.',
                style={'fontSize': 15, "width": "100%", 'whiteSpace': 'pre-wrap', 'background-color':'white', 'border-radius':'3px',
                       'border': '1px solid white', 'fontWeight':'bold', 'textAlign':'center', 'padding':'10px', 'color':'#071D41'}),
            dbc.Button(
                "Saiba mais sobre o painel",
                id="open",
                className="mr-5",
                outline=True,
                color="light",
                style={"width": "100%", 'fontWeight': 'bold', 'fontSize':15, 'height': '40px'}
            ),
            html.Br(),
            dbc.Modal(
                [
                    dbc.ModalHeader("Sobre o painel"),
                    dbc.ModalBody(
                        [
                        "O Painel da Inclusão Produtiva Urbana tem por objetivo reunir informações que possibilitem uma "
                        "compreensão ampla do cenário social e econômico nos níveis estadual e municipal.\n\nCom isso, espera-se auxiliar gestores públicos "
                        "em nível local e parceiros do setor empresarial e da sociedade civil a "
                        "desenharem estratégias de inclusão produtiva para a população de baixa renda, em especial daquela localizada no meio urbano. "
                        "Para isso, foram agregados em uma única plataforma dados sobre o contexto social - população, serviços e ações disponíveis, "
                        "a atividade econômica, empreendedorismo, microcrédito, dentre outras, obtidos a partir de um conjunto de bases públicas "
                        "governamentais.\n\nA ferramenta foi desenvolvida pelo Departamento de Inclusão Produtiva Urbana da Secretaria Nacional de "
                        "Inclusão Social e Produtiva, vinculada à Secretaria Especial do Desenvolvimento Social do Ministério da Cidadania. \n\n",
                        html.A(
                            "Conheça o portal do Progredir",
                            href="https://www.gov.br/cidadania/pt-br/acoes-e-programas/progredir",
                            target="_blank")
                    ]),
                    dbc.ModalFooter(
                        dbc.Button("Fechar", id="close-lg", className="ml-auto")
                    ),
                ],
                id="modal",
                centered=True,
                style={"width":"100%", 'whiteSpace': 'pre-wrap'},
            ),
            html.Br(),
            dbc.Button("Saiba mais sobre os dados", id='open1', className="mr-5", outline=True, color="light",
                       style={"width": "100%", 'fontWeight': 'bold', 'fontSize':15, 'height': '40px'}),
            dbc.Modal(
                [
                    dbc.ModalHeader("Dados utilizados no painel"),
                    dbc.ModalBody(
                        table
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Fechar", id="close1", className="ml-auto")),
                ],
                id="modal1",
                size='xl',
                centered=True,
                style={"width":"100%", 'whiteSpace': 'pre-wrap'},
            ),
        ], xs=12, sm=12, md=2, lg=2, xl=2, style={'backgroundColor':'#071D41', 'marginBottom':'20px'}
        ),
        # TABS
        html.Br(),
        dbc.Col(children=[
            dbc.Tabs([
                dbc.Tab(label="Contexto socioeconômico", tab_id="economia",
                        activeLabelClassName='flex-sm-fill text-sm-center bg-primary font-weight-bold',
                        tabClassName='m-auto rounded text-sm-center',
                        labelClassName='flex-sm-fill text-sm-center rounded text-white'),
                dbc.Tab(label="Perfil das pessoas no Cadastro Único", tab_id="social", activeLabelClassName='flex-sm-fill text-sm-center bg-primary font-weight-bold',
                        tabClassName='m-auto rounded text-sm-center', labelClassName='flex-sm-fill text-sm-center rounded text-white'),
                dbc.Tab(label="Situação de trabalho e emprego", tab_id="trabalho", activeLabelClassName='flex-sm-fill text-sm-center bg-primary font-weight-bold',
                        tabClassName='m-auto rounded text-sm-center', labelClassName='flex-sm-fill text-sm-center rounded text-white'),
                dbc.Tab(label="Perfil educacional", tab_id="educacao",
                        activeLabelClassName='flex-sm-fill text-sm-center bg-primary font-weight-bold',
                        tabClassName='m-auto rounded text-sm-center',
                        labelClassName='flex-sm-fill text-sm-center rounded text-white'),
                dbc.Tab(label="Iniciativas de inclusão produtiva", tab_id="servicos", activeLabelClassName='flex-sm-fill text-sm-center bg-primary font-weight-bold', tabClassName='m-auto rounded text-sm-center',
                        labelClassName='flex-sm-fill text-sm-center rounded text-white'),
                dbc.Tab(label="Estudos e pesquisas", tab_id="estudos", activeLabelClassName='flex-sm-fill text-sm-center bg-primary font-weight-bold', tabClassName='m-auto rounded text-sm-center',
                        labelClassName='flex-sm-fill text-sm-center rounded text-white'),
            ],
                id="tabs",
                active_tab="social",
                style={'flex': '1 1 0px'}
            ),
            html.Div(id="tab-content", className="p-10"),
        ], xs=12, sm=12, md=10, lg=10, xl=10, className='mt-100'),
    ], justify="center"),
    html.Br(),
], fluid=True, style={'backgroundColor':'#071D41'})

# SELEÇÃO DE UF E MUNICÍPIO
@app.callback(
    Output('w_municipios1', 'options'),
    [Input('w_municipios', 'value')]
)
def get_municipios_options(w_municipios):
    def1 = df[df['uf'] == w_municipios]
    return [{'label': i, 'value': i} for i in sorted(def1['municipio'].unique())]

@app.callback(
    Output('w_municipios1', 'value'),
    [Input('w_municipios1', 'options')],
)
def get_municipios_value(w_municipios1):
    return [k['value'] for k in w_municipios1][0]

# COLLAPSE TAB
@app.callback(
    Output("collapse-tab", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse-tab", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# MODAL SOBRE O PAINEL
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close-lg", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab")]
)
def render_tab_content(active_tab):
    if active_tab:
        if active_tab == "social":
            return dbc.Container(children=[
                html.Br(),
                dbc.Row(children=
                [
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H5("Cadastro Único (abr/2021)", className="card-title", style={'textAlign':'center'}),
                                    html.P(id='cadunico', style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold', 'margin-bottom':'1px'}),
                                    html.P(id='familias_cad', style={'color': 'grey', 'textAlign': 'center', 'fontSize': 15, 'margin-top':0, 'fontWeight':'bold'}),
                                    html.P(id='perc_cad', style={'color': '#f94144', 'textAlign': 'center', 'margin-top':'5px', 'margin-bottom':0, 'fontSize': 20, 'fontWeight': 'bold'}),
                                ]),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border':'white', 'marginBottom':'5px',
                                                                     'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=6, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H5("Bolsa Família (abr/2021)", className="card-title", style={'textAlign':'center'}),
                                    html.P(id='bolsa_familia', style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold', 'margin-bottom':'1px'}),
                                    html.P(id='familias_pbf', style={'color': 'grey', 'textAlign': 'center', 'fontSize': 15, 'margin-top': 0, 'fontWeight':'bold'}),
                                    html.P(id='perc_pbf', style={'color': '#f94144', 'textAlign': 'center', 'margin-top':'5px', 'margin-bottom':0, 'fontSize': 20, 'fontWeight': 'bold'}),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border': 'white', 'marginBottom':'5px',
                                                                     'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=6, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H5("Domicílio Urbano", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='urbano_cad',
                                           style={'color': '#1351B4', 'fontSize': 30, 'textAlign': 'center',
                                                  'fontWeight': 'bold'}),
                                    html.P(id='perc_urbano',
                                           style={'color': '#f94144', 'textAlign': 'center', 'margin-top':'5px',
                                                  'margin-bottom':0, 'fontSize': 20, 'fontWeight': 'bold'}),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey', 'height':'185px'}
                            )
                        ], xs=12, sm=12, md=6, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H5("Distribuição por sexo", className="card-title", style={'textAlign': 'center'}),
                                    dbc.Row(
                                        [
                                            html.H5(className="fas fa-male", style={'fontSize': 35, 'textAlign': 'center', 'color':'#f77f00'}),
                                            html.P(id='masc_cad',
                                                   style={'fontSize': 24, 'margin-top': '1px', 'fontWeight': 'bold', 'margin-left':'30px'}),
                                        ],
                                    ),
                                    dbc.Row(
                                        [
                                            html.H5(className="fas fa-female", style={'fontSize': 35, 'textAlign': 'center', 'align-items':'center', 'color':'#f77f00'}),
                                            html.P(id='fem_cad',
                                                   style={'margin-top': '1px', 'margin-left':'30px', 'margin-bottom':0, 'fontSize': 24, 'fontWeight': 'bold'}),
                                        ], style={'margin-top': '1px', 'margin-bottom':0},
                                    ),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px', 'align-items':'center',
                                       'box-shadow': '1px 1px 1px 1px lightgrey', 'height':'185px'}
                            )
                        ], xs=12, sm=12, md=6, lg=3, xl=3),
                ],
                    align='center'
                ),
                html.Br(),
                dbc.Row(
                    [
                    dbc.Col(dcc.Graph(id='cad_pbf'), style={'marginBottom':'10px'}, xs=12, sm=12, md=12, lg=6, xl=6),
                    dbc.Col(dcc.Graph(id='faixa_etaria'), xs=12, sm=12, md=12, lg=6, xl=6),
                        ],
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(id='outros_dados', xs=12, sm=12, md=12, lg=6, xl=6),
                    ], align='center'),
            ], fluid=True
            )
        elif active_tab == "trabalho":
            return dbc.Container(children=[
                html.Br(),
                dbc.Row(children=
                    [
                        dbc.Col(
                            [
                            dbc.Row(children=
                            [
                                dbc.Col(
                                    [
                                        dbc.Card(children=
                                        [
                                            dbc.CardBody(children=
                                            [
                                                html.H5("Situação de emprego formal", className="card-title",
                                                        style={'textAlign': 'center', 'fontWeight':'bold'}),
                                                html.P(
                                                    'Os dados de emprego formal foram obtidos da Relação Anual de Informações Sociais (RAIS), que é um cadastro administrativo, '
                                                    'instituído pelo Decreto nº 76.900/1975, de âmbito nacional, periodicidade anual e de declaração obrigatória '
                                                    'para todos os estabelecimentos do setor público e privado, inclusive para aqueles que não registraram vínculos empregatícios no exercício.',
                                                    style={'textAlign': 'justify', 'opacity': .7, 'fontSize': 15}),
                                            ]),
                                        ], color="#F8F8F8", outline=True,
                                            style={"width": "100%", 'border': 'white', 'marginBottom': '30px',
                                                   'box-shadow': '1px 1px 1px 1px lightgrey', 'heigth':'130px'}
                                        )
                                    ], xs=12, sm=12, md=12, lg=12, xl=12),
                                dbc.Col(
                                    [
                                        dbc.Card(children=
                                        [
                                            dbc.CardBody(children=
                                            [
                                                html.H5("Pessoas com carteira assinada (abr/2021)", className="card-title",
                                                        style={'textAlign': 'center'}),
                                                html.P(id='empregos',
                                                       style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 45,
                                                              'fontWeight': 'bold'}),
                                            ]),
                                        ], color="#F8F8F8", outline=True,
                                            style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                                   'box-shadow': '1px 1px 1px 1px lightgrey', 'height':'160px'}
                                        )
                                    ], xs=12, sm=12, md=12, lg=6, xl=6),
                                dbc.Col(
                                    [
                                        dbc.Card(children=
                                        [
                                            dbc.CardBody(children=
                                            [
                                                html.H6("Saldo empregos formais (12 meses)", className="card-title",
                                                        style={'textAlign': 'center'}),
                                                html.P(id='saldo_empregos12',
                                                       style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 40,
                                                              'fontWeight': 'bold', 'margin-bottom': 0, 'margin-top':0}),
                                                html.P(id='var_emprego',
                                                       style={'color': '#f94144', 'textAlign': 'center',
                                                              'margin-top':0, 'margin-bottom': 0, 'fontSize': 20,
                                                              'fontWeight': 'bold'}),
                                            ]
                                            ),
                                        ], color="#F8F8F8", outline=True,
                                            style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                                   'box-shadow': '1px 1px 1px 1px lightgrey', 'height':'160px'})
                                    ], xs=12, sm=12, md=12, lg=6, xl=6),
                            ],
                                align='center'
                            ),
                            html.Br(),
                            dbc.Row(
                                [
                                    dbc.Col(dcc.Graph(id='evolucao_empregos'), style={'marginBottom': '10px'}, xs=12,
                                            sm=12, md=12, lg=12, xl=12),
                                    dbc.Col(dcc.Graph(id='rem_setor'), style={'marginBottom': '10px'}, xs=12,
                                            sm=12, md=12, lg=12, xl=12),
                                    dbc.Col(dcc.Graph(id='vinculos_subsetor'), style={'marginBottom': '10px'}, xs=12,
                                            sm=12, md=12, lg=12, xl=12),
                                    dbc.Col(dcc.Graph(id='saldo_subsetor'), style={'marginBottom': '10px'}, xs=12,
                                            sm=12, md=12, lg=12, xl=12),
                                    dbc.Col([
                                        dcc.Graph(id='top_vinculos'),
                                        dbc.Button(
                                            "Abrir tabela com quantidade de vínculos de todas as ocupações",
                                            id="open-body-scroll",
                                            className="mt-2",
                                            color="dark",
                                        ),
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader("Tabela"),
                                                dbc.ModalBody(id="table"),
                                                dbc.ModalFooter(
                                                    dbc.Button(
                                                        "Fechar",
                                                        id="close-body-scroll",
                                                        className="ml-auto",
                                                        n_clicks=0,
                                                    )
                                                ),
                                            ],
                                            id="modal-body-scroll",
                                            scrollable=True,
                                            size="lg",
                                            is_open=False,
                                        ),
                                    ], style={'marginBottom': '10px'}, xs=12, sm=12, md=12, lg=12, xl=12),
                                ], align='center', justify="center",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col([
                                        html.P(
                                            [
                                                html.Span(
                                                    className="far fa-lightbulb",
                                                    id="tooltip-target",
                                                    style={'fontSize': 20, "cursor": "pointer", 'color': '#fb8500',
                                                           'padding-left': '10px', 'padding-top': '7px'},
                                                ),
                                            ], style={'background-color': 'white', 'margin-bottom': 0}
                                        ),
                                        dbc.Tooltip(
                                            "Veja as ocupações que vêm absorvendo mais gente no mercado de trabalho formal. "
                                            "Pode ser uma boa ideia investir na capacitação de pessoas para trabalhar nessas ocupações.",
                                            target="tooltip-target",
                                        ),
                                        dcc.Graph(id='saldo_ocupacao', config={'responsive': True}),
                                        dbc.Button(
                                            "Abrir tabela com saldo de empregos formais de todas as ocupações",
                                            id="open-body-scroll2", n_clicks=0,
                                            className="mt-2",
                                            color="dark",
                                        ),
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader("Tabela"),
                                                dbc.ModalBody(id="table3"),
                                                dbc.ModalFooter(
                                                    dbc.Button(
                                                        "Fechar",
                                                        id="close-body-scroll2",
                                                        className="ml-auto",
                                                        n_clicks=0,
                                                    )
                                                ),
                                            ],
                                            id="modal-body-scroll2",
                                            scrollable=True,
                                            size="lg",
                                            is_open=False,
                                        ),

                                    ], style={'marginBottom': '10px'}, xs=12, sm=12, md=12,
                                        lg=12, xl=12),
                                    dbc.Col([
                                        # dcc.Graph(id='remuneracao', config={'responsive': True}),
                                        dbc.Button(
                                            "Abrir tabela com remuneração média de todas as ocupações",
                                            id="open-body-scroll1", n_clicks=0,
                                            className="mt-2",
                                            color="dark",
                                        ),
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader("Tabela"),
                                                dbc.ModalBody(id="table2"),
                                                dbc.ModalFooter(
                                                    dbc.Button(
                                                        "Fechar",
                                                        id="close-body-scroll1",
                                                        className="ml-auto",
                                                        n_clicks=0,
                                                    )
                                                ),
                                            ],
                                            id="modal-body-scroll1",
                                            scrollable=True,
                                            size="lg",
                                            is_open=False,
                                        ),
                                    ], style={'marginBottom': '10px'}, xs=12, sm=12, md=12, lg=12, xl=12),
                                ], align='center', justify="center"),
                            html.Br(),
                                ], xs=12, sm=12, md=12, lg=6, xl=6),
                        dbc.Col(
                            [
                                dbc.Row(children=
                                [
                                    dbc.Col(
                                        [
                                            dbc.Card(children=
                                            [
                                                dbc.CardBody(children=
                                                [
                                                    html.H5("Situação de trabalho das pessoas inscritas no Cadastro Único", className="card-title",
                                                            style={'textAlign': 'center', 'fontWeight':'bold'}),
                                                    html.P(
                                                        'As informações sobre a situação de trabalho das pessoas inscritas no Cadastro Único são coletadas de pessoas '
                                                        'de 14 anos de idade ou mais e, para os propósitos do Cadastro Único, é considerado trabalho tanto o exercício '
                                                        'de atividades remuneradas quanto o exercício de atividades não remuneradas. Ressalta-se que também não é feita distinção '
                                                        'entre emprego formal e informal.',
                                                        style={'textAlign': 'justify', 'opacity': .7, 'fontSize': 15}),
                                                ]),
                                            ], color="#F8F8F8", outline=True,
                                                style={"width": "100%", 'border': 'white', 'marginBottom': '30px',
                                                       'box-shadow': '1px 1px 1px 1px lightgrey', 'heigth':'130px'}
                                            )
                                        ], xs=12, sm=12, md=12, lg=12, xl=12),
                                    dbc.Col(
                                        [
                                            dbc.Card(children=
                                            [
                                                dbc.CardBody(children=
                                                [
                                                    html.H5(id='trabalho_12meses',
                                                           style={'color': '#1351B4', 'textAlign': 'center',
                                                                  'fontSize': 50,
                                                                  'fontWeight': 'bold'}),
                                                    html.P("não trabalharam nos últimos 12 meses",
                                                           style={'textAlign': 'center', 'fontSize': 20, 'fontWeight': 'bold'}),
                                                ]),
                                            ], color="#F8F8F8", outline=True,
                                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                                       'box-shadow': '1px 1px 1px 1px lightgrey', 'height':'160px'}
                                            )
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                    dbc.Col(
                                        [
                                            dbc.Card(children=
                                            [
                                                dbc.CardBody(children=
                                                [
                                                    html.H5(id='trabalho_lastweek',
                                                           style={'color': '#1351B4', 'textAlign': 'center',
                                                                  'fontSize': 50,
                                                                  'fontWeight': 'bold'}),
                                                    html.P('não trabalharam na última semana',
                                                           style={'textAlign': 'center', 'margin-top': '5px', 'margin-bottom': 0,
                                                                  'fontSize': 20, 'fontWeight': 'bold'}),
                                                ]
                                                ),
                                            ], color="#F8F8F8", outline=True,
                                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                                       'box-shadow': '1px 1px 1px 1px lightgrey', 'height':'160px'})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                ],
                                    align='center'
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Col(dcc.Graph(id='funcao_principal'), style={'marginBottom': '10px'}, xs=12,
                                                sm=12, md=12, lg=12, xl=12),
                                        dbc.Col(dcc.Graph(id='mei', config={'responsive': True}), xs=12, sm=12, md=12, lg=12, xl=12)
                                    ],
                                    align='center', justify="center",
                                ),
                                html.Br(),
                            ], xs=12, sm=12, md=12, lg=6, xl=6
                        ),
                    ],
                ),
            ], fluid=True
            )
        elif active_tab == "educacao":
            return dbc.Container(children=[
                html.Br(),
                dbc.Row(children=
                [
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H5("Sobre os dados", className="card-title",
                                            style={'textAlign': 'center', 'fontWeight':'bold'}),
                                    html.P(
                                        'Os dados de distorção idade-série, evasão escolar e de remuneração média dos docentes da educação '
                                        'básica foram obtidos da página de indicadores educacionais do Instituto Nacional de Estudos e Pesquisas Educacionais'
                                        'Anísio Teixeira (INEP).',
                                        style={'textAlign': 'justify', 'opacity': .7, 'fontSize': 15}),
                                ]),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    html.Br(),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H5("Taxa de Distorção Idade-Série", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='idade_serie',
                                           style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 40,
                                                  'fontWeight': 'bold'}),
                                    html.P(id='idade_serie_brasil',
                                           style={'textAlign': 'center', 'fontSize': 20,
                                                  'fontWeight': 'bold'}),
                                    dbc.Button("Conheça o indicador", id="open_distorcao", n_clicks=0, color="primary", size='sm'),
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader("Taxa de Distorção Idade-Série"),
                                            dbc.ModalBody("A distorção idade-série é o indicador educacional que permite acompanhar o "
                                           "percentual de alunos, em cada série, que têm idade acima da esperada "
                                           "para o ano em que estão matriculados. Quanto menor a taxa, melhor a situação do sistema educacional."),
                                            dbc.ModalFooter(
                                                dbc.Button(
                                                    "Fechar", id="close_distorcao", className="ml-auto", n_clicks=0
                                                )
                                            ),
                                        ],
                                        id="modal_distorcao",
                                        is_open=False,
                                    ),
                                ]),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H5("Taxa de Evasão Escolar", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='evasao',
                                           style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 40,
                                                  'fontWeight': 'bold'}),
                                    html.P(id='evasao_brasil',
                                           style={'textAlign': 'center', 'fontSize': 20,
                                                  'fontWeight': 'bold'}),
                                    dbc.Button("Conheça o indicador", id="open_evasao", n_clicks=0, color="primary", size='sm'),
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader("Taxa de Evasão Escolar"),
                                            dbc.ModalBody("A taxa de evasão é um indicador de fluxo escolar de estudantes da educação básica"
                                                          "brasileira que avalia a permanência dos alunos no sistema educacional. Indicadores de fluxo escolar "
                                                          "avaliam a transição do aluno entre dois anos consecutivos considerando os seguintes cenários "
                                                          "possíveis: promoção, repetência, migração para EJA e evasão escolar.\n\n "
                                                          "No caso da taxa de evasão, quanto menor o indicador, menor o percentual de alunos que abandonaram o sistema educacional."),
                                            dbc.ModalFooter(
                                                dbc.Button(
                                                    "Fechar", id="close_evasao", className="ml-auto", n_clicks=0
                                                )
                                            ),
                                        ],
                                        id="modal_evasao",
                                        is_open=False,
                                        style={'whiteSpace': 'pre-wrap'},
                                    ),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey'})
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("Remuneração média dos docentes", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='rem_docentes_munic',
                                           style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 40,
                                                  'fontWeight': 'bold'}),
                                    html.P(id='rem_docentes_brasil',
                                           style={'textAlign': 'center', 'fontSize': 20,
                                                  'fontWeight': 'bold'}),
                                    dbc.Button("Saiba mais", id="open_rem", n_clicks=0, color="primary",
                                               size='sm'),
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader("Remuneração média dos docentes"),
                                            dbc.ModalBody([
                                                "Para o cálculo da remuneração média dos docentes da educação básica foi utilizada uma metodologia de pareamento de dados do "
                                                "Censo da Educação Básica e da Relação Anual de Informações Sociais (RAIS). Com isso, chegou-se à remuneração mensal bruta e padronizada para uma carga horária "
                                                "de 40 horas semanais, dos docentes em exercício em sala de aula, por dependência administrativa (federal, estadual, "
                                                "municipal e privada) e para diferentes níveis de agregação (município, UF, grandes regiões e Brasil)\n\n "
                                                "Para maiores detalhes, consulte a ",
                                                html.A('página do INEP.',
                                                       href="https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/remuneracao-media-dos-docentes",
                                                       target="_blank"),
                                            ]),
                                            dbc.ModalFooter(
                                                dbc.Button(
                                                    "Fechar", id="close_rem", className="ml-auto", n_clicks=0
                                                )
                                            ),
                                        ],
                                        id="modal_rem",
                                        style={'whiteSpace': 'pre-wrap'},
                                        is_open=False,
                                    ),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey'})
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                ],
                    align='center'
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col(dcc.Graph(id='escolaridade', config={'responsive': True}), style={'marginBottom': '10px'},
                            xs=12, sm=12, md=12, lg=6, xl=7),
                    dbc.Col(dcc.Graph(id='analfabetismo', config={'responsive': True}), style={'fontFamily':'Open Sans'}, xs=12, sm=12, md=12, lg=6,
                            xl=5),
                ]
                ),
                html.Br(),
            ], fluid=True
            )
        elif active_tab == "economia":
            return dbc.Container(children=[
                html.Br(),
                dbc.Row(children=
                [
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("População estimada (2020)", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='populacao',
                                           style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 30,
                                                  'fontWeight': 'bold', 'marginBottom': '15px'}),
                                    dbc.Button("Saiba mais", id="open_pop", n_clicks=0, color="primary", size='sm'),
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader("Sobre a estimativa da população"),
                                            dbc.ModalBody([
                                                "As estimativas de população são publicadas anualmente pelo IBGE. O método utiliza como insumos básicos as populações "
                                                "obtidas das Projeções da População para o Brasil e as Unidades da Federação mais recentes, bem como o crescimento populacional "
                                                "de cada Município na última década, delineado pelas respectivas populações recenseadas nos dois últimos Censos Demográficos realizados.\n\n "
                                                "Essas populações recenseadas, que servem de base para o cálculo da tendência de crescimento populacional dos Municípios, "
                                                "podem ser ajustadas em consonância com os ajustes da população adotados nas Projeções da População para o Brasil e as Unidades da Federação.\n\n"
                                                "Saiba mais no site do ",
                                            html.A('IBGE.',
                                                   href="https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html?=&t=o-que-e",
                                                   target="_blank")]),
                                            dbc.ModalFooter(
                                                dbc.Button(
                                                    "Fechar", id="close_pop", className="ml-auto", n_clicks=0
                                                )
                                            ),
                                        ],
                                        id="modal_pop",
                                        is_open=False,
                                        style={"width": "100%", 'whiteSpace': 'pre-wrap'},
                                    ),
                                ]),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey', 'height':'160px'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("PIB Total (2018)", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='pib_total',
                                           style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 30,
                                                  'fontWeight': 'bold', 'marginBottom': '15px'}),
                                    dbc.Button("Saiba mais", id="open_pib", n_clicks=0, color="primary", size='sm'),
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader("Sobre a estimativa da população"),
                                            dbc.ModalBody([
                                                "O PIB é a soma de todos os bens e serviços finais produzidos por um país, estado ou cidade, geralmente em um ano. "
                                                "Todos os países calculam o seu PIB nas suas respectivas moedas.\n\n"
                                                "O IBGE, em parceria com os Órgãos Estaduais de Estatística, as Secretarias Estaduais de Governo e a Superintendência da Zona Franca de Manaus - Suframa,"
                                                " divulga as estimativas do Produto Interno Bruto - PIB dos Municípios - referência 2010, sendo o último dado disponível referente a 2018. "
                                                "Os resultados são comparáveis entre si e estão completamente integrados às séries das Contas Nacionais e das Contas Regionais do Brasil, "
                                                "em conformidade, portanto, com o novo manual System of national accounts 2008, SNA 2008, e com a Classificação Nacional de Atividades Econômicas - CNAE 2.0.\n\n"
                                                "São apresentados, a preços correntes, os valores adicionados brutos dos três grandes setores de atividade econômica – Agropecuária, "
                                                "Indústria e Serviços – bem como os impostos, líquidos de subsídios, o PIB e o PIB per capita.\n\n "
                                                "Destaca-se o valor adicionado bruto da Administração, saúde e educação públicas e seguridade social, devido à relevância deste segmento "
                                                "na economia municipal. A análise dos resultados, ilustrada por meio de tabelas, quadros, gráficos e cartogramas, "
                                                "enfoca aspectos econômicos de abrangência nacional, regional e municipal.\n\n "
                                                "Saiba mais sobre o PIB no site do ",
                                                html.A('IBGE.',
                                                       href="https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=o-que-e",
                                                       target="_blank")]),
                                            dbc.ModalFooter(
                                                dbc.Button(
                                                    "Fechar", id="close_pib", className="ml-auto", n_clicks=0
                                                )
                                            ),
                                        ],
                                        id="modal_pib",
                                        is_open=False,
                                        style={"width": "100%", 'whiteSpace': 'pre-wrap'},
                                    ),
                                ]),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey', 'height':'160px'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("Índice Vulnerabilidade Social", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='ivs',
                                           style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 30,
                                                  'fontWeight': 'bold', 'marginBottom': '15px'}),
                                    dbc.Button("Conheça o índice", id="open_ivs", n_clicks=0, color="primary", size='sm'),
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader("Sobre o IVS"),
                                            dbc.ModalBody([
                                                "A partir do estudo do conceito de vulnerabilidade foram construídos 16 indicadores, que juntos forma o Índice de Vulnerabilidade Social. "
                                                "Esses indicadores estão inseridos em 3 dimensões, sendo elas a 1) infraestrutura urbana; 2) capital humano e 3) renda e trabalho. \n\n"
                                                "O índice varia de 0 a 1 e quanto menor o valor, menor a vulnerabilidade social da localidade. \n\n"
                                                "Saiba mais sobre o Índice e tenha acesso ao Atlas da Vulnerabilidade na plataforma desenvolvida pelo ",
                                                html.A('Instituto de Pesquisa Econômica Aplicada (IPEA).',
                                                       href="http://ivs.ipea.gov.br/index.php/pt/",
                                                       target="_blank")]),
                                            dbc.ModalFooter(
                                                dbc.Button(
                                                    "Fechar", id="close_ivs", className="ml-auto", n_clicks=0
                                                )
                                            ),
                                        ],
                                        id="modal_ivs",
                                        is_open=False,
                                        style={"width": "100%", 'whiteSpace': 'pre-wrap'},
                                    ),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey'})
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("Índice de Desenvolvimento Humano (2010)", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='idhm',
                                           style={'color': '#1351B4', 'textAlign': 'center', 'fontSize': 30,
                                                  'fontWeight': 'bold', 'marginBottom': '15px'}),
                                    dbc.Button("Conheça o índice", id="open_idh", n_clicks=0, color="primary",
                                               size='sm'),
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader("Sobre o IDHM"),
                                            dbc.ModalBody([
                                                "O Índice de Desenvolvimento Humano Municipal (IDHM) é uma medida composta de indicadores de três dimensões do desenvolvimento humano: "
                                                "longevidade, educação e renda. O índice varia de 0 a 1. Quanto mais próximo de 1, maior o desenvolvimento humano da localidade. \n\n"
                                                "O IDHM brasileiro segue as mesmas três dimensões do IDH Global - longevidade, educação e renda, mas vai além: "
                                                "adequa a metodologia global ao contexto brasileiro e à disponibilidade de indicadores nacionais. "
                                                "Embora meçam os mesmos fenômenos, os indicadores levados em conta no IDHM são mais adequados para avaliar o "
                                                "desenvolvimento dos municípios brasileiros. Assim, o IDHM - incluindo seus três componentes, IDHM Longevidade, "
                                                "IDHM Educação e IDHM Renda - conta um pouco da história dos municípios em três importantes dimensões do desenvolvimento "
                                                "humano durantes duas décadas da história brasileira. \n\n",
                                                html.A('Saiba mais sobre o Índice e tenha acesso ao Atlas do Desenvolvimento Humano.',
                                                       href="https://www.br.undp.org/content/brazil/pt/home/idh0/conceitos/o-que-e-o-idhm.html",
                                                       target="_blank")]),
                                            dbc.ModalFooter(
                                                dbc.Button(
                                                    "Fechar", id="close_idh", className="ml-auto", n_clicks=0
                                                )
                                            ),
                                        ],
                                        id="modal_idh",
                                        is_open=False,
                                        style={"width": "100%", 'whiteSpace': 'pre-wrap'},
                                    ),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True,
                                style={"width": "100%", 'border': 'white', 'marginBottom': '5px',
                                       'box-shadow': '1px 1px 1px 1px lightgrey'})
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                ],
                    align='center'
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='pib_setorial'), style={'marginBottom':'10px'}, xs=12, sm=12, md=12, lg=6, xl=4),
                        dbc.Col(dcc.Graph(id='empresas_setorial', config={'responsive':True}), style={'marginBottom':'10px'}, xs=12, sm=12, md=12, lg=6, xl=8)
                    ], className='row flex-display'
                ),
                html.Br(),
            ], fluid=True
            )
        elif active_tab == "servicos":
            return dbc.Container(children=[
                html.Br(),
                dbc.Row(
                    [
                        dbc.CardDeck(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="https://www.seduc.ce.gov.br/wp-content/uploads/sites/37/2020/02/Novos-Caminhos-Preto-1200x813.jpg",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Painel de Demandas por Qualificação Profissional",
                                                        className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "Quais ocupações devem empregar mais gente nos próximos anos no seu município? E quais cursos FIC podem "
                                                    "ser oferecidos para preparar as pessoas para entrar no mercado de trabalho? Veha as sugestões do Painel "
                                                    "de Demandas por Qualificação Profissional. A ferramenta foi desenvolvida pelo Ministério da Educação em "
                                                    "parceria com o Governo do Estado de Minas Gerais.",
                                                    className="card-text",
                                                ),
                                            ]
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Acesse o painel", color="primary", size='sm',
                                                       href='http://novoscaminhos.mec.gov.br/painel-de-demandas/demandas',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden',
                                    style={'box-shadow': '1px 1px 1px 1px lightgrey'},
                                ),
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src='http://portalfat.mte.gov.br/wp-content/uploads/2017/01/MARCA_SISTEMA-NACIONAL-DE-EMPREGO-SINE-01.jpg',
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5('SINE', className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "Serviço de busca de vagas de emprego no Sistema Nacional de Emprego (Sine) e agendamento de entrevista com possíveis empregadores."
                                                    "Pode acessar o serviço ppessoas, acima de 14 anos, que possuem CPF e Carteira de Trabalho e Previdência Social (CTPS).",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Buscar vagas no SINE", color="primary", size='sm',
                                                       href='https://www.gov.br/pt-br/servicos/buscar-emprego-no-sistema-nacional-de-emprego-sine',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden',
                                    style={'box-shadow': '1px 1px 1px 1px lightgrey'}),
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="https://images.unsplash.com/photo-1531545514256-b1400bc00f31?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mzh8fHlvdW5ncyUyMGxlYXJuaW5nfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Cursos de jovem aprendiz", className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "Aprendizagem Profissional é o programa de qualificação profissional e inserção no mercado de trabalho voltado para"
                                                    " jovens de 14 a 24 anos, e para pessoas com deficiência sem limite de idade.\n\n Trata-se de uma política que pode criar "
                                                    "oportunidades tanto para os jovens, especialmente no que se refere à inserção no mercado de trabalho, quanto para "
                                                    "as empresas, que têm a possibilidade de formar mão-de-obra qualificada.",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Acesse a lista de instituições", color="primary", size='sm',
                                                       href='http://blog.mds.gov.br/redesuas/plano-progredir-divulga-lista-de-instituicoes-que-podem-ofertar-curso-de-jovem-aprendiz/',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden',
                                    style={'box-shadow': '1px 1px 1px 1px lightgrey'}
                                ),
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="http://www.mds.gov.br/webarquivos/cidadania/marca_gov/progredir/Marca_Progredir.png",
                                            className='card-img-top',
                                            # style={'height':'30%', 'object-fit':'auto'},
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Plano Progredir", className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "É um plano de ações do Governo Federal para gerar emprego, renda e promover a construção da autonomia das pessoas inscritas "
                                                    "no Cadastro Único para Programas Sociais. O Progredir possui um aplicativo que conta com cursos de qualificação profissional, "
                                                    "vagas de emprego, uma área para elaboração de currículo, e a possibilidade de acessar microcrédito para empreender. "
                                                    "Todos ofertados por parceiros (empresas ou entes públicos) de forma gratuita.", className="card-text",
                                                ),
                                            ]
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Acesse a plataforma do Progredir", color="primary", size='sm',
                                                       href='http://cidadania.gov.br/progredir',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden',
                                    style={'box-shadow': '1px 1px 1px 1px lightgrey'})
                            ]
                        ),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.CardDeck(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="https://github.com/vitorlsantana/progredir_dashboard/blob/main/assets/mei.png?raw=true",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Microeempreendedorismo Individual (MEI)",
                                                        className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "O governo federal disponibiliza um portal com informações para quem deseja se formalizar como microeempreendedor"
                                                    "individual, para quem já está formalizado e deseja o acesso digital a produtos e serviços financeiros.\n\n Além"
                                                    "disso, o portal apresenta a legislação aplicada, estatísticas e cursos gratuitos para quem pretende se formalizar",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Saiba mais sobre o MEI", color="primary", size='sm',
                                                       href='https://www.gov.br/empresas-e-negocios/pt-br/empreendedor',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden',
                                    style={'box-shadow': '1px 1px 1px 1px lightgrey'}
                                ),
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="https://www.gov.br/pt-br/noticias/financas-impostos-e-gestao-publica/2020/03/governo-lanca-plataforma-para-oferta-de-produtos-e-servicos-gratuitos-a-populacao/todos-por-todos_govbr.png/@@images/9ddec400-0381-4d20-a751-28f7f2c1f2b6.png",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Todos por Todos", className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "A página Todos por Todos é uma campanha do Governo Federal para estimular o movimento solidário, "
                                                    "captando ofertas de serviços à população e propostas de doações aos governos, para o enfrentamento "
                                                    "à pandemia do novo coronavírus.", className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Conheça o Todos por Todos", color="primary", size='sm',
                                                       href='http://www.gov.br/pt-br/todosportodos/cursos-ead',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden',
                                    style={'box-shadow': '1px 1px 1px 1px lightgrey'}
                                ),
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="https://static.wixstatic.com/media/eafbd4_ae1f1ee9b9924e2397246a5e609880bb~mv2.jpg/v1/fit/w_828%2Ch_371%2Cal_c%2Cq_80/file.jpg",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Escola do Trabalhador 4.0", className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "A Escola do Trabalhador 4.0 é uma iniciativa do Ministério da Economia realizada em parceria com a Microsoft "
                                                    "para promoção de qualificação e inserção profissional."
                                                    "Trata-se de um programa de qualificação profissional que oferece cursos gratuitos em temas de tecnologia e produtividade. "
                                                    "Com o objetivo de ajudar o trabalhador brasileiro a se preparar para o mercado de trabalho.",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Acesse a plataforma", color="primary", size='sm',
                                                       href='https://empregamais.economia.gov.br/escoladotrabalhador40/',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden', style={'box-shadow': '1px 1px 1px 1px lightgrey'}
                                ),
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="http://utramig.mg.gov.br/wp-content/uploads/2021/03/Qualifica-_emprega-.png",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Qualifica Emprega +", className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "Qualifica Mais é uma parceria com o Ministério da Educação para a oferta de cursos de qualificação profissional, "
                                                    "à distância, na área de Tecnologia da Informação e Comunicação.",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Acesse o site", color="primary", size='sm',
                                                       href='https://www.gov.br/mec/pt-br/acesso-a-informacao/institucional/secretarias/secretaria-de-educacao-profissional/projeto-piloto-qualifica-mais',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden', style={'box-shadow': '1px 1px 1px 1px lightgrey'}
                                ),
                            ]
                        ),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.CardDeck(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="https://infosolda.com.br/wp-content/uploads/2021/01/senai.png",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Aprendizagem 4.0 / Mundo SENAI", className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "O Aprendizagem 4.0 é um programa que busca qualificar jovens de 14 a 24 anos por "
                                                    "meio de um currículo que contempla as competências técnicas e socioemocionais exigidas pela Indústria 4.0, "
                                                    "importantes no mundo do trabalho atual. A iniciativa é uma experiência do SENAI e conta com a "
                                                    "parceria da Secretaria Especial de Produtividade, Emprego e Produtividade do Ministério da Economia, "
                                                    "com o objetivo de estruturar novos modelos de oferta de aprendizagem para a economia 4.0.",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Acesse a plataforma", color="primary", size='sm',
                                                       href='https://mundosenai.com.br/aprendizagem40/',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden', style={'box-shadow': '1px 1px 1px 1px lightgrey'}
                                ),
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="https://aliancaempreendedora.org.br/bar/logo-alianca.svg",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Aliança Empreendedora", className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "Trata-se de uma iniciativa que busca apoiar empresas, organizações sociais e governos a desenvolver "
                                                    "modelos de negócios inclusivos e projetos de apoio a microempreendedores de baixa renda, "
                                                    "ampliando o acesso a conhecimento, redes, mercados e crédito para que desenvolvam ou iniciem seus empreendimentos",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Acesse o site e conheça", color="primary", size='sm',
                                                       href='https://aliancaempreendedora.org.br/',
                                                       target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden', style={'box-shadow': '1px 1px 1px 1px lightgrey'}
                                ),
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="http://rme.net.br/wp-content/uploads/2018/11/esbo%C3%A7o-logo-irme-1-1024x545.png",
                                            className='card-img-top',
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.H5("Instituto Rede Mulher Empreendedora (IRME)", className="card-title", style={'fontWeight': 'bold'}),
                                                html.P(
                                                    "O IRME é uma organização que tua no fomento à geração de renda da mulher, através do empreendedorismo e empregabilidade. "
                                                    "Desenvolve projetos e capacitações para mulheres em todo o Brasil, tendo como objetivo principal garantir independência "
                                                    "financeira e de decisão sobre seus negócios e vidas.",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                        dbc.CardFooter(
                                            dbc.Button("Acesse o site e conheça", color="primary", size='sm',
                                                       href='https://institutorme.org.br/', target="_blank"), style={'background-color':'white'}
                                        )
                                    ], className='card overflow-hidden', style={'box-shadow': '1px 1px 1px 1px lightgrey'}),
                            ]
                        ),
                    ]
                ),
            ], fluid=True
            )
        elif active_tab == "estudos":
            return dbc.Container(children=[
                html.Br(),
                dbc.Row(children=
                [
                    dbc.Col([
                        html.Div(children=
                        [
                            html.Img(
                                src='https://aupa.com.br/wp-content/uploads/2020/03/arymax.jpg',
                                style={'height': '100%', 'width': '120px', 'object-fit': 'cover'}),
                            html.Div([
                                html.H2("Inclusão Produtiva no Brasil",
                                        style={'font-size': '20px', 'font-weight': 'bold', 'margin': 0}
                                        ),
                                html.P(
                                    "O estudo traz um panorama sobre o tema da inclusão produtiva no Brasil e no mundo, seus principais desafios, atores envolvidos, "
                                    "assim como as mais promissoras soluções e grandes tendências.",
                                    style={'font-size': '15px', 'opacity': .7, 'margin-bottom': '10px',
                                           'margin-top': '10px'}
                                ),
                                dbc.Button("Acesse o estudo", outline=True, color="info", size='sm',
                                           href='https://arymax.org.br/conhecimento/inclusaoprodutivanobrasil/',
                                           target="_blank"),
                            ],
                                style={'padding': '16px'}
                            ),
                        ], style={'overflow': 'hidden', 'background': 'white', 'box-shadow': '0 0 15px rgba(0,0,0,0.2)', 'border-radius':'5px',
                                  'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px', 'width': '100%'}
                        ),
                        html.Div(children=
                        [
                            html.Img(
                                src='https://github.com/vitorlsantana/progredir_dashboard/blob/main/assets/o%20futuro%20da%20inclus%C3%A3o%20produtiva%20no%20brasil.png?raw=true',
                                style={'height': '100%', 'width': '120px',
                                       'object-fit': 'cover'}),
                            html.Div([
                                html.H2("O futuro da inclusão produtiva no Brasil",
                                        style={'font-size': '20px', 'font-weight': 'bold', 'margin': 0}
                                        ),
                                html.P(
                                    "O estudo nasceu do reconhecimento de que as ações emergenciais empreendidas para lidar com o desafio "
                                    "social desencadeado pela pandemia deveriam ser complementadas com uma reflexão profunda sobre o período "
                                    "que virá depois. Dessa forma, a publicação traz pensamentos que ajudam a compreender as características "
                                    "da crise, para onde ela está nos levando e quais políticas foram criadas para combatê-la. Por fim, aponta "
                                    "alternativas de enfrentamento desses desafios no pós-pandemia.",
                                    style={'font-size': '15px', 'opacity': .7, 'margin-bottom': '10px',
                                           'margin-top': '8px'}
                                    ),
                                dbc.Button("Acesse o estudo", outline=True, color="info", size='sm',
                                           href='https://arymax.org.br/conhecimento/inclusaoprodutivanobrasil/novo-estudo-inclusao-produtiva/',
                                           target="_blank"),
                            ],
                                style={'padding': '16px'}
                            ),
                        ], style={'overflow': 'hidden', 'background': 'white', 'box-shadow': '0 0 15px rgba(0,0,0,0.2)', 'border-radius':'5px',
                                  'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px', 'width': '100%'}
                        ),
                        html.Div(children=
                        [
                            html.Img(
                                src='https://github.com/vitorlsantana/progredir_dashboard/blob/main/assets/serie%20wwp.png?raw=true',
                                style={'height': '100%', 'width': '120px',
                                       'object-fit': 'cover'}),
                            html.Div([
                                html.H2("Série de estudos de caso de inclusão produtiva urbana no Brasil",
                                        style={'font-size': '20px', 'font-weight': 'bold', 'margin': 0}
                                        ),
                                html.P(
                                    "A série WWP de Estudos de Caso traz publicações dedicadas exclusivamente ao tema de inclusão produtiva, "
                                    "mostrando iniciativas que colaboram para o aumento da autonomia de famílias brasileiras em diferentes partes do país, "
                                    "de forma a enfrentar vulnerabilidades e aumentar a qualidade de vida.A série mostra também os desafios encarados "
                                    "pelos gestores públicos na implementação dessas políticas, assim como os limites de cada programa e intervenção. "
                                    "Cada documento acompanha um vídeo dinâmico e explicativo.",
                                    style={'font-size': '15px', 'opacity': .7, 'margin-bottom': '10px', 'margin-top': '8px'}
                                    ),
                                dbc.Button("Acesse o estudo", outline=True, color="info", size='sm',
                                           href='https://wwp.org.br/politica-social/inclusao-produtiva/',
                                           target="_blank"),
                            ],
                                style={'padding': '16px'}
                            ),
                        ], style={'overflow': 'hidden', 'background': 'white', 'box-shadow': '0 0 15px rgba(0,0,0,0.2)', 'border-radius':'5px',
                                  'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px', 'width': '100%'}
                        ),
                        html.Div(children=
                        [
                            html.Img(
                                src='https://openknowledge.worldbank.org/bitstream/handle/10986/18031/9781464802027.pdf.jpg?sequence=4&isAllowed=y',
                                style={'height': '100%', 'width': '120px', 'object-fit': 'cover'}),
                            html.Div([
                                html.H2("Entrepreneurship Education and Training Programs around the World",
                                        style={'font-size': '20px', 'font-weight': 'bold', 'margin': 0}
                                        ),
                                html.P(
                                    "O estudo analisa um conjunto de intervenções relacionadas a qualificação empreendedora, que inclui atividades "
                                    "de transmissão de mentalidades e habilidades específicas associadas ao empreendedorismo, bem como programas de "
                                    "educação e formação que visem gerar resultados de empreendedorismo. O objetivo deste estudo é identificar e "
                                    "organizar o cenário da qualificação empreendedora, tipos de programa, bem como as dimensões que moldam os resultados. "
                                    "O estudo descreve um conjunto de ideias práticas sobre o desenho e implementação de programas, resultados pretendidos, e contextos.",
                                    style={'font-size': '15px', 'opacity': .7, 'margin-bottom': '10px',
                                           'margin-top': '8px'}
                                    ),
                                dbc.Button("Acesse o estudo", outline=True, color="info", size='sm',
                                           href='https://openknowledge.worldbank.org/handle/10986/34917',
                                           target="_blank"),
                            ],
                                style={'padding': '16px'}
                            ),
                        ], style={'overflow': 'hidden', 'background': 'white',
                                  'box-shadow': '0 0 15px rgba(0,0,0,0.2)', 'margin-bottom': '20px', 'width': '100%',
                                  'border-radius': '5px', 'display': 'flex', 'align-items': 'center'}
                        ),
                        html.Div(children=
                        [
                            html.Img(
                                src='http://www.grade.org.pe/wp-content/uploads/hakuwinay_perspective2-600x352.jpg',
                                style={'height': '100%', 'width': '120px', 'object-fit': 'cover'}),
                            html.Div([
                                html.H2("Combinando protección social con generación de oportunidades económicas: una evaluación de los avances del programa Haku Wiñay",
                                        style={'font-size': '20px', 'font-weight': 'bold', 'margin': 0}
                                        ),
                                html.P(
                                    "O objetivo do estudo é fornecer evidências dos impactos iniciais que o projeto Mi Chacra Emprendedora-Haku Wiñay, no Peru, teve em "
                                    "uma amostra representativa de suas áreas de intervenção na zona rural. O trabalho situa o projeto no marco de "
                                    "intervenções que combinam programas de desenvolvimento produtivo com política social.",
                                    style={'font-size': '15px', 'opacity': .7, 'margin-bottom': '10px',
                                           'margin-top': '8px'}
                                ),
                                dbc.Button("Acesse o estudo", outline=True, color="info", size='sm',
                                           href='http://www.grade.org.pe/wp-content/uploads/LIBROGRADE_FORDHakuWinay.pdf',
                                           target="_blank"),
                            ],
                                style={'padding': '16px'}
                            ),
                        ], style={'overflow': 'hidden', 'background': 'white',
                                  'box-shadow': '0 0 15px rgba(0,0,0,0.2)', 'margin-bottom': '20px', 'width': '100%',
                                  'border-radius': '5px', 'display': 'flex', 'align-items': 'center'}
                        ),
                        ]
                    ),
                    dbc.Col([
                        html.Div(children=
                        [
                            html.Img(
                                src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_sqsm9EW7NYtDqpbbWxCzs-zwZVWk_2a-1A&usqp=CAU',
                                style={'height': '100%', 'width': '120px',
                                       'object-fit': 'cover'}),
                            html.Div([
                                html.H2("The State of Economic Inclusion Report 2021",
                                        style={'font-size': '20px', 'font-weight': 'bold', 'margin': 0}
                                        ),
                                html.P(
                                    "O Relatório lança luz sobre um dos maiores desafios enfrentados pelos formuladores de políticas de desenvolvimento:"
                                    "transformar a vida econômica das pessoas mais pobres e vulneráveis do mundo. O relatório fornece uma avaliação global "
                                    "sobre programas de inclusão econômica direcionados para os extremamente pobres e vulneráveis."
                                    "Com base nas experiências de mais de 75 países, o relatório considera a viabilidade de se ampliar em escala programas de inclusão econômica."
                                    "Este relatório estabelece uma linha de base para programas de inclusão econômica global.",
                                    style={'font-size': '15px', 'opacity': .7, 'margin-bottom': '10px', 'margin-top': '8px'}
                                    ),
                                dbc.Button("Acesse o estudo", outline=True, color="info", size='sm',
                                           href='https://www.peiglobal.org/state-of-economic-inclusion-report-2021',
                                           target="_blank"),
                            ],
                                style={'padding': '16px'}
                            ),
                        ], style={'overflow': 'hidden', 'background': 'white', 'box-shadow': '0 0 15px rgba(0,0,0,0.2)', 'border-radius':'5px',
                                  'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px', 'width': '100%'}
                        ),
                        html.Div(children=
                        [
                            html.Img(
                                src='https://blogs.worldbank.org/sites/default/files/voices/okr_stack_logo_300px.jpg',
                                style={'height': '100%', 'width': '120px',
                                       'object-fit': 'cover'}),
                            html.Div([
                                html.H2("USAID State of the Field Report: Examining the Evidence in Youth Workforce Development",
                                        style={'font-size': '20px', 'font-weight': 'bold', 'margin': 0}
                                        ),
                                html.P("O Relatório lança luz sobre um dos desafios mais difíceis enfrentados pelos formuladores de políticas de desenvolvimento: transformar a vida "
                                       "econômica das pessoas mais pobres e vulneráveis do mundo. O relatório apresenta dados e evidências de 219 programas de inclusão econômica, "
                                       "que atingem mais de 90 milhões de beneficiários. O relatório oferece quatro contribuições importantes: 1) Uma análise detalhada da natureza desses programas, "
                                       "das pessoas que vivem em extrema pobreza e vulnerabilidade a quem apoiam e dos desafios e oportunidades organizacionais "
                                       "inerentes à sua concepção e liderança; 2) Uma revisão de evidências de 80 avaliações quantitativas e qualitativas de "
                                       "programas de inclusão econômica em 37 países; 3) O primeiro estudo de custo de vários países, incluindo programas liderados "
                                       "pelo governo e outros programas de inclusão econômica, indicando que os programas mostram potencial para eficiência de custos "
                                       "quando integrados aos sistemas nacionais; e 4) Quatro estudos de caso detalhados sobre programas em andamento em Bangladesh, "
                                       "Índia, Peru e Sahel, que destacam as adaptações programáticas e institucionais necessárias para dar escalar em contextos bastante diversos.",
                                       style={'font-size': '15px', 'opacity': .7, 'margin-bottom': '10px',
                                              'margin-top': '8px'}
                                       ),
                                dbc.Button("Acesse o estudo", outline=True, color="info", size='sm',
                                           href='https://openknowledge.worldbank.org/bitstream/handle/10986/18031/9781464802027.pdf?sequence=1&isAllowed=y ',
                                           target="_blank"),
                            ],
                                style={'padding': '16px'}
                            ),
                        ], style={'overflow': 'hidden', 'background': 'white',
                                  'box-shadow': '0 0 15px rgba(0,0,0,0.2)', 'margin-bottom': '20px', 'width': '100%', 'border-radius':'5px',
                                  'display': 'flex', 'align-items': 'center'}
                        ),
                        html.Div(children=
                        [
                            html.Img(
                                src='https://i.pinimg.com/originals/20/ae/71/20ae718e7da5583f22ab4a325a988124.png',
                                style={'height': '100%', 'width': '120px',
                                       'object-fit': 'cover'}),
                            html.Div([
                                html.H2(
                                    "The Impact of an Adolescent Girls Employment Program",
                                    style={'font-size': '20px', 'font-weight': 'bold', 'margin': 0}
                                    ),
                                html.P(
                                    "O artigo apresenta resultados da avaliação de impacto do projeto de Empoderamento Econômico de Meninas Adolescentes e Mulheres Jovens (EPAG) na Libéria. "
                                    "O projeto EPAG foi lançado pelo Ministério de Gênero e Desenvolvimento da Libéria em 2009 com o objetivo de aumentar o emprego e a renda de 2.500 jovens "
                                    "mulheres liberianas, proporcionando meios de subsistência e treinamento em habilidades para a vida e facilitando sua transição para o trabalho produtivo. "
                                    "O estudo mostra que o programa aumentou o emprego em 47% e os ganhos em 80%. Além disso, a avaliação de impacto documenta efeitos positivos em uma "
                                    "variedade de medidas de empoderamento, incluindo acesso a dinheiro, autoconfiança e ansiedade sobre as circunstâncias e o futuro.",
                                    style={'font-size': '15px', 'opacity': .7, 'margin-bottom': '10px',
                                           'margin-top': '8px'}
                                    ),
                                dbc.Button("Acesse o estudo", outline=True, color="info", size='sm',
                                           href='https://documents.worldbank.org/en/publication/documents-reports/documentdetail/610391468299085610/the-impact-of-an-adolescent-girls-employment-program-the-epag-project-in-liberia',
                                           target="_blank"),
                            ],
                                style={'padding': '16px'}
                            ),
                        ], style={'overflow': 'hidden', 'background': 'white',
                                  'box-shadow': '0 0 15px rgba(0,0,0,0.2)', 'margin-bottom': '20px', 'width': '100%',
                                  'border-radius': '5px',
                                  'display': 'flex', 'align-items': 'center'}
                        ),
                    ]
                    ),
                ],
                ),
            ], fluid=True
            )
    return "No tab selected"

@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button2", "n_clicks")],
    [State("collapse2", "is_open")],
)
def toggle_collapse2(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse3", "is_open"),
    [Input("collapse-button3", "n_clicks")],
    [State("collapse3", "is_open")],
)
def toggle_collapse3(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse4", "is_open"),
    [Input("collapse-button4", "n_clicks")],
    [State("collapse4", "is_open")],
)
def toggle_collapse4(n, is_open):
    if n:
        return not is_open
    return is_open

# MODAL CADASTRO ÚNICO
@app.callback(
    Output("modal1", "is_open"),
    [Input("open1", "n_clicks"), Input("close1", "n_clicks")],
    [State("modal1", "is_open")],
)
def toggle_modal1(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# MODAL EDUCAÇÃO
@app.callback(
    Output("modal_evasao", "is_open"),
    [Input("open_evasao", "n_clicks"), Input("close_evasao", "n_clicks")],
    [State("modal_evasao", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal_distorcao", "is_open"),
    [Input("open_distorcao", "n_clicks"), Input("close_distorcao", "n_clicks")],
    [State("modal_distorcao", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal_rem", "is_open"),
    [Input("open_rem", "n_clicks"), Input("close_rem", "n_clicks")],
    [State("modal_rem", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# MODAL CONTEXTO SOCIOECONOMICO
@app.callback(
    Output("modal_pop", "is_open"),
    [Input("open_pop", "n_clicks"), Input("close_pop", "n_clicks")],
    [State("modal_pop", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal_pib", "is_open"),
    [Input("open_pib", "n_clicks"), Input("close_pib", "n_clicks")],
    [State("modal_pib", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal_ivs", "is_open"),
    [Input("open_ivs", "n_clicks"), Input("close_ivs", "n_clicks")],
    [State("modal_ivs", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal_idh", "is_open"),
    [Input("open_idh", "n_clicks"), Input("close_idh", "n_clicks")],
    [State("modal_idh", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#MODAL TABELAS RAIS
@app.callback(
    Output("modal-body-scroll", "is_open"),
    [
        Input("open-body-scroll", "n_clicks"),
        Input("close-body-scroll", "n_clicks"),
    ],
    [State("modal-body-scroll", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modal-body-scroll1", "is_open"),
    [
        Input("open-body-scroll1", "n_clicks"),
        Input("close-body-scroll1", "n_clicks"),
    ],
    [State("modal-body-scroll1", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal-body-scroll2", "is_open"),
    [
        Input("open-body-scroll2", "n_clicks"),
        Input("close-body-scroll2", "n_clicks"),
    ],
    [State("modal-body-scroll2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# LAYOUTS GRAPHS
layout_chart = dict(xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=1,
            ticks='outside',
            tickfont=dict(size=11, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=False,
        margin=dict(
            l=20,
            r=20,
            b=100,
            t=100,
            pad=0
        ),
        plot_bgcolor='white')

# POPULAÇÃO, PIB TOTAL E IDHM
@app.callback(
    Output('populacao', 'children'),
    Output('pib_total', 'children'),
    Output('idhm', 'children'),
    Output('ivs', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_pop_pib_idh(w_municipios, w_municipios1):
    df['pib_total'] = df['pib_total'].astype(float)
    populacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['populacao'].sum()
    populacao = f'{populacao:_.0f}'.replace('_', '.')
    pib = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_total'].sum() / 1000000
    pib = f'R$ {pib:_.2f} bi'.replace('.', ',').replace('_', '.')
    idhm = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['idhm'].sum()
    idhm = f'{idhm:_.3f}'.replace('.', ',').replace('_', '.')
    idhm_brasil = df[(df['uf'] == 'Brasil') & (df['municipio'] == ' Todos os Municípios')]['idhm'].sum()
    idhm_brasil = f'{idhm_brasil:_.3f}'.replace('.', ',').replace('_', '.')
    ivs = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['ivs'].sum()
    ivs = f'{ivs:_.3f}'.replace('.', ',').replace('_', '.')
    ivs_brasil = df[(df['uf'] == 'Brasil') & (df['municipio'] == ' Todos os Municípios')]['ivs'].sum()
    ivs_brasil = f'{ivs_brasil:_.3f}'.replace('.', ',').replace('_', '.')

    return populacao, pib, idhm + ' (Brasil - ' + f'{idhm_brasil})', ivs + ' (Brasil - ' + f'{ivs_brasil})'

# NÚMEROS CADASTRO ÚNICO / BOLSA FAMÍLIA / BPC
@app.callback(
    Output('cadunico', 'children'),
    Output('familias_cad', 'children'),
    Output('bolsa_familia', 'children'),
    Output('familias_pbf', 'children'),
    Output('perc_cad', 'children'),
    Output('perc_pbf', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_cadunico(w_municipios, w_municipios1):
    pessoas_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_cad'].sum()
    pessoas_cad = f'{pessoas_cad:_.0f}'.replace('.', ',').replace('_', '.')
    familias_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['familias_cad'].sum()
    familias_cad = f'{familias_cad:_.0f}'.replace('.', ',').replace('_', '.')
    pessoas_pbf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_pbf'].sum()
    pessoas_pbf = f'{pessoas_pbf:_.0f}'.replace('.', ',').replace('_', '.')
    familias_pbf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['familias_pbf'].sum()
    familias_pbf = f'{familias_pbf:_.0f}'.replace('.', ',').replace('_', '.')
    pessoas_cad1 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_cad'].sum()
    pessoas_pbf1 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_pbf'].sum()
    populacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['populacao'].sum()
    perc_cad = ((pessoas_cad1/populacao)*100).round(2)
    perc_pbf = ((pessoas_pbf1/populacao)*100).round(2)

    return pessoas_cad + ' pessoas', familias_cad + ' famílias', pessoas_pbf + ' pessoas', familias_pbf + ' famílias',\
           f'{perc_cad:.0f}% da população total', f'{perc_pbf:.0f}% da população total'

# DADOS EM TABELA
@app.callback(Output('outros_dados', 'children'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_table(w_municipios, w_municipios1):
    df1 = df[['uf', 'municipio', 'regiao', 'pais', 'bpc_ben', 'bpc_pcd_ben', 'bpc_idoso_ben', 'familias_catadores_cad', ]]
    df1 = df1.rename(columns={"bpc_ben":"Total de Beneficiários do Benefício de Prestação Continuada (BPC)",
                       "bpc_pcd_ben":"Beneficiários do BPC portadores de deficiência", "bpc_idoso_ben":"Beneficiários do BPC idosos",
                       "familias_catadores_cad":"Famílias de catadores de material reciclável inscritas no Cadastro Único"})
    df1 = df1.melt(id_vars=["uf", "municipio", "regiao", "pais"], var_name="Indicador", value_name="Quantidade")
    df2 = df1[(df1['municipio'] == w_municipios1) & (df1['uf'] == w_municipios)]
    df2 = df2.drop(['uf', 'municipio', 'regiao', 'pais'], axis=1)

    return dbc.Table.from_dataframe(df2, striped=True, bordered=True, hover=True, style={'background-color':'white'})

# EVOLUÇÃO DO CADUNICO E DO PBF
@app.callback(Output('cad_pbf', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_ev_cadunico(w_municipios, w_municipios1):
    df_cad['mês_ano'] = pd.to_datetime(df_cad['mês_ano'], format='%d/%m/%Y')
    # df_cad['mês_ano'] = df_cad['mês_ano'].dt.date
    uf2 = df_cad.groupby(['uf', 'mês_ano']).sum().reset_index()
    uf2['municipio'] = ' Todos os Municípios'
    regiao2 = df_cad.groupby(by=['regiao', 'mês_ano']).sum().reset_index()
    regiao2['municipio'] = ' Todos os Municípios'
    regiao2 = regiao2.rename(columns={"regiao": "uf"})
    pais2 = df_cad.groupby(by=["pais", 'mês_ano']).sum().reset_index()
    pais2['municipio'] = ' Todos os Municípios'
    pais2 = pais2.rename(columns={"pais": "uf"})
    df_cad1 = df_cad.append([uf2, regiao2, pais2], ignore_index=True)
    df_cad1 = df_cad1.sort_values(by=['mês_ano'], ascending=True)

    df2 = df_cad1[(df_cad1['municipio'] == w_municipios1) & (df_cad1['uf'] == w_municipios)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df2['mês_ano'], y=df2['pessoas_pbf'], name='Bolsa Família', mode='lines+markers',
                             marker=dict(size=7, color='black'),
                             hovertemplate="%{y:.2s}",
                             ))
    fig.add_trace(go.Scatter(x=df2['mês_ano'], y=df2['pessoas_pob_extremapob'], name='Pobreza e extrema pobreza', mode='lines+markers',
                             hovertemplate="%{y:.2s}",
                             marker=dict(size=7, color='#fb8500')))
    fig.add_trace(go.Scatter(x=df2['mês_ano'], y=df2['pessoas_cad'], name='Cadastro Único', mode='lines+markers',
                             hovertemplate="%{y:.2s}",
                             marker=dict(size=7, color='#f94144')))
    fig.update_layout(layout_chart)
    title = 'Pessoas inscritas no CadÚnico e beneficiárias<br>do Bolsa Família (2019-2021)' \
            '<br><span style="font-size:10px"><i>Ministério da Cidadania, abril/2021</span></i>'
    fig.update_layout(
        xaxis=dict(
            tickformat='%b %Y',
        ),
        hovermode="x unified",
        showlegend=True,
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
        title={
            'y': 0.93,
            'yanchor': 'top'},
    )
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
    ))
    return fig

# POPULAÇÃO DO CADUNICO POR SITUAÇÃO DO DOMICÍLIO E SEXO
@app.callback(Output('urbano_cad', 'children'),
              Output('perc_urbano', 'children'),
              Output('masc_cad', 'children'),
              Output('fem_cad', 'children'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_domicilio_sexo(w_municipios, w_municipios1):
    urbano = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pes_cad_urbano'].sum()
    urbano1 = f'{urbano:_.0f}'.replace('.', ',').replace('_', '.')
    masc_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_masculino'].sum()
    masc_cad1 = f'{masc_cad:_.0f}'.replace('.', ',').replace('_', '.')
    fem_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_feminino'].sum()
    fem_cad1 = f'{fem_cad:_.0f}'.replace('.', ',').replace('_', '.')

    populacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_cad'].sum()
    perc_urbano = (urbano/populacao*100).round(1)
    perc_masc = (masc_cad/populacao*100).round(1)
    perc_fem = (fem_cad/populacao * 100).round(1)

    return urbano1 + ' pessoas', f'{perc_urbano:.0f}% da pop. do CadÚnico', masc_cad1 + f' ({perc_masc:.0f}%)', fem_cad1 + f' ({perc_fem:.0f}%)'

# POPULAÇÃO DO CADUNICO POR FAIXA ETÁRIA
@app.callback(Output('faixa_etaria', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_age(w_municipios, w_municipios1):
    faixa = ['16 a 17', '18 a 24', '25 a 34', '35 a 39', '40 a 44', '45 a 49', '50 a 54', '55 a 59', '60 a 64']
    populacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_cad'].sum()
    faixa16_17 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_16_17_anos'].sum()
    perc_faixa16_17 = (faixa16_17/populacao*100).round(2)
    faixa18_24 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_18_24_anos'].sum()
    perc_faixa18_24 = (faixa18_24 / populacao * 100).round(2)
    faixa25_34 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_25_34_anos'].sum()
    perc_faixa25_34 = (faixa25_34 / populacao * 100).round(2)
    faixa35_39 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_35_39_anos'].sum()
    perc_faixa35_39 = (faixa35_39 / populacao * 100).round(2)
    faixa40_44 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_40_44_anos'].sum()
    perc_faixa40_44 = (faixa40_44 / populacao * 100).round(2)
    faixa45_49 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_45_49_anos'].sum()
    perc_faixa45_49 = (faixa45_49 / populacao * 100).round(2)
    faixa50_54 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_50_54_anos'].sum()
    perc_faixa50_54 = (faixa50_54 / populacao * 100).round(2)
    faixa55_59 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_55_59_anos'].sum()
    perc_faixa55_59 = (faixa55_59 / populacao * 100).round(2)
    faixa60_64 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_60_64_anos'].sum()
    perc_faixa60_64 = (faixa60_64 / populacao * 100).round(2)

    colors = ['#1351B4', '#fb8500', '#fb8500', '#1351B4', '#1351B4', '#1351B4', '#1351B4', '#1351B4', '#1351B4']

    fig = go.Figure()
    fig.add_trace(go.Bar(x=faixa, y=[faixa16_17, faixa18_24, faixa25_34, faixa35_39, faixa40_44, faixa45_49, faixa50_54, faixa55_59, faixa60_64],
                         showlegend=False, name='',
                         hovertemplate =
                         '<b>População</b>: %{y:.0f}'+
                         '<br><b>Faixa Etária</b>: %{x} anos<br>',
                         text=[perc_faixa16_17, perc_faixa18_24, perc_faixa25_34, perc_faixa35_39, perc_faixa40_44, perc_faixa45_49,
                               perc_faixa50_54,perc_faixa55_59, perc_faixa60_64], textposition='inside', textfont={'size':14},
                         texttemplate="%{text:.0f}%",
                         marker=dict(color=colors)))

    fig.update_layout(layout_chart)

    title = 'Pessoas inscritas no CadÚnico, por <b>faixa etária</b>' \
            '<br><span style="font-size:10px"><i>Ministério da Cidadania, abril/2021</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14
    )

    return fig

# POPULAÇÃO DO CADUNICO POR ESCOLARIDADE
@app.callback(Output('escolaridade', 'figure'),
              Output('analfabetismo', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_escolaridade(w_municipios, w_municipios1):
    nivel = ['Sem instrução', 'Fundamental<br>incompleto', 'Fundamental<br>completo', 'Ensino médio<br>incompleto',
             'Ensino médio<br>completo', 'Superior completo<br>ou incompleto']
    populacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_cad'].sum()
    sem_instrucao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_sem_instrucao'].sum()
    perc_sem_instrucao = (sem_instrucao / populacao * 100).round(2)
    fund_incompleto = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_fundamental_incompleto'].sum()
    perc_fund_incompleto = (fund_incompleto / populacao * 100).round(2)
    fund_completo = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_fundamental_completo'].sum()
    perc_fund_completo = (fund_completo / populacao * 100).round(2)
    medio_incompleto = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_medio_incompleto'].sum()
    perc_medio_incompleto = (medio_incompleto / populacao * 100).round(2)
    medio_completo = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_medio_completo'].sum()
    perc_medio_completo = (medio_completo / populacao * 100).round(2)
    superior = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_superior_completo_incompleto'].sum()
    perc_superior = (superior / populacao * 100).round(2)
    perc_abaixo_ensino_medio = ((sem_instrucao+fund_incompleto+fund_completo+medio_incompleto) / populacao * 100).round(2)

    sabe_ler_escrever = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['sabe_ler_escrever'].sum()
    nao_sabe_ler_escrever = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['não_sabe_ler_escrever'].sum()

    fig = go.Figure()
    fig.add_trace(go.Bar(x=nivel, y=[perc_sem_instrucao, perc_fund_incompleto, perc_fund_completo, perc_medio_incompleto, perc_medio_completo,
                               perc_superior],
                         text=[sem_instrucao, fund_incompleto, fund_completo, medio_incompleto, medio_completo, superior],
                         name='Cadastro Único', marker=dict(color='#FF8C00'), textposition='auto', textfont={'size':14},
                         hovertemplate=
                         '<b>População</b>: %{text:.0f}' +
                         '<br><b>Nível</b>: %{x}<br>',
                         texttemplate='%{y:.0f}%'
                         ),
                  )
    fig.add_trace(go.Bar(x=nivel, y=[7.2, 33.5, 8.0, 6.7, 25.1, 19.5],
                         text=[14140000, 67252000, 16122000, 13394000, 50513000, 39268000],
                         name='Geral', marker=dict(color='#1351B4'), textposition='auto', textfont={'size':14},
                         hovertemplate=
                         '<b>População</b>: %{text:.0f}' +
                         '<br><b>Nível</b>: %{x}<br>',
                         texttemplate='%{y:.0f}%',
                         ),
                  )
    fig.update_layout(layout_chart)
    title = 'Pessoas inscritas no Cadastro Único, por <br><b>nível de escolaridade</b>' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Cidadania (fev/2021) & IBGE/PNAD Contínua (abril/2021)</span></i>'
    fig.update_layout(
        barmode='group',
        showlegend=True,
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.35,
            xanchor="right",
            x=0.6
        )
    )

    annotations = []
    annotations.append(dict(xref='paper', yref='paper', x=0.4, y=0.6,
                            xanchor='left', yanchor='bottom',
                            text=f'{perc_abaixo_ensino_medio:.0f}% não possuem ensino<br>médio completo',
                            font=dict(size=15, color='white'),
                            showarrow=False, ax=20, ay=-20, bordercolor="#FF8C00", borderwidth=2, borderpad=6,
                            bgcolor="#FF8C00", align="center",
                            ))

    fig.update_layout(annotations=annotations)

    fig2 = make_subplots(
        rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
        )

    fig2.add_trace(go.Pie(labels=['Sabe ler e escrever', 'Não sabe ler e escrever'], values=[sabe_ler_escrever, nao_sabe_ler_escrever], showlegend=True, hole=.5,
                          marker=dict(colors=['#1351B4', '#FF8C00']), hoverinfo='label+value', texttemplate="%{percent:.0%f}", name="Região Selecionada",
                          hovertemplate="<b>%{label}<b> <br>%{value:.0f} pessoas</br>"
                          ), 1, 1)
    fig2.add_trace(go.Pie(labels=['Sabe ler e escrever', 'Não sabe ler e escrever'], values=[154232294, 11253000], hole=.5,
                         name="Brasil", hoverinfo='label+value', texttemplate="%{percent:.0%f}", hovertemplate="<b>%{label}<b> <br>%{value:.0f} pessoas</br>"), 1, 2)

    fig2.update_layout(
        margin=dict(
            l=20,
            r=20,
            b=100,
            t=100,
            pad=0
        ),
    )

    annotations = []

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.15,
                            xanchor='left', yanchor='bottom',
                            text='População, por <b>taxa de analfabetismo</b>' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Cidadania (fev/2021) & IBGE/PNAD Contínua (2018)</span></i>',
                            font=dict(size=14, color='#333333'),
                            showarrow=False))
    # Subtitle 1
    annotations.append(dict(xref='paper', yref='paper', x=0.08, y=0.93,
                            xanchor='left', yanchor='bottom',
                            text='Cadastro Único',
                            font=dict(size=13, color='rgb(37,37,37)'),
                            showarrow=False))
    # Subtitle 1
    annotations.append(dict(xref='paper', yref='paper', x=0.65, y=0.93,
                            xanchor='left', yanchor='bottom',
                            text='Geral Brasil',
                            font=dict(size=13, color='rgb(37,37,37)'),
                            showarrow=False))
    fig2.update_layout(annotations=annotations)

    return fig, fig2

# POPULAÇÃO DO CADUNICO POR FUNÇÃO PRINCIPAL E TRABALHO
@app.callback(Output('funcao_principal', 'figure'),
              Output('trabalho_12meses', 'children'),
              Output('trabalho_lastweek', 'children'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_cad_funcao(w_municipios, w_municipios1):
    df_funcao = df[
        ['uf', 'municipio', 'trab_autonomo', 'trab_temp_area_rura', 'emprego_sem_carteira', 'emprego_com_carteira',
         'trab_domestico_sem_carteira', 'trab_domestico_com_carteira',
         'trabalhador_não_remunerado', 'militar_servidor_publico', 'empregador', 'estagiario', 'aprendiz']]

    df_funcao = df_funcao.rename(columns={"trab_autonomo": "Autônomo", "trab_temp_area_rura": "Temporário na<br>Área Rural", 'emprego_sem_carteira': 'Emprego sem<br>Carteira',
                                          'emprego_com_carteira':'Emprego com<br>Carteira', 'trab_domestico_sem_carteira': 'Trabalho Doméstico<br>sem Carteira',
                                          'trab_domestico_com_carteira': 'Trabalho Doméstico<br>com Carteira', 'trabalhador_não_remunerado':'Trabalho não<br>Remunerado',
                                          'militar_servidor_publico':'Militar/Servidor<br>Público', 'empregador':'Empregador', 'estagiario':'Estagiário',
                                          'aprendiz':'Aprendiz'})
    df1 = pd.melt(df_funcao, id_vars=['uf', 'municipio'],
                  value_vars=['Autônomo', 'Temporário na<br>Área Rural', 'Emprego sem<br>Carteira', 'Emprego com<br>Carteira', 'Trabalho Doméstico<br>sem Carteira',
                                          'Trabalho Doméstico<br>com Carteira', 'Trabalho não<br>Remunerado', 'Militar/Servidor<br>Público', 'Empregador', 'Estagiário',
                                          'Aprendiz'])
    df2 = df1[(df1['uf'] == w_municipios) & (df1['municipio'] == w_municipios1)]
    df2 = df2.nlargest(6, 'value')

    trab_12_meses = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trab_12_meses'].sum()
    nao_trab_12_meses = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['não_trab_12_meses'].sum()
    sem_trab_12_meses = ((nao_trab_12_meses/(trab_12_meses+nao_trab_12_meses))*100).round(2)

    trab_last_week = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trab_semana_passada'].sum()
    nao_trab_last_week = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['não_trab_semana_passada'].sum()
    sem_trab_last_week = ((nao_trab_last_week / (trab_last_week + nao_trab_last_week)) * 100).round(1)

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=df2['variable'],
                          y=df2['value'], showlegend=False,
                          hovertemplate=
                          '<b>População</b>: %{y}' +
                          '<br><b>Função principal</b>: %{x}<br>', name='', marker=dict(color='#0C326F')))
    fig1.update_layout(layout_chart)

    title = 'Pessoas inscritas no Cadastro Único, por <br><b>função principal</b>' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Cidadania (abril/2021)</span></i>'
    fig1.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    return fig1, f'{sem_trab_12_meses:.0f}%', f'{sem_trab_last_week:.0f}%'

# EMPREENDEDORISMO
@app.callback(Output('mei', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_mei(w_municipios, w_municipios1):
    mei_cadunico = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['mei_cadunico'].astype('int').sum()
    mei_pbf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['mei_pbf'].astype('int').sum()

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=[mei_cadunico, mei_pbf], x=['Cadastro Único', 'Bolsa Família'],
        text=[mei_cadunico, mei_pbf], textfont={'size': 14},
        texttemplate='%{y:_.0f}', showlegend=False,
        hovertemplate="<b>%{x} <br>População: %{y:.0f}</br><b>",
        textposition='auto', name='MEI',
        marker=dict(color='#f8961e')
    ))

    fig.update_layout(layout_chart)

    title = 'Pessoas inscritas no MEI,<br><b>inscritas no CadÚnico</b> ou beneficiárias do <b>Bolsa Família</b>' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Cidadania (julho/2020)</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    return fig

# NÚMEROS SOBRE EMPRESAS
@app.callback(
    Output('empregos', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_estoque_empregos(w_municipios, w_municipios1):
    pessoal = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['estoque_empregos_abr2021'].sum()
    pessoal = f'{pessoal:_.0f}'.replace('_', '.')

    return pessoal

# PIB POR SETOR DE ATIVIDADE ECONÔMICA
@app.callback(Output('pib_setorial', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_pib_setorial(w_municipios, w_municipios1):
    agropecuaria = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]["pib_agropecuaria"].sum()
    industria = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_industria'].sum()
    servicos = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_servicos'].sum()
    admpublica = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_admpublica'].sum()

    fig = go.Figure()
    fig.add_trace(go.Pie(labels=['Agricultura', 'Indústria', 'Serviços', 'Administração'], values=[agropecuaria, industria, servicos, admpublica],
                         showlegend=True, name='Setor', hoverinfo='label+value',
                         texttemplate="%{percent:.0%f}",
                         hole=.5, textfont={'size': 15},
                         hovertemplate="<b>%{label} <br>PIB: R$ %{value:.2f}</br><b>"))

    title = 'PIB por setor de atividade econômica' \
            '<br><span style="font-size:10px"><i>Fonte: IBGE, 2018</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
        hovermode='closest'
    )

    return fig

# NÚMERO DE EMPRESAS POR SETOR DE ATIVIDADE ECONÔMICA
@app.callback(Output('empresas_setorial', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_empresas(w_municipios, w_municipios1):
    df_empresas = df[
        ['uf', 'municipio', 'empresas_agropecuaria', 'empresas_ind_extrativas', 'empresas_ind_transf', 'empresas_eletric_gas',
         'empresas_saneamento', 'empresas_construcao', 'empresas_comercio', 'empresas_transporte', 'empresas_alojamento_alimentacao',
         'empresas_info_comunic', 'empresas_financeiro', 'empresas_imobiliarias', 'empresas_ativ_profissionais_cient_tecnicas', 'empresas_ativ_administrativas',
         'empresas_educacao', 'empresas_saude_servicosocial', 'empresas_arte_cultura', 'empresas_outras_ativ_servicos']]

    df_empresas = df_empresas.rename(columns={'empresas_agropecuaria':'Agropecuária', 'empresas_ind_extrativas':'Indústria<br>Extrativa', 'empresas_ind_transf':'Indústria de<br>Transformação',
                                          'empresas_eletric_gas':'Eletricidade<br>e gás', 'empresas_saneamento':'Saneamento', 'empresas_construcao':'Construção',
                                          'empresas_comercio':'Comércio', 'empresas_transporte':'Transporte', 'empresas_alojamento_alimentacao':'Alojamento e<br>Alimentação',
                                          'empresas_info_comunic':'Informação e<br>Comunicação', 'empresas_financeiro':'Financeiras', 'empresas_imobiliarias': 'Imobiliárias',
                                          'empresas_ativ_profissionais_cient_tecnicas':'Atividades Científicas<br>e Técnicas', 'empresas_ativ_administrativas':'Atividades<br>administrativas',
                                          'empresas_educacao':'Educação', 'empresas_saude_servicosocial':'Saúde', 'empresas_arte_cultura':'Arte, Cultura e<br>Esportes',
                                          'empresas_outras_ativ_servicos':'Outras Atividades'})

    df1 = pd.melt(df_empresas, id_vars=['uf', 'municipio'],
                  value_vars=['Agropecuária', 'Indústria<br>Extrativa', 'Indústria de<br>Transformação', 'Eletricidade<br>e gás', 'Saneamento', 'Construção',
                                          'Comércio', 'Transporte', 'Alojamento e<br>Alimentação', 'Informação e<br>Comunicação', 'Financeiras', 'Imobiliárias',
                                          'Atividades Científicas<br>e Técnicas', 'Atividades<br>administrativas', 'Educação', 'Saúde', 'Arte, Cultura e<br>Esportes',
                                          'Outras Atividades'])
    df2 = df1[(df1['uf'] == w_municipios) & (df1['municipio'] == w_municipios1)]
    df2 = df2.nlargest(15, 'value')
    df2 = df2.sort_values(by=['value'], ascending=False)

    empresas = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_total'].sum()
    empresas1 = f'{empresas:_.0f}'.replace('_', '.')

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df2['variable'], y=df2['value'],
                         name='Setor', marker=dict(color='#1351B4'),
                         hovertemplate=
                         '<b>%{x}' + '<br>Número de empresas</b>: %{y}<b><br>',
                         ))
    fig.update_layout(layout_chart)

    title = 'Número de empresas, por setor de<br>atividade econômica</b>' \
            '<br><span style="font-size:10px"><i>Fonte: IBGE/CEMPRE, 2018</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    annotations = []

    # Anotação
    annotations.append(dict(xref='paper', yref='paper', x=0.4, y=0.6,
                            xanchor='left', yanchor='bottom',
                            text=f'{empresas1} empresas',
                            font=dict(size=20, color='white'),
                            showarrow=False, ax=20, ay=-30, bordercolor="#1351B4", borderwidth=2, borderpad=6,
                            bgcolor="#1351B4", align="center",))

    fig.update_layout(annotations=annotations)

    return fig

# DISTORÇÃO IDADE-SÉRIE, EVASÃO E REMUNERAÇÃO PROFESSORES
@app.callback(
    Output('rem_docentes_brasil', 'children'),
    Output('rem_docentes_munic', 'children'),
    Output('idade_serie', 'children'),
    Output('idade_serie_brasil', 'children'),
    Output('evasao', 'children'),
    Output('evasao_brasil', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_idade_serie(w_municipios, w_municipios1):
    idade_serie = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['distorcao_idade_serie'].sum()
    idade_serie = f'{idade_serie:_.2f}%'.replace('.', ',').replace('_', '.')
    idade_serie_brasil = df[(df['uf'] == 'Brasil') & (df['municipio'] == ' Todos os Municípios')]['distorcao_idade_serie'].sum()
    idade_serie_brasil = f'{idade_serie_brasil:_.2f}% é a média nacional'.replace('.', ',').replace('_', '.')
    evasao_municipio = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['taxa_evasao_abandono'].sum()
    evasao_municipio = f'{evasao_municipio:_.2f}%'.replace('.', ',').replace('_', '.')
    evasao_brasil = df[(df['uf'] == 'Brasil') & (df['municipio'] == ' Todos os Municípios')]['taxa_evasao_abandono'].sum()
    evasao_brasil = f'{evasao_brasil:_.2f}% é a média nacional'.replace('.', ',').replace('_', '.')
    remuneracao_brasil = df[(df['uf'] == 'Brasil') & (df['municipio'] == ' Todos os Municípios')]['remuneracao_docente_edbasica'].sum().round(1)
    remuneracao_brasil = f'R$ {remuneracao_brasil:_.2f} é a média nacional'.replace('.', ',').replace('_', '.')
    remuneracao_municipio = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['remuneracao_docente_edbasica'].sum().round(1)
    remuneracao_municipio = f'R$ {remuneracao_municipio:_.2f}'.replace('.', ',').replace('_', '.')

    return remuneracao_brasil, remuneracao_municipio, idade_serie, idade_serie_brasil, evasao_municipio, evasao_brasil

# SALDO E VARIAÇÃO DE EMPREGOS
@app.callback(
    Output('saldo_empregos12', 'children'),
    Output('var_emprego', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_saldo_empregos_recente(w_municipios, w_municipios1):
    df2 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos_12meses'].sum()
    df2 = f'{df2:_.0f}'.replace('.', ',').replace('_', '.')
    df3 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['var_saldo_empregos_12meses'].sum().round(2)
    df3 = f'Variação de {df3:_.2f}%'.replace('.', ',').replace('_', '.')

    return df2, df3

# EVOLUÇÃO DO SALDO DE EMPREGOS
@app.callback(Output('evolucao_empregos', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_ev_saldo_empregos(w_municipios, w_municipios1):
    anos = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
            '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
    saldo_empregos2002 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2002'].sum()
    saldo_emprego2003 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2003'].sum()
    saldo_emprego2004 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2004'].sum()
    saldo_emprego2005 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2005'].sum()
    saldo_emprego2006 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2006'].sum()
    saldo_emprego2007 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2007'].sum()
    saldo_emprego2008 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2008'].sum()
    saldo_emprego2009 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2009'].sum()
    saldo_emprego2010 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2010'].sum()
    saldo_emprego2011 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2011'].sum()
    saldo_emprego2012 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2012'].sum()
    saldo_emprego2013 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2013'].sum()
    saldo_emprego2014 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2014'].sum()
    saldo_emprego2015 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2015'].sum()
    saldo_emprego2016 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2016'].sum()
    saldo_emprego2017 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2017'].sum()
    saldo_emprego2018 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2018'].sum()
    saldo_emprego2019 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2019'].sum()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=anos, y=[saldo_empregos2002, saldo_emprego2003, saldo_emprego2004, saldo_emprego2005, saldo_emprego2006,
               saldo_emprego2007, saldo_emprego2008, saldo_emprego2009, saldo_emprego2010, saldo_emprego2011, saldo_emprego2012,
               saldo_emprego2013, saldo_emprego2014, saldo_emprego2015, saldo_emprego2016, saldo_emprego2017, saldo_emprego2018, saldo_emprego2019],
                             marker=dict(size=8, color='#1351B4')
                             ))
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=1,
            ticks='outside',
            zerolinecolor='grey',
            tickfont=dict(size=11, color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            showline=True,
            showticklabels=False,
            zerolinecolor='grey',
            zerolinewidth=0.5
        ),
        autosize=True,
        hovermode="x unified",
        margin=dict(
            l=15,
            r=15,
            b=100,
            t=100,
            pad=0
        ),
        showlegend=False,
        plot_bgcolor='white'
    )

    title = 'Evolução do <b>saldo de empregos formais</b><br>(2002-2019)' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Economia/RAIS, 2019</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    return fig

# EVOLUÇÃO DA REMUNERAÇÃO TOTAL
# @app.callback(Output('remuneracao', 'figure'),
#               Input('w_municipios', 'value'),
#               Input('w_municipios1', 'value')
#               )
# def display_remuneracao_ocupacoes(w_municipios, w_municipios1):
#     uf3 = df_remuneracao.groupby(by=["uf", 'ano']).mean().reset_index()
#     uf3['municipio'] = ' Todos os Municípios'
#     regiao3 = df_remuneracao.groupby(by=['regiao', 'ano']).mean().reset_index()
#     regiao3['municipio'] = ' Todos os Municípios'
#     regiao3 = regiao3.rename(columns={"regiao": "uf"})
#     pais3 = df_remuneracao.groupby(by=["pais", 'ano']).mean().reset_index()
#     pais3['municipio'] = ' Todos os Municípios'
#     pais3 = pais3.rename(columns={"pais": "uf"})
#     df_remuneracao1 = df_remuneracao.append([uf3, regiao3, pais3], ignore_index=True)
#     df_remuneracao1['ano'] = df_remuneracao1['ano'].astype('int')
#     df_remuneracao1['Total'] = df_remuneracao1['Total'].round(2)*1100
#
#     rem_brasil = df_remuneracao1[(df_remuneracao1['municipio'] == ' Todos os Municípios') & (df_remuneracao1['uf'] == 'Brasil') & (df_remuneracao1['ano'] == 2019)]['Total'].sum().round(1)
#     rem_municipio = df_remuneracao1[(df_remuneracao1['municipio'] == w_municipios1) & (df_remuneracao1['uf'] == w_municipios) & (df_remuneracao1['ano'] == 2019)]['Total'].sum().round(1)
#     municipio = df_remuneracao1[
#         (df_remuneracao1['municipio'] == w_municipios1) & (df_remuneracao1['uf'] == w_municipios) & (
#                     df_remuneracao1['ano'] == 2019)]['municipio']
#
#     fig = go.Figure()
#     fig.add_trace(go.Bar(x=['Brasil'], y=[rem_brasil], name='', marker=dict(color='#5992ED'),
#                           text=[rem_brasil], textfont={'size': 14},
#                           hovertemplate=
#                           '<b>%{x}</b>' +
#                           '<br><b>Remuneração média</b>: R$ %{y:.2f}<br>',
#                           ))
#     fig.add_trace(go.Bar(x=municipio, y=[rem_municipio], name='', marker=dict(color='#0C326F'),
#                           text=[rem_municipio], textfont={'size': 14},
#                           hovertemplate=
#                           '<b>%{x}</b>' +
#                           '<br><b>Remuneração média</b>: R$ %{y:.2f}<br>',
#                           ))
#
#     fig.update_layout(layout_chart, barmode='group', showlegend=False)
#
#     title = '<b>Remuneração média mensal</b> dos<br>empregos formais' \
#             '<br><span style="font-size:10px"><i>Fonte: Ministério da Economia/RAIS, 2019</span></i>'
#     fig.update_layout(
#         title_text=title,
#         title_font_color='#333333',
#         title_font_size=14,
#     )
#
#     return fig

# PLANILHA COM A REMUNERAÇÃO DE TODAS AS OCUPAÇÕES
@app.callback(
    Output('table2', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value'),
)
def update_remuneracao_table(w_municipios, w_municipios1):
    uf3 = df_remuneracao.groupby(by=["uf", 'ano']).mean().reset_index()
    uf3['municipio'] = ' Todos os Municípios'
    regiao3 = df_remuneracao.groupby(by=['regiao', 'ano']).mean().reset_index()
    regiao3['municipio'] = ' Todos os Municípios'
    regiao3 = regiao3.rename(columns={"regiao": "uf"})
    pais3 = df_remuneracao.groupby(by=["pais", 'ano']).mean().reset_index()
    pais3['municipio'] = ' Todos os Municípios'
    pais3 = pais3.rename(columns={"pais": "uf"})
    df_remuneracao1 = df_remuneracao.append([uf3, regiao3, pais3], ignore_index=True)
    df_remuneracao1['ano'] = df_remuneracao1['ano'].astype('int')

    df1 = df_remuneracao1.melt(id_vars=["uf", "municipio", "regiao", "pais", "ano"], var_name="Ocupação", value_name="Remuneração")
    df1['Remuneração'] = df1['Remuneração'].round(2) * 1100
    df1['Remuneração'] = df1['Remuneração'].map('R$ {:,.2f}'.format)
    df1['Ocupação'] = df1['Ocupação'].str.capitalize()
    df2 = df1[(df1['municipio'] == w_municipios1) & (df1['uf'] == w_municipios) & (df1['ano'] == 2019)]
    df2 = df2.iloc[1:, :]
    data = df2.to_dict('records')
    columns = [{"name": i, "id": i,} for i in df2[['Ocupação', 'Remuneração']]]
    export_format = "xlsx"
    return dash_table.DataTable(data=data, columns=columns, export_format=export_format, filter_action='native',
                                page_action="native", page_current=0, page_size=10, sort_action='native', export_headers="display",
                                style_as_list_view=True, style_header={'backgroundColor': '#0C326F', 'color':'white', 'fontWeight': 'bold','fontSize':12},
                                style_cell={'backgroundColor': 'white', 'color': 'black', 'fonteSize':12,
                                            'minWidth': 95, 'width': 95, 'maxWidth': 95},
                                )

# SUBSETORES COM MAIOR QUANTIDADE DE VÍNCULOS
@app.callback(
    Output('vinculos_subsetor', 'figure'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_saldo_vinculos(w_municipios, w_municipios1):
    uf = df_vinculos_subsetor_ibge.groupby(by=["uf"]).sum().reset_index()
    uf['municipio'] = ' Todos os Municípios'
    regiao = df_vinculos_subsetor_ibge.groupby(by=['regiao']).mean().reset_index()
    regiao['municipio'] = ' Todos os Municípios'
    regiao = regiao.rename(columns={"regiao": "uf"})
    pais = df_vinculos_subsetor_ibge.groupby(by=["pais"]).mean().reset_index()
    pais['municipio'] = ' Todos os Municípios'
    pais = pais.rename(columns={"pais": "uf"})
    df_saldo1 = df_vinculos_subsetor_ibge.append([uf, regiao, pais], ignore_index=True)

    df2 = df_saldo1.melt(id_vars=["uf", "municipio", "ibge6", "regiao", "pais"],
                          var_name="subsetor",
                          value_name="vinculos")
    df3 = df2[(df2['municipio'] == w_municipios1) & (df2['uf'] == w_municipios)]

    df3 = df3.nlargest(6, 'vinculos')
    df3 = df3.iloc[1: , :]

    fig = go.Figure()

    fig.add_trace(go.Bar(x=df3['subsetor'], y=df3['vinculos'], textfont={'size': 12}, textposition='auto', name='', marker=dict(color='#1351B4'),
                         hovertemplate='<b>%{x}' + '<br>Quantidade de Vínculos</b>: %{y}<b><br>'))

    fig.update_layout(layout_chart)

    title = 'Setores da economia com maior quantidade<br> de <b>vínculos de empregos formais</b>' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Economia/RAIS, 2019</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    return fig

# EVOLUÇÃO DA REMUNERAÇÃO POR SETOR DE ATIVIDADE ECONÔMICA
@app.callback(
    Output('rem_setor', 'figure'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def rem_setor(w_municipios, w_municipios1):
    data = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/data/remuneracao_SM_setor_IBGE_RAIS_2015_2019.csv'
    df = pd.read_csv(data, sep=';', encoding='latin1', decimal=',')
    df = df.drop(['Município'], axis=1)
    df['ano'] = df['ano'].astype('str')

    uf = df.groupby(by=["uf", 'ano']).sum().reset_index()
    uf['municipio'] = ' Todos os Municípios'
    regiao = df.groupby(by=['regiao', 'ano']).mean().reset_index()
    regiao['municipio'] = ' Todos os Municípios'
    regiao = regiao.rename(columns={"regiao": "uf"})
    pais = df.groupby(by=["pais", 'ano']).mean().reset_index()
    pais['municipio'] = ' Todos os Municípios'
    pais = pais.rename(columns={"pais": "uf"})
    df = df.append([uf, regiao, pais], ignore_index=True)

    df['Total'] = df['Total'].round(2)*1100
    df['Indústria'] = df['Indústria'].round(2) * 1100
    df['Construção Civil'] = df['Construção Civil'].round(2) * 1100
    df['Comércio'] = df['Comércio'].round(2) * 1100
    df['Serviços'] = df['Serviços'].round(2) * 1100
    df['Agropecuária'] = df['Agropecuária'].round(2) * 1100

    df1 = df[(df['municipio'] == w_municipios1) & (df['uf'] == w_municipios)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df1['ano'], y=df1['Indústria'], mode='lines+markers', name='Indústria',
                             hovertemplate='<b>Remuneração média</b>: R$ %{y:.2f}<br>'))
    fig.add_trace(go.Scatter(x=df1['ano'], y=df1['Construção Civil'], mode='lines+markers', name='Construção Civil',
                             hovertemplate='<b>Remuneração média</b>: R$ %{y:.2f}<br>'))
    fig.add_trace(go.Scatter(x=df1['ano'], y=df1['Comércio'], mode='lines+markers', name='Comércio',
                             hovertemplate='<b>Remuneração média</b>: R$ %{y:.2f}<br>'))
    fig.add_trace(go.Scatter(x=df1['ano'], y=df1['Serviços'], mode='lines+markers', name='Serviços',
                             hovertemplate='<b>Remuneração média</b>: R$ %{y:.2f}<br>'))
    fig.add_trace(go.Scatter(x=df1['ano'], y=df1['Agropecuária'], mode='lines+markers', name='Agropecuária',
                             hovertemplate='<b>Remuneração média</b>: R$ %{y:.2f}<br>'))
    fig.add_trace(go.Scatter(x=df1['ano'], y=df1['Total'], mode='lines+markers', name='Total',
                             hovertemplate='<b>Remuneração média</b>: R$ %{y:.2f}<br>'))

    fig.update_layout(layout_chart, showlegend=True)

    title = '<b>Evolução da remuneração média</b>, por setor <br>de atividade econômica (2015-2019)' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Economia/RAIS, 2019</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    return fig

# OCUPAÇÕES COM MAIOR QUANTIDADE DE VINCULOS
@app.callback(
    Output('top_vinculos', 'figure'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_top_vinculos(w_municipios, w_municipios1):
    uf4 = df_caged.groupby(by=["uf", 'ano']).sum().reset_index()
    uf4['municipio'] = ' Todos os Municípios'
    regiao4 = df_caged.groupby(by=['regiao', 'ano']).mean().reset_index()
    regiao4['municipio'] = ' Todos os Municípios'
    regiao4 = regiao4.rename(columns={"regiao": "uf"})
    pais4 = df_caged.groupby(by=["pais", 'ano']).mean().reset_index()
    pais4['municipio'] = ' Todos os Municípios'
    pais4 = pais4.rename(columns={"pais": "uf"})
    df_caged1 = df_caged.append([uf4, regiao4, pais4], ignore_index=True)
    df_caged1['ano'] = df_caged1['ano'].astype('int')

    df2 = df_caged1.melt(id_vars=["uf", "municipio", "ibge6", "regiao", "pais", "ano"],
                          var_name="ocupation",
                          value_name="vinculos")
    df2['vinculos'] = df2['vinculos'].astype('int')
    df2['ocupation'] = df2['ocupation'].str.capitalize()
    df3 = df2[(df2['municipio'] == w_municipios1) & (df2['uf'] == w_municipios) & (df2['ano'] == 2019)]

    df4 = df3.nlargest(6, 'vinculos')
    df5 = df4.iloc[1: , :]

    fig = go.Figure()

    fig.add_trace(go.Pie(labels=df5['ocupation'], values=df5['vinculos'],
                          hoverinfo='label+value', texttemplate="%{percent:.0%f}", hole=.5, textfont={'size': 12}))

    fig.update_layout(
        xaxis_tickfont_size=14,
        yaxis=dict(
            titlefont_size=16,
            tickfont_size=14,
        ),
        showlegend=False,
        margin=dict(
            l=15,
            r=15,
            b=100,
            t=100,
            pad=1
        ),
    )

    title = 'Ocupações com <b>maior quantidade<br>de vínculos ativos</b>' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Economia/RAIS, 2019</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    return fig

# PLANILHA COM TODOS AS OCUPAÇÕES POR QUANTIDADE DE VÍNCULOS
@app.callback(
    Output('table', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_top_vinculos_table(w_municipios, w_municipios1):
    uf4 = df_caged.groupby(by=["uf", 'ano']).sum().reset_index()
    uf4['municipio'] = ' Todos os Municípios'
    regiao4 = df_caged.groupby(by=['regiao', 'ano']).sum().reset_index()
    regiao4['municipio'] = ' Todos os Municípios'
    regiao4 = regiao4.rename(columns={"regiao": "uf"})
    pais4 = df_caged.groupby(by=["pais", 'ano']).sum().reset_index()
    pais4['municipio'] = ' Todos os Municípios'
    pais4 = pais4.rename(columns={"pais": "uf"})
    df_caged1 = df_caged.append([uf4, regiao4, pais4], ignore_index=True)
    df_caged1['ano'] = df_caged1['ano'].astype('int')

    df1 = df_caged1.melt(id_vars=["uf", "municipio", "regiao", "pais", "ano"], var_name="Ocupação", value_name="Quantidade de Vínculos")
    df1['Ocupação'] = df1['Ocupação'].str.capitalize()
    df2 = df1[(df1['municipio'] == w_municipios1) & (df1['uf'] == w_municipios) & (df1['ano'] == 2019)]
    df2 = df2.iloc[1:, :]
    data = df2.to_dict('records')
    columns = [{"name": i, "id": i,} for i in df2[['Ocupação', 'Quantidade de Vínculos']]]
    export_format = "xlsx"
    return dash_table.DataTable(data=data, columns=columns, export_format=export_format, filter_action='native',
                                page_action="native", page_current=0, page_size=10, sort_action='native', export_headers="display",
                                style_as_list_view=True, style_header={'backgroundColor': '#0C326F', 'color':'white', 'fontWeight': 'bold', 'fontSize':12},
                                style_cell={'backgroundColor': 'white', 'color': 'black', 'fonteSize':12,
                                            'minWidth': 95, 'width': 95, 'maxWidth': 95},
                                )

# SUBSETORES COM MAIOR SALDO DE EMPREGOS
@app.callback(
    Output('saldo_subsetor', 'figure'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_saldo_vinculos(w_municipios, w_municipios1):
    uf = df_saldo_subsetor_ibge.groupby(by=["uf"]).sum().reset_index()
    uf['municipio'] = ' Todos os Municípios'
    regiao = df_saldo_subsetor_ibge.groupby(by=['regiao']).mean().reset_index()
    regiao['municipio'] = ' Todos os Municípios'
    regiao = regiao.rename(columns={"regiao": "uf"})
    pais = df_saldo_subsetor_ibge.groupby(by=["pais"]).mean().reset_index()
    pais['municipio'] = ' Todos os Municípios'
    pais = pais.rename(columns={"pais": "uf"})
    df_saldo1 = df_saldo_subsetor_ibge.append([uf, regiao, pais], ignore_index=True)

    df2 = df_saldo1.melt(id_vars=["uf", "municipio", "ibge6", "regiao", "pais"],
                          var_name="subsetor",
                          value_name="saldo")
    df2['saldo'] = df2['saldo'].astype('int')
    df3 = df2[(df2['municipio'] == w_municipios1) & (df2['uf'] == w_municipios)]

    df3 = df3.nlargest(6, 'saldo')
    df3 = df3.iloc[1: , :]

    fig = go.Figure()

    fig.add_trace(go.Pie(labels=df3['subsetor'], values=df3['saldo'],
                          hoverinfo='label+value', texttemplate="%{percent:.0%f}", hole=.5, textfont={'size': 12}))

    fig.update_layout(
        xaxis_tickfont_size=14,
        yaxis=dict(
            titlefont_size=16,
            tickfont_size=14,
        ),
        showlegend=False,
        margin=dict(
            l=15,
            r=15,
            b=100,
            t=100,
            pad=1
        ),
    )

    title = 'Setores da economia com maior<br><b>saldo de empregos formais</b> (2019)' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Economia/RAIS, 2019</span></i>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    return fig

# OCUPAÇÕES COM MAIORES SALDO DE EMPREGOS
@app.callback(
    Output('saldo_ocupacao', 'figure'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_saldo_vinculos(w_municipios, w_municipios1):
    uf5 = df_saldo.groupby(by=["uf", 'ano']).sum().reset_index()
    uf5['municipio'] = ' Todos os Municípios'
    regiao5 = df_saldo.groupby(by=['regiao', 'ano']).mean().reset_index()
    regiao5['municipio'] = ' Todos os Municípios'
    regiao5 = regiao5.rename(columns={"regiao": "uf"})
    pais5 = df_saldo.groupby(by=["pais", 'ano']).mean().reset_index()
    pais5['municipio'] = ' Todos os Municípios'
    pais5 = pais5.rename(columns={"pais": "uf"})
    df_saldo1 = df_saldo.append([uf5, regiao5, pais5], ignore_index=True)
    df_saldo1['ano'] = df_saldo1['ano'].astype('int')

    df2 = df_saldo1.melt(id_vars=["uf", "municipio", "ibge", "regiao", "pais", "ano"],
                          var_name="ocupation",
                          value_name="saldo")
    df2['ocupation'] = df2['ocupation'].str.capitalize()
    df3 = df2[(df2['municipio'] == w_municipios1) & (df2['uf'] == w_municipios) & (df2['ano'] == 2019)]

    df3 = df3.nlargest(8, 'saldo')
    df3 = df3.iloc[1: , :]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=df3['saldo'], x=df3['ocupation'], textposition='auto', name='',
        marker=dict(color='#f8961e'),
        hovertemplate=
        '<b>Saldo de empregos</b>: %{y:.2s}' +
        '<br><b>Ocupação</b>: %{x}<br>',
    ))

    fig.update_layout(layout_chart)

    title = 'Ocupações com <b>maior saldo de<br>empregos formais</b> (2019)' \
            '<br><span style="font-size:10px"><i>Fonte: Ministério da Economia/RAIS, 2019</span></i>' \
            '<br><span style="font-size:20px", className="far fa-lightbulb"></span>'
    fig.update_layout(
        title_text=title,
        title_font_color='#333333',
        title_font_size=14,
    )

    # html.Span(
    #     className="far fa-lightbulb",
    #     id="tooltip-target",
    #     style={'fontSize': 20, "cursor": "pointer", 'color': '#fb8500',
    #            'padding-left': '10px', 'padding-top': '7px'},
    # ),

    return fig

# PLANILHA COM TODOS AS OCUPAÇÕES POR QUANTIDADE DE VÍNCULOS
@app.callback(
    Output('table3', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_saldo_vinculos_table(w_municipios, w_municipios1):
    uf5 = df_saldo.groupby(by=["uf", 'ano']).sum().reset_index()
    uf5['municipio'] = ' Todos os Municípios'
    regiao5 = df_saldo.groupby(by=['regiao', 'ano']).sum().reset_index()
    regiao5['municipio'] = ' Todos os Municípios'
    regiao5 = regiao5.rename(columns={"regiao": "uf"})
    pais5 = df_saldo.groupby(by=["pais", 'ano']).sum().reset_index()
    pais5['municipio'] = ' Todos os Municípios'
    pais5 = pais5.rename(columns={"pais": "uf"})
    df_saldo1 = df_saldo.append([uf5, regiao5, pais5], ignore_index=True)
    df_saldo1['ano'] = df_saldo1['ano'].astype('int')

    df1 = df_saldo1.melt(id_vars=["uf", "municipio", "regiao", "pais", "ano"], var_name="Ocupação", value_name="Saldo de Empregos")
    df1['Ocupação'] = df1['Ocupação'].str.capitalize()
    df2 = df1[(df1['municipio'] == w_municipios1) & (df1['uf'] == w_municipios) & (df1['ano'] == 2019)]
    df2 = df2.iloc[1:, :]
    data = df2.to_dict('records')
    columns = [{"name": i, "id": i,} for i in df2[['Ocupação', 'Saldo de Empregos']]]
    export_format = "xlsx"
    return dash_table.DataTable(data=data, columns=columns, export_format=export_format, filter_action='native',
                                page_action = "native", page_current=0, page_size=10, sort_action='native', export_headers="display",
                                style_as_list_view=True, style_header={'backgroundColor': '#0C326F', 'color':'white', 'fontWeight': 'bold', 'fontSize':12},
                                style_cell={'backgroundColor': 'white', 'color': 'black', 'fonteSize':12,
                                            'minWidth': 95, 'width': 95, 'maxWidth': 95},
                                )

if __name__ == '__main__':
    app.run_server(debug=True)





