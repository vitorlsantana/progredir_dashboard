import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_table

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}],
                suppress_callback_exceptions=True, )
server = app.server

# CARREGAR DADOS
data = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/base_painel_inclus%C3%A3o_produtiva.csv'
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
                                        'idhm':'mean', 'var_saldo_empregos_12meses':'mean', 'ivs':'mean', 'taxa_homicidios ':'mean'
                                        }).reset_index()
uf['municipio'] = 'Todos os Municípios'
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
                                        'idhm':'mean', 'var_saldo_empregos_12meses':'mean', 'ivs':'mean', 'taxa_homicidios ':'mean'
                                        }).reset_index()
regiao['municipio'] = 'Todos os Municípios'
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
                                        'idhm':'mean', 'var_saldo_empregos_12meses':'mean', 'ivs':'mean', 'taxa_homicidios ':'mean'
                                        }).reset_index()
pais['municipio'] = 'Todos os Municípios'
pais['uf'] = pais['pais']
df = df1.append([uf, regiao, pais], ignore_index=True)

data1 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/vinculos_ativos_ocupacao_subgruposprincipais_2015_2019.csv'
df_caged = pd.read_csv(data1, sep=';', encoding='latin1', low_memory=False)
uf1 = df_caged.groupby(by=["uf"]).sum().reset_index()
uf1['municipio'] = 'Todos os Municípios'
regiao1 = df_caged.groupby(by=['regiao']).sum().reset_index()
regiao1['municipio'] = 'Todos os Municípios'
regiao1['uf'] = regiao['regiao']
pais1 = df_caged.groupby(by=["pais"]).sum().reset_index()
pais1['municipio'] = 'Todos os Municípios'
pais1['uf'] = pais['pais']
df_caged = df_caged.append([uf1, regiao1, pais1], ignore_index=True)
df_caged_melted = df_caged.melt(id_vars=["uf", "municipio", "ibge6", 'regiao', 'pais', 'ano'],
                                var_name="ocupation",
                                value_name="vinculos")
# ocupations = df_caged_melted['ocupation'].unique()

data2 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/evolucao_pessoas_cad_pbf.csv'
df_cad = pd.read_csv(data2, sep=';', encoding='latin1', low_memory=False)
uf2 = df_cad.groupby(by=["uf"]).sum().reset_index()
uf2['municipio'] = 'Todos os Municípios'
regiao2 = df_cad.groupby(by=['regiao']).sum().reset_index()
regiao2['municipio'] = 'Todos os Municípios'
regiao2['uf'] = regiao['regiao']
pais2 = df_cad.groupby(by=["pais"]).sum().reset_index()
pais2['municipio'] = 'Todos os Municípios'
pais2['uf'] = pais['pais']
df_cad = df_cad.append([uf2, regiao2, pais2], ignore_index=True)

data3 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/remuneracao_SM_ocupacao_subgruposprincipais_2015_2019.csv'
df_remuneracao = pd.read_csv(data3, sep=';', encoding='latin1', low_memory=False)
uf3 = df_remuneracao.groupby(by=["uf"]).mean().reset_index()
uf3['municipio'] = 'Todos os Municípios'
regiao3 = df_remuneracao.groupby(by=['regiao']).mean().reset_index()
regiao3['municipio'] = 'Todos os Municípios'
regiao3['uf'] = regiao['regiao']
pais3 = df_remuneracao.groupby(by=["pais"]).mean().reset_index()
pais3['municipio'] = 'Todos os Municípios'
pais3['uf'] = pais['pais']
df_remuneracao = df_remuneracao.append([uf3, regiao3, pais3], ignore_index=True)

data4 = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/saldo_empregos_ocupacao_subgruposprincipais_2015_2019.csv'
df_saldo = pd.read_csv(data4, sep=';', encoding='latin1', low_memory=False)
uf4 = df_saldo.groupby(by=["uf"]).sum().reset_index()
uf4['municipio'] = 'Todos os Municípios'
regiao4 = df_saldo.groupby(by=['regiao']).sum().reset_index()
regiao4['municipio'] = 'Todos os Municípios'
regiao4['uf'] = regiao['regiao']
pais4 = df_saldo.groupby(by=["pais"]).sum().reset_index()
pais4['municipio'] = 'Todos os Municípios'
pais4['uf'] = pais['pais']
df_saldo = df_saldo.append([uf4, regiao4, pais4], ignore_index=True)

# data4 = 'C:\\Users\\Vitor Santana\\PycharmProjects\\painelProgredir\\cnes localizacao e regiao saude.csv'
# df5 = pd.read_csv(data4, sep=',', error_bad_lines=False)

# CONFIGURAÇÃO DE TABS
tab_height = '3vh',
tabs_styles = {
    # 'height': '40px',
    'align-items': 'center',
    'justifyContent':'center',
    'textAlign':'center',
    # 'width':'275px',
    'marginRight':'3px',
    # 'borderBottom': '0px solid transparent',
    'width': '25%',
    'font-size': '200%',
    'height': tab_height
}
tab_style = {
    # 'borderBottom': '0px solid #d6d6d6',
    # 'padding': '0.5rem 1.5rem',
    'color':'#586069',
    'fontWeight': 'bold',
    'border-radius': '3px',
    'background-color': 'white',
    'padding': '0','line-height': tab_height,
    'box-shadow': '1px 0px 1px 1px lightgrey',
    'justifyContent': 'center',
    'textAlign': 'center',
    # 'width':'275px',
    'width': '25%',
    'marginRight':'5px'
}
tab_selected_style = {
    'borderTop': '2px solid #5992ED',
    'height': '40px',
    # 'borderBottom': '0px solid #d6d6d6',
    'color': '#ffba08',
    # 'padding': '0px',
    'padding': '0','line-height': tab_height,
    'border-radius': '3px',
    'justifyContent': 'center',
    'textAlign': 'center',
    'width':'25%'
}

# --------------------------------------------------------------------------------------------------------------------------------------------
# NAVBAR
logo_progredir = "https://github.com/vitorlsantana/progredir_dashboard/blob/main/Marca_Progredir.png?raw=true"
logo_ministerio = 'http://www.mds.gov.br/webarquivos/cidadania/marca_gov/horizontal/ASSINATURA_CIDADANIA_216X64px.png'

app.layout = dbc.Container([
    # HEADER
    dbc.Row(
        [
            dbc.Col([], className='col-3'),
            dbc.Col(html.H1('Painel da Inclusão Produtiva Urbana', style={'color':'#1351B4', 'textAlign':'center', 'fontSize':40}),
                    className='col-6', style={'align':'center', 'padding':'30px'}, xs=12, sm=12, md=12, lg=12, xl=12),
            dbc.Col([], className='col-3'),
        ], className='row', align='center', style={'backgroundColor':'#FFFFF', 'box-shadow': '1px 1px 1px 1px lightgrey', 'margin-bottom':'20px'}
    ),
    # html.Br(),
    # dbc.Row(
    #         dbc.Col(
    #             [
    #                 html.Img(src=logo_progredir, style={'height': '100px'}),
    #                 html.H1("Painel da Inclusão Produtiva Urbana", style={'color':'#1351B4'})], style={'textAlign': 'center'}, xs=12, sm=12, md=12, lg=12, xl=12),
    #     align='center',
    #     justify='start',
    #     style={'backgroundColor':'#FFFFF', 'box-shadow': '1px 1px 1px 1px lightgrey'},),
    # GRID
    dbc.Row([
        # SIDEBAR
        dbc.Col([
            html.Label('Selecione a Região', style={'display': True, "width": "100%", 'color': '#0C326F', 'fontWeight': 'bold'},
                   className='mt-3'),
            dcc.Dropdown(
                id='w_municipios',
                multi=False,
                clearable=True,
                disabled=False,
                options=[{'label': i, 'value': i} for i in sorted(df['uf'].unique())],
                value='Brasil',
                placeholder="Selecione a região",
                style={'display': True, "width": "100%", 'height': '40px', 'color':'primary', 'outline':True}
            ),
            html.Br(),
            html.Label('Selecione o Município', style={'color': '#0C326F', 'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='w_municipios1',
                multi=False,
                clearable=True,
                disabled=False,
                value='Todos os Municípios',
                placeholder='Selecione o município',
                options=[],
                style={'display': True, "width": "100%", 'height': '40px'}
            ),
            html.Br(),
            dbc.Card(children=[
                dbc.CardBody(children=[
                    html.H5('População', style={'textAlign':'center', 'margin-top':'10px', }),
                    html.H4(id="populacao", style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold', 'margin-bottom':'30px'}),
                    html.H5('Produto Interno Bruto', style={'textAlign':'center'}),
                    html.H4(id="pib_total", style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold', 'margin-bottom':'30px'}),
                    html.H5('Índice de Desenvolvimento Humano', style={'textAlign':'center'}),
                    html.H4(id="idhm", style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold', 'margin-bottom':'10px'}),
                ], style={'padding':'0.30rem'}),
            ], id='data-box', color="#F8F8F8", style={"width": "100%"}),
            html.Br(),
            dbc.Button(
                "Saiba mais sobre o painel",
                id="open",
                className="mr-5",
                outline=True,
                color="dark",
                style={"width": "100%", 'fontWeight': 'bold'}
            ),
            html.Br(),
            dbc.Modal(
                [
                    dbc.ModalHeader("Sobre o painel"),
                    dbc.ModalBody(
                        "O Painel da Inclusão Produtiva Urbana tem por objetivo reunir informações que possibilitem uma "
                        "compreensão ampla do cenário social e econômico nos níveis estadual e municipal.\n\nCom isso, espera-se auxiliar gestores públicos "
                        "em nível local e parceiros do setor empresarial e da sociedade civil a "
                        "desenharem estratégias de inclusão produtiva para a população de baixa renda, em especial daquela localizada no meio urbano."
                        "Para isso, foram agregados em uma única plataforma dados sobre o contexto social - população, serviços e ações disponíveis, "
                        "a atividade econômica, empreendedorismo, microcrédito, dentre outras, obtidos a partir de um conjunto de bases públicas "
                        "governamentais.\n\nA ferramenta foi desenvolvida pelo Departamento de Inclusão Produtiva Urbana da Secretaria Nacional de "
                        "Inclusão Social e Produtiva, vinculada à Secretaria Especial do Desenvolvimento Social do Ministério da Cidadania."),
                    dbc.ModalFooter(
                        dbc.Button("Fechar", id="close", className="ml-auto")
                    ),
                ],
                id="modal",
                centered=True,
                style={"width":"90%", 'whiteSpace': 'pre-wrap'},
            ),
            html.Br(),
            dbc.Button("Saiba mais sobre o Cadastro Único", id='open1', className="mr-5", outline=True, color="dark", style={"width": "100%", 'fontWeight': 'bold'}),
            dbc.Modal(
                [
                    dbc.ModalHeader("Cadastro Único"),
                    dbc.ModalBody(
                        "O Cadastro Único para Programas Sociais do Governo Federal (Cadastro Único) é um instrumento "
                        "que identifica e caracteriza as famílias de baixa renda, permitindo que o governo conheça melhor a realidade socioeconômica dessa população.\n\n"
                        "Nele são registradas informações como: características da residência, identificação de cada pessoa, escolaridade, situação de trabalho e renda, entre outras."),
                    dbc.ModalFooter(
                        dbc.Button("Fechar", id="close1", className="ml-auto")),
                ],
                id="modal1",
                centered=True,
                style={"width":"100%", 'whiteSpace': 'pre-wrap'},
            ),
        ], xs=12, sm=12, md=2, lg=2, xl=2, style={'backgroundColor':'#FFFFF'}
        ),
        # TABS
        html.Br(),
        dbc.Col(children=[
            dbc.Tabs([
                dbc.Tab(label="Perfil das pessoas no Cadastro Único", tab_id="social", tab_style=tab_style, active_tab_style=tab_selected_style),
                dbc.Tab(label="Situação de emprego", tab_id="trabalho", tab_style=tab_style, active_tab_style=tab_selected_style),
                dbc.Tab(label="Iniciativas de Inclusão Produtiva", tab_id="servicos", tab_style=tab_style, active_tab_style=tab_selected_style)],
                id="tabs",
                active_tab="social"
            ),
            html.Div(id="tab-content", className="p-10"),
        ], xs=12, sm=12, md=10, lg=10, xl=10),
    ], justify="center"),
    html.Br(),
], fluid=True, style={'backgroundColor':'#FFFFF'})

# SELEÇÃO DE UF E MUNICÍPIO
@app.callback(
    Output('w_municipios1', 'options'),
    [Input('w_municipios', 'value')]
)
def get_municipios_options(w_municipios):
    def1 = df[df['uf'] == w_municipios]
    return [{'label': i, 'value': i} for i in def1['municipio'].unique()]

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

# POPULAÇÃO, PIB TOTAL E IDHM
@app.callback(
    Output('populacao', 'children'),
    Output('pib_total', 'children'),
    Output('idhm', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_pop_pib_idh(w_municipios, w_municipios1):
    populacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['populacao'].sum()
    populacao = f'{populacao:_.0f}'.replace('_', '.')
    df['pib_total'] = df['pib_total'].astype(float)
    pib = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_total'].sum() / 1000000
    pib = f'R$ {pib:_.2f} Bi'.replace('.', ',').replace('_', '.')
    idhm = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['idhm'].sum()

    return populacao, pib, idhm

# MODAL SOBRE O PAINEL
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
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
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
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
                                    html.P(id='cadunico', style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold'}),
                                ]),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border':'white', 'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H5("Bolsa Família (abr/2021)", className="card-title", style={'textAlign':'center'}),
                                    html.P(id='bolsa_familia', style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold'})]
                                ),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border': 'white', 'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("Pobreza e Extrema Pobreza (abr/2021)", className="card-title", style={'textAlign':'center'}),
                                    html.P(id='pobreza_extrema', style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold'})]
                                ),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border': 'white', 'box-shadow': '1px 1px 1px 1px lightgrey'})
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("Famílias de catadores (abr/2021)", className="card-title", style={'textAlign':'center'}),
                                    html.P(id='catadores', style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold'}),
                                ]),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border': 'white', 'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                ],
                    align='center'
                ),
                html.Br(),
                dbc.Row(
                    [
                    dbc.Col(dcc.Graph(id='cad_pbf'), xs=12, sm=12, md=12, lg=12, xl=8),
                    dbc.Col(dcc.Graph(id='bpc'), xs=12, sm=12, md=12, lg=12, xl=4),
                        ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='cad_sexo'), xs=12, sm=12, md=12, lg=3, xl=3),
                        dbc.Col(dcc.Graph(id='cad_domicilio', config={'displayModeBar': 'hover'}), xs=12, sm=12, md=12,
                                lg=3, xl=3),
                        dbc.Col(dcc.Graph(id='faixa_etaria'), xs=12, sm=12, md=12, lg=6, xl=6),
                    ]),
                html.Br(),
                dbc.Row([
                        dbc.Col(dcc.Graph(id='escolaridade', config={'responsive':True}), xs=12, sm=12, md=12, lg=6, xl=7),
                        dbc.Col(dcc.Graph(id='analfabetismo', config={'responsive':True}), xs=12, sm=12, md=12, lg=6, xl=5),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='evasao'), xs=12, sm=12, md=12, lg=4, xl=4),
                        dbc.Col(dcc.Graph(id='idade_serie'), xs=12, sm=12, md=12, lg=4, xl=4),
                        dbc.Col(dcc.Graph(id='remuneracao_docentes'), xs=12, sm=12, md=12, lg=4, xl=4),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='pib_setorial'), xs=12, sm=12, md=12, lg=6, xl=6),
                        html.Br(),
                        dbc.Col(
                            [
                                html.H4(id='empresas', style={'color':'#1351B4', 'textAlign':'center', 'fontSize':30, 'fontWeight':'bold'}),
                                dcc.Graph(id='empresas_setorial', config={'responsive':True})], xs=12, sm=12, md=12, lg=6, xl=6)
                    ], className='row flex-display', style={'margin-top':'20px'}
                )
            ], fluid=True
            )
        elif active_tab == "trabalho":
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
                                    html.H6("Pessoas com carteira assinada", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='empregos', style={'color':'#1351B4', 'textAlign': 'center', 'fontSize': 30, 'fontWeight': 'bold'}),
                                    html.P("Fonte: Ministério da Economia (jan/2020)", style={'textAlign': 'center', 'fontSize': 15}),
                                ]),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border': 'white', 'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("Vagas abertas no SINE (jun/2021)", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='sine', style={'color':'#1351B4', 'textAlign': 'center', 'fontSize': 30, 'fontWeight': 'bold'}),
                                    dbc.Button("Buscar vagas no SINE", outline=True, color="dark", style={"width": "100%"},
                                               href='https://www.gov.br/pt-br/servicos/buscar-emprego-no-sistema-nacional-de-emprego-sine',
                                               target="_blank"),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border': 'white', 'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("Saldo de empregos formais em 12 meses", className="card-title",
                                            style={'textAlign': 'center'}),
                                    html.P(id='saldo_empregos12', style={'color':'#1351B4', 'textAlign': 'center', 'fontSize': 30, 'fontWeight': 'bold'}),
                                    html.P(id='var_emprego', style={'textAlign': 'center', 'fontSize': 15}),
                                ]
                                ),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border': 'white', 'box-shadow': '1px 1px 1px 1px lightgrey'})
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                    dbc.Col(
                        [
                            dbc.Card(children=
                            [
                                dbc.CardBody(children=
                                [
                                    html.H6("Saldo de empregos formais em 2021", className="card-title", style={'textAlign': 'center'}),
                                    html.P(id='saldo_empregos2021', style={'color':'#1351B4', 'textAlign': 'center', 'fontSize': 30, 'fontWeight': 'bold'}),
                                    html.P("Fonte: Ministério da Economia (jan/2020)", style={'textAlign': 'center', 'fontSize': 15}),
                                ]),
                            ], color="#F8F8F8", outline=True, style={"width": "100%", 'border': 'white', 'box-shadow': '1px 1px 1px 1px lightgrey'}
                            )
                        ], xs=12, sm=12, md=12, lg=3, xl=3),
                ],
                    align='center'
                ),
                html.Br(),
                dbc.Row(
                    [
                    dbc.Col(dcc.Graph(id='funcao_principal'), xs=12, sm=12, md=12, lg=6, xl=8),
                    dbc.Col(dcc.Graph(id='trabalhou'), xs=12, sm=12, md=12, lg=6, xl=4)
                    ],
                    align='center', justify="center",
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='mei'), xs=12, sm=12, md=12, lg=4, xl=4),
                        dbc.Col(dcc.Graph(id='evolucao_empregos'), xs=12, sm=12, md=12, lg=8, xl=8),
            ], align='center', justify="center",
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col([
                            dcc.Graph(id='top_vinculos'),
                            dbc.Button(
                                "Abrir tabela com todas as ocupações",
                                id="collapse-button2",
                                className="mt-3",
                                color="dark",
                            ),
                            dbc.Collapse(
                                html.Div(id="table"),
                                id="collapse2",
                            ),
                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                        dbc.Col([
                            dcc.Graph(id='remuneracao'),
                            dbc.Button(
                                "Abrir tabela com todas as ocupações",
                                id="collapse-button3",
                                className="mt-3",
                                color="dark",
                            ),
                            dbc.Collapse(
                                html.Div(id="table2"),
                                id="collapse3",
                            ),
                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                    ], align='center', justify="center"),
                dbc.Row(
                        dbc.Col([
                            dcc.Graph(id='saldo_ocupacao'),
                            dbc.Button(
                                "Abrir tabela com todas as ocupações",
                                id="collapse-button4",
                                className="mt-3",
                                color="dark",
                            ),
                            dbc.Collapse(
                                html.Div(id="table3"),
                                id="collapse4",
                            ),
                        ], xs=12, sm=12, md=12, lg=6, xl=6)),
                html.Br(),
                # html.Div([
                #     html.Div([
                #         dcc.Dropdown(
                #             id='ocupacao',
                #             options=[{'label': i, 'value': i} for i in ocupations],
                #             value=''
                #         ),
                #         dcc.Graph(id='bar_chart2'),
                #         # dcc.RadioItems(
                #         #     id='crossfilter-xaxis-type',
                #         #     options=[{'label': i, 'value': i} for i in ['Remuneração média', 'Vínculos ativos']],
                #         #     value='Vínculos ativos',
                #         #     labelStyle={'display': 'inline-block'}
                #         # )
                #     ],
                #         style={'width': '49%', 'display': 'inline-block'}),
                #
                # ], style={
                #     'borderBottom': 'thin lightgrey solid',
                #     'backgroundColor': 'rgb(250, 250, 250)',
                #     'padding': '10px 5px'
                # }),
            ], fluid=True
            )
        elif active_tab == "servicos":
            return dbc.Container(children=[
                html.Br(),
                dbc.Row(children=
                [
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="https://www.seduc.ce.gov.br/wp-content/uploads/sites/37/2020/02/Novos-Caminhos-Preto-1200x813.jpg"),
                            dbc.CardBody(
                                [
                                    html.H5("Painel de Demandas por Qualificação Profissional", className="card-title"),
                                    html.P(
                                        "Apresenta sugestões de oferta de cursos técnicos e de qualificação profissional, por unidades"
                                        "da federação e respectivas mesorregiões, nos formatos painel interativo e relatórios em pdf.\n\n"
                                        "A ferramenta foi desenvolvida pelo Ministério da Educação em parceria com o Governo do Estao de Minas Gerais",
                                        className="card-text",
                                    ),
                                    dbc.Button("Acesse o painel", color="primary",
                                               href='http://novoscaminhos.mec.gov.br/painel-de-demandas/demandas',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="https://images.unsplash.com/photo-1531545514256-b1400bc00f31?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mzh8fHlvdW5ncyUyMGxlYXJuaW5nfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"),
                            dbc.CardBody(
                                [
                                    html.H5("Cursos de jovem aprendiz",
                                            className="card-title"),
                                    html.P(
                                        "Aprendizagem Profissional é o programa de qualificação profissional e inserção no mercado de trabalho voltado para"
                                        " jovens de 14 a 24 anos, e para pessoas com deficiência sem limite de idade.\n\n Trata-se de uma política que pode criar "
                                        "oportunidades tanto para os jovens, especialmente no que se refere à inserção no mercado de trabalho, quanto para "
                                        "as empresas, que têm a possibilidade de formar mão-de-obra qualificada.",
                                        className="card-text",
                                    ),
                                    dbc.Button("Acesse a lista de instituições", color="primary",
                                               href='http://blog.mds.gov.br/redesuas/plano-progredir-divulga-lista-de-instituicoes-que-podem-ofertar-curso-de-jovem-aprendiz/',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="https://www.gov.br/pt-br/apps/mei/view/++widget++form.widgets.imagem/@@download/MEI.png",
                                style={'height': "350px"}),
                            dbc.CardBody(
                                [
                                    html.H5("Microeempreendedorismo Individual (MEI)",
                                            className="card-title"),
                                    html.P(
                                        "O governo federal disponibiliza um portal com informações para quem deseja se formalizar como microeempreendedor"
                                        "individual, para quem já está formalizado e deseja o acesso digital a produtos e serviços financeiros.\n\n Além"
                                        "disso, o portal apresenta a legislação aplicada, estatísticas e cursos gratuitos para quem pretende se formalizar",
                                        className="card-text",
                                    ),
                                    dbc.Button("Saiba mais sobre o MEI", color="primary",
                                               href='https://www.gov.br/empresas-e-negocios/pt-br/empreendedor',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="http://www.mds.gov.br/webarquivos/cidadania/marca_gov/progredir/Marca_Progredir.png"),
                            dbc.CardBody(
                                [
                                    html.H5("Plano Progredir", className="card-title"),
                                    html.P(
                                        "É um plano de ações do Governo Federal para gerar emprego, renda e promover a construção da autonomia das pessoas inscritas "
                                        "no CADASTRO ÚNICO para programas Sociais do Governo Federal. O Progredir possui um aplicativo de internet para as pessoas "
                                        "inscritas no CADUNICO, que conta com cursos de qualificação profissional, vagas de emprego, uma área para elaboração de currículo, "
                                        "e a possibilidade de acessar microcrédito para empreender. Todos ofertados por parceiros (empresas ou entes públicos) "
                                        "em sua região de forma gratuita. ",
                                        className="card-text",
                                    ),
                                    dbc.Button("Acesse a plataforma do Progredir", color="primary",
                                               href='http://cidadania.gov.br/progredir',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="https://www.gov.br/pt-br/noticias/financas-impostos-e-gestao-publica/2020/03/governo-lanca-plataforma-para-oferta-de-produtos-e-servicos-gratuitos-a-populacao/todos-por-todos_govbr.png/@@images/9ddec400-0381-4d20-a751-28f7f2c1f2b6.png"),
                            dbc.CardBody(
                                [
                                    html.H5("Todos por Todos", className="card-title"),
                                    html.P(
                                        "A página Todos por Todos é uma campanha do Governo Federal para estimular o movimento solidário, "
                                        "captando ofertas de serviços à população e propostas de doações aos governos, para o enfrentamento "
                                        "à pandemia do novo coronavírus.",
                                        className="card-text",
                                    ),
                                    dbc.Button("Conheça o Todos por Todos", color="primary",
                                               href='http://www.gov.br/pt-br/todosportodos/cursos-ead',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="https://static.wixstatic.com/media/eafbd4_ae1f1ee9b9924e2397246a5e609880bb~mv2.jpg/v1/fit/w_828%2Ch_371%2Cal_c%2Cq_80/file.jpg"),
                            dbc.CardBody(
                                [
                                    html.H5("Escola do Trabalhador 4.0", className="card-title"),
                                    html.P(
                                        "A Escola do Trabalhador 4.0 é uma iniciativa do Ministério da Economia realizada em parceria com a Microsoft "
                                        "para promoção de qualificação e inserção profissional."
                                        "Trata-se de um programa de qualificação profissional que oferece cursos gratuitos em temas de tecnologia e produtividade. "
                                        "Com o objetivo de ajudar o trabalhador brasileiro a se preparar para o mercado de trabalho.",
                                        className="card-text",
                                    ),
                                    dbc.Button("Acesse a plataforma", color="primary",
                                               href='https://empregamais.economia.gov.br/escoladotrabalhador40/',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="http://utramig.mg.gov.br/wp-content/uploads/2021/03/Qualifica-_emprega-.png"),
                            dbc.CardBody(
                                [
                                    html.H5("Qualifica Emprega +", className="card-title"),
                                    html.P(
                                        "Qualifica Mais é uma parceria com o Ministério da Educação para a oferta de cursos de qualificação profissional, "
                                        "à distância, na área de Tecnologia da Informação e Comunicação.",
                                        className="card-text",
                                    ),
                                    dbc.Button("Acesse o site", color="primary",
                                               href='https://www.gov.br/mec/pt-br/acesso-a-informacao/institucional/secretarias/secretaria-de-educacao-profissional/projeto-piloto-qualifica-mais',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="https://infosolda.com.br/wp-content/uploads/2021/01/senai.png"),
                            dbc.CardBody(
                                [
                                    html.H5("Aprendizagem 4.0 / Mundo SENAI", className="card-title"),
                                    html.P(
                                        "O Aprendizagem 4.0 é um programa que busca qualificar jovens de 14 a 24 anos por "
                                        "meio de um currículo que contempla as competências técnicas e socioemocionais exigidas pela Indústria 4.0, "
                                        "importantes no mundo do trabalho atual. A iniciativa é uma experiência do SENAI e conta com a "
                                        "parceria da Secretaria Especial de Produtividade, Emprego e Produtividade do Ministério da Economia, "
                                        "com o objetivo de estruturar novos modelos de oferta de aprendizagem para a economia 4.0.",
                                        className="card-text",
                                    ),
                                    dbc.Button("Acesse a plataforma", color="primary",
                                               href='https://mundosenai.com.br/aprendizagem40/',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(src="https://feiraodasoportunidades.com.br/wp-content/uploads/2021/03/plat-300x190.png"),
                            dbc.CardBody(
                                [
                                    html.H5("Iniciativa 1 Milhão de Oportunidades", className="card-title"),
                                    html.P(
                                        "A iniciativa Um Milhão de Oportunidades é a maior articulação pela juventude do Brasil reunindo Nações Unidas, "
                                        "empresas, sociedade civil e governos para gerar um milhão de oportunidades de formação e acesso ao mundo do "
                                        "trabalho para adolescentes e jovens de 14 a 24 anos em situação de vulnerabilidade nos próximos dois anos",
                                        className="card-text",
                                    ),
                                    dbc.Button("Acesse a plataforma", color="primary",
                                               href='https://1mio.com.br/',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "100%", 'box-shadow': '1px 1px 1px 1px lightgrey'}),
                        html.Br(),
                    ], xs=12, sm=12, md=12, lg=4, xl=4
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

# NÚMEROS CADASTRO ÚNICO E BOLSA FAMÍLIA
@app.callback(
    Output('cadunico', 'children'),
    Output('bolsa_familia', 'children'),
    Output('pobreza_extrema', 'children'),
    Output('catadores', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_cadunico(w_municipios, w_municipios1):
    pessoas_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_cad'].sum()
    pessoas_cad = f'{pessoas_cad:_.0f}'.replace('.', ',').replace('_', '.')
    pessoas_pbf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_pbf'].sum()
    pessoas_pbf = f'{pessoas_pbf:_.0f}'.replace('.', ',').replace('_', '.')
    pobreza_extrema = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pobreza_extremapob_cad'].sum()
    pobreza_extrema = f'{pobreza_extrema:_.0f}'.replace('.', ',').replace('_', '.')
    catadores = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['familias_catadores_cad '].sum()
    catadores = f'{catadores:_.0f}'.replace('.', ',').replace('_', '.')

    return pessoas_cad + ' pessoas', pessoas_pbf + ' pessoas', pobreza_extrema + ' pessoas', catadores + ' famílias'

# NÚMEROS CADASTRO ÚNICO E BOLSA FAMÍLIA
@app.callback(
    Output('bpc', 'figure'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_bpc(w_municipios, w_municipios1):
    bpc_total = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['bpc_ben'].astype('int').sum()
    bpc_total = f'{bpc_total:_.0f}'.replace('.', ',').replace('_', '.')
    bpc_deficiencia = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['bpc_pcd_ben'].astype('int').sum()
    bpc_deficiencia = f'{bpc_deficiencia:_.0f}'.replace('.', ',').replace('_', '.')
    bpc_idosos = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['bpc_idoso_ben'].astype('int').sum()
    bpc_idosos = f'{bpc_idosos:_.0f}'.replace('.', ',').replace('_', '.')

    fig = go.Figure()
    fig.add_trace(go.Bar(x=['Beneficiários', 'Portador deficiência', 'Idoso'],
                         y=[bpc_total, bpc_deficiencia, bpc_idosos], name='BPC', marker=dict(color='#1351B4')))

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=1,
            ticks='outside',
            tickfont=dict(family='Arial', size=11, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        plot_bgcolor='white'
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Beneficío de Prestação Continuada',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, fev/2021',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))
    fig.update_layout(annotations=annotations)

    return fig

# EVOLUÇÃO DO CADUNICO E DO PBF
@app.callback(Output('cad_pbf', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_ev_cadunico(w_municipios, w_municipios1):
    # result = pd.concat([df, df_cad], ignore_index=True, sort=False)
    df1 = df_cad[(df_cad['municipio'] == w_municipios1) & (df_cad['uf'] == w_municipios)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df1['mês_ano'], y=df1['pessoas_pbf'], name='Bolsa Família', mode='lines+markers',
                             marker=dict(size=10, color='black')))
    fig.add_trace(go.Scatter(x=df1['mês_ano'], y=df1['pessoas_cad'], name='Cadastro Único', mode='lines+markers',
                             marker=dict(size=10, color='#f94144')))
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=1,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=10,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=True,
        hovermode="x unified",
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor='white',
    )
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.00,
        xanchor="right",
        x=1
    ))

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.15,
                            xanchor='left', yanchor='bottom',
                            text='Evolução do nº de pessoas inscritas no CadÚnico e de<br>beneficiárias do Bolsa Família (2018-2021)',
                            font=dict(family='Arial', size=16, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, abr/2021',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))
    fig.update_layout(annotations=annotations)

    return fig

# POPULAÇÃO DO CADUNICO POR SITUAÇÃO DO DOMICÍLIO E SEXO
@app.callback(Output('cad_domicilio', 'figure'),
              Output('cad_sexo', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_domicilio_sexo(w_municipios, w_municipios1):
    urbano = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pes_cad_urbano'].sum()
    rural = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pes_cad_rural'].sum()
    masc_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_masculino'].sum()
    fem_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_feminino'].sum()

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=['Masculino'], y=[masc_cad], name='Masculino', marker=dict(color='#1351B4')))
    fig1.add_trace(go.Bar(x=['Feminino'], y=[fem_cad], name='Feminino', marker=dict(color='#F08080')))
    fig1.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=1,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
            titlefont_size=12,
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        # legend=dict(
        #     x=1,
        #     y=1.0,
        #     bgcolor='rgba(255, 255, 255, 0)',
        #     bordercolor='rgba(255, 255, 255, 0)'
        # ),
        plot_bgcolor='white',
        showlegend=False,
        barmode='group',
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='População do CadÚnico,<br>por sexo',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, abr/2021',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))

    fig1.update_layout(annotations=annotations)

    fig2 = go.Figure()

    colors = ['#1351B4', '#f6bd60']
    fig2.add_trace(go.Pie(labels=['Urbano', 'Rural'], values=[urbano, rural], name='Domicílio', marker=dict(colors=colors), hole=.5, textfont={'family': "Arial", 'size': 15}))

    fig2.update_layout(
        xaxis_tickfont_size=14,
        yaxis=dict(
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=-0.3,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='População do CadÚnico,<br>situação do domicílio',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, abr/2021',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))

    fig2.update_layout(annotations=annotations)

    return fig1, fig2

# POPULAÇÃO DO CADUNICO POR FAIXA ETÁRIA
@app.callback(Output('faixa_etaria', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_age(w_municipios, w_municipios1):
    faixa = ['16 a 17', '18 a 24', '25 a 34', '35 a 39', '40 a 44', '45 a 49', '50 a 54', '55 a 59', '60 a 64']
    populacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_cad'].sum()
    faixa16_17 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_16_17_anos'].sum()
    perc_faixa16_17 = (faixa16_17/populacao*100).round(1)
    faixa18_24 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_18_24_anos'].sum()
    perc_faixa18_24 = (faixa18_24 / populacao * 100).round(1)
    faixa25_34 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_25_34_anos'].sum()
    perc_faixa25_34 = (faixa25_34 / populacao * 100).round(1)
    faixa35_39 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_35_39_anos'].sum()
    perc_faixa35_39 = (faixa35_39 / populacao * 100).round(1)
    faixa40_44 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_40_44_anos'].sum()
    perc_faixa40_44 = (faixa40_44 / populacao * 100).round(1)
    faixa45_49 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_45_49_anos'].sum()
    perc_faixa45_49 = (faixa45_49 / populacao * 100).round(1)
    faixa50_54 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_50_54_anos'].sum()
    perc_faixa50_54 = (faixa50_54 / populacao * 100).round(1)
    faixa55_59 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_55_59_anos'].sum()
    perc_faixa55_59 = (faixa55_59 / populacao * 100).round(1)
    faixa60_64 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_60_64_anos'].sum()
    perc_faixa60_64 = (faixa60_64 / populacao * 100).round(1)


    fig = go.Figure()
    fig.add_trace(go.Bar(x=faixa, y=[faixa16_17, faixa18_24, faixa25_34, faixa35_39, faixa40_44, faixa45_49, faixa50_54, faixa55_59, faixa60_64],
                         showlegend=False, textposition='auto', name='Faixa Etária', text=[perc_faixa16_17, perc_faixa18_24, perc_faixa25_34,
                                                                                           perc_faixa35_39, perc_faixa40_44, perc_faixa45_49, perc_faixa50_54,
                                                                                           perc_faixa55_59, perc_faixa60_64],
                         marker=dict(color='#1351B4')))

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=False,
        margin=dict(autoexpand=True),
        plot_bgcolor='white'
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='População do Cadastro Único,<br>por faixa etária',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, abr/2021',
                            font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)

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
    perc_sem_instrucao = (sem_instrucao / populacao * 100).round(1)
    fund_incompleto = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_fundamental_incompleto'].sum()
    perc_fund_incompleto = (fund_incompleto / populacao * 100).round(1)
    fund_completo = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_fundamental_completo'].sum()
    perc_fund_completo = (fund_completo / populacao * 100).round(1)
    medio_incompleto = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_medio_incompleto'].sum()
    perc_medio_incompleto = (medio_incompleto / populacao * 100).round(1)
    medio_completo = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_medio_completo'].sum()
    perc_medio_completo = (medio_completo / populacao * 100).round(1)
    superior = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_superior_completo_incompleto'].sum()
    perc_superior = (superior / populacao * 100).round(1)

    sabe_ler_escrever = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['sabe_ler_escrever'].sum()
    nao_sabe_ler_escrever = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['não_sabe_ler_escrever'].sum()

    fig = go.Figure()
    fig.add_trace(go.Bar(x=nivel, y=[sem_instrucao, fund_incompleto, fund_completo, medio_incompleto, medio_completo, superior],
                         text=[perc_sem_instrucao, perc_fund_incompleto, perc_fund_completo, perc_medio_incompleto, perc_medio_completo,
                               perc_superior], name='Escolaridade', marker=dict(color='#2670E8'), textposition='auto'))
    fig.update_layout(bargap=0.25, bargroupgap=0.2)
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=10, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=False,
        margin=dict(autoexpand=True),
        plot_bgcolor='white'
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='População do Cadastro Único, por<br>nível de escolaridade',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, fev/2021',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)

    fig2 = go.Figure()
    colors = ['#f6bd60', '#1351B4']
    fig2.add_trace(go.Pie(labels=['Sabe ler e escrever', 'Não sabe ler e escrever'], values=[sabe_ler_escrever, nao_sabe_ler_escrever], showlegend=True,
                         name='Analfabetismo', hole=.5, marker=dict(colors=colors), textfont={'family': "Arial", 'size': 15}))

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='População do CadÚnico,<br>por alfabetização',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.7, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, fev/2021',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))

    fig2.update_layout(annotations=annotations)

    return fig, fig2

# DISTORÇÃO IDADE-SÉRIE, EVASÃO E REMUNERAÇÃO PROFESSORES
@app.callback(
    Output('idade_serie', 'figure'),
    Output('remuneracao_docentes', 'figure'),
    Output('evasao', 'figure'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_idade_serie(w_municipios, w_municipios1):
    remuneracao_brasil = df[(df['uf'] == 'Brasil') & (df['municipio'] == 'Todos os Municípios')]['remuneracao_docente_edbasica'].sum()
    remuneracao_municipio = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['remuneracao_docente_edbasica'].sum()

    evasao_brasil = df['taxa_evasao_abandono'].mean()
    evasao_municipio = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['taxa_evasao_abandono'].sum()

    idade_serie_brasil = df['distorcao_idade_serie'].mean()
    idade_serie = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['distorcao_idade_serie'].sum()

    municipio = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['municipio']

    fig = go.Figure()
    fig.add_trace(go.Bar(x=['Brasil', municipio], y=[evasao_brasil, evasao_municipio]))
    fig.update_layout(
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)',
            linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=10, color='rgb(82, 82, 82)'),),
        yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False,),
        autosize=True, margin=dict(autoexpand=True), plot_bgcolor='white')

    annotations = []

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Taxa de evasão escolar',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'), showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top', text='Fonte: INEP, 2020',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'), showarrow=False))

    fig.update_layout(annotations=annotations)

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=['Brasil', municipio], y=[remuneracao_brasil, remuneracao_municipio]))

    fig2.update_layout(
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)',
            linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=10, color='rgb(82, 82, 82)'),),
        yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False,),
        autosize=True, margin=dict(autoexpand=True), plot_bgcolor='white'
    )

    annotations = []

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom', text='Remuneração média dos docentes<br>da educação básica',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'), showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top', text='Fonte: INEP, 2020',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'), showarrow=False))

    fig2.update_layout(annotations=annotations)

    fig3 = go.Figure()
    fig3.add_trace(go.Bar(x=['Brasil', municipio], y=[idade_serie_brasil, idade_serie]))

    fig3.update_layout(
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)',
            linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=10, color='rgb(82, 82, 82)'),),
        yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False,),
        autosize=True, margin=dict(autoexpand=True), plot_bgcolor='white')

    annotations = []

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom', text='Taxa de distorção idade-série',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'), showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top', text='Fonte: INEP, 2020',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'), showarrow=False))

    fig3.update_layout(annotations=annotations)

    return fig, fig2, fig3

# NÚMEROS SOBRE EMPRESAS E ESTOQUE DE EMPREGOS
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
                         showlegend=True, name='Setor', hoverinfo='label+value', textinfo='percent', hole=.5, textfont={'family': "Arial", 'size': 15}))

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='PIB por setor de<br>atividade econômica',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: IBGE, 2018',
                            font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations, hovermode='closest')

    return fig

# NÚMERO DE EMPRESAS POR SETOR DE ATIVIDADE ECONÔMICA
@app.callback(Output('empresas_setorial', 'figure'),
              Output('empresas', 'children'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_empresas(w_municipios, w_municipios1):
    setores = ['Agropecuária', 'Indústria<br>Extrativa', 'Indústria de<br>Transformação', 'Construção', 'Comércio', 'Transporte', 'Alojamento e<br>Alimentação', 'Informação e<br>Comunicação',
               'Atividades Científicas<br>e Técnicas', 'Atividades< >Administrativas',
               'Educação', 'Saúde', 'Arte, Cultura e<br>Esportes', 'Outras Atividades']
    agropecuaria = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_agropecuaria'].sum()
    ind_extrativa = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_ind_extrativas'].sum()
    ind_transf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_ind_transf'].sum()
    # eletric_gas = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_eletric_gas'].sum()
    # saneamento = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_saneamento'].sum()
    construcao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_construcao'].sum()
    comercio = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_comercio'].sum()
    transporte = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_transporte'].sum()
    aloj_alimentacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_alojamento_alimentacao'].sum()
    info_comunic = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_info_comunic'].sum()
    # financeiro = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_financeiro'].sum()
    # imobiliarias = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_imobiliarias'].sum()
    ativ_prof = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_ativ_profissionais_cient_tecnicas'].sum()
    ativ_administrativas = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_ativ_administrativas'].sum()
    educacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_educacao'].sum()
    saude = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_saude_servicosocial'].sum()
    arte_cultura = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_arte_cultura'].sum()
    outras_ativ = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_outras_ativ_servicos'].sum()

    empresas = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_total'].sum()
    empresas1 = f'{empresas:_.0f}'.replace('_', '.')

    fig = go.Figure()
    fig.add_trace(go.Bar(x=setores, y=[agropecuaria, ind_extrativa, ind_transf, construcao, comercio, transporte,
                    aloj_alimentacao, info_comunic, ativ_prof, ativ_administrativas, educacao, saude, arte_cultura, outras_ativ],
                         name='Atividade', marker=dict(color='#2670E8')))

    fig.update_layout(bargap=0.25, bargroupgap=0.2)
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=10, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        plot_bgcolor='white'
    )

    annotations = []

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Número de empresas, por setor<br>de atividade econômica',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: IBGE/CEMPRE, 2018',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)

    return fig, empresas1 + ' empresas'

# VAGAS ABERTAS NO SINE
@app.callback(Output('sine', 'children'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_sine(w_municipios, w_municipios1):
    vagas_sine = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['vagas_sine'].sum()
    return vagas_sine

# SALDO E VARIAÇÃO DE EMPREGOS
@app.callback(
    Output('saldo_empregos12', 'children'),
    Output('saldo_empregos2021', 'children'),
    Output('var_emprego', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def display_saldo_empregos_recente(w_municipios, w_municipios1):
    df1 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2021'].sum()
    df1 = f'{df1:_.0f}'.replace('.', ',').replace('_', '.')
    df2 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos_12meses'].sum()
    df2 = f'{df2:_.0f}'.replace('.', ',').replace('_', '.')
    df3 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['var_saldo_empregos_12meses'].sum()

    return df2, df1, df3

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
                             marker=dict(size=10, color='#1351B4')
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
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)',
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
        margin=dict(autoexpand=True),
        showlegend=False,
        plot_bgcolor='white'
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Evolução do saldo de empregos formais (2002-2019)',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Economia/RAIS, 2020',
                            font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)

    return fig

# POPULAÇÃO DO CADUNICO POR FUNÇÃO PRINCIPAL E TRABALHO
@app.callback(Output('funcao_principal', 'figure'),
              Output('trabalhou', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_cad_funcao(w_municipios, w_municipios1):
    funcao_principal = ['Autônomo', 'Temporário na<br>Área Rural', 'Emprego sem<br>Carteira', 'Emprego com<br>Carteira', 'Trabalho Doméstico<br>sem Carteira',
             'Trabalho Doméstico<br>com Carteira', 'Trabalho não<br>Remunerado', 'Militar/Servidor<br>Público', 'Empregador', 'Estagiário', 'Aprendiz']
    trab_autonomo = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trab_autonomo'].sum()
    trab_temp_area_rural = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trab_temp_area_rura'].sum()
    emprego_sem_carteira = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['emprego_sem_carteira'].sum()
    emprego_com_carteira = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['emprego_com_carteira'].sum()
    trab_domestico_sem_carteira = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trab_domestico_sem_carteira'].sum()
    trab_domestico_com_carteira = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trab_domestico_com_carteira'].sum()
    trabalhador_nao_remunerado = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trabalhador_não_remunerado'].sum()
    militar_servidor_publico = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['militar_servidor_publico'].sum()
    empregador = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empregador'].sum()
    estagiario = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['estagiario'].sum()
    aprendiz = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['aprendiz'].sum()

    trab_12_meses = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trab_12_meses'].sum()
    nao_trab_12_meses = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['não_trab_12_meses'].sum()

    trab_last_week = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['trab_semana_passada'].sum()
    nao_trab_last_week = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['não_trab_semana_passada'].sum()

    fig1 = go.Figure()

    fig1.add_trace(go.Bar(x=funcao_principal,
                         y=[trab_autonomo, trab_temp_area_rural, emprego_sem_carteira, emprego_com_carteira, trab_domestico_sem_carteira,
                            trab_domestico_com_carteira, trabalhador_nao_remunerado, militar_servidor_publico, empregador, estagiario, aprendiz],
                          textposition='inside', name='Função Principal', marker=dict(color='#0C326F')))
    fig1.update_layout(bargap=0.25, bargroupgap=0.2)
    fig1.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=1,
            ticks='outside',
            tickfont=dict(family='Arial', size=10, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=False,
        plot_bgcolor='white'
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='População do CadÚnico, por função<br> principal e frequência do trabalho',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.25,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, fev/2021',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))

    fig1.update_layout(annotations=annotations)

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        y=[trab_12_meses, trab_last_week],
        x=['Trabalhou nos últimos<br>12 meses', 'Trabalhou na<br>última semana'], textposition='inside',
        name='Sim',
        marker=dict(
            color='#0C326F',
            line=dict(color='white', width=1)
        )
    ))
    fig2.add_trace(go.Bar(
        y=[nao_trab_12_meses, nao_trab_last_week],
        x=['Trabalhou nos últimos<br>12 meses', 'Trabalhou na<br>última semana'], textposition='inside',
        name='Não',
        marker=dict(
            color='#f8961e',
            line=dict(color='white', width=1)
        )
    ))

    fig2.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=False,
        margin=dict(autoexpand=True),
        showlegend=False,
        plot_bgcolor='white',
        # barmode = 'stack'
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Situação de trabalho nos últimos<br>12 meses e na última semana',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Cadastro Único, fev/2021',
                            font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
                            showarrow=False))

    fig2.update_layout(annotations=annotations)

    return fig1, fig2

# EVOLUÇÃO DA REMUNERAÇÃO TOTAL
@app.callback(Output('remuneracao', 'figure'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_remuneracao_ocupacoes(w_municipios, w_municipios1):
    # result = pd.merge(df_remuneracao, df_geral, on=['uf', 'municipio'])
    df2 = df_remuneracao[(df_remuneracao['municipio'] == w_municipios1) & (df_remuneracao['uf'] == w_municipios)]
    df3 = df2.groupby('ano')['Total'].sum()
    df3 = df3.reset_index()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df3['ano'], y=df3['Total'], marker=dict(color='#0C326F')))
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=True,
            showline=False,
            showticklabels=True,
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=False,
        plot_bgcolor='white'
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Evolução da remuneração média mensal<br>(Em número de salários mínimo)',
                            font=dict(family='Arial', size=18, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Economia/RAIS, 2020',
                            font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)

    return fig

# PLANILHA COM A REMUNERAÇÃO DE TODAS AS OCUPAÇÕES
@app.callback(
    Output('table2', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_remuneracao_table(w_municipios, w_municipios1):
    df1 = df_remuneracao.melt(id_vars=["uf", "municipio", "regiao", "pais", "ano"], var_name="Ocupação", value_name="Remuneração")
    df2 = df1[(df1['municipio'] == w_municipios1) & (df1['uf'] == w_municipios) & (df1['ano'] == 2019)]
    df2 = df2.iloc[1:, :]
    data = df2.to_dict('records')
    columns = [{"name": i, "id": i,} for i in df2[['Ocupação', 'Remuneração']]]
    export_format = "xlsx"
    return dash_table.DataTable(data=data, columns=columns, export_format=export_format, filter_action='native',
                                page_action = "native", page_current=0, page_size=10, sort_action='native', export_headers="display",
                                style_as_list_view=True, style_header={'backgroundColor': '#0C326F', 'color':'white', 'fontWeight': 'bold', 'fontFamily':'Arial', 'fontSize':12},
                                style_cell={'backgroundColor': 'white', 'color': 'black', 'fontFamily':'Arial', 'fonteSize':12,
                                            'minWidth': 95, 'width': 95, 'maxWidth': 95},
                                )

# EMPREENDEDORISMO
@app.callback(Output('mei', 'figure'),
              # Output('mei_pbf', 'children'),
              Input('w_municipios', 'value'),
              Input('w_municipios1', 'value')
              )
def display_mei(w_municipios, w_municipios1):
    mei_cadunico = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['mei_cadunico'].astype('int').sum()
    mei_cadunico = f'{mei_cadunico:_.0f}'.replace('.', ',').replace('_', '.')
    mei_pbf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['mei_pbf'].astype('int').sum()
    mei_pbf = f'{mei_pbf:_.0f}'.replace('.', ',').replace('_', '.')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=[mei_cadunico, mei_pbf], x=['Cadastro Único', 'Bolsa Família'], textposition='inside', name='MEI',
        marker=dict(color='#f8961e', line=dict(color='white', width=1)
        )
    ))

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=False,
        plot_bgcolor='white',
    )

    annotations = []
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Microeempreendedor Indivudual (MEI)',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Cidadania/Ministério da Economia, jul/2020',
                            font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)


    return fig

# OCUPAÇÕES COM MAIORES VINCULOS
@app.callback(
    Output('top_vinculos', 'figure'),
    # [Input('dropdown', 'value')],
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_top_vinculos(w_municipios, w_municipios1):
    df2 = df_caged.melt(id_vars=["uf", "municipio", "ibge6", "regiao", "pais", "ano"],
                          var_name="ocupation",
                          value_name="vinculos")
    df2['vinculos'] = df2['vinculos'].astype('int')
    df2['ocupation'] = df2['ocupation'].str.capitalize()
    df3 = df2[(df2['municipio'] == w_municipios1) & (df2['uf'] == w_municipios) & (df2['ano'] == 2019)]
    # df_caged1['ocupation'] = df_caged1['ocupation'].astype('float')
    # df1 = pd.concat([df, df_caged1], axis=1)
    # df2 = df1[(df1['uf'] == w_municipios) & (df1['municipio'] == w_municipios1) & (df1['ocupation'] == ocupation)]
    # mask = df_caged1['uf'] == w_municipios
    # mask = df_caged1['municipio'] == w_municipios1
    # mask = df_caged1['ocupation'] == ocupation
    # fig = px.bar(df_caged1[mask], x='ano', y='vinculos')
    #
    # result = pd.concat([df_caged11, df], axis=1)
    # df1 = result[(result['uf'] == w_municipios) & (result['municipio'] == w_municipios1)]

    df4 = df3.nlargest(6, 'vinculos')
    df5 = df4.iloc[1: , :]

    fig = go.Figure()

    fig.add_trace(go.Pie(labels=df5['ocupation'], values=df5['vinculos'],
                          hoverinfo='label+value', textinfo='percent', hole=.5, textfont={'family': "Arial", 'size': 12}))

    annotations = []

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Ocupações com maior quantidade<br>de vínculos',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Economia/RAIS, 2020',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))


    fig.update_layout(annotations=annotations)
    return fig

# PLANILHA COM TODOS AS OCUPAÇÕES POR QUANTIDADE DE VÍNCULOS
@app.callback(
    Output('table', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_top_vinculos_table(w_municipios, w_municipios1):
    df1 = df_caged.melt(id_vars=["uf", "municipio", "regiao", "pais", "ano"], var_name="Ocupação", value_name="Quantidade de Vínculos")
    df2 = df1[(df1['municipio'] == w_municipios1) & (df1['uf'] == w_municipios) & (df1['ano'] == 2019)]
    df2 = df2.iloc[1:, :]
    data = df2.to_dict('records')
    columns = [{"name": i, "id": i,} for i in df2[['Ocupação', 'Quantidade de Vínculos']]]
    export_format = "xlsx"
    return dash_table.DataTable(data=data, columns=columns, export_format=export_format, filter_action='native',
                                page_action = "native", page_current=0, page_size=10, sort_action='native', export_headers="display",
                                style_as_list_view=True, style_header={'backgroundColor': '#0C326F', 'color':'white', 'fontWeight': 'bold', 'fontFamily':'Arial', 'fontSize':12},
                                style_cell={'backgroundColor': 'white', 'color': 'black', 'fontFamily':'Arial', 'fonteSize':12,
                                            'minWidth': 95, 'width': 95, 'maxWidth': 95},
                                )

# OCUPAÇÕES COM MAIORES VINCULOS
@app.callback(
    Output('saldo_ocupacao', 'figure'),
    # [Input('dropdown', 'value')],
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_saldo_vinculos(w_municipios, w_municipios1):
    df2 = df_saldo.melt(id_vars=["uf", "municipio", "ibge", "regiao", "pais", "ano"],
                          var_name="ocupation",
                          value_name="saldo")
    df2['ocupation'] = df2['ocupation'].str.capitalize()
    df3 = df2[(df2['municipio'] == w_municipios1) & (df2['uf'] == w_municipios) & (df2['ano'] == 2019)]

    df3 = df3.nlargest(6, 'saldo')
    df3 = df3.iloc[1: , :]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=df3['saldo'], x=df3['ocupation'], textposition='inside', name='Saldo',
        marker=dict(color='#f8961e', line=dict(color='white', width=1)
        )))

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=2,
            ticks='outside',
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)'),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=False,
        plot_bgcolor='white',
    )

    annotations = []

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                            xanchor='left', yanchor='bottom',
                            text='Ocupações com maior saldo<br>de empregos formais',
                            font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
                            xanchor='center', yanchor='top',
                            text='Fonte: Ministério da Economia/RAIS, 2020',
                            font=dict(family='Arial', size=13, color='rgb(150,150,150)'),
                            showarrow=False))


    fig.update_layout(annotations=annotations)
    return fig

# PLANILHA COM TODOS AS OCUPAÇÕES POR QUANTODADE DE VÍNCULOS
@app.callback(
    Output('table3', 'children'),
    Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')
)
def update_saldo_vinculos_table(w_municipios, w_municipios1):
    df1 = df_saldo.melt(id_vars=["uf", "municipio", "regiao", "pais", "ano"], var_name="Ocupação", value_name="Saldo de Empregos")
    df2 = df1[(df1['municipio'] == w_municipios1) & (df1['uf'] == w_municipios) & (df1['ano'] == 2019)]
    df2 = df2.iloc[1:, :]
    data = df2.to_dict('records')
    columns = [{"name": i, "id": i,} for i in df2[['Ocupação', 'Saldo de Empregos']]]
    export_format = "xlsx"
    return dash_table.DataTable(data=data, columns=columns, export_format=export_format, filter_action='native',
                                page_action = "native", page_current=0, page_size=10, sort_action='native', export_headers="display",
                                style_as_list_view=True, style_header={'backgroundColor': '#0C326F', 'color':'white', 'fontWeight': 'bold', 'fontFamily':'Arial', 'fontSize':12},
                                style_cell={'backgroundColor': 'white', 'color': 'black', 'fontFamily':'Arial', 'fonteSize':12,
                                            'minWidth': 95, 'width': 95, 'maxWidth': 95},
                                )

# # EVOLUCAO DOS VINCULOS POR OCUPAÇÃO
# # @app.callback(
# #     Output('bar_chart2', 'figure'),
# #     [Input('ocupacao', 'value')],
# #     [Input('w_municipios', 'value')],
# #     [Input('w_municipios1', 'value')],
# # )
# # def update_barchart2(w_municipios, w_municipios1, vinculos_ocupacao):
# #     # df1 = df_remuneracao2.melt(id_vars=["uf", "municipio", "ibge6", 'ano'],
# #     #         var_name="ocupation",
# #     #         value_name="remuneracao")
# #     df1 = df10[(df10['municipio'] == w_municipios1) & (df10['uf'] == w_municipios) & (df10['ocupation'] == ocupacao)]
# #
# #     #     # df_caged1['ocupation'] = df_caged1['ocupation'].astype('float')
# #     #     # df1 = pd.concat([df, df_caged1], axis=1)
# #     #     # df2 = df1[(df1['uf'] == w_municipios) & (df1['municipio'] == w_municipios1) & (df1['ocupation'] == ocupation)]
# #     #     # mask = df_caged1['uf'] == w_municipios
# #     #     # mask = df_caged1['municipio'] == w_municipios1
# #     #     # mask = df_caged1['ocupation'] == ocupation
# #     #     # fig = px.bar(df_caged1[mask], x='ano', y='vinculos')
# #     #
# #     fig = go.Figure()
# #     fig.add_trace(go.Bar(x=df1['ano'], y=df1['vinculos'], name='Total de vínculos, por ano'))
# #
# #     fig.update_layout(bargap=0.25, bargroupgap=0.2)
# #     fig.update_layout(
# #         xaxis=dict(
# #             showline=True,
# #             showgrid=False,
# #             showticklabels=True,
# #             linecolor='rgb(204, 204, 204)',
# #             linewidth=2,
# #             ticks='outside',
# #             tickfont=dict(
# #                 family='Arial',
# #                 size=12,
# #                 color='rgb(82, 82, 82)',
# #             ),
# #         ),
# #         yaxis=dict(
# #             showgrid=False,
# #             zeroline=False,
# #             showline=False,
# #             showticklabels=False,
# #         ),
# #         autosize=False,
# #         margin=dict(
# #             autoexpand=False,
# #             l=100,
# #             r=20,
# #             t=110,
# #         ),
# #         showlegend=False,
# #         plot_bgcolor='white'
# #     )
# #
# #     annotations = []
# #     # Title
# #     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
# #                             xanchor='left', yanchor='bottom',
# #                             text='Remuneração média',
# #                             font=dict(family='Arial',
# #                                       size=20,
# #                                       color='rgb(37,37,37)'),
# #                             showarrow=False))
# #     # Source
# #     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
# #                             xanchor='center', yanchor='top',
# #                             text='Fonte: Ministério da Economia/RAIS',
# #                             font=dict(family='Arial',
# #                                       size=15,
# #                                       color='rgb(150,150,150)'),
# #                             showarrow=False))
# #
# #     fig.update_layout(annotations=annotations)
# #
# #     return fig
#
# # MAPA COM UNIDADES DE SAÚDE
# # fig10 = px.scatter_mapbox(df5, lat="nu_latitude", lon="nu_longitude", text='no_fantasia',
# #                           color_continuous_scale=px.colors.cyclical.IceFire, size_max=200, zoom=0)
# #
# # fig10.update_layout(
# #     hovermode='closest',
# #     mapbox=dict(
# #         style='open-street-map',
# #         domain={'x': [1, 1], 'y': [1, 1]},
# #         bearing=0,
# #         center=dict(
# #             lat=-14,
# #             lon=-53
# #         ),
# #         pitch=0,
# #         zoom=5
# #     ),
# # )

if __name__ == '__main__':
    app.run_server(debug=True)





