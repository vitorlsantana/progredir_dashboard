import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# suppress_callback_exceptions=True
server = app.server

# CARREGAR DADOS
data = 'https://raw.githubusercontent.com/vitorlsantana/progredir_dashboard/main/base_painel_inclus%C3%A3o_produtiva.csv'
df = pd.read_csv(data, sep=';', encoding='latin1')

# data1 = 'https://github.com/vitorlsantana/progredir_dashboard/blob/ff0df63a3acd93453c376a0a1555714aa7d588c6/vinculos_ativos_ocupacao_subgruposprincipais_2015_2019.csv'
# df_caged = pd.read_csv(data1, sep=';', encoding='latin1')
# df_caged_melted = df_caged.melt(id_vars=["uf", "municipio", "ibge6", 'ano'],
#                                 var_name="ocupation",
#                                 value_name="vinculos")
# ocupations = df_caged_melted['ocupation'].unique()

# data2 = 'https://github.com/vitorlsantana/progredir_dashboard/blob/ff0df63a3acd93453c376a0a1555714aa7d588c6/evolucao_pessoas_cad_pbf.csv'
# df_cad = pd.read_csv(data2, sep=';', encoding='latin1')
#
# data3 = 'https://github.com/vitorlsantana/progredir_dashboard/blob/ff0df63a3acd93453c376a0a1555714aa7d588c6/remuneracao_SM_ocupacao_subgruposprincipais_2015_2019.csv'
# df_remuneracao = pd.read_csv(data3, sep=';', encoding='latin1')

# data4 = 'C:\\Users\\Vitor Santana\\PycharmProjects\\painelProgredir\\cnes localizacao e regiao saude.csv'
# df5 = pd.read_csv(data4, sep=',', error_bad_lines=False)

# --------------------------------------------------------------------------------------------------------------------------------------------
# NAVBAR
logo_progredir = "http://www.mds.gov.br/webarquivos/cidadania/marc" \
                 "a_gov/progredir/Marca_Progredir.png"
logo_ministerio = 'http://www.mds.gov.br/webarquivos/cidadania/marca_gov/horizontal/ASSINATURA_CIDADANIA_216X64px.png'

logo = dbc.Row(
    [
        dbc.Col(html.Img(src=logo_ministerio, height="90px")),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-1 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.Div(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=logo_progredir, height="175px")),
                    dbc.Col(dbc.NavbarBrand("Painel da Inclusão Produtiva Urbana", className="ml-15",
                                            style={'color': '#1E3248', 'fontSize': 40, 'fontWeight': 'bold'})),
                ],
                align="center",
                no_gutters=True,
            ),
            className="ml-auto flex-nowrap mt-3 mt-md-0",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(logo, id="navbar-collapse", navbar=True),
    ],
    color="light",
    dark=True,
    style={"border": "1px #EBEBEB solid"}
)

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# ----------------------------------------------------------------------------------------------------------------------
# LAYOUT
# Dropdwon

state = df['uf'].unique()

sidebar = dbc.Container(
    [
        html.P('Selecione a UF', style={'display': True, "width": "20rem", 'color': '#1E3248', 'fontWeight': 'bold'},
               className='mt-3'),
        dcc.Dropdown(
            id='w_municipios',
            multi=False,
            clearable=True,
            disabled=False,
            options=[{'label': i, 'value': i} for i in state],
            value='Alagoas',
            placeholder="Selecione a UF",
            style={'display': True, "width": "18rem", 'height': '40px'}
        ),
        html.Br(),
        html.P('Selecione o Município', style={'color': '#1E3248', 'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='w_municipios1',
            multi=False,
            clearable=True,
            disabled=False,
            value='',
            placeholder='Selecione o município',
            options=[],
            style={'display': True, "width": "18rem", 'height': '40px'}
        ),
        html.Br(),
        dbc.Card(children=[
            dbc.CardBody(children=[
                html.H6('População'),
                html.H4(id="populacao"),
                html.Br(),
                html.H6('PIB'),
                html.H4(id="pib_total"),
                html.Br(),
                html.H6('IDHM'),
                html.H4(id="idhm"),
            ]
            ),
        ],
            id='data-box',
            color="dark", inverse=True,
            style={"width": "18rem"}
        ),
        html.Br(),
        dbc.Button(
            "Saiba mais sobre o painel",
            id="collapse-button",
            className="mr-5",
            outline=True,
            color="dark",
            style={"width": "18rem", 'fontWeight': 'bold'}
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(
                "O Painel da Inclusão Produtiva Urbana tem por objetivo reunir informações que possibilitem uma "
                "compreensão ampla do cenário social e econômico nos níveis estadual e municipal.\n\nCom isso, espera-se auxiliar gestores públicos em nível local e parceiros do setor empresarial e da sociedade civil a "
                "desenharem estratégias de inclusão produtiva para a população de baixa renda, em especial daquela localizada no meio urbano."
                "Para isso, foram agregados em uma única plataforma dados sobre o contexto social -- população, serviços e ações disponíveis, "
                "a atividade econômica, empreendedorismo, microcrédito, dentre outras, obtidos a partir de um conjunto de bases públicas "
                "governamentais.\n\nA ferramenta foi desenvolvida pelo Departamento de Inclusão Produtiva Urbana da Secretaria Nacional de "
                "Inclusão Social e Produtiva, vinculada à Secretaria Especial do Desenvolvimento Social do Ministério da Cidadania."),
                     style={"width": "18rem", 'whiteSpace': 'pre-wrap'}
                     ),
            id="collapse2",
        ),
    ], fluid=True
)

@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse2", "is_open")],
)
def toggle_collapse2(n, is_open):
    if n:
        return not is_open
    return is_open
#
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
    [State('w_municipios1', 'value')]
)
def get_municipios_value(w_municipios1):
    return [k['value'] for k in w_municipios1][0]
#
# POPULAÇÃO, PIB TOTAL E IDHM
@app.callback(
    [
        Output('populacao', 'children'),
        Output('pib_total', 'children'),
        Output('idhm', 'children'),
    ],
    [Input('w_municipios', 'value'),
    Input('w_municipios1', 'value')],
    [State('w_municipios1', 'value')])
def display_content(w_municipios, w_municipios1):
    populacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['populacao'].sum()
    populacao1 = f'{populacao:_.0f}'.replace('_', '.')
    df['pib_total'] = df['pib_total'].astype(float)
    pib = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_total'].sum() / 1000000
    pib1 = f'R$ {pib:_.2f} Bi'.replace('.', ',').replace('_', '.')
    idhm = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['idhm'].sum()

    return populacao1 + ' habitantes', pib1, idhm

# MODAL SOBRE O PAINEL
@app.callback(
    Output("modal-centered", "is_open"),
    [Input("open-centered", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
#
# CONFIGURAÇÃO DE TABS
tabs_styles = dict(height='40px', color='dark', fontColor='dark', alignItems='center', justifyContent='center',
                   textAlign='center')

tab_style = dict(padding='2px', height='40px', width='275px', fontWeight='bold', fontFamily='Arial', color='dark',
                 fontColor='dark', alignItems='center', justifyContent='center', textAlign='center')

tab_selected_style = dict(borderTop='light', borderBottom='white', backgroundColor='light',
                          color='light', height='40px', width='275px', padding='2px', textAlign='center')
#
grid = html.Div(children=[
    dbc.Row(children=[
        dbc.Col(children=[
            sidebar,
        ], style={"border": "1px #EBEBEB solid"}, width=2),
        dbc.Col(children=[
            dbc.Tabs(
                [
                    dbc.Tab(label="Contexto econômico e social", tab_id="social", tab_style=tab_style,
                            active_tab_style=tab_selected_style),
                    dbc.Tab(label="Mundo do Trabalho", tab_id="trabalho", tab_style=tab_style,
                            active_tab_style=tab_selected_style),
                    dbc.Tab(label="Serviços", tab_id="servicos", tab_style=tab_style,
                            active_tab_style=tab_selected_style),
                ],
                id="tabs",
                active_tab="social", className="p-2"
            ),
            html.Div(id="tab-content", className="p-4"),
        ], style={"border": "1px #EBEBEB solid"}, width=10)
    ], justify="center", no_gutters=True)
])

app.layout = html.Div(
    [
        navbar,
        grid,
    ],
    style={"border": "1px #EBEBEB solid"}
)

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
                dbc.Row(children=
                [
                    dbc.Col([dbc.Card(children=
                    [dbc.CardBody(children=
                    [
                        html.H5("Cadastro Único", className="card-title"),
                        html.H3(id='cadunico'),
                        html.Br(),
                        html.H5('Programa Bolsa Família', className="card-title"),
                        html.H3(id='bolsa_familia'),
                        html.Br(),
                        dbc.Button("Saiba Mais sobre o Cadastro Único", id='open1', color="primary"),
                        dbc.Modal(
                            [
                                dbc.ModalHeader("Cadastro Único"),
                                dbc.ModalBody(
                                    "O Cadastro Único para Programas Sociais do Governo Federal (Cadastro Único) é um instrumento "
                                    "que identifica e caracteriza as famílias de baixa renda, "
                                    "permitindo que o governo conheça melhor a realidade socioeconômica dessa população.\n\n"
                                    "Nele são registradas informações como: características da residência, identificação "
                                    "de cada pessoa, escolaridade, situação de trabalho e renda, entre outras."),
                                dbc.ModalFooter(
                                    dbc.Button("Fechar", id="close1", className="ml-auto")
                                ),
                            ],
                            id="modal1",
                            centered=True,
                            style={"width":"50rem", 'whiteSpace': 'pre-wrap'},
                        ),
                    ]), ], color="#E2EBF3", outline=True, style={"width": "20rem", 'border':'white'}
                    )], width=3),
                    dbc.Col(dcc.Graph(id='cad_pbf'), width=9),
                ],
                    align='center'
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='domicilio_sexo', config={'displayModeBar': 'hover'}), width=6),
                        dbc.Col(dcc.Graph(id='faixa_etaria'), width=6),
                        dbc.Col(dcc.Graph(id='escolaridade'), width=6),
                        dbc.Col(dcc.Graph(id='pib_setorial'), width=6),
                    ],
                ),
                # html.Div(dcc.Graph(figure=fig10))
            ], fluid=True
            )
        elif active_tab == "trabalho":
            return dbc.Container(children=[
                dbc.Row(children=
                [
                    dbc.Col(dcc.Graph(id='evolucao_empregos'), width=8),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5("Pessoal Ocupado", className="card-title"),
                                    html.H3(id='empregos', className="card-text")
                                ]
                            ),
                            dbc.CardBody(
                                [
                                    html.H5("Vagas abertas no SINE", className="card-title"),
                                    html.H3(id='sine', className="card-text"),
                                    html.Br(),
                                    dbc.Button("Buscar vagas no SINE", color="primary",
                                               href='https://www.gov.br/pt-br/servicos/buscar-emprego-no-sistema-nacional-de-emprego-sine',
                                               target="_blank"),
                                ]
                            ),
                        ], color="#E2EBF3", outline=True, style={"width": "20rem", 'border':'white'}),
                    ], width=4),
                ],
                    align='center', justify="center", no_gutters=True
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id='estoque_empregos'),
                                html.Br(),
                                html.H5(id='var_emprego'),
                            ], style={'textAlign': 'center'}, width=6),
                        dbc.Col(
                            [
                                html.H4(id='empresas_total'),
                                dcc.Graph(id='empresas_setorial'),
                            ], style={'textAlign': 'center'}, width=6),
                        dbc.Col(dcc.Graph(id='top_vinculos'), width=6),
                        dbc.Col(dcc.Graph(id='remuneracao'), width=6),
                        dbc.Col(dcc.Graph(id='mei'), width=6)
                    ]
                ),
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
                        ], style={"width": "25rem"}),
                    ], width=4
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
                        ], style={"width": "25rem"}),
                    ], width=4
                    ),
                    dbc.Col([dbc.Card(
                        [
                            dbc.CardImg(
                                src="https://www.gov.br/pt-br/apps/mei/view/++widget++form.widgets.imagem/@@download/MEI.png",
                                style={'height': "350px"}),
                            dbc.CardBody(
                                [
                                    html.H5("Informações sobre o MEI",
                                            className="card-title"),
                                    html.P(
                                        "O governo federal disponibiliza um portal com informações para quem deseja se formalizar como microeempreendedor"
                                        "individual, para quem já está formalizado e deseja o acesso digital a produtos e serviços financeiros.\n\n Além"
                                        "disso, o portal apresenta a legislação aplicada, estatísticas e cursos gratuitos para quem pretende se formalizar",
                                        className="card-text",
                                    ),
                                    dbc.Button("Acesse o site", color="primary",
                                               href='https://www.gov.br/empresas-e-negocios/pt-br/empreendedor',
                                               target="_blank"),
                                ]
                            ),
                        ], style={"width": "25rem"}),
                    ], width=4
                    ),
                ],
                ),
            ], fluid=True
            )
    return "No tab selected"

# MODAL CADASTRO ÚNICO
@app.callback(
    Output("modal1", "is_open"),
    [Input("open1", "n_clicks"), Input("close1", "n_clicks")],
    [State("modal1", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
#
# NÚMEROS CADASTRO ÚNICO E BOLSA FAMÍLIA
@app.callback(
    [
        Output('cadunico', 'children'),
        Output('bolsa_familia', 'children'),
        # Output('card_num6', 'children')
    ],
    [Input('w_municipios', 'value')],
    [Input('w_municipios1', 'value')])
def display_cadunico(w_municipios, w_municipios1):
    pessoas_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_cad'].sum()
    pessoas_cad = f'{pessoas_cad:_.0f}'.replace('.', ',').replace('_', '.')
    pessoas_pbf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pessoas_pbf'].sum()
    pessoas_pbf = f'{pessoas_pbf:_.0f}'.replace('.', ',').replace('_', '.')
    # pobreza_extrema = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pobreza_extremapob_cad'].sum()
    # pobreza_extrema = f'{pobreza_extrema:_.0f}'.replace('.', ',').replace('_', '.')

    return pessoas_cad + ' pessoas', pessoas_pbf + ' pessoas'
#
# # EVOLUÇÃO DO CADUNICO E DO PBF
# @app.callback(Output('cad_pbf', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_ev_cadunico(w_municipios, w_municipios1):
#     result = pd.concat([df, df_cad], ignore_index=True, sort=False)
#     df1 = result[(result['municipio'] == w_municipios1) & (result['uf'] == w_municipios)]
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=df1['mês_ano'], y=df1['pessoas_pbf'], name='Bolsa Família', mode='lines+markers',
#                              marker=dict(size=10, color='black')))
#     fig.add_trace(go.Bar(x=df1['mês_ano'], y=df1['pessoas_cad'], name='Cadastro Único'))
#     fig.update_layout(bargap=0.3, bargroupgap=0.15)
#     fig.update_layout(
#         xaxis=dict(
#             showline=True,
#             showgrid=False,
#             showticklabels=True,
#             linecolor='rgb(204, 204, 204)',
#             linewidth=1,
#             ticks='outside',
#             tickfont=dict(
#                 family='Arial',
#                 size=11,
#                 color='rgb(82, 82, 82)',
#             ),
#         ),
#         yaxis=dict(
#             showgrid=False,
#             zeroline=False,
#             showline=False,
#             showticklabels=False,
#         ),
#         autosize=True,
#         margin=dict(autoexpand=True),
#         showlegend=True,
#         plot_bgcolor='white'
#     )
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
#                             xanchor='left', yanchor='bottom',
#                             text='Evolução do nº de pessoas inscritas no CadÚnico e de beneficiárias do Bolsa Família (2018-2021)',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: Ministério da Cidadania/Cadastro Único',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#     fig.update_layout(annotations=annotations)
#
#     return fig
#
# # POPULAÇÃO DO CADUNICO POR SITUAÇÃO DO DOMICÍLIO E SEXO
# @app.callback(Output('domicilio_sexo', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_domicilio_sexo(w_municipios, w_municipios1):
#     urbano = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pes_cad_urbano'].sum()
#     rural = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pes_cad_rural'].sum()
#     masc_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_masculino'].sum()
#     fem_cad = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_feminino'].sum()
#
#     fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'bar'}, {'type': 'domain'}]])
#
#     fig.add_trace(go.Bar(x=['Masculino', 'Feminino'], y=[masc_cad, fem_cad], showlegend=False, text=[masc_cad, fem_cad],
#                          textposition='auto', name='Sexo'), row=1, col=1)
#     fig.add_trace(go.Pie(labels=['Urbano', 'Rural'], values=[urbano, rural], showlegend=True, name='Domicílio'), row=1, col=2)
#
#     fig.update_layout(
#         xaxis=dict(
#             showline=True,
#             showgrid=False,
#             showticklabels=True,
#             linecolor='rgb(204, 204, 204)',
#             linewidth=2,
#             ticks='outside',
#             tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)'),
#         ),
#         yaxis=dict(
#             showgrid=False,
#             zeroline=False,
#             showline=False,
#             showticklabels=True,
#         ),
#         autosize=False,
#         margin=dict(autoexpand=True),
#         plot_bgcolor='white'
#     )
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='População do CadÚnico, por situação do domicílio e sexo',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: Ministério da Cidadania/Cadastro Único',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations)
#
#     return fig
#
# # POPULAÇÃO DO CADUNICO POR FAIXA ETÁRIA
# @app.callback(Output('faixa_etaria', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_age(w_municipios, w_municipios1):
#     faixa = ['16 a 17', '18 a 24', '25 a 34', '35 a 39', '40 a 44', '45 a 49', '50 a 54', '55 a 59', '60 a 64']
#     faixa16_17 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_16_17_anos'].sum()
#     faixa18_24 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_18_24_anos'].sum()
#     faixa25_34 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_25_34_anos'].sum()
#     faixa35_39 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_35_39_anos'].sum()
#     faixa40_44 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_40_44_anos'].sum()
#     faixa45_49 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_45_49_anos'].sum()
#     faixa50_54 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_50_54_anos'].sum()
#     faixa55_59 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_55_59_anos'].sum()
#     faixa60_64 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['faixa_etaria_pessoas_60_64_anos'].sum()
#
#     fig = go.Figure()
#     fig.add_trace(go.Bar(x=faixa, y=[faixa16_17, faixa18_24, faixa25_34, faixa35_39, faixa40_44, faixa45_49, faixa50_54, faixa55_59, faixa60_64],
#                          showlegend=False, textposition='auto', name='Faixa Etária'))
#
#     fig.update_layout(
#         xaxis=dict(
#             showline=True,
#             showgrid=False,
#             showticklabels=True,
#             linecolor='rgb(204, 204, 204)',
#             linewidth=2,
#             ticks='outside',
#             tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)'),
#         ),
#         yaxis=dict(
#             showgrid=False,
#             zeroline=False,
#             showline=False,
#             showticklabels=False,
#         ),
#         autosize=False,
#         margin=dict(autoexpand=True),
#         plot_bgcolor='white'
#     )
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='População do Cadastro Único, por faixa etária',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: Ministério da Cidadania/Cadastro Único',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations)
#
#     return fig
#
# # POPULAÇÃO DO CADUNICO POR ESCOLARIDADE
# @app.callback(Output('escolaridade', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_escolaridade(w_municipios, w_municipios1):
#     nivel = ['Sem instrução', 'Fundamental incompleto', 'Fundamental completo', 'Ensino médio incompleto',
#              'Ensino médio completo', 'Superior completo ou incompleto']
#     sem_instrucao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_sem_instrucao'].sum()
#     fund_incompleto = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_fundamental_incompleto'].sum()
#     fund_completo = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_fundamental_completo'].sum()
#     medio_incompleto = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_medio_incompleto'].sum()
#     medio_completo = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_ensino_medio_completo'].sum()
#     superior = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['cad_superior_completo_incompleto'].sum()
#
#     fig = go.Figure()
#     fig.add_trace(go.Bar(x=[sem_instrucao, fund_incompleto, fund_completo, medio_incompleto, medio_completo, superior], y=nivel, orientation='h', textposition='inside'))
#     fig.update_layout(bargap=0.25, bargroupgap=0.2)
#     fig.update_layout(
#         xaxis=dict(
#             showline=True,
#             showgrid=False,
#             showticklabels=True,
#             linecolor='rgb(204, 204, 204)',
#             linewidth=2,
#             ticks='outside',
#             tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)'),
#         ),
#         yaxis=dict(
#             showgrid=False,
#             zeroline=False,
#             showline=False,
#             showticklabels=True,
#         ),
#         autosize=False,
#         margin=dict(autoexpand=True),
#         showlegend=False,
#         plot_bgcolor='white'
#     )
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='População do CadÚnico, por nível de escolaridade',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: Ministério da Cidadania/Cadastro Único',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations)
#
#     return fig
#
# # NÚMEROS SOBRE EMPRESAS E ESTOQUE DE EMPREGOS
# @app.callback(
#     [
#         Output('empresas_total', 'children'),
#         Output('empregos', 'children'),
#     ],
#     [Input('w_municipios', 'value')],
#     [Input('w_municipios1', 'value')])
# def display_content(w_municipios, w_municipios1):
#     empresas = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_total'].sum()
#     empresas1 = f'{empresas:_.0f}'.replace('_', '.')
#     pessoal = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['estoque_empregos_abr2021'].sum()
#     pessoal = f'{pessoal:_.0f}'.replace('_', '.')
#
#     return empresas1 + ' empresas', pessoal
#
# # PIB POR SETOR DE ATIVIDADE ECONÔMICA
# @app.callback(Output('pib_setorial', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_content(w_municipios, w_municipios1):
#     agropecuaria = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]["pib_agropecuaria"].sum()
#     # agropecuaria = f'{agropecuaria:_.0f}'.replace('.', ',').replace('_', '.')
#     industria = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_industria'].sum()
#     servicos = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_servicos'].sum()
#     admpublica = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['pib_admpublica'].sum()
#
#     fig = go.Figure()
#     fig.add_trace(go.Pie(labels=['Agricultura', 'Indústria', 'Serviços', 'Administração'], values=[agropecuaria, industria, servicos, admpublica],
#                          showlegend=True, name='Setor', hoverinfo='label+value', textinfo='percent', hole=.3, textfont={'family': "Arial", 'size': 15}))
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='PIB por setor de atividade econômica',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: IBGE',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations, hovermode='closest')
#
#     return fig
#
# # NÚMERO DE EMPRESAS POR SETOR DE ATIVIDADE ECONÔMICA
# @app.callback(Output('empresas_setorial', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_content(w_municipios, w_municipios1):
#     setores = ['Agropecuária', 'Indústria Extrativa', 'Indústria de Transformação', 'Eletricidade e Gás',
#                'Saneamento Básico', 'Construção', 'Comérico', 'Transporte', 'Alojamento e Alimentação', 'Informação e Comunicação',
#                'Instituições Financeiras', 'Imobiliárias', 'Atividades Profissionais, Científicas e Técnicas', 'Atividades Administrativas',
#                'Educação', 'Saúde', 'Arte, Cultura e Esportes', 'Outras Atividades']
#     agropecuaria = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_agropecuaria'].sum()
#     ind_extrativa = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_ind_extrativas'].sum()
#     ind_transf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_ind_transf'].sum()
#     eletric_gas = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_eletric_gas'].sum()
#     saneamento = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_saneamento'].sum()
#     construcao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_construcao'].sum()
#     comercio = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_comercio'].sum()
#     transporte = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_transporte'].sum()
#     aloj_alimentacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_alojamento_alimentacao'].sum()
#     info_comunic = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_info_comunic'].sum()
#     financeiro = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_financeiro'].sum()
#     imobiliarias = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_imobiliarias'].sum()
#     ativ_prof = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_ativ_profissionais_cient_tecnicas'].sum()
#     ativ_administrativas = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_ativ_administrativas'].sum()
#     educacao = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_educacao'].sum()
#     saude = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_saude_servicosocial'].sum()
#     arte_cultura = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_arte_cultura'].sum()
#     outras_ativ = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['empresas_outras_ativ_servicos'].sum()
#
#     fig = go.Figure()
#     fig.add_trace(go.Pie(labels=setores, values=[agropecuaria, ind_extrativa, ind_transf, eletric_gas, saneamento, construcao, comercio, transporte,
#                     aloj_alimentacao,info_comunic, financeiro, imobiliarias, ativ_prof, ativ_administrativas, educacao, saude, arte_cultura, outras_ativ],
#                          showlegend=True, name='Setor', hoverinfo='label+value', textinfo='percent', hole=.3, textfont={'family': "Arial", 'size': 15}))
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='Número de empresas, por setor de atividade econômica',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: IBGE/CEMPRE',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations, hovermode='closest')
#
#     return fig
#
# # VAGAS ABERTAS NO SINE
# @app.callback(Output('sine', 'children'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_content(w_municipios, w_municipios1):
#     vagas_sine = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['vagas_sine'].sum()
#     return vagas_sine
#
# # SALDO E VARIAÇÃO DE EMPREGOS
# @app.callback(
#     [
#         Output('estoque_empregos', 'figure'),
#         Output('var_emprego', 'children'),
#     ],
#     [Input('w_municipios', 'value')],
#     [Input('w_municipios1', 'value')])
# def display_content1(w_municipios, w_municipios1):
#     df1 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2021'].sum()
#     df2 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos_12meses'].sum()
#     df3 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['var_saldo_empregos_12meses'].sum()
#
#     fig = go.Figure()
#     fig.add_trace(go.Bar(x=['Saldo de empregos em 2021', 'Saldo de empregos em 12 meses'], y=[df1, df2]))
#     fig.update_layout(bargap=0.25, bargroupgap=0.2)
#     fig.update_layout(
#         xaxis=dict(
#             showline=True,
#             showgrid=False,
#             showticklabels=True,
#             linecolor='rgb(204, 204, 204)',
#             linewidth=2,
#             ticks='outside',
#             tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)',
#             ),
#         ),
#         yaxis=dict(
#             showgrid=False,
#             zeroline=False,
#             showline=False,
#             showticklabels=False,
#         ),
#         autosize=True,
#         margin=dict(autoexpand=True),
#         showlegend=False,
#         plot_bgcolor='white'
#     )
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='Saldo de empregos em 2021 e em 12 meses',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: Ministério da Economia/CAGED',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations)
#
#     return fig, 'Variação percentual de ' + df3 + '% em 12 meses'
#
# # EVOLUÇÃO DO SALDO DE EMPREGOS
# @app.callback(Output('evolucao_empregos', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_content(w_municipios, w_municipios1):
#     anos = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
#             '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
#     saldo_empregos2002 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2002'].sum()
#     saldo_emprego2003 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2003'].sum()
#     saldo_emprego2004 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2004'].sum()
#     saldo_emprego2005 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2005'].sum()
#     saldo_emprego2006 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2006'].sum()
#     saldo_emprego2007 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2007'].sum()
#     saldo_emprego2008 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2008'].sum()
#     saldo_emprego2009 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2009'].sum()
#     saldo_emprego2010 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2010'].sum()
#     saldo_emprego2011 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2011'].sum()
#     saldo_emprego2012 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2012'].sum()
#     saldo_emprego2013 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2013'].sum()
#     saldo_emprego2014 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2014'].sum()
#     saldo_emprego2015 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2015'].sum()
#     saldo_emprego2016 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2016'].sum()
#     saldo_emprego2017 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2017'].sum()
#     saldo_emprego2018 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2018'].sum()
#     saldo_emprego2019 = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['saldo_empregos2019'].sum()
#
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=anos, y=[saldo_empregos2002, saldo_emprego2003, saldo_emprego2004, saldo_emprego2005, saldo_emprego2006,
#                saldo_emprego2007, saldo_emprego2008, saldo_emprego2009, saldo_emprego2010, saldo_emprego2011, saldo_emprego2012,
#                saldo_emprego2013, saldo_emprego2014, saldo_emprego2015, saldo_emprego2016, saldo_emprego2017, saldo_emprego2018, saldo_emprego2019]))
#
#     fig.update_layout(
#         xaxis=dict(
#             showline=True,
#             showgrid=False,
#             showticklabels=True,
#             linecolor='rgb(204, 204, 204)',
#             linewidth=2,
#             ticks='outside',
#             tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)',
#             ),
#         ),
#         yaxis=dict(
#             showgrid=False,
#             zeroline=False,
#             showline=False,
#             showticklabels=True,
#         ),
#         autosize=True,
#         margin=dict(autoexpand=True),
#         showlegend=False,
#         plot_bgcolor='white'
#     )
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='Evolução do saldo de empregos (2002-2019)',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: Ministério da Economia/CAGED',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations)
#
#     return fig
#
# # EVOLUÇÃO DA REMUNERAÇÃO TOTAL
# @app.callback(Output('remuneracao', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_content(w_municipios, w_municipios1):
#     result = pd.merge(df_remuneracao, df, on=['uf', 'municipio'])
#     df2 = result[(result['municipio'] == w_municipios1) & (result['uf'] == w_municipios)].copy()
#     df3 = df2.groupby('ano')['Total'].sum()
#     df3 = df3.reset_index()
#
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=df3['ano'], y=df3['Total']))
#     fig.update_layout(
#         xaxis=dict(
#             showline=True,
#             showgrid=False,
#             showticklabels=True,
#             linecolor='rgb(204, 204, 204)',
#             linewidth=2,
#             ticks='outside',
#             tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)',
#             ),
#         ),
#         yaxis=dict(
#             showgrid=False,
#             zeroline=False,
#             showline=False,
#             showticklabels=False,
#         ),
#         autosize=True,
#         margin=dict(autoexpand=True),
#         showlegend=False,
#         plot_bgcolor='white'
#     )
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='Evolução da remuneração média mensal (salário mínimo)',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: Ministério da Economia/RAIS, 2020',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations)
#
#     return fig
#
# # EMPREENDEDORISMO
# @app.callback(Output('mei', 'figure'),
#               [Input('w_municipios', 'value')],
#               [Input('w_municipios1', 'value')])
# def display_content(w_municipios, w_municipios1):
#     mei_cadunico = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['mei_cadunico'].sum()
#     mei_pbf = df[(df['uf'] == w_municipios) & (df['municipio'] == w_municipios1)]['mei_pbf'].sum()
#
#     return {
#         'data': [go.Bar(
#             x=['Mei no Cadastro Único', 'MEI no Bolsa Família'],
#             y=[mei_cadunico, mei_pbf],
#             textfont=dict(
#                 family="Ariaç",
#                 size=20,
#                 color="LightSeaGreen")
#         )],
#         'layout': go.Layout(
#             title={'text': 'MEI no CadÚnico e no Bolsa Família', 'yanchor': 'top', 'xanchor': 'center'},)
#     }
#
# # OCUPAÇÕES COM MAIORES VINCULOS
# @app.callback(
#     Output('top_vinculos', 'figure'),
#     # [Input('dropdown', 'value')],
#     [Input('w_municipios', 'value')],
#     [Input('w_municipios1', 'value')],
# )
# def update_top_vinculos(w_municipios, w_municipios1):
#     df1 = df_caged.melt(id_vars=["uf", "municipio", "ibge6", 'ano'],
#                           var_name="ocupation",
#                           value_name="vinculos")
#     df2 = df1[(df1['municipio'] == w_municipios1) & (df1['uf'] == w_municipios) & (df1['ano'] == 2019)]
#     # df_caged1['ocupation'] = df_caged1['ocupation'].astype('float')
#     # df1 = pd.concat([df, df_caged1], axis=1)
#     # df2 = df1[(df1['uf'] == w_municipios) & (df1['municipio'] == w_municipios1) & (df1['ocupation'] == ocupation)]
#     # mask = df_caged1['uf'] == w_municipios
#     # mask = df_caged1['municipio'] == w_municipios1
#     # mask = df_caged1['ocupation'] == ocupation
#     # fig = px.bar(df_caged1[mask], x='ano', y='vinculos')
#     #
#     # result = pd.concat([df_caged11, df], axis=1)
#     # df1 = result[(result['uf'] == w_municipios) & (result['municipio'] == w_municipios1)]
#
#     df3 = df2.nlargest(6, 'vinculos')
#     df3 = df3.iloc[1: , :]
#
#     fig = go.Figure()
#     fig.add_trace(go.Bar(x=df3['vinculos'], y=df3['ocupation'], orientation='h', textposition='inside'))
#
#     fig.update_layout(
#         xaxis=dict(
#             showline=True,
#             showgrid=False,
#             showticklabels=True,
#             linecolor='rgb(204, 204, 204)',
#             linewidth=2,
#             ticks='outside',
#             tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)',
#             ),
#         ),
#         yaxis=dict(
#             showgrid=False,
#             zeroline=False,
#             showline=False,
#             showticklabels=True,
#         ),
#         autosize=True,
#         margin=dict(autoexpand=True),
#         showlegend=False,
#         plot_bgcolor='white'
#     )
#
#     annotations = []
#     # Title
#     annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
#                             xanchor='left', yanchor='bottom',
#                             text='Ocupações com maior quantidade de vínculos',
#                             font=dict(family='Arial', size=20, color='rgb(37,37,37)'),
#                             showarrow=False))
#     # Source
#     annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.2,
#                             xanchor='center', yanchor='top',
#                             text='Fonte: Ministério da Economia/RAIS, 2020',
#                             font=dict(family='Arial', size=15, color='rgb(150,150,150)'),
#                             showarrow=False))
#
#     fig.update_layout(annotations=annotations)
#     return fig
#
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





