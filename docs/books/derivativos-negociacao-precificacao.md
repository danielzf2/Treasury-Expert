---
title: "Derivativos Negociacao e Precificacao"
source_pdf: "Derivativos Negociacao e Precificacao.pdf"
converter: "mistral-ocr-latest"
date_converted: "2026-03-27T18:51:09Z"
category: "books"
sanitized: true
reviewed: false
---
LEONEL MOLERO EDUARDO MELLO

# DERIVATIVOS

NEGOCIAÇÃO E PRECIFICAÇÃO

2.ª EDIÇÃO

Saint Paul
Editora

---

# DERIVATIVOS

Negociação e precificação

---

LEONEL MOLERO
EDUARDO
MELLO

# DERIVATIVOS

NEGOCIAÇÃO E PRECIFICAÇÃO

2.ª EDIÇÃO

Saint Paul
Editora

---

© 2020, Saint Paul Editora Ltda.

2.ª edição, 2020

Todos os direitos reservados.

É proibida a reprodução total ou parcial de qualquer forma ou por qualquer meio. A violação dos direitos do autor (Lei n. 9.610/1998) é crime estabelecido pelo artigo 184 do Código Penal.

Depósito Legal na Biblioteca Nacional conforme Lei n. 10.994, de 14 de dezembro de 2004.

# Isenção e limitação de responsabilidade

Os autores deste livro são os exclusivos responsáveis por seu conteúdo, bem como pelas opiniões neste expressas, as quais refletem seus posicionamentos. As visões, opiniões e conteúdo deste trabalho não refletem, necessariamente, o posicionamento de seus atuais ou ex-empregadores, os quais não tiveram nenhum envolvimento, contribuição ou participação, seja direta ou indiretamente, na elaboração deste trabalho, de modo que não poderá os comprometer. Os exemplos contidos neste livro foram preparados e apresentados para fins exclusivamente didáticos, tendo por objetivo a fixação da teoria apresentada. Sendo assim, de maneira nenhuma deverão ser interpretados com o objetivo de sugerir ao leitor que aplique as estratégias ipsis litteris, pois outras variáveis devem ser consideradas, tais quais, mas não se limitando, as condições de mercado, spreads, taxas e impostos.

Coordenação editorial: Nathalia Pinheiro
Revisão: Bárbara Piloto Sincerre
Capa: Ricardo Ferreira
Diagramação: Karina Tenório Silva
Imagem da capa: Kasto/123RF

Dados Internacionais de Catalogação na Publicação (CIP)
(Câmara Brasileira do Livro, SP, Brasil)

Molero, Leonel
Derivativos [livro eletrônico] : Negociação e precificação / Leonel Molero, Eduardo Morato Mello -- 2. ed. -- São Paulo : Saint Paul Editora, 2020.
ePub

ISBN 978-65-86407-14-3

1. Bolsa de mercadorias 2. Derivativos financeiros 3. Mercado de opções 4. Mercado futuro 5. Negociação 6. Preços I. Mello, Eduardo Morato. II. Título.

20-44955
CDD-332.645

Índices para catálogo sistemático:

1. Derivativos: Mercado financeiro: Economia 332.645
Maria Alice Ferreira – Bibliotecária – CRB-8/7964

Saint Paul Editora Ltda.
R. Pamplona, n. 1616, portão 3, Jardim Paulista | São Paulo, SP | Brasil | CEP 01405-002
www.saintpaul.com.br | editora@saintpaul.com.br
Saint Paul Editora Ltda. é uma empresa do Grupo Saint Paul Institute of Finance S. P. Ltda.

---

.

---

Dedicamos às nossas famílias.

---



Sumário

APRESENTAÇÃO
Capítulo 1 - Introdução ao mercado de derivativos
1.1 Tipos de liquidação
1.2 Derivativo mitigador de riscos
1.3 Participantes do mercado de derivativos
1.4 Derivativos tóxicos
1.5 Mercado de derivativos de bolsa
1.5.1 .Atuação da bolsa no mercado de
derivativos
1.5.2 O papel das clearings no mercado de
derivativos
1.5.3 Papel das corretoras no mercado de
derivativos
1.5.4 Depósito de garantias em bolsa
1.6 Mercado de derivativos de balcão
1.7 Os principais contratos de derivativos
1.7.1 Contrato a termo
1.7.2 Contrato futuro
1.7.3 Swaps
1.7.4 Opções
1.8 Taxas discretas e contínuas
Capítulo 2 - Mercado a termo
2.1 Nomenclatura e notações dos termos
2.2 Mercado a termo de ações
2.3 Financiador a termo
2.4 O contrato a termo e a premissa de não
arbitragem
2.5 Arbitragem de contratos a termo de moedas

---



2.6 Marcação a mercado do contrato a termo

Capítulo 3 - Mercado futuro

3.1 O contrato futuro

3.2 Diferenças entre contrato a termo e futuro

3.3 Futuro de dólar

3.3.1 Rolagem de futuro de dólar

3.3.2 Minicontrato de dólar futuro

3.3.3 Ajuste de operação com futuro de dólar

3.3.4 Casado de dólar e FRP

3.4 Contrato futuro de Índice BOVESPA

3.4.1 Minicontrato de IBOVESPA

3.4.2 Rolagem de IBOVESPA e IR1

3.4.3 Beta hedge

3.4.4 Breve discussão sobre o beta

3.5 Contrato futuro de DI

3.6 Ajuste de operação no contrato futuro de DI

3.6.1 Hedge de renda fixa usando o futuro de DI

3.7 Futuro de DDI

3.8 FRA de cupom

3.9 Dólar sintético e curva de dólar

Capítulo 4 - Swaps

4.1 Indexadores disponíveis

4.2 Swaps – Aplicações

4.2.1 Swap pré x dólar: hedge de exportação

4.2.2 Swap dólar x Selic: fundo cambial

4.2.3 Swap IGP-M x DI: empresa prestadora de

serviços

4.2.4 Swap DI x Pré: banco de montadora

4.3 Marcação a mercado de pontas do swap de

acordo com o tipo de indexador

4.3.1 Ponta pré-fixada

4.3.2 Ponta dólar + cupom cambial

---



4.3.3 Ponta índice de preços: IPCA e IGP-M

4.3.4 Ponta taxa de juros: DI e Selic

4.4 Contrato de swap cambial com ajuste periódico baseado em operações compromissadas de um dia (SCS)

4.4.1 Cálculo do SCS

4.5 O ciclo de vida de um swap

4.5.1 Swap DI versus Pré: precificação

4.5.2 Swap DI versus Pré: marcação a mercado

4.5.3 Swap DI versus Pré: liquidação

4.5.4 Swap IPCA versus Pré: precificação

4.5.5 Swap IPCA versus Pré: marcação a mercado

4.5.6 Swap IPCA versus Pré: liquidação

4.5.7 Swap DI versus Dólar: precificação

4.5.8 Swap DI versus Dólar: marcação a mercado

4.5.9 Swap DI versus Dólar: liquidação no vencimento

4.5.10 Conclusão

4.6 Swap Libor x pré-fixado em dólar

4.6.1 Breve explanação sobre swap de Libor

4.6.2 Eurodólar

4.6.3 Eurodólar – Ajuste de convexidade

4.6.4 Fluxos de caixa de um swap Libor x pré-fixado

4.6.5 Swaps de Libor – Antes e depois da crise de crédito de 2007

4.6.6 Precificação

4.6.7 Convenções de contagem de dias corridos

4.6.8 Precificando um swap Libor sem garantia e sem spread

4.6.9 Precificando um swap Libor com garantia

4.6.10 Marcação a mercado do swap de Libor

---



4.6.11 O futuro da taxa Libor como indexador pós-fixado

Capítulo 5 - Mercado de opções

5.1 História das opções

5.2 Estrutura de uma opção

5.3 Entendendo ganhos e perdas nas posições de opções

5.3.1 Ganhos e perdas – Comprado em call

5.3.2 Ganhos e perdas – Vendido em call

5.3.3 Ganhos e perdas – Comprado em put

5.3.4 Ganhos e perdas – Vendido em put

5.4 Ganhos e perdas de estratégias direcionais básicas com opções

5.4.1 Financiamento

5.4.2 Bull call spread

5.4.3 Bear call spread

5.4.4 Strangle

5.4.5 Butterfly

Capítulo 6 - Precificação de opções

6.1 Processos estocásticos

6.1.1 A trajetória dos preços no tempo

6.1.2 A variável aleatória

6.1.3 Processo de Wiener

6.1.4 Lema de Itô

6.1.5 Reversão à média

6.2 Simulação de Monte Carlo

6.2.1 Simulação de Monte Carlo para processo de Wiener

6.2.2 Simulação de Monte Carlo para reversão à média

6.3 Precificação de opções de ações – Modelo de

Black e Scholes

---



6.3.1 Black e Scholes com taxa de juros na forma discreta
 6.3.2 Preço da put europeia de ações
 6.3.3 Cálculo da volatilidade
 6.3.4 Volatilidade com EWMA
6.4 Precificação de opções de ações com pagamento de dividendos
6.5 Precificação de opções de ativos com custo de carregamento
6.6 Precificação de opções de moeda com cupom cambial
6.7 Precificação de opções sobre futuros de moeda e índice de bolsa
6.8 Precificação de opções de taxas de juros
6.9 Precificação de opções perpétuas
6.10 Precificação de opções com barreira
 6.10.1 Aplicação de precificação de opção com barreira
Capítulo 7 - Gregas das opções
7.1 Delta e gama
7.2 O efeito delta-gama
7.3 O delta hedge
 7.3.1 Delta hedge com ativo
7.4 Delta
 7.4.1 Delta e at the moneyness da opção
7.5 Gama
7.6 Vega
7.7 Posição nas gregas
7.8 Theta
7.9 Rô
 7.9.1 Rô para taxa de juros contínua
7.10 Rô para taxa de juros discreta

---



7.11 Resumo geral das gregas

7.12 Posição nas gregas em put e call

7.13 Gregas para simulação de Monte Carlo

7.14 Gregas de uma carteira

Capítulo 8 - Operações com volatilidade de opções

8.1 Volatilidade implícita

8.2 Sorriso e superfície de volatilidade

8.2.1 Preços das opções durante o pregão

8.2.2 Superfície de volatilidade

8.3 Cone de volatilidade

8.4 Operações com volatilidade

8.4.1 Operações com robô

8.4.2 Compra e venda de volatilidade

8.4.3 Volatilidade com ativo à vista

8.4.4 Spread de volatilidade

8.4.5 Arbitragem de volatilidade vega neutra

8.4.6 Spread gama neutro

8.4.7 Volatilidade a termo

Capítulo 9 - Derivativos de commodities

9.1 Conceitos fundamentais do mercado de

commodities

9.2 Mercado à vista, termo e futuro de commodity

9.2.1 Mercado à vista

9.2.2 Mercado a termo

9.2.3 Mercado futuro de commodity

9.2.4 Mercados de açúcar e etanol

9.2.5 Mercados de petróleo

9.3 Teoria da estocagem

9.3.1 Princípios da teoria da estocagem

9.3.2 Custo de carregamento

9.3.3 Contango e backwardation

9.3.4 Backwardation forte e fraco

---



9.3.5 Retorno de conveniência
9.4 Modelagem de preços de commodities
 9.4.1 Modelo com base no CAPM
 9.4.2 Modelos de um, dois e três fatores
 9.4.3 Modelos de curto e de longo prazos
 9.4.4 Teoria da paridade de duas commodities de Walras
 9.4.5 Relação do preço do petróleo com outras commodities
9.5 Condição de não arbitragem do preço futuro
9.6 Reversão à média do retorno de conveniência
9.7 Movimento browniano do preço à vista
9.8 Relação do petróleo com o preço da commodity
9.9 Relação da volatilidade do mercado com o preço da commodity
9.10 Sazonalidade
9.11 Modelo com variáveis exógenas para precificação de commodities
Capítulo 10 - XVA – Ajustes na avaliação de derivativos
10.1 Introdução
10.2 Premissas pré-crise de 2007-2008
10.3 Credit Value Adjustment (CVA)
 10.3.1 Risco de crédito de contraparte versus risco de crédito
 10.3.2 Wrong way risk
 10.3.3 O CVA Contábil
10.4 DVA: o outro lado do CVA
10.5 Funding Value Adjustment (FVA)
10.6 Capital Value Adjustment (KVA)
10.7 Considerações finais

---



Capítulo 11 - Certificado de Operações Estruturadas (COE)

11.1 Introdução

11.2 Características do COE

11.3 COE para o emissor

11.3.1 COE como alternativa de lucros

11.3.2 Responsabilidades do emissor do COE

11.4 Características do COE na emissão

11.5 Os ativos subjacentes do COE

11.5.1 Fundos de capital protegido

11.6 Surgimento do COE

11.6.1 Structured notes

11.6.2 Credit-Linked Notes (CLN)

11.7 Tipos mais comuns de COEs

11.7.1 COE com call

11.7.2 COE com put

11.7.3 COE com call spread

11.7.4 COE com call knock out

11.7.5 COE com call knock in

11.7.6 COE com straddle

11.7.7 COE com strangle

11.7.8 COE com call digital

11.7.9 COE com range accrual

11.8 Exemplo de operação com o COE

11.8.1 Precificação da operação

11.8.2 Resultado do COE para o titular

11.8.3 Hedge do COE para o emissor

Capítulo 12 - Hedge de empresas

12.1 Introdução

12.2 Fazer hedge ou não?

12.2.1 Vantagens do hedge

12.3 Desvantagens do hedge

---



12.4 Hedge ou especulação?

12.5 Fatores de risco

12.6 Hedge de fluxo de caixa e de balanço

12.6.1 Exemplo de net exposure

12.7 Efetividade do hedge

12.7.1 Índice de efetividade do hedge

12.8 Gerenciamento de risco de mercado

12.8.1 Value at Risk (VaR)

12.8.2 Exemplo de VaR de variação cambial

12.8.3 Análise de Stress

12.9 Política de hedge

12.10 Hedge de taxas de juros

Capítulo 13 - Planos de opções para executivos: stock option plan

13.1 Plano de opções da compra de ações

13.2 Aprovação do plano de opções

13.3 Modalidades de planos

13.4 Datas de outorga, maturação e vencimento do plano de opções

13.5 Instrumento de outorga

13.6 O preço de exercício

13.7 Procedimentos para o exercício da opção

13.8 Despesas do plano de opções

13.8.1 Reconhecimento de opções com entrega de instrumentos patrimoniais

13.8.2 Reconhecimento de opções com liquidação em caixa

13.9 Divulgação do plano de opções

13.10 Cálculo de fair value das opções de compra de ações para executivos

13.10.1 Cálculo da volatilidade para precificação de opções para executivos

---



13.10.2 Estimar volatilidade com base no CAPM
- 13.10.3 Fator de diluição
- 13.10.4 Taxa de abandono esperada do plano
- 13.10.5 Prazo esperado de exercício de compra da ação
REFERÊNCIAS
Anexo A - Processo ARMA/GARCH para volatilidade heterocedástica

---

# APRESENTAÇÃO

A motivação que nos levou a escrever este livro foi a necessidade de preencher algumas acunas sobre tópicos específicos ainda não abordados nas bibliografias relativas ao mercado brasileiro de derivativos. Esta obra possui conteúdo pragmático, voltado para a prática do mercado. Contudo, mantivemos o rigor acadêmico ao longo do texto.

Este livro é direcionado aos alunos de pós-graduação, para cursos introdutórios ou avançados em derivativos, de lato ou stricto sensu. Dada sua abordagem prática, pode ser utilizado por profissionais que atuam direta ou indiretamente no mercado de derivativos. Consideramos que o conteúdo será mais facilmente assimilado por alunos de Administração, Economia, Engenharia, Matemática, em suma, que possuam formação em métodos quantitativos e mínimo conhecimento em mercado financeiro.

Como professores e profissionais do mercado de derivativos que somos, percebemos que existe um aprendizado incompleto sobre o tema derivativos pelos alunos provenientes da graduação; este livro poderá complementar esse aprendizado. Em geral, os profissionais que atuam no mercado de derivativos conseguem obter muito conteúdo na web. Porém, acreditamos que esses profissionais necessitam de um livro de prateleira para fazer consultas, eventualmente, sobre tópicos específicos; que tenha uma explicação objetiva, com exemplos numéricos implementáveis, resolvidos passo a passo.

O conteúdo, estruturado na forma de capítulos, é gradativamente apresentado ao longo do texto, em ordem crescente de dificuldade, sobre os temas relativos aos derivativos. Nos primeiros capítulos, da primeira metade do livro, apresentamos a estrutura dos quatro grupos de contratos derivativos, na sua forma *plain vanilla*, nesta ordem: termos, futuros, swaps e opções. Na segunda metade do livro, abordamos tópicos mais avançados, tais como: precificação de opções, gregas, operações com volatilidade, xVA, COE e hedge nas empresas.

Nesta obra, alguns tópicos apresentados são um pouco mais específicos, que o tornam mais interessante para alguns profissionais. Por exemplo, o

---

capítulo de derivativos de commodities, que possui uma abordagem academicamente adequada e voltada para o mercado brasileiro de commodities agrícolas, é mais interessante para os profissionais que atuam nessa área. Outro capítulo bem específico, porém interessante para muitos profissionais, é o de operações com volatilidade de opções, que aborda técnicas utilizadas em operações proprietárias de bancos e fundos de investimentos. Outro capítulo atraente para alguns leitores é o de Stock Option Plan, no qual explicamos alguns detalhes do plano de opções para executivos. Também abordamos alguns impactos da crise de crédito de 2007 na precificação de derivativos, especificamente no swap de London InterBank Offered Rate (Libor).

Nesta segunda edição, incluímos mais três capítulos. No capítulo sobre Certificado de Operações Estruturadas (COE), abordamos os tipos de operação, as vantagens para o titular e para o banco emissor. No capítulo sobre xVA, tratamos sobre a precificação dos derivativos considerando análise de crédito, consumo de capital e funding do banco. Adicionamos também um capítulo sobre o hedge nas empresas, que inclui o cálculo de exposure, hedge cambial, elaboração de política de hedge e hedge de taxa de juros.

A estrutura do conteúdo deste livro é bem usual, com a qual os estudantes estão acostumados. Em cada capítulo é apresentada a teoria específica e, na seção seguinte, no mesmo capítulo, é apresentado um exemplo numérico, cujo cálculo é detalhadamente explicado. Ao final de cada capítulo foram disponibilizados exercícios para a fixação do conteúdo.

E, por fim, gostaríamos de nos desculpar pelo uso indiscriminado de anglicismos ao longo do texto. Aliás, hábito recorrente entre profissionais de mercado financeiro.

Boa leitura!

Os autores

---

CAPITULO 1

# Introdução ao mercado de derivativos

---

O mercado de derivativos surgiu da necessidade de os comerciantes transacionarem mercadorias para entrega e pagamento no futuro. O objetivo primário desse mercado era garantir o fornecimento e o preço, com certa antecipação.

Quando negociamos um ativo por encomenda, fixando as características do ativo e o preço, essa negociação possui características de derivativo.

Por exemplo, quando o moinho negocia o preço do trigo com o produtor agrícola, antes mesmo de este ser colhido, essa negociação pode ser considerada como um derivativo, pois fixam-se o preço, a quantidade e a qualidade do trigo que será entregue no futuro.

Outro exemplo de derivativo ocorre quando uma indústria siderúrgica negocia antecipadamente o fornecimento de energia elétrica, definindo o preço, a quantidade e as características do fornecimento.

Quando uma empresa negocia a taxa para uma operação de câmbio que ocorrerá no futuro, isto certamente é um derivativo.

O derivativo está mais presente em nossas vidas do que podemos imaginar, até mesmo um compromisso de compra e venda de um imóvel possui características de derivativo, pois está discriminado o preço, a data futura para pagamento e as condições para entrega do imóvel.

O derivativo permite a eliminação de incertezas nas negociações, principalmente em relação a preços. O derivativo é um contrato firmado entre as partes, de compra ou venda de um determinado ativo – denominado como ativo-base ou ativo-objeto. Outra característica do contrato derivativo é que normalmente não é exigido investimento inicial das partes; ou quando é exigido algum desembolso no início do contrato, o valor deste é significativamente menor do que o necessário para comprar o ativo-objeto.

# 1.1 Tipos de liquidação

Algumas operações com derivativos podem ou não envolver a entrega do ativo-objeto. Quando o derivativo envolve a entrega do ativo-objeto,

---

dizemos que existe entrega física e quando não envolve a entrega do ativo-objeto, a liquidação é feita pela diferença entre o preço definido no contrato de derivativo e o preço do ativo-objeto.

Para que seja feita a liquidação por diferença é necessário que o preço do ativo-objeto seja divulgado por uma instituição referenciada e isenta.

Por exemplo, alguns preços de commodities, que servem como referência para liquidação de operações com derivativos são divulgados pelo Centro de Estudos Avançados em Economia Aplicada (Cepea) vinculado à Escola Superior de Agricultura Luiz de Queiroz (Esalq-USP). No caso de taxas de juros, o Depósito Interfinanceiro (DI) é divulgado pela Central de Custódia e Liquidação Financeira de Títulos (Cetip).

O dólar comercial, referência para a liquidação da maior parte das operações com derivativos de câmbio, é divulgado diariamente pelo Banco Central do Brasil (BACEN).

# 1.2 Derivativo mitigador de riscos

Investidores e poupadores estão expostos a riscos financeiros relativos à variação de preços de ativos, que vão desde imóveis, taxas de juros, câmbio, preços de produtos agrícolas, até produtos menos triviais, como o preço da arroba de gado bovino vivo, ou o valor da energia elétrica utilizada para a produção de alumínio.

Quando recursos são investidos em uma atividade produtiva, o investidor tem de enfrentar não só os riscos específicos do negócio, como a incerteza na demanda pelo produto, riscos de greve, acidentes de trabalho, fornecimento de insumos, mas também outros riscos, como política monetária do país, incerteza no preço de mercado do produto vendido, riscos políticos e cambiais.

---

Os derivativos foram essencialmente criados para transferir os riscos que não são inerentes à atividade econômica na qual o produtor está envolvido para outra parte interessada em assumir esse risco em troca de alguma remuneração.

A transferência de riscos funciona como um tipo de seguro contra perdas inesperadas causadas por variáveis que fogem do controle do produtor, que já possui incertezas suficientes.

A transferência de riscos pode ser interessante para o produtor, desde que o prêmio paga por esse seguro não seja uma quantia proibitiva para o seu negócio, inviabilizando economicamente sua atividade. A outra parte, que assume esses riscos, precisa diversificá-los, de forma a obter ganhos na média dos retornos dos contratos. Certamente poderá haver perdas em algumas situações, o importante é obter ganhos na soma total das operações e não nas operações individuais.

Surgiu a necessidade, portanto, de criar um instrumento que tenha como finalidade a transferência entre tomadores e doadores de riscos sob forma de taxas, esse instrumento foi denominado como **derivativo** (do inglês, derivative).

> Derivativo pode ser definido, portanto, como um acordo entre duas partes, de compra ou venda de um determinado ativo que será liquidado em data futura, preestabelecida, por um preço previamente combinado, normalmente sem a necessidade de um investimento inicial. Quando é exigido algum desembolso no início do contrato, o valor deste é significativamente menor do que o necessário para comprar o ativo-objeto.

O ativo-objeto, no qual é referenciado o derivativo, pode ser desde suco de laranja, ouro, soja, milho, algodão e carne suína até ações, taxa de juros, de câmbio e títulos públicos.

O agricultor de soja, por exemplo, deve vender o seu produto em certa época do ano. No momento da venda da soja, se o preço de mercado não lhe for atraente, ele pode estocar o produto e vendê-lo quando o preço subir. Alternativamente, o agricultor pode vender a soja sob encomenda antes mesmo de plantá-la, garantindo,

---

assim,

o preço de venda e a viabilidade econômica do seu negócio.

Um apostador, em contrapartida, pode negociar antecipadamente a soja com o agricultor, pois pode antever uma tendência nos preços com base na análise de informações relacionadas à soja, ou seja, irá adquirir a soja sob encomenda do agricultor, com intuito de lucrar com a alta dos preços.

Tão logo o apostador receba a soja, vendê-la-á no mercado, obtendo um lucro na diferença dos preços. O risco que o apostador assume nessa transação é de errar em suas previsões, o preço de mercado da soja despencar e ele ter de realizar uma perda no diferencial de preços no futuro.

A operação de transferência de incertezas possibilitada pelos derivativos pode possuir duas interpretações distintas quanto à posição assumida:

- quando tiver a finalidade de proteção contra riscos financeiros será denominada de hedge (palavra em inglês que se difundiu no mercado brasileiro, que será mantida em sua forma original);
- quando a finalidade da posição for a de assumir riscos para a obtenção de lucro, será denominada especulação.

## 1.3 Participantes do mercado de derivativos

O mercado de derivativos permite que seus participantes atuem com objetivos distintos. Os produtores de mercadoria física podem utilizar esse mercado para se proteger contra oscilações do preço de venda, enquanto a indústria compradora pode utilizar o mercado para fixar o preço de seus insumos. Outros participantes, especialistas na formação de preços, podem utilizar o mercado com o intuito de fazer lucros com as oscilações nos preços.

---

Os participantes que atuam no mercado de derivativos com o intuito de reduzir seus riscos, procurando uma proteção contra a volatilidade dos preços, são denominados de **hedgers**. Por exemplo, o produtor do ativo físico ou o comprador da indústria de transformação.

Vamos imaginar a situação de um produtor de **commodity** que utiliza contratos futuros para fazer hedge, o hedger pode proteger o valor desta commodity, realizando, simultaneamente, uma venda na mesma quantidade em contratos futuros. Se as variações no preço da commodity à vista forem iguais as do preço do contrato futuro, ou seja, se os movimentos de preço forem paralelos, uma perda com os preços à vista pode ser compensada por um ganho de igual montante nos contratos futuros. Porém, na prática, o produtor não ficará preocupado com a aderência das variações dos preços à vista e futuro durante a vida do contrato, dado que no vencimento do contrato, o preço à vista será igual ao do futuro.

Outro tipo de participante do mercado de derivativos é o especulador. Normalmente, ele não é o produtor do bem físico, nem deseja a entrega física da mercadoria, apenas o ajuste financeiro por diferença entre o preço de mercado e o preço fixado em contrato.

O especulador é um especialista na formação de preços e atua no mercado com o objetivo de fazer lucro com as oscilações de preços. Seu papel é importante porque proporciona liquidez ao mercado de derivativos, permitindo que outros participantes possam assumir posições inversas em relação às suas.

O papel do especulador é o de assumir o risco transferido pelo hedger, com o intuito de auferir algum tipo de ganho. O mercado de derivativos permite a transferência de risco de um grupo para outro. O hedger estaria disposto, nesse caso, a pagar um prêmio pelo risco transferido ao especulador.

Para obter ganhos anormais, o especulador deve ter uma previsão da demanda mais precisa do que o investidor regular. Porém, assumindo a hipótese do mercado eficiente, não poderia haver ganho especulativo consistente, pois os preços refletem toda a informação disponível.

O terceiro participante do mercado de derivativos é o arbitrador – aquele que atua no mercado de derivativos com o intuito de fazer lucro certo, sem

---

assumir riscos, aproveitando a diferença de preços de um mesmo ativo que é negociado em mercados diferentes. O arbitrador compra e vende simultaneamente, não fica com o ativo e, consequentemente, não precisa dispor de recursos financeiros, seu papel no mercado é atuar como regulador de preços e manter o equilíbrio dos mercados.

A arbitragem surge de um desequilíbrio entre o preço futuro e o preço à vista, considerando, por exemplo, o custo de carregamento e da taxa de juros livre de risco.

Logo, os participantes do mercado de derivativos, quanto à posição que assumem, podem ser classificados como:

- **Hedger**: indivíduo que atua no mercado de derivativos em busca de proteção contra riscos financeiros, normalmente é o produtor do bem físico. A atuação dos hedgers não é permanente, opera com derivativos apenas quando lhe for necessário. As necessidades desse participante por si só justificam a existência do mercado de derivativos.
- **Especulador**: injustamente associado a um termo pejorativo, o especulador é aquele que atua no mercado assumindo riscos em busca de ganhos, pode ser considerado como um tipo de apostador, sem ele não haveria para quem o hedger transferir seus riscos. O especulador é um especialista que conhece o mercado e o comportamento dos preços, ele não ganha sempre em suas apostas, o seu objetivo é operar muitas vezes e ganhar na média das operações.

O seu papel é importante, pois é responsável pelo grande número de transações que realiza, em conferir liquidez aos contratos de derivativos.

- **Arbitrador**: indivíduo que atua no mercado de derivativos com o intuito de fazer lucro certo, sem assumir riscos, aproveitando a diferença de preços de um mesmo ativo que é negociado em mercados diferentes. O arbitrador compra e vende simultaneamente, ele não fica com o ativo e, consequentemente, não precisa dispor de recursos, seu papel no mercado é como regulador de preços e na manutenção do equilíbrio

---

dos mercados. Um exemplo de operação de arbitragem é o que acontecia entre os agentes corretores que atuavam na década de 1980, nas bolsas de ações de São Paulo e do Rio de Janeiro, que negociavam o mesmo tipo de ação ao portador. Por problemas de liquidez,

os preços oscilavam de forma diferente nas duas bolsas, criando a possibilidade de compras e vendas simultâneas nos dois recintos de negociação, garantindo lucro certo sem desembolso de caixa. Nesse caso, o arbitrador acabava

mantendo os preços equilibrados entre as duas bolsas. Atualmente, o arbitrador pode, por exemplo, aproveitar-se de distorções entre o preço à vista

e o preço futuro. Nessa situação, o arbitrador pode comprar o ativo à vista e vender a futuro, ou vice-versa.

- Financiador: sujeito que participa do mercado de derivativos com a intenção de investir seus recursos para obter em troca uma taxa de juros mais atraente do que as obtidas com títulos de renda fixa. Para obtê-la, precisa realizar mais de um negócio, que costuma ser a compra de um determinado ativo à vista e a simultânea venda do derivativo. O seu papel é importante, pois acaba proporcionando liquidez às posições vendidas em certos contratos derivativos, como é o caso dos termos e das opções. Alguns participantes do mercado podem fazer a operação inversa à feita pelo financiador, no caso, a venda do ativo à vista e a simultânea compra a termo, esse tipo de operação é realizada para a captação de recursos.

No mercado de derivativos, também é importante salientar o papel do intermediário financeiro, que viabiliza a execução da operação em bolsa, normalmente na figura das Corretoras de Títulos e Valores Mobiliários (CTVM). Esses participantes podem atuar como formadores de opinião para seus clientes, recebendo comissão pelas transações em forma de corretagem.

# 1.4 Derivativos tóxicos

---

No mercado de derivativos é relativamente fácil para que alguns participantes confundam a verdadeira função de seus papéis. Alguns participantes que deveriam atuar como hedgers, pela natureza do seu negócio, acabam seduzidos pelas possibilidades de ganhos que as posições especulativas podem proporcionar.

Geralmente, os resultados especulativos malsucedidos no mercado de derivativos são decorrência do mau uso e do desconhecimento sobre a posição assumida nas operações.

Alguns eventos que ocorreram em operações especulativas acabaram apelidando algumas operações específicas como derivativos tóxicos.

Mas o que vem a ser um derivativo tóxico? São operações de balcão, que foram negociadas por empresas com objetivo especulativo, que geraram prejuízos. Uma operação comumente conhecida como derivativo tóxico é o Target Forward (Tarf), uma estrutura similar a um termo de dólar, na qual o investidor deve receber 100% da variação cambial se a direção do dólar lhe for favorável, e deve pagar 200% da variação cambial se este lhe for desfavorável. Aparentemente, é uma estrutura criada para prejudicar o investidor, porém, no Tarf, o investidor é compensado por um intervalo de variação do dólar, em que ele pode ganhar mais do que o intervalo de perda. Ou seja, nessa operação, a probabilidade de ganhar é maior do que a de perder, porém o valor da perda também é maior, na verdade, duas vezes maior, do que o valor do ganho.

# 1.5 Mercado de derivativos de bolsa

---

O mercado de derivativos pode ser classificado como de bolsa e de balcão em relação à forma e ao local em que as operações são realizadas.

O mercado de bolsa é realizado em recinto fechado organizado exclusivamente para a realização de operações de compra e venda de ativos financeiros.

Todas as operações negociadas fora da bolsa são consideradas operações de balcão.

# Como podemos definir a bolsa?

Bolsa é um ambiente de negociação em que ativos padronizados são negociados, e os participantes nele reunidos possuem o mesmo intuito, que é o de negociar esses ativos.

No mercado de derivativos, as operações de bolsa são padronizadas quanto aos prazos de vencimento, tamanho dos contratos, ativos-objetos de negociação e na forma de cotação.

O ambiente de negociação em bolsa pode ser físico ou eletrônico. O ambiente físico ocorre no pregão viva-voz, que é realizado em rodas de negociação, diretamente pelos operadores de pregão. No pregão eletrônico, os negócios são realizados em plataformas eletrônicas de negociação, sem a necessidade de intervenção humana direta.

No Brasil, o pregão viva-voz, ambiente em que as ordens eram executadas pelos operadores e auxiliares de pregão, encerrou-se em 30 de junho de 2009, com o fim do pregão no recinto da BM&F.

Atualmente, as negociações dos derivativos em bolsa são feitas pelo sistema eletrônico, o que torna as negociações mais ágeis e permite o uso de algoritmos e os robôs de negociação, que são softwares que colocam a ordem de negociação de forma automática.

A atuação dos participantes do antigo mercado viva-voz era realizada dentro do recinto da bolsa, permitida apenas aos agentes corretores, representados pelos operadores de pregão ou agentes especiais. As transações ocorriam dentro da bolsa, nas chamadas rodas de negociação, cada contrato derivativo possuía sua roda específica de operadores.

---

# 1.5.1 Atuação da bolsa no mercado de derivativos

A bolsa que abriga o mercado de derivativos no Brasil atualmente é a B3 - Brasil, Bolsa, Balcão. Com a aprovação da Comissão de Valores Mobiliários (CVM) da combinação das operações entre a BM&FBOVESPA e a Cetip, a razão social da BM&FBOVESPA SA foi alterada para B3 SA (Brasil, Bolsa, Balcão).

O horário em que a bolsa está em funcionamento, período no qual as operações podem ser realizadas, é chamado de pregão, que ocorre apenas em dias úteis. Durante o horário de pregão, os preços dos ativos e derivativos oscilam livremente, de acordo com as transações realizadas por meio dos sistemas da bolsa.

A liquidação das operações, tanto liquidação física quanto financeira, é garantida pela bolsa, mediante um depósito antecipado de garantias. Os preços dos derivativos negociados em bolsa oscilam dentro de limites permitidos, e em momentos de alta volatilidade, a bolsa pode intervir na continuidade do pregão, com o intuito de evitar problemas sistêmicos.

As operações são diariamente divulgadas pelos boletins das bolsas e pelos sistemas de informações de mercado, que publicam as cotações e preços apregoados de compra e venda em tempo real.

Como as operações registradas em bolsa são públicas, o processo de fiscalização é feito pela própria bolsa, que atua como órgão regulador, e por instituições competentes, como a CVM, o que inibe a realização de transações em desacordo com suas regras. Além disso, as operações são realizadas sempre nos valores apregoados pelos participantes, ou seja, dificultando transações fora dos preços de mercado.

Os investidores atuam em bolsa por intermédio das corretoras e não são abertamente identificados, pois seu registro é feito por meio de um número (código do cliente), permanecendo, dessa forma, no anonimato, o que ajuda

---

a manter a eficiência do mercado, sem a identificação de vendedores e compradores.

No mercado de derivativos de bolsa, as operações são públicas, porém os clientes são anônimos.

Pelo serviço prestado ao fornecer o ambiente de negociação para os ativos, a bolsa cobra emolumentos, que é uma taxa, por contrato ou ativo negociado, com valores iguais a todos os participantes, sem distinção.

A bolsa necessita obrigatoriamente de uma clearing, que realiza a liquidação das operações e faz o controle das garantias. A clearing também cobra taxas pelos seus serviços, como: taxas de registro e taxas de liquidação. Essas taxas vêm discriminadas na nota de corretagem.

## 1.5.2 O papel das clearings no mercado de derivativos

As clearings ou câmaras de liquidação e custódia são essenciais para o bom andamento do mercado de derivativos em bolsa e balcão. A bolsa é apenas o ambiente de negociação, a clearing é a instituição que realmente faz liquidações, pagamentos, entrega de ativos e garante que o fluxo operacional ocorra sem grandes percalços para os participantes do mercado de derivativos.

A liquidação é o ato de pagar ou entregar o ativo-objeto. Nas operações em bolsa, a liquidação pode ser física ou financeira. Em uma operação de compra e venda, a liquidação física ocorre quando existe a entrega do ativo-objeto, em decorrência de uma venda; enquanto que a liquidação financeira ocorre no pagamento, em decorrência da compra.

A clearing é responsável pela liquidação e custódia, que significa a guarda do ativo. Entretanto, desde o início da década de 1990, não existe mais guarda

---

física dos ativos. Atualmente, os papéis são escriturais nominativos. A escrituração é feita eletronicamente pelo sistema da clearing. É importante salientar que para alguns derivativos, como de algumas commodities, é possível optar pela liquidação por meio da entrega física da mercadoria nos armazéns cadastrados junto a B3, que define, ainda, uma série de restrições quanto às especificações físicas do produto.

Há sempre o risco dos participantes ficarem inadimplentes em uma das duas pontas da operação, ou seja, podem vender, mas não terem o ativo para entregar – denominado venda a descoberto – ou podem comprar, sem terem os recursos financeiros para pagar – ficando, assim, inadimplentes. Por isso o papel da clearing é tão essencial.

A clearing permite que todos os participantes que pagaram, recebam seu ativo e, em contrapartida, todos aqueles que entregaram os ativos, recebam os recursos financeiros provenientes da venda. Essa garantia ocorre nas liquidações de derivativos listados em bolsa e em alguns casos de derivativos de balcão, contratados com garantia (veremos mais adiante os mercados de derivativos de balcão).

A clearing utiliza o sistema Delivery Versus Payment (DVP). Nesse sistema, a clearing recebe o dinheiro antes de entregar os ativos, e recebe os ativos antes de pagar por eles. Dessa forma, ela sempre recebe antes de pagar, sem correr o risco de ficar inadimplente.

Quando ocorre liquidação de operações de câmbio, por exemplo, a clearing usa o sistema Payment Versus Payment (PVP), pois, nesse caso, ocorre apenas troca de moedas. Para esse tipo de liquidação, a bolsa utiliza os serviços do Banco B3 como banco liquidante.

Atualmente, a clearing é apenas um departamento da bolsa, com algumas subdivisões: i) clearing de derivativos, ii) clearing de ativos, iii) clearing de câmbio e iv) clearing de ações. A bolsa consolidou todas as clearings em uma: a clearing única.

A maior vantagem de se ter uma clearing única é que todas as posições, tanto de garantias quanto de contratos de derivativos, estão centralizadas em um único sistema de liquidação e custódia, de maneira que a bolsa possa enxergar a posição global dos comitentes e os fatores de risco da sua posição, chamando garantias para a posição como um todo.

---

Dessa maneira, a necessidade de depósito de garantias reduz muito, pois a posição global chamaria menos margem do que cada posição tomada individualmente, por causa do efeito da diversificação de risco entre os fatores.

Em suma, uma clearing única é operacionalmente mais fácil de ser utilizada pelos investidores e necessita menor volume de depósitos de garantia.

A bolsa é a vendedora de todos os compradores e a compradora de todos os vendedores.
A bolsa é efetivamente a contraparte das operações.

## 1.5.3 Papel das corretoras no mercado de derivativos

Só é possível negociar em bolsa por intermédio das corretoras (CTVM). São as ordens de compra e venda em nome das corretoras que aparecem nas filas de negociação de ativos e derivativos, o cliente permanece no anonimato. O cliente é identificado por um código perante a bolsa quando a ordem é executada.

As ordens são realizadas de forma eletrônica, o sistema da corretora serve como roteador das ordens dos seus clientes para o sistema da bolsa. Atualmente, além do roteamento de ordens, os corretores prestam outros tipos de serviços, como o fornecimento de informações, tornando o mercado mais eficiente e auxiliando seus clientes na tomada de decisão.

A receita das corretoras geralmente é baseada na corretagem, que pode ser livremente negociada com cada um dos clientes da corretora, de forma distinta. Além da corretagem, a corretora pode faturar com o floating, ou seja, pode aplicar os recursos dos seus clientes em benefício próprio,

---

provenientes da conta margem e da intermediação de operações. Como a maioria das operações não é liquidada em D+0, a corretora exige de seus clientes que os recursos estejam disponíveis imediatamente, mesmo que a liquidação ocorra dias depois. Com isso, a corretora pode aplicar esses recursos no mercado de open – de remuneração diária.

O cliente é da corretora, e não da bolsa. Logo, toda responsabilidade com relação à liquidação financeira das operações, aos depósitos de garantia e eventual inadimplência do cliente é da corretora, que assume esse risco. Em alguns casos, a corretora pode permitir a alavancagem, ou seja, se o cliente comprar ativos em valores superiores aos recursos financeiros que possui em conta. Em geral, essas operações ocorrem na forma de day trade.

> Day trade são operações na qual toda posição comprada é vendida no mesmo dia, não necessariamente nessa ordem, com o intuito de auferir ganhos em um único dia.

# 1.5.4 Depósito de garantias em bolsa

A maior parte dos ativos depositados como garantia em bolsas é título público. Porém, é possível depositar outros ativos, tais como: ações, títulos privados (ex. Certificado de Depósito Bancário – CDB), cartas de fiança e outros ativos. Em geral, a clearing da bolsa aplica um deságio sobre o valor da margem depositada, que depende da liquidez do ativo depositado e da qualidade creditícia de seu emissor. Os ativos depositados em margem também compõem os fatores de risco do portfólio que o comitente possui em bolsa.

Os títulos públicos têm maior valor para depósito em margem, porque a bolsa considera o valor do PU550, informado diariamente pela Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais (Anbima). O PU550 é equivalente a quase o valor de mercado atual do papel, de tal

---

forma que quase 100% do valor do título é considerado como garantia em bolsa. Como os títulos públicos possuem mais valor em margem, consequentemente é o ativo mais utilizado para tal.

Os títulos públicos são adquiridos em mercados de balcão, podendo ser obtidos diretamente na corretora, realizando o depósito da garantia em bolsa.

A garantia depositada somente será executada se o cliente ficar inadimplente na liquidação financeira de suas operações em bolsa.

Importante lembrar que os títulos depositados em garantia ainda pertencem ao cliente, ficando apenas bloqueados para a venda. Por exemplo, se houver um pagamento de cupom de juros desse título o cliente receberá em sua conta na corretora.

## 1.6 Mercado de derivativos de balcão

O mercado de balcão é aquele realizado diretamente entre as partes, em que as operações são livremente pactuadas. As características das transações, quanto ao prazo e ativo-objeto, são negociadas de modo flexível entre as partes. Os negócios com derivativos realizados em mercado de balcão não necessitam de recinto específico e as operações, em grande parte, são feitas por telefone. Apesar de a negociação ocorrer sem o intermédio da bolsa, a regulação brasileira determina que as instituições financeiras devam registrar os instrumentos financeiros derivativos em sistema administrado por entidades de registro e de liquidação financeira de ativos devidamente autorizados pelo Banco Central do Brasil ou pela Comissão de Valores Mobiliários.

Como essas operações podem ser registradas sem a exigência de garantias, existe o risco individual de crédito entre as contrapartes. O registro dessas

---

operações deve ser feito pelas instituições competentes para tal, como a Cetip (que agora faz parte da B3).

As operações de balcão podem ser registradas com a opção de garantia de liquidação pela clearing, essa opção será determinada no momento do registro, com o consentimento de ambas as partes, sendo que o depósito de garantias passará a ser exigido e administrado pela clearing. Dessa forma, o risco de crédito de ambas as partes passa ser com a clearing, assim como o de uma operação de bolsa.

O processo de registro de operações com derivativos em balcão é flexível, desta maneira, é possível registrar diversos tipos de indexadores, em datas de vencimento não padronizadas, e valores variados. O mercado de balcão oferece maior flexibilidade nos registros das operações em detrimento da liquidez desses instrumentos.

## 1.7 Os principais contratos de derivativos

Os contratos de derivativos são divididos em quatro grandes grupos: termos, futuros, swaps e opções. Esses instrumentos, em sua forma mais simples, são denominados como plain vanilla, em sua forma mais complexa, são denominados como derivativos exóticos.

## 1.7.1 Contrato a termo

O contrato a termo ou forward, em inglês, é a forma mais simples de derivativo, podendo envolver ou não entrega física de mercadoria. O contrato a termo permite que sejam fixados prazo, preço, características e quantidade do ativo-objeto negociado.

---

Por exemplo, suponha que um investidor queira comprar US$ 500.000 daqui a seis meses para honrar um compromisso referente a uma importação. Ele poderia fazer um investimento em dólares hoje ou, alternativamente, poderia ficar comprado em um termo de dólar. Uma conveniência importante para o importador é que no contrato a termo ele não precisa desembolsar nada no instante em que fecha o contrato. Por outro lado, caso deseje fazer o hedge no mercado à vista, necessitaria desembolsar os reais necessários para a compra dos US$ 500.000.

Suponha que o investidor consiga contratar essa operação com uma instituição financeira, com vencimento para daqui a seis meses, a uma taxa de R$ 3,88. Isso significa que ele fixou seu passivo a R$ 3,88 por dólar. Para todo comprador a termo é obrigatória a existência de um vendedor de termo, ou seja, de uma posição inversa.

Depois da operação a termo contratada, vamos supor que o dólar, ao final de seis meses, subiu para R$ 3,98. No vencimento, a liquidação será pela diferença entre o dólar PTAX divulgado na véspera do vencimento e o dólar a termo contratado na operação, da seguinte forma:



Ajuste = (3,98 - 3,88)500.000 = R\ 50.000



Isso significa que o investidor comprado a termo, neste caso, o importador, receberá R$ 50.000 no vencimento da operação. E, por consequência, o vendedor a termo terá de pagar o mesmo valor.

Agora, vamos supor um cenário distinto, no qual o dólar PTAX fica abaixo do preço contratado no termo do vencimento, a R$ 3,83, o resultado da operação para o investidor seria o seguinte:



Ajuste = (3,83 - 3,88)500.000 = -R\ 25.000



Ou seja, o importador teria de pagar R$ 25.000 para a instituição financeira no vencimento da operação. Em contrapartida, o seu passivo de importação também ficaria menor, pois o dólar baixou, compensando a perda no termo.

O termo é a forma mais simples de derivativo, sendo muito didático para entender a essência das operações com derivativos. A Figura 1.1 a seguir denota o resultado com uma operação a termo, o eixo vertical é o resultado

---

no vencimento da operação e o eixo horizontal é a cotação do dólar no vencimento:

Figura 1.1 | Resultado do comprado a termo
![img-0.jpeg](img-0.jpeg)
Fonte: Elaborada pelos autores.

Nota-se, por meio da análise da figura, que o resultado da operação aumenta linearmente à medida que o dólar no vencimento fica maior. No caso da instituição financeira, que está vendida a termo, ao analisar o resultado no vencimento da operação tomada isoladamente, o resultado deverá ser representado pela Figura 1.2:

Figura 1.2 | Resultado do vendido a termo
![img-1.jpeg](img-1.jpeg)
Fonte: Elaborada pelos autores.

---

# 1.7.2 Contrato futuro

O contrato futuro diferencia-se do contrato a termo por duas questões: i) no contrato a termo tem-se baixa liquidez, enquanto que no contrato futuro se tem alta liquidez; entenda liquidez como a capacidade de entrar e sair da posição a qualquer momento; ii) no contrato a termo tem-se risco de crédito (exceto quando é registrado com a opção com garantia na clearing), enquanto que no contrato futuro se tem risco bolsa ou risco clearing.

O contrato futuro tem alta liquidez, porque a bolsa adota a padronização nos contratos. Os contratos são padronizados da seguinte forma:

1. Características no contrato: as especificações do ativo-objeto, a quantidade negociada por contrato e as formas de liquidação – física e financeira.

2. Vencimento do contrato: as datas de vencimento são padronizadas, por exemplo, o contrato futuro de dólar tem vencimento sempre no primeiro dia útil de cada mês. A data de vencimento fixa facilita a negociação, porque os investidores sempre vão negociar o mesmo vencimento. O vencimento padronizado faz com que os comitentes tenham de rolar a posição para próximos vencimentos se quiserem carregar posições por tempo posterior ao vencimento do contrato.

3. Cotação: o preço de negociação do ativo-objeto também é feito de forma padronizada, por exemplo, no contrato futuro de dólar a cotação é feita em reais para cada US$ 1.000 dólares. A cotação dos contratos futuros foi padronizada para facilitar a negociação.

Para eliminar risco de crédito entre os comitentes nas operações com futuros, a bolsa coloca-se como contraparte central das operações. Nesse caso, o risco de contraparte que se assume é o risco da bolsa, que possui

---

risco de crédito quase nulo, devido aos mecanismos de segurança que utiliza para proteger as partes contra eventual inadiplência. A bolsa adota três procedimentos de segurança para ser contraparte central nas operações com futuros:

1. Depósito de garantia: a bolsa solicita depósitos de garantias dos comitentes antes de iniciar a operação e assumir posições no mercado futuro. Diversos ativos podem ser utilizados para depósito em bolsa, como títulos públicos, títulos privados e ações. Ao final de cada dia, a bolsa pode pedir um reforço das garantias, denominado chamada de margem.

2. Ajustes diários: a bolsa utiliza o sistema de liquidações financeiras diárias das operações realizadas durante o pregão ou carregadas em aberto de um dia para o outro. As liquidações financeiras diárias das posições com contratos futuros permitem reduzir o risco da operação para a oscilação de um dia e, como consequência, reduzir o volume necessário de depósitos garantias.

A bolsa necessita de margens de garantia apenas para cobrir a oscilação de um dia nos ajustes dos contratos futuros.

3. Limites de oscilação: a bolsa adotou esse mecanismo de segurança devido a um evento ocorrido no mercado na década de 1990. Em janeiro de 1999, houve uma crise cambial no Brasil, com mudança do regime cambial por bandas para regime flutuante. Devido a forte desvalorização cambial que houve na época, alguns comitentes que estavam com posições vendidas em futuro de dólar ficaram inadimplentes, de tal forma que as garantias depositadas foram insuficientes para honrar toda posição do inadimplemento de ajustes das operações com contratos futuros. A partir do ano de 1999, a bolsa adotou os limites de oscilação para as cotações dos contratos futuros. No início de cada pregão, a bolsa estabelece o preço máximo e o preço mínimo no qual cada contrato

---

futuro pode ser negociado. Ou seja, não haverá registro de negócios se houver vendedores cotando acima do limite superior ou compradores cotando abaixo do limite inferior. Dessa maneira, a bolsa minimizou o efeito de grandes oscilações e reduziu o chamado risco sistêmico.

A operacionalização de contratos futuros é muito similar nas bolsas de contratos futuros no mundo todo. Os códigos de vencimento, depósitos de margem e ajustes diários são parecidos. Se entendermos a negociação de contratos futuros na bolsa brasileira será fácil entender nas bolsas de outros países.

## 1.7.3 Swaps

Os swaps são operações típicas de balcão, geralmente realizadas entre empresas e bancos e muito utilizadas para operações de hedge. É muito comum que as pessoas confundam swap com hedge e pensem que toda operação de swap é destinada ao hedge ou mesmo que esses são sinônimos. Essa é uma percepção equivocada, pois o swap é um derivativo que pode ser utilizado tanto para hedge quanto para especulação.

Os swaps são contratos nos quais as contrapartes acordam em trocar fluxos de caixa ou rentabilidades. No swap, um fluxo de caixa é ativo para o investidor enquanto que o outro fluxo de caixa é passivo. A liquidação financeira do swap é feita pela diferença dos dois fluxos de caixa no vencimento.

Os swaps aceitam praticamente qualquer indexador em seus fluxos de caixa, por exemplo, IPCA (Índice Nacional de Preços ao Consumidor Amplo) mais cupom, dólar mais cupom, ou até mesmo preço de commodities, desde que seja um ativo-objeto cujo preço seja publicamente e fidedignamente divulgado.

---

# 1.7.4 Opções

Os contratos de opções possuem estrutura operacional muito parecida com uma operação a termo. O que distingue a opção do termo é o fato de que uma das partes tem o direito de cancelar a operação de opção caso o resultado da operação lhe seja desfavorável, portanto, deverá pagar um prêmio para a outra parte, para ter esse direito.

Vamos utilizar o exemplo da nossa operação com termo de dólar, no qual o investidor queria comprar US$ 500.000 dólares com vencimento para daqui a seis meses.

No exemplo com o termo, se o dólar PTAX ficasse acima do preço a termo, o investidor receberia um valor, que é a diferença entre o preço do dólar no vencimento e o preço a termo. No nosso exemplo, o PTAX no vencimento estava R$ 3,98 e o preço a termo era R$ 3,88, resultando em um ganho, para o investidor, de R$ 0,10 por dólar.

No momento seguinte discutimos o caso de o dólar baixar para R$ 3,83. Nesse caso, o resultado seria desfavorável para o investidor comprado no termo de dólar.

Se a operação fosse com opção, o investidor comprado poderia solicitar o cancelamento da operação, caso o dólar ficasse abaixo do preço preestabelecido, nesse caso a opção “viraria pó”.

Para ter esse benefício, o comprador deve pagar um valor em dinheiro para o vendedor, no início da operação, denominado prêmio da opção.

O preço preestabelecido do ativo-objeto é denominado como preço de exercício ou comumente denominado como strike. Quem paga o prêmio é denominado titular da opção, e quem recebe o prêmio é o lançador da opção.

O mercado de opções permite uma diversidade de operações, no qual os investidores podem se posicionar com intuitos distintos.

As figuras 1.3 e 1.4 a seguir representam o resultado de uma opção de compra para titular e para o lançador de opção de compra, utilizando nosso exemplo de dólar, e supondo pagamento de prêmio inicial de R$ 20.000:

---

Figura 1.3 | Resultado do titular de opção de compra
![img-2.jpeg](img-2.jpeg)
Fonte: Elaborada pelos autores.

O titular possui uma perda limitada, enquanto o lançador possui um ganho limitado, conforme visualizamos na figura a seguir:

Figura 1.4 | Resultado do lançador de opção de compra
![img-3.jpeg](img-3.jpeg)
Fonte: Elaborada pelos autores.

---

# 1.8 Taxas discretas e contínuas

Quando trabalhamos com derivativos, eventualmente, precisaremos estimar parâmetros, para fins de precificação. Em geral, a distribuição de probabilidade com a qual trabalhamos é a normal, portanto, teremos de trabalhar com uma variável X sim N(μ, σ^2).

Uma variável aleatória com distribuição normal, por característica, deve ir de menos infinito a mais infinito.

Geralmente, a variável aleatória considerada é o preço (S_t) do ativo-objeto, no qual o derivativo é referenciado, ou seja, sem nenhum tipo de transformação. Sabe-se, porém, que o preço do ativo não pode assumir valores negativos, deve estar no intervalo 0 < S_t < ∞.

Por exemplo: qual o menor valor possível de uma ação? É zero, portanto, não é uma variável que vai para menos infinito. Logo, não possui distribuição normal, por definição. Dessa maneira, não é possível descrever a distribuição de probabilidade do preço do ativo por meio de uma função normal.

Contudo, é possível aplicar transformações no preço do ativo-objeto, no intuito de encontrar a variável cuja distribuição de probabilidade seja mais bem ajustada à função normal.

A taxa de retorno discreta (r_t) é obtida por meio da variação do preço do ativo, da seguinte forma:



r_t = S_t/S_(t-1) - 1   (1.1)



A taxa de retorno discreta também não pode apresentar uma distribuição de probabilidade normal, pois o retorno discreto não pode assumir valores

---

inferiores a -100%, pertence ao intervalo -1 < r_t < ∞, pois, de outra forma, o preço do ativo poderia assumir valores negativos.

Continuando com nosso exemplo: qual é o menor retorno possível de uma ação qualquer?

A resposta é -100%, quando o preço da ação atingir valor igual a zero.

A taxa de retorno contínua, por outro lado, é obtida pela diferença dos logaritmos naturais dos preços, segundo a seguinte equação:



R_t = ln(S_t) - ln(S_(t-1))   (1.2)



O retorno contínuo pode, portanto, ser representado da seguinte forma:



R_t = ln(S_t/S_(t-1))   (1.3)



Uma das vantagens do retorno contínuo é que, em modelos de variáveis que seguem processos estocásticos, geralmente utilizados para a precificação de derivativos, é possível extrair o componente de tendência da amostra ao tirar as diferenças dos valores observados. Ao obter o retorno contínuo, tiram-se as diferenças dos logaritmos naturais, o que permite, além de eliminar a tendência dos preços, que a variável taxa de retorno assuma valores dentro do intervalo -∞ < R_t < ∞, exigido para uma distribuição normal.

A Figura 1.5 denota a comparação da taxa de retorno discreta e contínua para as variações no preço do ativo-objeto. No eixo horizontal do gráfico está a variação no preço no ativo denotada por S_t / S_(t-1), no eixo vertical está o retorno, medido em termos percentuais.

À medida que o preço do ativo-objeto decresce, o retorno contínuo tende a menos infinito.

Figura 1.5 | Comparação entre retorno discreto e contínuo

---

![img-4.jpeg](img-4.jpeg)

Fonte: Elaborada pelos autores.

Para taxas entre ± 5%, os retornos discreto e contínuo são muito similares em termos percentuais, eles destoam para variações de maior dimensão. Por razão da cacterística de normalidade e da eliminação de tendência proporcionada pela diferença dos logaritmos, usaremos daqui por diante, o retorno contínuo na maior parte das notações. Além disso, é possível converter taxas discretas em contínuas a qualquer momento, pois o retorno discreto pode ser apresentado do seguinte modo:



(1 + r_t) = S_t/S_(t-1)   (1.4)



Fazendo o exponencial dos dois lados da equação do retorno contínuo, teremos:

---



e^(R_t) = S_t/S_(t-1)   (1.5)



Igualando as duas equações, teremos o cálculo do retorno discreto a partir do retorno contínuo:



r_t = e^(R_t) - 1   (1.6)



E, consequentemente, o retorno contínuo, calculado a partir do retorno discreto:



R_t = ln(1 + r_t)   (1.7)



Existe uma relação bijetora entre essas duas funções, o que permite que trabalhemos com retornos contínuos e a qualquer momento possamos converter para retornos discretos, e vice-versa.

As taxas contínuas também simplificam fórmulas complexas que veremos no decorrer do livro, facilitando significativamente os cálculos. Outra vantagem é que para calcular o retorno acumulado de uma série de retornos, basta somar as taxas contínuas: suponha que o preço inicial de um ativo seja R$ 100. Vamos considerar que no segundo dia o preço subiu para R$ 110 e no terceiro dia caiu novamente para R$ 100. Ao somarmos os retornos contínuos diários veremos que o retorno acumulado é zero, o que faz sentido, pois o preço do ativo no terceiro dia retornou ao seu valor original. Seguem os cálculos dos retornos contínuos do exemplo:

O primeiro retorno, R_t, que calcularemos é em função da variação de preços entre o primeiro e segundo dia da série:



R_t = ln(110/100) = 9,53\%



---

Depois calcularemos o retorno entre o segundo e terceiro dia, R_(t+1):



R_(t+1) = ln (100/110) = -9,53\%



Observe que a soma dos retornos, 9,53\% + (-9,53\%) é igual a zero.

## RESUMO

Neste capítulo introduzimos os conceitos iniciais do mercado de derivativos quanto à sua forma de liquidação e locais de negociação; quanto aos participantes do mercado e aos papéis que cada um deles desempenha. Abordamos a estrutura de negociação em bolsa e a atuação da clearing e uma explicação inicial dos quatro grandes grupos de contratos derivativos.

## EXERCÍCIOS PROPOSTOS

1. Assinale um dos papéis do especulador financeiro no mercado de derivativos:

a. Fazer lucro certo sem assumir riscos.
b. Procura lucrar com a diferença de preços de um mesmo ativo em mercados diferentes.
c. Sempre obtém lucros, em qualquer situação de mercado.
d. Procura fazer lucro, assumindo riscos.

2. Assinale qual das afirmações a seguir é a correta:

a. O arbitrador procura lucrar com as oscilações de preços no mercado futuro, assumindo riscos de mercado.
b. O arbitrador trava um lucro imediato, tirando vantagens da diferença de preços de um mesmo ativo em mercados diferentes.
c. O arbitrador é aquele que produz fisicamente o produto, buscando no mercado futuro um seguro contra oscilações de preço no mercado à vista.
d. O arbitrador é indicado pela B3 para realizar operações de arbitragem nos mercados futuros.

---

3. Um financiador a termo deve:
a. Comprar o ativo-objeto a termo e vendê-lo à vista.
b. Vender à vista e comprá-lo a termo.
c. Comprar a termo e vendê-lo a prazo.
d. Comprar à vista e vendê-lo a termo.
e. Financiar o ativo-objeto e vendê-lo à vista.

4. Defina derivativo.

5. O que são derivativos tóxicos?

6. Quais as principais diferenças entre os contratos futuros e a termo?

7. Explique as principais diferenças entre os mercados de derivativos de bolsa (listados) e de balcão.

8. Qual o papel das clearings ou Câmaras de Liquidação e Custódia?

9. Suponha que você é um produtor de café e deseja eliminar as incertezas de preço da sua produção. Como o uso de derivativos poderia proteger sua safra das oscilações de preços?

10. Qual o racional de a regulação brasileira determinar que as instituições financeiras registrem todos os instrumentos financeiros derivativos em sistema administrado por entidades de registro e de liquidação financeira de ativos devidamente autorizados pelo Banco Central do Brasil ou pela Comissão de Valores Mobiliários?

11. Explique quais são as conveniências das taxas na forma contínua em relação às taxas na forma discreta.

---

12. Calcule o valor futuro (VF) de uma aplicação de R$ 1.000,00 a uma taxa de 5,8269% ao ano, assumindo o regime de capitalização contínua e o prazo de um ano.

13. Sem utilizar a fórmula de conversão de taxa contínua para discreta, calcule a taxa discreta ao ano equivalente do exercício anterior. Dica: calcule a rentabilidade da aplicação.

---

# CAPITULO 2
## Mercado a termo

---

Um contrato a termo é um acordo entre duas partes que define, com antecedência, a quantidade, o preço, a data de entrega e a forma de pagamento de um ativo-objeto negociado. O principal objetivo do contrato a termo é fixar antecipadamente o preço pago pelo ativo-objeto antes da efetiva liquidação da operação, que ocorrerá em uma data futura. Outra característica do contrato a termo é que não há investimento inicial das partes, ou seja, não há liquidação ou desembolso financeiro de nenhuma das partes no início do contrato.

O contrato a termo, no mercado de derivativos, é caracterizado por ser uma operação típica de balcão, em que as duas partes possuem, simultaneamente, obrigações e direitos.

Para ilustrar as características de uma operação a termo, imagine a seguinte situação: uma roupa feita sob medida por um alfaiate. Um cliente interessado em um terno vai à alfaiataria, tira as medidas, escolhe o tecido e firma um preço, após algumas semanas o cliente retorna para pagar e retirar a vestimenta que havia encomendado.

O preço combinado pelo terno inclui o custo com a mão de obra, o custo com o tecido e avimento e a margem de lucro auferida pelo alfaiate. Depois de combinar o preço com o cliente, o alfaiate, ao comprar o tecido no dia seguinte, percebe que houve uma pequena oscilação no preço para cima, o que evidentemente reduziria a sua margem de lucro.

Mesmo assim o alfaiate permanece com o preço pelo terno preestabelecido sem alterações e sem desagradar seu cliente. O prazo estabelecido é suficiente para a elaboração do terno com segurança para ajustes e pequenas correções, sem atraso. No dia marcado o terno é entregue e o pagamento é feito.

A transação mencionada, apesar de sua trivialidade, possui todas as características de uma operação a termo.

---

# 2.1 Nomenclatura e notações dos termos

Para fins de notação, utilizaremos a seguinte nomenclatura:

S_0: representa o preço do ativo à vista na data da operação, t=0

F: representa o preço do ativo a termo fixado no contrato

S_T: representa o preço do ativo à vista na data de vencimento, t = T

A posição do participante do mercado em relação ao contrato a termo será representada da seguinte maneira:

[-F]: vendida a termo

[+F]: comprada a termo

No exemplo do alfaiate, podemos dizer que o cliente estava comprado a termo, enquanto que o alfaiate estava vendido a termo.

A seguir, pode-se visualizar graficamente na Figura 2.1 a estrutura de uma operação a termo, na qual foi realizado um negócio na data de hoje pelo preço contratado fixado em F, sendo que o preço do ativo à vista estava cotado por S_0. O preço do ativo oscilou, chegando ao preço de S_T no vencimento da operação:

Figura 2.1 | Operação a termo
![img-5.jpeg](img-5.jpeg)
Fonte: Elaborada pelos autores.

---

Com relação à posição no contrato a termo, o comprado ganha quando o valor do ativo-objeto subir e o vendido a termo ganha quando o preço do ativo-objeto cair. Sendo W_C o resultado da operação a termo no vencimento para o comprador a termo, tem-se a seguinte relação com o preço do ativo:



W_C = S_T - F (2.1)



Considerando W_V o resultado da operação a termo no vencimento para o vendedor a termo:



W_V = F - S_T (2.2)



Para o comprador a termo, quando o preço do ativo supera o preço do ativo a termo no vencimento, o resultado da operação é positivo:



W_C > 0 ⇒ S_T > F (2.3)



## Exemplo 2.1 - Operação a termo: o criador de gado

Um pecuarista possui 100 cabeças de gado magro no pasto, estima-se que deverá levar seis meses para que possa engordar e vender os bois para o frigorífico pesando, em média, 25 arrobas cada um deles. Hoje, o valor da arroba de boi à vista está em R$ 145.

Preocupado com o preço da carne no mercado interno, o criador poderia fazer a venda a termo de 2.500 arrobas de boi a um preço de R$ 149 por arroba ao frigorífico, para o prazo de seis meses. Dessa maneira, o criador poderia garantir o seu lucro e preocupar-se apenas com os problemas relacionados à criação do gado.

Ao final de seis meses, no vencimento da operação a termo, a arroba de boi gordo à vista está cotada a R$ 144. Qual deverá ser o ganho do pecuarista nessa operação a termo, isoladamente?

Fazendo a venda a termo, com o gado ainda magro, o pecuarista garantiu o preço de venda dos bois a um preço de R$ 149 (F) por arroba, logo, sua posição na operação é como vendedor a termo. Sabendo-se que no vencimento o preço à vista está a R$ 144, o ganho por arroba do pecuarista na operação a termo será de:



W_V = 149 - 144 = R · 5



Sendo assim, o resultado final para o pecuarista da operação de venda a termo de todo o lote de boi gordo foi de:



W_(V  Total) = 5 × 2.500 = R · 12.500



---

O frigorífico, um comprador a termo, teve um resultado negativo na operação de R$ 12.500, valor igual ao da posição do pecuarista, com o sinal invertido. Se o frigorífico tivesse deixado para comprar o gado à vista no vencimento, poderia ter evitado este prejuízo, porém, estaria sujeito às oscilações inesperadas de preços.

Vamos considerar outra situação, na qual o preço da arroba de boi à vista poderia ter subido. Supondo que no vencimento da operação o preço da arroba de boi gordo esteja a R$ 155. Nesse caso seria desvantajoso para o criador de boi, que, no vencimento, poderia ter obtido maior lucro com a venda do seu gado. Mas o criador de boi deveria assumir o risco do preço da arroba de boi? Conceitualmente, não.

Tanto um criador de boi quanto um produtor agrícola ou uma montadora de veículos, por exemplo, se puderem se proteger contra riscos financeiros que não dependam da sua influência ou capacidade administrativa, será mais seguro. Dessa forma, podem focar em suas atividades principais. Exemplos de riscos que deveriam ser protegidos: variação cambial, variação de preços de mercadorias e taxas de juros.

## 2.2 Mercado a termo de ações

Os contratos a termo de ações são negociados no balcão, porém registrados em bolsa de valores. Assim como um contrato a termo tradicional, o termo de ação consiste em um compromisso de compra ou venda de uma determinada ação, a um preço predeterminado, que será liquidado em uma data futura.

**Vencimentos:** os prazos até o vencimento dos contratos a termo de ações são feitos, usualmente, em 30, 60 e 90 dias corridos. Negócios com vencimentos diferentes também podem ocorrer, mas não é usual. Teoricamente, os limites definidos pela B3 são de no mínimo 16 e no máximo de 999 dias corridos.

---

Garantia de liquidação: diferentemente das demais operações a termo de balcão, o termo de ação necessita de depósitos de margem de garantia, porém a liquidação da operação é garantida pela clearing house da B3.

Entrega física: no mercado a termo de ações existe a entrega física do ativo. No vencimento do termo, o comprador a termo é obrigado a ter os recursos necessários para a aquisição das ações. Em contrapartida, o vendedor a termo deverá possuir as ações para a entrega. A bolsa permite o registro de operações com liquidação por diferença, mas não é comumente praticado no mercado.

Liquidação antecipada: o contrato a termo de ações pode ser registrado em duas modalidades: i) liquidação no vencimento e ii) liquidação antecipada. Nesta última, apenas o comprador pode solicitar a liquidação antecipada da operação, com no mínimo três dias úteis antes do vencimento. O vendedor não pode solicitar a liquidação antecipada, dessa forma, o termo de ações é um pouco diferente do termo tradicional, pois existe uma assimetria de direitos e obrigações entre as partes.

Depósito de garantias: quando o investidor opta em comprar uma ação a termo não há desembolso de recursos no momento inicial, porém deverá depositar margem de garantia inicial. Posteriormente, poderão ser solicitadas margens de garantia adicionais, que dependerão da diferença do preço do termo em relação à ação à vista e da volatilidade da ação, calculada pela clearing da bolsa.

Os dividendos e direitos distribuídos às ações do contrato a termo pertencem ao comprador e serão recebidos, juntamente com as ações, na data da liquidação.

Falta de liquidez: a falta de liquidez é uma das características do contrato a termo de ações. Depois de realizada a operação, dificilmente poderá ser desfeita. Isso ocorre porque quando uma ação a termo permanece em carteira por alguns dias, o seu prazo fica diferente dos 30, 60 ou 90 dias.

---

Para se desfazer da posição será necessário o consentimento da contraparte inicial ou que o comprador antecipe a liquidação. A falta de liquidez pode gerar certa ineficiência no mercado a termo, ou seja, o investidor poderá ser penalizado no preço para se desfazer de uma posição.

## Exemplo 2.2 - Termo de ação

A seguir, veremos um exemplo de compra de contrato a termo de ação:

Suponha que as ações preferenciais nominativas da empresa Alpargatas, código ALPA4, está sendo negociada no mercado à vista, na B3, à cotação de R$ 10,00 por ação.

O mesmo papel está sendo negociado a termo, com liquidação em 60 dias corridos, ao preço de R$ 10,21 por ação.

Um investidor acredita na alta do preço desta ação, mas não possui os recursos necessários para adquiri-la à vista. Esse investidor decide, então, comprar 20.000 ações ALPA4 a termo, passível de antecipação, pois poderá apostar na alta da ação, mesmo não a possuindo à vista.

Para realizar essa operação, o comprador deverá depositar margens de garantia iniciais na clearing de ações da B3. Suponha que o investidor possua uma carteira de ações, cujo valor a mercado seja suficiente para cobrir o depósito das garantias solicitadas, e assim o faz.

Ao realizar a operação de compra a termo com antecipação, o comprador poderá solicitar a antecipação da liquidação do contrato a termo, quando lhe for favorável.

Consideremos que a operação de compra a termo foi efetivada na data de hoje e, ao decorrer dos dias, ocorra uma oscilação na cotação da ALPA4. Decorridos 30 dias após o início da operação, a cotação à vista da ALPA4 atinge o patamar de R$ 11,50 por ação, com isso, o comprador a termo decide antecipar a liquidação para garantir um lucro na operação.

A Figura 2.2 a seguir descreve a antecipação feita pelo comprador a termo, com a compra da ação pelo preço estipulado no termo e a consecutiva venda dessa no mercado à vista:

Figura 2.2 | Antecipação do comprador em operação a termo de ação

---

![img-6.jpeg](img-6.jpeg)
Fonte: Elaborada pelos autores.

O lucro do comprador a termo por ação com a liquidação antecipada será de:



W_c = 11,50 - 10,21 = R\ 1,29



O comprador, ao realizar a antecipação do termo, obterá um lucro total de R$ 25.800 ou R$ 1,29 para cada uma das 20.000 ações de ALPA4 compradas a termo. Não haverá desembolso adicional de caixa e não precisará adquirir as ações fisicamente, pois, com a antecipação, haverá a compra da ação a termo e imediata venda no mercado à vista, com liquidação em D+2. O saldo do ganho da operação será discriminado em nota de corretagem e creditado na conta do investidor.

A garantia, inicialmente depositada, estará liberada para retirada com o encerramento da operação de compra a termo, que foi liquidada antecipadamente.

# 2.3 Financiador a termo

Daremos continuidade ao exemplo anterior de compra a termo, para isso precisamos definir a operação de financiamento a termo.

O financiamento a termo consiste na compra de uma ação à vista e simultânea venda desta a termo, com o objetivo de proporcionar um resultado similar a um investimento em renda fixa. Essa operação pode ser contratada diretamente nas corretoras, mediante negociação em balcão e posterior registro em bolsa, logo, possui garantia de liquidação pela clearing.

---

O financiamento a termo é considerado uma venda coberta, por isso não há chamadas de margens adicionais por parte da clearing.

Sendo assim, podemos representar a operação da seguinte forma:



[ + S ₀, - F ] (2.4)



Quando o financiador compra à vista e vende a termo, tem por objetivo realizar uma operação de renda fixa, com garantia da clearing, logo, a operação não possui risco de liquidação no vencimento. A Figura 2.3 representa uma operação de financiamento a termo de ação, supondo que a liquidação de compra da ação à vista ocorra em dois dias úteis (D + 2):

Figura 2.3 | Financiamento a termo de ação
![img-7.jpeg](img-7.jpeg)
Fonte: Elaborada pelos autores.

O financiador obtém uma renda fixa porque o seu investimento inicial é o preço da ação à vista e receberá pela venda dessa mesma ação o valor fixado no termo, obtendo uma taxa de juros, conforme a seguinte equação:



i = ln (F/S ₀) 252/n (2.5)



---

Sendo n o número de dias úteis da operação, considerando que o desembolso de caixa ocorre em D + 2, no nosso exemplo n = 39 dias úteis, logo a taxa anualizada obtida seria:



i = ln (10,21/10) 252/40 = 13,09\%



Suponha que a taxa obtida pelo financiador seja exatamente a taxa livre de risco no período, dado que não existem benefícios fiscais, qual é a vantagem para se fazer essa operação?

O financiador a termo de ações é contraparte do comprado a termo.

Se, eventualmente, houver antecipação do termo de ações, solicitada pelo comprador, haverá uma consequente redução do prazo da operação.

No nosso exemplo, ao comprador antecipar o termo para 30 dias corridos, sabendo que, nesse prazo, teriam 21 dias úteis, o resultado para o financiador seria de:



i = ln (10,21/10) 252/21 = 24,94\%



Com a redução do prazo, o financiador obteve uma taxa 90% superior à taxa livre de risco, de forma que, nessa operação, o comprador a termo ganha com a alta da cotação da ação, e o vendido a termo, sob forma de financiador, ganha com a redução do prazo de liquidação.

Nesse caso, as duas partes ganharam.

Mas se a cotação da ação cair e não houver antecipação?

---

Nesse caso, o financiador recebe a taxa livre de risco, enquanto que o comprador do termo terá uma perda decorrente da queda do preço da ação.

Suponha que no vencimento a cotação da ALPA4 esteja a R$ 9,00 por ação, qual seria o resultado desta operação para o comprador a termo?

Figura 2.4 | Resultado de compra a termo de ação
![img-8.jpeg](img-8.jpeg)
Fonte: Elaborada pelos autores.

O comprador a termo apostava na subida de preço da ação, o que não ocorreu.

O resultado para o comprador deverá ser um prejuízo total de:



W_C = (9 - 10,21) × 20.000 = -R\24.200 



# 2.4 O contrato a termo e a premissa de não arbitragem

Assumiremos a premissa de que o mercado financeiro é basicamente racional, no qual o investidor não consiga obter ganhos anormais sem

---

assumir riscos, mais especificamente, assumiremos a premissa de condição de não arbitragem.

Não iremos ser tão rígidos a ponto de negar a existência de distorções momentâneas nos preços, que permitam operações de arbitragem. Podemos aceitar que oportunidades de arbitragem surjam, mas não possam persistir, pois algum participante, eventualmente – na verdade, muito rapidamente –, identifica a oportunidade e executa as operações necessárias para se beneficiar da situação, garantindo um lucro certo sem assumir riscos, e levando os preços novamente ao equilíbrio.

Partiremos também da premissa de que é possível replicar uma posição de termo com uma carteira sintética, composta pelo ativo-objeto e por um empréstimo pela taxa livre de risco. Ou seja, o termo e a carteira sintética, em condição de não arbitragem, devem ter o mesmo resultado final.

Analisaremos uma situação na qual serão implementadas uma carteira composta por um contrato a termo e uma carteira sintética, composta pelo ativo-objeto e por um empréstimo.

Nesse momento, por simplificação, assumiremos que o ativo não paga dividendos e não possui custos de armazenagem. Em outras palavras, assumiremos que não existe nenhum ônus em manter o ativo, assim como nenhum benefício.

Uma maneira de montar uma carteira, assumindo determinada expectativa, seria comprar um contrato a termo. Sabendo que S_T é o preço do ativo na data T, e F é o preço do ativo a termo, no vencimento T, o resultado da operação será:



W_C = S_T - F \ (2.7)



O resultado da carteira composta pelo termo, W_C, será a diferença entre o preço do ativo-objeto no vencimento e o preço do ativo a termo.

Outra maneira de montar uma carteira com base na sua expectativa, no instante zero, consistiria em comprar o ativo-objeto utilizando recursos obtidos por meio de um empréstimo com o prazo T.

---

Nesse caso, o resultado da operação no vencimento será o valor do ativo-objeto em T, representado por S_T, menos o pagamento do empréstimo, que é o valor do ativo-objeto no instante zero S_0, acrescido de juros r:



W_S = S_T - S_0 e^(rT)   (2.8)



O resultado da carteira sintética, W_S, será a diferença entre o preço do ativo-objeto no vencimento menos o valor pago pelo empréstimo. Para realizar essa operação, fizemos um empréstimo no valor de S_0, à taxa de juros r, pelo prazo T.

Aqui cabe um esclarecimento: você pode se perguntar "mas e se eu já tenho o dinheiro, não preciso pegar emprestado, assim eu elimino o custo do empréstimo, certo?".

Na verdade, é preciso considerar o custo de oportunidade de aplicar na taxa livre de risco. Caso o investidor tivesse o montante necessário para a compra do ativo à vista, esses recursos poderiam estar aplicados pela taxa r. Logo, o custo de empréstimo deverá ser igual ao custo de oportunidade para que a premissa de não arbitragem permaneça válida. Dessa forma, W_C é igual a W_S, portanto:



F = S_0 e^(rT)   (2.9)



Observe que o preço a termo, em condição de não arbitragem não é necessariamente igual à expectativa do preço à vista no vencimento, mas sim igual ao preço do ativo à vista remunerado pela taxa livre de risco.

Exemplificaremos situações de distorções no mercado que permitem a arbitragem, ou "almoço grátis", e quais as estratégias para se beneficiar dessas distorções.

Em cada exemplo a seguir, mostraremos duas situações em relação ao preço do contrato a termo: na primeira situação, mostraremos um contrato a

---

termo sobrevalorizado, em seguida, mostraremos um contrato a termo subvalorizado. Para simplificar, assumiremos as seguintes premissas:

- não há custos de transação;
- o preço de compra do termo é igual ao de venda;
- o lucro nas operações está sujeito ao mesmo tratamento tributário;
- a taxa de aplicação é a mesma da taxa de captação;
- distorções nos preços que permitem a arbitragem não são persistentes;
- não há risco de crédito;
- é possível venda a descoberto (short selling), sem custo.

## Exemplo 2.3 – Arbitragem de contratos a termo de ativos sem rendimento e sem custos de armazenagem

Neste exemplo, utilizaremos os seguintes dados:



{l}
S_0 = R\ 106,00 

r = 14,80\%  a.a.o (taxa contínua) 

Dias úteis = 63 ( T = 63/252  ou  T = 0,25  ano )




Para identificar se o preço do contrato a termo cotado no mercado obedece à premissa de não arbitragem, é necessário calcular o preço livre de arbitragem do ativo a termo:



F = 106 × e^(0,1480 × 0,25) = R\ 110,00



Agora que calculamos o preço livre de arbitragem a termo do ativo, analisaremos duas situações de arbitragem e como se beneficiar em cada uma delas.

### Situação 1 – Preço do ativo a termo cotado pelo mercado está sobrevalorizado

Vamos supor que você receba a cotação de R\ 112,00 para negociar esse ativo a termo. O que você deve fazer para se beneficiar da situação? Calculamos que o preço livre de arbitragem do ativo a termo é R\ 110,00. Ou seja, o preço cotado é

---

maior do que o livre de arbitragem. Para entender a estratégia adotada, primeiro, precisamos decidir se devemos comprar ou vender o ativo a termo cotado. Como o preço cotado é maior do que o calculado (o preço de não arbitragem) – o que faz sentido, comprar ou vender o ativo a termo pelo preço cotado? Ora, quando queremos vender algo, queremos conseguir o maior preço possível. Nessa situação observamos uma distorção do preço do ativo a termo: o preço cotado está mais caro do que deveria, pois é maior do que o preço de não arbitragem. A ideia aqui é, concomitantemente, comprar “barato” e vender “caro” o mesmo ativo, travando um lucro. Logo, devemos vender o ativo a termo pelo preço cotado, R$ 112,00, e comprar o ativo à vista por R$ 106,00. Então, a estratégia a ser implementada é:

1. vender a termo a R$ 112,00;
2. comprar o ativo à vista pelo valor de mercado, R$ 106,00;
3. fazer um empréstimo no valor do ativo à vista, R$ 106,00, à taxa de juros r, 14,80% a.a.o., e prazo de 63 dias úteis ou 0,25 ano.

É importante esclarecer que todas as etapas anteriores deverão ser executadas simultaneamente.

Será que a estratégia deu certo? Observe que todos os parâmetros para calcular o que ocorrerá no vencimento já estão definidos, não há incerteza – o resultado da arbitragem independe do preço do ativo no vencimento. Então, no vencimento teremos os seguintes fluxos de caixa:

- recebimento pela venda do ativo pelo preço a termo: R$ 112,00;
- pagamento do empréstimo: 
106 × e^(0,1480 × 0,25) = R$ 110,00.

Podemos verificar que travamos um lucro de R$ 2,00 para cada unidade do ativo negociado.

## Situação 2 – Preço do ativo a termo cotado pelo mercado está subvalorizado

Agora vamos supor que você receba a cotação de R$ 108,00 para negociar esse ativo a termo. O que você deve fazer para se beneficiar da situação? Já calculamos que o preço livre de arbitragem do ativo a termo é de R$ 110,00. Ou seja, o preço cotado é menor do que o livre de arbitragem. Como o preço cotado é menor do que o calculado (o preço de não arbitragem), o que faz sentido, comprar ou vender o ativo a termo pelo preço cotado?

Quando queremos comprar algo, queremos garantir o menor preço possível. Nessa situação observamos uma distorção do preço do ativo a termo: o preço cotado está mais barato do que deveria, pois é menor do que o preço de não arbitragem. Logo, devemos comprar o ativo a termo pelo preço cotado, R$ 108,00. Então, a estratégia a ser implementada é:

1. comprar a termo a R$ 108,00;
2. vender o ativo à vista pelo valor de mercado, R$ 106,00 – lembre-se que

---

assumimos que é possível venda a descoberto (short selling), sem custo;

3. aplicar o valor da venda do ativo à vista, R$ 106,00, à taxa de juros r, 14,80% a.a.o., e prazo de 63 dias úteis ou 0,25 ano.

Será que a estratégia deu certo? Observe que todos os parâmetros para calcular o que ocorrerá no vencimento já estão definidos, não há incerteza – o resultado da arbitragem independe do preço do ativo no vencimento. Então, no vencimento teremos os seguintes fluxos de caixa:

- recebimento da aplicação pela taxa livre de risco, 14,80% a.a.o.: 
106 × e^(0,1480 × 0,25) = R\ 110,00;

- pagamento pela compra do ativo a termo ao preço, previamente fixado, de R$ 108,00.

Podemos verificar que, mais uma vez, obtivemos um lucro de R$ 2,00 para cada unidade do ativo negociado.

## Exemplo 2.4 – Arbitragem de contratos a termo de ativos com rendimento conhecido

Ao tratar de um termo de ativo com rendimento, precisamos fazer alguns ajustes. Podemos pensar nesse rendimento como sendo, por exemplo, o dividendo pago por uma determinada ação listada na bolsa. Podemos considerar esse dividendo pelo seu valor monetário, que sabemos quando e quanto será pago em dividendos dentro do prazo do contrato a termo. Dessa forma, a fórmula de não arbitragem do preço do ativo a termo será:



F = (S_0 - I)e^(rT) \ (2.10)



Sendo que I é o valor presente dos dividendos que serão recebidos até o vencimento do contrato a termo.

Agora, faremos um exemplo considerando os seguintes dados:



S_0 = R\ 106,00





r = 14,80\%  a.a.o (taxa contínua)





Prazo do Termo = 63  dias úteis \ (T = 63/252  ou  T = 0,25  ano)





d = R\ 5,00 \ (valor do dividendo)



---



Prazo do Pagamento do Dividendo = 25  dias úteis   (T = 25/252  ou  T = 0,10  ano)



Para identificar se o preço do contrato a termo cotado no mercado obedece à premissa de não arbitragem, é necessário calcular o preço livre de arbitragem do ativo a termo. Primeiro, vamos calcular o valor presente do dividendo:



I = 5,00/e^(0.1480 × 0,10) = R\4,93



Agora, basta substituir:



F = (106 - 4,93) e^(0.1480 × 0,25) = R\104,88



Uma vez calculado o preço livre de arbitragem a termo do ativo, analisaremos duas situações de arbitragem e como se beneficiar em cada uma delas.

Caso seja conhecida a taxa de rendimento contínua referente ao dividendo, podemos trabalhar com a fórmula a seguir:



F = S_0 e^((t - q)T)   (2.11)



Sendo que q é a taxa de rendimento contínua do dividendo.

## Situação 1 - Preço do ativo a termo cotado pelo mercado está sobrevalorizado

Vamos supor que você receba a cotação de R\108,88 para negociar esse ativo a termo.

O que você deve fazer para se beneficiar da situação? Calculamos que o preço livre de arbitragem do ativo a termo é R\104,88 e recebemos uma cotação desse ativo a termo de R\108,88.

Ou seja, o preço cotado é maior do que o livre de arbitragem.

Para entender a estratégia adotada, primeiro precisamos entender se devemos comprar ou vender o ativo a termo cotado. Quando queremos vender algo, queremos conseguir vender pelo maior preço possível, certo?

Nessa situação observamos uma distorção do preço do ativo a termo: o preço cotado está mais caro do que deveria, pois é maior do que o preço de não arbitragem. Logo, devemos vender o ativo a termo pelo preço cotado, R\108,88. Desse modo, a estratégia a ser implementada é:

---

1. vender a termo a R$ 108,88;
2. comprar o ativo à vista pelo valor de mercado, R$ 106,00;
3. fazer um empréstimo no valor do ativo à vista, R$ 106,00, à taxa de juros r, 14,80% a.a.o. no prazo de 63 dias úteis ou 0,25 ano.

Todas as etapas mencionadas deverão ser executadas simultaneamente.

Agora, vamos verificar se a estratégia foi bem-sucedida. Observe que todos os parâmetros para calcular o que ocorrerá no vencimento já estão definidos, não há incerteza – o resultado da arbitragem independe do preço do ativo no vencimento. Então, teremos os seguintes fluxos de caixa:

- recebimento pela venda do ativo pelo preço a termo: R$ 108,88;
- pagamento do empréstimo: 106 × e^(0.1480 × 0.25) = R$ 110,00;
- aplicação do dividendo pela taxa livre de risco, desde o seu recebimento até o vencimento do termo: 5,00 × e^(0.1480 × (63 - 25)/252) = R$ 5,12.

Podemos verificar que travamos um lucro de R$ 4,00 ou (108,88 – 110,00 + 5,12), para cada unidade do ativo negociado. Observe que o lucro que calculamos pelos fluxos de caixa no vencimento do termo nada mais é do que a diferença entre o valor a termo sobrevalorizado, R$ 108,88, e o valor livre de arbitragem, R$ 104,88.

## Situação 2 – Preço do ativo a termo cotado pelo mercado está subvalorizado

Agora vamos supor que você receba a cotação de R$ 100,88 para negociar esse ativo a termo. O que você deve fazer para se beneficiar da situação? Já calculamos que o preço livre de arbitragem do ativo a termo é de R$ 104,88. Ou seja, o preço cotado é menor do que o livre de arbitragem. Observamos uma distorção do preço do ativo a termo: o preço cotado está mais barato do que deveria, pois é menor do que o preço de não arbitragem. Logo, devemos comprar o ativo a termo pelo preço cotado, R$ 108,00. Então, a estratégia a ser implementada é:

1. comprar a termo a R$ 100,88;
2. vender o ativo à vista pelo valor de mercado, R$ 106,00 – lembre-se que assumimos que é possível venda a descoberto (short selling), sem custo;
3. aplicar o valor da venda do ativo à vista, R$ 106,00, à taxa de juros r, 14,80% a.a.o., e o prazo de 63 dias úteis ou 0,25 ano.

Será que a estratégia deu certo? Observe que todos os parâmetros para calcular o que ocorrerá no vencimento já estão definidos, não há incerteza – o resultado da arbitragem independe do preço do ativo no vencimento. Então, no vencimento teremos os seguintes fluxos de caixa:

- recebimento da aplicação pela taxa livre de risco, 14,80% a.a.o.: 106 × e^(0.1480 × 0.25) = R$ 110,00;

---

- pagamento pela compra do ativo a termo ao preço, previamente fixado, de R$ 100,88;
- é importante esclarecer que ao vendermos a descoberto, somos responsáveis pelo pagamento dos dividendos pagos por aquela ação. Como essa ação paga dividendo, teremos de fazer um empréstimo de R$ 5,00, referente ao valor do dividendo pelo prazo remanescente e pela taxa livre de risco. No vencimento do termo teremos de pagar 5,00 × e^(0,1480 × (63 - 25)/252) = R$ 5,12.

Podemos verificar que travamos um lucro de R$ 4,00 ou (110,00 - 100,88 - 5,12), para cada unidade do ativo negociado. Observe que o lucro que calculamos pelos fluxos de caixa no vencimento do termo nada mais é do que a diferença entre o valor livre de arbitragem, R$ 104,88, e o valor a termo (subvalorizado), R$ 100,88.

## Exemplo 2.5 – Arbitragem de contratos a termo de commodities

O mercado de termo de commodities tem algumas peculiaridades em relação a outros ativos. O modelo para calcular o preço de não arbitragem segue o mesmo racional dos modelos que vimos anteriormente, porém existem variáveis adicionais, como os custos de armazenagem e as possíveis vantagens de ter o ativo físico disponível. Aqui é importante entender o papel da estocagem ou armazenagem nos mercados de commodities. Em certas ocasiões, o preço à vista da mercadoria pode ficar acima do preço no mercado a termo, ou futuro. Isso ocorre porque o detentor da mercadoria física possui o benefício de reter os estoques e, em busca de melhores preços, aguardar um momento melhor para realizar a venda.

O detentor do estoque, ao tomar essa decisão, deve levar em consideração algumas variáveis relevantes, tais como as taxas de juros, a sazonalidade nos preços, o custo de armazenagem e o benefício esperado com o aumento do preço de venda.

O custo de carregamento é a soma de todos os custos para manutenção dos estoques da mercadoria física e é calculado a partir do custo de financiamento – representado principalmente pela taxa livre de risco e custo de armazenagem, descontando-se o benefício de se ter a mercadoria física disponível, ou retorno de conveniência.

Então podemos expandir o modelo incorporando as principais variáveis que interferem no mercado de commodities:



F = S_0 e^((r + u - γ)T)   (2.12)



Sendo que u e γ representam as taxas na forma contínua do custo de armazenagem e do retorno de conveniência. Na prática, o retorno de conveniência não é conhecido, mas sim calculado por meio das outras variáveis, assim como o custo de

---

armazenagem é normalmente expresso por um valor em alguma unidade monetária (reais, dólares etc.) e não na forma de taxas contínuas. Para simplificar, assumiremos que as variáveis do custo de carregamento são sabidas e expressas por taxas na forma contínua, com o objetivo de tornar os exemplos mais intuitivos.

Agora, faremos um exemplo considerando os seguintes dados:



S₀ = 106,00





r = 14,80\%  a.a.o. (taxa contínua)





u = 2,00\%  a.a.o. (taxa contínua - custo de armazenagem)





y = 3,80\%  a.a.o. (taxa contínua - retorno de conveniência)





Prazo do Termo = 63  dias úteis   (T = 63/252  ou  T = 0,25  ano)



Para identificar se preço do contrato a termo cotado no mercado obedece a premissa de não arbitragem, é necessário calcular o preço livre de arbitragem do ativo:



F = 106,00 e^((0,1480 + 0,02 - 0,038) × 0,25) = R\109,50



Calculado o preço livre de arbitragem a termo do ativo, analisaremos duas situações de arbitragem e como se beneficiar em cada uma delas.

# Situação 1 - Preço do ativo a termo cotado pelo mercado está sobrevalorizado

Vamos supor que você receba a cotação de R$ 113,50 para negociar esse ativo a termo. O que você deve fazer para se beneficiar da situação? Calculamos que o preço livre

de arbitragem do ativo a termo é R$ 109,50. Ou seja, o preço cotado é maior do que o

livre de arbitragem. Para entender a estratégia adotada, primeiro é preciso entender se devemos comprar ou vender o ativo a termo cotado. Quando queremos vender algo, queremos vender pelo maior preço possível. Nessa situação observamos uma distorção do preço do ativo a termo: o preço cotado está mais caro do que deveria, pois é maior do que o preço de não arbitragem. Logo, devemos vender o ativo a termo pelo preço cotado, R$ 113,50. Então, a estratégia a ser implementada é:

1. Vender a termo a R$ 113,50;
2. Comprar o ativo à vista pelo valor de mercado, R$ 109,50;
3. Fazer um empréstimo no valor do ativo à vista, R$ 109,50, à taxa de juros r, 14,80% a.a.o., e prazo de 63 dias úteis ou R$ 0,25 ano.

Todas as etapas mencionadas deverão ser executadas simultaneamente.

Agora vamos verificar se a estratégia foi bem-sucedida. Observe que todos os parâmetros para calcular o que ocorrerá no vencimento já estão definidos, não há incerteza – o resultado da arbitragem independe do preço do ativo no vencimento.

---

O lucro travado será a diferença entre o preço do termo negociado e o preço livre de arbitragem, 113,50 - 109,50 = R$ 4,00.

## Situação 2 - Preço do ativo a termo cotado pelo mercado está subvalorizado

Agora vamos supor que você receba a cotação de R$ 105,50 para negociar esse ativo a termo. O que você deve fazer para se beneficiar da situação? Já calculamos que o preço livre de arbitragem do ativo a termo é R$ 109,50. Ou seja, o preço cotado é menor do que o livre de arbitragem. Como o preço cotado é menor do que calculado (o preço de não arbitragem) — o que faz sentido, comprar ou vender o ativo a termo pelo preço cotado? Ora, a ideia é travar um lucro, comprando "barato" e vendendo "caro" o mesmo ativo. Nesta situação observamos uma distorção do preço do ativo a termo: o preço cotado está mais barato do que deveria, pois é menor do que o preço de não arbitragem. Logo, devemos comprar o ativo a termo pelo preço cotado, R$ 105,50. Então, a estratégia a ser implementada é:

1. comprar a termo a R$ 105,50;
2. vender o ativo à vista pelo valor de mercado, R$ 106,00 — lembre-se que assumimos que é possível venda a descoberto (short selling), sem custo;
3. aplicar o valor da venda do ativo à vista, R$ 106,00, à taxa de juros r, 14,80% a.a.o., e prazo de 63 dias úteis ou 0,25 ano.

É importante esclarecer que todas as etapas anteriores deverão ser executadas simultaneamente.

Agora vamos verificar se a estratégia foi bem-sucedida. Observe que todos os parâmetros para calcular o que ocorrerá no vencimento já estão definidos, não há incerteza — o resultado da arbitragem independe do preço do ativo no vencimento.

O lucro travado será a diferença entre o preço livre de arbitragem e o preço do termo negociado, 109,50 - 105,50 = R$ 4,00.

## 2.5 Arbitragem de contratos a termo de moedas

---

No Brasil, a principal moeda estrangeira utilizada nos contratos a termo e futuro é o dólar, portanto, utilizaremos essa moeda como base deste exemplo – a intuição é a mesma para as outras moedas.

Para calcular a taxa de câmbio a termo é útil fazer uma revisão das taxas de juros a termo.

A Figura 2.5 a seguir representa a taxa de juros a termo:

Figura 2.5 | Representação gráfica da taxa de juros a termo em reais
![img-9.jpeg](img-9.jpeg)
Fonte: Elaborada pelos autores.

Sendo que r_(fwd) é a taxa for Ward discreta, a termo, em reais entre o período T = 1 e T = 2. Algebricamente, temos:



(1 + r_(fwd)) = (1 + r_2)/(1 + r_1) 



Analogamente, podemos aplicar o mesmo raciocínio para o cupom cambial, que é a taxa de juros em dólar no Brasil, como apresentado na Figura 2.6:

Figura 2.6 | Representação gráfica do cupom cambial a termo
![img-10.jpeg](img-10.jpeg)

---

Fonte: Elaborada pelos autores.

Sendo que FRC, neste exemplo, é o cupom cambial a termo no Brasil entre o período T = 1 e T = 2. As taxas expressas por cc representam o cupom cambial "sujo", pois a variação cambial parte da PTAX do dia anterior. O FRC é chamado de FRA de cupom ou Forward Rate Agreement de Cupom Cambial. Algebricamente, temos:



(1 + FRC) = (1 + c c_2)/(1 + c c_1) 



Agora, vamos partir da premissa de que o mercado financeiro é basicamente racional, ou seja, esperamos obter o mesmo rendimento aplicando pela taxa de juros livre de risco em reais e em dólar, no Brasil. A taxa de juros local em dólar é o que conhecemos por cupom cambial e difere, por exemplo, da taxa de juros em dólar nos Estados Unidos, pois a taxa brasileira incorpora determinados riscos intrínsecos ao nosso país.

Algebricamente, para não haver arbitragem temos:



(1 + r) = (1 + c c) × VC 



Sendo que cc representa o cupom cambial e VC a variação cambial. Ou seja, o rendimento em reais pela taxa livre de risco é igual ao rendimento em dólar no Brasil. Esse rendimento em dólar inclui a variação cambial definida pelo mercado naquele instante, acrescida do cupom cambial. Podemos reescrever a Equação 2.15 desta maneira, especificando o componente da variação cambial:



(1 + r) = (1 + c c_(impo)) × D_r/D_0 



---

Sendo que D_0 seria uma taxa de câmbio de referência à vista e D_T seria a taxa a termo. Devido a algumas peculiaridades do mercado nacional, essas duas taxas não são observáveis.

O mercado futuro de dólar normalmente apresenta liquidez para os contratos mais curtos, tipicamente o próximo vencimento. O cupom cambial observável é o cupom "sujo" e não o "limpo". O cupom "limpo" utiliza a taxa de câmbio no mercado spot, ou à vista – e não a taxa Ptax do dia anterior. Apesar de intuitiva, a equação anterior não é implementável para identificar distorções que permitam arbitragem no mercado brasileiro. O melhor que conseguimos com os dados disponíveis no mercado local é:



(1 + r) = (1 + c c_(s u j o)) × D _T/D_(P T A X) tag {2.17}



Sendo que o dólar a termo, D_T, é a incógnita e D_(PTAX) é a taxa de câmbio PTAX do dia útil anterior. A equação anterior ainda não é suficiente para obtermos uma cotação do dólar a termo, pois estamos trabalhando com o cupom cambial sujo e uma taxa de câmbio defasada em um dia útil. Antes de chegarmos à equação utilizada no mercado brasileiro, vamos reescrever a equação anterior:



(1 + c c_(s u j o)) = (1 + r) × D_(P T A X)/D _T tag {2.18}



Para "limparmos" o cupom cambial, vamos substituir o cupom sujo, cc, no FRC:



(1 + F R C) = (1 + r ₂) × D_(P T A X)/D ₂/(1 + r ₁) × D_(P T A X)/D ₁ tag {2.19}



---

Sendo que subscrito representado por "1" e "2" indicam o período, assumindo que estamos no instante 0. Com um pouco de álgebra, obtém-se a seguinte simplificação:



(1 + FRC) = (1 + r_2)/(1 + r_1) × D_1/D_2   (2.20)



Vamos generalizar a equação anterior, partindo das seguintes premissas:

- o dólar futuro para o próximo vencimento, T = 1, é observável;
- a taxa FRC apresenta liquidez e também é observável;
- assim como podemos calcular o dólar a termo para o período T = 2, podemos calculá-lo para qualquer outro período a frente de T = 1;
- para simplificar, o período T coincide com os vencimentos dos contratos futuros da B3, sendo T = 1 o próximo vencimento, T = 2 o vencimento imediatamente posterior.

A nossa incógnita é D_2, que podemos generalizar para qualquer prazo posterior a T = 1, ou simplesmente D_T. Dessa forma, podemos isolar D_T, e, finalmente, obter a equação utilizada no mercado local para cotar um contrato a termo de dólar, agora considerando a contagem de dias úteis, du, e dias corridos, dc, correspondente aos períodos:



D_T = (1 + r_T)^(dos/262)/(1 + r_1)^(dos/262) × D_(F1)/1 + FRC_T × dc_T - dc_1/360   (2.21)



## Exemplo 2.6 - Termo de dólar

Para calcularmos os termos de dólar, vamos assumir os seguintes dados, observáveis na B3: a taxa de juros local livre de risco, na sua forma discreta, é cotada por meio dos contratos DI, e taxas FRC são observáveis no intradia, assim

---

como o dólar futuro do próximo vencimento, T = 1. É importante mencionar que a convenção para a cotação do dólar futuro é multiplicar a taxa por 1.000, ou seja, uma taxa de câmbio futura reais/dólar de 3,132,55 é cotada a 3.132,55. A tabela a seguir apresenta as cotações dos contratos futuros:

Tabela 2.1 | Dados de contratos futuros

|  T | Dias úteis | Dias corridos | r | FRC | Dólar futuro  |
| --- | --- | --- | --- | --- | --- |
|  1 | 14 | 24 | 12,6200% | - | 3.132,55  |
|  2 | 34 | 52 | 12,8300% | 1,3715% |   |
|  3 | 55 | 82 | 12,9970% | 1,5025% |   |

Fonte: Elaborada pelos autores.

Vamos assumir também que a taxa divulgada pelo BACEN no fechamento da data acima, 10 de abril de 2015, como sendo a nossa taxa do ativo à vista: R$ 3,0789.

Então, vamos calcular o preço de não arbitragem do dólar a termo para daqui a 55 dias úteis, ou T = 3.

Substituindo na equação do termo de dólar, temos:



D_(T=3) = (1+0,12997)^(55/252)/(1+0,12620)^(14/252) × 3.132,55/1+0,015025 × 82-24/360 = R\3.188,33



Ou seja, a taxa de câmbio a termo livre de arbitragem para o dólar daqui a 55 dias úteis é de R$ 3,18833.

Agora que calculamos o preço livre de arbitragem do termo de dólar, analisaremos duas situações de arbitragem e como se beneficiar em cada uma delas.

Situação 1 - Preço do ativo a termo cotado pelo mercado está sobrevalorizado

Vamos supor que você receba a cotação de R$ 3,38833 para negociar US$ 1 milhão a termo.

O que você deve fazer para se beneficiar dessa situação? Bem, calculamos que o preço livre de arbitragem do ativo a termo é de R$ 3,18833. Ou seja, o preço cotado é maior do que

o livre de arbitragem. Para entender a estratégia adotada, primeiro precisamos entender se devemos comprar ou vender o ativo a termo cotado. Nessa situação

---

observamos uma distorção do preço do ativo a termo: o preço cotado está mais caro do que deveria, pois é maior do que o preço de não arbitragem. Logo, devemos vender o ativo a termo pelo preço cotado, R$ 3,38833.

Então, a estratégia a ser implementada é:

1. vender a termo a R$ 3,38833;
2. comprar o ativo à vista pelo valor de mercado, R$ 3,0789;
3. fazer um empréstimo no valor do ativo à vista e pela quantidade de dólares negociado, US$ 1 milhão × 3,0789 = R$ 3.078.890, à taxa de juros r, 12,2191% a.a.o. na forma contínua, ou ln(1+12,9970%) e prazo de 55 dias úteis.

É importante esclarecer que todas as etapas mencionadas deverão ser executadas simultaneamente.

Agora, verificaremos se a estratégia foi bem-sucedida. Observe que todos os parâmetros para calcular o que ocorrerá no vencimento já estão definidos, não há incerteza – o resultado da arbitragem independe do preço do ativo no vencimento. No vencimento, teremos:

- recebimento pela venda do ativo pelo valor a termo: US$ 1 milhão × 3,38833 = R$ 3.388.330
- pagamento do empréstimo: R$ 3.078.890 × e^(0,122191 + 55/252) = R$ 3.162.104,58

O lucro travado será a diferença entre os fluxos de caixa no vencimento, R$ 226.225,42.

## Situação 2 – Preço do ativo a termo cotado pelo mercado está subvalorizado

Agora vamos supor que você receba a cotação de R$ 2,98833 para negociar US$ 1 milhão a termo. O que você deve fazer para se beneficiar da situação? Já calculamos que o preço livre de arbitragem do ativo a termo é R$ 3,18833. Ou seja, o preço cotado é menor do que o livre de arbitragem. Como o preço cotado é menor do que calculado (o preço de não arbitragem) – o que faz sentido, comprar ou vender o ativo a termo pelo preço cotado? Ora, a ideia é travar um lucro, comprando "barato" e vendendo "caro" o mesmo ativo. Nesta situação observamos uma distorção do preço do ativo a termo: o preço cotado está mais barato do que deveria, pois é menor do que o preço de não arbitragem. Logo, devemos comprar o ativo a termo pelo preço cotado, R$ 2,98833. Então, a estratégia a ser implementada é:

1. comprar a termo a 2,98833;
2. vender o ativo à vista pelo valor de mercado, R$ 3,0798 – lembre-se que assumimos que é possível venda a descoberto (short selling), sem custo;
3. aplicar o valor recebido pela venda do ativo à vista, US$ 1 milhão × 3,0789 = R$ 3.078.900, à taxa de juros r, 12,2191% a.a.o. na forma contínua ou

---

ln(1 + 12,9970\%), e prazo de 55 dias úteis.

Observe que todos os parâmetros para calcular o que ocorrerá no vencimento já estão definidos, não há incerteza – o resultado da arbitragem independe do preço do ativo no vencimento. No vencimento, teremos:

- pagamento pela compra do ativo pelo valor a termo: US$ 1 milhão × 2,98833 = R$ 2.988.330;
- recebimento da aplicação: R$ 3.078.900 × e^(0,122191 + 55/262) = R$ 3.162.114,85.

O lucro travado será a diferença entre os fluxos de caixa no vencimento, R$ 173.784,85.

## 2.6 Marcação a mercado do contrato a termo

Vamos supor que compramos há um mês um contrato a termo especificando o seu preço em R$ 100,00, e que esse contrato vence daqui a exatamente um ano. Vamos supor também que um contrato a termo, para o mesmo ativo e vencimento da nossa posição comprada a termo valha hoje R$ 110,00. Vamos pensar... o fato do preço do ativo a termo ter aumentado é favorável ou não para a nossa posição comprada?

Nesse caso, travamos o preço de compra em R$ 100,00 e, agora, o mercado está precificando esse mesmo ativo, no mesmo prazo, em R$ 110,00. Se as condições de mercado permanecessem constantes, no vencimento e o ativo realmente valesse R$ 110,00 no vencimento, teríamos um lucro de 110,00 – 100,00 = R$ 10,00, ou seja, teríamos comprado algo por um preço predeterminado em R$ 100,00 e que estaria valendo R$ 110,00.

Esse lucro de R$ 10,00 ocorreria somente daqui a um ano. Parece intuitivo que o resultado estimado hoje, ou marcado a mercado, seria o valor presente destes R$ 10,00 – correto? Então, o valor a mercado do nosso contrato comprado a termo pode ser representado pela seguinte fórmula:

---



MTM_(Termo) = (F_(t  hoje) - F_(t  original)) e^(-rT)   (2.22)



Sendo F_(t  hoje) o preço do ativo a termo cotado hoje (mesmo vencimento do nosso contrato aberto anteriormente) e F_(t  original) o preço do ativo a termo que travamos originalmente quando compramos o termo.

Então, assumindo uma taxa de juros livre de risco, na forma contínua, de 10% a.a. e o prazo de um ano, temos:



MTM_(Termo) = (110 - 100) e^(-0,10 × 1)



Logo,



MTM_(Termo) = 9,05



Para calcular a marcação a mercado de uma posição vendida a termo, basta ajustar a fórmula para:



MTM_(Termo) = - (F_(t  hoje) - F_(t  original)) e^(-rT)   (2.23)



## RESUMO

Neste capítulo abordamos o mercado a termo na sua estrutura operacional, como também as regras de formação de preços por arbitragem. Foram explicadas as operações a termo com ações e a operação de financiamento a termos, termo de commodities, de moeda e ativos com rendimento.

## EXERCÍCIOS PROPOSTOS

1. Uma operação a termo possui as seguintes características:

---

a. Contrato de compra ou venda com liquidação imediata
b. Contrato de compra ou venda com liquidação em prazo determinado
c. Possui duas curvas, uma ativa e outra passiva
d. Não possui liquidação garantida

2. Um criador de boi gordo pode vender arrobas de boi a termo para um frigorífico para seis meses, prazo ideal para o criador, a R$ 141 a arroba, o preço à vista da arroba está a R$ 145 hoje:
a. O criador deve aguardar o preço da arroba cair para R$ 141 para depois vender a termo para o frigorífico.
b. O criador deve esperar.
c. O criador deve vender o boi a termo imediatamente para se proteger contra oscilações no preço.
d. O criador conhece o preço do boi gordo e, por isso, não precisa comprá-lo a termo.
e. O criador deve comprar arrobas de boi gordo a termo, pois pode especular com os preços de venda.

3. O preço da saca do café está a  156 para o contrato futuro de janeiro. Um cafeicultor vende no mercado futuro 700 sacas, garantindo um lucro operacional de  5 por saca. Porém, em janeiro, o preço da saca está a  162, logo, o cafeicultor:
a. Teve prejuízo de  4.200
b. Teve prejuízo de  700
c. Teve lucro de  7.700
d. Teve lucro de  3.500
e. Não teve lucro, nem prejuízo

4. O contrato a termo é registrado:
a. Apenas em bolsa
b. Apenas no balcão
c. Na bolsa e no balcão
d. Apenas na B3

5. O preço de um contrato a termo de ações na B3:
a. É igual ao preço da ação à vista
b. É menor que o preço da ação à vista

---

c. E igual ao preço da ação à vista mais uma parcela correspondente aos juros
d. É maior que o preço a termo de PETR4

6. O termo de ações pode ser negociado nos seguintes prazos:
a. No mínimo 16 dias e no máximo 999 dias corridos
b. Qualquer prazo, desde que seja mais do que três dias úteis
c. Apenas em 30, 60 e 90 dias corridos
d. Com vencimento de, no máximo, 24 meses

7. A liquidação de um contrato de termo de ação:
a. Não pode ser antecipada
b. Pode ser antecipada, com a entrega das ações pelo preço estipulado no termo
c. Pode ser antecipada, com a entrega das ações pelo preço de mercado
d. Pode ser antecipada, com a entrega das ações por preço estipulado pela CBLC

8. A antecipação de um contrato a termo de ações:
a. Pode ser solicitada pelo comprador
b. Pode ser solicitada pelo vendedor
c. Não pode ser solicitada antes do vencimento
d. Não implica na entrega física das ações

9. Um financiador a termo compra ações Petrobrás PN à vista por  12 e vende a termo por  12,24 com 42 d.u. Sabendo-se que a liquidação financeira da operação à vista acontece em três dias úteis, a taxa de retorno obtida pelo financiador é de:
|  a. 14,50% a.a.o. | c. 12,87% a.a.o. | e. 12,00% a.a.o.  |
| --- | --- | --- |
|  b. 13,65% a.a.o. | d. 15,06% a.a.o. |   |

10. Um arbitrador analisa as taxas de câmbio e do DI em busca de uma operação de ganho certo. O dólar à vista está cotado a R$ 3,17, a taxa do CDI está cotada a 14,3% a.a.o. para quatro meses (120 dias corridos) e o cupom de dólar a 3,5% a.a. Para que o arbitrador não consiga realizar ganhos, o valor do dólar a termo para quatro meses, (ou 83 dias úteis) deverá ser de:
|  c.  3,49 | e.  3,23  |
| --- | --- |

---

a.  3,86
b.  3,01 d.  3,27

11. O dólar a termo para 60 dias (42 dias úteis) está cotado a R$ 3,35, sendo que a taxa do CDI projetada para o mesmo período é de 14% a.a.o. Sendo o dólar à vista cotado a R$ 3,29, a taxa de remuneração do dólar (cupom cambial) deverá ser de:

a. 3,32% a.a. c. 4,10% a.a. e. 3,30% a.a.
b. 2,26% a.a. d. 14,16% a.a.

12. Defina o que é um contrato a termo.

13. Uma empresa tem de tomar uma decisão de investimento com base nas premissas a seguir: tem tem disponível uma taxa de aplicação em CDB Pré de 14% a.a.o., mas tem também um ativo com rendimento em dólar de 4,46% a.a. Sabendo que o prazo que a empresa está disposta a investir é de 270 dias corridos (193 dias úteis), dólar spot é de R$ 3,25, e o dólar a termo é de R$ 3,50, qual o melhor investimento para empresa? Há a possibilidade de arbitragem?

14. Considere a tabela a seguir com dados de fechamento da B3.

|  Cód. | Vencimento | Du | Dc | DI 1 dia | Taxa spot | FRC | Dólar  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  K15 | 4-5-2015 | 14 | 24 | 99.341,90 |  | - | 3.102,54  |
|  M15 | 1-6-2015 | 34 | 52 | 98.384,54 |  | 1,38% |   |
|  N15 | 1-7-2015 | 55 | 82 | 97.368,38 |  | 1,50% |   |

Calcule:
a. As taxas de juros à vista, com base nos preços de ajuste do contrato DI futuro.
b. O dólar sintético (dólar a termo) para 1/6 e 1/7.
c. Calcule o ajuste de uma operação de compra de dólar a termo com vencimento em 1/7/2015 e com notional de US$ 5 milhões. Assuma que a taxa de câmbio fixada deste contrato de termo foi a calculada no item b). Assuma também que o dólar de fechamento no vencimento da operação foi de  3,50.

---

15. (Sugestão: utilize o MS-Excel para resolver este exercício) Considere os PUs de ajuste do mercado futuro de juros – DI futuro de 1 dia e os PUs de ajuste do mercado futuro de cupom cambial – DDI, ambos negociados na B3:

|  N. | Du | Dc | DI-1dia | Taxa spot | FRC | Dólar  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 10 | 13 | 99.481,39 |  | -- | 3.000,00  |
|  2 | 30 | 45 | 98.426,57 |  | 1,00% |   |
|  3 | 50 | 75 | 97.349,17 |  | 1,50% |   |
|  4 | 72 | 105 | 96.085,48 |  | 2,00% |   |

**Determinar:**

a. As taxas de juros à vista.
b. As taxas de câmbio a termo (dólar sintético).
c. Calcule o ajuste de uma operação de venda de dólar a termo com vencimento em 72 dias úteis e com notional de US$ 10 milhões. Assuma que a taxa de câmbio fixada neste contrato de termo foi a calculada no item b. Assuma também que o dólar de fechamento no vencimento da operação foi  3,20.

---

# CAPITULO 3
## Mercado futuro

---

Neste capítulo, aprenderemos as regras de operacionalização dos contratos futuros como ajuste diário e chamada de margem. Essas regras são muito similares em outros mercados futuros de bolsas ao redor do mundo. O que diferencia os mercados futuros no Brasil de outras bolsas são as características do ativo, os ativos aceitos como depósito de garantia, existência ou não de liquidação física, tamanhos de lotes e formas de cotação. O restante é muito similar, até mesmo os códigos de vencimento dos contratos futuros.

A estrutura moderna de negociação em mercados futuros surgiu nos Estados Unidos, na segunda metade do século 19. Em 1848, foi fundada a Chicago Board of Trade (CBOT), que desde o início operava commodities agrícolas.

Apresentaremos os diferentes tipos de mercados futuros existentes no Brasil: renda variável, moeda e juros. Vale ressaltar que existe farto material didático de excelente qualidade disponível na internet – especialmente no site da Bolsa (B3) – sobre as especificações dos contratos futuros. Nas seções seguintes, vamos apresentar os principais contratos futuros e as possibilidades de realizar operações de hedge, arbitragem e especulação.

## 3.1 O contrato futuro

Mais padronizado do que o mercado a termo, o mercado futuro está presente em mercados organizados de bolsas. Os contratos futuros possuem, em sua maioria, maior volume de negociação do que o contrato a termo, portanto são mais líquidos, mais transparentes para as partes envolvidas e publicamente divulgados, servindo como referência na formação de preços.

O contrato futuro é bastante similar ao termo. É também um acordo de compra e venda de determinado ativo, com liquidação em data preestabelecida e a preço predeterminado.

A liquidação do contrato futuro também pode ser física ou por diferença. Nas negociações do mercado futuro, as contrapartes não se conhecem, são

---

anônimas, porém as operações são publicamente divulgadas. Na prática, a bolsa é a contraparte de todas as partes.

No Brasil, os contratos futuros são negociados em bolsa, na B3. Schouchana e Miceli (2004, p. 10) definem as características do contrato futuro da seguinte maneira: Nos contratos futuros, constam especificações de qualidade dos produtos negociados, cotação, variação mínima de apregoação, oscilação máxima diária, unidade de negociação, meses de vencimento, data de vencimento, local de formação do preço e de entrega da mercadoria, período e procedimentos de entrega e retirada da mercadoria, liquidação financeira, arbitramento, ativos aceitos como margens de garantia e custos operacionais. Os contratos futuros são padronizados, de modo que, no pregão, sejam negociados o preço e a quantidade de contratos, uma vez que todos se referem ao mesmo produto, mesmo local de entrega e mesma quantidade por contrato.

As características dos contratos futuros são padronizadas pela bolsa: prazos, volumes, tamanho do contrato, características do ativo, cotação em bolsa, ajustes diários e margens de garantia.

A câmara de liquidação, para garantir a efetiva liquidação das operações, exige depósitos de garantia dos participantes do mercado. No caso de qualquer uma das partes não honrar com suas obrigações em relação ao contrato futuro, a câmara de liquidação pode, arbitrariamente, executar as garantias depositadas e liquidar a posição do participante inadimplente.

Para reduzir os valores de depósito de margem, as bolsas de valores adotaram o mecanismo de ajustes diários. Eles consistem nas liquidações financeiras das posições pelo método de ajuste por diferença, ou seja, a câmara de liquidação, com base nos preços de ajuste divulgados pela bolsa, realiza o fluxo financeiro das posições dos participantes, em relação às oscilações de preços dos contratos futuros de um dia para o outro.

Com a utilização do mecanismo de ajuste diário, a margem de garantia requerida para cobrir a liquidação financeira de um dia fica muito menor do que se fosse exigida para cobrir o equivalente ao período integral do contrato. Na prática, a liquidação financeira dos contratos futuros é diluída, ocorrendo em partes - diariamente - em vez de em uma única vez no vencimento, como nos contratos a termo.

---

# 3.2 Diferenças entre contrato a termo e futuro

As regras de arbitragem, já explicadas anteriormente, para o mercado a termo são também aplicáveis ao mercado futuro.

Existem algumas diferenças fundamentais entre o mercado a termo e futuro. A primeira é que o termo é negociado em balcão, enquanto que o futuro é negociado em bolsa. No Brasil, o mercado futuro é negociado exclusivamente em pregão eletrônico.

Outra diferença é que o mercado futuro possui alta liquidez enquanto o mercado a termo possui baixa liquidez. Vamos entender a liquidez como a capacidade de entrar e sair de posição comprada ou vendida sem dificuldades. O mercado futuro, em geral, é mais líquido devido à padronização. As principais padronizações promovidas pela bolsa são: a. Contrato: no contrato futuro são padronizadas as características do ativo-objeto negociado, possibilidade de entrega física, tamanho do lote de negociação por contrato, código de negociação, regras para o ajuste diário e liquidação no vencimento do contrato. O contrato padronizado permite que os participantes negociem exatamente o mesmo tamanho de lote em unidades de contratos futuros.

b. Vencimento: os contratos futuros possuem datas de vencimento fixadas, por exemplo, o contrato futuro de dólar possui vencimento sempre no primeiro dia útil de cada mês. Mesmo tendo vencimento padronizado, os participantes conseguem encerrar sua posição a qualquer momento, operando seus contratos antes da data de vencimento, devido à alta liquidez.

c. Cotação: a forma de negociação dos contratos futuros é padronizada desde que a negociação era feita pelo pregão viva-voz. A padronização dos contratos facilita o apregoamento do contrato. Por exemplo, o contrato futuro de DI é negociado na forma de taxa de juros exponencial 252, com três casas decimais.

---

Outra diferença entre o contrato a termo e futuro é que o futuro possui garantia da bolsa – especificamente, da clearing da bolsa – ou seja, a bolsa é a contraparte central. Portanto, quando se opera contratos futuros há baixíssimo risco de crédito de contraparte. Apesar das operações serem realizadas entre diversas contrapartes, é a bolsa, que, no fim, assume o risco como contraparte dos comitentes com posição em aberto. Para assumir o risco de contraparte, a bolsa utiliza alguns mecanismos de segurança, entre eles:

a. Solicitação de depósito de garantias: para operar contratos futuros em bolsa é necessário o depósito de ativos em garantia, que depende da exposição em risco da carteira do comitente de seus contratos em aberto.

A bolsa pode pedir depósitos de garantia adicional, denominados chamada de margem. A bolsa recalcula diariamente a exposição a risco, os cenários de estresse, os fatores de risco e a volatilidade para recalcular a margem necessária para depósito de cada um dos comitentes. Os ativos aceitos como garantia são: ações, dinheiro, cartas de fiança, mas, principalmente, títulos públicos. Atualmente, cerca de 90% de todo o depósito de garantia para contratos futuros são títulos públicos. Qual a vantagem de depositar títulos públicos como garantia em bolsa? Os valores dos títulos públicos são determinados pelo PU da Resolução 550 do BACEN, que são os preços dos títulos para lastro, que considera quase 100% do seu valor de mercado, enquanto que o valor em garantia de ações é determinado por uma tabela de deságio, e apenas as ações mais líquidas possuem valor de garantia em margem.

Dessa maneira, é muito mais vantajoso depositar títulos públicos em margem para negociação com contratos futuros, pois possuem valor maior e remuneram o investidor.

b. Ajuste diário: a bolsa realiza liquidações financeiras diárias de todas as negociações com contratos futuros e das posições em aberto carregadas para o dia seguinte. Isso ocorre para mitigar o risco de liquidação no vencimento. No contrato a termo, a liquidação financeira se faz, de maneira geral, apenas no vencimento, ou seja, as contrapartes assumem um risco acumulado de crédito por toda a existência do contrato a termo, enquanto que, no contrato futuro, as liquidações financeiras

---

ocorrem diariamente, com base no preço de ajuste divulgado pela bolsa. O ajuste diário foi adotado para reduzir o risco

de liquidação e inadimplência e, com isso, reduziu também margem de garantia necessária. Se o contrato futuro fosse liquidado como um contrato a termo, ou seja, apenas no vencimento, o valor de margem de garantia solicitado pela bolsa seria muito maior.

c. Limites de oscilação: esse mecanismo de segurança foi adotado pela bolsa, porque, em janeiro de 1999, houve a maxidesvalorização do real e, com isso, alguns comitentes com posição vendida em dólar ficaram inadimplentes, e os ativos depositados em margem perderam valor com a crise que se instaurou naquela época, de tal forma que os ativos depositados em margem não foram suficientes para cobrir os ajustes diários. A bolsa teve de utilizar recursos do fundo de liquidação, quando os ativos depositados em garantia se esgotaram. No mesmo ano, em 1999, a BM&F passou a adotar os limites de oscilação. Nesse mecanismo, antes do início de cada pregão, a bolsa divulga os limites superior e inferior de preços nos quais cada contrato futuro pode ser negociado, sendo que não é permitido executar ordens fora dos limites estipulados pela bolsa. Com esse mecanismo, a bolsa visa evitar que os preços dos contratos futuros oscilem acima dos riscos cobertos pelos valores das garantias depositadas, evitando, dessa forma, usar recursos do fundo de liquidação.

Se a cotação de qualquer contrato futuro atingir algum dos limites, as ordens não são executadas até que as ordens colocadas fiquem novamente dentro do intervalo. Esse mecanismo é diferente do cicuit breaker, que ocorre no mercado de ações. Nos limites de oscilação, se as ordens não voltarem para dentro dos limites estipulados pela bolsa, as execuções das operações somente ocorrerão no dia seguinte, quando novos limites forem divulgados e novas ordens forem enviadas.

Uma pergunta pertinente que pode ser suscitada pelo leitor é: se já existem os ajustes diários para mitigarem os riscos de inadimplência de uma contraparte, qual o motivo da bolsa ainda pedir o depósito de garantias? Os ajustes diários são calculados após o fechamento do pregão e tendem a cobrir os riscos de inadimplência dadas as oscilações "normais" de preços. Uma variação drástica de preços resultará em um ajuste diário "anormal",

---

de grande magnitude, para uma das partes. Neste caso, pode ocorrer que essa parte não tenha condições de arcar com esse ajuste inesperado. Por isso, a bolsa, preventivamente, solicita os depósitos de garantia, pois no caso de uma das partes não ter condições financeiras de pagar pelo ajuste, as garantias previamente depositadas por esta parte permitiriam à bolsa viabilizar a liquidação do ajuste diário. Portanto, a principal função das garantias é tentar cobrir o risco de oscilações não cotidianas, causadas por eventos de estresse no mercado.

# 3.3 Futuro de dólar

O contrato futuro de dólar é um dos contratos mais líquidos da bolsa, possui vencimento sempre no primeiro dia útil de cada mês. O tamanho do contrato é de US$ 50 mil, negociado em múltiplos de cinco contratos e sua cotação é em reais para cada US$ 1.000.

A cotação do dólar é a mesma desde quando o pregão era viva-voz, que se encerrou em junho de 2009. Agora, a negociação desses instrumentos é feita por meio de plataforma eletrônica.

Vamos analisar o volume negociado de dólar e suas características na Tabela 3.1:

Tabela 3.1 | Volume negociado de futuro de dólar

|  Veneto | Contr. Abert. | Contr. Fech. | N. Negoc. | Contr. Negoc. | Vol.  |
| --- | --- | --- | --- | --- | --- |
|  V17 | 474.559 | 490.080 | 32.880 | 286.725 | 45.102.908.000  |
|  X17 | 10.300 | 10.300 | 3 | 1.090 | 172.438.000  |
|  Z17 | 4.005 | 4.005 | 0 | 0 | 0  |
|  F18 | 9.090 | 9.090 | 3 | 1.000 | 159.740.000  |

Fonte: B3.

Na primeira coluna estão os códigos de vencimento, por exemplo, V17 é o vencimento no primeiro dia útil de outubro de 2017, X17 é o vencimento

---

de novembro de 2017, e assim sucessivamente.

A segunda coluna indica o volume de contratos em aberto na abertura do pregão, a terceira coluna indica o volume de contratos em aberto no fechamento do pregão, a quarta coluna indica o número de negócios ocorridos durante o pregão em questão. A quinta coluna indica a quantidade de contratos negociados no dia, enquanto que, a última coluna da direita indica o volume negociado em reais, ou seja, cerca de R$ 45 bilhões em valor nocional foram negociados no dia, no primeiro vencimento do futuro de dólar.

Analisando a tabela, podemos notar que a liquidez é muito concentrada no primeiro vencimento de dólar. Se quisermos fazer uma operação longa, utilizando contratos futuros de dólar, deveremos carregar o primeiro vencimento, fazendo a rolagem a cada mês.

# A flexibilidade do contrato futuro de dólar

O fato do contrato de dólar possuir vencimento apenas no primeiro dia útil de cada mês pode passar a falsa impressão de que não é possível fazer um hedge, por exemplo, de uma operação de câmbio que vencerá no dia 15 do mês.

Vamos lembrar que o contrato futuro de dólar é muito líquido, o que significa que podemos carregar a posição de hedge virtualmente para qualquer prazo. Ou seja, se um hedger mantém uma posição comprada em dólar, para proteger uma operação de câmbio que ocorrerá no dia 15, é possível encerrar a posição em dólar futuro na data exata, ou seja, vendendo os contratos futuros exatamente no dia 15, protegendo-se até a data desejada.

Vamos supor que uma empresa possua um passivo em dólares e deseja fazer o hedge utilizando contratos futuros de dólar negociados em bolsa. Para executar o hedge desse passivo, a empresa deverá comprar futuro de dólar em igual proporção. Por exemplo, se a empresa possui uma dívida de US$ 50 milhões, deverá comprar mil contratos de dólar, cujo valor nocional é de US$ 50 mil por contrato.

---

# 3.3.1 Rolagem de futuro de dólar

No vencimento do futuro de dólar, a posição extingue-se, utilizando como último preço de ajuste o dólar oficial divulgado pelo BACEN, conhecido como PTAX800.

Se quisermos dar continuidade na posição, devemos executar a rolagem do dólar, que pode ser realizada de duas formas: a. Encerrando posição no primeiro vencimento e abrindo posição no segundo vencimento: para isso, temos de vender os contratos do primeiro vencimento, se estivéssemos originalmente comprados, e recomprar no próximo vencimento, ou vice-versa, se a posição original for vendida em dólar. Esse procedimento gera o que denominamos de disputa entre comprados e vendidos. No momento da rolagem, todos querem os melhores preços, para reduzir o custo de carregamento da posição.

b. DR1: a bolsa disponibilizou uma estratégia que consiste na rolagem rápida do futuro de dólar. Quando compramos um DR1, a bolsa registra a compra do segundo vencimento de futuro de dólar e a venda do primeiro vencimento. O que é negociado no DR1 é apenas a diferença, em termos de pontos para cada US$ 1.000, entre o segundo vencimento de futuro de dólar e o primeiro. Cada DR1 negociado está na proporção de um contrato futuro de US$ 50 mil.

## Exemplo 3.1 - DR1

O DR1 é um instrumento prático para realizar a rolagem de dólar. Vamos supor que o primeiro vencimento de futuro de dólar, V1, está sendo negociado a 3.153 pontos e o DR1 está sendo negociado a 14 pontos. Suponhamos também que temos uma posição em aberto, comprada em 5.000 contratos de futuro de dólar de vencimento V1 e queremos rolar para o próximo vencimento.

Como faremos a rolagem de dólar para o próximo vencimento - V2?

---

O que devemos fazer é comprar 5.000 DR1, se desejamos vender V1 e comprar V2. Ao executar a operação de DR1, a bolsa registra uma venda de 5.000 contratos de vencimento V1 ao preço de 3.153 e uma compra de 5.000 contratos, vencimento V2 ao preço de 3.167. Ou seja, o preço no segundo vencimento é igual a 3153 + 14 = 3167, logo, adicionamos os pontos do DR1 ao primeiro vencimento para determinar o preço do segundo.

Se, por acaso, o participante queira rolar uma posição vendida, é necessário apenas vender DR1 na mesma quantidade. É importante notar que, no código do DR1 aparece o vencimento dos dois contratos, por exemplo, V7X7.

## 3.3.2 Minicontrato de dólar futuro

Inicialmente, o minicontrato de dólar foi dimensionado para a negociação por pessoa física. O mini foi direcionado ao que a bolsa denominava de web trading, para negociações via home broker. Atualmente, o mini de futuro de dólar é negociado em diversas plataformas, não apenas por pessoa física.

O mini de dólar possui um tamanho de US$ 10 mil, ou seja, um quinto do tamanho do contrato padrão de dólar. Além disso, pode ser negociado em lotes unitários, não precisa ser negociado em múltiplos de cinco contratos, como é feito no contrato padrão.

É possível arbitrar entre o minicontrato de dólar e o contrato padrão?

Há possibilidade de arbitragem, ajustando as quantidades na proporção de cinco contratos padrão para cada 25 minicontratos de futuro de dólar. Geralmente, esses contratos já estão perfeitamente arbitrados, pois como é uma arbitragem simples de ser realizada, haverá sempre robôs de comitentes procurando pequenas diferenças de preços.

---

# 3.3.3 Ajuste de operação com futuro de dólar

A Tabela 3.2 apresenta os preços de negociação e de ajuste diário do contrato futuro de dólar:

Tabela 3.2 | Preços e ajustes do contrato futuro de dólar

|  Veneto | Preço abert. | Preço mín. | Preço máx. | Preço méd. | Últ. preço | Ajuste  |
| --- | --- | --- | --- | --- | --- | --- |
|  V17 | 3.153,00 | 3.134,00 | 3.159,00 | 3.146,07 | 3.153,50 | 3.153,64  |
|  X17 | 3.164,00 | 3.164,00 | 3.164,00 | 3.164,00 | 3.164,00 | 3.167,22  |
|  Z17 | 0 | 0 | 0 | 0 | 0 | 3.179,16  |
|  F18 | 3.195,00 | 3.194,50 | 3.195,00 | 3.194,80 | 3.194,50 | 3.190,12  |

Fonte: B3.

Na última coluna da direita, podemos observar os preços de ajuste divulgados diariamente pela bolsa. Os preços de ajuste são utilizados para o cálculo de ajuste diário para as operações realizadas no dia e para as posições carregadas em aberto do dia anterior.

É possível notar, também, que, mesmo em vencimentos que não houve negociação, a bolsa divulga o preço de ajuste para as posições que, eventualmente, foram carregadas em aberto de datas anteriores.

Os preços de ajuste divulgados pela bolsa, além de serem essenciais para o ajuste financeiro diário das operações, também são importantes para a marcação a mercado de outras operações, pois passam a ser preços de referência.

É importante lembrar que os preços de ajuste, principalmente o do futuro de dólar, estão em condição de não arbitragem, ou seja, o ajuste respeita as equações de arbitragem comumente utilizadas no mercado de derivativos e discutidas em capítulos anteriores.

---

Para a equação de ajuste das operações de dólar futuro utilizaremos a notação similar à da bolsa, para não gerar inconsistência, que é apresentada da seguinte forma:



AJ = (PA - PO)N(50) \ (3.1)



Sendo:

**AJ**: valor do ajuste diário

**PA**: preço de ajuste do dólar, divulgado diariamente pela bolsa, na cotação reais para cada US$ 1.000

**PO**: preço da operação em reais para cada US$ 1.000

**N**: número de contratos, em múltiplos de 5

No contrato padrão de dólar, multiplicamos por 50 ao final, no minicontrato, multiplicamos por 10.

## Ajuste de futuro de dólar

Agora, utilizando os preços de ajuste da tabela, vamos fazer um exemplo de operação de dólar. Vamos supor que fizemos duas operações de futuro de dólar, sendo uma comprada e uma vendida, da seguinte forma:

Tabela 3.3 | Exemplo de operação com futuro de dólar

|  Operação | Posição | Quantidade | Contrato | Vencimento | Preço da operação | Preço de ajuste  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | Comprada | 500 | Fut. de Dol. | V17 | 3.134 | 3.153,64  |
|  2 | Vendida | 300 | Fut. de Dol. | V17 | 3.159 | 3.153,64  |

Fonte: Elaborada pelos autores.

Utilizando as informações da Tabela 3.3, podemos determinar a posição em aberto.

Se o participante comprou 500 e vendeu 300 contratos, logo, ao fim do

---



pregão, a posição em aberto ficou comprada em 200 contratos futuros de dólar, ao preço de ajuste de 3.153,64. Todos os comitentes que ficam com posição em aberto ao final do pregão, o preço dessa posição será o de ajuste, divulgado pela bolsa.

Vamos agora calcular o valor do ajuste diário da operação 1, que foi uma compra de 500 futuros ao preço de 3.134. O valor do ajuste será:

AJ=(3.153,64-3.134)500(50)=491.000

Na operação 1, receberemos um valor positivo de ajuste de R$ 491.000,00, e na operação 2 o valor de ajuste será:

AJ=(3.153,64-3.159)(-300)(50)=80.400

Na operação 2, receberemos um valor positivo de ajuste de R$ 80.400,00. O ajuste total diário será a soma dos ajustes de todas as operações realizadas no dia, adicionando-se a isso as operações em aberto do dia anterior, no nosso exemplo:

AJ_(total)=80.400+491.000=571.400

O ajuste diário total será positivo em R$ 571.400,00, cuja liquidação financeira ocorrerá em D+1.

## 3.3.4 Casado de dólar e FRP

A operação de casado de dólar consiste em duas operações simultâneas e invertidas em dólar à vista e futuro de dólar, na mesma proporção. O que se deseja operar é a diferença de pontos entre o dólar à vista e o futuro.

---

Quando um banco executa uma operação de câmbio para uma empresa, na verdade, estará operando casado de dólar. Por exemplo, se um banco vende dólares para um importador, simultaneamente comprará dólar futuro, garantindo um lucro por arbitragem, na diferença de pontos entre o dólar pronto e o futuro.

Os pontos de diferença podem ser calculados em condição de não arbitragem, pela subtração entre as cotações do dólar futuro e do dólar pronto, multiplicado por 1.000:



D ₀ = F - S ₀   (3.2)



Sendo:

D₀: diferença em pontos entre o dólar futuro e à vista, neste momento

Devemos considerar ainda que existe uma relação entre os preços à vista e futuro, obtida pela diferença entre a taxa livre de risco e o custo de carregamento, conforme a seguinte equação geral de arbitragem:



F = S ₀ e^((r - q) T) = S ₀ e^(r T)/e^(q T)   (3.3)



Podemos substituir, na Equação 3.3, a taxa de juros e o cupom cambial, ambas na forma discreta, para obtermos uma fórmula simples de formação de preços entre o dólar futuro e o à vista:



F = S ₀ (1 + i)^(n _u/2 5 2)/(1 + c c n _c/3 6 0)   (3.4)



Sendo:

i: taxa de juros exponencial na base 252 dias úteis

cc: cupom cambial linear na base 360 dias corridos

n_u: dias úteis n_c: dias corridos

---

Podemos isolar o dólar à vista na Equação 3.5:



S ₀ = F (1 + c c n _c/3 6 0)/(1 + i)^(n _o/2 5 2) tag {3.5}



E substituir o dólar à vista para os cálculos dos pontos do casado de dólar, assim teremos:



D ₀ = F [ 1 - (1 + c c n _c/3 6 0)/(1 + i)^(n _o/2 5 2) ] tag {3.6}



Com base na Equação 3.6, podemos determinar a diferença, em termos de pontos, entre o primeiro vencimento de contrato futuro de dólar e o dólar à vista, mesmo não havendo negócios à vista de dólar. Com relação ao mercado de dólar, podemos acrescentar ainda as seguintes premissas: ■ O contrato futuro de dólar é mais líquido do que o dólar à vista, e é negociado ao longo do dia, durante o pregão de bolsa.

■ O mercado de futuro de dólar é referência para formação de preços do dólar à vista, e não o contrário. Quando uma instituição realiza cotação de dólar à vista, estará utilizando o futuro como referência.

## Exemplo 3.2 - Cálculo de pontos de dólar casado

Sabendo que o futuro de dólar está cotado a 3.150, a taxa pré-fixada livre de risco está a 8,10% a.a.o. para um período de 19 dias úteis e o cupom cambial está cotado em 2,30% a.a., para 28 dias corridos. Quais são os pontos de diferença entre o dólar futuro e o dólar à vista, sabendo que o dólar à vista liquida em D+2, em dois dias úteis e quatro dias corridos?

---

Em uma operação de câmbio, é conveniente lembrar que haverá liquidação em reais e liquidação em dólares. Os reais são liquidados no Brasil, em reserva bancária, que dependerá da agenda de feriados nacionais, enquanto que os dólares serão liquidados por Nova Iorque, logo, os feriados desta cidade serão levados em consideração.

Podemos entender a liquidação dos dois instrumentos do casado, futuro e dólar à vista, com base na Figura 3.1:

Figura 3.1 | Exemplo de liquidação do casado de dólar
![img-11.jpeg](img-11.jpeg)
Fonte: Elaborada pelos autores.

O dólar à vista liquida em dois dias úteis e quatro dias corridos, enquanto que o vencimento do contrato futuro de dólar ocorre em 19 dias úteis e 28 dias corridos. Consequentemente, a diferença de prazo entre a liquidação de cada um dos instrumentos é de 17 dias úteis e 24 dias corridos.

Agora, podemos calcular os pontos de diferença do casado de dólar:



D ₀ = 3.150 [ 1 - (1 + 0,0230, 24/360)/(1 + 0,0810)^(17/262) ] = 11,70



Os resultados dos cálculos indicam uma diferença de 11,7 pontos entre o futuro de dólar e o dólar à vista. Sabendo que o futuro de dólar está cotado a 3.150, o spot deverá ser cotado, em condição de não arbitragem, a 3.138,30 pontos. Ao longo do pregão, esse cálculo é refeito sempre que se desejar cotar o dólar à vista.

---

Forward points

A bolsa permite a negociação de Forward Points (FRP), que são os pontos de diferença entre o primeiro vencimento (vencimento base) de futuro de dólar e o PTAX (dólar oficial do BACEN) do dia.

A operação consiste na compra e venda de pontos entre o PTAX do dia e dólar futuro. Quando negociamos pontos de FRP – compra ou venda de pontos – a bolsa registra ao final do pregão uma operação de igual posição no futuro de dólar, cujo preço de negociação será igual ao PTAX do dia, multiplicado por 1.000, a este são somados os pontos negociados no FRP.

Exemplo 3.3 - FRP

Vamos supor que o PTAX de fechamento do dia foi divulgado às 14h, cotado a R$ 3,137 por dólar. No mesmo dia, às 11h, havíamos comprado 20 instrumentos de FRP a 12 pontos cada um. Ao final do pregão, somaremos os pontos ao PTAX divulgado e teremos uma posição resultante de 20 contratos futuros de dólar, ao preço de operação de 3.137 +12 = 3.149 pontos cada um. O ajuste do resultado da operação com FRP é feito no futuro de dólar.

Em operações de day trade com FRP, por exemplo, não haverá posição em aberto no futuro de dólar ao final do dia. Porém, haverá ajuste financeiro de cada uma das operações registradas no FRP durante o pregão, por meio do futuro de dólar.

3.4 Contrato futuro de Índice BOVESPA

O contrato futuro de Índice BOVESPA tem como ativo-objeto a carteira teórica de ações divulgadas pela bolsa, que serve como referência para o

---

mercado de ações.

Assim como o contrato futuro de dólar, o futuro de IBOVESPA – ou simplesmente futuro de índice – possui liquidez concentrada no primeiro vencimento.

O vencimento do futuro de IBOVESPA é distinto aos demais ativos financeiros. Enquanto que o vencimento dos outros contratos futuros ocorre sempre no primeiro dia útil do mês, o vencimento do futuro de índice ocorre sempre na quarta-feira mais próxima do dia 15 dos meses pares.

Existe uma lógica nesse tipo de vencimento, quando nos lembramos das operações realizadas no antigo pregão viva-voz. As duas maiores rodas de negociação do pregão na BM&FBOVESPA eram o futuro de dólar e de índice. Quando ocorria o vencimento de contratos futuros, os operadores de pregão tinham uma tarefa intensa para rolar as posições no viva-voz, considerando a disputa entre comprados e vendidos.

Não seria razoável que as duas maiores rodas tivessem vencimento na mesma data, logo, era coerente que o futuro de índice tivesse vencimento no meio do mês, enquanto que o dólar tivesse vencimento no início do mês. Essa mesma agenda de vencimentos foi herdada pelo atual sistema eletrônico de negociação.

O contrato futuro de IBOVESPA é operado em pontos do índice, sendo que o contrato padrão é negociado a um real por ponto, em lotes de cinco contratos.

A fórmula para o cálculo do ajuste diário das operações realizadas no futuro de índice é a seguinte:



AJ = (PA - PO)N \ (3.7)



Sendo:

- AJ: valor do ajuste diário
- PA: preço de ajuste, divulgado diariamente pela bolsa, em pontos do Índice BOVESPA PO: preço da operação em pontos do índice
- N: número de contratos

---

Exemplo 3.4 - Ajuste de operação com futuro de Índice BOVESPA

A Tabela 3.4 apresenta um exemplo de duas operações com futuro de índice realizadas em um mesmo dia.

Tabela 3.4 | Exemplo de operação com futuro de IBOVESPA

|  Operação | Posição | Quantidade | Contrato | Vencto | Preço da operação | Preço de ajuste  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | Comprada | 200 | Fut. de IND | V17 | 76.525 | 76.808  |
|  2 | Vendida | 100 | Fut. de IND | V17 | 77.570 | 76.808  |

Fonte: Elaborada pelos autores.

O comitente ficou com posição em aberto comprada em 100 contratos de IBOVESPA. O preço da posição em aberto é o preço de ajuste de 76.808.

A posição em aberto será carregada para o dia seguinte e será ajustada juntamente com as demais operações que o comitente porventura venha a realizar no dia seguinte.

Agora, calcularemos o valor do ajuste diário da operação 1, que foi uma compra de 200 contratos futuros ao preço de 76.525, logo, o valor do ajuste diário será:



AJ = (76.808 - 76.525) (+200) = 56.600



Na operação 1, iremos receber um valor positivo de ajuste de R$ 56.600,00, enquanto que na operação 2 o valor de ajuste será:



AJ = (76.808 - 77.570) (-100) = 76.200



Na operação 2, iremos receber um valor positivo de ajuste de R$ 76.200,00. Logo, o ajuste diário total será a soma dos ajustes das operações realizadas no dia, adicionando-se a isso as operações em aberto do dia anterior:



AJ_(total) = 56.600 + 76.200 = 132.800



O ajuste diário total será positivo em R$ 132.800,00, cuja liquidação financeira ocorrerá em D+1.

---

# 3.4.1 Minicontrato de IBOVESPA

Assim como o mini de dólar, o mini de IBOVESPA foi inicialmente dimensionado para as operações com pessoa física. O tamanho do mini de índice é R$ 0,20 para cada ponto do Índice BOVESPA. Logo, cada cinco contratos mini de índice equivalem a um contrato padrão, podendo, também, serem negociados em lotes unitários.

Atualmente, os minicontratos de IBOVESPA possuem mais liquidez do que o contrato padrão, tanto em números de negócios quanto em valor nocional total.

Os preços de ajuste divulgados pela bolsa são rigorosamente os mesmos para os contratos mini e padrão.

# 3.4.2 Rolagem de IBOVESPA e IR1

Próximo ao vencimento do contrato, se o comitente desejar manter uma posição vendida, por exemplo, deverá realizar a rolagem dos seus contratos. Para isso deverá comprar a posição no primeiro vencimento e simultaneamente vendê-la no segundo vencimento.

Se o comitente assim não o fizer, no vencimento do contrato a posição se encerra, fazendo o último ajuste com base no IBOVESPA do dia.

O IR1 é um instrumento utilizado para a rolagem automática do contrato futuro de Índice BOVESPA padrão. Por exemplo, se tivermos uma posição vendida em 20 contratos futuros de índice e quisermos rolar para o próximo vencimento, precisamos apenas vender 20 unidades de IR1. Nesse caso, a bolsa irá registrar uma compra de 20 contratos do primeiro vencimento e uma simultânea venda de 20 contratos no segundo vencimento.

Mas como ficam os preços dos contratos negociados? Suponha que a venda do IR1 seja feita por 800 pontos, e o primeiro vencimento de futuro de

---

IBOV seja negociado a 75.190 pontos, o preço registrado de venda do segundo vencimento será de 75.190 + 800 = 75.990 pontos do Índice BOVESPA.

## 3.4.3 Beta hedge

Se montarmos uma carteira composta por todas as ações da carteira teórica do IBOVESPA, na mesma proporção, e vendermos futuro de Índice BOVESPA, em mesmo valor financeiro, qual seria o resultado dessa carteira?

O resultado dessa carteira seria uma taxa de juros pouco inferior à taxa pré-fixada livre de risco, ou a taxa do futuro de DI, mesmo assim seria uma remuneração em torno de 85\% a 90\% dessa taxa pré-fixada.

Essa taxa um pouco menor ocorre por conta do custo de carregamento das ações, representado pelo aluguel das ações por meio do BTC. A Equação 3.8 de arbitragem representa essa relação:



F = Pi₀ e^((r - q) T) tag {3.8}



Sendo:

- F: cotação do contrato futuro de Índice BOVESPA
- Pi_0: carteira de ações representativas do IBOVESPA
- r: taxa livre de risco pré-fixada na forma contínua
- q: custo de carregamento, com base no custo de aluguel das ações, na forma contínua T: tempo até vencimento do contrato futuro

Vamos imaginar uma situação distinta: usaremos uma carteira de ações que supere os retornos do IBOVESPA e hedgear essa carteira com futuro de índice.

---

Suponha que tenhamos à nossa disposição uma equipe de analistas de ações, que consiga selecionar uma carteira composta por empresas, cujas ações obtenham retornos que superem o resultado do IBOVESPA, como podemos montar uma estratégia utilizando contratos futuros?

Vamos partir da premissa que a venda de futuro de índice permita eliminar o risco sistemático das carteiras de ações, ou seja, o risco bolsa das ações. O resultado remanescente de uma carteira *hedgeada* como essa é um retorno próximo ao do ativo livre de risco, menos o custo de carregamento, acrescentando um prêmio adicional, que definiremos como alfa de Jensen (1968).

O alfa de Jensen, conforme mencionado, é o retorno incremental da carteira de ações do retorno ajustado pelo seu risco sistemático, é o que denominamos como risco individual do portfólio de ações. O alfa de Jensen pode ser calculado da seguinte forma:



alpha_J = R̄_Π - [ r + β (R̄_M - r) ] 



Sendo:

R̄_Π: média dos retornos da carteira de ações r: taxa livre de risco histórica

R̄_M: retorno médio do mercado, representado pelo IBOVESPA β: beta da carteira de ações

Se o alfa for positivo, a carteira *hedgeada* de ações terá um retorno acima da taxa livre de risco.

Essa carteira de ações em questão não pode ser muito diversificada, pois não poderemos eliminar totalmente o risco individual ou diversificável. Na prática, isso equivale dizer que essa carteira de ações deverá ter em torno de dez empresas para ser vitoriosa em sua estratégia. Se aumentar muito o número de empresas, haverá uma diversificação do risco individual e será difícil superar o IBOVESPA.

Para proteger contra o risco sistemático, teremos de realizar o beta *hedge*.

---

Para realizar o beta hedge, precisaremos vender contratos futuros de índice em quantidade que seja suficiente para neutralizar o beta.

Podemos determinar a quantidade de futuros de Índice BOVESPA, conforme a Equação 3.10:



Q_(IND) = - (β - β^(prime)) P_(11)/P_(IND)   (3.10)



Sendo:

- Q_(IND): quantidade de contratos de Índice BOVESPA necessários para o beta hedge β: beta da carteira de ações
- β^(prime): beta alvo (quando se quer eliminar o risco sistemático, o beta alvo é geralmente igual a zero) P_(II): valor a mercado da carteira de ações
- P_(IND): cotação do futuro de Índice BOVESPA

Utilizamos o beta alvo citado, porque podemos ter o intuito apenas de reduzir o risco sistemático, e não o neutralizar, nesse caso β^(prime) < β. Em alguns casos, pode-se ter o intuito de aumentar o risco do beta e alavancar os ganhos, nesse caso β^(prime) > β.

Quando se realiza o beta hedge, haverá um risco de base diário. Isso ocorre porque o preço de ajuste dos contratos futuros e o fechamento do mercado de ações ocorrem em horários diferentes. Essa discrepância de horários provoca um descasamento de preços de fechamento, que se regula durante o pregão no dia seguinte. Esse descasamento deve ser levado em consideração, principalmente por gestores de fundos, pois o valor da carteira é calculado com base nos preços de fechamento. Grande parte da volatilidade será causada pelo risco de base, mas não afetará o resultado do portfólio, porque esse

será sempre negociado durante o pregão, quando os preços voltam ao equilíbrio.

Além disso, haverá uma volatilidade adicional causada pelo risco individual do portfólio de ações. A partir do momento que temos uma carteira, cuja

---

composição é diferente da carteira teórica do IBOVESPA, haverá natural movimentação de preços em discrepância com o contrato futuro de índice.

# 3.4.4 Breve discussão sobre o beta

Podemos discutir diversas maneiras para calcular o beta ideal de uma carteira de ações e o cálculo da quantidade de contratos para o beta hedge. O nosso intuito é fazer breves comentários sobre as dificuldades encontradas na utilização desse indicador de risco sistemático.

O beta de uma ação, em relação ao IBOVESPA, é o coeficiente angular de uma regressão linear MQO (Mínimos Quadrados Ordinários) dos retornos contínuos dessa ação em relação aos retornos do IBOVESPA, obtido dentro de um intervalo amostral. Essa é a forma mais simplista de se obter o beta de uma ação. A regressão linear é ilustrada graficamente pela Figura 3.2, cujo eixo horizontal representa os retornos do IBOV e o eixo vertical indica os retornos de uma carteira hipotética de ações:

Figura 3.2 | Exemplo de retornos de uma carteira de ações e IBOVESPA
![img-12.jpeg](img-12.jpeg)
Fonte: Elaborada pelos autores.

---

O coeficiente angular, no caso o beta, pode ser calculado da seguinte forma:



β = c o v (R _Π , R _M)/v a r (R _M) tag {3.11}



Sendo:

R_Π: retorno histórico da carteira de ações

R_M: retorno do mercado, nesse caso, representado pelo IBOVESPA

Algumas premissas devem ser levadas em consideração quando calculamos o beta:

- A janela amostral que será utilizada na regressão. Devemos lembrar que o beta de uma empresa pode mudar a cada publicação de balanço, pois podem alterar os índices financeiro e de alavancagem operacional. O problema da janela amostral pode ser resolvido com a utilização de um fator de decaimento exponencial EWMA para o cálculo do beta. Discuteremos o EWMA mais adiante, neste momento basta saber que é uma técnica que permite dar maior peso às observações mais recentes. Geralmente, usamos um fator de decaimento entre 0,94 e 0,98, que permite uma amostra representativa de um ano de retornos.

- O erro-padrão, o teste de significância estatística do coeficiente angular e dos resíduos da regressão.

- Empresas com problemas de liquidez, cujos preços não oscilam de acordo com o mercado. Em alguns casos, quando há falta de liquidez ou quando a empresa é uma small cap, e sua inclusão não é impeditiva para a montagem da carteira, podemos usar uma variável dummy na regressão do beta dessa empresa, obtendo um beta de alta e um beta de baixa. Utilizaremos um beta diferente (um pouco maior) para empresas menores, devido ao risco adicional pela falta de liquidez quando o mercado está em baixa.

---

O beta de uma carteira de ações também pode ser obtido por meio do beta individual de cada empresa, ponderado pela participação de cada uma das ações que compõem a carteira, conforme a Equação 3.12:



β = Σ(j=1 até n) w_j beta_j   (3.12)



Sendo:

- β: beta da carteira de ações
- w_j: peso da ação na carteira
- beta_j: beta da j-ésima ação da carteira
- n: número de ações que compõem a carteira

## Exemplo 3.5 - Beta hedge

Vamos supor que temos uma carteira de ações no valor de R$ 23,5 milhões, cujo beta é 1,17. O próximo vencimento de futuro de Índice BOVESPA está cotado a 75.210 pontos. Se quisermos neutralizar o risco sistemático, quantos contratos futuro de IBOV deveríamos vender para tentar eliminar o risco sistemático da carteira? E a quantidade de minicontratos?

Para resolver esse problema, vamos inicialmente calcular a quantidade de contratos padrão, considerando um beta-alvo igual a zero:



Q_(IND) = -(1,17) 23.500.000/75.210 = -365,58



Arredondando a quantidade de contratos para múltiplos de cinco, seria necessário vender 365 contratos padrão de futuro de IBOVESPA para neutralizar o beta da carteira de ações em questão. Ou seriam necessários 1.828 minicontratos de índice para fazer o mesmo beta hedge.

Utilizando o mesmo exemplo, quantos contratos seriam necessários para se obter um beta-alvo de 0,5? Usando a mesma equação, obteremos a quantidade de contratos:



Q_(IND) = -(1,17 - 0,5) 23.500.000/75.210 = -209,35



---

Logo, seria necessária a venda de 210 contratos padrão ou 1.047 minicontratos de índice para obter o beta-alvo de 0,5.

# 3.5 Contrato futuro de DI

O futuro de DI é o contrato futuro de taxas de juros, especificamente a taxa média de depósitos interfinanceiros (DI) de um dia. O objeto de negociação é a compra e a venda de taxas de juros. O valor de face desse contrato é de R$ 100.000, cujo preço unitário (PU) é calculado descontando-se o valor de face pela taxa negociada.

Nesse contrato, a negociação é feita em taxa, porém, o ajuste diário é calculado pelo PU.

> Quando compramos contrato futuro de DI, estamos comprados em taxa de juros.

Qual a utilidade do contrato futuro de DI para o mercado financeiro?

Imagine que um banco de montadora realiza financiamento de veículos, que geralmente possui prazos relativamente longos, por taxas pré-fixadas. Este banco, portanto, será possuidor de uma carteira de recebíveis pré-fixados. O que ocorrerá com o valor presente dessa carteira de recebíveis se a taxa de juros de mercado aumentar? Haverá uma perda de valor dessa carteira.

Se a taxa de juros de longo prazo subir, consequentemente, o banco perderá dinheiro, estará vendido em taxas de juros. E o que deverá fazer para se hedgear no mercado futuro de DI? Comprar taxa de juros, de forma que, toda a perda ocorrida na carteira de recebíveis, por conta do aumento na taxa de juros, será compensado por um ganho, em mesmo montante, no contrato futuro de DI.

# Compreendendo o futuro de DI

---

O futuro de dólar e o futuro de índice são mais fáceis de entender do que o contrato futuro de taxa de juros, pois o conceito de compra e venda de taxa de juros é menos intuitivo. A Figura 3.3 representa uma operação no contrato futuro de DI:

Figura 3.3 | Contrato futuro de DI
![img-13.jpeg](img-13.jpeg)
Fonte: Elaborada pelos autores.

No exemplo anterior, fizemos uma operação com futuro de DI, cuja taxa negociada é 7,80% na base ano over exponencial 252 dias úteis, o prazo, nesse exemplo, é de 340 dias úteis. À medida que a taxa sobe, tudo o mais constante, o PU irá cair.

Quando estamos comprados em taxa de juros, estamos simultaneamente vendidos no PU, e vice-versa. Isso ocorre, porque quando a taxa sobe, o PU diminui.

Vamos imaginar o seguinte exemplo: se comprarmos taxa a 7,80% a.a.o., e a taxa subir, no mesmo dia, para 8,00% a.a.o., iremos ganhar ou perder dinheiro?

Você deve pensar na taxa de juros como o preço de uma mercadoria, se compramos uma mercadoria por R$ 7,80 e, no mesmo dia, o preço aumentar para R$ 8,00, ganharemos dinheiro. Com a taxa de juros é a mesma interpretação. Se comprarmos taxa a 7,80 % a.a.o. e agora está valendo 8% a.a.o., ganharemos dinheiro também. Porém, o valor financeiro desse ganho será calculado com base no PU.

---

A seguir, na Tabela 3.5, observaremos as operações no mercado futuro de DI ocorridas durante um dia de prego em bolsa:

Tabela 3.5 | Volume negociado de futuro de DI

|  Veneto | Contr. Abert. | Contr. Fech. | Núm. Negoc. | Contr. Negoc. | Vol.  |
| --- | --- | --- | --- | --- | --- |
|  X17 | 544.298 | 551.398 | 23 | 19.720 | 1.961.821.515  |
|  Z17 | 379.080 | 379.095 | 6 | 260 | 25.719.821  |
|  F18 | 4.965.357 | 4.856.437 | 1.333 | 106.335 | 10.462.204.003  |
|  G18 | 81.865 | 81.865 | 19 | 2.540 | 248.449.786  |

Fonte: B3.

Os contratos futuros de DI, diferentemente do dólar e IBOVESPA, possuem liquidez nos vencimentos mais longos, a bolsa abre muitas séries de vencimentos, superiores a 10 anos de maturidade. Os vencimentos mais negociados são as "cabeças" de trimestre: janeiro, abril, julho e outubro. Porém, os verdadeiros pilares da curva de juros, por possuírem maior liquidez, são as "cabeças" de ano, os vencimentos de janeiro, começados pela letra F, como o F18, vencimento em janeiro de 2018, que está na coluna esquerda da tabela.

O ajuste diário do contrato futuro de DI, como mencionado anteriormente, é realizado por meio do PU. A fórmula de ajuste das operações com o DI é apresentada a seguir: AJ = (PA - PO)N (3.13) Sendo:

AJ: valor do ajuste diário

PA: PU de ajuste, divulgado diariamente pela bolsa

PU: PU da operação, calculado com base na taxa negociada

N: número de contratos, com sinal inverso à quantidade negociada

O número de contratos na equação de ajuste levará sinal inverso ao da posição negociada, isso acontece porque a negociação ocorre em taxa, porém, o ajuste é calculado em PU.

---

Por exemplo, ao comprarmos 300 contratos futuros de DI, estaremos comprados em taxa. Logo, a quantidade de contratos considerada no ajuste diário será N = -300.

Na Tabela 3.6 estão os preços de negociação e ajuste dos contratos futuros de DI publicados pela bolsa.

Tabela 3.6 | Ajustes do contrato futuro de DI

|  Veneto | Ajuste anter. | Ajuste corrig. | Preço abert. | Preço mín. | Preço máx. | Preço méd. | Últ. Preço | Ajuste  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  X17 | 99.483,98 | 99.514,73 | 7,972 | 7,972 | 7,98 | 7,973 | 7,973 | 99.483,84  |
|  Z17 | 98.921,13 | 98.951,94 | 7,653 | 7,653 | 7,661 | 7,658 | 7,66 | 98.921,22  |
|  F18 | 98.388,22 | 98.420,46 | 7,45 | 7,44 | 7,455 | 7,444 | 7,44 | 98.389,91  |
|  G18 | 97.812,63 | 97.847,20 | 7,315 | 7,295 | 7,315 | 7,302 | 7,3 | 97.816,83  |

Fonte: B3.

Na última coluna da direita estão os preços de ajuste divulgados diariamente pela bolsa. Note que o preço de ajuste está apresentado em PU, e são utilizados para o cálculo de ajuste diário, para as operações realizadas no dia e para as posições carregadas em aberto do dia anterior.

Na segunda coluna da esquerda, estão PUs de ajuste do fechamento do dia anterior, na terceira coluna estão os PUs corrigidos. A bolsa acrescenta um dia de CDI sobre os PUs de ajuste do dia anterior para calcular os ajustes das posições em aberto carregadas de um dia para o outro.

# 3.6 Ajuste de operação no contrato futuro de DI

Vamos fazer um exemplo de ajuste de duas operações realizadas com futuro de DI, com vencimento em janeiro de 2023, sendo uma comprada e uma vendida em contrato futuro, da seguinte forma:

---

Tabela 3.7 | Exemplo de operação com futuro de DI

|  Operação | Posição | Quantidade | Contrato | Vencimento | Preço da operação | Prazo até vencimento em dias úteis | Preço de ajuste  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  1 | Comprada | 1.000 | Fut. de DI | F23 | 9,61 | 1321 | 61.754,73  |
|  2 | Vendida | 800 | Fut. de DI | F23 | 9,74 | 1321 | 61.754,73  |

Fonte: Elaborada pelos autores.

Utilizando as informações da Tabela 3.7 podemos determinar que a posição está em aberto. Se o participante comprou 1.000 e vendeu 800 contratos, logo, ao fim do pregão, a posição em aberto ficou comprada em taxa de 200 contratos futuros DI.

Uma operação foi comprada em taxa de 9,61% a.a.o., enquanto que a outra ficou vendida em taxa de 9,74% a.a.o.

O primeiro passo será calcular o PU da operação, para depois calcularmos os ajustes das operações. O preço da operação 1 é calculado descontando-se o valor de face pela taxa negociada:



PO_1 = 100.000/(1 + 0,0961)^(1321/252) = 61.816,28



O PU da operação 1 é 61.816,28 e o PU da operação 2 é calculado da seguinte maneira:



PO_2 = 100.000/(1 + 0,0974)^(1321/252) = 61.433,37



Agora, vamos calcular o valor do ajuste diário da operação 1, que foi uma compra de 1.000 contratos futuros à taxa de 9,61% a.a.o., logo, o valor do ajuste diário será:



AJ = (67.754,73 - 61.816,28) (-1.000) = 61.550



---

Na operação 1, receberemos um valor positivo de ajuste de R$ 61.550,00, e na operação 2 o valor de ajuste será:



AJ = (67.754,73 - 61.433,37) (+800) = 257.088



Na operação 2, receberemos um valor positivo de ajuste de R$ 257.088,00. Logo, o ajuste diário total será a soma dos ajustes de todas as operações realizadas no dia, adicionando-se a isso as operações em aberto do dia anterior:



AJ_(total) = 61.550 + 257.088 = 318.638



O ajuste diário total será positivo em R$ 318.638,00, cuja liquidação financeira ocorrerá em D+1 e estará disponível na conta corretora.

## 3.6.1 Hedge de renda fixa usando o futuro de DI

Suponha que possuímos uma carteira de títulos públicos pré-fixados e queremos eliminar o risco de taxas de juros, utilizando o contrato futuro de DI.

Primeiro, devemos definir o conceito de risco de taxa de juros. Sabemos que existe uma oscilação na curva de juros e que os valores presentes dos títulos caem quando a taxa de juros aumenta.

A curva de juros, formada por meio dos contratos futuros de DI, pode ser entendida como as taxas de juros projetadas no futuro, considerando as premissas de não arbitragem entre os mercados. É uma expectativa da trajetória das taxas de juros. É o que denominamos como estrutura temporal de taxa de juros (ETTJ). A Figura 3.4 mostra a curva de juros ou ETTJ, obtida por meio das taxas dos contratos futuros de DI:

---

Figura 3.4 | Exemplo de estrutura temporal de taxas de juros
![img-14.jpeg](img-14.jpeg)
Fonte: Elaborada pelos autores.

O hedge de taxa pré-fixada, utilizando os contratos futuros de DI, procura proteger o valor presente das carteiras pré-fixadas contra os movimentos na curva de juros.

# O risco de renda fixa

Vamos observar novamente o exemplo de contrato futuro de DI visto anteriormente e replicado na Figura 3.5:

Figura 3.5 | Contrato futuro de DI
![img-15.jpeg](img-15.jpeg)

---

Fonte: Elaborada pelos autores.

Utilizando o exemplo anterior, vamos imaginar que houve uma mudança no patamar da taxa de juros. Vamos supor que houve um aumento de 1% (um ponto percentual), de 7,80% a.a.o. para 8,80% a.a.o. Com o aumento na taxa de juros, o valor presente do PU cairá para 89.244,21, provocando uma variação negativa (perda) no valor presente de R$ 1.118,77.

Sabemos que quando a taxa de juros sobe, o valor presente diminui. Essa relação pode ser representada pela figura a seguir:

Figura 3.6 | Relação do valor presente e taxa de juros
![img-16.jpeg](img-16.jpeg)
Fonte: Elaborada pelos autores.

Na Figura 3.6, quando a taxa de juros aumenta de i_1 para i_2, haverá, como consequência, uma redução do valor presente de P_1 para P_2. Podemos tentar quantificar essa variação do valor presente, dada uma variação na taxa de juros, pela primeira derivada parcial do valor presente em relação à taxa, representada, na Figura 3.6, pela reta tangente.

A primeira derivada é uma aproximação linear de uma variação que é resultante de uma função exponencial. Logo, haverá um erro nessa aproximação, representado na figura pela letra "e".

---

A equação genérica de desconto a valor presente, para taxas de juros discretas e exponenciais, é representada pela seguinte equação:



P = F (1 + i)^(- T) (3.14)



Sendo:

- P: valor presente do título de renda fixa
- F: valor de face ou valor futuro
- i: taxas de juros discreta, pré-fixada e exponencial T: tempo até o vencimento do título

O que queremos identificar é a relação, dada pela primeira derivada parcial do valor presente do título, em relação à taxa de juros. O objetivo final é o de obter uma medida de risco de taxa pré-fixada, que associe as variações nas taxas de juros com as possíveis oscilações de valor presente dos títulos de renda fixa.

A primeira derivada do valor presente em relação à taxa de juros, partindo da equação genérica de desconto a valor presente, pode ser escrita da seguinte forma:



∂ P/∂ i = - T F (1 + i)^(- T - 1)   (3.15)



Que, alternativamente, pode ser escrita deste modo:



∂ P/∂ i = - T/(1 + i) F/(1 + i) ^T   (3.16)



Vamos partir da premissa que a *duration* de um título, que possui apenas um fluxo de caixa, é igual ao prazo T até o vencimento. Vamos também assumir que a *duration* modificada (DM) é igual a T / (1 + i).

Podemos reescrever a equação anterior assumindo que a variação da taxa de juros é infinitesimalmente pequena, com i → 0, da seguinte forma:

---



Δ P/Δ i = - D ^* F/(1 + i) ^T   (3.17)



Sendo:

D^*: duration modificada

Sabendo que F / (1 + i)^T é igual ao valor presente P, teremos que a variação no valor presente será dada pela DM, multiplicada pelo valor presente do título e pela variação esperada na taxa de juros, conforme a seguinte equação:



Δ P = - D ^* (P) Δ i   (3.18)



Partindo da Equação 3.18, calcularemos a variação do valor presente, com base no exemplo inicial do nosso contrato futuro de DI. Sabendo que o prazo até vencimento no contrato é de 340 dias úteis, podemos obter a duration em anos:



D = 340/252 = 1,3492



O contrato tem um prazo de 1,3492 ano até vencimento, vamos obter agora a duration modificada:



D ^* = 1,3492/(1 + 0,0780) = 1,2516



A duration modificada resultante foi de 1,2516.

O que significa uma duration modificada de 1,2516? Significa que, se a taxa de juros aumentar em um ponto percentual (1% a.a.o.), o valor presente do título vai cair aproximadamente 1,2516%.

---

Agora, calcularemos a variação no valor presente, partindo da *duration* modificada calculada, do PU de R$ 90.362,98, para uma variação de 1% a.a.o. na taxa de juros:



Δ P = -1,2526(90.362,98)0,01 = -1.130,98



A variação obtida pela primeira derivada parcial foi negativa em R$ 1.130,98, diferente do valor obtido pela variação discreta, que foi uma perda de -R$ 1.118,77. Isso ocorre porque houve um erro de aproximação, conforme mencionado anteriormente.

Podemos reduzir esse erro por meio da segunda derivada da equação do valor presente, que resultaria no seguinte:



∂^2 P/∂ t^2 = T(T+1)F(1+i)^(-T-2)   (3.19)



Alternativamente, podemos reescrever essa equação deste modo:



∂^2 P/∂ t^2 = T(T+1)/(1+i)^2 F/(1+i)^T   (3.20)



O componente T(T+1)/(1+i)^2 na equação é denominado como *convexidade*, que fornece a variação da *duration* modificada para uma dada variação na taxa de juros. A convexidade reduz o tamanho da DM quando a taxa de juros sobe, enquanto que aumenta o valor absoluto da DM quando a taxa de juros cai.

Quando a taxa de juros sobe, consequentemente, o valor presente do título cai, a convexidade reduz a queda. Alternativamente, quando a taxa de juros cai, o valor presente sobe, a convexidade faz subir mais. O efeito da convexidade é sempre

---

benéfico para o investidor em títulos de renda fixa, pois o faz perder menos e ganhar mais.

Agora, vamos calcular a convexidade para o exemplo com contrato futuro, utilizando a *duration* de 1,3492, teremos o seguinte:



C = 1,3492(1,3492 + 1)/(1 + 0,0780)^2 = 2,7275



O resultado da convexidade de 2,7275 significa que, se a taxa de juros subisse 1 ponto percentual, a *duration* modificada diminuiria em 0,027275, em termos absolutos.

Ou seja, a DM diminuiria de 1,2516 para aproximadamente 1,2243. Dessa maneira, a DM ficaria menor, logo, o valor presente do título ficaria menos sensível à variação da taxa de juros. Alternativamente, se a taxa de juros caísse 1 ponto percentual, a convexidade incrementaria o valor da DM para 1,2789, o que faria aumentar a sensibilidade do valor presente do título e, consequentemente, os ganhos do investidor em renda fixa.

Vamos adicionar a convexidade em uma expansão da série de Taylor, até a segunda derivada, para Δ i → 0, teremos:



Δ P = -D'(P)Δ i + 1/2C(P)Δ i^2   (3.21)



Sendo:

D^*: duration modificada C: convexidade

Vamos dar continuidade ao nosso exemplo com o futuro de DI, calculando agora a variação do valor presente, considerando a DM e a convexidade conjuntamente, teremos:



Δ = -1,2526(90.362,98)0,01 + 1/22,7275(90.362,98)(0,01)^2 = -1.118,66



---

Ao acrescentar a segunda derivada, conseguimos obter um resultado mais aproximado à variação discreta, ou seja, negativo em R$ 1.118,66.

De posse da DM e da convexidade, calcularemos medidas para fazer o hedge de renda fixa.

## O hedge de renda fixa

As medidas mais conhecidas para o hedge de renda fixa são: DV01 e DV10. Vamos entender o DV01 como uma medida da variação do valor presente do título (ou contrato futuro de DI) para uma variação de um ponto base na taxa de juros (0,01% a.a.o.), pode ser representado pela seguinte equação:



DV_(01) = D^*(P) 0,01/100   (3.22)



Geralmente, no DV01, não utilizamos o sinal negativo na equação da duration modificada, pois já é sabido que, quando a taxa de juros sobe, o valor presente do título diminui. Como a variação de 1 pb na taxa de juros é muito pequena, não há necessidade de usar a segunda derivada, ou seja, a convexidade. A tradução do DV01 é dollar value of 01, mas acabamos usando a mesma nomenclatura para títulos em reais.

O DV10 é muito parecido com o DV01, porém mede a variação do valor presente para uma variação de 10 pontos base na taxa de juros (0,10% a.a.o.). Geralmente, é mais adequado ao mercado brasileiro, devido as variações um pouco maiores nas taxas de juros comparado ao mercado americano de títulos. O DV10 é uma medida que pode ser calculada da seguinte forma:



DV_(10) = D^*(P) (0,10/100) - 1/2 C(P) (0,10/100)²   (3.23)



---

No DV10, é recomendável utilizar a segunda derivada, pois a variação é um pouco maior na taxa de juros, comparado ao DV01. A segunda derivada fornece maior precisão no resultado do DV10.

Para fazer o hedge de renda fixa, devemos neutralizar o DV01 ou o DV10 do portfólio, conforme a seguinte equação:



DV01_Π = Σ(j=1 até n) DV01_j Q_j   (3.24)  Sendo:



DV01_Π: DV01 alvo da carteira de títulos (se quisermos neutralizar o risco de renda fixa, o alvo deverá ser igual a zero) n: número de títulos e derivativos de renda fixa que compõem as carteiras DV01_j: DV01 do j-ésimo instrumento de renda fixa na carteira Q_j: quantidade do j-ésimo instrumento de renda fixa na carteira

Se formos fazer o hedge de renda fixa com o DV10, a equação possuirá uma estrutura similar:



DV10_Π = Σ(j=1 até n) DV10_j Q_j   (3.25)



Ao fazer o hedge de uma carteira de renda fixa, o prazo dessa carteira, medido por meio da duration de Macaulay, é relevante para a escolha do contrato futuro de DI adequado.

Se essa carteira a ser hedgeada for muito longa, recomenda-se fragmentar o hedge, dividindo essa carteira em tranches de um ano de duração e hedgeando cada tranche com os contratos futuros de DI de vencimento em janeiro de cada ano (código F).

## Exemplo 3.7 - Exemplo de hedge de taxa de juros pré-fixada

Vamos fazer o hedge de taxa pré-fixada de uma carteira de títulos públicos utilizando uma posição comprada na taxa em contratos futuros de DI.

Suponha que temos uma carteira de títulos públicos pré-fixados, que possua uma duration de 2,9365 anos, cujo valor presente, descontado a uma taxa de 9,35%

---

a.a.o. seja de R$ 24 milhões.

Vamos utilizar para fazer o hedge um contrato futuro de DI que vence daqui a exatamente 720 dias úteis e está sendo negociado à taxa de 9,20% a.a.o.

Vamos calcular o DV01 e o DV10 para a carteira de títulos e para o futuro de DI separadamente.

O primeiro passo será obter a duration modificada dos títulos públicos, da seguinte forma:



D^* = 2,9365/(1+0,0935) = 2,6854



O próximo passo será calcular a convexidade dos títulos:



C = 2,9365(2,9365+1)/(1+0,0935)^2 = 9,6672



Agora calculamos o DV01 dos títulos:



DV01 = 2,6854 (24.000.000) × 0,01 = 6.444,99



E, por fim, o DV10 dos títulos públicos:



DV10 = 2,6854(24.000.000) × 0,10 - 1/2 × 9,6672(24.000.000) × 0,10^2 = 64.333,92



Logo, nos títulos públicos pré-fixados, o DV01 será igual a R$ 6.444,99 e o DV10, igual a R$ 64.333,92.

Agora, repetiremos os mesmos passos para o contrato futuro de DI. Mas antes vamos calcular a duration simples:



D = 720/252 = 2,8571  anos



E o preço unitário do contrato futuro de DI, que sempre tem valor de face igual a R$ 100.000:

---



P = 100.000/(1 + 0,092)^(720/252) = 77.766,48



Calculamos a *duration* modificada:



D^* = 2,8571/(1 + 0,092) = 2,6164



E a convexidade:



C = 2,8571(2,8571 + 1)/(1 + 0,092)^2 = 9,2417



Calculamos o DV01 do contrato futuro de DI:



DV01 = 2,6164 (77.766,48) 0,01 = 20,3471



E, finalmente, o DV10:



DV10 = 2,6164(77.766,48)0,10 - 1/29,2417(77.766,48)0,10^2 = 203,1113



A Tabela 3.8 resume os resultados encontrados no contrato futuro de DI e na carteira de títulos públicos pré-fixados:

Tabela 3.8 | Resultados do exemplo de hedge de renda fixa

|   | Futuro de DI | Títulos públicos pré-fixados  |
| --- | --- | --- |
|  T | 2,8571 anos | 2,9365 anos  |
|  P | R$ 77.766,48 | R$ 24.000.000,00  |
|  i | 9,20% a.a.o. | 9,35% a.a.o.  |

---

|  DM | 2,6164 | 2,6854  |
| --- | --- | --- |
|  C | 9,2417 | 9,6672  |
|  DV01 | 20,35 | 6.444,99  |
|  DV10 | 203,11 | 64.333,92  |

Fonte: Elaborada pelos autores.

Para fazer o hedge de renda fixa, devemos comprar taxa por meio dos contratos futuros de DI de tal forma a neutralizar o DV01 ou o DV10. O objetivo é determinar a quantidade de contratos futuros de DI para fazer o hedge de taxa pré-fixada. Nesse exemplo, dado que a duration T do contrato futuro é similar a dos títulos, podemos simplesmente dividir o DV01 dos títulos pelo do contrato futuro, da seguinte forma:



Q_(DI) = 6.444,99/20,3471 = 316,753



Logo, teremos de comprar 317 contratos futuros de DI para neutralizar o risco de taxa de juros, resultado similar é obtido quando dividimos o DV10 dos títulos pelos dos contratos futuros:



Q_(DI) = 64.333,92/203,1113 = 316,7422



Apesar da pequena diferença do resultado final, chegamos aos mesmos 317 contratos de futuro de DI para o hedge de taxa pré-fixada.

Na verdade, a simplificação anterior é resultante da equação utilizada para o hedge, em que o somatório do DV01, multiplicado pela quantidade de cada instrumento, deve ser igual ao alvo, nesse caso, igual a zero, conforme o seguinte cálculo:  DV01_Π = -6.444,99 + 20,3471(316,753) = 0 

O DV01 dos títulos públicos pré-fixados fica com sinal negativo na equação porque estamos vendidos em taxa de juros. Isso ocorre porque quando a taxa de juros sobe, perdemos valor presente dos títulos.

# 3.7 Futuro de DDI

---

O futuro de DDI é um contrato de cupom cambial, com negociação muito similar ao futuro de DI. DDI significa Diferencial Dólar-DI. Neste contrato o valor de face é US$ 100.000 ajustado diariamente pelo preço unitário, descontado pelo cupom cambial negociado. Cada ponto do PU é equivalente a 50 centavos de dólar, dessa forma, o tamanho do contrato efetivo é 50% do seu valor de face, logo, US$ 50.000. O cupom cambial negociado é uma taxa linear na base 360 dias corridos.

A Figura 3.7 representa um contrato futuro de DDI.

Figura 3.7 | Contrato futuro de DDI
![img-17.jpeg](img-17.jpeg)
Fonte: Elaborada pelos autores.

Na Figura 3.7, o cupom cambial negociado é 2,90% a.a. que gerou um PU de 95.979,52, que seria equivalente a US$ 47.989,76 por contrato.

O ajuste do contrato futuro de DDI é feito da seguinte forma:



AJ = (PA - PO) M (TC_(t-1)) N 



Sendo:

- AJ: valor do ajuste diário
- PA: PU de ajuste, divulgado diariamente pela bolsa

---

PO: PU da operação, calculado com base no cupom cambial negociado

M: valor em dólar de cada ponto de PU, estabelecido pela bolsa, atualmente igual a US$ 0,50

TCt-1: dólar oficial do BACEN, PTAX800 do dia anterior N: número de contratos, com sinal inverso à quantidade negociada em taxa

Como o PU desse contrato está expresso em dólares, a bolsa precisa converter o resultado para reais, para isso, multiplica o resultado da operação pela taxa do oficial do dólar, PTAX do dia anterior. No início do pregão, o último PTAX disponível é sempre o do dia anterior. Contudo, o PTAX do dia anterior pode ser muito diferente do dólar à vista do dia da operação. Dessa maneira, haverá uma compensação no cupom cambial por essa diferença em relação ao PTAX.

No ajuste do DDI, recebe-se o resultado com a operação de cupom cambial mais a "sujeira" da variação cambial em decorrência do PTAX. Por isso esse contrato é denominado como cupom sujo e, atualmente, não possui muita liquidez.

O DDI surgiu em 1996, nesse período a variação cambial era pouco expressiva, dado que o regime cambial brasileiro à época era o de banda cambial, com intervenção intensa do Banco Central sobre o câmbio.

Em janeiro de 1999, o regime cambial mudou para flutuante, com menos intervenções do BACEN no câmbio, apenas contendo o excesso de volatilidade.

Com o aumento da volatilidade do dólar, as operações com DDI passaram a ficar menos interessantes, perdendo liquidez nas negociações, isso porque a sujeira do PTAX passou a ser relevante no resultado das operações. Em 2001, a bolsa lançou uma estratégia denominada de FRA de cupom ou cupom limpo.

# 3.8 FRA de cupom

---

O FRA de cupom ou FRC é uma estratégia na qual são negociados dois vencimentos de DDI, um vencimento mais longo, igual ao vencimento do FRC, e um vencimento mais curto, na verdade, o mais curto disponível.

Essa estratégia permite a limpeza do cupom e, consequentemente, a neutralização do efeito provocado pelo PTAX.

FRA (do inglês, Forward Rate Agreement) ou acordo de taxa a termo é um tipo de operação que foi bastante comum nas tesourarias dos bancos com outros contratos futuros, na época em que esse instrumento foi criado a bolsa apenas utilizou o nome da estratégia aplicada ao cupom cambial.

O FRA de cupom é uma taxa a termo de DDI. Quando se compra um FRC se está, na verdade, comprando um vencimento longo de DDI e vendendo um vencimento curto, em proporções diferentes, da seguinte forma:



[ + F R C ] = [ + D D I_(l o n g o) ; - D D I_(c u r t o) ] tag {3.27}



A Figura 3.8 representa a operação de FRC na bolsa e a posição resultante nos vencimentos de DDI:

Figura 3.8 | FRA de cupom
![img-18.jpeg](img-18.jpeg)
Fonte: Elaborada pelos autores.

Na figura anterior podemos notar que o FRC é uma taxa a termo, que começa no primeiro vencimento do DDI, na figura representado por DDI_1, e termina no vencimento longo de DDI, igual ao negociado no FRC, na figura representado por DDI_2.

Consideramos que o FRC é uma taxa a termo, logo, podemos representar essa taxa a termo da seguinte forma:

---



DV01_Π = Σ(j=1 até n) DV01_jQ_j   (3.28)



Adicionalmente a essa equação, introduziremos uma nova equação genérica, em condição de não arbitragem, na qual as taxas de contratos futuros são formadas:



(1 + DI) = (1 + DDI) D_f/PTAX   (3.29)



Sendo:

- DI: taxa de juros do DI ao período
- DDI: taxa de cupom cambial do DDI ao período
- D_f: cotação do dólar futuro de mesmo vencimento que o DDI e DI
- PTAX: dólar divulgado pelo BACEN em D-1

Como o DDI não possui liquidez, vamos isolá-lo na Equação 3.30:



(1 + DDI) = (1 + DI) PTAX/D_f   (3.30)



O próximo passo será substituir o DDI na equação do FRC 3.28, respeitando os prazos longo e curto da equação inicial, da seguinte forma:



(1 + FRC) = (1 + DI₂) PTAX/D_(f₁)/(1 + DI₁) PTAX/D_(f₁)   (3.31)



Sendo:

- DI₂ e DI₁: taxa de juros do DI ao período, com vencimento longo e curto, respectivamente D_(r2) e D_(r1): cotação do dólar futuro de vencimento longo e curto, iguais aos do DI

---

Com base na Equação 3.31, o PTAX desaparece, ou seja, o FRC "limpa" o efeito do PTAX no cupom cambial, resultando a seguinte equação:



(1 + FRC) = (1 + DI_2)D_(f_1)/(1 + DI_1)D_(f_2) 



A Equação 3.32 é uma relação em condição de não arbitragem das taxas a termo de juros, cupom cambial e variação cambial.

# 3.9 Dólar sintético e curva de dólar

Quando um banco faz uma cotação de termo de dólar para um cliente, onde o banco poderá obter uma referência para essa cotação, dado que o futuro de dólar possui liquidez apenas no primeiro vencimento em bolsa?

Ele pode obter essa referência nas cotações dos contratos de juros e cupom cambial em bolsa, com base na equação de não arbitragem a termo anteriormente apresentada. Pode-se determinar o valor de um vencimento longo de futuro de dólar, isolando-se esse vencimento na equação, denominado de dólar sintético, ou dólar futuro sintético:



D_(f_2) = (1 + DI_2)D_(f_1)/(1 + DI_1)(1 + FRC) 



## Exemplo 3.8 - Dólar sintético

Suponha que queremos calcular o dólar sintético, para, por exemplo, uma cotação de um termo de dólar, com vencimento em janeiro de 2021. Para isso, obtivemos as seguintes cotações dos contratos futuros negociados em bolsa, conforme a Tabela 3.9.

Tabela 3.9 | Cotações de contratos futuros

---

|  Vencimento | Data de vencimento | Futuro de DI | Futuro de dólar | FRC | Prazo em dias úteis | Prazo em dias corridos  |
| --- | --- | --- | --- | --- | --- | --- |
|  X17 | 1-nov.-2017 | 7,880 | 3.177,15 | - | 11 | 15  |
|  F18 | 2-jan.-2018 | 7,367 | - | 2,21 | 51 | 77  |
|  F19 | 2-jan.-2019 | 7,272 | - | 2,49 | 301 | 442  |
|  F20 | 2-jan.-2020 | 8,227 | - | 2,79 | 554 | 807  |
|  F21 | 4-jan.-2021 | 8,920 | - | 3,10 | 805 | 1.175  |

Fonte: Elaborada pelos autores.

Com base nas cotações dos contratos futuros, vamos calcular o dólar sintético com vencimento em janeiro de 2021, da seguinte forma:



D_(f_1) = (1 + 0,0892)^(805/252) (3.177,15)/(1 + 0,0788)^(11/252) {1 + [0,0310 (1.175 - 15)/360]} = 3.782,59



O dólar sintético calculado para janeiro de 2021 é de R$ 3,78259. É importante ressaltar que, nos cálculos, o FRC é uma taxa que começa no primeiro vencimento, por isso subtraímos os primeiros 15 dias corridos no cupom cambial do FRC.

Utilizando a mesma equação, é possível calcular uma curva de dólar, calculando-se o dólar sintético para todos os prazos, cujos resultados são apresentados na Tabela 3.10:

Tabela 3.10 | Curva de dólar

|  Vencimento | Data de vencimento | Futuro de DI | Futuro de dólar | FRC | Prazo em dias úteis | Prazo em dias corridos  |
| --- | --- | --- | --- | --- | --- | --- |
|  X17 | 1-nov.-2017 | 7,880 | 3.177,15 |  | 11 | 15  |
|  F18 | 2-jan.-2018 | 7,367 | 3.200,35 | 2,21 | 51 | 77  |
|  F19 | 2-jan.-2019 | 7,272 | 3.344,82 | 2,49 | 301 | 442  |
|  F20 | 2-jan.-2020 | 8,227 | 3.549,87 | 2,79 | 554 | 807  |
|  F21 | 4-jan.-2021 | 8,920 | 3.782,59 | 3,10 | 805 | 1.175  |

Fonte: Elaborada pelos autores.

---

Com a curva de dólar é possível precificar e cotar derivativos de balcão, desde swaps, termos, como também opções de dólar, que são precificadas pelo modelo desenvolvido por Black (1976), o qual veremos no decorrer deste livro.

## RESUMO

Neste capítulo, abordamos a estrutura operacional de negociação com contratos futuros, com ênfase em futuros sobre ativos financeiros. Foram explicados os contratos futuros de dólar, índice BOVESPA, cupom cambial e exemplos de ajustes diários com cada um dos contratos. Por fim, explicamos a formação de preços e projeção da curva de dólar.

## EXERCÍCIOS PROPOSTOS

1. Ajustes diários na B3 são:
a. Apuração do resultado financeiro das posições negociadas na B3
b. Chamadas de margem de garantias
c. Margens adicionais de garantia na CBLC
d. Apuração do resultado das posições com opções

2. Chamadas de margem na B3 são:
a. Solicitação de depósitos de garantia para as posições em aberto b. Ajustes financeiros das posições em aberto c. Solicitação de depósitos adicionais de garantia na CBLC
d. Ajustes financeiros das operações em D+1, inclusive day trade

3. O futuro de DI:
a. É um contrato negociado no balcão
b. Vence no valor de R$ 1.000,00
c. É o futuro de taxa de juros em reais, definida pela acumulação das taxas diárias do DI d. É o futuro de cupom cambial, em reais, definida pela acumulação das taxas diárias do DI

---

4. Com relação ao futuro de taxa de câmbio de dólar comercial (futuro de dólar) na B3: a. Não possui limites de oscilação diária máxima b. É composto por dois contratos de DI, um comprado curto e outro vendido longo c. A cotação é feita em dólares por R$ 1.000,00

d. O tamanho do contrato é de US$ 50.000,00

5. Os ativos aceitos como garantia na B3 para as operações com futuros são: a. Imóveis

b. American depositary receipts (ADR)

c. Quotas de empresas de capital fechado

d. Cartas de fiança

6. O dólar PTAX 800 está em R$ 3,16, e o dólar futuro que vence no próximo mês, em 15 dias úteis, está sendo negociado à cotação de R$ 3.140,00, com base nessas informações, a alternativa que melhor descreve o mercado neste momento é: a. O dólar futuro do primeiro vencimento sempre está abaixo do PTAX 800.

b. Há expectativa de queda para o dólar à vista (pronto) até o primeiro dia útil do próximo mês em relação a PTAX800.

c. Indica que o dólar pronto está acima do futuro de primeiro vencimento.

d. Indica que não há necessidade de se fazer hedge cambial neste momento.

e. O mercado está desequilibrado, com possibilidades de arbitragem.

7. As características do contrato de dólar futuro negociado na B3 são: a. Ajustados diariamente pela B3

b. Cotado pelo valor de R$ 1.000,00

c. O tamanho do contrato é de R$ 100.000,00 ou US$ 50.000,00, dos dois, o menor d. O vencimento é no segundo dia útil da primeira semana do mês e. Não exigem chamada de margem como nas operações a termo

8. Com relação às operações de day trade com futuros: a. O operador deve vender toda a sua posição no final do dia, mesmo que já esteja vendido b. Há necessidade de depósito de garantias, mesmo que a posição esteja zerada no final do dia c. Os ajustes são feitos apenas sobre a posição em aberto com liquidação financeira em D+0

d. Não há ajustes sobre a posição em aberto

e. O comprado liquida sua posição vendendo seus contratos

---

9. Referente à posição com futuros é correto dizer: a. Excluindo as operações de day trade, toda vez que estamos comprados no PU (preço unitário), estamos comprados na taxa e vice-versa.

b. Nos contratos de futuro de DI e DDI, toda vez que estamos comprados no PU (preço unitário), estamos vendidos na taxa e vice-versa.

c. Para ficar comprado na taxa de juros a termo é preciso comprar taxa curta e vender taxa longa.

d. Para ficar vendido na taxa de juros a termo é preciso vender taxa curta e comprar taxa longa.

e. Nenhuma das alternativas anteriores.

Com a seguinte curva de juros spot calculada com base nos ajustes dos contratos de DI futuro, responda as questões seguintes (veja as taxas no ano de 2002 - por curiosidade - qual era o cenário político-econômico na época?):

|  Vencimento | PU | Prazo em dias úteis | Taxa efetiva | Taxa a.a.o.  |
| --- | --- | --- | --- | --- |
|  Nov./2002 | 99,547.32 | 6 | 0.5% | 20.99%  |
|  Dec./2002 | 97,962.64 | 26 | 2.1% | 22.08%  |
|  Jan./2003 | 96,217.52 | 47 | 3.9% | 22.97%  |
|  Fe./2003 | 94,298.89 | 69 | 6.0% | 23.91%  |
|  Apr./2003 | 90,910.93 | 108 | 10.0% | 24.90%  |
|  Jul./2003 | 85,302.06 | 169 | 17.2% | 26.75%  |
|  Oc./2003 | 79,005.32 | 235 | 26.6% | 28.75%  |

10. Com a curva de juros spot calculada com base nos contratos de DI futuro, assinale a alternativa verdadeira: a. A curva de juros à vista está negativamente inclinada b. A curva de juros à vista não está inclinada

c. As taxas de prazos mais longos são menores que as taxas mais curtas d. A curva de juros à vista está positivamente inclinada

11. Se uma carteira estivesse comprada na taxa de 23,5% a.a.o. de 100 contratos de futuro de DI vencimento em abril/2003, com base nos preços de ajuste da tabela anterior, o ajuste financeiro desta carteira seria: a. R$ 59.872,64

b. R - 59.872,64

c. R$ 44.024,99

---

d. R - 44.024,99

e. R zero

12. Os pontos de diferença (forward points) entre o câmbio pronto D+2 (4 dias corridos) e o futuro de dólar devem ser, sabendo que o dólar futuro que vence em 18 du (23 dc) está cotado a 3.784 e que o futuro de DI e o cupom cambial (linha) estão cotados, respectivamente a: 7,50% a.a.o. e 3% a.a.: a. 11,37
b. 45,09
c. 27,76
d. 13,57
e. 13,30

13. O FRA de cupom:
a. É composto por dois vencimentos de contratos de DI, um curto e outro longo
b. É a taxa a termo de cupom cambial
c. Possui menos liquidez do que o contrato de DDI d. É composto por um contrato de DDI

14. Em relação ao FRA de cupom negociado na B3: a. É conhecido como cupom sujo, pois elimina o efeito do dólar PTAX 800
b. É composto por uma posição comprada em dois contratos de DDI, um curto e um longo c. É conhecido como cupom limpo
d. É uma taxa à vista de cupom cambial

Utilizando as seguintes taxas de ajuste de futuro de DDI (cupom cambial), com data de ref. 3 de dezembro de 2014, responda as seguintes questões:

|  Vencimento | PU de ajuste | Prazo em dias corridos  |
| --- | --- | --- |
|  Jan./2015 | 99.180,96 | 31  |
|  Fev./2015 | 99.027,88 | 60  |
|  Mar./2015 | 98.849,83 | 88  |
|  Abr./2015 | 98.640,33 | 119  |
|  Jul./2015 | 98.010,39 | 210  |
|  Out./2015 | 97.240,95 | 304  |

---

Jan./2016 96.495,47 395

15. A taxa anual de ajuste do contrato futuro de DDI com vencimento em julho de 2015 é: a. -4,50% a.a.
b. 3,48% a.a.
c. 12,00% a.a.
d. 5,25% a.a.
e. 2,26% a.a.

16. A cotação do FRA de cupom (FRC) de vencimento em janeiro de 2016, calculada com base nos ajustes contratos de futuro de DDI da tabela anterior: a. 6,25% a.a.
b. 5,00% a.a.
c. 3,00% a.a.
d. 2,75% a.a.
e. Não é possível calcular com as informações disponíveis Utilizando as seguintes cotações no mercado futuro, com data de ref. 25 de novembro de 2015, responda as seguintes questões:

|  Vencimento | Futuro DI % a.a.o. | Futuro dólar | FRA cupom % a.a. | Prazo dias úteis | Prazo dias corridos  |
| --- | --- | --- | --- | --- | --- |
|  Dez/2015 | 17,20 | 3.749 | - | 4 | 6  |
|  Jan./2016 | 17,44 | - | 1,97 | 27 | 39  |
|  Fev./2016 | 17,62 | - | 2,00 | 48 | 68  |
|  Mar./2016 | 17,78 | - | 2,03 | 66 | 96  |
|  Abr./2016 | 17,92 | - | 2,14 | 88 | 127  |
|  Jul./2016 | 18,06 | - | 2,27 | 151 | 218  |
|  Out./2016 | 18,01 | - | 2,45 | 216 | 312  |
|  Jan./2017 | 17,83 | - | 2,57 | 278 | 403  |

17. O dólar sintético calculado com vencimento em 88 dias úteis (127 dias corridos) será de: a. R$ 3,885
b. R$ 4,328
c. R$ 3,933
d. R$ 4,750
e. R$ 4,629

---

18. A duration modificada do contrato futuro de DI julho 2016 é: a. 0,8049% PU/1% a.a.o.
b. 0,3028% PU/1% a.a.o.
c. 0,4539% PU/1% a.a.o.
d. 0,5075% PU/1% a.a.o.
e. 1,0000% PU/1% a.a.o.

19. A convexidade do contrato futuro de DI julho 2016 é: a. 0,6875% PU/1%² a.a.o.
b. 2,8292% PU/1%² a.a.o.
c. 0,9762% PU/1%² a.a.o.
d. 0,3571% PU/1%² a.a.o.
e. 1,9722% PU/1%² a.a.o.

20. Ainda utilizando a tabela, quantos contratos de futuro de DI com vencimento em janeiro de 2017 seriam necessários para fazer o hedge de taxa pré (nível apenas) de uma carteira de LTN, cujo valor presente, a uma taxa de 17,85% a.a.o., é R$ 12,7 milhões e que possua uma duration de 1,2324 ano over: a. Comprado na taxa em 2.340 DI jan. 2017
b. Comprado na taxa em 170 DI jan. 2017
c. Comprado na taxa em 1.730 DI jan. 2017
d. Vendido na taxa em 170 DI jan. 2017
e. Vendido na taxa em 2.340 DI jan. 2017

21. Beta hedge - O beta de uma determinada carteira de ações, cujo valor de mercado é R$ 25,5 milhões, é 1,174. O próximo vencimento do futuro de IBOVESPA está cotado a 54.431 pontos (R$ 1 por ponto). Para fazer o beta hedge da carteira precisamos ficar: a. Comprado em 5.000 contratos de futuro de índice b. Comprado em 399 contratos de futuro de índice c. Vendido em 399 contratos de futuro de índice d. Vendido em 550 contratos de futuro de índice e. Não é possível saber sem o beta de cada ação que compõe a carteira

---

# CAPITULO 4

## Swaps

---

O swap é um contrato que permite às contrapartes trocarem fluxos de caixa atrelados a diferentes indexadores. Os swaps são contratos negociados em balcão e devem ser registrados nas clearings autorizadas pelo Banco Central do Brasil, especificamente a BM&FBOVESPA ou a Cetip, que depois da fusão passaram a se chamar B3 (Brasil, Bolsa, Balcão). Nesse contrato, as partes trocam um índice de rentabilidade por outro, com o intuito de fazer hedge, casar posições ativas com posições passivas, equalizar preços, arbitrar mercados, minimizar os custos de funding ou até alavancar posições. Para tanto, devem escolher a combinação de variáveis apropriadas à sua operação, definindo preço, prazo e tamanho, optando igualmente pela garantia ou não na hora do registro. Intrinsicamente, as contrapartes estão trocando riscos.

Nos swaps com garantia, a clearing garante a liquidação do contrato, protegendo contra inadimplência na liquidação. Para isso, são exigidos ativos como garantias das contrapartes do swap, que ficarão sob custódia da clearing.

No registro do swap é possível definir fluxos de caixa, como pagamentos de juros ou amortizações, em datas anteriores ao vencimento do contrato. Caso contrário, o swap é registrado como "pagamento final", no qual o diferencial entre o "a receber" e o "a pagar" é liquidado somente no vencimento do contrato.

A B3 oferece várias opções de registro do contrato, com o objetivo de atender às demandas do mercado quanto à customização do produto, por isso é útil verificar a documentação atualizada das clearings antes de definir quais as características que melhor atendam às necessidades de cada contraparte.

# 4.1 Indexadores disponíveis

O swap é um contrato que permite às contrapartes trocarem fluxos de caixa atrelados a diferentes indexadores. As clearings permitem registrar grande variedade de indexadores. No Quando 4.1 estão os indexadores aceitos na B3:

Quadro 4.1 | Indexadores disponíveis para swaps pela B3

|  Índice de preços | Ações | Taxas de juros | Taxas de câmbio  |
| --- | --- | --- | --- |
|  IPCA | IBOVESPA | DI | Dólar  |
|  IGP-M | IBrX | Pré | Euro  |
|   |  | Selic | Iene  |
|   |  | TJLP |   |
|   |  | TR |   |

Fonte: B3 (2015).

---

A Cetip também aceita o registro de diversos indexadores. No quadro a seguir estão os indexadores disponíveis antes da fusão com a BM&FOVESPA:

Quadro 4.2 | Indexadores disponíveis para swaps pela Cetip

|  Índice de preços | Mercadorias | Ações | Taxas de juros | Taxas de câmbio  |
| --- | --- | --- | --- | --- |
|  IPCA | Ouro | IBOVESPA | DI | Dólar  |
|  IGP-M | Outras |  | Pré | Euro  |
|  IGP-DI |  |  | Selic | Franco suíço  |
|  INPC |  |  | TJLP | Outras  |
|   |  |  | TR |   |
|   |  |  | Libor |   |
|   |  |  | TJMI |   |

Fonte: Cetip (2015).

# 4.2 Swaps - Aplicações

Mostraremos alguns exemplos de como o swap pode ser usado para hedge por empresas. Assumiremos que a contraparte será uma instituição financeira, que dá liquidez ao mercado de swaps. Representaremos graficamente as contrapartes dos swaps por retângulos e os fluxos de caixa por setas. O sentido da seta indica a parte que recebe aquele fluxo de caixa do swap:

Figura 4.1 | Representação gráfica do swap
![img-19.jpeg](img-19.jpeg)
Fonte: Elaborada pelos autores.

Cada fluxo de caixa, também chamado de "ponta" ou "perna" do swap, é corrigido por um indexador específico, conforme acordado entre as partes. Na prática, o swap é liquidado pelo valor líquido, apurando-se o valor de cada uma das pontas e calculando a diferença entre elas. Depois de calculada a diferença, a contraparte devedora paga a contraparte credora. No início do swap não é possível saber qual parte irá pagar ou receber, isso dependerá de como o indexador de cada ponta se apreciou em relação ao outro.

Nas próximas seções, apresentaremos alguns exemplos de como o swap pode ser utilizado para atender às necessidades de hedge de diferentes tipos de empresas.

---

# 4.2.1 Swap pré x dólar: hedge de exportação

Um exportador acabou de firmar um contrato de exportação no valor de US$ 10.000.000, pelo qual receberá o equivalente em reais desse montante em 55 dias úteis. O exportador não deseja ter sua receita exposta à variação cambial, dado que seus custos são fundamentalmente em reais e está com receio de que o dólar deprecie perante o real. Uma drástica depreciação do dólar poderia acarretar prejuízo ao exportador, pois correria o risco de não conseguir cobrir seus custos operacionais. Visando diminuir o risco de sua receita, o exportador procura uma instituição financeira para fazer o hedge, fixando seu recebível em reais. A instituição financeira propõe um swap, no qual o banco converte o fluxo que o exportador receberá em dólares por um fluxo pré-fixado em reais.

Esse swap pode ser representado graficamente, de forma resumida, pela Figura 4.2:

Figura 4.2 | Representação gráfica do swap
![img-20.jpeg](img-20.jpeg)
Fonte: Elaborada pelos autores.

Na Figura 4.2, os números circulados indicam o fluxo de caixa e não a ordem de recebimento ou pagamento, já que, idealmente, os fluxos ocorrem no mesmo dia. As linhas contínuas representam a direção dos fluxos de caixa específicos do swap:

- Fluxo 1: representa o recebível em dólar pela exportação. Este fluxo de caixa não faz parte do contrato de swap, sendo, na verdade, o motivador da operação.
- Fluxo 2: representa a ponta em dólar do swap. O exportador contrata o swap de tal maneira que o valor recebido pela exportação será repassado à instituição financeira. Assumindo que não exista o risco de base e de spread, o fluxo 2 cancela-se com o fluxo 1
- Fluxo 3: representa a ponta pré-fixada em reais, convertendo o recebível do exportador em um valor em reais conhecido desde o momento da

---

contratação do swap, por se tratar de um fluxo de caixa atrelado a uma taxa pré-fixada em reais.

Agora que entendemos o racional desse swap, vamos calcular o seu resultado no vencimento assumindo as seguintes informações:

- D_0 = 3,0466: taxa de câmbio inicial para referência da atualização cambial. Normalmente, é a PTAX do dia anterior ao registro do swap.
- D_T = 3,1026: taxa de câmbio final para referência da atualização cambial. Normalmente, é a PTAX do dia anterior à data de liquidação do swap. Essa taxa, obviamente, não é conhecida no momento da contratação do swap.
- PRÉ = 17,85\% a.a.o.: taxa pré-fixada negociada no swap que remunerará o fluxo 3. Essa taxa é definida com base da variação cambial estimada para o período no momento da contratação do swap, não devendo ser confundida com a taxa pré-fixada definida pelo mercado de DI futuro.
- du = 55: prazo do swap em dias úteis, definido assim para corresponder com o prazo de recebimento do exportador pela exportação.
- Nocional = R\  30.466.000: valor-base do contrato em reais a ser registrado na B3 ou na Cetip. Nesse swap específico, o valor do nocional é simplesmente o valor correspondente em reais ao valor em dólar que o exportador deseja hedgear, ou seja, US$ 10.000.000 multiplicado pela taxa de câmbio de referência no início do contrato, D_0 = 3,0466.

Para apurar o resultado do swap no término do contrato, é preciso calcular o valor do nocional atualizado de cada ponta do swap no vencimento da operação.

O valor atualizado (VA) da ponta dólar do swap no vencimento é calculado pela seguinte fórmula:



VA_(Dólar) = Nocional × D_T/D_0   (4.1)



Substituindo os dados do exemplo na equação anterior, teremos:



VA_(Dólar) = R\ 31.026.000,00



Agora, vamos calcular o VA da ponta PRÉ:

---



V A_(P R E) = N o c i o n a l × (1 + P R E)^(d ₀/2 5 2) tag {4.2}



Substituindo:



V A_(D o l a r) = 3 0. 4 6 6. 0 0 0 × (1 + 0, 1 7 8 5)^(5 5/2 5 2)



O resultado da curva pré-fixada será:



V A_(D o l a r) = R S 3 1. 5 7 7. 9 1 1, 4 9



O resultado líquido do swap para o exportador será a diferença entre a ponta que representa um recebimento para ele (fluxo 3) e a ponta pagadora (fluxo 2):



R e s u l t a d o_(E x p o r t a d o r) = 3 1. 5 7 7. 9 1 1, 4 9 - 3 1. 0 2 6. 0 0 0



Então:



R e s u l t a d o_(E x p o r t a d o r) = R S 5 5 1. 9 1 1, 4 9



Nesse caso, na liquidação do swap o exportador receberá da instituição financeira R$ 551.911,49. Na prática, o exportador fixou a receita da exportação em R$ 31.577.911,49, assumindo que a receita da exportação de US$ 10.000.000 tenha sido convertida em reais pela mesma taxa de câmbio utilizada na liquidação da ponta dólar do swap.

## 4.2.2 Swap dólar x Selic: fundo cambial

Um gestor de um fundo cambial mantém uma carteira de LFT¹ que usa, principalmente, como ativo depositado em garantia nas clearings, para atender possíveis chamadas de margens. Visando deixar a rentabilidade mais aderente à variação cambial, que é o propósito do fundo, o gestor procura uma instituição financeira para trocar a rentabilidade

---

indexada à taxa Selic das LFTs por uma rentabilidade atrelada à variação cambial. O valor atual da carteira de LFT é de aproximadamente R$ 20.000.000, vencendo em 150 dias úteis (218 dias corridos). O gestor do fundo procura uma instituição financeira para fazer a troca de rentabilidade por meio de um swap. Esse swap pode ser representado graficamente, de forma resumida, pela Figura 4.3: Figura 4.3 | Representação gráfica do swap

![img-21.jpeg](img-21.jpeg)
Fonte: Elaborada pelos autores.

Os números indicam o fluxo de caixa e as linhas contínuas representam os fluxos de caixa específicos do swap:

- Fluxo 1: representa o recebimento referente ao vencimento das LFTs (atreladas à taxa Selic).
- Fluxo 2: representa a ponta Selic do swap. O fundo contrata o swap de tal maneira que o valor recebido pelo vencimento das LFTs será repassado à instituição financeira. Na prática, o fluxo 2 cancela o fluxo 1.
- Fluxo 3: representa a ponta atrelada ao dólar, convertendo o recebimento do fluxo de caixa referente à liquidação das LFTs por um fluxo atrelado ao dólar. Neste caso, além da variação cambial, a essa ponta é adicionado o cupom cambial. O componente do cupom cambial nesse fluxo de caixa é justificado pela Paridade Coberta da Taxa de Juros, cuja relação de taxas de juros locais e estrangeiras obedece a seguinte equação:



(1 + i_(R e a i s)) = (1 + c c) × D _T/D ₀ tag {4.3}



Em que 1 + i_(Reais) representa o fator de correção pela taxa de juros local, normalmente pode ser o da taxa DI ou da Selic. Neste caso, o i_(Reais) representa a taxa Selic. O fator 1 + cc representa a correção pela taxa de juros em dólar no Brasil, sendo cc o cupom cambial. O componente D_T/D_0 representa a variação cambial projetada.

---

Agora que entendemos o racional deste swap, vamos calcular o seu resultado no vencimento, assumindo as seguintes informações:

- D_0 = 3,1049: taxa de câmbio inicial para referência da atualização cambial. Normalmente, é a PTAX do dia anterior ao registro do swap.
- D_T = 3,1800: taxa de câmbio final para referência da atualização cambial. Normalmente, é a PTAX do dia anterior à data de liquidação do swap. Essa taxa, obviamente, não é conhecida no momento da contratação do swap.
- Selic = 13,25% a.a.o.: variação apurada da taxa Selic desde o início do swap até o seu vencimento. Essa taxa, obviamente, não é conhecida no momento da contratação do swap. Na prática, a variação da Selic é calculada diariamente, com base nos fatores de capitalização de um dia divulgados pelo BACEN.
- du = 150: prazo do swap em dias úteis, definido assim para corresponder com o vencimento da carteira de LFT do fundo.
- dc = 218: prazo do swap em dias corridos.
- cc = 1,50\% a.a.: taxa do cupom cambial. O cupom cambial é a taxa de juros em dólar no Brasil. Essa é a taxa pela qual o swap é negociado.
- Nacional = R\ 20.000.000: valor-base do contrato em reais a ser registrado na B3 ou na Cetip. Esse valor é o montante que o fundo deseja converter da taxa Selic para dólar (mais cupom cambial).

Para apurar o resultado do swap no término do contrato é preciso calcular o valor do nocional atualizado de cada ponta do swap no vencimento da operação.

Vamos calcular então o VA da ponta Selic:



VA_(Selic) = Nacional × (1 + Selic)^(du/252)   (4.4)



Substituindo os dados do exemplo na equação:



VA_(Selic) = 20.000.000 × (1 + 0,1325)^(150/252)



Resultou o seguinte:

---



V A_(S e l i c) = R S 2 1. 5 3 7. 5 1 5, 2 2



O VA da ponta dólar + cupom cambial do swap no vencimento é calculado pela seguinte fórmula:



V A_(Dólar) = N o c i o n a l × (1 + c c × d c/3 6 0) × D _x/D ₀   (4. 5)



Substituindo:



V A_(Dólar) = 2 0. 0 0 0. 0 0 0 × (1 + 0, 0 1 5 × 2 1 8/3 6 0) × 3 , 1 8 0 0/3 , 1 0 4 9



Teremos:



V A_(Dólar) = R S 2 0. 6 6 9. 8 1 2, 2 3



O resultado líquido do swap para o fundo cambial será a diferença entre a ponta que representa um recebimento para ele (fluxo 3) e a ponta pagadora (fluxo 2):



R e s u l t a d o_(F u n d o) = 2 0. 6 6 9. 8 1 2, 2 3 - 2 1. 5 3 7. 5 1 5, 2 2



Então:



R e s u l t a d o_(F u n d o) = - R S 8 6 7. 7 0 2, 9 9



Neste caso, na liquidação do swap o fundo deverá pagar à instituição financeira R$ 835.031,35. Mesmo tendo um prejuízo no swap, o fundo atingiu o seu objetivo de converter o fluxo de caixa atrelado à Selic para dólar.

# 4.2.3 Swap IGP-M x DI: empresa prestadora de serviços

---

Uma empresa que tem uma parte significativa de suas despesas vinculadas à prestação de serviços, atreladas ao Índice Geral de Preços do Mercado (IGP-M), deseja convertê-las em taxas DI. O seu departamento financeiro analisou o passivo indexado ao IGP-M e considera apropriado um hedge no valor de R$ 20.000.000, com vencimento em 78 dias úteis. Então, a empresa procura uma instituição financeira para trocar o indexador de seu passivo por meio de um swap, que pode ser representado graficamente, de forma resumida, pela Figura 4.4:

Figura 4.4 | Representação gráfica do swap
![img-22.jpeg](img-22.jpeg)
Fonte: Elaborada pelos autores.

Os números indicam o fluxo de caixa e as linhas contínuas representam os fluxos de caixa específicos do swap:

- Fluxo 1: representa o passivo indexado ao IGP-M.
- Fluxo 2: representa a ponta atrelada ao IGP-M do swap. Na prática, o fluxo 2 cancela o fluxo 1. A essa ponta é adicionada uma taxa, o cupom de IGP-M.
- Fluxo 3: representa a ponta DI do swap.

Agora que entendemos o racional desse swap, vamos calcular o seu resultado no vencimento com base nas seguintes informações:

- du = 78: prazo do swap em dias úteis, definido assim para corresponder com o seu passivo atrelado ao IGP-M.
- Cupom IGP-M = 8,50% a.a.o.: taxa do cupom de IGP-M. Essa é a taxa negociada no swap.

---

- IGP-M = 5,85\% a.a.o.: variação apurada do IGP-M desde o início do swap até o seu vencimento. Essa taxa, obviamente, não é conhecida no momento da contratação do swap. Na prática, a variação do IGP-M é calculada com base nos números índices do IGP-M, da data de início e de final do swap, divulgados pela Fundação Getulio Vargas (FGV).
- DI = 13,40\% a.a.o.: variação apurada da taxa DI desde o início do swap até o seu vencimento. Essa taxa também não é conhecida no momento da contratação do swap. Na prática, a variação do DI é calculada diariamente, representada pelos fatores de capitalização de um dia divulgados pela Cetip – B3.
- Nacional = R\ 20.000.000: valor-base do contrato em reais a ser registrado na B3. Esse é o valor que a empresa deseja converter de IGP-M para o DI.

Para apurar o resultado do swap no término do contrato é preciso atualizar o valor do nocional de cada ponta do swap até o vencimento da operação.

Agora, vamos calcular o VA no final do contrato da ponta IGP-M + Cupom de IGP-M do swap, que nada mais é do que a variação do IGP-M no período mais o cupom:



VA_(IGPM) = Nocional × (1 + IGPM)^(du/252) × (1 + CupomIGPM)^(du/252) 



Substituindo os dados do exemplo na equação anterior:



VA_(IGPM) = 20.000.000 × (1 + 0,0585)^(78/252) × (1 + 0,085)^(78/252)



Teremos o seguinte resultado:



VA_(IGPM) = R\ 20.875.589,73



Agora vamos calcular o VA da ponta DI:



VA_(DI) = Nocional × (1 + DI)^(du/252) 



Substituindo:

---



V A_(D I) = 2 0. 0 0 0. 0 0 0 × (1 + 0, 1 3 4 0)^(7 8/2 5 2)



Então:



V A_(D I) = R S 2 0. 7 9 3. 8 0 8, 3 2



O resultado líquido do swap para a empresa será a diferença entre a ponta que representa um recebimento para ele (fluxo 2) e a ponta pagadora (fluxo 3):



R e s u l t a d o_(E m p r e s a) = 2 0. 8 7 5. 5 8 9, 7 3 - 2 0. 7 9 3. 8 0 8, 3 2



Então:



R e s u l t a d o_(E m p r e s a) = R S 8 1. 7 8 1, 4 1



Nesse caso, na liquidação do swap, a empresa deverá receber da instituição financeira R$ 81.781,41.

# 4.2.4 Swap DI x Pré: banco de montadora

Um banco de montadora de veículos tem uma parte significativa de suas receitas atreladas às taxas pré-fixadas em reais, em decorrência dos financiamentos de veículos. Para diminuir o risco em relação a um aumento nas taxas de juros, o banco deseja converter suas receitas em taxas pré-fixadas para pós-fixadas, especificamente atreladas ao DI.

O departamento financeiro analisou os seus recebíveis e considera apropriado fazer um hedge no valor de R$ 20.000.000, com vencimento em 150 dias úteis. Então, o banco procura uma instituição financeira para trocar o indexador de seu ativo por meio de um swap, que pode ser representado graficamente, de forma resumida, pela Figura 4.5:

Figura 4.5 | Representação gráfica do swap

---

![img-23.jpeg](img-23.jpeg)
Fonte: Elaborada pelos autores.

Os números indicam os fluxos de caixa e não necessariamente a ordem de recebimento ou pagamento. As linhas contínuas representam os fluxos de caixa específicos do swap:

- Fluxo 1: representa o ativo indexado à taxa PRÉ;
- Fluxo 2: representa a ponta pré-fixada do swap; o fluxo 2 cancela-se com o Fluxo 1;
- Fluxo 3: representa a ponta DI do swap.

Agora que entendemos o racional desse swap, vamos calcular o seu resultado no vencimento com base nas seguintes informações:

- du = 150: prazo do swap em dias úteis, definido assim para corresponder com a duration – prazo médio ponderado – do seu ativo.
- PRÉ = 13,30\% a.a.o.: taxa interna de retorno da carteira de recebíveis do banco de montadora.
- DI = 13,40\% a.a.o.: variação apurada da taxa DI desde o início do swap até o seu vencimento. Essa taxa não é conhecida no momento da contratação do swap. Na prática, a variação do DI é calculada diariamente, representada pelos fatores de capitalização de um dia divulgados pela Cetip.
- Nacional = R\ 20.000.000: valor-base do contrato em reais a ser registrado na B3.

Para apurar o resultado do swap no término do contrato, é preciso calcular o valor do nocional atualizado de cada ponta do swap no vencimento da operação. Vamos calcular o VA da ponta PRÉ do swap:



VA_(PRÉ) = Nacional × (1 + PRÉ)^(du/252) 



Substituindo os dados do exemplo:

---



V A_(P R E) = 2 0. 0 0 0. 0 0 0 × (1 + 0, 1 3 3 0)^(1 5 0/2 5 2)



Teremos o seguinte resultado:



V A_(P R E) = R \ 2 1. 5 4 3. 1 7 4, 7 3



Agora, vamos calcular o VA da ponta DI, com base na seguinte equação:



V A_(D I) = N o c i o n a l × (1 + D I)^(d u/2 5 2) tag {4.9}



Substituindo, teremos:



V A_(D I) = 2 0. 0 0 0. 0 0 0 × (1 + 0, 1 3 4 0)^(1 5 0/2 5 2)



Então:



V A_(D I) = R \ 2 1. 5 5 4. 4 9 0, 7 3



O resultado líquido do swap para o banco da montadora será a diferença entre a ponta que representa um recebimento para ele (fluxo 3) e a ponta pagadora (fluxo 2):



R e s u l t a d o_(M o n t a d o r a) = 2 1. 5 5 4. 4 9 0, 7 3 - 2 1. 5 4 3. 1 7 4, 7 3



Então:



R e s u l t a d o_(M o n t a d o r a) = R \ 1 1. 3 1 6, 0 0



Nesse caso, na liquidação do swap, o banco da montadora deverá receber da instituição financeira R$ 11.316,00.

---

# 4.3 Marcação a mercado de pontas do swap de acordo com o tipo de indexador

Aqui mostraremos o cálculo de marcação a mercado de pontas do swap considerando alguns indexadores comuns no mercado brasileiro. A regra genérica para marcação a mercado é reprecificar a operação, substituindo a taxa originalmente contratada pela taxa de mercado atual, considerando o prazo remanescente a partir de uma data-base, que é a data da apuração do valor a mercado. Para os swaps, esse procedimento é feito para cada uma das pontas.

## 4.3.1 Ponta pré-fixada

Na ponta pré-fixada, o valor futuro da ponta do swap já é conhecido. Portanto, basta trazer o valor futuro ao presente, considerando a taxa vigente de mercado.



V_(mtm) = Nocional × (1 + PRacute{E}_(Contrato))^(du/252)/(1 + PRacute{E}_(mtm))^(du'/252) 



Sendo:

- V_(mtm): valor a mercado da ponta pré-fixada do swap
- nocional: valor-base do swap
- PRacute{E}_(Contrato): taxa pré-fixada contrada na negociação do swap
- PRacute{E}_(mtm): taxa pré-fixada de mercado para esse tipo de swap na data da apuração da marcação a mercado
- du: quantidade de dias úteis da contração até o vencimento do swap
- du': quantidade de dias úteis da data-base de apuração do valor de mercado da ponta até o vencimento

## 4.3.2 Ponta dólar + cupom cambial

A seguir, a equação para marcação a mercado da ponta dólar + cupom cambial:

---



V_(mtm) = Nocional × (1 + C C_(Contrato) × dc/360) × D/D_0/(1 + C C_(mtm) × dc'/360) 



Sendo:

V_(mtm): valor a mercado da ponta do swap **Nocional**: valor-base do swap CC_(Contrato): taxa do cupom cambial contrada na negociação do swap CC_(mtm): taxa do cupom cambial de mercado para esse tipo de swap na data da apuração da marcação a mercado D: PTAX do dia anterior à data de apuração da marcação a mercado D_0: PTAX do dia anterior à data de contratação do swap dc: quantidade de dias corridos da contratação até o vencimento do swap dc': quantidade de dias corridos da data-base de apuração do valor de mercado da ponta, até o vencimento

A equação de marcação a mercado para essa ponta é a mesma para as demais moedas estrangeiras. A diferença é que cada moeda tem sua própria curva de juros ou cupom cambial.

# 4.3.3 Ponta índice de preços: IPCA e IGP-M

A seguir a equação para marcação a mercado, que serve tanto para a ponta IPCA quanto para a IGP-M, mas antes é necessário corrigir o valor da ponta pelo índice da data de início do swap até a data que estamos apurando o valor a mercado:



V_c = Nocional × IND_n/IND_0 × (1 + IND_(Prof))^(dn_n/dn_m) 



Então:



V_(mtm) = V_c × (1 + Cupom_(Contrato))^(dn/252)/(1 + Cupom_(mtm))^(dn'/252) 



Sendo:

---

V_(mtm): valor a mercado da ponta do swap V_c: valor corrigido pelo índice, da data de início do swap até a data-base (data de apuração da marcação à mercado) **Nocional**: valor-base do swap

**Cupom_(Contrato)**: taxa do cupom do índice contrada na negociação do swap

**Cupom_(mtm)**: taxa do cupom do índice de mercado para esse tipo de swap na data da apuração da marcação a mercado

**IND_n**: número do índice divulgado no momento do início do swap

**IND_n**: número do índice mais recente divulgado até o momento da data-base de marcação a mercado

**IND_Proj**: número do índice projetado, divulgado pela Anbima du: quantidade de dias úteis da contração até o vencimento do swap du': quantidade de dias úteis da data-base de apuração do valor de mercado da ponta, até o vencimento du_n: quantidade de dias úteis do início do mês corrente até a data-base du_m: quantidade de dias úteis do mês corrente

## 4.3.4 Ponta taxa de juros: DI e Selic

A seguir, a equação para marcação a mercado que serve tanto para a ponta DI quanto para a Selic, mas antes é necessário corrigir o valor da ponta pelo índice da data de início do swap até a data que estamos apurando o resultado via marcação a mercado:



V_c = Nocional × ∏(j=0 até n) { [ (1 + Taxa_j)^(1/252) - 1 ] × Taxa_(Contrato) + 1 } 



Então:



V_(mtm) = frac{V_c × { [ (1 + PRÉ)^(1/252) - 1 ] × Taxa_(Contrato) + 1 }^(du') { [ (1 + PRÉ)^(1/252) - 1 ] × Taxa_(mtm) + 1 }^(du') 



Sendo:

V_(mtm): valor a mercado da ponta do swap V_c: valor corrigido pela taxa de juros (DI ou Selic, depende da especificação do swap), da data de início do swap até a data-base (data de apuração da marcação a mercado) **Nocional**: valor base do swap

---

Taxa_(Contrato): percentual do DI ou Selic contratada na negociação do swap Taxa_(mtm): percentual do DI ou Selic de mercado para esse tipo de swap na data da apuração da marcação a mercado Taxa_j: taxa anualizada do DI ou Selic do j-ésimo dia PRÉ: taxa pré-fixada para o período da data-base até o vencimento do swap du^*: quantidade de dias úteis da data-base de apuração do valor de mercado da ponta, até o vencimento

# 4.4 Contrato de swap cambial com ajuste periódico baseado em operações compromissadas de um dia (SCS)

Nesta seção faremos uma breve explicação do swap cambial com ajuste periódico de OC1 disponibilizado na B3.

O SCS é um instrumento que permite ao Banco Central do Brasil (BCB) reduzir a volatilidade da taxa de câmbio. O SCS também atende às demandas do mercado local por produtos referenciados à taxa Selic, ao mesmo tempo em que permite a proteção contra a variação do dólar. Nesse instrumento, uma das pontas do swap é remunerada pela taxa Selic, enquanto a outra é atrelada à variação cambial mais o cupom.

A operação é denominada de swap cambial tradicional quando o BCB compra contratos de SCS do mercado:

Figura 4.6 | Representação gráfica do swap cambial tradicional
![img-24.jpeg](img-24.jpeg)
Fonte: Elaborada pelos autores.

Observe que na Figura 4.6 a posição comprada em contratos SCS será ativa na taxa Selic e passiva em variação cambial mais cupom cambial.

Quando o BCB vende contratos de SCS ao mercado, essa operação é denominada swap cambial reverso, conforme ilustrado na Figura 4.7:

Figura 4.7 | Representação gráfica do swap cambial reverso
![img-25.jpeg](img-25.jpeg)
Fonte: Elaborada pelos autores.

---

Observe que na venda de contratos SCS a posição será passiva na taxa Selic e ativa em variação cambial mais cupom.

O BCB oferece esse produto ao mercado por meio de leilão eletrônico. O leilão pode ser de compra ou venda de SCS. As instituições financeiras podem participar do leilão, sendo as propostas vencedoras registradas na B3. A partir do registro, esses contratos podem ser negociados livremente e assumem algumas características dos contratos futuro, como o pagamento ou recebimento de ajuste diário, margem em garantia e padronização de algumas características do contrato.

## 4.4.1 Cálculo do SCS

Assim como o swap dólar x Selic, o SCS é cotado e negociado pela taxa de cupom cambial. O valor da ponta cambial no vencimento é padronizado e definido em US$ 50.000,00. Logo, o valor inicial do contrato para as duas pontas é calculado conforme a Equação 4.16:



Nocional = U\50.000,00/(1 + cc × dc/360) 



Sendo:

**Nocional**: valor inicial em dólares de um contrato **cc**: taxa de cupom cambial negociado

**dc**: número de dias corridos entre o início e o vencimento, exclusive do swap

O ajuste diário do contrato é calculado pela seguinte equação:



AP_t = [ VP_t - 50.000,00/(1 + dc × i_s/360) ] × TC_(t-1) × (1 + Selic_t)^(1/252) 



Sendo:

**AP_t**: ajuste diário em "t"

**Nocional**: valor base do swap

**i_s**: taxa de cupom cambial para as operações Selic x dólar de mercado para o prazo a decorrer do contrato **dc**: prazo em dias corridos, da apuração até o

---

vencimento Selic_t: taxa Selic relativa ao dia do ajuste VP_t: valor inicial do contrato, o nocional de um contrato, atualizado para o dia "t", calculado conforme a Equação 4.18:



VP_t = VP_(t-1) × FC_t   (4.18)



Sendo:

FC_t: fator de correção diário do PU do contrato, calculado conforme a Equação 4.19:



FC_t = ∏(i=1 até k) (1 + Selic_(t-i))^(1/2 · 2)/D_(t-1)/D_(t-2)   (4.19)



Sendo:

Selic_(t-j): taxa Selic referente ao j-ésimo dia útil anterior ao dia "t"

k: número de dias úteis entre o dia "t" e o último dia de negociação D_(t-n): taxa de câmbio do dia "t-n"

# 4.5 O ciclo de vida de um swap

As operações com contratos de swap sem garantia possuem o que definimos como ciclo de vida, que compreende o período desde a data de contratação do instrumento entre as partes, passando pelos procedimentos intermediários de marcação a mercado, até a liquidação no vencimento. Durante o processo de precificação, o risco de crédito entre as partes não será mensurado, ou seja, será considerado apenas o risco de mercado do swap.

Logo, apresentaremos o racional de precificação, marcação a mercado e liquidação, seguindo o conceito de fair value (valor justo). Podemos representar o ciclo de vida de um swap sem cupom de juros conforme a figura a seguir, em que observamos que no momento inicial de contratação do swap entre as partes, deve-se fazer a precificação com base nas informações de mercado naquele momento. Ao longo da vida do contrato devemos marcá-lo a mercado, que pode ser em periodicidade diária dependendo da contraparte envolvida e, ao fim, calculamos os fluxos finais de liquidação do swap no vencimento.

Figura 4.8 | Representação simplificada do ciclo de vida de um swap

---

![img-26.jpeg](img-26.jpeg)
Fonte: Elaborada pelos autores.

Para explicarmos o ciclo de vida geral do swap, adotamos as seguintes premissas:

- O swap está sendo precificado com base nas taxas vigentes de mercado no momento da negociação, ou seja, ambas as partes estão avaliando qual o preço "justo" que definirá os termos contratuais do swap;
- Uma vez negociado, o swap é contabilizado diariamente pelo valor de mercado, com base nas taxas vigentes ao final do dia;
- No momento da liquidação, o valor de cada ponta do swap é apurado de acordo com os termos contratuais do swap e a liquidação é feita pelo valor líquido.

A seguir explicaremos o ciclo de vida de dois contratos de swap: DI x Pré, que é constituído por uma curva pós-fixada e outra com taxa pré-fixada e o IPCA x Pré que possui em uma de suas curvas o índice de inflação IPCA-IBGE, geralmente adicionado de um cupom e, na outra, uma taxa pré-fixada em reais.

# 4.5.1 Swap DI versus Pré: precificação

Neste tópico mostraremos como precificar um swap com uma curva pré-fixada e a outra indexada à taxa do DI, pós-fixada.

Para exemplificar, consideramos que a maturidade do contrato terá um prazo de exatamente 252 dias úteis. Partiremos da premissa de ausência de risco de crédito, dessa forma, coletamos os dados da curva de DI futuro da B3 para o prazo mencionado, resultando em uma taxa para um ano de 7,5% a.a.o.

Vamos assumir que queremos ficar ativo na ponta DI e pagar a taxa pré-fixada. Graficamente, teremos a figura a seguir, que nós receberemos indexado a taxa do DI, indicado pela seta com sentido à esquerda e pagaremos a taxa pré-fixada, no outro sentido:

Figura 4.9 | Representação simplificada do swap DI versus Pré
![img-27.jpeg](img-27.jpeg)
Fonte: Elaborada pelos autores.

---

Qual taxa devemos contratar esse swap? Em outras palavras, qual a taxa de juros pré-fixada que você aceitaria pagar em troca da rentabilidade flutuante de 100% do DI?

Para precificar um swap pré-fixado versus DI, ou seja, definir qual é a taxa pré-fixada contratual, devemos entender que, em condição de não arbitragem, a taxa pré-fixada deve ser igual à expectativa das taxas acumuladas diárias do DI, conforme a seguinte equação:



(1 + E [ Pre])^(K/252) = ∏(j = 0 até K - 1) (1 + E [ DI_j])   (4.20)



Sendo:

(1 + E[Pre]) representa o fator de capitalização referente à taxa pré-fixada livre de risco para um determinado prazo, neste exemplo com base no mercado de DI futuro da B3; (1 + E[DI_j]) representa o fator de capitalização diário referente à taxa de DI de fechamento do j-ésimo dia.

Então, podemos definir que a expectativa da taxa pré-fixada livre de risco tem como base a expectativa das taxas DI over a ser acumuladas de hoje, j = 0, até o dia anterior à liquidação no vencimento do contrato, k - 1.

O mercado futuro de DI expressa, nas taxas negociadas ao longo do pregão, dentre outras variáveis, as expectativas das taxas do DI no futuro. Dessa forma, a taxa pré-fixada pode ser obtida, por exemplo, por meio do mercado de DI Futuro da B3, que incorpora as expectativas definidas pela Equação 4.20.

Vamos assumir que fechamos o swap com os seguintes termos contratuais:

- Estamos ativos na taxa do DI a 100% do DI;
- Pela Equação 4.20, a taxa pré-fixada será 7,50% a.a.o. Nesse exemplo, assumimos que não há spread;
- Prazo: 252 dias úteis;
- Valor nocional do swap na data de contratação: R$ 10 milhões.
- Não possui pagamentos de cupom ou ajuste intermediários, ou seja, liquidação financeira apenas no vencimento.

## 4.5.2 Swap DI versus Pré: marcação a mercado

---

Vamos supor que foram passados 52 dias úteis após a data de contratação do swap, durante esse período constatamos que a taxa DI acumulada realizada desde a data de início do contrato até hoje foi de 1,4937782% para o período e que a curva dos contratos futuros de DI indica uma taxa de 7,25% a.a.o. para o prazo remanescente, 200 dias úteis. Na figura a seguir podemos constatar o momento do ciclo de vida do swap, considerando que a data zero, D0, é a data inicial de contratação do swap:

Figura 4.10 | Decorridos 52 dias úteis
![img-28.jpeg](img-28.jpeg)
Fonte: Elaborada pelos autores.

Desejamos calcular o valor marcado a mercado (MtM) desse swap. Para isso, precisamos calcular o valor de mercado de cada uma de suas pontas: Vamos começar pela marcação a mercado da ponta ativa. Graficamente:

Figura 4.11 | Marcação a mercado da ponta DI
![img-29.jpeg](img-29.jpeg)
Fonte: Elaborada pelos autores.

Sabemos que a marcação a mercado significa trazer ao valor presente o fluxo de caixa esperado pelas taxas vigentes de mercado. Então, para a ponta 100% do DI, temos:



MtM_(DI) = 10.000.000 × (1 + DI_(DI)^(52)) × (1 + E[DI_(52)^(152)])/(1 + E[Pré_(52)^(152)])



Vamos entender a equação acima. No numerador temos o valor esperado do fluxo de caixa no vencimento, que é a correção dos R$ 10 milhões pela taxa do DI over realizada da data do início do contrato até o dia útil 52 e da expectativa da realização diária da taxa do DI over do dia 52, "hoje", até o vencimento. O denominador considera a taxa pré-fixada de

---

mercado para o período remanescente para trazer o fluxo de caixa esperado ao valor presente.

Podemos simplificar a equação anterior, pois, como notamos anteriormente, a taxa pré-fixada para o prazo remanescente é a expectativa das taxas do DI over acumuladas de hoje até o vencimento:



MtM_(DI) = 10.000.000 × (1 + DI_N^(32)) × (1 + E[DI_(32)^(252)])/(1 + E[Pré_(32)^(252)])



Podemos calcular o valor de marcação a mercado da ponta DI:



MtM_(DI) = 10.000.000 × (1 + 0,014937782)



Então,



MtM_(DI) = R\ 10.149.377,82



Agora, vamos calcular o valor a mercado da ponta pré-fixada. Graficamente:

Figura 4.12 | Marcação a mercado da ponta pré-fixada
![img-30.jpeg](img-30.jpeg)
Fonte: Elaborada pelos autores.

Para calcular o valor de mercado da ponta pré-fixada, basta calcular o valor presente do fluxo de caixa, 10.000.000 × (1 + 0,075)^(32/252) = R\ 10.750.000,00, pela taxa vigente de mercado para o prazo remanescente, 7,25% a.a.o.



MtM_(Pre) = R\ 10.750.000,00/(1 + 7,25\%)^(32/252)



---

Então,



MtM_(Pre) = R\ 10.169.125,86



Dado que estamos ativos na ponta DI e passivos na ponta pré-fixada, qual o resultado de marcação a mercado para nós no 52º dia útil? É a diferença entre o valor de mercado da ponta ativa e o da ponta passiva: R$ 10.149.377,82 – R$ 10.169.125,86. Logo, nesse exemplo, o nosso resultado de marcação a mercado é uma perda de R$ 19.748,03.

## 4.5.3 Swap DI versus Pré: liquidação

No dia da liquidação do swap, apuramos que a taxa do DI acumulada realizada na vida do swap foi de 7,354582% ao período. Vamos calcular o valor liquidado.

Na ponta ativa, indexada a 100% do DI, temos:



Liquidação_(DI) = 10.000.000 × (1 + 7,354582\%)



Então,



Liquidação_(DI) = R\ 10.735.458,20



Na ponta passiva, pré-fixada a 7,50% a.a.o., temos:



Liquidação_(DI) = R\ 10.000.000 × (1 + 7,50\%)^(252/252)



Então,



Liquidação_(Pré) = R\ 10.750.000,00



A liquidação de um swap ocorre pela diferença entre as pontas ativa e passiva, então:



Valor Liquidado_(Nós) = R\ 10.735.458,20 - 10.750.000,00 = R\ -14.541,80



Ou seja, nós pagamos R$ 14.541,80 na liquidação do swap.

---

# 4.5.4 Swap IPCA versus Pré: precificação

Neste tópico mostraremos como precificar um swap com uma ponta pré-fixada e a outra indexada à taxa ao IPCA.

Assumimos que queremos ficar ativos na ponta indexada ao IPCA e pagar a taxa pré-fixada. Graficamente, temos:

Figura 4.13 | Representação simplificada do swap IPCA versus Pré
![img-31.jpeg](img-31.jpeg)
Fonte: Elaborada pelos autores.

Estamos negociando um swap com o prazo de 252 dias úteis. Coletando os dados de mercado, aqui assumindo as curvas zero cupom de títulos do Tesouro fornecidos pela Anbima, temos:

Tabela 4.1 | Taxas de mercado no momento da precificação a.a.o.

|  ETTJ - Inflação Implícita (IPCA (% a.a./252)  |   |   |   |
| --- | --- | --- | --- |
|  Vértices | ETTJ IPCA | ETTJ Pré | Inflação implícita  |
|  252 | 2,0338% | 5,3175% | 3,2182%  |
|  378 | 1,8885% | 5,4783% | 3,5233%  |
|  504 | 2,0249% | 5,7243% | 3,6260%  |

Fonte: Elaborada pelos autores com base em dados da Anbima (2019).

Como interpretar a tabela anterior? É preciso antes definir as colunas:

- Vértices: são os prazos em dias úteis;
- ETTJ IPCA: representa o cupom de IPCA ou taxa de juros reais – que representa a taxa de juros acima da inflação nominal;
- ETTJ Pré: taxa pré-fixada ou taxa nominal de juros;
- Inflação implícita: aceitando a hipótese de Fisher, indica a taxa esperada de inflação.

---

A hipótese de Fisher estabelece que a taxa nominal de juros é a soma da taxa de juros reais e da inflação esperada. Como as taxas da Tabela 4.1 estão na forma discreta, podemos representar a hipótese de Fisher pela Equação 4.21:



(1 + ETTJPRE)^(du/252) = (1 + ETTJIPCA)^(du/252) × (1 + Inflação Implícita)^(du/252)   (4.21)



Só para mostrar como a hipótese de Fisher é uma premissa aceita pela Tabela 4.1, substituindo as taxas na Equação 4.21 para o vértice de prazo 252 dias úteis, temos:



(1 + 5,3175\%)^(252/252) = (1 + 2,0338\%)^(252/252) × (1 + 3,2182\%)^(252/252)



Então, constatamos que o lado esquerdo da equação é, de fato, igual ao lado direito da equação, ou seja, 1,053175.

Com base na Tabela 4.1, qual a taxa que deveríamos cotar um swap de prazo de 252 dias úteis? Em outras palavras, qual a taxa de cupom de IPCA que desejamos receber, assumindo que fixamos a taxa em 5,3175% a.a.o.? Pela relação de Fisher, a taxa de cupom de IPCA é de 2,0338% a.a.o.

Utilizando as informações anteriores, vamos assumir que fechamos um swap conforme os termos contratuais a seguir:

- Estamos ativos na ponta IPCA, mais um cupom de IPCA de 2,0338% a.a.o.;
- Estamos passivos na taxa pré-fixada a 5,3175% a.a.o.;
- Prazo: 252 dias úteis;
- Nocional: R$ 10 milhões.

## 4.5.5 Swap IPCA versus Pré: marcação a mercado

Passados 52 dias úteis, constatamos que a inflação realizada desde a data de início do contrato até hoje foi de 0,75% a.p., que as curvas de mercado projetam a taxa pré-fixada em 5,00% a.a.o. e a taxa de cupom de IPCA em 1,50% a.a.o. para o prazo remanescente, 200 dias úteis:

![img-32.jpeg](img-32.jpeg)
Figura 4.14 | Decorridos 52 dias úteis

---

Fonte: Elaborada pelos autores.

Desejamos calcular o valor MtM desse swap. Para isso, precisamos calcular o valor de mercado de cada uma das pontas.

Vamos começar pela marcação a mercado da ponta ativa. Graficamente:

Figura 4.15 | Marcação a mercado da ponta IPCA
![img-33.jpeg](img-33.jpeg)
Fonte: Elaborada pelos autores.

Sabemos que a marcação a mercado é trazer ao valor presente o fluxo de caixa esperado pelas taxas vigentes de mercado. Então, para a ponta IPCA, temos:



MtM_(IPCA) = 10.000.000 × (1 + IPCA_0^(52)) × (1 + E[IPCA_(52)^(252)]) × (1 + ContratoCupomIPCA_0^(252))/(1 + Pré_(52)^(252))



Sendo:

(1 + IPCA_0^(52)) representa o fator de capitalização referente ao IPCA acumulado da data de início do contrato até o 52^a dia útil; (1 + E[IPCA_(52)^(252)]) representa o fator de capitalização referente à inflação implícita, ou IPCA esperado, do 52^a dia útil até o vencimento do swap; (1 + ContratoCupomIPCA_(52)^(252)) é o fator de capitalização referente ao cupom de IPCA contratado, da data de início do contrato até o seu vencimento; 1/(1 + Pré_(52)^(252)) é o fator de desconto com base na taxa livre de risco, nesse exemplo, coletada pelas taxas zero cupom de títulos do Tesouro pela Anbima, para o prazo remanescente do swap.

Então, no numerador temos o valor esperado do fluxo de caixa, que é a correção dos R$ 10 milhões pelo IPCA realizado da data de início do contrato até o dia 52^a útil, a da expectativa do IPCA do dia 52, "hoje", até o vencimento e do cupom de IPCA contratual

---

do swap, que é aplicado ao nocional desde a data de início do swap até o vencimento. O denominador considera a taxa pré-fixada de mercado para o período remanescente para trazer o fluxo de caixa esperado ao valor presente.

Pela relação de Fisher, podemos substituir o denominador. Então, temos:



MtM_(IPCA) = 10.000.000 × (1 + IPCA_0^(52)) × (1 + E[IPCA_(52)^(252)]) × (1 + ContratoCupomIPCA_0^(252))/(1 + E[IPCA_(52)^(252)]) × (1 + MercadoCupomIPCA_(52)^(252))



Sendo:

(1 + MercadoCupomIPCA_0^(252)) é o fator de capitalização referente ao cupom de IPCA de mercado, observado para o prazo remanescente.

Podemos simplificar a equação acima:



MtM_(IPCA) = 10.000.000 × (1 + IPCA_0^(52)) × (1 + E[IPCA_(52)^(252)]) × (1 + ContratoCupomIPCA_0^(252))/(1 + E[IPCA_(52)^(252)]) × (1 + MercadoCupomIPCA_(52)^(252))



A fórmula simplificada é definida por:



MtM_(IPCA) = 10.000.000 × (1 + IPCA_0^(52)) × (1 + ContratoCupomIPCA_0^(252))/(1 + MercadoCupomIPCA_(52)^(252))



Observamos que a fórmula simplificada é menos intuitiva do que a fórmula completa, mas é a que utilizamos na prática, pois exige menos variáveis para obter o valor de mercado da ponta IPCA do swap.

Agora podemos calcular o valor de marcação a mercado da ponta IPCA:



MtM_(IPCA) = 10.000.000 × (1 + 0,75\%) × (1 + 2,0338\%)^(252)/(1 + 1,50\%)^(200)



Logo,



MtM_(IPCA) = R
 10.159.149,15



---

Vamos calcular o valor a mercado da ponta pré-fixada. Graficamente:

Figura 4.16 | Marcação a mercado da ponta pré-fixada
![img-34.jpeg](img-34.jpeg)
Fonte: Elaborada pelos autores.

Para calcular o valor de mercado da ponta pré-fixada, basta calcular o valor presente do fluxo de caixa, 10.000.000 × (1 + 0,053175)^(252/252) = R\  10.531.750,00, pela taxa vigente de mercado de 5,00\% a.a.o., para o prazo remanescente.



MtM_(Pré) = 10.531.750,00/(1 + 5,00\%)^(200/252)



Então,



MtM_(Pré) = R\  10.131.730,69



Lembrando que estamos ativos na ponta IPCA e passivos na ponta pré-fixada. Qual o resultado de marcação a mercado no 52^(circ) dia útil? Basta calcularmos a diferença entre o valor de mercado da ponta ativa e o da ponta passiva: R\ 10.159.149,15 - R\ 10.131.730,69. Logo, nesse exemplo, o nosso resultado de marcação a mercado é um ganho de R\ 27.418,46.

# 4.5.6 Swap IPCA versus Pré: liquidação

---

No dia da liquidação do swap apuramos que o IPCA acumulado na vida do swap foi de 3,50% ao período. Vamos calcular o valor liquidado.

Na ponta ativa, indexada ao IPCA, temos:



Liquidação_(IPCA) = 10.000.000 × (1 + 3,50\%) × (1 + 2,0338\%)^(252over 252)



Então,



Liquidação_(IPCA) = R\ 10.560.498,30



Na ponta passiva, pré-fixada a 5,3175% a.a.o., temos o seguinte resultado:



Liquidação_(Pré) = 10.000.000 × (1 + 5,3175\%)^(252over 252)



Então,



Liquidação_(Pré) = R\ 10.531.750,00



A liquidação de um swap ocorre pela diferença entre a ponta ativa e a passiva, então:



Valor Liquidado_(Nós) = R\ 10.560.498,30 - 10.531.750,00 = R\ 28.748,30



Ou seja, nós recebemos R\ 28.748,30 na liquidação do swap.

## 4.5.7 Swap DI versus Dólar: precificação

Para entender o ciclo de vida de um swap DI versus Dólar, vamos assumir que somos um exportador que deseja converter uma receita de USD 2.521.550 esperada para daqui um ano. Para isso estamos negociando um swap DI versus Dólar com o prazo de 252 dias úteis (360 dias corridos). Abaixo as informações extraídas de mercado no momento da precificação:

- Futuro DI₁ (curto): 1,906% a.a.o.; prazo: 8 du

---

- Futuro DI_T (longo): 3,116% a.a.o.; prazo: 252 du
- FRC_T: 1,139% a.a.: termo entre 12 dc e 360 dc
- Dólar Futuro (D_1): 5.315,75 (próximo vencimento)
- BRL/USD PTAX = 5,3000

Abaixo a representação deste swap de acordo com os fluxos de rentabilidade:

Figura 4.17 | Representação simplificada do swap DI versus Dólar
![img-35.jpeg](img-35.jpeg)
Fonte: Elaborada pelos autores.

Para precificar este swap, é preciso calcular o cupom cambial de acordo com as informações vigentes de mercado. Para isso, devemos calcular o dólar sintético:



D _T = (1 + D I _T)^(d u _T / 2 5 2)/(1 + D I ₁)^(d u ₁ / 2 5 2) × D ₁/1 + F R C _T × d c _T - d c ₁/3 6 0 tag {4.22}



Sendo:

D₁: cotação do dólar futuro de vencimento curto em du₁

DI_T, DI₁: taxa de juros do DI ao período, com vencimento longo e curto, respectivamente FRC_T: FRA de cupom com vencimento em dcₜ

du_T, du₁: número de dias úteis para o último e primeiro vencimento de futuro de DI, respectivamente dc_T, dc₁: número de dias corridos para o último e primeiro vencimento de futuro de DI, respectivamente, utilizado para cálculo do FRA de cupom

Substituindo com as taxas de mercado dadas no enunciado, temos que:



D _T = (1 + 3,116\%)^(252/252)/(1 + 1,906\%)^(9/252) × 5.315,75/1 + 1,139\% × 360 - 12/360 = 5.418,45



Portanto, o dólar sintético, projetado para o vencimento do swap em 360 dias corridos é R$ 5.418,45.

Na prática, dividimos o resultado acima por mil, pois precisamos de uma taxa reais por dólar, logo o dólar da curva para precificar o swap será R$ 5,41845.

---

Após calcular o dólar sintético pelas taxas vigentes de mercado, devemos calcular o cupom cambial, que definirá os termos contratuais deste swap DI versus Dólar, para isso utilizaremos o dólar sintético na seguinte equação:



CC_(contrato) = {[ (1 + DI_T) du/252 × D_0/D_T ] - 1 } × 360/dc   (4.23)



Sendo:

D_0: PTAX, dólar divulgado pelo BACEN em D-1. Em alguns casos o banco pode sugerir uma outra taxa de câmbio no lugar do PTAX, como o dólar spot. No nosso exemplo usaremos o PTAX, por ser mais usual du e dc: número de dias úteis e corridos até o vencimento do SWAP, respectivamente.

Substituindo os dados do exemplo na equação acima:



CC_(contrato) = {[ (1 + 3,116\%) 252/252 × 5,3000/5,41845 ] - 1 } × 360/360 = 0,862\%  a. a.



Assumindo que o cupom cambial contratual não tenha nenhum spread adicionado a ele, temos o cupom cambial resultante de 0,862% a.a.

Logo, neste swap, o exportador receberá 100% da variação do DI e, em troca, pagará variação cambial mais um cupom cambial contratual de 0,862% a.a.

Antes de fecharmos o swap, precisamos definir o nocional, que será o valor presente da nossa receita futura em dólar, descontando a valor presente o valor a ser hedgeado pela empresa:



National_(USD) = 2.521.550,00/1 + 0,862\% × 360/360 = 2.500.00



Como o nocional do swap será US$ 2,5 milhões que deverá ser registrado em reais, portanto fazemos a conversão utilizando o dólar inicial:



National_(BRL) = 2.500.000 × 5,3000 = R\  13.250.000



Portanto, o valor nocional para registro na B3 será de R$ 13.250.000.

Com base nos cálculos realizados, para a contratação do swap DI versus Dólar, teremos os seguintes termos contratuais:

- Taxa BRL/USD no momento da contratação: 5,3000;
- O exportador está ativo na ponta DI;

---

- O exportador está passivo na ponta dólar, mais um cupom cambial de 0,862% a.a.;
- Prazo: 252 dias úteis com 360 dias corridos;
- Nocional: R$ 13.250.000.

# 4.5.8 Swap DI versus Dólar: marcação a mercado

Iremos marcar a mercado o swap passados 52 dias úteis, ou 80 dias corridos, desde sua contratação. Verificamos as seguintes taxas vigentes de mercado:

- D_T = 5,3700 (dólar sintético);
- Taxa pré-fixada observada pela curva de DI futuro interpolada para o prazo remanescente = 2,75% a.a.o.
- DI acumulado desde a contratação do swap até a data da atual de marcação a mercado foi de 0,45% a.p.

Podemos representar graficamente a marcação a mercado antes do vencimento do swap:

Figura 4.18 | Decorridos 52 dias úteis
![img-36.jpeg](img-36.jpeg)
Fonte: Elaborada pelos autores

Desejamos calcular o valor MtM – o valor marcado a mercado – deste swap. Para isso, devemos calcular o valor de mercado de cada uma das pontas, ativa e passiva.

Vamos começar pela marcação a mercado da ponta ativa de 100% do DI. Graficamente teremos:

Figura 4.19 | Marcação a mercado da ponta DI

---

![img-37.jpeg](img-37.jpeg)
Fonte: Elaborada pelos autores

Para calcular a ponta DI, devemos aplicar a taxa do DI acumulado desde a data de contratação do swap sobre o valor nocional em reais:



MtM_(DI) = 13.250.000 × (1 + 0,45\%) = R\ 13.309.625,00



Após calcular a ponta ativa, agora vamos calcular a marcação a mercado da ponta passiva em dólar mais cupom cambial:

Figura 4.20 | Marcação a mercado da ponta Dólar
![img-38.jpeg](img-38.jpeg)
Fonte: Elaborada pelos autores

Como estamos avaliando a ponta indexada ao dólar com cupom cambial, devemos fazer a contagem por dias corridos. A equação abaixo mostra o racional de marcação a mercado desta ponta. No numerador temos o valor esperado do fluxo de caixa, que é a correção do nocional inicial de R$ 13.125.000 pela variação cambial mais o cupom cambial fixado no momento da contratação do swap de 0,862% a.a. O denominador considera a taxa pré-fixada de mercado para o período remanescente para descontar o fluxo de caixa esperado ao valor presente.

Analogamente à relação de Fisher usada na marcação a mercado da ponta IPCA, temos que:



MtM_(Dolar) = 13.250.000 × (E[VC_0^(360)]) × (1 + ContratoCupom_0^(360))/(1 + Pré_(52du)^(252du))



---

Sendo:

VC₀^(360) : é a variação cambial desde a data da contratação até o vencimento do swap

ContratoCupom^(360)₀ : cupom original contratual do swap

Pré^(252du)_(52du) : taxa pré-fixada desde a data de marcação a mercado até o vencimento do swap

Substituindo os dados na equação acima, teremos:



MtM_(Dolar) = 13.250.000 × 5,37/5,30 × (1 + 0,862\% × 360/360)/(1 + 2,75\% 200/252) = R\ 13.252.298,54



A ponta passiva de dólar mais um cupom cambial marcada a mercado resultou em um valor de R\ 13.252.298,54.

Lembrando que estamos ativo na ponta DI e passivo na ponta dólar, qual o resultado de marcação a mercado no 52º dia útil (80º dia corrido)? Basta calcularmos a diferença entre o valor de mercado da ponta ativa e o da ponta passiva: R\ 13.309.625,00 - R\ 13.252.298,54. Logo, neste exemplo, o nosso resultado de marcação a mercado é um ganho de R\ 57.326,46.

# 4.5.9 Swap DI versus Dólar: liquidação no vencimento

Assumindo que PTAX apurada no vencimento da operação foi BRL/USD 5,35 e que o DI acumulado desde a data de contratação 3,00% ao período, vamos calcular o valor da liquidação do swap.

O valor da ponta ativa, indexada ao DI, é R\ 13.647.500,00, obtido da seguinte maneira:



R\ 13.250.000 × (1 + 3,00\%)



O valor da ponta passiva, em dólar, é R\ 13.490.292,50, ou:

---



R
 13.250.000,00 × 5,35/5,30 × (1 + 0,862\% × 5,35/5,30)



Então, o valor a liquidar do nosso ponto de vista (exportador) é R\ 13.647.500,00 menos R\ 13.490.292,50. Então, recebemos à contraparte R\ 157.207,50 no vencimento.

## 4.5.10 Conclusão

Observamos que algumas das fórmulas finais de marcação a mercado utilizadas são simplificadas, o que acaba prejudicando o seu entendimento. Nesta seção descrevemos o racional de precificação e marcação a mercado de alguns dos swaps feitos no mercado local, partindo das equações em suas formas completas, explicando sua intuição, antes de aplicá-las em suas formas simplificadas. No caso do swap cambial, utilizamos a metodologia de cálculo do dólar sintético, vista no capítulo anterior.

## 4.6 Swap Libor x pré-fixado em dólar

Este livro tem como enfoque o mercado de derivativos nacional, contudo, achamos pertinente dedicar algumas páginas para tratar dos swaps de Libor, por serem operações relevantes nos mercados internacional e brasileiro. Aproveitaremos para tratar de mudanças na precificação desse swap após a crise de crédito internacional de 2007. Os swaps de Libor podem ser feitos referenciando diferentes moedas.

Por sua importância, aqui traremos exemplos de swaps em que a moeda-base é o dólar americano.

## 4.6.1 Breve explicação sobre swap de Libor

O swap de libor versus pré-fixado poder ser representada pela Figura 4.21.

Figura 4.21 | Swap de Libor

---

![img-39.jpeg](img-39.jpeg)
Fonte: Elaborada pelos autores.

Os números na Figura 4.21 indicam o fluxo de caixa e as linhas contínuas representam os fluxos de caixa do swap:

- Fluxo 1: representa o passivo pós-fixado (Libor) da empresa. Esse fluxo não faz parte do contrato de swap;
- Fluxo 2: representa a ponta atrelada à taxa Libor do swap, na prática, o fluxo 2 cancela o fluxo 1;
- Fluxo 3: representa a ponta pré-fixada.

O racional da operação pode ser uma empresa desejando fixar seus custos pós-fixados, por isso procura uma instituição financeira para fazer a troca de rentabilidade, transformando um passivo pós-fixado em pré-fixado.

A taxa Libor é uma taxa média de juros, na qual bancos estão dispostos a emprestar uns aos outros no mercado internacional. É uma taxa referencial de transações internacionais. Até a crise de crédito de 2007 era aceita como uma proxy da taxa de juros livre de risco. Como veremos adiante, a realidade mostrou que, sob determinadas condições de mercado, a Libor não é uma boa proxy livre de risco, impactando na precificação dos derivativos.

A maior dificuldade para nós, brasileiros, de entender os swaps de Libor, é devido às convenções de cálculos, frequências dos fluxos de caixa e formação de preço. Uma vez que entendamos as diferentes convenções, um pouco de matemática financeira e recursos do Microsoft Excel seremos capazes de:

- precificar um swap de Libor, entendendo como o seu preço é formado no mercado internacional;
- calcular a marcação a mercado de um swap de Libor já existente.

## 4.6.2 Eurodólar

---

Para entendermos o mercado formador de taxas de swaps é necessário falar um pouco do mercado futuro de eurodólar ou eurodollar futures. Este mercado é um importante formador de preço dos swaps de Libor, sendo um benchmark para os investidores em âmbito global e uma ferramenta para fazer o hedge das flutuações de taxas de juros de curto prazo, em dólares norte-americanos. O preço de ajuste final para os futuros de eurodólar é determinado pela taxa interbancária de três meses da Libor, no último dia de negociação. Os eurodólares são dólares norte-americanos, depositados em bancos comerciais fora dos Estados Unidos. Os preços do mercado futuro de eurodólar refletem as expectativas de taxas de juros referentes aos depósitos de eurodólar de prazos de três meses, para datas específicas no futuro (taxas forward).

Os contratos futuros de eurodólar são negociados em bolsa, na Chicago Mercantile Exchange (CME). As definições do contrato aqui descritas foram baseadas nas próprias definições dessa bolsa, que possui ampla documentação sobre as características do contrato.

## 4.6.3 Eurodólar - Ajuste de convexidade

As taxas expressas pelos contratos futuros de eurodólar sofrem pequenos ajustes ao serem usadas para calcular as taxas Libor vigentes. Esse ajuste é chamado de ajuste de convexidade. Esse ajuste é necessário, pois não podemos assumir que as taxas indicadas pelos futuros de eurodólar sejam idênticas às taxas Libor forward. Os futuros são liquidados diariamente via ajustes diários, já os fluxos de um swap atrelados à taxa Libor dos swaps são liquidados de uma vez, na data de liquidação do fluxo. Até então, estávamos assumindo que os preços e taxas dos futuros são iguais aos dos termos (ou mercado de balcão, com o de swaps). Como as taxas refletidas pelos futuros de eurodólar são um pouco diferentes das taxas dos swaps de Libor, optamos por mostrar o ajuste feito pelo mercado nas taxas dos swaps de Libor.

Os livros-texto, como o de Hull (2012), indicam a seguinte fórmula para ajustar as taxas dos futuros de eurodólar para taxas forward:



Rate_(Forward) = Rate_(Futures) - 0,5σ²T₁T₂   (4.24)



Onde T₁ é o início do período da taxa futura ou forward, T₂ o final deste período e σ é a volatilidade anual das variações do short-term interest rate. As taxas devem ser expressas na sua forma contínua.

A seguir, um exemplo do ajuste de convexidade, "Cvx Adj", consultado no sistema da Bloomberg:

---

Figura 4.22 | Tela Bloomberg: exemplo de ajuste de convexidade
![img-40.jpeg](img-40.jpeg)
Fonte: Bloomberg (2017).

# 4.6.4 Fluxos de caixa de um swap Libor x pré-fixado

Comumente, esses swaps têm fluxos de caixas intermediários, assemelhando-se a títulos que pagam cupom. A periodicidade típica é que a ponta pré-fixada pague cupons semestrais e a ponta Libor pague cupons trimestrais.

É importante entendermos que a Libor do primeiro fluxo de caixa é fixada no início do swap. Na verdade, a convenção para swaps de Libor plain vanilla é que a taxa Libor é definida (ou reset) no início do período do pagamento daquele fluxo de caixa, k_(12+1), ou seja, a taxa Libor utilizada para calcular o fluxo de caixa de t + 1 é fixada em t, ou seja, no período anterior. A Figura 4.10 representa os fluxos de caixa:

![img-41.jpeg](img-41.jpeg)
Figura 4.23 | Exemplo de fluxos de caixa atrelados à Libor

---

Fonte: Elaborada pelos autores.

# 4.6.5 Swaps de Libor - Antes e depois da crise de crédito de 2007

Como mencionamos, a taxa Libor, além de popular indexadora de uma das pontas dos swaps de taxas de juros internacionais (interest rate swaps), era considerada uma taxa muito próxima de ser a livre de risco, sendo usada para calcular os valores presentes dos fluxos de caixa do swap. A Figura 4.11 mostra que essa crença foi abalada durante a crise de 2007:

Figura 4.24 | O spread Libor-OIS
![img-42.jpeg](img-42.jpeg)
Fonte: Federal Reserve Bank of St. Louis.

OIS é a sigla para overnight indexed swap, que é um indexador representado por uma taxa de juros, computada diariamente. Nos Estados Unidos, é a effective federal funds rate, equivalente à taxa DI diária no Brasil.

O spread Libor-OIS é um indicador do risco de crédito e liquidez no setor bancário e é calculado em basis points, indicado no eixo vertical da Figura 4.11. Durante a crise, os bancos hesitaram em emprestar uns aos outros, ou seja, assumiu-se um risco de crédito entre os bancos até então inexistente, ou pelo menos não nas proporções vistas.

A curva de juros da OIS passou a ser o padrão de mercado na precificação destes swaps. Esta é a curva que as clearings usam para marcar a mercado os swaps e definir as margens e garantias exigidas. Após o Dodd-Frank Act, em 2010, passou a ser mandatório o registro de swaps em clearings e passou-se a exigir que estes swaps fossem da modalidade com garantia (collateralized).

---

## 4.6.6 Precificação

Na precificação do swap de Libor é fundamental sabermos se o swap é sem garantia (non-collaterilaZed) ou com garantia (collaterilaZed). A diferença principal é que nos swaps sem garantia, a taxa Libor, além de ser indexadora da ponta pós-fixada, é assumida como taxa adequada para trazer os fluxos de caixas a valores presentes. Como o risco de crédito da contraparte está incorporado à taxa Libor, o racional é que esta é a taxa apropriada para calcular os valores presentes dos fluxos dos swaps registrados sem garantia. Já nos swaps com garantia, a proxy da taxa livre de risco é a taxa OIS. Veremos como precificar combinações de swaps sem e com garantia.

Aqui definimos precificação como o momento de negociação no qual as partes estão negociando as taxas contratuais do swap. O processo de precificação determina a taxa pré-fixada. Então, quando precificamos esses tipos de swap, o que estamos buscando é a taxa pré-fixada contratual.

Nos exemplos que mostraremos de precificação dos contratos, assumiremos o seguinte:

- swaps do tipo plain vanilla;
- os valores presentes das duas pontas dos swaps são iguais;
- logo, o NPV do swap, a soma das pontas ativa e passiva, é zero no instante em que o swap é registrado.

Podemos entender os swaps de Libor x pré-fixado como uma série de contratos for Wards de diferentes vencimentos. Neste livro, optamos por abordar esses swaps como sendo títulos que pagam cupons periódicos e cupom mais principal no vencimento, sendo a ponta pré-fixada representada por um título pré-fixado e a ponta Libor por um título pós-fixado.

Apresentaremos o procedimento e cálculos necessários para precificar os swaps aqui exemplificados partindo de exemplos reais extraídos do sistema Bloomberg.

## 4.6.7 Convenções de contagem de dias corridos

---

No mercado internacional, existem várias maneiras de contar os dias corridos. Aqui utilizaremos duas formas para que o leitor se familiarize com as que são pertinentes aos swaps de Libor:

- Dias corridos reais Actual/360, ou seja, considera-se a quantidade de dias corridos pelo calendário entre dois períodos;
- Dias corridos 30/360, que considera que cada mês tem 30 dias corridos.

Indicaremos nos exemplos a convenção utilizada nos cálculos.

# 4.6.8 Precificando um swap Libor sem garantia e sem spread

Os swaps sem garantia representavam a principal modalidade antes da crise. Sua precificação é mais simples do que o swap com garantia, pois a mesma taxa libor indexadora da ponta pós-fixada era utilizada para trazer aos valores presentes tanto dos fluxos pós-fixados quanto dos pré-fixados.

Assumindo um swap sem garantia, em que a data do fechamento do contrato do swap seja no início do período de reset da cotação da Libor, e que não haja spread, qual deverá ser a soma dos valores presentes dos fluxos de caixa da ponta Libor?

Ora, se os fluxos de caixa são indexados à Libor e são trazidos aos valores presentes pela própria Libor (sem spread), o resultado só pode ser o valor do principal ou do nocional! Observemos a Figura 4.12:

Figura 4.25 | Swaps sem garantia e sem spread: NPV é igual ao nocional nas datas de reset da Libor
![img-43.jpeg](img-43.jpeg)
Fonte: Elaborada pelos autores.

Como na precificação desse tipo de swap, sem garantia e sem spread, o NPV das duas pontas do swap são iguais em módulo, podemos inferir que o módulo do NPV da ponta

---

pré-fixada também será igual ao notional ou ao principal do swap.

Agora, mostraremos a precificação de um swap Libor x pré-fixado pela seguinte tela da Bloomberg:

Figura 4.26 | Tela Bloomberg: precificação de swap Libor x pré-fixado sem garantia e sem spread
![img-44.jpeg](img-44.jpeg)
Fonte: Bloomberg (2017).

Na tela da Bloomberg, a taxa pré-fixada é determinada pelos parâmetros definidos no contrato, por exemplo:

- o NPV do swap é zero;
- não existe nenhum prêmio nem spread;
- os NPVs das pontas Libor e pré-fixadas são iguais em módulo;
- os módulos dos NPVs individuais de cada ponta são iguais ao notional do swap.

Outras informações relevantes desse swap:

---

- os fluxos de caixa da ponta pré-fixada são pagos semestralmente;
- os fluxos de caixa da ponta Libor são pagos trimestralmente, no seu reset;
- a taxa Libor do primeiro fluxo de caixa da ponta pós-fixada já está definida.

A partir dos parâmetros definidos no contrato, a Bloomberg precificou a taxa pré-fixada em 1,947954% ao ano. Como esse cálculo foi feito? Vamos mostrar replicando os cálculos em Microsoft Excel. Os quatro primeiros passos têm por objetivo calcular as taxas de desconto (discount factors), que são os fatores de descontos usados para trazer os fluxos de caixa ao valor presente, processo imprescindível tanto na precificação quanto na marcação a mercado do swap.

1. O primeiro passo é utilizar as taxas Libor indicadas pelo mercado no momento da precificação e fornecidas pela Bloomberg nas datas de reset dos fluxos de caixa atrelados à Libor. É importante entender que essas taxas Libor do exemplo são taxas forward de três meses, expressas ao ano — e não ao trimestre.

2. A partir das taxas Libor forward de três meses, calcular os fatores de capitalização de cada período pela seguinte fórmula:



FC_(Período) = Libor_(Período) × dc/360 + 1   (4.25)



Sendo:

FC_(Período): fator de capitalização no período, neste caso trimestral Libor_(Período): Libor de mercado para aquele trimestre, expressa na forma anual dc: dias corridos no período

3. A partir dos fatores de capitalização trimestrais, acumulá-los para obter os fatores de capitalização acumulados:



FC_(Acc) = ∏(1 até k) FC_(Período) · k   (4.26)



Em que o FC_(Acc), fator de capitalização acumulado, nada mais é do que o produtório dos fatores de capitalização de três meses.

---

4. De posse dos fatores de capitalização acumulados, calculamos os fatores de desconto (discount factors).



F D _t = 1/F C_(A c c) · t, (4. 2 7)



Dessa forma, para trazer os fluxos de caixa aos seus valores presentes, basta multiplicá-los pelos respectivos fatores de desconto.

O procedimento anteriormente descrito nesses quatro primeiros passos pode ser implementado no Microsoft Excel. Os números entre parênteses indicados nas colunas da Tabela 4.1 correspondem aos passos descritos.

Tabela 4.1 | Exemplo do cálculo das taxas de desconto

|  Libor de 3 meses (1) | Fator de capitalização no período (2) | Fator de capitalização acumulado(3) | Fator de desconto spot (4) | Dias corridos (no trimestre)  |
| --- | --- | --- | --- | --- |
|  1.32306% | 1.003418 | 1.003418 | 0.996594 | 93  |
|  1.52092% | 1.003760 | 1.007191 | 0.992861 | 89  |
|  1.60382% | 1.004054 | 1.011274 | 0.988852 | 91  |
|  1.68697% | 1.004311 | 1.015634 | 0.984607 | 92  |
|  1.75756% | 1.004540 | 1.020245 | 0.980157 | 93  |
|  1.83835% | 1.004494 | 1.024830 | 0.975772 | 88  |
|  1.88311% | 1.004812 | 1.029762 | 0.971098 | 92  |
|  1.89909% | 1.004853 | 1.034759 | 0.966408 | 92  |
|  1.92597% | 1.004975 | 1.039908 | 0.961624 | 93  |
|  1.97572% | 1.004884 | 1.044987 | 0.956950 | 89  |
|  2.02478% | 1.005174 | 1.050394 | 0.952023 | 92  |
|  2.07369% | 1.005299 | 1.055961 | 0.947005 | 92  |
|  2.07183% | 1.005467 | 1.061734 | 0.941855 | 95  |
|  2.11061% | 1.005042 | 1.067087 | 0.937130 | 86  |
|  2.14900% | 1.005492 | 1.072948 | 0.932012 | 92  |
|  2.18815% | 1.005714 | 1.079078 | 0.926717 | 94  |
|  2.19456% | 1.005669 | 1.085196 | 0.921493 | 93  |
|  2.22695% | 1.005320 | 1.090969 | 0.916616 | 86  |
|  2.25993% | 1.005901 | 1.097407 | 0.911239 | 94  |
|  2.29242% | 1.005795 | 1.103766 | 0.905989 | 91  |

---

Fonte: Elaborada pelos autores.

Uma vez calculados os fatores de capitalização e as taxas de desconto, vamos calcular os fluxos de caixa semestrais e seus valores presentes. Vamos começar pelos fluxos da ponta pré-fixada.

5. Para calcular os fluxos da ponta pré-fixada, basta aplicar a seguinte fórmula:



Fluxo_(Pré) = Nocional × Pré × dc/360   (4.28)



Sendo:

**Fluxo}_(Pré): valor do fluxo de caixa pré-fixado **Pré**: taxa pré-fixada no swap **dc**: dias corridos no período

Consideramos que no último fluxo de caixa haverá pagamento do nocional mais cupom de juros. Neste exemplo, o valor do nocional da ponta pré-fixada é positivo, pois estamos recebendo uma taxa pré-fixada.

Agora vamos calcular os fluxos de caixa da ponta Libor:

6. Para calcular os fluxos trimestrais da ponta Libor, basta aplicar a seguinte fórmula:



Fluxo_(Libor) = Nocional ( FC_(Período) - 1 )   (4.29)



Sendo:

**Fluxo}_(Pré): valor do fluxo de caixa pós-fixado **FC}_(Período): fator de capitalização no período

No último fluxo de caixa haverá pagamento do nocional mais cupom de juros.

Veremos agora a conveniência de termos calculado os fatores de desconto (discount factors). Para calcularmos os valores presentes dos fluxos de caixa, tanto do pré-fixado quanto do pós-fixado, basta multiplicarmos estes pelos respectivos fatores de desconto previamente calculados.

7. Para calcular os valores presentes dos fluxos de caixa, basta aplicar a seguinte fórmula:

---



V P_(F l u x o) = F l u x o × F D (4. 3 0)



Em que,

VP_(Fluxo) é o valor presente respectivo fluxo de caixa.

8. E, finalmente, para calcular o NPV do swap basta somar os valores presentes de ambas as pontas do swap. Neste momento, o NPV do swap está zero pelo nosso exemplo.

O procedimento anteriormente descrito do quinto ao oitavo passo pode ser implementado no Microsoft Excel. Os números entre parênteses indicados nas colunas da Tabela 4.2 correspondem aos passos descritos.

Tabela 4.2 | Exemplo do cálculo dos fluxos de caixa e seus valores presentes

|  Libor + spread | Dias corridos | Fluxo de caixa pré-fixado (recebe) (5) | Fluxo de caixa floating (paga) (6) | VP do fluxo pré-fixado (7) | VP do fluxo Libor (7) | NPV (8)  |
| --- | --- | --- | --- | --- | --- | --- |
|  1.32306% | 93 | 0.00 | -34,179.05 | 0.00 | -34,062.63 | -34,062.63  |
|  1.52092% | 89 | 98,479.91 | -37,600.52 | 97,776.81 | -37,332.07 | 60,444.74  |
|  1.60382% | 91 | 0.00 | -40,541.01 | 0.00 | -40,089.04 | -40,089.04  |
|  1.68697% | 92 | 99,021.00 | -43,111.46 | 97,496.76 | -42,447.83 | 55,048.92  |
|  1.75756% | 93 | 0.00 | -45,403.63 | 0.00 | -44,502.67 | -44,502.67  |
|  1.83835% | 88 | 97,938.81 | -44,937.44 | 95,565.92 | -43,848.69 | 51,717.23  |
|  1.88311% | 92 | 0.00 | -48,123.92 | 0.00 | -46,733.06 | -46,733.06  |
|  1.89909% | 92 | 99,562.10 | -48,532.30 | 96,217.63 | -46,902.01 | 49,315.62  |
|  1.92597% | 93 | 0.00 | -49,754.23 | 0.00 | -47,844.84 | -47,844.84  |
|  1.97572% | 89 | 98,479.91 | -48,844.19 | 94,240.30 | -46,741.43 | 47,498.88  |
|  2.02478% | 92 | 0.00 | -51,744.38 | 0.00 | -49,261.86 | -49,261.86  |
|  2.07369% | 92 | 99,562.10 | -52,994.30 | 94,285.79 | -50,185.86 | 44,099.93  |
|  2.07183% | 95 | 0.00 | -54,673.29 | 0.00 | -51,494.33 | -51,494.33  |
|  2.11061% | 86 | 97,938.81 | -50,420.13 | 91,781.43 | -47,250.23 | 44,531.20  |
|  2.14900% | 92 | 0.00 | -54,918.89 | 0.00 | -51,185.05 | -51,185.05  |
|  2.18815% | 94 | 100,644.30 | -57,135.03 | 93,268.79 | -52,948.00 | 40,320.78  |
|  2.19456% | 93 | 0.00 | -56,692.80 | 0.00 | -52,242.01 | -52,242.01  |
|  2.22695% | 86 | 96,856.61 | -53,199.36 | 88,780.37 | -48,763.41 | 40,016.96  |

---

|  2.25993% | 94 | 0.00 | -59,009.28 | 0.00 | -53,771.58 | -53,771.58  |
| --- | --- | --- | --- | --- | --- | --- |
|  2.29242% | 91 | 10,100,103.20 | -10,057,947.28 | 9,150,586.20 | -9,112,393.38 | 38,192.81  |
|   |  |  |  | 10,000,000.00 | -10,000,000.00 | 0.00  |

Fonte: Elaborada pelos autores.

Nesse exemplo usamos a convenção Actual/360 para a contagem de dias corridos em ambas as pontas do swap. No Microsoft Excel, digitamos a taxa pré-fixada do swap calculada pela Bloomberg, 1,947954. Caso quiséssemos obtê-la usando o Microsoft Excel, bastaria digitar uma taxa qualquer no cupom e, via "atingir meta", encontrá-la definindo que o NPV do swap é zero.

# 4.6.9 Precificando um swap Libor com garantia

Agora vamos mostrar como precificar um swap com garantia, ou seja, uma modalidade de swap que utiliza a taxa OIS como base de cálculo das taxas de desconto. Vamos analisar o exemplo definido na tela da Bloomberg:

Figura 4.27 | Tela Bloomberg: precificação de swap Libor x pré-fixado com garantia
![img-45.jpeg](img-45.jpeg)
Fonte: Bloomberg (2017).

---

Habilitando a funcionalidade "OIS DC Stripping", utilizaremos as taxas de desconto do swap calculadas a partir das expectativas das taxas OIS futuras. O sistema Bloomberg já faz esse cálculo:

Figura 4.28 | Tela Bloomberg: fluxos de caixa do swap com garantia
![img-46.jpeg](img-46.jpeg)
Fonte: Bloomberg (2017).

Veremos que como a taxa OIS é menor do que a taxa Libor e, consequentemente, os fatores de desconto OIS são maiores, o NPV em módulo das duas pontas de um swap com garantia aumenta. A título de comparação, segue a tela da Bloomberg com os fluxos de caixa de um swap com características idênticas, mas sem garantia. Ou seja, os fatores de desconto do swap sem garantia são menores, pois foram obtidos das taxas Libor. Aqui, a título de demonstração, optamos por definir o NPV no início da operação, no momento da

---

precificação, como zero: Figura 4.29 | Tela Bloomberg: fluxos de caixa do swap sem

![img-47.jpeg](img-47.jpeg)

Fonte: Bloomberg (2017).

Para implementar os cálculos em Microsoft Excel do swap com garantia, basta seguir os passos já demonstrados no swap sem garantia, porém, no swap com garantia, as taxas de desconto são calculadas a partir das taxas da curva OIS, e não da Libor.

Uma observação importante é que neste swap assumimos os padrões definidos pela tela da Bloomberg para a contagem de dias corridos: 30/360 para a ponta pré-fixada e Actual/360 para a ponta Libor. É importante entender as convenções vigentes na hora de operar este swap no mundo real.

No swap com garantia não podemos mais assumir que o módulo do NPV de cada uma das pontas é igual ao nocional, pois os fluxos de caixa são calculados a partir de taxas Libor e trazidos a valor presente por uma taxa OIS, que é menor do que a Libor.

# 4.6.10 Marcação a mercado do swap de Libor

Para marcar a mercado o swap de Libor basta trazer os valores projetados dos fluxos de caixa pelas taxas de desconto vigentes na data-base da apuração. Como os valores estão em moeda estrangeira, nos nossos exemplos, em dólar americano, é necessário o seguinte procedimento para adequar a marcação a mercado em reais:

---

1. Converter os fluxos de caixa em dólar para reais pelas taxas calculadas da curva de dólar futuro, de acordo com os prazos dos fluxos; 2. Trazer a valor presente os fluxos de caixa convertidos para reais pelas taxas de juros spot local, dada pela curva pré-fixada livre de risco brasileira.

## 4.6.11 O futuro da taxa Libor como indexador pós-fixado

Até o momento, vimos como o mercado se adequou após constatar que a taxa Libor pode não ser uma boa proxy da taxa livre de risco. Nesse caso, passamos a utilizar as taxas OIS como alternativa para as taxas livre de risco. De acordo com o artigo de Hull e White, "Libor vs. OIS: the derivatives discounting dilemma", o racional utilizado para o uso das taxas OIS como proxy da taxa livre de risco para os derivativos com garantia, collateralized, é que o derivativo lastreado pela garantia tem um rendimento próximo da effective funds rate. Para derivativos sem garantia, ainda se assume a taxa Libor como sendo a taxa para calcular os fatores de desconto desses derivativos. Em seu artigo, Hull e White, argumentam que a taxa OIS deveria ser usada como a proxy da taxa livre de risco em todas as situações, seja o derivativo com ou sem garantia.

Discussões ainda mais impactantes estão ocorrendo sobre quais taxas devem substituir as taxas Libor. Agora a discussão não é mais se a Libor pode ser considerada como uma taxa livre de risco, ou seja, a taxa de cálculo dos fatores de desconto. O que alguns reguladores vêm questionando é se a taxa Libor é uma taxa legítima, ou suficientemente íntegra, para ser usada para desconto de valores monetários. Isso gera algumas perguntas, como quais as taxas que deverão substituir a Libor? Como o mercado aceitará um potencial fim da taxa Libor? No momento em que escrevemos este livro, essas perguntas ainda estão sem repostas.

## RESUMO

Neste capítulo definimos o que é um swap e o racional de se utilizar esse produto em algumas operações de hedge. Tratamos da precificação e marcação a mercado desses swaps. Primeiro, tratamos de alguns exemplos contextualizados ao mercado brasileiro. Optamos por abordar os swaps de Libor, pelos seguintes motivos: 1. Importância do produto nos mercados internacional e brasileiro; 2. O impacto profundo da crise de 2007 na precificação e marcação mercado de derivativos; 3. Carência de literatura local sobre o tema, principalmente que trata pós crise de 2007.

---

EXERCÍCIOS PROPOSTOS

1. Uma montadora de veículos possui um passivo de US$ 7 milhões referente a exigíveis de importação que irá saldar em 7 meses, a empresa, para se proteger contra os riscos cambiais, pode: a. Vender dólar a termo para 7,2 meses.
b. Comprar futuro de dólar na B3, que não exige garantias.
c. Fazer um empréstimo em reais e investir em um ativo financeiro que rende a variação cambial mais um cupom.
d. Aguardar o melhor momento para fazer hedge.
e. Fazer um empréstimo em dólares e pagar o passivo de importação.

Para responder as questões seguintes utilize as informações a seguir:

Considere as seguintes taxas do DI e dólar futuro cotados no dia de hoje e os respectivos prazos até o vencimento:

|   | Taxa DI % a.a.o. | US | dias úteis | dias corridos  |
| --- | --- | --- | --- | --- |
|  Jan. | 14,40 | 3.640 | 15 | 21  |
|  Fev. | 14,60 | 3.647 | 37 | 53  |
|  Mar. | 14,84 | 3.652 | 56 | 80  |
|  Abr. | 15,10 | 3.658 | 77 | 110  |
|  Maio | 15,45 | 3.660 | 98 | 140  |

Dólar Ptax 800 na data de hoje: 3,620 R/US

Uma empresa tem um compromisso daqui a 56 d.u. de US$ 500.000,00 e deseja converter esse compromisso, utilizando um swap, para reais, a uma taxa pré-fixada.

2. A que taxa deve ser fechado o swap (over ano)? (Assuma a taxa de mercado): a. 6,41 % a.a.o.
b. 2,27 % a.a.o.
c. 1,32 % a.a.o.
d. 4,04 % a.a.o.
e. 9,47 % a.a.o.

3. O valor do principal (nocional) da operação em reais, na data de registro: a. R$ 1.750.000
b. R$ 1.810.000
c. US$ 500.000
d. R$ 1.753.345,23
e. Não é possível calcular

---

4. No vencimento do swap o dólar PTAX 800 está a 3,67 R/US. Qual será o valor de ajuste, líquido de IR? (alíquota de IR = 22,5%)?

a. R$ 5.246,23
b. R$ 3.451,27
c. R$ 1.879,21
d. R$ 6.974,67
e. R$ 14.320,22

5. Imagine que a empresa não consiga fechar o swap dólar x Pré de 56 d.u. anteriormente descrito, pois está sem liquidez. Decide fechar, então, um swap dólar x DI no valor de mercado e 100% de CDI, para o mesmo vencimento. A taxa deve ser: a. Dólar + 3,29% a.a.

b. Dólar + 9,99% a.a.
c. Dólar + 14,2% a.a.
d. Dólar + 23,5% a.a.
e. Dólar + 1,23% a.a.

6. A empresa decide converter seu passivo em taxa flutuante (DI) para um passivo pré-fixado, utilizando um swap DI x Pré com vencimento em 56 d.u. Utilizando a curva de mercado, qual deve ser a taxa de negociação do swap?

a. 13,56% a.a.o.
b. 14,84% a.a.o.
c. 12,98% a.a.o.
d. 11,12% a.a.o.
e. 21,39% a.a.o.

7. Swap DI x dólar. Uma empresa exportadora tem um recebível de US$ 15 milhões no prazo de 80 dias corridos (56 dias úteis) e deseja converter esse ativo em uma taxa em reais pós-fixada (DI). A empresa recebe a seguinte cotação de um banco para fazer um swap dólar x DI: o banco aceita receber dólar (variação cambial) + 4,00% a.a. e pagar 100% do DI para o prazo do recebível da empresa. Assumindo que a taxa de câmbio atual (de referência no início da operação) seja 3,25, calcule o resultado desse swap caso a taxa de câmbio no vencimento seja 3,20 e que o DI apurado no período foi 14% a.a.o.

8. Swap DI x Pré. Uma empresa decide converter seu passivo em taxa flutuante (DI) em um passivo pré-fixado utilizando um swap DI x Pré com vencimento em 55 dias úteis. Com base nas cotações a seguir (curva de mercado de DI futuro da B3), qual deve ser a taxa de negociação (sem spread) do swap?

|  Cód. | Vencimento | du | dc | DI 1 dia  |
| --- | --- | --- | --- | --- |
|  K15 | 04-maio-2015 | 14 | 24 | 99.341,90  |
|  M15 | 01-jun.-2015 | 34 | 52 | 98.384,54  |
|  N15 | 01-jul.-2015 | 55 | 82 | 97.368,38  |

---

9. Swap dólar x Pré. Uma empresa tem um passivo em dólar de US$ 10 milhões, com vencimento em 45 dias corridos (34 dias úteis) e deseja eliminar esse risco cambial por meio de um swap dólar x Pré. Assuma que o banco (contraparte) aceita receber uma taxa pré de 4,80% a.a.o. para fechar a operação para fazer o hedge cambial da empresa e que a taxa de câmbio atual (de preferência no início da operação) seja 3,25.

a. Descreva como seria essa operação de swap para que a empresa elimine o risco cambial de seu passivo.
b. Assumindo que o swap tenha sido fechado com o banco, qual será o resultado desse swap caso a taxa de câmbio no vencimento seja 3,40?

10. Na precificação e marcação a mercado dos swaps de Libor versus pré-fixado calculamos os fatores de desconto (discount factors). Qual o papel dos discount factors no cálculo da precificação e marcação a mercado desses swaps?

11. Qual a justificativa de se utilizar as taxas OIS para calcular os fatores de desconto (discount factors) em vez das taxas Libor nos swaps Libor versus pré-fixado?

12. Em quais circunstâncias são utilizadas as taxas OIS para calcular os fatores de desconto dos swaps? E as taxas Libor?

1LFT (Letra Financeira do Tesouro) é um título pós-fixado em reais que possui um único fluxo de pagamento, no vencimento. O seu rendimento é atrelado à taxa Selic.

---

CAPITULO 5

# Mercado de opções

---

# 5.1 História das opções

De acordo com os registros de Copeland e Antikarov (2001, p. 7), a mais antiga opção registrada pela história está narrada entre os escritos de Aristóteles, a história de Tales, filósofo sofista. Tales, interpretando as folhas de chá, previu uma colheita abundante de azeitonas, pegou suas economias e negociou com os donos das prensas de azeite, pagando-lhes pelo direito de alugar as prensas por um preço preestabelecido no período de colheitas.

Como previsto por Tales, a safra superou as expectativas. Tales pagou o valor anteriormente combinado pelo aluguel das prensas, mas cobrou dos plantadores um preço mais elevado para a extração do precioso azeite.

De acordo com Gastineau (1979, p. 14), os gregos não foram os únicos a utilizar opções; os fenícios e os romanos utilizavam opções para negócios feitos com os carregamentos de seus navios. O uso extensivo de opções ocorreu após a Idade Média, no começo do século 17, com as lavouras de tulipa na Holanda.

Os produtores de tulipa pagavam prêmios aos comerciantes para ter o direito de vender sua produção a um preço predeterminado, garantindo um preço mínimo para as suas tulipas. As opções sobre tulipas eram um tipo de venda a termo com o pagamento de prêmio inicial, similar a uma opção de venda.

Segundo Gastineau (1979), o mercado de opções de tulipa era desorganizado, e os produtores não tinham garantia de que os comerciantes realmente honrariam a compra do produto no vencimento da opção. O mercado de opções de tulipas na Holanda quebrou no inverno de 1637, pois os comerciantes recusaram-se a pagar os preços determinados pelas opções. Os produtores lesados recorreram ao Conselho Provençal de Haia, para tentar restabelecer a credibilidade do mercado de tulipas, mas a decisão da corte foi complacente com a inadimplência dos comerciantes, que nunca foram intimados a honrar seus compromissos. Ironicamente, a Holanda continuou a utilizar opções mesmo após a quebra do mercado de tulipas. Poucos anos depois, opções sobre cotas da Companhia Holandesa da Índia Ocidental começaram a ser negociadas.

---

No final do século 17, em Londres, tiveram início os primeiros negócios de opções sobre ações. O uso do novo instrumento, na época, era considerado uma atividade puramente especulativa e, com a pressão de alguns participantes do mercado de ações, as opções foram consideradas uma atividade ilegal, em 1733, pelo Ato de Barnard, sendo revogado apenas em 1860. Após a revogação, o mercado de opções permaneceu ativo em Londres somente até a crise de 1931, quando o instrumento foi temporariamente banido.

O mercado de opções nos Estados Unidos teve seu início no final do século 18, com um agiota chamado Russell Sage, que emprestava dinheiro a taxas elevadas. Sage exigia títulos como garantia pelos empréstimos que fazia, e vendia aos seus devedores uma opção de compra, que dava o direito aos endividados de reaverem seus títulos a um preço predeterminado. O prêmio da opção representava o ganho de Sage na operação.

O mercado de opções de ações nos Estados Unidos, segundo Gastineau (1979, p. 16), contribuiu para a crise de 1929. Pequenos investidores foram vítimas de corretores de ações entusiasmados que faziam recomendações de compra de opções pouco fundamentadas para a época. Esses abusos acabaram depois que rigorosas leis foram aplicadas no mercado de capitais norte-americano pós-crise.

Copeland e Weston (1988, p. 240) afirmam que o primeiro mercado organizado de opções foi desenvolvido em 26 de abril de 1973 na Bolsa de Chicago (CBOE¹). No ano seguinte ao lançamento do instrumento, o volume de transações na CBOE era superior ao volume de operações com ações.

A Bolsa de Valores de São Paulo (BOVESPA) foi a primeira a introduzir, no Brasil, no final da década de 1970, as operações com opções sobre ações.

## 5.2 Estrutura de uma opção

---

Opção pode ser definida como um contrato que propicia aos seus detentores o direito de compra ou venda de um ativo determinado a um preço preestabelecido em um prazo determinado. Seria equivalente a dizer que um indivíduo tem a vantagem de optar pela compra ou venda de um ativo específico em uma data futura, sabendo de antemão o preço que irá pagar ou receber pelo ativo, tendo a garantia de que a contraparte será obrigada a realizar o negócio no futuro, dentro de especificações rezadas em contrato.

No contrato de opção, apenas uma das partes envolvidas possui o direito, e não a obrigação, de exercer a liquidação do contrato no vencimento. Essa característica distingue a opção de um contrato a termo, no qual as duas partes envolvidas têm a obrigação de liquidar o contrato em data prevista.

A parte que possui o direito de decisão é denominada titular da opção, enquanto que a contraparte que assume a obrigação de cumprir o contrato, caso assim seja determinado pelo titular, é denominada lançador da opção.

Há dois tipos de opção: opção de compra (call), que dá direito ao titular de comprar um determinado ativo a preço e prazo preestabelecidos; e opção de venda (put), que dá ao titular o direito de vender o ativo.

O titular da opção, na maioria dos casos, precisa pagar um determinado valor ao lançador da opção, referente à vantagem que ele obtém na decisão de liquidação. Esse valor é denominado prêmio ou preço da opção. Portanto, o titular da opção é detentor do direito de exercer a liquidação, mediante pagamento de prêmio ao lançador, que tem obrigação de vender ou comprar no exercício, caso solicitado pelo titular.

Wilmott (1998, p. 26) define algumas das características dos contratos de opção:

- Prêmio – valor pago inicialmente pelo direito de exercer o contrato, no caso de opção de compra é representado por c, e opção de venda por p.
- Ativo subjacente – ativo no qual o valor da opção é referenciado, representado por S, podendo ser ações, taxas de câmbio, taxas de juros, imóveis, veículos, produtos agrícolas, desde "... o preço de suínos vivos até a quantidade de neve numa estação de esqui" (HULL, 1998, p. 1).

---

- Vencimento – data-limite do prazo no qual a opção fica vigente, data na qual a opção deixa de existir e de dar direitos ao seu detentor, denotado como t.
- Preço de exercício – preço preestabelecido de liquidação da opção, representado por K.
- Valor intrínseco – pagamento que o titular da opção poderá receber no vencimento, caso exerça seu direito, ou seja, se a compra ou a venda ocorrer de fato.
- “Dentro do dinheiro” – ocorre quando o valor intrínseco da opção é positivo. Na opção de compra ocorre quando o preço do ativo subjacente é superior ao preço de exercício da opção.
- “Fora do dinheiro” – ocorre quando a opção não possui nenhum valor intrínseco. No caso da opção de compra, quando o valor do ativo subjacente é inferior ao preço de exercício da opção.
- “No dinheiro” – ocorre quando o preço do ativo subjacente é igual ao preço de exercício.
- Posição comprada – uma quantidade positiva de determinado contrato.
O titular da opção sempre está em uma posição comprada com relação ao prêmio.
- Posição vendida – uma quantidade negativa de determinado contrato.
Posição do lançador com relação ao prêmio da opção.

A Figura 5.1 representa uma operação com opção de compra até a data de exercício, na qual o preço do ativo subjacente no vencimento, representado por S_t, é superior ao preço de exercício. O titular da opção, nesse caso, exerce seu direito de compra do ativo pelo preço de exercício, realizando um lucro.

Figura 5.1 | Exemplo de opção

---

![img-48.jpeg](img-48.jpeg)
Fonte: Elaborada pelos autores.

O contrato de opção, no qual o titular pode exercer seu direito a qualquer momento até o vencimento, é definido como do tipo americano. Quando o direito pode ser exercido somente na data de vencimento, é definido como do tipo europeu.

# 5.3 Entendendo ganhos e perdas nas posições de opções

Antes de abordarmos o Modelo Black e Scholes (1973), é útil entender o cálculo dos resultados das posições em opções no seu vencimento. Esse cálculo é simplificado, pois não considera o valor do dinheiro no tempo. Entretanto, os cálculos que veremos neste capítulo são muito intuitivos sobre o que ocorre em termos de ganhos e perdas em cada posição de opção em função dos diferentes preços que o ativo-objeto, S_t, possa assumir no vencimento. Outra vantagem dos cálculos dos resultados que veremos é que não é necessário utilizar nenhum modelo matemático complexo e nenhuma premissa estatística, basta um pouco de aritmética.

Entenderemos o que ocorre nas quatro situações possíveis de serem assumidas com opções: comprado em call, vendido em call, comprado em put e vendido em put. Para simplificar, assumiremos que as posições são compostas por uma unidade de contrato de opção. Quando mostrarmos as principais estratégias com opções, generalizaremos os cálculos para posições

---

compostas por mais de um contrato da mesma opção. Também assumiremos que estamos tratando com posições de opções do tipo europeias.

## 5.3.1 Ganhos e perdas - Comprado em call

Vejamos como calcular o resultado de uma posição comprada em uma call, +C (o "+" representa a compra da opção), no seu vencimento:



R_(+C) = Max[S_t - K; 0] - c   (5.1)



O que a Equação 5.1 está nos mostrando é que o resultado da posição comprada em call, R_(+C), é a diferença entre o preço do ativo-objeto no vencimento da opção, S_t, menos o preço de exercício, K, considerando o prêmio pago pela opção, c.

O comprador de uma opção de compra não poderá perder mais do que o prêmio pago, c. Logo, se a diferença entre o preço do ativo-objeto no vencimento e o preço de exercício for negativa, ou seja, o preço do ativo-objeto for menor do que o preço de exercício, assume-se que o resultado desta diferença é zero, pois esta opção não será exercida nesta condição. Daí o racional do termo Max[S_t - K; 0]. Ou seja, se S_t - K for negativo, uma perda para o comprador da call, assume-se o resultado como sendo zero. Quando incluímos o preço pago pela call, c, para completarmos a Equação 5.1, constatamos que realmente a perda máxima para o comprador da call é o valor pago pela opção, seu prêmio.

A figura 5.2 representa o resultado da posição comprada em call considerando diferentes níveis de preços do ativo-objeto no vencimento:

---

Figura 5.2 | Resultado de posição comprada em uma call
![img-49.jpeg](img-49.jpeg)
Fonte: Elaborada pelos autores.

Na Figura 5.2 podemos observar que o comprador da call se beneficia quando o preço do ativo-objeto aumenta. A linha horizontal da Figura 5.2 mostra um resultado negativo para o comprador da call, pois representa o prêmio pago pela call. O ponto de equilíbrio da posição ocorre quando o preço do ativo-objeto no vencimento aumenta suficientemente para cobrir o valor pago pelo prêmio da opção.

# 5.3.2 Ganhos e perdas - Vendido em call

Vejamos como calcular o resultado de uma posição vendida em uma call, -C (o sinal negativo representa a venda da opção), no seu vencimento:



R_(-C) = -\{Max[S_t - K; 0] - c\}   (5.2)



Ou seja, o resultado da posição vendida em call é o oposto da posição comprada em call.

O ganho do titular da call é a perda para o vendedor da call e vice-versa, por isso o sinal negativo antes das chaves. Reescrevendo a Equação 5.2 para torná-la mais intuitiva, teremos:



R_(-C) = -Max[S_t - K; 0] + c   (5.3)



---

Para obter um ganho na posição vendida em call, é necessário que o preço do ativo--objeto no vencimento seja menor do que o preço de exercício mais o prêmio. O ganho máximo do lançador da call será o prêmio, que ocorrerá caso o preço do ativo-objeto no vencimento seja menor do que o preço de exercício da opção.

A Figura 5.3 representa o resultado da posição vendida em call considerando diferentes níveis de preços do ativo-objeto no vencimento:

Figura 5.3 | Resultado de posição vendida em uma call
![img-50.jpeg](img-50.jpeg)
Fonte: Elaborada pelos autores.

Na Figura 5.3 podemos notar que o vendedor da call se beneficia quando o preço do ativo-objeto cai. A linha horizontal mostra um resultado positivo para o vendedor da call, pois representa o prêmio recebido. O ponto de equilíbrio da posição ocorre quando o preço do ativo-objeto no vencimento aumenta suficientemente para consumir o valor recebido pelo prêmio da opção.

# 5.3.3 Ganhos e perdas - Comprado em put

Vejamos como calcular o resultado de uma posição comprada em uma put, +P, no seu vencimento:

---



R_(+p) = Max[K - S_t; 0] - p   (5.4)



A Equação 5.4 nos mostra que o resultado da posição comprada em put, R_(+p), é a diferença entre o preço de exercício, K, e o preço do ativo-objeto no vencimento da opção, S_t, considerando o prêmio pago pela opção, P.

O comprador de uma opção de venda não poderá perder mais do que o prêmio pago, p. Logo, se a diferença entre o preço de exercício e o preço do ativo-objeto no vencimento for negativa, ou seja, o preço do ativo-objeto for maior do que o preço de exercício, assume-se que o resultado desta diferença é zero, pois esta opção não será exercida nesta condição. Daí o racional do termo Max[K - S_t; 0]. Ou seja, se K - S_t for negativo, uma perda para o comprador da put, assume-se este resultado como sendo zero. Quando incluímos o preço pago pela put, p, para completarmos a Equação 5.4, constatamos que realmente a perda máxima para o comprador da put é o valor pago pela opção, seu prêmio.

A Figura 5.4 representa o resultado da posição comprada em put considerando diferentes níveis de preços do ativo-objeto no vencimento:

Figura 5.4 | Resultado de posição comprada em uma put
![img-51.jpeg](img-51.jpeg)
Fonte: Elaborada pelos autores.

Na Figura 5.4 podemos ver que o comprador da put se beneficia quando o preço do ativo-objeto diminui. A linha horizontal do gráfico mostra um resultado negativo para o comprador da put, pois representa o prêmio pago pela opção. O breakeven da posição ocorre quando o preço do ativo-objeto no vencimento diminui suficientemente para cobrir o valor pago pelo prêmio da opção.

---

# 5.3.4 Ganhos e perdas - Vendido em put

Vejamos como calcular o resultado de uma posição vendida em uma put, -P no seu vencimento:



R_(-p) = -\{ max [K - S_t; 0] - p\}   (5.5)



Ou seja, o resultado da posição vendida em put é o oposto da posição comprada em put. O ganho do titular da put é a perda para o vendedor da put e vice-versa, por isso o sinal negativo antes das chaves. Reescrevendo a equação anterior teremos:



R_(-p) = - max [K - S_t; 0] + p   (5.6)



O ganho máximo do lançador da put será o prêmio recebido pela venda da opção e ocorrerá caso o preço do ativo-objeto no vencimento for maior do que o preço de exercício da opção.

A Figura 5.5 a seguir representa o resultado da posição vendida em put considerando diferentes níveis de preços do ativo-objeto no vencimento:

Figura 5.5 | Resultado de posição vendida em uma put
![img-52.jpeg](img-52.jpeg)
Fonte: Elaborada pelos autores.

Na Figura 5.5 podemos observar que o vendedor da put se beneficia quando o preço do ativo-objeto aumenta. A linha horizontal mostra um

---

resultado positivo para o vendedor da put, pois representa o prêmio recebido. O ponto de equilíbrio da posição ocorre quando o preço do ativo-objeto no vencimento cai suficientemente para consumir o valor recebido pelo prêmio da opção.

# 5.4 Ganhos e perdas de estratégias direcionais básicas com opções

Agora que entendemos os cálculos dos resultados de cada uma das possíveis posições que podemos assumir no mercado de opções, vamos apresentar o racional de algumas estratégias direcionais que podemos fazer com esses instrumentos. Calcularemos os resultados das estratégias e montaremos seus gráficos.

# 5.4.1 Financiamento

Financiamento consiste em montar uma renda fixa com risco, ou seja, uma operação com um ganho relativamente certo se utilizarmos uma call deep in the money. A posição é equivalente a estar comprado em um título de renda fixa e vendido em uma put sintética.

Podemos resumir essa estratégia com a seguinte notação, [+S_0; -C]. Ou seja, compra do ativo-objeto no instante zero e venda simultânea de uma call. Vejamos um exemplo desta estratégia:

- Compra de uma ação a R$ 36,00. Na convenção da notação, +S36;
- Venda de uma call com o preço de exercício de R$ 38,00 a R$ 1,00. Na convenção da notação, -C38.

---

Podemos, então, resumir essa estratégia pela segunte notação: [+S36; -C38]. Para calcularmos o resultado da estratégia, basta calcular o resultado de cada uma de suas posições para diferentes níveis de preços do ativo-objeto no vencimento, S_t. Mostraremos as fórmulas genéricas dos cálculos dos resultados de cada uma das posições, ou seja, considerando as quantidades, Q. Até então vínhamos calculando os resultados assumindo um contrato da opção. Implementaremos os cálculos no Microsoft Excel, assim como os gráficos.

Vamos considerar a fórmula a seguir para calcular o resultado da posição +S_0:



R_(+S_0) = Q(S_t - S_0)   (5.7)



Ou seja, o resultado da posição do ativo-objeto no vencimento da opção será a diferença de preço do ativo-objeto no vencimento da opção menos o valor pago por este no instante zero, considerando a quantidade.

Vejamos a fórmula a seguir para calcular a posição -C38 vendida a R$ 1,00 (prêmio, c):



R_(-C) = -Q Max [S_t - K; 0] + Qc   (5.8)



Observe a Tabela 5.1 a seguir, do resultado da estratégia de financiamento de opção, para dados preços do ativo-objeto, na coluna à direita está o resultado da estratégia. Quando o preço da ação estiver em R$ 35,00, o resultado da estratégia será igual a zero:

Tabela 5.1 | Resultado do exemplo de financiamento

|   | St | +S36 | -C38 | Estratégia  |
| --- | --- | --- | --- | --- |
|   | 20 | -16 | 1 | -15  |
|   | 22 | -14 | 1 | -13  |
|   | 24 | -12 | 1 | -11  |

---

|   | 26 | -10 | 1 | -9  |
| --- | --- | --- | --- | --- |
|   | 28 | -8 | 1 | -7  |
|   | 30 | -6 | 1 | -5  |
|   | 32 | -4 | 1 | -3  |
|   | 34 | -2 | 1 | -1  |
|  breakeven | 35 | -1 | 1 | 0  |
|   | 36 | 0 | 1 | 1  |
|   | 38 | 2 | 1 | 3  |
|   | 40 | 4 | -1 | 3  |
|   | 42 | 6 | -3 | 3  |
|   | 44 | 8 | -5 | 3  |
|   | 46 | 10 | -7 | 3  |

Fonte: Elaborada pelos autores.

O ponto de equilíbrio pode ser calculado de forma algébrica, geométrica, ou convenientemente, via o algoritmo "atingir meta" do Microsoft Excel.

A Figura 5.6 a seguir apresenta o resultado do financiamento de opção. Nessa figura e nas seguintes de estratégias direcionais, o eixo vertical denota o resultado financeiro da estratégia, enquanto que o eixo horizontal representa os preços do ativo-objeto:

Figura 5.6 | Resultado do exemplo de financiamento de opção
![img-53.jpeg](img-53.jpeg)
Fonte: Elaborada pelos autores.

---

O racional dessa estratégia é financiar parte da compra do ativo-objeto por meio de uma venda de call. Alternativamente, essa estratégia tem o mesmo racional que uma venda de put. Ao adotar essa estratégia o investidor tem a expectativa de que o preço do ativo-objeto no vencimento seja maior do que R$ 35,00.

Se quando estamos comprados no ativo-objeto e vendidos em uma call, o resultado será vendido em uma put. O que podemos fazer para hedgear essa posição?

Para hedgear a posição, podemos comprar uma put europeia, de mesmo preço de exercício e vencimento da call. Ao fazermos isso, teremos, como resultado, uma operação livre de risco, equivalente a uma renda fixa, cujo valor futuro será o strike da opção. A taxa de juros obtida na operação será o equivalente a: 
rT = ln (K/S_0 - c + p)
 (5.9) Supondo que r é uma taxa livre de risco, podemos calcular o preço da put, dado o prêmio da call, essa relação é denominada como put-call parity:



p = K/e^(r T) - S ₀ + c tag {5.10}



## Exemplo 5.1 - Put-call parity

Utilizando os dados do financiamento do exemplo anterior, mas sabendo que a opção vence daqui a 21 dias úteis, e que a taxa de juros, está a 7\% a.a. na forma contínua, qual deverá ser o preço da put, em condição de não arbitragem? Podemos calcular da seguinte forma:



p = 38/e^(r u m (21/p r o)/3 6 + 1) - 36 + 1 = 2,78



Logo, o prêmio da put deveria ser R$ 2,78, supondo a ausência de risco de liquidação ou crédito.

---

# 5.4.2 Bull call spread

O bull call spread ou trava de alta com call é uma estratégia na qual se compra uma call de um determinado preço de exercício e se vende uma call, do mesmo ativo-objeto, por um preço de exercício maior do que a da call comprada. Quando essa operação é registrada em bolsa, não haverá chamada de margem, pois entende-se que, se a call de strike maior for exercida, a de strike menor também será. Logo, o investidor nesse tipo de estratégia não ficará vendido a descoberto no ativo.

Vamos entender também que essa é uma operação de barateamento da compra de opção, com a limitação de ganhos no caso de uma alta excessiva do ativo-objeto.

Vejamos um exemplo desta estratégia:

- Compra de uma call com o preço de exercício de R$ 38,00 a R$ 1,00. Na convenção da notação, +C38.
- Venda de uma call com o preço de exercício de R$ 40,00 a R$ 0,25. Na convenção da notação, -C40.

Podemos resumir essa estratégia pela seguinte notação, [+C38; -C40].

Vamos considerar a seguinte fórmula para calcular o resultado da posição +C38, comprada a R$ 1,00 (prêmio, c):



R_(+C) = QMax [ S_t - K; 0 ] - Qc \ (5.11)



E a fórmula para calcular a posição -C40, vendida a R$ 0,25 (prêmio, c):



R_(-C) = -QMax [ S_t - K; 0 ] + Qc \ (5.12)



---

Vejamos agora a Tabela 5.2 com o resultado da estratégia de bull call spread:

Tabela 5.2 | Resultado do exemplo de bull call spread

|   | St | +C38 | -C40 | Estratégia  |
| --- | --- | --- | --- | --- |
|   | 20 | -1,00 | 0,25 | -0,75  |
|   | 22 | -1,00 | 0,25 | -0,75  |
|   | 24 | -1,00 | 0,25 | -0,75  |
|   | 26 | -1,00 | 0,25 | -0,75  |
|   | 28 | -1,00 | 0,25 | -0,75  |
|   | 30 | -1,00 | 0,25 | -0,75  |
|   | 32 | -1,00 | 0,25 | -0,75  |
|   | 34 | -1,00 | 0,25 | -0,75  |
|   | 36 | -1,00 | 0,25 | -0,75  |
|   | 38 | -1,00 | 0,25 | -0,75  |
|  breakeven | 38.75 | -0,25 | 0,25 | 0,00  |
|   | 40 | 1,00 | 0,25 | 1,25  |
|   | 42 | 3,00 | -1,75 | 1,25  |
|   | 44 | 5,00 | -3,75 | 1,25  |
|   | 46 | 7,00 | -5,75 | 1,25  |

Fonte: Elaborada pelos autores.

O resultado gráfico dessa estratégia é apresentado na Figura 5.7 a seguir:

---

Figura 5.7 | Resultado do exemplo de bull call spread
![img-54.jpeg](img-54.jpeg)
Fonte: Elaborada pelos autores.

Essa é uma estratégia direcional, na qual existe uma expectativa de alta no preço do ativo-objeto. Porém, o ganho na alta é limitado, pois parte do prêmio da +C38 foi financiado com o prêmio da -C40.

# 5.4.3 Bear call spread

O bear call spread ou trava de baixa com call é uma estratégia na qual se vende uma call de um determinado preço de exercício e se compra uma call, do mesmo ativo-objeto, por um preço de exercício maior do que a da call vendida. Essa estratégia pode ser considerada como uma reversão do bull call spread, quando negociada em bolsa, pode gerar chamada de margem, pois pode ficar vendida a descoberto.

Nessa estratégia, o investidor está apostando na baixa no preço do ativo, porém com um ganho limitado.

Vejamos um exemplo desta estratégia:

---

- Venda de uma call com o preço de exercício de R$ 38,00 a R$ 1,00. Na convenção da notação, -C38;
- Compra de uma call com o preço de exercício de R$ 40,00 a R$ 0,25. Na convenção da notação, +C40.

Podemos resumir essa estratégia pela seguinte notação, [-C38; +C40].

Vamos considerar a seguinte fórmula para calcular o resultado da posição - C38:



R_(-C) = -QMax[S_t - K;0] + Qc(5.13)



E a fórmula para calcular a posição +C40, vendida a R$ 0,25 (prêmio, c) é:



R_(+C) = QMax[S_t - K;0] - Qc(5.14)



A Tabela 5.3 apresenta o resultado da estratégia bear call spread para diversos preços do ativo-objeto.

Tabela 5.3 | Resultado do exemplo de bear call spread

|   | St | -C38 | +C40 | Estratégia  |
| --- | --- | --- | --- | --- |
|   | 20 | 1,00 | -0,25 | 0,75  |
|   | 24 | 1,00 | -0,25 | 0,75  |
|   | 26 | 1,00 | -0,25 | 0,75  |
|   | 28 | 1,00 | -0,25 | 0,75  |
|   | 30 | 1,00 | -0,25 | 0,75  |
|   | 32 | 1,00 | -0,25 | 0,75  |
|   | 34 | 1,00 | -0,25 | 0,75  |
|   | 36 | 1,00 | -0,25 | 0,75  |

---

|   | 38 | 1,00 | -0,25 | 0,75  |
| --- | --- | --- | --- | --- |
|  breakeven | 38,75 | 0,25 | -0,25 | 0,00  |
|   | 40 | -1,00 | -0,25 | -1,25  |
|   | 42 | -3,00 | 1,75 | -1,25  |
|   | 44 | -5,00 | 3,75 | -1,25  |
|   | 46 | -7,00 | 5,75 | -1,25  |

Fonte: Elaborada pelos autores.

Na Figura 5.8, podemos notar que o resultado positivo está abaixo de R$ 38,75 (ponto de equilíbrio), porém é um ganho limitado:

Figura 5.8 | Resultado do exemplo de bear call spread
![img-55.jpeg](img-55.jpeg)
Fonte: Elaborada pelos autores.

Essa é uma estratégia direcional, na qual existe uma expectativa de queda no preço do ativo-objeto. Porém, o ganho na queda é limitado, como o prêmio da opção +C40 é menor do que o prêmio da -C38, essa é uma estratégia geradora de caixa.

---

# 5.4.4 Strangle

O strangle é uma estratégia na qual se compra uma call de um determinado preço de exercício e se compra uma put, do mesmo ativo-objeto, de um preço de exercício diferente da call. O objetivo dessa estratégia é obter ganhos com o movimento do preço do ativo, na alta ou na baixa. Se o preço do ativo ficar estável, haverá perda limitada.

Vejamos um exemplo desta estratégia:

- Compra de uma call com o preço de exercício de R$ 26,00 a R$ 1,00. Na convenção da notação, +C26.
- Compra de uma put com o preço de exercício de R$ 28,00 a R$ 1,80. Na convenção da notação, +P28.

Podemos resumir essa estratégia pela seguinte notação, [+C26; +P28].

Vamos considerar a seguinte fórmula para calcular o resultado da posição +C26:



R_(+C) = QMax [ S_t - K; 0 ] - Qc \ (5.15)



E a fórmula para calcular a posição +P28, comprada a R$ 1,80 (prêmio, P) é:



R_(+P) = QMax [ K - S_t; 0 ] - Qp \ (5.16)



O resultado na Tabela 5.4 é igual a soma de cada resultado individual, essa estratégia possui dois pontos de equilíbrio, na alta e na baixa.

---

Tabela 5.4 | Resultado do exemplo de strangle

|   | St | +C26 | +P28 | Estratégia  |
| --- | --- | --- | --- | --- |
|   | 20 | -1,00 | 6,20 | 5,20  |
|   | 22 | -1,00 | 4,20 | 3,20  |
|   | 24 | -1,00 | 2,20 | 1,20  |
|  breakeven | 25,2 | -1,00 | 1,00 | 0,00  |
|   | 26 | -1,00 | 0,20 | -0,80  |
|   | 28 | 1,00 | -1,80 | -0,80  |
|  breakeven | 28,8 | 1,80 | -1,80 | 0,00  |
|   | 30 | 3,00 | -1,80 | 1,20  |
|   | 32 | 5,00 | -1,80 | 3,20  |
|   | 34 | 7,00 | -1,80 | 5,20  |

Fonte: Elaborada pelos autores.

Podemos analisar a Figura 5.9 em que os ganhos são auferidos apenas se o preço do ativo-objeto ficar abaixo de R$ 25,20 ou acima de R$ 28,80:

Figura 5.9 | Resultado do exemplo de strangle
![img-56.jpeg](img-56.jpeg)
Fonte: Elaborada pelos autores.

---

Essa é uma estratégia direcional, na qual existe uma expectativa de mudanças bruscas no preço do ativo-objeto, tanto para baixo quanto para cima.

## 5.4.5 Butterfly

A butterfly ou trava-borboleta é uma estratégia na qual se utilizam três preços de exercício diferentes. Para montarmos essa estratégia, devemos comprar uma call de preço de exercício menor, vender duas calls de preço de exercício intermediário, e comprar outra call de preço de exercício maior que o das anteriores. Todas as calls são do mesmo ativo-objeto e mesmo vencimento.

Nessa estratégia, de compra de trava-borboleta, o objetivo será o de apostar na estabilidade do preço do ativo-objeto, dentro de um determinado intervalo de ganho.

Vamos exemplificar a estratégia trava-borboleta:

- Compra de uma call com o preço de exercício de R$ 32,00 a R$ 1,30. Na convenção da notação, +C32.
- Venda de duas calls com o preço de exercício de R$ 34,00 a R$ 0,32. Na convenção da notação, -2C34.
- Compra de uma call com o preço de exercício de R$ 36,00 a R$ 0,10. Na convenção da notação, +C36.

Podemos então resumir essa estratégia pela seguinte notação, [+C32; -2C34; +C36].

---

Vamos considerar a Fórmula 5.17 a seguir para calcular o resultado da posição +C26 e +C36:



R_(+ C) = Q Max [ S _t - K; 0 ] - Q c (5.17)



E a Fórmula 5.18 para calcular a posição -2C34:



R_(- C) = - Q Max [ S _t - K; 0 ] + Q c (5.18)



De posse das equações anteriores, vamos calcular o resultado da estratégia, que é a soma dos resultados das posições individuais, apresentado na Tabela 5.5 a seguir:

Tabela 5.5 | Resultado do exemplo de butterfly

|   | St | +C32 | -2C34 | +C36 | Estratégia  |
| --- | --- | --- | --- | --- | --- |
|   | 20 | -1,30 | 0,64 | -0,10 | -0,76  |
|   | 22 | -1,30 | 0,64 | -0,10 | -0,76  |
|   | 24 | -1,30 | 0,64 | -0,10 | -0,76  |
|   | 26 | -1,30 | 0,64 | -0,10 | -0,76  |
|   | 28 | -1,30 | 0,64 | -0,10 | -0,76  |
|   | 30 | -1,30 | 0,64 | -0,10 | -0,76  |
|   | 32 | -1,30 | 0,64 | -0,10 | -0,76  |
|  breakeven | 32,76 | -0,54 | 0,64 | -0,10 | 0,00  |
|   | 34 | 0,70 | 0,64 | -0,10 | 1,24  |
|  breakeven | 35,24 | 1,94 | -1,84 | -0,10 | 0,00  |
|   | 36 | 2,70 | -3,36 | -0,10 | -0,76  |
|   | 38 | 4,70 | -7,36 | 1,90 | -0,76  |
|   | 40 | 6,70 | -11,36 | 3,90 | -0,76  |
|   | 42 | 8,70 | -15,36 | 5,90 | -0,76  |
|   | 44 | 10,70 | -19,36 | 7,90 | -0,76  |

Fonte: Elaborada pelos autores.

Podemos notar, por meio da análise da Figura 5.10 a seguir, que o ganho está entre o intervalo de preço do ativo-objeto de R$ 32,76 a R$ 35,24.

---

Figura 5.10 | Resultado do exemplo de butterfly
![img-57.jpeg](img-57.jpeg)
Fonte: Elaborada pelos autores.

Essa é uma estratégia direcional na qual existe uma expectativa de estabilidade do preço do ativo-objeto dentro do intervalo de preços. Essa operação possui a característica de um ponto de ganho máximo, se no vencimento das opções o preço do ativo estiver a R$ 34,00, o ganho será de R$ 1,24.

Ao longo deste capítulo apresentamos apenas algumas das estratégias direcionais possíveis de serem montadas com opções. Existem diversas outras estratégias que podem ser adotadas, como straddle, condor, seagul, Zero cost collar, target forward e participating forward. A imaginação passa a ser o limite em se tratando de estratégias direcionais com opções.

Das estratégias citadas é possível gerar variantes, por exemplo, invertendo as compras e vendas das posições individuais. Com isso, calcularíamos os resultados das pontas opostas das estratégias aqui apresentadas. Em geral, quando montamos estratégias direcionais não há necessidade de

---

carregamento até o vencimento da opção, a reversão pode ser feita antecipadamente, resultando em lucro ou prejuízo parciais.

Como mencionado anteriormente, não consideramos o valor do dinheiro no tempo nas estratégias direcionais.

# RESUMO

Neste capítulo, tratamos os contratos de opções na sua forma mais simples, tais como opções de compra – call – e opção de venda – put. Foram feitas considerações com relação ao exercício das opções americanas e europeias. Foram apresentados exemplos de precificação por arbitragem, por meio da put-call parity, e estratégias direcionais introdutórias, tais como: bull call spread, strangle e butterfly.

# EXERCÍCIOS PROPOSTOS

Para cada uma das estratégias a seguir:

1. Quais os tipos de contratos de opções existentes:

a. Opções de compra (call) e opções de venda (put) b. Opções de compra (put) e opções de venda (call) c. Opções de compra e venda de ações
d. Opções de compra e venda flexíveis

2. Uma opção que possa ser exercida somente na data do vencimento do contrato chama-se: a. Opção tipo americano
b. Opção tipo inglês
c. Opção tipo put e call d. Opção tipo europeu

3. Assinale a afirmação correta:

a. Vendedor de uma opção tem direito – não a obrigação – de exercê-la b. Comprador de uma opção tem obrigação – não o direito – de exercê-la c. Comprador de uma opção tem direito – não a obrigação – de exercê-la d. Vendedor de uma opção tem direito e obrigação de exercê-la

---

e. Nenhuma das alternativas anteriores

4. Um indivíduo está posicionado em uma operação de opção, e seu provável resultado é representado pelo gráfico a seguir, logo ele está:

![img-58.jpeg](img-58.jpeg)

a. Long call
b. Long put
c. Short call
d. Short put
e. Ele é lançador da opção

5. O valor do prêmio de uma call de strike igual a R$ 100,00 é de R$ 11,00, e vencimento em 23 d.u., sendo que o preço do ativo na data de hoje é de R$ 95,00, e a taxa livre de risco é de 22% a.a., o preço da put de mesmo vencimento e preço de exercício deve ser (put-call parity): a. R$ 11,00
b. R$ 12,23
c. R$ 13,28
d. R$ 14,20
e. R$ 15,11

6. Calcule os resultados em uma tabela no Microsoft Excel de cada uma das posições e da estratégia para diversos preços do ativo-objeto no vencimento da opção, executando os seguintes passos: ■ Plote os gráficos ■ Identifique o(s) breakeven(s)

■ Explique o racional ou motivação de fazer cada uma das estratégias. Quais as expectativas que justificariam tal estratégia ■ Indique o nome da estratégia a. Compra do ativo a R$ 39,00 e venda de call C40 a R$ 1,20, [+S39; -C40];
b. Compra de call C40 a R$ 1,20 e venda de C42 a R$ 0,21, [+C40; -C42];
c. Venda de call C40 a R$ 1,20 e compra de C42 a 0,21, [-C40; +C42];
d. Compra de call C40 a R$ 1,20, venda de duas calls C42 a R$ 0,21 e compra de call C44 a R$ 0,05, [+C40; -2C42, +C44];
e. Compra de call C40 a R

---

1,20 e compra de put P40 a R$ 1,20, [+C40; +P40]; f. Compra de call C40 a R$ 1,20 e compra de put P42 a 2,10, [+C40; +P42]; g. Compra de call C40 a R$ 1,20 e venda de put P40 a R$ 1,20, [+C40; -P40].

1 Chicago Board of Options Exchange (CBOE), que significa Bolsa de Opções de Chicago na língua inglesa.

---

CAPITULO 6

# Precificação de opções

---

Neste capítulo apresentaremos alguns modelos para a precificação de opções. O critério de seleção adotado na escolha dos modelos apresentados foi sua utilidade prática, pois na literatura existem diversas formas de precificação, que não têm uso pragmático.

No início do capítulo, especificamos os dois principais processos estocásticos de ativos negociados no mercado e, em seguida, apresentamos um método numérico para precificação de opções, denominado Simulação de Monte Carlo.

Posteriormente, explicitamos modelos de equações fechadas, tendo como base o modelo de Black e Scholes (1973), para precificação de opções sobre diversos ativos, tais como: ações, ações com dividendos, ativos com custo de carregamento, câmbio, contratos futuros, IBOVESPA e IDI.

Este capítulo é dedicado, em sua maior parte, às precificações de opções plain vanilla, ou seja, opções na sua forma mais simples, sem componentes exóticos.

## 6.1 Processos estocásticos

### 6.1.1 A trajetória dos preços no tempo

Para se determinar o preço de um ativo (S_t) é preciso definir qual é o modelo que melhor descreve a trajetória dos seus preços no tempo. Por essa razão, optamos por adotar um modelo que tenha o tempo como variável independente, que descreva um processo estocástico. O modelo que se quer determinar é o seguinte:



S_(t-1) xrightarrow{Modelo} S_t 



---

Um processo estocástico é suposto para uma variável cujos valores mudem com o tempo e possuam um componente aleatório. Um modelo que descreve o processo estocástico de uma variável, como o preço de um ativo, possui pelo menos dois componentes distintos: um componente determinístico e um componente estocástico, ou seja, aleatório no tempo. Em verdade, o componente determinístico pode assumir valor zero, descrevendo um processo particular denominado de movimento browniano.

De acordo com Hull (2012), o preço de um ativo não é observado em tempo contínuo, ou seja, os preços são observados quando há negociação e nos intervalos em que ocorram os pregões, ou seja, em tempo discreto.

Por essa razão, o modelo que se deseja obter para descrever a trajetória de preços do ativo será inicialmente desenvolvido em tempo discreto e depois generalizado em tempo contínuo.

## 6.1.2 A variável aleatória

Para determinar um modelo de formação de preços é preciso estudar as propriedades estatísticas da variável aleatória e a função conhecida que melhor descreva a sua distribuição de probabilidade.

A função de distribuição normal proposta por Karl F. Gauss em meados do século 19, em seus trabalhos sobre erros de observações astronômicas, descreve muitos dos fenômenos da natureza e, para grandes amostras, é possível generalizar propriedades dos estimadores dos parâmetros analisados.

Diz-se que uma variável aleatória tem distribuição normal X sim N(μ, σ^2), com os parâmetros μ e σ^2, quando sua função é dada por:



f(x) = 1/σ √(2π) e^(-(x - μ)/2σ^2)   (6.2)



---

Sendo:

- x: variável aleatória observada
- μ: média populacional
- σ^2: variância populacional

Uma premissa relevante para a variável aleatória em questão é que seus valores possam estar no intervalo -∞ < x < ∞.

A distribuição normal pode ser simplificada para um caso particular: a variável normal padronizada Z sim N(0,1), sendo -∞ < Z < ∞, cuja função é dada por:



f(z) = 1/√(2π) e^(-z^2/2)   (6.3)



É possível converter uma dada observação amostral x para uma normal padronizada Z aplicando-se a seguinte transformação:



z = x - mu_x/sigma_x   (6.4)



Suponha que consideremos que a variável aleatória é o preço (S_t) do ativo em nível, ou seja, sem nenhum tipo de transformação. Sabe-se, porém, que o preço do ativo não pode assumir valores negativos, deve estar no intervalo 0 < S_t < ∞. Dessa maneira, não é possível descrever a distribuição de probabilidade do preço por meio de uma função normal. Contudo, é possível aplicar transformações na variável, no intuito de encontrar a variável cuja distribuição de probabilidade seja mais bem ajustada à função normal.

As taxas de retorno podem ser discretas ou contínuas. A taxa de retorno discreta (r_t) é obtida da seguinte forma:

---



r _t = S _t/S_(t - 1) - 1 tag {6.5}



A taxa de retorno discreta também não pode apresentar uma distribuição de probabilidade normal, porque o retorno discreto não pode assumir valores inferiores a -100\%, pertence ao intervalo -1 < r_t < ∞, pois, de outra forma, o preço do ativo poderia assumir valores negativos.

A taxa de retorno contínua, por outro lado, é obtida pela diferença dos logaritmos naturais dos preços, segundo a equação a seguir:



R _t = ln (S _t) - ln (S_(t - 1)) tag {6.6}



Portanto, o retorno contínuo pode ser representado da seguinte forma:



R _t = ln (S _t/S_(t - 1)) tag {6.7}



Uma das vantagens do retorno contínuo é que em modelos de variáveis que seguem processos estocásticos é possível extrair o componente de tendência da amostra ao tirar as diferenças dos valores observados. Ao obter o retorno contínuo, tiram-se as diferenças dos logaritmos naturais, o que permite, além de eliminar a tendência dos preços, que a variável taxa de retorno assuma valores dentro do intervalo -∞ < R_t < ∞ exigido para uma distribuição normal. Tem-se na Figura 6.1 uma representação gráfica do que seria uma distribuição de retornos R_t transformada em uma normal padronizada:

Figura 6.1 | Curvas normal e normal padronizada

---

![img-59.jpeg](img-59.jpeg)

![img-60.jpeg](img-60.jpeg)
Fonte: Elaborada pelos autores.

Os retornos de uma ação podem, ou não, ter uma distribuição normal, com média μ e variância σ^2. A Figura 6.2 a seguir apresenta o histograma dos retornos contínuos das cotações históricas da ação da Vale. Para o histograma foi utilizada uma base de dados histórica de cotações de último negócio de dez anos de pregão, ajustadas para dividendos:

![img-61.jpeg](img-61.jpeg)
Figura 6.2 | Histograma dos retornos logarítmicos da Vale

---

Fonte: Elaborada pelos autores.

O histograma dos retornos contínuos da Vale, definitivamente, parece-se com uma distribuição normal. Porém, em testes de normalidade de assimetria e curtose conjuntas, geralmente, rejeita-se a normalidade, isso ocorre porque o poder de rejeição de hipótese nula aumenta, quanto mais elementos estiverem presentes na amostra.

Em amostras de retorno de ações, como a representada pelo histograma da Figura 6.2, estão presentes assimetria e curtose. A amostra de retornos é, geralmente, leptocúrtica, apresentando o que denominamos de *fat tails*, caudas longas ou grossas.

Podemos interpretar as caudas longas como eventos extremos nos retornos dos ativos, que ocorrem em uma frequência maior do que ocorre em uma distribuição de probabilidade normal.

Dessa forma, se considerarmos que os retornos contínuos possuem distribuição normal, estaremos subestimando a probabilidade dos eventos extremos.

Os eventos extremos são aqueles que podem dar resultados mais expressivos para o investidor, positivos ou negativos. Estaremos negligenciando os momentos de grandes perdas e eventos de alta rentabilidade para o ativo.

Em precificação de opções, a leptocurtose ocasionará o que denominamos de *smile* de volatilidade, que será tratado de forma mais detalhada posteriormente.

# 6.1.3 Processo de Wiener

O retorno contínuo dos preços de um ativo pode seguir um processo estocástico conhecido como processo de Wiener. Esse processo é utilizado na Física para descrever o movimento de uma partícula que é sujeita a um grande número de pequenos choques moleculares e algumas vezes referido como movimento browniano.

---

Partindo da premissa que a distribuição de probabilidade dos retornos seja descrita por uma função normal, R_t sim N(μ, σ^2), uma observação da variável aleatória R_t pode ser transformada em Z por meio da equação a seguir:



z = R_t - mu_t/sigma_t 



Pode-se padronizar uma dada observação, sendo z = (R_t - mu_t) / sigma_t e, dessa forma, calcular o retorno partindo-se de um Z dado, conforme a seguinte equação:



R_t = mu_t + sigma_t z 



Dado que o retorno contínuo pode ser calculado pela diferença dos logaritmos naturais, o logaritmo do preço à vista pode ser escrito em função do retorno:



ln(S_t) = ln(S_(t-1)) + R_t 



O preço à vista de um ativo pode ser calculado aplicando-se o retorno contínuo ao preço imediatamente anterior, S_t = S_(t-1) e^(R_t). É possível modelar a função do preço utilizando, no lugar do retorno, sua média e desvio-padrão:



S_t = S_(t-1) e^(mu_t + sigma_t z) 



Ao determinar o processo estocástico que descreve a trajetória do preço de um ativo no passado é possível realizar uma projeção um passo à frente, partindo da premissa que esse processo modelado seja persistente no tempo. A previsão do valor de S_(t+1) pode ser feita da seguinte maneira:

---



S_(t+1) = S_(t-1) e^(R_t) e^(R_(t+1)) 



Supondo que os retornos contínuos são independentes e identicamente distribuídos i.i.d.: covar [R_(t-1), R_t] = 0 e Var[R_(t-1)] = Var[R_t], tem-se a seguinte relação para as médias e variâncias:



mu_t + mu_(t+1) = 2mu_t 





Var[R_(t-1) + R_t] = Var[R_(t-1)] + Var[R_t] + 2covar[R_(t-1), R_t] 





Var[R_(t-1) + R_t] = 2Var[R_t],  i.i.d.



Dado que o desvio-padrão do retorno é sigma_t = √{Var[R_t]}, pode-se propor a seguinte relação para a projeção um passo à frente do preço do ativo:



S_(t+1) = S_(t-1) e^(2mu_t + √(2)sigma_t z) 



Para uma previsão Δ t à frente, com Δ t → 0, generalizamos a seguinte função:



S_(t+1) = S_t e^(tmu_t + √(t)sigma_t z) 



Em tempo contínuo, para um intervalo de tempo infinitesimal dt é possível preservar a relação dos preços do ativo:



S_(t+dt) = S_t e^(dtmu_t + √(dt)sigma_t z) 



---

Sendo a equação que especifica a dinâmica dos retornos é dada por:



ln (S_(t + d t)) = ln (S _t) + d t mu_t + √ {d t} sigma_t z tag {6.18}





R _t = d t mu_t + √ {d t} sigma_t z tag {6.19}



Ou simplesmente:



R _t = μ d t + σ √ {d t} z,   i. i. d. tag {6.20}



O preço de um ativo pode seguir um processo estocástico particular, denominado processo de Markov ou markoviano, no qual apenas o preço de hoje é relevante para a previsão do preço futuro, sendo irrelevantes os valores passados.

O processo de Wiener é um processo estocástico com média zero e variância igual a 1. O movimento browniano é um caso particular do processo de Wiener Generalizado, que permite valores diferentes de 0 e 1 para a média e variância, respectivamente.

Ou seja, permite a existência de drift mu_t nos retornos contínuos.

Conforme visto anteriormente, aplicou-se a primeira diferença para eliminar a tendência nos preços, pode-se aplicar a diferença mais uma vez, a fim de eliminar a tendência nos retornos, conforme segue:



R _t = mu_t + sigma_t z





R_(t + 1) = mu_t + sigma_t z^(prime),   i. i. d. tag {6.21}





Δ R_(t + 1) = R_(t + 1) - R _t



---

A primeira diferença dos retornos é igual à segunda diferença do logaritmo dos preços Δ R_t = Δ²ln (S_t), calculada, independente e identicamente distribuídas (i.i.d.), da seguinte forma:



Δ R_(t + 1) = mu_t - mu_t + sigma_t z^(prime) - sigma_t z tag {6.22}



Tendo a variância da diferença dos retornos dada por:



{l} V a r [ R_(t + 1) - R _t ] = V a r [ R_(t + 1) ] + V a r [ R _t ] - 2 c o v a r [ R_(t + 1), R _t ] tag {6.23} 
 V a r [ R_(t + 1) - R _t ] = 2 V a r [ R _t ],   i. i. d. 
 



Dessa forma, elimina-se o componente determinístico, permanecendo apenas o componente estocástico:



{l} √ {2 V a r [ R _t ]} = √ {2} sigma_t tag {6.24} 
 Δ R_(t + 1) = √ {2} sigma_t z 
 



Ou na forma contínua:



d R = √ {d t} sigma_t z tag {6.25}



De forma genérica, é possível supor que a diferença dos retornos de um ativo é composta apenas de choques aleatórios e que dependam exclusivamente da volatilidade sigma_t dos retornos. No limite com Δ t → 0 supõe-se que:



R _t = ln S _t/S_(t - 1) ≈ S _t - S_(t - 1)/S_(t - 1) ≈ d S/S_(t - 1) tag {6.26}



---

Dado que o retorno é uma função de sua média e volatilidade, a equação que descreve a dinâmica do retorno de um ativo pode ser dada por:



d S/S _t = μ d t + σ √ {d t} z tag {6.27}



O uso da taxa de retorno discreta na equação do movimento browniano dos preços de um ativo, como na Equação 6.27, pode ser questionável. Os retornos discretos possuem uma distribuição que, apesar de assemelhar-se a uma distribuição normal, não possui as condições necessárias para que seja normal, pois o retorno discreto não pode ser menor do que -100\%.

Na seção seguinte será feita uma breve explicação do Lema de Itô, que permite a determinação do processo de uma variável transformada.

## 6.1.4 Lema de Itô

Por meio do Lema de Itô é possível obter uma equação que descreve a dinâmica de uma variável transformada (y_t) como função da variável original (S_t), ou seja, y_t = f(S_t). Para o preço de um ativo, deseja-se determinar a função do logaritmo natural do preço no tempo t:



y _t = ln (S _t) tag {6.28}



A equação do movimento browniano, do preço de um ativo, pode ser representada da seguinte forma, conforme visto anteriormente:



d S = μ S _t d t + σ S _t √ {d t} z tag {6.29}



---

A Equação 6.29 é um modelo de difusão de preços de um ativo (S) por meio de um processo estocástico. Para uma variável (x) qualquer, aleatória no tempo, na qual a simbologia (.) significa uma função da variável x, cuja equação de difusão é representada por:



dx = μ(.) dt + σ(.) dz_t   (6.30)



No modelo anterior, o componente estocástico √(dt)z é representado por simplicidade de notação, apenas por dz_t, com Δ t → 0, Z_t denota Z em função do tempo, e determina que Z_t é igual à soma de suas pequenas diferenças, representada pela integral:



z_t - z_0 = ∫(s=0 até t) dz_s   (6.31)



Sendo as esperanças de dz_t dadas por:



{l}
E_t(dz_t) = 0   (6.32) 

E_t(dz_t^2) = dt




Cochrane (2005, p. 460) sugere a construção de uma variável y que seja uma função de x, y_t = f(x_t), com o intuito de explicar os procedimentos adotados no Lema de Itô.

Partindo da definição anterior de que √(dt)z é representado por dz_t, para Δ t → 0, sugere que dz_t^2 = dt e que os termos dt dz, dt^2 tendem a zero e que, aproximadamente, pequenas variações no valor da variável transformada y podem ser calculadas pela derivada parcial em função de x, conforme a seguinte equação:

---



Δ y ≈ dy/dx Δ x   (6.33)



Na expansão de segunda ordem da série de Taylor para a variável y em função de x, tem-se:



dy = df(x)/dx dx + 1/2 d^2 f(x)/dx^2 dx^2   (6.34)



Expandindo o segundo termo da equação, com base na equação de difusão estocástica de dx, tem-se:



dx^2 = [ mu_x dt + sigma_x dz_t ]^2 = mu_x^2 dt^2 + sigma_x^2 dz_t^2 + 2 mu_x sigma_x dt dz_t   (6.35)



Agora, aplica-se a regra definida no Lema de Itô, em que dt^2 = 0 e que dz_t^2 = dt, tem-se, portanto, que dx^2 = sigma_x^2 dt. Substituindo-se os valores de dx e dx^2 na equação de dy:



dy = df(x)/dx ( mu_x dt + sigma_x dz_t ) + 1/2 d^2 f(x)/dx^2 sigma_x^2 dt   (6.36)





dy = [ df(x)/dx mu_x + 1/2 d^2 f(x)/dx^2 sigma_x^2 ] dt + df(x)/dx sigma_x dz_t   (6.37)



Logo, a equação do Lema de Itô que determina o modelo de difusão estocástica da variável transformada y, em função da variável original x, é representada por:

---



d y = [ d f (x)/d x mu_x (.) + 1/2 d ² f (x)/d x ² sigma_x ² (.) ² ] d t + d f (x)/d x sigma_x (.) d z _t tag {6.38}



A peculiaridade dessa equação está na presença de um segundo termo no componente determinístico.

Definida a equação do Lema de Itô é possível voltar ao problema inicial, no qual se deseja determinar a equação de dispersão estocástica do logaritmo natural do preço de um ativo (S_t), utilizando-se uma variável transformada definida pela função y_t = ln (S_t), da qual se pode calcular as seguintes derivadas parciais:



∂ y _t/∂ S _t = 1/S _t, ∂² y/∂ S ² = - 1/S _t ² tag {6.39}



A equação de dispersão da variável y deverá ser igual a:



d y = [ 1/S _t mu_x S _t + 1/2 (- 1/S _t ²) sigma_x ² S _t ² ] d t + 1/S _t sigma_x S _t d z _t tag {6.40}



Ou simplesmente:



d y = [ mu_x - 1/2 sigma_x ² ] d t + sigma_x d z _t tag {6.41}



A Equação 6.41 é de grande utilidade para os modelos de precificação de derivativos, como é possível observar nos trabalhos de Black e Scholes (1973, p. 639) e Merton (1973, p. 160), que definem equações fechadas para precificação de opções. Esses modelos descrevem processos estocásticos em movimento browniano para preços de ativos financeiros.

---

# 6.1.5 Reversão à média

O modelo analisado na seção anterior utilizou uma variável aleatória transformada: as diferenças dos logaritmos do preço do ativo S_t. O objetivo dessa transformação foi tornar a série estacionária. Porém, é possível estimar modelos lineares estacionários utilizando variáveis não estacionárias. Definidas como variáveis cointegradas.

Quando há cointegração, significa que, mesmo que alguns eventos possam causar mudanças permanentes na variável em questão, y_t, existe algum tipo de relação de equilíbrio de longo prazo (long-run), unindo as variáveis novamente.

A principal característica de variáveis cointegradas, segundo Enders (2004, p. 328) é que a “... trajetória é influenciada por quaisquer desvios extensos do equilíbrio de longo prazo”. Mesmo que o sistema como um todo retorne para o equilíbrio de longo prazo, pelo menos uma das variáveis continuará respondendo ao efeito do desequilíbrio ocorrido. Em outras palavras: a dinâmica de curto prazo (short-run) deve ser influenciada pelos desvios ocorridos nas relações de longo prazo (long-run).

O processo de retorno ao equilíbrio de longo prazo é definido como correção do erro. Esse processo, característico de variáveis cointegradas, é definido como processo Ohrnstein-Uhlenbeck de reversão à média.

O processo de reversão à média começa a partir de um processo autorregressivo de ordem 1, AR(1). Supondo que o preço do ativo (S_t) cointegre com ele mesmo, descrevendo um processo AR(1), conforme a seguinte equação:



S_t = beta_0 + beta_1 S_(t-1) + varepsilon_t 



Sendo:

---

ε_t: ruído branco, componente de erro estocástico do processo AR(1)

β₀ e β₁: coeficientes da regressão

A média do preço é dada por E[S_t] = beta₀ + beta₁S_(t - 1), ou seja, o preço pode ser calculado em relação à sua média:



S _t = mu_t + varepsilon_t   (6.43)



Partindo da Equação 6.43 é possível definir uma nova variável: o desvio em relação à média D_t = S_t - mu_t é similar ao ruído branco varepsilon_t. O valor esperado do desvio D_t, no limite, é igual a zero, E[D_t] = 0. No processo de reversão à média é possível estimar o modelo de regressão dos desvios seguindo um processo de média móvel:



D _t = α D_(t - 1) + zeta_t   (6.44)



Sendo:

zeta_t: ruído branco

α: coeficiente da regressão

Nesse caso, para um processo de reversão à média, o coeficiente α da regressão deve ser negativo e, em módulo, menor que 1, ou seja, -1 < α < 0.

Utilizando a Equação 6.44, substitui-se o desvio da média D_t, e chega-se a seguinte equação:



S _t - μ = α (S_(t - 1) - μ) + zeta_t   (6.45)



Subtraindo-se S_(t-1) dos dois lados da equação:

---



S _t - S_(t - 1) = α (S_(t - 1) - μ) - S_(t - 1) + μ + zeta_t tag {6.46}



E, por fim, partindo de um processo AR(1), chega-se ao modelo de reversão a média em tempo discreto para o preço de um ativo:



S _t - S_(t - 1) = - (1 - α) (S_(t - 1) - μ) + zeta_t tag {6.47}



Com a versão análoga em tempo contínuo dada por:



d S = - φ (S _t - μ) d t + σ d z _t tag {6.48}



Sendo:

φ: velocidade de reversão à média

É conveniente lembrar que é possível agregar ao modelo uma matriz (n × m) com outras variáveis explicativas x_t, estacionárias ou não, que cointegrem com o modelo.

Com S_t = mu_t + varepsilon_t, o modelo teria a seguinte representação genérica:



S _t = β^(prime) x _t + varepsilon_t tag {6.49}



Sendo:

x_t: matriz (n × m) de variáveis explicativas

β: vetor (m × 1) de coeficientes da regressão

Até aqui, apresentamos os processos estocásticos que descrevem a trajetória dos preços de um ativo. Os processos relevantes vistos foram: movimento

---

browniano e reversão à média. Partindo desses processos foram desenvolvidos modelos que tentam descrever, a partir da combinação de variáveis, o comportamento dos preços de ativos, para precificação de opções.

## 6.2 Simulação de Monte Carlo

A simulação de Monte Carlo consiste no sorteio aleatório da variável normal padronizada Z sim N(0,1), que pode ser utilizada para simular trajetórias do preço do ativo no futuro para um dado processo estocástico e para parâmetros previamente estimados.

O objetivo da simulação de Monte Carlo na precificação de opções é o de simular um número computacionalmente viável de trajetórias do preço do ativo até o vencimento da opção.

Esse método é particularmente útil quando a opção possui características exóticas *path dependent* (dependente da trajetória). Nas opções exóticas do tipo *path dependent*, o resultado no exercício da opção depende da trajetória do preço do ativo-objeto durante a vigência do contrato. Por exemplo, uma opção que possui barreiras, *knock in* e *out*, ou preços médios (asiática) em suas características de contrato.

Enfim, quando não é possível, ou muito difícil de se obter uma equação fechada para precificar opções, pode-se lançar mão de um algoritmo que contenha a simulação de Monte Carlo para precificá-las.

A construção de um algoritmo que contenha um método de simulação de Monte Carlo é de fácil implementação. Além disso, com a evolução da robustez computacional, tanto em hardware quanto em software, é possível gerar um grande número de simulações, ou seja, uma amostra de trajetórias suficientemente grande, para precificar adequadamente a opção.

---

O processo gerador de dados de números aleatórios utilizado na simulação deve ser não viesado, geralmente são algoritmos prontos em aplicativos computacionais.

É importante lembrar que os algoritmos não são perfeitamente aleatórios por natureza, pois os computadores não têm como realizar sorteios aleatórios de fato.

## 6.2.1 Simulação de Monte Carlo para processo de Wiener

Atualmente, a forma em que a simulação de Monte Carlo é mais utilizada para precificação de opções, considera o retorno discreto do preço dos ativos seguindo um processo de Wiener com o Lema de Itô, do seguinte modo:



R_t = (μ - 1/2 σ^2) dt + σ dz_t   (6.50)



Para Delta_t → 0, ou seja, para um intervalo de tempo infinitesimalmente pequeno, a equação anterior pode ser representada da seguinte forma:



ln(S_(t+Δ t)) - ln(S_t) = (μ - 1/2 σ^2) Δ t + σ √(Δ t) z   (6.51)



Para a simulação da cotação da ação para um período Delta_t à frente, tem-se que:



S_(t+Δ t) = S_t e^((μ - 1/2 σ^2) Δ t + σ √(Δ t) z)   (6.52)



---

Utilizando a equação anterior, vamos fazer um exemplo de simulação de Monte Carlo para precificar uma opção de compra (call) de ação que vencerá dentro de cinco dias úteis. Consideraremos uma volatilidade σ de 35\% a.a.o. (base 252) e uma média μ de 14\% a.a.o. (taxa livre de risco na forma contínua), que segue um processo de Wiener. Suponha que a cotação da ação está hoje a R$ 32, cujo preço de exercício da opção de compra também é R$ 32. Vamos precificar essa opção partindo da seguinte matriz de variáveis Z sim N(0,1) sorteadas, com três trajetórias:

Tabela 6.1 | Variáveis z sorteadas

|  Dias | Trajetória 1 | Trajetória 2 | Trajetória 3  |
| --- | --- | --- | --- |
|  1 | -1,86 | -0,45 | -0,56  |
|  2 | -0,56 | 0,33 | 0,20  |
|  3 | 0,50 | -0,17 | 1,15  |
|  4 | 1,09 | -1,44 | 1,01  |
|  5 | 0,82 | 1,01 | 1,05  |

Fonte: Elaborada pelos autores.

Com base na Tabela 6.1, vamos calcular o preço da ação no primeiro dia da trajetória 1, tendo como base os estimadores de parâmetros fornecidos:



S_(1,1) = 32 e^((0,14 - 1/20,35^2)1/252 + 0,35 √(1/252) (-1,86)) = 30,7239



O preço da ação no primeiro dia é de R$ 30,7055, agora vamos calcular o preço no segundo dia da trajetória 1, partindo do valor obtido no dia 1:



S_(2,1) = 30,7239 e^((0,14 - 1/20,35^2)1/252 + 0,35 √(1/252) (-0,56)) = 30,3563



---

Assim, sucessivamente, calculamos todos os dias, das très trajetórias, considerando que o preço da ação na data zero era R$ 32:

Tabela 6.2 | Trajetórias do preço da ação
|  Dias | Trajetória 1 | Trajetória 2 | Trajetória 3  |
| --- | --- | --- | --- |
|  0 | 32,0000 | 32,0000 | 32,0000  |
|  1 | 30,7239 | 31,6940 | 31,6172  |
|  2 | 30,3563 | 31,9354 | 31,7669  |
|  3 | 30,7024 | 31,8259 | 32,5928  |
|  4 | 31,4590 | 30,8409 | 33,3371  |
|  5 | 32,0430 | 31,5453 | 34,1286  |

Fonte: Elaborada pelos autores.

Partindo da premissa de que as três trajetórias são equiprováveis e o strike igual a R$ 32, o payoff da opção no vencimento nas três trajetórias seria R$ 0,0430, zero e R$ 2,1286, respectivamente. O resultado da média aritmética dos três payoffs é de R$ 0,7238, que descontado a valor presente, deve ser o prêmio da opção:



C = 0 , 7 2 3 8/e^(0 , 1 4 (5/2 5 2)) = 0, 7 2 1 8



O exemplo descrito anteriormente tem um objetivo didático, pois três trajetórias é um número muito pequeno para se obter uma amostra de trajetórias adequadas para precificar a opção.

A figura a seguir exemplifica graficamente as diversas trajetórias de uma simulação de Monte Carlo seguindo um processo de Wiener:

Figura 6.3 | Simulação de Monte Carlo para processo de Wiener

---

![img-62.jpeg](img-62.jpeg)
Fonte: Elaborada pelos autores.

# 6.2.2 Simulação de Monte Carlo para reversão à média

A simulação de Monte Carlo pode ser implementada para diversos processos estocásticos. Implementaremos o Monte Carlo para precificar opções, cuja trajetória dos preços do ativo-objeto descreva um processo de reversão à média, de forma que a variável cointegre com ela mesma, e que seja possível estimar um modelo linear estacionário, utilizando uma variável não estacionária, neste caso, o preço do ativo-objeto.

Isso acontece porque existe uma relação de equilíbrio de longo prazo (long run), e que desvios de curto prazo podem ser corrigidos por um fator de correção de erro.

Suponha que o preço de uma determinada commodity sofra desvios de curto prazo, decorrentes de uma escassez momentânea, que ocasione a redução nos níveis dos estoques globais. Com base na análise do comportamento dessa commodity é possível que o preço volte para um equilíbrio de longo prazo, assim que os níveis dos estoques estejam novamente regulados para um patamar médio histórico e quando o período de escassez esteja terminado ou controlado.

Se o preço do ativo seguir um processo de reversão à média em tempo contínuo, seria representado pela Equação 6.53:

---



dS = - φ (S _t - μ) d t + σ d z _t tag {6.53}



Sendo:

φ: velocidade de reversão à média

Para Δ t → 0, um intervalo de tempo infinitesimalmente pequeno, a equação anterior pode ser representada da seguinte forma:



S_(t + Δ t) = S _t - φ (S _t - μ) Δ t + σ √ {Δ t} z _t tag {6.54}



Partindo da premissa de que o preço do ativo-objeto siga o processo de reversão à média anteriormente descrito, vamos fazer um exemplo de precificação de opção de compra (call), com base nas seguintes informações: volatilidade σ de 26\% a.a.o., uma taxa de juros livre de risco na forma contínua de 14\% a.a.o. A média de equilíbrio μ é de R$ 29 e o preço do ativo na data de hoje é de R$ 31, e a velocidade de reversão à média φ é de 200\% ao ano, partindo da mesma matriz de variáveis z sim N(0,1) sorteadas que utilizamos no exemplo anterior:

Tabela 6.3 | Variáveis z sorteadas

|  Dias | Trajetória 1 | Trajetória 2 | Trajetória 3  |
| --- | --- | --- | --- |
|  1 | -1,86 | -0,45 | -0,56  |
|  2 | -0,56 | 0,33 | 0,20  |
|  3 | 0,50 | -0,17 | 1,15  |
|  4 | 1,09 | -1,44 | 1,01  |
|  5 | 0,82 | 1,01 | 1,05  |

Fonte: Elaborada pelos autores.

---

No exemplo de reversão à média, queremos precificar uma opção de compra de preço de exercício igual a R$ 30, com vencimento que ocorrerá em cinco dias úteis. Vamos realizar a simulação de três trajetórias.

Para calcular o preço do ativo no primeiro dia da trajetória 1, faremos da seguinte forma, sabendo que o preço do ativo na data inicial é R$ 31:



S_(1,1) = 31 - 2(31 - 29)1/252 + 0,26√(1/252) (-1,86) = 30,9457



O preço projetado para o segundo dia da trajetória 1 deve ser calculado da seguinte maneira:



S_(2,1) = 30,9457 - 2(30,95 - 29)1/252 + 0,26√(1/252) (-0,56) = 30,9134



E, assim sucessivamente, calculamos todos os dias das três trajetórias do nosso exemplo, cujos resultados são apresentados na Tabela 6.4:

Tabela 6.4 | Trajetórias do preço do ativo

|  Dias | Trajetória 1 | Trajetória 2 | Trajetória 3  |
| --- | --- | --- | --- |
|  0 | 31,0000 | 31,0000 | 31,0000  |
|  1 | 30,9457 | 30,9688 | 30,9670  |
|  2 | 30,9134 | 30,9508 | 30,9469  |
|  3 | 30,8988 | 30,9248 | 30,9425  |
|  4 | 30,8940 | 30,8783 | 30,9360  |
|  5 | 30,8849 | 30,8725 | 30,9301  |

Fonte: Elaborada pelos autores.

---

Partindo da mesma premissa de que as três trajetórias são equiprováveis e o strike igual a R$ 30, o payoff da opção no vencimento nas três trajetórias deve ser: R$ 0,8849, R$ 0,8725 e R$ 0,9301, respectivamente. Resultando na média aritmética de R$ 0,8958, que, descontada a valor presente, deve ser o prêmio da opção:



C = 0,8958/e^(0,14(\%_(252))) = 0,8933



O preço da opção anterior, mais uma vez, é apenas um exemplo didático.

A média de longo prazo não precisa ser uma constante, pode ser uma variável dependente de variáveis exógenas observáveis. Suponha que o processo de reversão à média seja uma commodity, por exemplo, cuja média de longo prazo seja dependente do preço do barril de petróleo, ou pode ter a presença de sazonalidade. Ou seja, a média pode ser uma variável dependente y_t modelada da seguinte forma:



y_t = β' x_t + varepsilon_t   (6.55)



Sendo:

- x_t: matriz (n x m) de variáveis explicativas
- β: vetor (m x 1) de coeficientes da regressão

A média do preço do ativo pode seguir também um processo estocástico que pode ser estimado simultaneamente com o processo de reversão à média. Mais adiante discutiremos o processo de reversão à média do retorno de conveniência e de características específicas da modelagem de preços de commodities e seus respectivos contratos futuros.

A seguir, a Figura 6.4 exemplifica graficamente uma simulação de Monte Carlo, com diversas trajetórias projetadas para um processo de reversão à média.

---

Figura 6.4 | Simulação de Monte Carlo para reversão à média
![img-63.jpeg](img-63.jpeg)
Fonte: Elaborada pelos autores.

# 6.3 Precificação de opções de ações - Modelo de Black e Scholes

Para precificar uma opção de compra, call, de ação do tipo europeia sabendo que o preço do ativo na data de hoje seja S₀, o preço de exercício – strike – seja igual a K, que o vencimento ocorra em n dias úteis, qual deve ser o preço C dessa opção?

Vamos partir da premissa inicial de que o ativo não possua risco, ou seja, não possua volatilidade. Dessa maneira, o preço ou prêmio dessa call seria dado apenas pelo preço do ativo à vista, subtraído pelo strike descontado a valor presente, pela taxa livre de risco. Sabendo que o prêmio de uma opção não pode ser menor do que zero, o prêmio seria calculado, em ausência de risco, da seguinte forma:



5,00 × e^(0,1480 × (63 - 25)/252) = R\ 5,12 



---

Sendo:

Cᵢ: valor intrínseco da opção

S₀: o preço do ativo na data zero

r: taxa do ativo livre de risco

t: tempo até vencimento da opção

O prêmio da opção, partindo da premissa de ausência de risco no ativo à vista, é denominado como **valor intrínseco** da opção, e pode ser representado graficamente da seguinte forma:

Figura 6.5 | Representação do prêmio da opção – valor intrínseco, sem risco
![img-64.jpeg](img-64.jpeg)
Fonte: Elaborada pelos autores.

Na Figura 6.5, nota-se que, à medida que o preço do ativo-objeto aumenta, o valor intrínseco da call também aumenta.

Analisaremos o comportamento do prêmio de uma opção, agora, partindo da premissa mais realista de existência de risco no ativo-objeto, ou seja, com volatilidade.

Quando observamos o preço de uma opção no mercado, cujo ativo-objeto possui risco, o prêmio seria uma curva com valores maiores do que a observada no valor intrínseco:

Figura 6.6 | Representação do prêmio da opção com risco

---

![img-65.jpeg](img-65.jpeg)
Fonte: Elaborada pelos autores.

A figura anterior possui as terminologias *out*, *at* e *in the money*.

Apenas para reiterar, a *call at the money* ou no dinheiro é aquela cujo preço do ativo à vista é um valor próximo do *strike*. A *call in the money* ou dentro do dinheiro é aquela na qual o preço à vista é muito superior ao *strike*, com alta probabilidade de exercício, enquanto que na *call out of the money* ou fora do dinheiro, o preço do ativo à vista está abaixo do *strike*.

Portanto, podemos considerar que existe um prêmio acima do valor intrínseco quando o ativo possui risco e que esse prêmio depende do *moneyness* da opção.

As opções *at the money* possuem um prêmio de risco relativamente maior do que as opções *in* ou *out of the money*. Nestas últimas, o preço é bem próximo ao valor intrínseco, com pouco prêmio pelo risco.

É possível entender essas características das opções de forma intuitiva: quando o preço do ativo está próximo do *strike*, esse será o ponto de máxima incerteza, pois se o preço do ativo cair um pouco, a opção virará pó, enquanto que, se subir um pouco, dará exercício. Por essa razão, quando a opção está *at the money*, o prêmio pelo risco é máximo.

Podemos definir, portanto, que o preço da opção pode ser dado pelo seu valor intrínseco mais um prêmio pelo risco, ou valor extrínseco, conforme a seguinte relação:



C = C_t + prêmio pelo risco \ (6.57)



---

O modelo proposto por Black e Scholes (1973) permite a precificação do prêmio pelo risco.

Bernstein (1997, p. 313) disserta sobre a origem do modelo:

Na primavera de 1970, Scholes contou a Merton as dificuldades que ele e Black estavam tendo. O problema despertou imediatamente a interesse de Merton. Em pouco tempo, ele resolveu o dilema dos colegas, mostrando que eles estavam no caminho certo por motivos que eles próprios haviam ignorado. O modelo logo foi completado.

Quando adotamos o modelo de precificação de opções de Black e Scholes (1973, p. 640), os seguintes pressupostos devem ser assumidos:

- a taxa de juros de curto prazo do ativo livre de risco é conhecida e constante no tempo;
- o preço do ativo subjacente segue um processo de passeio aleatório em tempo contínuo;
- a distribuição dos possíveis valores do ativo subjacente no final de qualquer intervalo finito é lognormal, ou seja, não pode ser menor que zero;
- a variância do retorno do ativo subjacente é constante;
- a empresa não paga dividendos (o que pode ser corrigido com opções de ações protegidas de dividendos como as brasileiras);
- a opção é uma call do tipo europeu, ou seja, pode ser exercida apenas no vencimento.

A seguir apresentamos o modelo de Black e Scholes (1973, p. 640) para precificação de uma call europeia:

---



C = S ₀ N (d 1) - K e^(- r t) N (d 2)





d 1 = ln (S ₀/K) + t (σ²/2 + r)/σ √ {t} tag {6.58}





d 2 = ln (S ₀/K) + t (r - σ²/2)/σ √ {t} = d 1 - σ √ {t}



Sendo:

- N(d1): função densidade de probabilidade acumulada da variável normal padronizada d1
- N(d2): função densidade de probabilidade acumulada da variável normal padronizada d2
- K: preço de exercício da opção
- t: prazo até o vencimento da opção
- S_0: valor do ativo subjacente no instante zero
- r: taxa livre de risco na forma contínua
- σ: volatilidade constante até o vencimento da opção

É importante lembrar que todas as variáveis expostas anteriormente devem estar anualizadas, por exemplo, o prazo deverá estar em anos, a taxa de juros e a volatilidade, geralmente, são apresentadas na base 252 dias úteis.

Antes de apresentarmos exemplos de aplicação do modelo, vamos entender as características de duas variáveis importantes: d1 e d2. Estas duas variáveis são dois valores da distribuição de Z sim N(0,1) normal padronizada. O d2 estará sempre à esquerda de d1. Quando o valor de d1 é negativo, significa que a opção está out of the money, quando é positivo, consequentemente, significa que a opção está in the money e at the money, quando o valor de d1 é igual ou próximo de zero. A Figura 6.7 a seguir representa um exemplo da posição de d1 e d2:

---

Figura 6.7 | Variáveis d_1 e d_2
![img-66.jpeg](img-66.jpeg)
Fonte: Elaborada pelos autores.

N(d1) e N(d2) no modelo de Black e Scholes são as integrais da função normal padronizada, sendo N(d1) = ∫(-∞ até d1) f(z) dz, ou seja, a área da curva normal entre -∞ até d1, também conhecido como f.d.a (d1) ou também pode ser descrito como a P(-∞ < z < d1).

Os valores de N(d1) e N(d2) podem ser facilmente calculados com funções do Microsoft Excel, além de diversos aplicativos estatísticos.

# 6.3.1 Black e Scholes com taxa de juros na forma discreta

No modelo apresentado anteriormente, a taxa de juros deve ser inserida na forma contínua, porém, quando implementamos o modelo para o mercado brasileiro, geralmente utilizamos a taxa pré-fixada livre de risco para o período até o vencimento da opção na forma discreta. Nesse caso, precisamos converter essa taxa para a forma contínua antes de implementar o modelo:



r = ln (1 + i) (6.59)



---

Sendo:

i: taxa pré-fixada livre de risco, na forma discreta, no mercado brasileiro

Se fizermos o exponencial e elevarmos os dois lados da equação por t, teremos:



e^(rt) = (1 + i)^t (6.60)



Dessa maneira, é possível substituir a taxa de juros na forma contínua pela taxa de juros na forma discreta na equação de Black e Scholes, descontado o strike a valor presente pela taxa pré-fixada:



C = S_0 N(d1) - K/(1 + i)^t N(d2)





d1 = ln [ S_0/K (1 + i)^t ] + t ( σ^2/2 )/σ √(t) 





d2 = d1 - σ √(t)



De fato, ao converter a taxa de juros discreta para contínua, pode-se aplicar o modelo na forma original, a Equação 6.61 é apenas uma alternativa para implementar o modelo sem a necessidade dessa conversão de taxas fora do modelo. Mostraremos neste capítulo que o resultado da precificação da call é rigorosamente o mesmo nas duas versões do modelo.

---

# 6.3.2 Preço da put europeia de ações

O modelo de Black e Scholes também pode ser implementado para a precificação de uma put europeia de ação que não paga dividendos, da seguinte forma:



P = K e^(- r t) N (- d 2) - S ₀ N (- d 1)





d 1 = ln (S ₀/K) + t (σ²/2 + r)/σ √ {t} tag {6.62}





d 2 = d 1 - σ √ {t}



Lembrando que a taxa pré-fixada livre de risco discreta também deve ser convertida para a forma contínua antes de implementar a precificação da put, sendo r = ln (1 + i).

# 6.3.3 Cálculo da volatilidade

A volatilidade é calculada pelo desvio-padrão dos retornos contínuos do ativo-objeto que pode ser feito utilizando uma amostra histórica de preços.

Existem diversas maneiras de calcular a volatilidade histórica, Galdi e Pereira (2007, p. 74) sugerem duas diferentes formas: EWMA (Exponential Weighted Moving Average) e GARCH (Generalized Autoregressive Conditional Heteroskedasticity Model). Ao final do livro há o Anexo A, exemplificando o método de estimação da volatilidade, supondo um processo heterocedístico GARCH.

---

A volatilidade deve ser inserida no modelo de precificação de Black e Scholes na base anual com 252 dias úteis. Calcula-se o desvio-padrão dos retornos contínuos das cotações diárias da ação-objeto e depois é feita a anualização desse desvio, multiplicando-o por √(252), para isso, deve-se supor que os retornos contínuos são independentes e identicamente distribuídos (i.i.d.), sendo a covariância entre os retornos igual a zero e a variância constante no tempo, da seguinte forma:



Var[R_0 + ... + R_t] = Var[R_0] + ... + Var[R_t] 





Var[R_0 + ... + R_t] = tVar[R_t],  i.i.d.



Na equação anterior, a variância da soma dos retornos é igual a soma das variâncias, partindo da premissa de que a covariância é nula. Supondo que a variância é constante no tempo, tem-se que a variância anual é igual a variância diária multiplicada por 252. Logo, a volatilidade anualizada pode ser calculada da seguinte forma:



sigma_(anual) = √(252)sigma_(diária),  i.i.d.



O tamanho da amostra de retornos para o cálculo da volatilidade é bastante relativo, geralmente o tamanho mínimo da janela amostral necessária para o cálculo da volatilidade deverá ser do tamanho equivalente ao prazo até o vencimento da opção que se queira precificar.

## 6.3.4 Volatilidade com EWMA

Para calcular a volatilidade pode-se, alternativamente, utilizar uma técnica de decaimento exponencial da probabilidade, supondo que os retornos recentes possuem informação mais relevante, em termos de volatilidade, do que os retornos mais antigos. Uma forma simples de dar maior peso aos

---

retornos mais recentes é a adoção do EWMA para o ajuste exponencial da probabilidade dos retornos.

Supondo que a média e o desvio de uma determinada amostra de retornos são calculados com base em seus estimadores populacionais de média e variância:



E(R) = Σ(j=1 até n) P(R_j) R_j 





var(R) = Σ(j=1 até n) P(R_j) [ R_j - E(R) ]²



Sendo:

- n: tamanho da amostra de retornos
- P(R_j): probabilidade do retorno j-ésimo da amostra
- E(R): esperança do retorno
- var(R): variância do retorno

Em distribuições de probabilidade uniformes, os valores de P(R_j) são constantes e iguais a 1/n.

Para calcularmos a volatilidade EWMA, vamos decair o valor de R(R_j) à medida que o retorno fica mais antigo na amostra, utilizando um fator de decaimento exponencial λ.

Dessa maneira, podemos calcular a probabilidade do j-ésimo retorno da amostra da seguinte forma:



P(R_j) = λ^j/Σ(i=1 até n) λ^j 



O denominador da equação anterior é igual à soma dos termos de uma P.G.^1 finita de razão λ, que pode ser escrita, de forma mais concisa, da seguinte

---

maneira:



P (R _j) = λ^j (λ - 1)/(λ^n - 1) λ (6. 6 7)



Sendo que os estimadores dos parâmetros populacionais possam ser calculados com EWMA da seguinte forma:



{l} E_(E W M A) (R) = Σ(j = 1) ^n λ^j (λ - 1)/(λ^n - 1) λ R _j 
 v a r_(E W M A) (R) = Σ(j = 1) ^n λ^j (λ - 1)/(λ^n - 1) λ [ R _j - E_(E W M A) (R) ] ^p tag {6.68} 
 



E a volatilidade anualizada EWMA, sigma_(EWMA), calculada pela raiz quadrada da variância e multiplicada por √(252).

## Exemplo 6.1 - Aplicação do modelo de Black e Scholes para opções de ações

Agora, vamos fazer um exemplo de aplicação do modelo de Black e Scholes para precificar uma opção de ação negociada na B3.

No nosso exemplo, utilizaremos uma opção de compra de ação (call), de código VALEJ16, cujo preço de exercício é R$ 16,13, que vencerá daqui a exatos 34 dias úteis, sabendo que o preço da ação-objeto está, atualmente, à cotação de R$ 15,10.

Para isso, precisaremos utilizar a taxa de juros pré-fixada livre de risco de 14,23% a.a. e a volatilidade histórica de 42,30% a.a., na base 252 dias úteis.

Se quisermos usar o modelo na forma contínua, o primeiro passo é converter a taxa de juros pré-fixada na forma discreta para a forma contínua:



r = ln (1 + 0, 1423) = 0, 13304 tag {6.69}



Agora calculamos d1 e d2:

---



d1 = ln(15,10/16,13) + (34/252)(0,423^2/2 + 0,13304)/0,423√(34/252) = -0,23148 





d2 = -0,23148 - 0,423√(34/252) = -0,38685



Em seguida, obtemos os valores de N(d1) e N(d2), pela função densidade de probabilidade acumulada da normal padronizada (função disponível no Microsoft Excel) que são, respectivamente: 0,40847 e 0,34943. Logo, o preço da call de Vale será:



C = 15,10(0,40847) - 16,13/e^(0,13304(34/252))(0,34943) = 0,6319 



## Exemplo 6.2 - Precificação de opções de ações utilizando taxas discretas

Dando continuidade no exemplo anterior, podemos, alternativamente, utilizar o modelo com taxa de juros discreta, para isso, calculamos o strike, descontado a valor presente, pela taxa de juros pré-fixada livre de risco:



K/(1+i)^t = 16,13/(1+0,1423)^(34/252) = 15,84304 



Em seguida, calculamos d1 e d2:



d1 = ln(15,10/15,84304) + (34/252)(0,423^2/2)/0,423√(34/252) = -0,23148 





d2 = -0,23148 - 0,423√(34/252) = -0,38685



---

Com N(d1) e N(d2) calculados na normal padronizada acumulada, respectivamente: 0,40847 e 0,34943, obtemos o preço da call:



C = 15,10(040847) - 15,84304(0,34943) = 0,6319 \ (6.74)



O resultado obtido é rigorosamente igual ao obtido no exemplo anterior.

# 6.4 Precificação de opções de ações com pagamento de dividendos

Quando uma ação de uma companhia vira ex-dividendos, o valor dos dividendos é descontado do valor da ação, ou seja, reduz o valor da ação.

As nossas opções de ações negociadas em bolsa possuem proteção contra pagamento de dividendos. Quando a ação vira ex-dividendos, a bolsa abate o valor desses dividendos do preço de exercício, dessa forma não haverá perda para o titular da opção de compra nem ganhos para o titular da opção de venda negociadas em bolsa. Para fazer isso, a bolsa ajusta o valor dos dividendos até a data do vencimento da opção, pela taxa livre de risco.

Se não houvesse esse mecanismo de proteção, quando a empresa pagasse dividendos, o titular de uma call de ações teria uma perda no valor dos dividendos, caso não tivesse considerado os dividendos na precificação da opção.

Vamos apresentar o modelo destinado à precificação de opções de ações que não possuem proteção contra pagamento de dividendos, proposto por Merton (1973, p. 160).

O modelo é similar ao modelo original de Black e Scholes, adicionando uma nova variável, que é o dividend yield ou rentabilidade dos dividendos, na

---

forma contínua, representado pela letra q, partindo da premissa de que esta é uma variável conhecida e constante.

Supondo que, quanto maior o pagamento de dividendos esperado, maior será a redução no valor da ação. Dessa maneira, o dividend yield reduzirá, também, o valor da opção, ao reduzir o valor de S_0. Uma das alternativas é a de substituir o preço do ativo à vista, no modelo original, pelo preço do ativo reduzido pela taxa de dividendos, e precificar a opção normalmente.

Logo, vamos substituir S_0 por S_0 e^(-qt) na equação original de Black e Scholes e precificar uma call europeia com dividend yield igual a q:



C = S_0 e^(-qt) N(d1) - K e^(-rt) N(d2)





d1 = ln(S_0 e^(-qt)/K) + t(σ^2/2 + r)/σ √(t) 





d2 = d1 - σ √(t)



Considerando que ln(e^(-qt)) = -qt, teremos a equação de precificação de opções de ações com dividendos na sua forma mais conhecida:



C = S_0 e^(-qt) N(d1) - K e^(-rt) N(d2)





d1 = ln(S_0/K) + t(σ^2/2 + r - q)/σ √(t) 





d2 = d1 - σ √(t)



---

Sendo:

N(d1): função densidade de probabilidade acumulada da variável normal padronizada d1

N(d2): função densidade de probabilidade acumulada da variável normal padronizada d2

K: preço de exercício da opção

t: prazo até o vencimento da opção

S_0: valor do ativo subjacente no instante zero

r: taxa livre de risco na forma contínua

q: dividend yield na forma contínua

σ: volatilidade constante até o vencimento da opção

É conveniente reiterar que, tanto a taxa de juros quanto o dividend yield, geralmente são variáveis obtidas no mercado na forma discreta. Caso utilizemos o modelo Black e Scholes na sua forma original, as taxas precisam ser convertidas para a forma contínua antes de serem inseridas na equação. Isso é feito da seguinte maneira:



{l}
r = ln (1 + i) 

q = ln (1 + d)





Sendo:

i: taxa livre de risco pré-fixada na forma discreta

q: dividend yield na forma discreta

Sendo as variáveis d1 e d2 obtidas da mesma forma que na call, uma put europeia de ações, com taxa de dividendos q, pode ser precificada da seguinte maneira:



P = K e^(-rt) N(-d2) - S_0 e^(-qt) N(-d1)




Exemplo 6.3 - Precificação de opções com pagamento de dividendos

---

Vamos utilizar o exemplo anterior de aplicação do modelo de Black e Scholes para precificar uma opção de ação, agora com uma taxa de dividend yield esperada de 3% a.a., e sem proteção contra pagamento de dividendos. Esta será a opção de compra de ação (call), cujo preço de exercício é R$ 16,13, que vencerá daqui a 34 dias úteis, e o preço da ação-objeto VALE está atualmente à cotação de R$ 15,10. A taxa de juros pré-fixada considerada é de 14,23% a.a. e volatilidade histórica de 42,30% a.a., ambas na base 252 dias úteis.

O primeiro passo é converter a taxa de juros e o dividend yield, para a forma contínua:



{l}
r = ln (1 + 0,1423) = 0,13304 

q = ln (1 + 0,03) = 0,02956





Agora, calculamos d_1 e d_2:



d_2 = -0,23148 - 0,423 √(34/252) = -0,41252





d_1 = ln(15,10/16,13) + (34/252)(0,423^2/2 + 0,13304 - 0,02956)/0,423 √(34/252) = -0,25715




Em seguida, obtemos os valores de N(d_1) e N(d_2) pela probabilidade acumulada da normal padronizada: 0,39853 e 0,33998, respectivamente. Logo, o preço da call de Vale será:



C = 15,10/e^(0,02956(34/252))(0,39853) - 16,13/e^(0,13304(34/252))(0,33998) = 0,6075




Quando precificamos a opção anterior sem a taxa de dividendos, pelo modelo de Black e Scholes original, o preço obtido é R$ 0,6319, ao adicionar os dividendos no

---

modelo de Merton (1973), o preço ficou menor, R$ 0,6075. Isso ocorre porque, quanto maior o dividend yield menor será o preço da opção de ação.

# 6.5 Precificação de opções de ativos com custo de carregamento

Vamos partir da premissa que q na precificação de uma opção é o custo de carregamento. Por definição, o custo de carregamento é uma taxa de empréstimo do ativo, por exemplo, no caso do dólar é o cupom cambial, no caso das ações é o empréstimo de ações (Banco de Títulos Calispa – BTC), ou mesmo no caso de uma commodity, é o retorno de conveniência.

Para vender um ativo a descoberto, precisamos fazer um empréstimo do ativo e pagar o custo de carregamento q, para depois vendê-lo. Ao possuir um ativo à vista, teremos o custo oportunidade de emprestar esse ativo nessa mesma taxa q.

Logo, com a posse do ativo à vista, deveremos descontar o custo de carregamento, o mesmo ocorrerá com a precificação de uma opção de compra desse ativo, também deveremos descontar o custo de carregamento.

A interpretação do custo de carregamento em precificação de opções é similar à taxa de dividendos no modelo de Merton (1973), ou seja, também se substitui S_0 por S_0 e^(-qt) na equação original de Black e Scholes, partindo da premissa de que q é o custo de carregamento.

# 6.6 Precificação de opções de moeda com cupom cambial

---

O modelo de Garman e Kohlhagen (1983) é utilizado para precificação de opções de moeda, considerando que o custo de carregamento é a taxa de juros livre de risco na moeda-objeto da opção a qual se deseja precificar. Por exemplo, se queremos precificar uma opção de dólar, utilizaremos uma taxa de juros livre de risco em dólar.

O modelo para precificação de opções de moeda, com a taxa de juros na moeda-objeto é apresentado da seguinte forma para uma call:



C = S ₀ e^(- r _f t) N (d 1) - K e^(- r t) N (d 2)





d 1 = ln (S ₀/K) + t (σ²/2 + r - r _f)/σ √ {t} tag {6.82}





d 2 = d 1 - σ √ {t}



Sendo:

- **N(d1)**: função densidade de probabilidade acumulada da variável normal padronizada d1
- **N(d2)**: função densidade de probabilidade acumulada da variável normal padronizada d2
- **K**: preço de exercício da opção em cotação na moeda
- **t**: prazo até o vencimento da opção
- **S₀**: cotação atual da moeda no instante zero
- **r**: taxa livre de risco doméstica na forma contínua
- **σ**: volatilidade constante até o vencimento da opção

Alternativamente, para precificar uma opção de dólar em reais, vamos considerar que a taxa de juros em dólar no Brasil é o cupom cambial,

---

apresentado na base linear 360. Dessa maneira, uma call de dólar deveria ser precificada da seguinte maneira:



C = S ₀/(1 + c c n_(d c)/3 6 0) N (d 1) - K/(1 + i)^(n_(d c)/2 5 2) N (d 2)





d 1 = ln (S ₀ (1 + i)^(n_(d u)/2 5 2)/K (1 + c c n_(d c)/3 6 0)) + (n_(d u)/2 5 2) (σ²/2)/σ √ {n_(d u)/2 5 2} tag {6.83}





d 2 = d 1 - σ √ {n_(d u)/2 5 2}



Sendo:

- cc: cupom cambial do dólar na base linear 360
- n_(du): número de dias úteis até o vencimento da opção
- n_(dc): número de dias corridos até o vencimento da opção
- i: taxa de juros pré-fixada livre de risco em reais

Sendo que d1 e d2 são calculados da mesma forma que na call, o valor da put de dólar em reais poderia ser calculado da seguinte forma:



P = K/(1 + i)^(n_(d c)/2 5 2) N (- d 2) - S ₀/(1 + c c . n_(d c)/3 6 0) N (- d 1) tag {6.84}



Exemplo 6.4 - Precificação de opção de moeda

Vamos fazer um exemplo de precificação de uma opção de dólar, considerando o cupom cambial como variável de entrada do modelo. Suponha que a cotação do

---

dólar está atualmente a R$ 3,22 e queremos precificar uma opção de compra de dólar, call, com preço de exercício igual a R$ 3,25 que vencerá em 86 dias úteis ou 126 dias corridos.

A taxa de juros pré-fixada em reais é de 12,80% a.a., na base exponencial 252 dias úteis, enquanto que o cupom cambial está a 2,70% a.a., na base linear 360 dias corridos. Sabendo que a volatilidade do dólar é 27% a.a., os valores de d1 e d2 seriam obtidos da seguinte maneira:



d1 = ln (3,22(1+0,128)^(86/252)/3,25(1+0,027.126/360)) + (86/252)(0,27^2/2)/0,27√{86/252} = 0,22104 tag {6.85}





d2 = 0,22104 - 0,27√{86/252} = 0,06331



Os valores de N(d1) e N(d2) são, respectivamente, 0,58747 e 0,52524. Com isso, podemos calcular o valor da call de dólar:



C = 3,22/(1+0,027.126/360) · 0,58747 - 3,25/(1+0,128)^(86/252) · 0,52524 = 0,23566 tag {6.86}



O preço da call seria de R$ 0,23566 por dólar.

# 6.7 Precificação de opções sobre futuros de moeda e índice de bolsa

---

O modelo de Merton (1973) pode ser utilizado com o custo de carregamento q no ativo, de tal maneira que se substitui S_0 por S_0 e^(-qt) na equação de Black e Scholes, pois q pode ser considerado como um custo de oportunidade e redutor do valor do preço à vista. Vamos revisitar a equação de arbitragem entre o preço à vista e contratos a termo, em que o preço do ativo à vista, descontado pelo custo de carregamento, é igual ao preço do contrato a termo, descontado pela taxa de juros livre de risco:



S_0 e^(-qt) = F e^(-rt)   (6.87)



Partindo da premissa de que a mesma relação para contratos a termo pode ser feita para contratos futuros, em condição de não arbitragem, substitui-se S_0 e^(-qt) por F e^(-rt) na equação de Merton (1973) e obtemos a equação para precificação de opções sobre futuros sugerida por Black (1976):



C = e^(-rt) [ FN(d1) - KN(d2) ]





d1 = ln(F/K) + t(σ^2/2)/σ √(t) 





d2 = d1 - σ √(t)



Sendo d1 e d2 obtidos da mesma forma que na call, o valor da put sobre futuros pode ser calculado da seguinte maneira:



P = e^(-rt) [ KN(-d2) - FN(-d1) ]   (6.89)



---

As equações anteriores podem ser utilizadas para precificação de opções de futuro dólar e índice de bolsa, no caso em que o vencimento da opção seja o mesmo do contrato futuro.

Na verdade, o modelo de Black é muito prático para precificação de opções de qualquer ativo-objeto, que possua contratos futuros, quando comparado aos modelos de Merton (1973) e de Garman e Kohlhagen (1983).

O modelo de Black (1976) apresenta sua utilidade também para precificação de opções de dólar negociadas no mercado de balcão, mesmo não tendo o contrato futuro de dólar com vencimento equivalente ao da opção. Isso é possível porque podemos projetar uma curva de dólar por arbitragem, obtendo um dólar futuro sintético e precificar a opção utilizando o modelo de Black.

## Exemplo 6.5 - Precificação de opção de futuro de Índice BOVESPA

Um contrato futuro de IBOVESPA que vence daqui a 29 dias úteis está cotado a 56.220 pontos. Vamos precificar uma call de strike igual de 56.100 pontos, de mesmo vencimento do contrato futuro, sabendo que a volatilidade do IBOVESPA é de 42% a.a. e a taxa de juros livre de risco está a 12,90% a.a., ambas na base 252 dias úteis.

Vamos converter a taxa de juros pré-fixada para a forma contínua:



r = ln (1 + 0,1290) = 0,12133 



Calculamos d_1 e d_2:



d_1 = ln(56220/56100) + 29/252(0,42^2/2)/0,42√(29/252) = 0,08624 





d_2 = 0,08624 - 0,42√(29/252) = -0,05624



---

Os valores de N(d1) e N(d2) são, respectivamente, 0,53436 e 0,47757. Logo, o valor da call de futuro de IBOVESPA será:



C = e^(-0,12133^(29)/252) [ 56.220(0,53436) - 56.100(0,47757) ] = 3.204,76 



Ou seja, R$ 3.204,76 para cada opção sobre contrato futuro de IBOVESPA.

## Exemplo 6.6 - Precificação de opção de futuro de dólar

O contrato futuro de dólar, que vence em 17 dias úteis, está cotado em 3.210 pontos, em reais para cada US$ 1.000. Vamos precificar uma call de dólar de strike igual de 3.200 pontos, de mesmo vencimento que o contrato futuro, sabendo que a volatilidade do dólar é de 27% a.a. e a taxa de juros livre de risco está a 12,90% a.a., ambas na base 252 dias úteis.

A taxa de juros pré-fixada, convertida para a forma contínua, é de 0,12133. Os valores de d1 e d2 serão:



d1 = ln (3.210/3.200) + 17/252 (0,27^2/2)/0,27 √(17/252) = 0,07956 





d2 = 0,07956 - 0,27 √(17/252) = 0,00943



Os valores de N(d1) e N(d2) são 0,53170 e 0,50376, respectivamente. O valor da call de dólar será:



C = e^(-0,12133^(17)/252) [ 3.210(0,53170) - 3.200(0,50376) ] = 93,96 



Portanto, o preço da opção de dólar será de R$ 93,96 para cada US$ 1.000.

---

# 6.8 Precificação de opções de taxas de juros

O modelo de Black (1976), de opções sobre futuros, pode ser utilizado para a precificação de opções de juros, mais especificamente, opções de Índice DI (IDI). O IDI é calculado pela acumulação das taxas diárias do DI.

O objeto negociado na opção de IDI é compra ou venda de taxas de juros, ao comprar uma call de IDI, estamos comprados em taxas de juros, pagando um prêmio por isso.

A opção de IDI pode ser utilizada como alternativa para hedge de taxa de juros, quando se deseja proteger uma carteira de títulos pré-fixados contra uma eventual alta na taxa de juros.

Para precificar uma opção de IDI vamos utilizar o contrato futuro de DI, pois ambos possuem vencimentos na mesma data.

A volatilidade da opção de IDI é calculada pelo desvio-padrão dos retornos logaritmos do Preço Unitário (PU), com duração constante.

## Exemplo 6.7 - Precificação de opção de IDI

Uma opção de compra de IDI vence em 335 dias úteis, o seu preço de exercício é de 266.000 pontos. O contrato futuro de mesmo vencimento está negociado à taxa de 12,80% a.a. na base 252 dias úteis. Hoje, o IDI está a 215.694,62 pontos, a R$ 1 por ponto. A volatilidade de duração constante – 335 dias úteis – é de 13% a.a.

Para precificar a opção, o primeiro passo é calcular o IDI esperado, para o vencimento da opção, levando o IDI a valor futuro pela taxa do contrato futuro de DI:



F = 215.694,62(1 + 0,128)^(335/252) = 253.149,58   (6.95)



Agora, calculamos os valores de d_1 e d_2 da call de IDI, pelo modelo de opções sobre futuros:

---



d1 = ln(253.149,58/266.000) + 335/252 (0,13^2/2)/0,13 √(335/252) = -0,25541 





d2 = -0,25541 - 0,13 √(335/252) = -0,40530



Não é necessário converter a taxa do contrato futuro de DI para forma contínua, vamos utilizá-la na forma discreta, sabendo que e^(ct) = (1 + i)^t. Os valores de N(d1) e N(d2), com base na probabilidade da curva normal, são 0,39920 e 0,34263, respectivamente.

Logo, o valor da call de IDI será:



C = [253.149,58(0,39920) - 266.000(0,34263)]/(1 + 0,128)^(335/252) = 8.451,17 



Ou seja, o preço da opção de IDI será de R$ 8.451,17.

# 6.9 Precificação de opções perpétuas

Opções perpétuas são aquelas nas quais existe a possibilidade de um exercício antecipado, porém essas não possuem data específica de vencimento.

Para poder precificar essas opções, supõe-se que as opções perpétuas podem ser exercidas quando o preço da ação atinge uma barreira ótima para o exercício. Antes de atingir essa barreira ótima, o detentor da opção não a exerce, sendo que essa opção continua válida indefinidamente.

---

Não há uma fórmula fechada para o cálculo de opções americanas, mas é possível obter uma fórmula para o cálculo de opções com um tempo infinito para o vencimento.

A razão para isso, segundo Haug (2007), é que o tempo para o vencimento será sempre o mesmo, infinito, independentemente da passagem do tempo. Ou seja, não importa o momento no qual vamos avaliar uma opção perpétua, o prazo será sempre o mesmo, infinito. Dessa forma, o período para o vencimento não depende do momento no qual avaliamos a opção, o que torna o processo de avaliação independente do tempo.

A fórmula fechada para o cálculo de uma *call* americana perpétua é dada pela seguinte equação:



C = K/y ₁ - 1 [ (y ₁ - 1) S ₀/y ₁ K ]^(y ₁) tag {6.98}



O valor de y₁ é obtido da seguinte forma:



y ₁ = 1/2 - r - q/σ² + √ {(r - q/σ² - 1/2) ² + 2 r/σ²} tag {6.99}



E a barreira ótima de exercício B^* dessa *call* é dada pela seguinte equação:



B ^* = K (y ₁/y ₁ - 1)   (6.100)



Sendo:

- C: prêmio da *call*
- K: preço de exercício da opção de compra

---

S₀: preço à vista da ação, na data de referência (data-base ou dia da precificação)

r: taxa livre de risco na forma contínua

q: taxa anual de pagamento de dividendos na forma contínua

Uma put perpétua pode ser calculada da seguinte forma:



P = K/1 - y ₂ [ (y ₂ - 1)/y ₂ S ₀/K ]^(y ₂) tag {6.101}



Em que y₂ é obtido da seguinte maneira:



y ₂ = 1/2 - r - q/σ² - √ {(r - q/σ² - 1/2) ² + 2 r/σ²} tag {6.102}



E a barreira ótima de exercício dessa put perpétua é obtida a partir da seguinte equação:



B ^* = K (y ₂/y ₂ - 1) tag {6.103}



## Exemplo 6.8 - Precificação de uma opção perpétua

Vamos exemplificar uma put que oferece o direito de vender uma determinada ação perpetuamente, ou seja, esse direito não expira. O preço da ação hoje é de R$ 22 e o preço de exercício é de R$ 24, supondo uma taxa de juros de longo prazo de 10% a.a.o., uma volatilidade esperada de 42% a.a.o. e um dividend yield de 3% a.a. Nesse caso, é relativamente difícil estimar a volatilidade e a taxa de juros, pois não há prazo para essa projeção, dado que a opção não possui maturidade fixa.

---

Primeiro, vamos calcular os valores da taxa de juros e os dividendos na forma contínua:



{l}
r = ln (1 + 0,10) = 0,09531 

q = ln (1 + 0,03) = 0,02956





E, agora, calculamos o valor de y_2:



{l}
y_2 = 1/2 - 0,09531 - 0,02956/0,42^2 - √( ( 0,09531 - 0,02956/0,42^2 - 1/2 )^2 + 2(0,09531)/0,42^2 ) 

y_2 = -0,92003





Podemos calcular também o valor da barreira ótima:



B^* = 24 [ (-0,92003)/(-0,92003) - 1 ] = 11,50




A barreira ótima é de R$ 11,50 e o valor da put perpétua será de R$ 6,88 conforme o resultado dos seguintes cálculos:



P = 24/1 - (-0,92003) { [ (-0,92003) - 1/(-0,92003) ] 22/24 }^((-0,92003)) = 6,88




# 6.10 Precificação de opções com barreira

---

Neste tópico apresentamos o modelo de Reiner e Rubinstein (1991) para precificar opções com barreira. O escopo desse modelo é a precificação de opções de exercício do tipo europeu e verificação americana da barreira, ou seja, a todo instante verifica-se se o preço do ativo-objeto atingiu a barreira.

Nas opções com barreira do tipo knock-in, os direitos e obrigações relativos ao exercício da opção passam a existir caso o preço do ativo-objeto atinja a barreira definida no contrato antes do vencimento da opção. Já nas opções do tipo knock-out, os direitos e as obrigações relativos ao exercício da opção deixam de existir caso o preço do ativo-objeto atinja a barreira definida no contrato antes do vencimento da opção.

Além de diferenciar as opções do tipo in e out, também é necessário identificar se a barreira deverá ser atingida por uma trajetória ascendente do preço do ativo-objeto (up) ou descendente (down) a partir do preço inicial do ativo-objeto, S_0, no momento da precificação.

Logo, podemos classificar as opções com barreira em quatro tipos básicos:

- up-and-out: é quando o preço do ativo-objeto, S_0, está abaixo do preço da barreira e os direitos e as obrigações relativos ao exercício da opção deixam de existir caso o preço do ativo-objeto atinja a barreira;
- up-and-in: é quando o preço do ativo-objeto, S_0, está abaixo do preço da barreira e os direitos e as obrigações relativos ao exercício da opção passam a existir caso o preço do ativo-objeto atinja a barreira;
- down-and-out: é quando o preço do ativo-objeto, S_0, está acima do preço da barreira e os direitos e as obrigações relativos ao exercício da opção deixam de existir caso o preço do ativo-objeto atinja a barreira;
- down-and-in: é quando o preço do ativo-objeto, S_0, está acima do preço da barreira e os direitos e as obrigações relativos ao exercício da opção passam a existir caso o preço do ativo-objeto atinja a barreira.

---

As variáveis que influenciam o preço de uma opção com barreira são as mesmas de uma opção plain vanilla, precificada pelo modelo de Black e Scholes (1973). Porém, nas opções com barreira, outros fatores também influenciam em seu preço:

- o tipo de barreira (in ou out);
- a diferença entre o preço de exercício e o preço de barreira;
- a diferença entre o preço do ativo-objeto e o preço da barreira.

Quanto mais improvável for o conjunto de trajetórias que resultarão em exercício da opção, menor será o preço da opção.

Quando comparamos os preços de diferentes opções, quanto mais inusitadas forem as trajetórias do ativo-objeto para ocorrer o exercício, menor será o preço da opção. Fazendo uma comparação entre as opções com barreira e as opções plain vanilla é importante entendermos que as barreiras colocam restrições de exercício ao detentor da opção. Logo, as opções com barreira serão mais baratas que as opções plain vanilla.

Pense da seguinte maneira, se você detém um direito, você quer que esse direito seja o mais irrestrito possível. A partir do momento que são colocadas limitações nesse direito, menos desejável ele será ao seu detentor, ou seja, menos o direito valerá.

Voltando ao modelo de Reiner e Rubinstein (1991), é importante mencionar que existem várias maneiras de apresentá-lo, conforme literaturas nacional e internacional.

O modelo é, na verdade, um conjunto de fórmulas, que contemplam as 16 combinações possíveis de precificação de opções com barreira, que consideram as seguintes características: call ou put, in ou out, up ou down e se o preço de exercício for maior ou menor do que o da barreira. A diferença na forma de apresentação está na convenção da notação e de como subdividir as fórmulas.

---

A seguir, vamos definir as variáveis que serão utilizadas na precificação das opções com barreira:

S₀: preço do ativo-objeto

K: preço de exercício da opção

t: prazo até a data de exercício da opção

r: taxa de juros livre de risco na forma contínua

q: dividendos, na forma contínua

σ: volatilidade do retorno do ativo-objeto

H: preço da barreira (knock-in ou knock-out)

Estas são as equações das variáveis auxiliares que facilitarão os cálculos das opções com barreira:



A = varnothing S₀ e^(-qt) N(varnothing x₁) - varnothing K e^(-rt) N(varnothing x₁ - varnothing σ √(t))   (6.108)





A = varnothing S₀ e^(-qt) N(varnothing x₁) - varnothing K e^(-rt) N(varnothing x₁ - varnothing σ √(t))   (6.109)





C = varnothing S₀ e^(-qt) (H/S₀)^(2(μ + 1)) N(eta y₁) - varnothing K e^(-rt) (H/S₀)^(2μ) N(eta y₁ - eta σ √(t))   (6.110)





D = varnothing S₀ e^(-qt) (H/S₀)^(2(μ + 1)) N(eta y₂) - varnothing K e^(-rt) (H/S₀)^(2μ) N(eta y₂ - eta σ √(t))   (6.111)



Sendo:



λ = r - q + σ²/2   (6.112)



---



μ = λ - 1   (6.113)





x_1 = ln(S_0/K)/σ√(t) + (1 + μ)σ√(t)   (6.114)





x_2 = ln(S_0/H)/σ√(t) + (1 + μ)σ√(t)   (6.115)





y_1 = ln(H^2/S_0 K)/σ√(t) + (1 + μ)σ√(t)   (6.116)





y_2 = ln(H/S_0)/σ√(t) + (1 + μ)σ√(t)   (6.117)



Vamos definir mais algumas variáveis utilizadas nas equações anteriores:




varnothing = +1, & se a opção for call 

varnothing = -1, & se a opção for put







eta = +1, & se o tipo de barreira for down 

eta = -1, & se o tipo de barreira for up




Então, podemos escrever as fórmulas de precificação das opções com barreira conforme as fórmulas a seguir, para as diversas possibilidades de put ou call, up ou down, in ou out.

Quando o preço de exercício for maior do que o da barreira (K > H):



Call_(down-and-in) = C   (6.118)



---



Put_(down-and-in) = B - C + D \ (6.119)





Call_(up-and-in) = A \ (6.120)





Put_(up-and-in) = A - B + D \ (6.121)





Call_(down-and-out) = A - C \ (6.122)





Put_(down-and-out) = A - B + C - D \ (6.123)





Call_(up-and-out) = O \ (6.124)





Put_(up-and-out) = B - D \ (6.125)



Quando o preço de exercício for menor do que o da barreira (K < H):



Call_(down-and-in) = A - B + D \ (6.126)





Put_(down-and-in) = A \ (6.127)





Call_(up-and-in) = B - C + D \ (6.128)





Put_(up-and-in) = C \ (6.129)





Call_(down-and-out) = B - D \ (6.130)





Put_(down-and-out) = O \ (6.131)





Call_(up-and-out) = A - B + C - D \ (6.132)





Put_(up-and-out) = A - C \ (6.133)



## 6.10.1 Aplicação de precificação de opção com barreira

---

Caso você esteja usando este livro para implementar o modelo de Reiner e Rubinstein no Microsoft Excel ou em algum outro software, achamos útil precificar cada um dos 16 tipos de opções e listar os valores das variáveis principais em cada tipo de opção. O processo de validação é bastante relevante antes de usarmos qualquer modelo de precificação. Sempre que possível, valide o seu modelo com algum software disponível. Neste livro, nós validamos as fórmulas anteriores das opções com barreira com o software Derivagem, disponível no site do Professor John Hull.

Para precificar todas as 16 possíveis opções com barreira do modelo de Reiner e Rubinstein (1991) mantivemos constantes algumas variáveis das opções, como preço do ativo-objeto, prazo, taxa de juros livre de risco, volatilidade e dividendos. Na Tabela 6.5 estão os dados do exemplo da opção que iremos precificar para os diversos tipos de barreira. Partimos da premissa de que as taxas a seguir estão em sua forma contínua e anualizada:

Tabela 6.5 | Dados do exemplo de opções com barreira
|  Variável | Valor  |
| --- | --- |
|  S₀ = | 100,00  |
|  t = | 0,25  |
|  r = | 10,00%  |
|  σ = | 30,00 %  |
|  q = | 0,00%  |

Fonte: Elaborada pelos autores.

# 1. Opções do tipo down, quando o strike é maior do que a barreira

Utilizando os dados da tabela anterior vamos precificar opções do tipo down, quando K > H, a Tabela 6.6 apresenta os valores do exemplo para a barreira e o strike:

Tabela 6.6 | O preço de exercício é maior do que o da barreira, K > H

---

|  Variável | Valor  |
| --- | --- |
|  K = | 90,00  |
|  H = | 80,00  |

Fonte: Elaborada pelos autores.

Utilizando as equações de precificação com barreira, calculamos as variáveis auxiliares. Primeiro, vamos calcular o μ:



μ = 0,10 + 0,30^2/2/0,30^2 - 1 = 0,6111



Agora, vamos calcular o x_1:



x_1 = ln(100/90)/0,30√(0,25) + (1 + 0,6111)0,30√(0,25) = 0,9441



Calculamos, agora, o x_2:



x_2 = ln(100/80)/0,30√(0,25) + (1 + 0,6111)0,30√(0,25) = 1,7293



Por fim, o y_1 e y_2:

---



y ₁ = ln (8 0 ²/1 0 0 × 9 0)/0 , 3 0 √ {0 , 2 5} + (1 + 0, 6 1 1 1) 0, 3 0 √ {0 , 2 5} = - 2, 0 3 1 2





y ₂ = ln (8 0/1 0 0)/0 , 3 0 √ {0 , 2 5} + (1 + 0, 6 1 1 1) 0, 3 0 √ {0 , 2 5} = - 1, 2 4 6 0



Os resultados estão resumidamente apresentados na tabela a seguir:

Tabela 6.7 | Variáveis auxiliares – Parte 1

|  μ | x₁ | x₂ | y₁ | y₂  |
| --- | --- | --- | --- | --- |
|  0,6111 | 0,9441 | 1,7293 | -2,0312 | -1,2460  |

Fonte: Elaborada pelos autores.

Agora, calculamos os valores de A, B, C e D. Exemplificaremos os cálculos de uma call do tipo doWn-and-in e registraremos os valores na Tabela 6.8 para as outras opções do tipo doWn para K > H:



A = 1 × 1 0 0 e^(- 0 × 0, 2 5) N (1 × 0, 9 4 4 1) - 1 × 9 0 e^(- 0, 1 0 × 0, 2 5) N (1 × 0, 9 4 4 1 - 1 × 0, 3 0 √ {0 , 2 5}) = 1 3, 7 1 2 8





B = 1 × 1 0 0 e^(- 0 × 0, 2 5) N (1 × 1, 7 2 9 3) - 1 × 9 0 e^(- 0, 1 × 0, 2 5) N (1 × 1, 7 2 9 3 - 1 × 0, 3 0 √ {0 , 2 5}) = 1 3, 0 4 9 4





C = 1 × 1 0 0 e^(- 0 × 0, 2 5) (8 0/1 0 0)^(2 (0, 6 1 1 1 + 1)) N (1 × - 2, 0 3 1 2) - 1 × 9 0 e^(- 0, 1 × 0, 2 5) (8 0/1 0 0)^(2 × 0, 6 1 1 1) N (1 × - 2, 0 3 1 2 - 1 × 0, 3 0 √ {0 , 2 5}) = 0, 0 5 4 3





D = 1 × 1 0 0 e^(- 0 × 0, 2 5) (8 0/1 0 0)^(2 (0, 6 1 1 1 + 1)) N (1 × - 1, 2 4 6 0) - 1 × 9 0 e^(- 0, 1 × 0, 2 5) (8 0/1 0 0)^(2 × 0, 6 1 1 1) N (1 × - 1, 2 4 6 0 - 1 × 0, 3 0 √ {0 , 2 5}) = - 0, 2 5 3 2 5



Tabela 6.8 | Variáveis auxiliares – Parte 2

|  Opção | A | B | C | D  |
| --- | --- | --- | --- | --- |

---

|  Call_(down-and-in) | 13,7128 | 13,0494 | 0,0543 | -0,2535  |
| --- | --- | --- | --- | --- |
|  Put_(down-and-in) | 1,4907 | 0,8273 | -0,0543 | 0,2535  |
|  Call_(down-and-out) | 13,7128 | 13,0494 | 0,0543 | -0,2535  |
|  Put_(down-and-out) | 1,4907 | 0,8273 | -0,0543 | 0,2535  |

Fonte: Elaborada pelos autores.

Então, calculamos as seguintes possibilidades de opções do tipo down, que verifica a barreira em caso de queda do preço do ativo:



Call_(down-and-in) = 0,0543





Put_(down-and-in) = 0,8273 - (-0,0543) + 0,2535 = 1,1351





Call_(down-and-out) = 13,7125 - 0,0543 = 13,6585





Put_(down-and-out) = 1,4907 - 0,8273 + (-0,0543) - 0,2535 = 0,3556



Consolidamos os resultados do cálculo do prêmio das opções na tabela a seguir:

Tabela 6.9 | Preços das opções com barreira do tipo down e K > H

|  Opção | Prêmio  |
| --- | --- |
|  Call_(down-and-in) | 0,0543  |
|  Put_(down-and-in) | 1,1351  |
|  Call_(down-and-out) | 13,6585  |
|  Put_(down-and-out) | 0,3556  |

Fonte: Elaborada pelos autores.

2. Opções do tipo up, quando o strike é maior do que a barreira

---

Agora, vamos precificar opções do tipo up, quando K > H, a tabela seguinte apresenta o strike e a barreira:

Tabela 6.10 | O preço de exercício é maior do que o da barreira, K > H

|  Variável | Valor  |
| --- | --- |
|  K = | 120,00  |
|  H = | 110,00  |

Fonte: Elaborada pelos autores.

Calculamos as variáveis auxiliares, cujos resultados são apresentados nas tabelas a seguir:

Tabela 6.11 | Variáveis auxiliares – Parte 1

|  μ | x₁ | x₂ | y₁ | y₂  |
| --- | --- | --- | --- | --- |
|  0,6111 | -0,9738 | -0,3937 | 0,2970 | 0,8771  |

Fonte: Elaborada pelos autores.

Tabela 6.12 | Variáveis auxiliares – Parte 2

|  Opção | A | B | C | D  |
| --- | --- | --- | --- | --- |
|  Call_(up-and-in) | 1,2287 | 0,3604 | -5,9643 | -4,8557  |
|  Put_(up-and-in) | 18,2659 | 17,3976 | 5,9643 | 4,8557  |
|  Call_(up-and-out) | 1,2287 | 0,3604 | -5,9643 | -4,8557  |
|  Put_(up-and-out) | 18,2659 | 17,3976 | 5,9643 | 4,8557  |

Fonte: Elaborada pelos autores.

Calculamos as seguintes possibilidades de opções do tipo up, que verifica a barreira em caso de queda do preço do ativo:

Tabela 6.13 | Preços das opções com barreira do tipo up e K > H

---

|  Opção | Prêmio  |
| --- | --- |
|  Call_(up-and-in) | 1,2287  |
|  Put_(up-and-in) | 5,7240  |
|  Call_(up-and-out) | 0,0000  |
|  Put_(up-and-out) | 12,5419  |

Fonte: Elaborada pelos autores.

# 3. Opções do tipo `down`, quando o `strike` é menor do que a barreira

Agora, vamos precificar as opções do tipo `down`, quando K < H, a seguinte tabela apresenta os valores de preço de exercício e barreira:

Tabela 6.14 | O preço de exercício é menor do que o da barreira, K < H

|  Variável | Valor  |
| --- | --- |
|  K = | 80,00  |
|  H = | 90,00  |

Fonte: Elaborada pelos autores.

Calculamos as variáveis auxiliares, cujos resultados são apresentados nas tabelas a seguir:

Tabela 6.15 | Variáveis auxiliares – Parte 1

|  μ | x₁ | x₂ | y₁ | y₂  |
| --- | --- | --- | --- | --- |
|  0,6111 | 1,7293 | 0,9441 | 0,3245 | -0,4607  |

Fonte: Elaborada pelos autores.

Tabela 6.16 | Variáveis auxiliares – Parte 2

|  Opção | A | B | C | D  |
| --- | --- | --- | --- | --- |
|  Call_(down-and-in) | 22,2453 | 21,3828 | 5,6163 | 4,3974  |

---

|  Put_(down-and-in) | 0,2701 | -0,5924 | -5,6163 | -4,3974  |
| --- | --- | --- | --- | --- |
|  Call_(down-and-out) | 22,2453 | 21,3828 | 5,6163 | 4,3974  |
|  Put_(down-and-out) | 0,2701 | -0,5924 | -5,6163 | -4,3974  |

Fonte: Elaborada pelos autores.

E, então, calculamos as seguintes possibilidades de opções do tipo down, que verifica a barreira em caso de aumento do preço do ativo:

Tabela 6.17 | Preços das opções com barreira do tipo down e K < H

|  Opção | Prêmio  |
| --- | --- |
|  Call_(down-and-in) | 5,2598  |
|  Put_(down-and-in) | 0,2701  |
|  Call_(down-and-out) | 16,9855  |
|  Put_(down-and-out) | 0,0000  |

Fonte: Elaborada pelos autores.

# 4. Opções do tipo up, quando o strike é menor do que a barreira

Agora, vamos precificar as opções do tipo up, quando K < H:

Tabela 6.18 | O preço de exercício é menor do que o da barreira, K < H

|  Variável | Valor  |
| --- | --- |
|  K = | 110,00  |
|  H = | 120,00  |

Fonte: Elaborada pelos autores.

Calculamos as variáveis auxiliares, os resultados são apresentados a seguir:

---

Tabela 6.19 | Variáveis auxiliares – Parte 1

|  μ | x₁ | x₂ | y₁ | y₂  |
| --- | --- | --- | --- | --- |
|  0,6111 | -0,3937 | -0,9738 | 2,0372 | 1,4571  |

Fonte: Elaborada pelos autores.

Tabela 6.20 | Variáveis auxiliares – Parte 2

|  Opção | A | B | C | D  |
| --- | --- | --- | --- | --- |
|  Call_(up-and-in) | 3,2211 | 2,5019 | -0,2183 | 0,2388  |
|  Put_(up-and-in) | 10,5052 | 9,7860 | 0,2183 | -0,2388  |
|  Call_(up-and-out) | 3,2211 | 2,5019 | -0,2183 | 0,2388  |
|  Put_(up-and-out) | 10,5052 | 9,7860 | 0,2183 | -0,2388  |

Fonte: Elaborada pelos autores.

Então, calculamos as seguintes possibilidades de opções do tipo up, que verifica a barreira em caso de aumento do preço do ativo:

Tabela 6.21 | Preços das opções com barreira do tipo up e K < H

|  Opção | Prêmio  |
| --- | --- |
|  Call_(up-and-in) | 2,9590  |
|  Put_(up-and-in) | 0,2183  |
|  Call_(up-and-out) | 0,2621  |
|  Put_(up-and-out) | 10,2869  |

Fonte: Elaborada pelos autores.

# RESUMO

Neste capítulo, apresentamos apenas os modelos de precificação de opções mais utilizados e conhecidos da literatura financeira. Atualmente, os artigos acadêmicos sobre os modelos de precificação de opções possuem uma vasta abordagem. É um tema rico e amplamente explorado.

---

EXERCÍCIOS PROPOSTOS

1. Precifique *call* de ação protegida de dividendos:
- Strike: R$ 36,00
- Prazo: 22 dias úteis
- Preço da ação à vista: 35,70
- Taxa de juros: 7,80% a.a.o.
- Volatilidade: 39% a.a.o.

2. Precifique uma *call* de dólar (US$ 1.000) com os seguintes dados:
- Prazo: 10 dias úteis
- Futuro de dólar: 3.143,80
- Strike: 3.150
- Taxa de juros: 7,70% a.a.o.
- Volatilidade: 18,60% a.a.o.

3. Calcule o preço da seguinte opção de ação protegida de dividendos e das outras opções:
a. *Call* e *put* europeia de Vale
- Data de hoje: 17 jan. 2018
- Vencimento da opção: 19 fev. 2018
- Strike: R$ 43,62
- n: 21 du
- Preço à vista da VALE3: 43,00
- Taxa de juros: 6,80% a.a.o.

---

Volatilidade: 28% a.a.o.

## b. Call e put europeia de dólar (US$ 1.000) na B3

Data de hoje: 17 jan. 2018

Vencimento da opção: 1 mar. 2018

n: 29 du

Futuro de dólar: 3240

Strike: 3300

Taxa de juros: 6,80% a.a.o.

Volatilidade: 13,00% a.a.o.

## c. Call e put europeia de IBOVESPA

Data de hoje: 17 jan. 2018

Vencimento da opção: 14 mar. 2018

n: 38 du

Futuro de IBOV: 80200

Strike: 80.000

Taxa de juros: 6,80% a.a.o.

Volatilidade: 28,00% a.a.o.

## d. Call e put europeia de IDI

Data de hoje: 17 jan. 2018

Vencimento da opção: 1 jan. 2019

n: 238 du

IDI atual: 248.543,62

Strike: 263.200

Taxa de juros do futuro de DI: 6,91% a.a.o.

Volatilidade: 5,00% a.a.o.

## 4. Simulação de Monte Carlo.

a. Movimento browniano: calcule os preços estimados do ativo nos próximos quatro dias (P₁, P₂, P₃, P₄), dado que o preço à vista do ativo é  50, sabendo que a média esperada dos retornos é de 14% a.a.o. e a volatilidade dos retornos é de 39% a.a.o. Utilize os valores simulados de z ~ N(0,1) para os cálculos.

|  Dia | 0 | 1 | 2 | 3 | 4  |
| --- | --- | --- | --- | --- | --- |

---

|  Z | - | -0,10 | 0,23 | 0,58 | -1,40  |
| --- | --- | --- | --- | --- | --- |
|  P | 50 | P₁ | P₂ | P₃ | P₄  |

b. Reversão à média: Calcule os preços estimados do ativo nos próximos quatro dias (P₁, P₂, P₃, P₄), supondo que o ativo siga um processo de reversão à média, dado que o preço à vista do ativo é  50, sua média é de  49, sua volatilidade 35% a.a.o., com um fator de velocidade de reversão à média de 10% ao dia. Utilize os valores simulados de z ~ N(0,1) da tabela anterior para os cálculos.

5. Implementando o modelo de Black e Scholes no Microsoft Excel, determine o valor das opções a seguir:

a. Ativo: call
Prazo até o vencimento: 63 dias úteis
Preço de exercício: R$ 26,00
Preço à vista do ativo: R$ 25,25
Taxa de juros: 15,00% a.a.o.
Volatilidade: 30,00% a.a.o.

b. Ativo: put
Prazo até o vencimento: 22 dias úteis
Preço de exercício: R$ 100,00
Preço à vista do ativo: R102,00
Taxa de juros: 14,00% a.a.o.
Volatilidade: 27,00% a.a.o.

---

6. Utilizando a fórmula de paridade `put-call` (calcule o valor da `put` no item a) e da `call` no item b). Verifique com o resultado obtido pela fórmula do modelo Black e Scholes.

7. Implementando o modelo de Black e Scholes no Microsoft Excel, calcule o preço de uma `call` via paridade, sabendo que a `put` correspondente está sendo negociada a 2,00. Assuma os seguintes dados:
- Prazo: 60 du
- Taxa de juros: 14,00% a.a.o.
- Preço de exercício: 50,00
- Preço do ativo à vista: 52,00

Calcule a volatilidade implícita.

8. Implementando o modelo de Black e Scholes no Microsoft Excel, calcule o preço de uma `put` via paridade, sabendo que a `call` correspondente está sendo negociada a 5,00. Assuma os seguintes dados:
- Prazo: 72 du
- Taxa de juros: 15,00% a.a.o.
- Preço de exercício: 100,00
- Preço do ativo à vista: 95,00

Calcule a volatilidade implícita.

1 Progressão Geométrica.

---

CAPITULO 7

# Gregas das opções

---

Vamos apresentar o que é denominado por “gregas”, que fornecem as variações do preço das opções em relação às outras variáveis dos modelos de precificação.

As gregas serão úteis não apenas para a montagem de portfólios com estratégias especulativas em volatilidade, mas também para o hedge feito pelos bancos em operações com clientes institucionais e corporativos.

# 7.1 Delta e gama

O delta fornece a variação do prêmio da opção com relação a variações do preço do ativo para variações infinitesimais pequenas no preço do ativo. Para Δ S → 0, o delta é equivalente a primeira derivada parcial do prêmio da opção em relação ao preço do ativo:



Delta = Δ C/Δ S ≈ ∂ C/∂ S 



O que significa dizer que se o preço do ativo sobe, o prêmio da call também sobe.

O delta mede essa relação. Pode ser calculado por uma variação discreta infinitesimamente pequena ou pela derivada parcial.

O gama é a segunda derivada parcial do prêmio da opção, em relação ao preço do ativo. Também é importante pois o gama fornece a variação do delta quando o preço do ativo também se altera:



Gama = Δ Delta/Δ S ≈ ∂^2 C/∂ S^2 



---

Quando o preço do ativo aumenta, o prêmio da call aumenta, devido ao seu delta. Entretanto, quando o preço do ativo aumenta, o delta também aumenta – esse é o efeito do gama.

Posteriormente, neste capítulo, discutiremos o cálculo de cada uma das gregas para os modelos de precificação de opções. O delta e o gama são as mais importantes, por isso as abordamos logo no início do capítulo.

## 7.2 O efeito delta-gama

Suponha que o preço de uma call seja de R$ 3 e, no mesmo instante, o preço do ativo-objeto (por exemplo, uma ação) está cotado a R$ 42. Suponha também que o delta dessa call seja 0,60.

O que significa um delta de 0,60?

Delta de 0,60 significa que, para cada aumento de R$ 1 na cotação da ação, a call subirá R$ 0,60 ou, de outra forma, significa dizer também que, ao ficar comprado na call, equivale a ficar comprado em 60% da ação.

Suponha que o preço da ação possa subir ou cair R$ 1, por consequência disso, o prêmio da opção oscilaria entre R$ 3,60 e R$ 2,40, na figura a seguir S é o preço da ação e C o prêmio da call:

![img-67.jpeg](img-67.jpeg)
Figura 7.1 | Efeito delta da call para delta = 0,60

---

Fonte: Elaborada pelos autores.

Dessa maneira, quando o preço da ação estiver a R$ 43, a call valerá R$ 3,60 e, consequentemente, quando o preço da ação estiver a R$ 41, o prêmio da call estará valendo R$ 2,40.

À medida que o preço do ativo aumenta, o delta da opção também vai aumentar, devido ao efeito do gama. Agora, suponha que no próximo aumento de R$ 1 no preço da ação, o delta passe a valer 0,70, ou seja, o prêmio da opção aumentará 70 centavos para cada aumento de R$ 1 no preço da ação:

Figura 7.2 | Efeito delta da call para delta = 0,70
![img-68.jpeg](img-68.jpeg)
Fonte: Elaborada pelos autores.

Com a variação do preço da ação para R$ 44, o prêmio da call subiu de R$ 3,60 para R$ 4,30, considerando uma variação discreta de R$ 0,70.

O aumento do delta ocorreu devido ao efeito do gama. O gama faz com que o delta da call aumente com o aumento do preço do ativo.

Ainda utilizando o exemplo, vamos calcular os valores do delta e do gama a partir das variações discretas dos preços do ativo. O delta, como definido anteriormente, pode ser calculado pela variação do prêmio da opção para uma dada variação no preço do ativo, conforme a seguinte equação:

---



Delta = 3,60 - 3,00/43 - 42 = 0,60



O gama, similarmente, também pode ser calculado por variações discretas no valor do delta para uma dada variação discreta no preço do ativo, nesse caso, o delta mudou de 0,60 para 0,70, considerando uma variação de R$ 2 no preço do ativo, de R$ 40 para R$ 42. Podemos calcular o gama da seguinte maneira:



Gama = 0,70 - 0,60/44 - 42 = 0,05



O gama de 0,05 significa que o delta aumentará em 5 centavos para cada variação positiva de R$ 1 no preço do ativo.

Utilizando as variações de preços descritas podemos calcular a variação do prêmio da opção utilizando a série de Taylor até segunda derivada, ou seja, até o gama, considerando que Δ C é a variação discreta no preço da opção, teremos:



C = Delta(Δ S) + 1/2 Gama(Δ S)^2   (7.3)



Substituindo os números do nosso exemplo na Equação 7.5, sabendo que a variação total no preço do ativo foi R$ 2, teremos:



Δ = 0,60(2) + 1/2 0,05(2)^2 = 1,30



---

Calculamos, portanto, que o prêmio da opção variou R$ 1,30, ou seja, subiu de R$ 3,00 para R$ 4,30, com a variação de R$ 2,00 no preço do ativo, de R$ 42,00 para R$ 44,00.

Com base no exemplo anterior, concluímos que o prêmio da call aumenta com a variação do preço do ativo, porque o seu delta é positivo. O delta também aumenta com a variação do preço do ativo, devido ao efeito do gama.

## 7.3 O delta hedge

Vamos continuar o exemplo anterior para explicar o delta hedge em uma carteira de ativos.

Voltando ao momento inicial, quando a ação ainda valia R$ 42,00 e o delta era 0,60 e o prêmio da call era de R$ 3,00.

Se você tivesse uma carteira com seis mil ações, quantas opções precisaria vender para que pequenas variações no preço da ação não afetasse o resultado da sua carteira?

Em outras palavras: suponha que você queira fazer um hedge no preço do ativo, de tal maneira que neutralize qualquer resultado com as variações no preço do ativo.

Se para cada variação de R$ 1,00 no preço do ativo a call varia R$ 0,60, você teria de vender dez mil calls para proteger a carteira de seis mil ações contra oscilações no preço do ativo. Vamos analisar o resultado dessa carteira, considerando que esta seja marcada a mercado para dadas situações de preço do ativo. Se o valor da ação estiver em R$ 42, a carteira de seis mil ações valerá R$ 252 mil. No entanto, a carteira de dez mil opções estará valendo R$ 30 mil negativo (pois a posição é vendida), logo, o valor total da carteira será de R$ 222 mil, conforme o quadro a seguir:

---

NÚCLEO DE PESQUISA, DOCUMENTAÇÃO E REFERÊNCIA SOBRE MOVIMENTOS SOCIAIS E POLÍTICAS PÚBLICAS NO CAMPO CPDA/UFRRJ

Quadro 7.1 | Marcação a mercado de delta hedge

|  Variável | Valor da carteira marcada a mercado  |   |   |
| --- | --- | --- | --- |
|  Preço da ação | 42 | 43 | 44  |
|  Preço da opção | 3,00 | 3,60 | 4,30  |
|  Comprado em 6.000 ações | 252.000,00 | 258.000,00 | 264.000,00  |
|  Vendido em 10.000 calls | - 30.000,00 | - 36.000,00 | - 43.000,00  |
|  Valor total | 222.000,00 | 222.000,00 | 221.000,00  |

Fonte: Elaborado pelos autores.

Observando o quadro anterior, verificamos que, em um segundo momento, quando o preço da ação sobe para R$ 43, o valor da posição em ações aumenta para R$ 258 mil, enquanto que o das opções vai para R$ 36 mil negativo, a soma das duas posições continua resultando em um valor global da carteira de R$ 222 mil, que pode ser observado na última linha do quadro. Ou seja, o valor da ação mudou, mas o valor da carteira permaneceu estável.

Entretanto, quando o preço da ação sobe para R$ 44, o valor da carteira de ações sobe para R$ 264 mil e a posição com opções passa a valer R$ 43 mil negativo, pois cada opção passa a valer R$ 4,30 por call. O que resultou em um valor total da carteira de R$ 221 mil, logo, houve perda de R$ 1 mil.

Mas por que o valor da carteira reduziu quando o preço do ativo subiu para R$ 43? Isso ocorreu devido ao efeito do gama, com o aumento do preço da ação, o delta também aumentou, com isso nossa posição com opções ficou mais vendida, o delta hedge não ficou totalmente eficiente, pois naquele momento nós passamos a ficar parcialmente direcional.

O delta hedge é dinâmico, precisa ser balanceado regularmente para manter a proporção adequada entre o ativo e a opção. Mas qual a frequência de ajuste ideal para o delta hedge? Dependerá o valor do gama das opções. Quanto maior for o gama, mais frequente será o delta hedge.

Avenida Presidente Vargas, 417 – 7º andar – Centro – Rio de Janeiro – RJ – CEP: 20071-003
Telefone: +55 21 2224-8577 R. 207 – email: msppdocampo@gmail.com

---

O delta serve apenas para variações infinitesimais no preço do ativo-objeto, ou seja, é bem provável que a carteira precise ser ajustada, ou "recalibrada", várias vezes ao dia.

No nosso exemplo, quando o delta aumenta, ficaremos mais vendidos, logo, para balancear novamente o delta hedge, posso comprar opções ou comprar ações, até ajustar novamente a proporção do delta.

Veremos no capítulo de operações com volatilidade que é importante que o delta da carteira esteja permanentemente zerado.

## 7.3.1 Delta hedge com ativo

É possível fazer o delta hedge utilizando o próprio ativo-objeto, sendo que a proporção de ativo dependerá do delta das opções.

A seguir, a relação de delta hedge utilizando o ativo-objeto, nesse caso, ficamos comprados na ação e vendidos da call, na proporção de 1 ação para 1 / Δ opções:



{l}
[ + S ₀; - Δ^(- 1) C ],  ou  (7.4) 

[ + Δ S ₀; - C ]




Ou no caso de ficarmos vendidos em ações e comprados em opções:



{l}
[ - S ₀; + Δ^(- 1) C ],  ou  (7.5) 

[ - Δ S ₀; + C ]




Por exemplo, uma posição comprada em 2.000 ações precisaria estar vendida em quantas calls para neutralizar a posição, dado um delta de 0,8?

---



Q _C = - Q _s/Δ = - 2 . 0 0 0/0 , 8 = - 2. 5 0 0



Ou seja, deveríamos ficar vendidos em 2.500 calls para fazer o delta hedge da carteira.

Se o preço da ação subisse em R$ 1,00, qual seria o resultado na variação de valor da carteira?



R = Δ S ₀ Q _s + Δ C Q _C = (1) (2. 0 0 0) + (0, 8) (- 2. 5 0 0) = 0



# 7.4 Delta

Como definimos anteriormente, o delta fornece a variação do prêmio da opção com relação a variações do preço do ativo, é a primeira derivada parcial em relação ao preço do ativo. O delta da call europeia, nesse caso, é o próprio N(d₁):



D e l t a_(C A L L) = N (d ₁) (7. 6)



O delta da put europeia é o seguinte:



D e l t a_(P U T) = N (d ₁) - 1 (7. 7)



Ou seja, o delta da put europeia é complementar ao delta da call, em módulo, desde que tenham o mesmo preço de exercício e o mesmo prazo até vencimento:

---



Delta_(CALL) - Delta_(PUT) = 1 \ (7.8)



O delta para o modelo Black (1976) de uma call de opções sobre futuros é:



Delta_(CALL) = N(d_1)/e^(prime 1) \ (7.9)



E o delta de uma put de opções sobre futuros é:



Delta_(PUT) = N(d_1) - 1/e^(prime 1) \ (7.10)



O delta de uma call de um ativo que tem um custo de carregamento q:



Delta_(CALL) = N(d_1)/e^(prime 1) \ (7.11)



E o delta de uma put com custo de carregamento:



Delta_(PUT) = N(d_1) - 1/e^(prime 1) \ (7.12)



O delta de uma call é representado pela seguinte figura tridimensional, em que os eixos são o tempo, preço do ativo e o delta. Na figura, é possível observar que quando o preço do ativo aumenta, o delta também aumenta, tendendo assintoticamente ao valor 1, mas nunca é igual a 1. O contrário também é verdadeiro, à medida que o preço do ativo cai, o delta reduz-se e aproxima-se assintoticamente a zero, mas nunca chega a zero.

À medida que a opção se aproxima do vencimento, o delta muda de 0 para 1

---

quase que instantaneamente, isso significa que o delta hedge desse tipo de opção é muito difícil de ser feito, dado que o delta muda quase de forma binária pouco antes do vencimento.

Figura 7.3 | O delta de uma call
![img-69.jpeg](img-69.jpeg)
Fonte: Elaborada pelos autores.

# 7.4.1 Delta e at the moneyness da opção

Há diferentes formas de identificar se uma opção encontra-se dentro ou fora do dinheiro – in ou out of the money. Estas maneiras estão listadas a seguir:

- At the money à vista (spot): quando comparamos o preço à vista da ação com o valor do strike, mesmo sabendo que esses ocorrem em momentos diferentes no tempo. É um método bem simples, porém com menos precisão de informação.
- At the money a termo (forward): quando colocamos o preço à vista e o strike em um mesmo momento no tempo. Nesse caso, descontamos o strike a valor presente pela taxa livre de risco.

---

- At the money delta: o delta também indica a probabilidade de exercício da opção, logo, se for maior do que 0,50, indica opção in the money, e se for menor do que 0,50, indica que a opção está out of the money.

As situações que uma opção pode estar em relação ao preço de exercício antes da data de exercício são as seguintes:

- In the money (Δ > 0,5): ocorre quando a probabilidade de exercício da opção é alta. Quando o preço do ativo é superior ao strike a valor presente de uma call dentro do dinheiro, antes do exercício. Quando o delta é muito elevado, a elasticidade do preço da opção com o preço do ativo S_0 é máxima, chegando assintoticamente a 1.

Figura 7.4 | At the money – delta
![img-70.jpeg](img-70.jpeg)
Fonte: Elaborada pelos autores.

- Out of the money (Δ < 0,5): neste caso, a probabilidade de exercício é baixa, quando o preço do ativo S_0 é muito inferior ao preço de exercício K da call. A probabilidade de exercício não é nula, mas é

---

muito baixa. O delta de uma opção fora do dinheiro é baixo, aproximando-se assintoticamente a zero.

- At the money (Δ=0,5): característica de maior risco de uma opção, pois, como o preço do ativo está muito colado no strike descontado, não se sabe se a opção pode dar exercício ou não, por isso o prêmio sobre o risco cobrado no preço da opção é maior quando ela está no dinheiro. Pode-se considerar que uma opção está no dinheiro (at the money) se o delta dela estiver entre 0,45 e 0,55.

## 7.5 Gama

O gama é a segunda derivada parcial do preço da opção em relação ao preço do ativo, também pode ser definido como a variação do delta para uma dada variação no preço do ativo. O gama fornece o quanto o delta muda, em centavos, para uma variação de R$ 1 no preço do ativo.

Na figura a seguir é possível analisar a relação dos valores do delta e do gama de uma call para variações no preço do ativo.

- O primeiro gráfico mostra a relação entre o preço da call e o preço do ativo-objeto. É possível notar que a curva fica mais inclinada à medida que o preço do ativo-objeto aumenta.
- O segundo gráfico mostra a relação entre o delta e o preço do ativo-objeto. Observe que o valor do delta aumenta sempre com o aumento do preço do ativo, com inclinação crescente até delta = 0,5 e, a partir de então, passa a ter uma inclinação menos accentuada.
- O terceiro gráfico é o do gama, ele fornece a inclinação do gráfico do delta, a inclinação do delta começa baixa para opções out of the money, fica alta nas opções at the money, e volta a cair para as opções in the money.

Figura 7.5 | Relação delta-gama

---

Figura 7.6 | Distribuição normal padronizada não acumulada
![img-71.jpeg](img-71.jpeg)
Fonte: Elaborada pelos autores.

O gama de call e put europeia pode ser calculado da seguinte maneira:



G a m a = N^(prime) (d ₁)/S ₀ σ √ {t} tag {7.13}



O N^(prime)(d_1) é a derivada da integral N(d₁), nesse caso é a própria função f(z). Na Figura 7.6 a seguir, o N^(prime)(d_1) mostra a altura da curva para dados valores de d₁ no eixo do z :

---

![img-72.jpeg](img-72.jpeg)

Fonte: Elaborada pelos autores.

O gama para o modelo Black (1976) de call e put de opções sobre futuros é:



Gama = e^(-rt) N'(d_1)/Fσ√(t)   (7.14)



E o gama de call e put de um ativo que tem um custo de carregamento q é dado por:



Gama = e^(-qt) N'(d_1)/S_0σ√(t)   (7.15)



A seguinte figura representa o gama para uma call europeia. Podemos notar que o gama at the money é maior do que para in e out of the money. É possível notar também que o gama explode, tendendo a infinito, com a proximidade do vencimento. Ou seja, perto do vencimento, uma pequena alteração no preço do ativo-objeto, altera muito o delta. Logo, essa não é uma boa opção para fazer o delta hedge.

Figura 7.7 | Gama de uma call

---

![img-73.jpeg](img-73.jpeg)
Fonte: Elaborada pelos autores.

## Exemplo 7.1 - Cálculo de gama

Vamos calcular o gama de uma opção de compra de ação (call), de código VALEJ16, cujo preço de exercício é de R$ 16,13, que vencerá daqui a exatos 34 dias úteis, assumindo que o preço da ação-objeto seja de R$ 15,10.

Para isso, precisaremos utilizar a taxa de juros pré-fixada livre de risco de 14,23% a.a. e a volatilidade de 42,30% a.a., na base 252 dias úteis.

O primeiro passo é converter a taxa de juros pré-fixada para a forma contínua:



r = ln (1 + 0,1423) = 0,13304



Agora, calculamos d_1:



d_1 = ln (15,10/16,13) + (34/252) (0,423^2/2 + 0,13304)/0,423 √(34/252) = -0,23148



---

Podemos obter o delta pelo N(d₁), da distribuição normal acumulada, igual a 0,4085, ou seja, dado um z = -0,23148 obtemos uma probabilidade acumulada igual a 40,85\%. Isso significa que a opção está out-of-the-money.

E obtemos o N'(d_1) da distribuição normal padronizada não acumulada, igual a 0,3884, logo, o valor do gama será:



Gama = 0,3884/15,10 · (0,4230) √(34/252) = 0,1655



O resultado do gama é 0,1655, ou seja, se o preço do ativo aumentar R$ 1, o delta aumentará em torno de 16,55 centavos de real.

## 7.6 Vega

O vega fornece a variação do prêmio da opção para uma dada variação percentual na volatilidade. O vega é uma das variáveis mais relevantes para as operações com volatilidade. Para comprar volatilidade deve-se ficar vega positivo em sua carteira.

Pode ser calculado pela variação discreta do preço da opção para uma dada variação infinitesimalmente pequena na volatilidade, com Δσ rightarrow 0, ou pela derivada parcial.

Quando a volatilidade aumenta, o preço da opção também aumenta, uma explicação para que esse fenômeno ocorra é porque há um acréscimo na distância entre o d_1 e d_2, dado que:



d_2 = d_1 - σ √(t)   (7.16)



---

Quando a volatilidade σ aumenta, a diferença entre o d_1 e d_2 aumenta e, por consequência, incrementa o preço da opção. Dessa maneira, ao ficar vega positivo, estaremos comprados em volatilidade.

A equação a seguir define o vega para call e put europeia:



Vega = S_0 √(t) N'(d_1) 



O vega para o modelo Black (1976) de call e put de opções sobre futuros é:



Vega = F √(t) N'(d_1)/e^(τ t) 



O vega de call e put de um ativo que tem um custo de carregamento q é dado por:



Vega = S_0 √(t) N'(d_1)/e^(qt) 



Na Figura 7.8 a seguir representamos o gráfico do vega. O vega é maior para as opções at the money, o que significa que essas opções são as melhores quando se deseja comprar volatilidade. O vega decai à medida que a opção se aproxima do vencimento, dessa forma, as opções próximas do vencimento possuem pouco vega. As opções deep out ou deep in the money possuem vega baixo, ou seja, as opções que estão nos extremos da curva a seguir.

Figura 7.8 | Gráfico de vega de uma call

---

![img-74.jpeg](img-74.jpeg)

Fonte: Elaborada pelos autores.

## Exemplo 7.2 - Cálculo de vega

Utilizando os mesmos dados do exemplo do gama, com N'(d_1) igual a 0,3884, sabendo que o preço da ação-objeto é de R$ 15,10, a volatilidade de 42,30% a.a., de uma call europeia que vence em 34 dias úteis, teremos o vega igual a:



Vega = 15,10 √(34/252) = 0,3884 = 2,1542



O resultado do vega é de R$ 2,1542 para uma variação de 100% na volatilidade, isso acontece porque na derivada parcial, o denominador fica igual a 1, no caso da volatilidade, isso significa uma variação de 100%, ou seja, supondo um salto na volatilidade de 42,30% para 142,30% a.a.

É mais interessante calcularmos o vega para uma variação de 1% na volatilidade. Nesse caso, precisamos dividir o resultado obtido do vega por 100:



Vega_(1\%) = 2,1542/100 = 0,021542



---

Isso significa que, se a volatilidade subir
1\%
, o preço da opção subirá R$ 0,021542, pouco mais de 2 centavos de real.

# 7.7 Posição nas gregas

Vamos analisar a posição nas gregas quando compramos ou vendemos uma call europeia. Suponhamos que montamos a seguinte carteira delta hedgeada, vendida em ação e comprada em call, da seguinte forma:  [-S₀; + Δ^(-1)C] .

Ao analisar as gregas dessa carteira, quando observamos apenas a compra de call, estamos:

- Delta positivo: porque equivale a ficar comprado em  Δ  ações.
- Gama positivo: porque o delta hedge dinâmico nos favorece. Isso ocorre porque quando o preço do ativo sobre, ficamos mais comprados com o aumento do delta, e teremos de vender o ativo para delta hedgear. O movimento contrário também nos favorece. Quando o preço da ação cai, ficaremos mais vendidos, e teremos de comprar ativo para delta hedgear. Vendemos na alta e compramos na baixa, proporcionando lucros com o delta hedge dinâmico.
- Vega positivo: ao ficar comprado em call, estaremos comprados em volatilidade.

Ao comprar call, ficamos delta, gama e vega positivos. Ao comprar a put, ficamos delta negativo, porém gama e vega positivos.

# 7.8 Theta

---

O theta é uma grega resultante da relação entre a variação do preço da opção com a mera passagem dos dias até o vencimento. À medida que o tempo passa, o preço da call diminui, ou seja, perde valor.

O theta possui dois componentes, um deles relativo aos juros, que denominamos como theta juro, e o outro, relacionado à volatilidade, denominado theta vol.

Conforme o vencimento da call se aproxima, a variável t diminui. Isso significa que, dado uma taxa de juros qualquer, o valor do exercício descontado ao valor presente aumenta. O efeito do tempo na taxa de juros pode ser observado na seguinte equação, quando o t diminui, o valor do strike descontado a valor presente aumenta, logo o valor da call diminui:



C = S ₀ N (d 1) - K/(1 + i) ^t N (d 2) tag {7.20}



No caso da put o efeito do theta juro é contrário ao da call, quando o tempo diminui, o strike aumenta e, consequentemente, haverá aumento no preço da put. O que é possível notar na seguinte equação de precificação de put:



P = K/(1 + i) ^t N (- d 2) - S ₀ N (- d 1) tag {7.21}



Conforme a opção se aproxima do vencimento, o efeito da volatilidade se reduz gradativamente, pois a distância entre o d₁ e d₂ estreita-se com a redução do tempo. Esse efeito é denominado como theta vol. Tanto o prêmio da call quanto o da put aumentam na medida em que a diferença entre d₁ e d₂ aumenta. Na equação seguinte podemos notar que se o tempo diminui, a diferença entre d₁ e d₂ diminui, consequentemente, haverá redução do prêmio das opções:

---



d ₂ = d ₁ - σ √ {t} tag {7.22}



Na equação anterior, se o t diminui, o preço da opção também diminui, pois reduz a distância entre d1 e d2.

O theta possui dois componentes: theta juro e theta vol. O efeito theta juro é positivo para put e negativo para call, entretanto, o efeito do theta vol é negativo tanto para put quanto para call.

Ao ficarmos comprados em call, estamos theta negativo, perderemos valor com a passagem dos dias.

O theta total de uma call europeia é igual à soma do theta juro com o theta vol:



Theta_(TOTAL) = Theta_(JURO) + Theta_(VOL) tag {7.23}



Sendo o theta juro de uma call europeia dado por:



Theta_(JURO) = - r K/e^(r t) N (d 2) tag {7.24}



E o theta vol da call europeia é obtido da seguinte forma:



Theta_(VOL) = - S ₀ N^(prime) (d 1) σ/2 √ {t} tag {7.25}



Logo, o theta total de uma call europeia será dado por:

---



Theta = - S_0 N'(d1)σ/2√(t) - rK/e^(prime t) N(d2) 



O theta de uma put europeia é dado pela seguinte equação:



Theta = - S_0 N'(d1)σ/2√(t) + rK/e^(prime t) N(-d2) 



O theta para o modelo Black (1976) de call de opções sobre futuros é:



Theta = - F N'(d1)σ/e^(prime t) 2√(t) + rFN(d1)/e^(prime t) - rK/e^(prime t) N(d2) 



E o theta para o modelo Black (1976) de put de opções sobre futuros é dado por:



Theta = - F N'(d1)σ/e^(prime t) 2√(t) - rFN(-d1)/e^(prime t) + rK/e^(prime t) N(-d2) 



O theta de call de um ativo que tem um custo de carregamento q é dado por:



Theta = - S_0 N'(d1)σ/e^(qt) 2√(t) + qS_0 N(d1)/e^(qt) - rK/e^(prime t) N(d2) 



---

E o theta de put de um ativo que tem um custo de carregamento q é dado por:



Theta = - S ₀ N^(prime) (d 1) σ/e^(q t) 2 √ {t} - q S ₀ N (- d 1)/e^(q t) + r K/e^(r t) N (- d 2) tag {7.31}



A Figura 7.9 a seguir é a representação gráfica do theta de uma call. O theta, assim como o gama, explode com a proximidade do vencimento se estiver at the money, ou seja, o detentor dessa call perderá muito valor nos últimos dias da opção. Note que o eixo horizontal é negativo:

Figura 7.9 | Gráfico do theta para call
![img-75.jpeg](img-75.jpeg)
Fonte: Elaborada pelos autores.

A Figura 7.9 apresenta um gráfico que não é simétrico, é possível notar que as opções in the money, que estão do lado direito do gráfico, possuem o

---

theta mais elevado do que as opções out of the money.

## Exemplo 7.3 - Cálculo de theta

Vamos calcular o theta de uma opção de compra de ação europeia *call*, código VALEJ16, cujo preço de exercício é de R$ 16,13, que vencerá daqui a 34 dias úteis, assumindo que o preço da ação-objeto seja de R$ 15,10.

Para isso, precisaremos utilizar a taxa de juros pré-fixada livre de risco de 14,23% a.a. e a volatilidade de 42,30% a.a., na base 252 dias úteis.

Convertemos a taxa de juros pré-fixada para a forma contínua:



r = ln(1 + 0,1423) = 013304



Agora, calculamos d_1:



d_1 = ln(15,10/16,13) + (34/252)(0,423^2/2 + 0,13304)/0,423√(34/252) = -0,23148



E d_2:



d_2 = -0,23148 - 0,423 √(34/252) = -0,38685



Os valores de N'(d_1) e N(d_2) são, respectivamente, 0,3884 e 0,3494, logo, o theta é obtido da seguinte forma:

---



Theta = - 15,10(0,3884)0,423/2√(34/252) - 0,13304(16,13)/e^(0,1330434/252) 0,3494 = -4,11348



O resultado do theta é R - 4,11348, para uma variação de um ano no tempo, isso acontece porque na derivada parcial o denominador fica igual a 1, isso significa uma variação de um ano no prazo da opção.

É mais interessante calcularmos o theta para uma variação de um dia útil na maturidade da opção. Ou seja, um dia útil aproximando-se do vencimento, nesse caso específico, reduziremos de 34 para 33 dias úteis. Para obter o resultado desejado, dividiremos por 252 o resultado obtido anteriormente no cálculo do theta:



Theta_(tdu) = -4,11348/252 = -0,01632



O resultado anterior indica que o preço da opção diminui 1,632 centavos de real para cada dia útil que se aproxima do vencimento.

## 7.9 Rô

O rô é uma das gregas que indica a variação do preço da opção com o incremento nas taxas de juros. O comportamento do rô para *call* e *put* é diferente. Quando há um aumento na taxa de juros, o valor da *call* aumenta e o valor da *put* diminui.

Observando a equação a seguir, veremos que, à medida que a taxa de juros r aumenta, o preço de exercício, o valor presente, diminui e, consequentemente, o preço da *call* aumenta:



C = S_0 N(d1) - K/e^α N(d2) 



---

Na verdade, vamos trabalhar com dois tipos de ró, um para variação na taxa de juros discreta e outro para a taxa de juros contínua. Apresentamos também o ró para taxas discretas, pois será muito útil quando considerarmos que o ró pode ser hedgeado por meio de contratos futuros de DI, cuja taxa de juros negociada é discreta. Primeiro, apresentamos o ró para variações infinitesimais na taxa de juros contínua.

## 7.9.1 Ró para taxa de juros contínua

O ró de uma *call* europeia, para taxa de juros contínua, será dado por:



R hat {o} = K t/e^(prime τ) N (d 2) tag {7.33}



O ró de uma *put* europeia, para taxa de juros contínua, é calculado da seguinte forma:



R hat {o} = - K t/e^(prime τ) N (- d 2) tag {7.34}



O ró para o modelo Black (1976) de *call* de opções sobre futuros, para taxa de juros contínua, é:



R hat {o} = - t [ F N (d 1) - K N (d 2) ]/e^(prime τ) tag {7.35}



---

E o ró para o modelo Black (1976) de put de opções sobre futuros, para taxa de juros contínua, é dado por:



R hat {o} = - t [ K N (- d 2) - F N (- d 1) ]/e^(prime prime) tag {7.36}



O ró de call de um ativo que tem um custo de carregamento q, para taxa de juros contínua, é dado por:



R hat {o} = K t/e^(prime prime) N (d 2) tag {7.37}



E o ró de put de um ativo que tem um custo de carregamento q, para taxa de juros contínua, é dado por:



R hat {o} = - K t/e^(prime prime) N (- d 2) tag {7.38}



A figura a seguir representa graficamente o ró de uma call europeia. Nela podemos notar que o ró decresce à medida que nos aproximamos do vencimento da opção, e que o ró das opções in the money são maiores comparado ao das opções out of the money.

Figura 7.10 | Gráfico de ró de uma call

---

![img-76.jpeg](img-76.jpeg)
Fonte: Elaborada pelos autores.

# 7.10 Ró para taxa de juros discreta

Quando estamos comprados em call, estamos rô positivo, ou seja, com o aumento da taxa de juros, aumenta o preço da opção. Equivale a ficar comprado em taxa de juros. Geralmente, o rô é calculado para cada variação de um ponto percentual na taxa de juros pré-fixada. O rô equivale a 100 vezes o DV01 (variação para um ponto base, ou 0,01%).

Agora, vamos apresentar o rô considerando variações na taxa de juros discreta, sabendo que podemos obter a taxa de juros discreta i da seguinte forma:

---



i = e ^r - 1 tag {7.39}



O ró de uma call europeia, para taxa de juros discreta, será dado por:



R hat {o} = K t/e^(r (t + 1)) N (d 2) tag {7.40}



O ró de uma put europeia, para taxa de juros discreta, é calculado da seguinte forma:



R hat {o} = - K t/e^(r (t + 1)) N (- d 2) tag {7.41}



O ró para o modelo Black (1976) de call de opções sobre futuros, para taxa de juros discreta, é:



R hat {o} = - t [ F N (d 1) - K N (d 2) ]/e^(r t) tag {7.42}



E o ró para o modelo Black (1976) de put de opções sobre futuros, para taxa de juros discreta, é dado por:



R hat {o} = - t [ K N (- d 2) - F N (- d 1) ]/e^(r (t + 1)) tag {7.43}



O ró de call de um ativo que tem um custo de carregamento q, para taxa de juros discreta, é dado por:

---



R hat {o} = K t/e^(r (t + 1)) N (d 2) tag {7.44}



E o ró de put de um ativo que tem um custo de carregamento q, para taxa de juros discreta, é dado por:



R hat {o} = - K t/e^(r (t + 1)) N (- d 2) tag {7.45}



Para fazer o hedge de ró, com taxa de juros discreta, podemos utilizar contratos futuros de DI em posição inversa. Para isso, podemos calcular a quantidade de contratos futuros de DI para fazer o hedge pelo DV01. Em geral, para as opções de ações negociadas em bolsa, o valor do ró é bem pequeno, e não se faz o hedge de taxa nessas posições de opções.

Para opções mais longas, por exemplo, opções de balcão, o ró passa a ser significativo e deve ser monitorado e eventualmente hedgeado.

## Exemplo 7.4 - Cálculo de ró

Utilizando os mesmos dados do exemplo anterior, vamos calcular o ró de uma opção de compra de ação europeia (call), cujo preço de exercício é R$ 16,13, que vencerá em 34 dias úteis e o preço da ação-objeto é R$ 15,10. A taxa de juros pré-fixada livre de risco considerada é de 14,23% a.a. e a volatilidade de 42,30% a.a., na base 252 dias úteis.

Primeiro, convertemos a taxa de juros pré-fixada para a forma contínua:



r = ln (1 + 01423) = 0,13304



Agora, calculamos d2:

---



d2 = ln(15,10/16,13) + (34/252)(0,13304 - 0,423^2/2)/0,423√(34/252) = -0,38685



O valor de N(d2) é 0,3494, logo, o rô da call será:



Rδ = 16,13(34/252)/e^(0,1330434/252) · 0,3494 = 0,7469



O resultado do cálculo do rô para variações infinitesimais na taxa de juros contínua foi de

R$ 0,7469, ele fornece a variação do valor da opção para uma variação de 100 pontos percentuais na taxa de juros contínua, ou seja, para uma variação de 100% na taxa r. Geralmente, desejamos um rô para uma variação de 1%, logo, vamos dividir o resultado por 100:



Rdelta_(1\%) = 0,7469/100 = 0,007469



Isso significa que, para cada aumento de um ponto percentual na taxa de juros contínua, o preço da opção aumentará 0,7469 centavo de real.

Porém, é mais útil calcular o rô para variações na taxa de juros discreta, pois é mais usual no mercado brasileiro, e podemos hedgear utilizando o futuro de DI. O rô para variações infinitesimais na taxa de juros discreta é calculado da seguinte forma:



Rδ = 16,13(34/252)/e^(0,13304(34/252 + 1)) · 0,3494 = 0,6539



---

O resultado do cálculo do rô para variações na taxa de juros discreta foi de R$ 0,6539, resultado da variação da opção para uma variação de 100 pontos percentuais na taxa de juros discreta, ou seja, para uma variação de 100% na taxa i. Ao dividir o resultado por 100, obtemos um rô para cada aumento de um ponto percentual na taxa de juros discreta, de 0,6539 centavo de real, ou seja, na terceira casa decimal de reais.

# 7.11 Resumo geral das gregas

Nos quadros a seguir, apresentamos as fórmulas das gregas para opções europeias, utilizando como base o modelo de Black e Scholes (1973), opções sobre futuros, e opções com custo de carregamento q:

Quadro 7.2 | Gregas de call

|  Grega | Europeia | Futuros | Carregamento q | Ajuste  |
| --- | --- | --- | --- | --- |
|  Delta | Q_(IND) | N(d_1)/e^a | N(d_1)/e^a | Nenhum  |
|  Gama | N'(d_1)/S_0σ√(t) | e^(-a) N'(d_1)/Fσ√(t) | e^(-a) N'(d_1)/S_0σ√(t) | Nenhum  |
|  Vega 1% | S_0√(t)N'(d_1) | e^(-a) N'(d_1)/Fσ√(t) | S_0√(t)N'(d_1)/e^a | Resultado dividido por 100  |
|  Theta 1 du | -S_0N'(d1)σ/2√(t)
-rK/e^aN(d2) |  |  | Resultado dividido por 252  |

---

|   |  | FN'(d1)σ/e^(rt)2√(t)
+ rFN(d1)/e^(rt)
-rK/e^(rt)N(d2) | S_0N'(d1)σ/e^(gt)2√(t)
+ qS_0N(d1)/e^(gt)
-rK/e^(rt)N(d2) |   |
| --- | --- | --- | --- | --- |
|  Rô 1% de variação na taxa de juros contínua | Kt/e^(rt)N(d2) | -t[FN(d1)-KN(d2)]/e^(rt) | Kt/e^(rt)N(d2) | Resultado dividido por 100  |
|  Rô 1% de variação na taxa de juros discreta | Kt/e^(r(t+1))N(d2) | -t[FN(d1)-KN(d2)]/e^(rt) | Kt/e^(r(t+1))N(d2) | Resultado dividido por 100  |

Fonte: Elaborado pelos autores.

Quadro 7.3 | Gregas de put

|  Grega | Europeia | Futuros | Carregamento q | Ajuste  |
| --- | --- | --- | --- | --- |
|  Delta | N(d_1)-1 | N(d_1)-1/e^(rt) | N(d_1)-1/e^(rt) | Nenhum  |
|  Gama | N'(d_1)/S_0σ√(t) | e^(-rt) N'(d_1)/Fσ√(t) | e^(-qt) N'(d_1)/S_0σ√(t) | Nenhum  |
|  Vega 1% | S_0√(t)N'(d_1) | e^(-rt) N'(d_1)/Fσ√(t) | S_0√(t)N'(d_1)/e^(gt) | Resultado dividido por 100  |
|  Theta 1 du | -S_0N'(d1)σ/2√(t) |  |  | Resultado dividido por 252  |
|   |  -rK/e^(rt)N(d2) |  |   |   |

---

|   |  | FN'(d1)σ/e^(rt)2√(t)
rFN(-d1)/e^(rt)
+rK/e^(rt)N(-d2) | S_0N'(d1)σ/e^(rt)2√(t)
qS_0N(-d1)/e^(rt)
+rK/e^(rt)N(-d2) |   |
| --- | --- | --- | --- | --- |
|  Rô 1% de variação na taxa de juros contínua | -Kt/e^(rt)N(-d2) | t[KN(-d2)-FN(-d1)]/e^(rt) | -Kt/e^(rt)N(-d2) | Resultado dividido por 100  |
|  Rô 1% de variação na taxa de juros discreta | -Kt/e^(r(t+1))N(-d2) | t[KN(-d2)-FN(-d1)]/e^(rt) | -Kt/e^(r(t+1))N(-d2) | Resultado dividido por 100  |

Fonte: Elaborado pelos autores.

# 7.12 Posição nas gregas em put e call

Quando estamos comprados em call, a posição nas gregas ficará da seguinte maneira:

- delta positivo: equivale a ficar comprado no ativo;
- gama positivo: o delta hedge nos favorece;
- vega positivo: ganhamos com o aumento da volatilidade implícita;
- theta negativo: perdemos com o emagrecimento do prêmio da call;
- ró positivo: estamos comprados em taxas de juros.

---

Ao ficar comprado em put, a posição fica da seguinte maneira:

- delta negativo: equivale a ficar vendido no ativo;
- gama positivo: o delta hedge favorece o resultado;
- vega positivo: ganhamos com o aumento da volatilidade implícita;
- theta vol positivo e theta juro negativo;
- rō negativo: ficamos vendidos em taxas de juros.

As gregas possuem comportamentos distintos conforme o tempo remanescente para o vencimento da opção. Como o tempo é relativo, vamos supor que longe do exercício seriam seis meses, e perto do exercício, uma semana.

Perto do vencimento da opção, o comportamento das gregas é o seguinte:

- o delta muda abruptamente de valor para pequenas variações no preço do ativo;
- o gama explode, se a opção estiver at the money;
- o vega fica baixo, com pouca sensibilidade para variações na volatilidade;
- o theta explode, se a opção estiver at the money;
- o rō fica baixo.

Quando está longe do vencimento, as gregas ficam da seguinte maneira:

- o delta muda pouco de valor, o delta hedge é menos dinâmico, mais fácil de hedgear;
- o gama é baixo, o que indica poucas alterações no delta;
- o vega é alto, com muita sensibilidade para variações na volatilidade;
- o theta é baixo também, com pouco emagrecimento;
- o rō é alto, principalmente para as opções in the money.

---

# 7.13 Gregas para simulação de Monte Carlo

Não importa qual é o modelo que você utiliza para precificação de opção, sempre será possível calcular as gregas. Isso pode ser feito aplicando-se variações discretas infinitesimais de pequenas em cada uma das variáveis utilizadas para a precificação da opção.

Vamos supor que queiramos calcular as gregas de uma opção precificada por simulação de Monte Carlo, considerando um processo estocástico conhecido, com base no que foi discutido nos capítulos anteriores.

Vamos fazer um exemplo de simulação de Monte Carlo de uma opção de compra (call) de ação, que vencerá dentro de cinco dias úteis. Consideraremos uma volatilidade σ de 35\% a.a.o. e uma média μ de 14\% a.a.o., (taxa livre de risco), que segue um processo de Wiener, com o lema de Itô. Suponha que a cotação da ação está hoje a R$ 32, cujo preço de exercício da opção de compra também é R$ 32. O preço da opção será R$ 0,7218 por simulação de Monte Carlo, considerando as três trajetórias de variáveis z sim N(0,1) sorteadas:

Tabela 7.1 | Variáveis z sorteadas

|  Dias | Trajetória 1 | Trajetória 2 | Trajetória 3  |
| --- | --- | --- | --- |
|  1 | -1,86 | -0,45 | -0,56  |
|  2 | -0,56 | 0,33 | 0,20  |
|  3 | 0,50 | -0,17 | 1,15  |
|  4 | 1,09 | -1,44 | 1,01  |
|  5 | 0,82 | 1,01 | 1,05  |

Fonte: Elaborada pelos autores.

---

Para calcular o delta, devemos somar R$ 0,10 ao preço do ativo-objeto, resultando em R$ 32,10 e recalcular o preço da opção. Com o aumento do preço do ativo-objeto, o valor da opção subirá o equivalente a R$ 0,0355. Podemos calcular o delta da seguinte forma:



Delta = Δ C/Δ S = 0,0355/0,10 = 0,3550



O mesmo procedimento deve ser adotado para as outras gregas, por exemplo, o rô resultou em R$ 0,00422 e o vega é igual a R$ 0,01877.

# 7.14 Gregas de uma carteira

As gregas de uma carteira são iguais à soma de todas as gregas das opções que compõem essa carteira, proporcional a quantidade de cada um desses instrumentos. Esse procedimento pode ser adotado mesmo que as opções tenham preços de exercício e vencimentos diferentes.

Porém, não se pode somar as gregas de carteiras de opções sobre ativos-objetos diferentes, mesmo que se trate de ações ordinárias (ON) e preferenciais (PN) de uma mesma empresa.

A soma das gregas em uma carteira será útil nas operações com volatilidade, que serão abordadas no próximo capítulo.

É importante reiterar que ativo-objeto possui apenas delta, não possui as outras gregas, e o delta do ativo-objeto é sempre igual a 1.

As equações a seguir mostram o somatório das gregas da carteira, que representamos por Π:

---



Delta_Π = Σ(j=1 até n) Delta_j Q_j   Theta_Π = Σ(j=1 até n) Theta_j Q_j





Gamma_Π = Σ(j=1 até n) Gamma_j Q_j   rho_Π = Σ(j=1 até n) rho_j Q_j 





V_Π = Σ(j=1 até n) V_j Q_j



As gregas da carteira são iguais à soma de todas as gregas das opções que formam a carteira, sobre um mesmo ativo-objeto.

## RESUMO

Neste capítulo, apresentamos as gregas de opções sobre ações, futuros e ativos com custo de carregamento e dividendos. Vimos também o delta hedge e o comportamento das gregas à medida que nos aproximamos do vencimento da opção. O conteúdo deste capítulo será relevante para o entendimento das operações com volatilidade que serão abordadas posteriormente.

## EXERCÍCIOS PROPOSTOS

1. Calcule as cinco gregas da seguinte *call* de ação protegida de dividendos:

Strike: R$ 36,00

Prazo: 22 dias úteis

Preço da ação à vista da: 35,70

Taxa de juros: 7,80% a.a.o

Volatilidade: 39% a.a.o

2. Calcule as cinco gregas da *call* de dólar (US$ 1.000) com os seguintes dados:

---

Prazo: 10 dias úteis

Futuro de dólar: 3.143,80

Strike: 3.150

Taxa de juros: 7,70% a.a.o.

Volatilidade: 18,60% a.a.o.

3. Calcule as cinco gregas da seguinte put de ação europeia protegida de dividendos:

Strike: R$ 36,00

Prazo: 22 dias úteis

Preço da ação à vista da: 35,70

Taxa de juros: 7,80% a.a.o.

Volatilidade: 39% a.a.o.

4. Calcule as cinco gregas da put de dólar (US$ 1.000) com os seguintes dados:

Prazo: 10 dias úteis

Futuro de dólar: 3.143,80

Strike: 3.150

Taxa de juros: 7,70% a.a.o.

Volatilidade: 18,60% a.a.o.

---

CAPITULO 8

# Operações com volatilidade de opções

---

Para entender a lógica operacional das operações com volatilidade é necessário estudar as gregas, apresentadas no capítulo anterior.

Neste capítulo, apresentaremos a superfície de volatilidade e algumas operações com opções, que podem ser usadas para especulação, arbitragem e para o hedge.

As operações com volatilidade são delta hedgeadas, consequentemente, os movimentos do preço do ativo base não interferem no resultado da carteira, são operações não--direcionais. Nesse caso, o que negociaremos é a própria superfície de volatilidade, que é composta pelas volatilidades implícitas de opções negociadas em bolsa sobre um mesmo ativo-objeto, de diversos vencimentos e preços de exercício.

As operações com volatilidade (trading de volatilidade) possuem um cunho predominantemente especulativo, mas também podem ser utilizadas em operações realizadas para empresas. Quando um banco realiza uma operação de hedge com opções para uma empresa, o banco pode estar, na verdade, operando volatilidade.

Por mais estranho que possa soar aos ouvidos do investidor incauto: as operações com volatilidade possuem baixo risco, isso ocorre porque são sempre delta hedgeadas, por isso têm um risco reduzido de exposição às oscilações do ativo-objeto.

Geralmente, quem opera volatilidade assume posições em opções muito maiores do que aqueles que realizam operações direcionais, logo, o operador de volatilidade opera em volume e frequência maiores do que os direcionais.

Outra característica de operações com volatilidade: sempre estaremos vendidos a descoberto em opções. Logo, todas as operações de volatilidade chamarão margem em bolsa.

Se for operar volatilidade, uma das primeiras etapas deverá ser a compra de um ativo, por exemplo, um título público e subsequente depósito em margem na clearing da bolsa.

## 8.1 Volatilidade implícita

---

A volatilidade implícita é obtida a partir do preço da opção. Nas equações fechadas de precificação de opções não é possível isolar o desvio-padrão. Para calcular a volatilidade implícita é necessário um método numérico iterativo, como o algoritmo de Newton e Raphson.

Podemos entender a volatilidade implícita como uma expectativa da volatilidade do ativo--objeto refletida nos preços das opções negociadas.

Vamos partir da premissa de volatilidade homocedástica, ou seja, constante, até o vencimento da opção. Podemos estimar a volatilidade implícita por meio do preço da opção, a partir de um processo iterativo, utilizando a derivada parcial em relação à volatilidade, ou seja, o vega. O método deve permitir que se obtenha um preço de opção igual ao preço de mercado, alternando a variável volatilidade, via tentativa e erro, até a convergência dos preços.

Uma forma rudimentar de se obter esse resultado é por meio do "atingir meta" do Microsoft Excel. Não é difícil, porém, a implementação em código de um método iterativo, do tipo "Do While", para calcular a volatilidade. A diferença entre o preço de mercado da opção e o preço calculado com uma volatilidade inicial (definida arbitrariamente, também chamada de "semente") é minimizada, recursivamente, alterando a volatilidade, por meio da seguinte equação:



sigma_n = sigma_(n-1) - (C_(n-1) - C_(merc))/Vega 



Sendo:

- n: número de iterações até chegar no preço de mercado da opção
- C_(merc): preço de mercado da opção C_(n-1): preço calculado da opção com base na volatilidade sigma_(n-1)

---

Exemplo 8.1 - Cálculo de volatilidade implícita

Vamos trabalhar com um exemplo de cálculo de volatilidade implícita utilizando um método recursivo, com base no vega da opção.

Queremos calcular a volatilidade implícita de uma *call* europeia, que está sendo negociada a R$ 0,53 por opção, que vence em 34 dias úteis, cujo preço de exercício é de R$ 16,13, sabendo que o preço da ação-objeto é de R$ 15,10 e a taxa de juros está a 14,23% a.a.o.

O cálculo da volatilidade implícita será feito nos seguintes passos:

1. Calcular o preço da opção a partir de uma volatilidade inicial, que chamaremos de "semente". Essa volatilidade inicial não precisa ser próxima da volatilidade real, serve apenas para o algoritmo calcular um primeiro preço da opção. Conforme forem ocorrendo as iterações, o preço da opção convergirá ao prêmio de mercado.

2. Calcular o vega e, com isso, a nova volatilidade.

3. Repetir os passos 1 e 2 até que cheguemos a uma diferença aceitável (infinitesimalmente pequena) entre o preço de mercado e o preço calculado da opção. A volatilidade implícita será a volatilidade que fornecerá esse preço calculado.

Para o cálculo da volatilidade implícita devemos partir de uma volatilidade "semente", vamos supor, 45% a.a.o. Quanto mais próxima a volatilidade inicial for da implícita de mercado, mais rápido será o processo de iteração.

Inicialmente, convertemos a taxa de juros pré-fixada para a forma contínua:



r = ln(1 + 0,1423) = 0,13304



Agora, calculamos d_1 e d_2, por Black e Scholes (1973), partindo da volatilidade inicial:



d_1 = ln(15,10/16,13) + (34/252)(0,45^2/2 + 0,13304)/0,45√(34/252) = -0,20797





d_2 = -0,20797 - 0,45√(34/252) = -0,37326



---

Em seguida, obtemos os valores de N(d1) e N(d2), que são, respectivamente, 0,4176 e 0,3545. Logo, o preço calculado da call será:



C = 15,10(0,4176) - 16,13/e^(0,13304(34/252))(0,3545) = 0,6902



Com N'(d_1) igual a 0,3904, temos o vega igual a:



Vega = 15,10√(34/252)} \ 0,3904 = 2,1654



A partir do vega, calculamos a nova volatilidade:



sigma_2 = 0,45 - (0,6902 · 0,53)/2,1654 = 37,60\%  a.a.o.



Com a nova volatilidade calculada, repetimos os passos 1 e 2 para obter um resultado mais refinado.

Ao calcular o preço da opção com a volatilidade de 37,60% a.a.o. (base 252), chegamos em um valor de R$ 0,5312, ou seja, um resultado mais próximo ao preço de mercado da opção de R$ 0,53 e obtivemos um vega de R$ 2,1284. Recursivamente, podemos calcular a terceira volatilidade:



sigma_3 = 0,3760 - (0,5312 · 0,53)/2,1284 = 37,55\%  a.a.o.



Com essa volatilidade, finalmente chegamos ao resultado desejado de preço da opção de R$ 0,5300001, com uma pequena diferença na sétima casa decimal.

Logo, a volatilidade implícita obtida no cálculo de iteração é 37,55% a.a.o.

---

# 8.2 Sorriso e superfície de volatilidade

Podemos calcular a volatilidade implícita de opções de um mesmo vencimento, porém de preços de exercícios distintos, sobre um mesmo ativo-objeto. É possível fazer isso com opções de ações negociadas em bolsa, cujo resultado esperado pode ser representado na seguinte figura:

Figura 8.1 | Sorriso de volatilidade
![img-77.jpeg](img-77.jpeg)
Fonte: Elaborada pelos autores.

Conseguimos identificar que as opções *at the money*, na parte central da figura, representado pelo *strike* 40, possuem uma volatilidade implícita menor do que as *in* e *out of the money*.

O sorriso de volatilidade é composto pelas volatilidades implícitas de opções com preços de exercício diferentes, porém de mesmo vencimento.

O efeito do sorriso de volatilidade pode ser explicado por dois motivos distintos:

- Leptocurtose na distribuição de probabilidade real dos retornos contínuos: o efeito das caudas grossas faz com que os retornos

---

observados na realidade, nos extremos da distribuição normal, ocorram em uma frequência maior do que o previsto pela distribuição normal. Isso faz com que os modelos de precificação de opções subprecifiquem as opções que estão nos extremos, que são exatamente as in e out of the money, logo, as opções com deltas muito baixos ou muito elevados. O smile de volatilidade é uma forma de compensar, aumentando gradativamente a volatilidade, o valor mais baixo do prêmio fornecido pelos modelos que usam a distribuição normal como premissa.

O sorriso de volatilidade pode ser explicado como uma compensação na volatilidade das caudas grossas na distribuição dos retornos dos ativos-objetos.

- Prêmio pela menor liquidez: as opções in e out of the money possuem menos liquidez do que as opções at the money. Uma menor negociação provoca maiores spreads entre preços de compra e preços de venda, que faz com que um vendedor de opção cobre um prêmio maior pela falta de liquidez, pois teria mais dificuldade de reverter a posição.

O motivo da formação do sorriso de volatilidade pode ser apenas um dos motivos anteriormente citados, ou pode ser uma combinação dos dois motivos, ou seja, é difícil determinar uma única razão. A Figura 8.2 apresenta graficamente o que chamamos de bid-ask-smile, é o sorriso formado pelos melhores preços de venda e de compra das opções em cada um dos strikes:

---

Figura 8.2 | Bid-ask smile
![img-78.jpeg](img-78.jpeg)
Fonte: Elaborada pelos autores.

É possível notar, na figura anterior, que existe um spread de volatilidade maior nas opções in e out of the money do que na opção at the money. Esse fenômeno, de certa forma, corrobora a premissa de que a menor liquidez pode fazer com que os spreads de volatilidade fiquem um pouco mais abertos nos extremos.

## 8.2.1 Preços das opções durante o pregão

Para o cálculo do sorriso de volatilidade podemos usar o preço do último negócio ou os melhores preços de compra ou venda de cada uma das opções, preços que podem ser observados no book de negociação em bolsa das opções, em determinado momento do pregão.

No entanto, pode acontecer, que em poucos segundos de negociação, o último negócio fique abaixo do preço de compra ou acima do preço de venda, como devemos proceder nesse caso?

Se o último negócio for menor do que o preço de compra ou maior do que o preço de venda, devemos substituí-lo pela média aritmética simples entre preço de compra e preço de venda da opção. Vamos denominar este como o último negócio ajustado.

---

Esse procedimento deve ser adotado porque utilizaremos a volatilidade implícita do último negócio ajustado para calcular as gregas, e não poderíamos trabalhar com uma variável defasada que poderia fornecer gregas distorcidas.

## 8.2.2 Superfície de volatilidade

Quando calculamos o sorriso de volatilidade em vários vencimentos das opções, adicionaremos um terceiro eixo, resultando em um gráfico em três dimensões. A Figura 8.3 apresenta uma superfície de volatilidade, sendo que no eixo horizontal estão os strikes, no eixo vertical está a volatilidade anualizada e na profundidade está o prazo até vencimento da opção.

Figura 8.3 | Superfície de volatilidade
![img-79.jpeg](img-79.jpeg)
Fonte: Elaborada pelos autores.

Na superfície anterior, as opções de prazos mais longos estão à frente, enquanto as de prazos mais curtos estão ao fundo. Na figura seguinte, mostramos a mesma superfície de volatilidade em perspectiva distinta, com os prazos mais longos ao fundo e os mais curtos à frente:

---

Figura 8.4 | Superfície de volatilidade – Outra perspectiva
![img-80.jpeg](img-80.jpeg)
Fonte: Elaborada pelos autores.

A superfície de volatilidade é uma composição de vários sorrisos de volatilidade para opções com prazos de vencimento diferentes. Nos negócios com volatilidade, apostamos nos movimentos dessa superfície.

Quando negociamos volatilidade, estamos, na verdade, apostando nos movimentos da superfície de volatilidade. Ao vender opções de um determinado ativo-objeto a um cliente corporativo, a instituição financeira tem como referência a superfície de volatilidade das opções daquele ativo-objeto. Em verdade, o spread que o banco cobra nesse tipo de operação é em volatilidade, adicionando este à superfície.

Os movimentos da superfície de volatilidade são os seguintes:

- A superfície de volatilidade pode ter um **movimento de nível**, ou seja, um deslocamento paralelo em toda a sua estrutura, quando há um aumento geral nas volatilidades implícitas das opções daquele ativo-objeto.
- Pode ter um **movimento de inclinação calendário**: quando as volatilidades dos vencimentos mais curtos se movimentam de forma distinta das dos vencimentos mais longos. A estrutura pode se inclinar ou desinclinar.

---

- Pode haver um movimento lateral: quando há mudanças no preço do ativo--objeto, o que é bem comum, algumas opções que estavam out of the money podem se tornar at the money, ou vice-versa. Da mesma forma, uma in the money, pode se tornar at the money, ou deep in the money, dependendo do movimento do ativo-objeto.
- Concavidade do smile: o smile possui certa concavidade, que, por determinadas condições de mercado, pode ficar momentaneamente plano, ou seja, sem concavidade (flat). Existem operações que é possível comprar a concavidade ou a inclinação do sorriso (skew).

## 8.3 Cone de volatilidade

O cone de volatilidade é um recurso que auxilia o operador na tomada de decisão na compra ou na venda de volatilidade implícita com as opções.

É importante lembrar que o cone não pode ser o único critério para tomada de decisão, o operador deverá conhecer e acompanhar o comportamento da superfície de volatilidade e utilizar o cone apenas como um recurso de apoio para a tomada de decisão.

O cone é formado por janelas móveis de volatilidade histórica. Dessas janelas móveis, devem-se extrair os valores máximos e mínimos das volatilidades históricas, como também os seus intervalos com 95% de confiança.

## Exemplo 8.2 - Cone de volatilidade

Com base em uma amostra histórica de retornos de um ativo-objeto, calculamos janelas móveis de volatilidade dentro de um período exato de um ano, o que resultou em 248 retornos históricos.

Calculamos para 10, 15, 20 e 25 dias de janelas móveis.

Por exemplo, na janela móvel de 10 dias, fazemos isso dia a dia, utilizando os 10 últimos retornos, o que resultou em uma amostra de 239 desvios-padrões. Repetimos os cálculos para janelas de 15 retornos, que resultou em uma amostra de 234 desvios, e assim por diante.

---

Na tabela a seguir são exemplificados valores de máximo, mínimo e média da volatilidade histórica dentro do período de um ano:

Tabela 8.1 | Resultados do cone de volatilidade
|   | 10 | 15 | 20 | 25  |
| --- | --- | --- | --- | --- |
|  Média | 44,51% | 46,18% | 47,12% | 47,51%  |
|  Máximo | 85,81% | 79,17% | 72,52% | 67,31%  |
|  Mínimo | 23,69% | 28,57% | 29,88% | 33,78%  |

Fonte: Elaborada pelos autores.

A figura a seguir apresenta os resultados do cone de volatilidade com os valores obtidos na tabela:

Figura 8.5 | Cone de volatilidade
![img-81.jpeg](img-81.jpeg)
Fonte: Elaborada pelos autores.

Com base no cone de volatilidade, devemos comprar volatilidade quando a volatilidade implícita tocar no limite mínimo e, consequentemente, vender quando esta tocar no limite máximo.

---

Como o cone de volatilidade é calculado com base na volatilidade histórica, é bem possível que a volatilidade implícita possa ultrapassar os limites definidos no cone, principalmente em tempos de crise.

Podemos também calcular um intervalo de confiança para as volatilidades do cone, ou seja, podemos calcular o desvio-padrão das volatilidades e seu respectivo intervalo de confiança em uma distribuição normal.

Tabela 8.2 | Resultados do cone de volatilidade com 95% de confiança

|   | 10 | 15 | 20 | 25  |
| --- | --- | --- | --- | --- |
|  Média | 44,51% | 46,18% | 47,12% | 47,51%  |
|  Superior | 64,05% | 62,99% | 62,23% | 61,27%  |
|  Inferior | 24,97% | 29,37% | 32,01% | 33,76%  |
|  Desvio-padrão | 11,88% | 10,22% | 9,19% | 8,36%  |

Fonte: Elaborada pelos autores.

A tabela anterior apresenta o intervalo superior somando-se 1,6549 desvios em relação à média, e o intervalo inferior, subtraindo-se a mesma quantidade de desvios. O que nos fornece um intervalo de confiança bicaudal de 95%.

A figura a seguir apresenta o cone de volatilidade, calculado com base em intervalos de confiança:

Figura 8.6 | Cone de volatilidade com 95% de confiança
![img-82.jpeg](img-82.jpeg)

---

Fonte: Elaborada pelos autores.

# 8.4 Operações com volatilidade

Vamos começar com as estratégias com volatilidade, com suas possibilidades em relação à superfície de volatilidade e as principais formas de operar.

# 8.4.1 Operações com robô

Atualmente, é quase inviável realizar qualquer operação não-direcional que não seja com o uso de um robô, um algoritmo que calcule e envie suas ordens diretamente ao sistema da bolsa.

O ideal é contratar um robô pronto, previamente testado, que tenha um servidor com um mínimo de latência em relação ao sistema da bolsa.

Qual a diferença entre um operador humano e um robô?
O robô realiza os cálculos com base em um algoritmo, envia as ordens ao sistema da bolsa e verifica a execução. O operador humano realiza as mesmas etapas, porém, de forma mais demorada.

Uma vantagem dos robôs são as ordens multileg, ou seja, podem enviar ordens simultâneas em diversos derivativos ou ativos, em mercados diferentes, dado um certo parâmetro predefinido pelo usuário. O parâmetro define a relação de variáveis que são calculadas com os preços de ativos e derivativos ou preços de compra ou venda, nas filas de ordens.

---

Programar um sistema para colocar ordens em seu próprio servidor físico pode não ser uma boa ideia. A distância entre a sua localização física e o sistema da bolsa pode aumentar o tempo de execução, e atrasos de milésimos de segundo podem inviabilizar as operações.

É preciso verificar também a velocidade dos algoritmos programados no robô. Alguns robôs são mais lentos do que outros devido ao código de programação. Alguns possuem códigos mais enxutos em linguagens de programação de execução mais rápida. Certamente, esses robôs executarão as ordens com maior velocidade.

O roteamento das ordens por parte da corretora deve também pesar no momento da escolha, pois o tempo decorrido no: i) cálculo do algoritmo no servidor, ii) roteamento da ordem e iii) execução da ordem é crucial para o sucesso das operações com volatilidade.

O programa instalado no servidor, denominado robô, é o que elabora e envia as ordens. Ao mesmo tempo em que envia a sua ordem, também envia as de outros usuários.

A capacidade computacional instalada, dado o número de ordens enviadas e executadas, é uma das variáveis que também deve ser considerada, na hora de escolher o robô.

O usuário seleciona quais instrumentos operará, parametrizando o programa instalado no servidor. O robô simplesmente calcula e dispara o envio de ordens, quando as condições de mercado satisfazem os parâmetros definidos no algoritmo do programa pelo usuário.

A figura a seguir representa graficamente, de forma resumida, a execução de uma ordem por meio de um robô:

Figura 8.7 | Execução de ordem com robô

---

![img-83.jpeg](img-83.jpeg)
Fonte: Elaborada pelos autores.

Atualmente existem diversos tipos de robô, alguns são programados para atender à necessidade de cada tipo de operação e de usuário, outros são robôs multifuncionais, com diversos algoritmos pré-programados. A melhor forma de selecionar o robô mais adequado para as suas operações é testando as múltiplas alternativas que existem no mercado, cuja interface lhe seja mais amigável de interagir e que a ordem seja executada a contento.

## 8.4.2 Compra e venda de volatilidade

Nos negócios com volatilidade, o objeto de negociação é a volatilidade implícita no preço das opções. Podemos classificar as operações com volatilidade da seguinte forma: ■ Compra de volatilidade (vega positiva): uma posição comprada em volatilidade é aquela em que um acréscimo na volatilidade implícita das opções proporciona lucro. A posição comprada aposta na abertura da volatilidade implícita.

■ Venda de volatilidade (vega negativa): inverso da compra de volatilidade, um decréscimo na volatilidade implícita das opções que compõem a carteira proporciona lucro. A posição vendida aposta no fechamento da volatilidade implícita.

■ Arbitragem de volatilidade (vega neutra): é uma posição montada para não ficar nem vendida, nem comprada em volatilidade. É neutra em volatilidade, um acréscimo ou decréscimo na volatilidade não afeta o resultado. Procura travar um ganho com opções que estão com volatilidades irregulares, proporcionando um ganho com o equilíbrio do mercado.

---

Nessas operações não se opera o preço do ativo, por isso o delta deve ser sempre neutralizado. Portanto, deve ser feita a manutenção do delta para que este fique sempre zerado. As operações de volatilidade ocorrem em períodos distantes do vencimento. Quanto à velocidade de execução, as operações podem ser divididas de duas formas: Curto prazo (1 dia): aproveitam o movimento dos preços de opções no intraday e procuram arbitrar a ineficiência das volatilidades implícitas. Pode ser feito, por exemplo, com apenas um tipo de opção.

- Longo prazo (mais de 1 dia): especulação em abertura ou fechamento da volatilidade em vários dias, mantendo a posição em carteira até a realização da estratégia, incorrendo em custo de carregamento e calibração do delta da posição. O custo de carregamento pode ser classificado em dois tipos:

- efeito gama: custo de neutralização do delta;
- efeito theta: custo do emagrecimento do preço da call.

## 8.4.3 Volatilidade com ativo à vista

A operação mais simples com volatilidade é a que utiliza apenas uma opção e o ativo à vista.

Podemos ficar comprados em volatilidade, comprando uma call e vendendo, simultaneamente, o ativo-objeto à vista para fazer o delta hedge, ou ao contrário, vendendo volatilidade com a venda de call e comprando ativo à vista para zerar o delta.

A vantagem de se utilizar o ativo-objeto à vista é que esse possui apenas uma grega: o delta do ativo, que é sempre igual a 1.

Para realizar o delta hedge, podemos fazê-lo da seguinte forma:

- Vendido em volatilidade: ficarmos vendidos na call e comprados no ativo-objeto, na proporção de 1 opção para Δ ativo:

---



[ - C; + Δ S ₀ ] tag {8.2}



- Comprado em volatilidade: ficarmos comprados em call e vendidos no ativo-objeto:



[ + C; - Δ S ₀ ] tag {8.3}



Esse tipo de operação é simples, a ponto de ser até ingênua, sendo o primórdio das operações com volatilidade, mesmo assim, possui efetividade quando executada com precisão.

A desvantagem desse tipo de operação ocorre pelo fato de que o ativo à vista possui um custo financeiro elevado para sua compra ou venda a descoberto, o que pode limitar a alavancagem nas estratégias com volatilidade. Outra desvantagem é que a liquidação financeira das ações e opções ocorrem em períodos diferentes, por exemplo, as opções liquidam em D+1, enquanto as ações liquidam em D+2. É preciso tomar cuidado na montagem e desmontagem dessas operações para não "estourar" o caixa, pois quando compramos opções e, simultaneamente, vendemos ações, os recursos da venda das ações só entram em conta um dia útil depois do débito da compra de opções.

## Relação das operações de volatilidade e as gregas

Agora, vamos analisar as operações com volatilidade com ativo-objeto à vista, e a relação dessas operações com as gregas, apresentadas na Tabela 8.3 a seguir:

Tabela 8.3 | Volatilidade com call e ativo à vista e posição nas gregas

|  Grega | Comprado em volatilidade | Vendido em volatilidade  |
| --- | --- | --- |
|  Delta | Neutro | Neutro  |
|  Gama | Positivo | Negativo  |
|  Vega | Positivo | Negativo  |

---

Theta Negativo Positivo Rô Positivo Negativo

Fonte: Elaborada pelos autores.

Vamos começar falando do theta. Quando a posição é carregada por mais de um dia, o theta passa a ser relevante. Por exemplo, em uma posição comprada em volatilidade, o theta negativo provoca um emagrecimento diário da opção, provocando perdas.

O inverso ocorre em uma operação vendida em volatilidade.

Por outro lado, o gama positivo pode proporcionar ganhos em uma operação comprada em volatilidade, pois favorecerá na execução do delta hedge.

Em uma posição gama positiva, vendemos na alta e compramos na baixa, proporcionando ganhos com o delta hedge. Em compensação, teremos uma perda diária por estarmos vendidos em theta.

O gama positivo proporcionará ganhos porque estamos comprados em opções, quando o preço do ativo-objeto aumenta, o delta também aumenta, fazendo com que a carteira fique comprada – para fazer o delta hedge precisamos vender parte da posição em ativo-objeto ou calls para mantermos o delta zerado. Na posição gama positiva, quando o preço do ativo-objeto diminui, o delta diminui, fazendo com que a carteira fique vendida, teremos de comprar mais ações do ativo-objeto ou calls para mantermos o delta zerado.

Carregar uma posição gama negativa de um dia para outro pode provocar perdas inesperadas na abertura do pregão do dia seguinte, isso ocorre porque, apesar do pregão ser interrompido durante a noite, o mercado continua agindo; uma forte crise na abertura do pregão pode provocar uma queda abrupta no preço do ativo-objeto, transformando uma operação vendida em volatilidade em um grande pesadelo direcional, passível de perdas consideráveis.

---

Quanto maior o vega da posição, maior será a exposição à volatilidade, ou seja, se estivermos vega positivo em um cenário de aumento de volatilidade implícita, um vega maior proporcionará maiores ganhos. Logo, quanto mais at the money a opção estiver, maiores serão os ganhos.

## Exemplo 8.3 - Operação de volatilidade com ativo à vista

Temos uma call, negociada a R$ 1,89, com delta igual a 0,50 e vega igual a 0,058 (para cada variação de 1% da volatilidade anualizada), suponha que a ação, ativo-objeto dessa call, está sendo negociada a R$ 39,29 por ação, suponha também que queiramos montar uma estratégia que proporcione um ganho de R$ 15.000,00 para cada ponto percentual de abertura (aumento) na volatilidade implícita. Como podemos montar essa estratégia?

O primeiro passo será determinar quantas opções precisamos comprar para obter um vega total de R$ 15.000,00 na carteira. Sabendo que a grega da carteira é igual a soma das gregas dos instrumentos que a compõem, dividimos o vega da carteira pelo da opção:



Q_(CALL) = 15.000/0,058 = 258.621



Logo, necessitaremos comprar 258.621 calls para a montagem da carteira de vega igual a R$ 15.000. Vamos arredondar o lote para múltiplos de 100, ou seja 258.600. Agora, vamos determinar o delta da carteira, resultante da posição em call, multiplicando o delta da opção pela sua quantidade, conforme o seguinte cálculo:



Deltaₙ = (0,50) · 258.600 = 129.300



Logo, o delta da carteira será igual a 129.300, ou seja, para fazer o delta hedge, teremos que vender 129,3 mil ações. Para carregar a posição por mais de um dia, antes teremos de fazer um empréstimo de ações, para podermos vendê-las a descoberto. O empréstimo de ações ocasionará chamada de margem e consequente depósito de garantias em bolsa, além do custo do próprio aluguel.

O valor marcado a mercado dessa estratégia é igual à posição comprada das opções e à vendida das ações, multiplicado pelos seus respectivos valores, que seria igual

---

a:



MtM = 258.600(1,89) - 129.300(39,29) = -4.591.443



Esse resultado significa que a carteira gerou um financeiro marcado a mercado de - R$ 4.591.443,00.

## 8.4.4 Spread de volatilidade

Agora, vamos abordar uma das operações de volatilidade mais utilizadas atualmente no mercado. Nessa operação não haverá necessidade do ativo-objeto, apenas opções. Para operar volatilidade não é obrigatório se negociar o ativo-objeto, nem mesmo tê-lo em carteira.

A vantagem desse tipo de operação é que necessita apenas de depósito de margem inicial e um caixa necessário para compra e venda de opções, que é bem menor, comparado ao caixa necessário para compra e venda de ações, como apresentado no tópico anterior.

O objetivo dessa estratégia é a neutralização do delta, substituindo o ativo-objeto por uma call deep in the money.

> Uma call deep in the money possui delta elevado, próximo de 1 e baixa liquidez quando comparada às opções at the money. Também possui gama, vega e theta relativamente baixos, o que faz dessa opção uma excelente substituta ao ativo-objeto.

Estratégia de compra de volatilidade que consiste em posição comprada em uma call at the money e vendida em outra call deep in the money com vega baixo, ambas de mesmo vencimento e strikes diferentes.

A call deep in the money simula o ativo à vista, e a posição fica com o delta neutro, sem utilizar ativo à vista. O delta hedge, nesse caso, pode ser feito vendendo uma quantidade, na proporção invertida de deltas, da opção de strike menor E_1 com relação à opção de strike maior, E_2, da seguinte forma:

---



[ - Delta_(E ₂) C_(E ₁), + Delta_(E ₁) C_(E ₂) ] tag {8.4}



Sendo:

C_(E1): call de preço de exercício menor deep in the money C_(E2): call de preço de exercício maior at the money Delta_(E1): delta da opção de preço de exercício menor

Delta_(E2): delta da opção de preço de exercício maior

A Figura 8.8 a seguir representa a posição dos strikes relativos aos seus respectivos preços de exercício:

Figura 8.8 | Spread delta neutro com opções
![img-84.jpeg](img-84.jpeg)
Fonte: Elaborada pelos autores.

A rigor, podemos fazer spread de volatilidade e delta hedge com qualquer par de opções, desde que sejam de um mesmo vencimento. Os pares podem ser out of the money, in the money ou at the money. É possível comprar ou vender volatilidade praticamente com qualquer par de opções, desde que tenham strikes diferentes.

## Exemplo 8.4 - Spread de volatilidade

Temos uma call₁, deep in the money, negociada a R$ 5,88, com delta igual a 0,89 e vega igual a 0,027 e uma call₂, at the money, negociada a R$ 1,89, com delta igual a 0,50 e vega igual a 0,058. Suponha também que queiramos montar uma estratégia que proporcione um ganho de R$ 15.000,00 para cada ponto percentual de abertura (aumento) na volatilidade implícita. Como podemos montar essa estratégia?

---

O primeiro passo é determinar quantas opções precisamos comprar e vender para obter um vega resultante de R$ 15.000,00 na carteira. Sabendo que a grega da carteira é igual à soma das gregas dos instrumentos que a compõem, o vega resultante da carteira pode ser descrito pela seguinte equação:



V _Π = Q ₁ V ₁ + Q ₂ V ₂ = 1 5. 0 0 0 tag {8.5}



Sendo:

V₁: vega da call₁ deep in the money Q₁: quantidade da call₁

V₂: vega da call₂ at the money Q₂: quantidade da call₂

V_Π: vega total da carteira, nesse caso, igual a 15.000

O delta resultante da carteira é igual ao delta somado das duas opções, que deverá ser igual a zero. Se quisermos um delta neutralizado:



Delta_Π = Q ₁ Delta₁ + Q ₂ Delta₂ = 0 tag {8.6}



Sendo:

Delta₁: delta da call₁ deep in the money Delta₁: delta da call₂ at the money Delta_Π: delta total da carteira, nesse caso, igual a zero Com as equações do vega e do delta, teremos um sistema de equações:



{ {l} Q ₁ V ₁ + Q ₂ V ₂ = 1 5. 0 0 0 
 Q ₁ Delta₁ + Q ₂ Delta₂ = 0   tag {8.7}



Agora, vamos substituir os valores das gregas das opções no sistema de equações:



{ {l} Q ₁ (0, 0 2 7) + Q ₂ (0, 0 5 8) = 1 5. 0 0 0 
 Q ₁ (0, 8 9) + Q ₂ (0, 5 0) = 0  



Devemos resolver o sistema para descobrir os valores de Q₁ e Q₂.

Isolando o valor de Q₂ na segunda equação do delta:



Q ₂ = - Q ₁ (0 , 8 9)/(0 , 5 0)



E substituir na equação do vega:

---



- Q ₁ (0 , 8 9)/(0 , 5 0) (0, 0 5 8) + Q ₁ (0, 0 2 7) = 1 5. 0 0 0



Colocando o  Q₁  em evidência, teremos:



Q ₁ (0, 0 2 7 - 0, 1 0 3 2 4) = 1 5. 0 0 0



Logo, teremos  Q₁  igual a:



Q ₁ = - 1 5 . 0 0 0/0 , 0 7 6 2 4 = - 1 9 6. 7 4 7



O resultado indica que devemos ficar vendidos em 196.747 opções deep in the money. Vamos arredondar a quantidade para 197.700 e obter a quantidade da outra call, consequentemente,  Q₂  será igual a:



Q ₂ = - 1 9 6. 7 0 0 (0 , 8 9)/(0 , 5 0) = 3 5 0. 1 2 6



Conforme o resultado dos calculos, devemos ficar comprados em 350.126 opções de delta igual a 0,50 e vendidos em 196.700 opções de delta igual a 0,89. Sabendo que as opções de ações são negociadas em lotes múltiplos de 100, vamos arredondar as quantidades para 350.100 e 196.700.

O valor marcado a mercado da carteira é igual a posição das opções, multiplicada pelos seus respectivos valores:



M t M = 3 5 0. 1 0 0 (1, 8 9) - 1 9 6. 7 0 0 (5, 8 8) = - 4 9 4. 9 0 7



A posição marcada a mercado resultou em um financeiro de R$ 494.907, comparativamente, bem inferior à posição da estratégia que utiliza o ativo-objeto à vista para o delta hedge, para obter o mesmo vega resultante de R$ 15.000.

Com relação a depósito de garantias, nessa estratégia estamos vendidos na opção de strike menor, logo, haverá chamada de margem para essas opções.

---

# 8.4.5 Arbitragem de volatilidade vega neutra

As operações de arbitragem tem como objetivo obter um pequeno lucro, porém correndo um risco menor. Para isso, é necessário operar grandes volumes de opções.

Podemos montar uma estratégia de arbitragem de volatilidade neutralizando o vega e o delta, simultaneamente. Essa estratégia consiste em aproveitar pequenos momentos de distorção de volatilidade implícita entre dois strikes de opções de um mesmo vencimento.

A distorção mais comum ocorre na concavidade do smile. Em alguns momentos, o smile pode ficar flat, ou seja, plano.

Nesse momento, surge a oportunidade de comprar a concavidade do smile, apostando que este se forme novamente, com o equilíbrio dos preços e consequente aumento do coeficiente quadrático. Na verdade, a operação de arbitragem utiliza apenas um dos lados do smile, montando uma operação denominada skeW.

O skew consiste em comprar ou vender a inclinação da volatilidade entre dois strikes de opções, procurando ganhar com a mudança da diferença da volatilidade implícita entre essas opções.

O skeW vertical é montado com opções de mesmo vencimento, enquanto que o skeW horizontal é feito com opções de datas de vencimento distintos. Geralmente, nas operações de skeW, operamos com vega e delta neutralizados.

A neutralização do vega permite que movimentos de nível na superfície de volatilidade não afetem o resultado da carteira, apenas movimentos de inclinação das volatilidades implícitas ou na concavidade do smile impactam o resultado.

---

Como realizar a operação de arbitragem de volatilidade?

Uma das maneiras é utilizar duas opções com volatilidades distintas e mesmo vencimento, comprando uma opção e vendendo a outra. A opção que vamos comprar é aquela na qual acreditamos que a volatilidade implícita esteja baixa e, consequentemente, venderemos a de volatilidade que consideremos mais alta. À primeira vista, essa operação é muito similar a um spread de volatilidade, a diferença está na proporção entre essas opções. No spread tradicional, utilizamos o par de opções para neutralizar o delta. Na arbitragem de volatilidade, essa proporção será utilizada para neutralizar o vega e ficar exposto apenas no delta. Contudo, o delta pode ser neutralizado com um terceiro instrumento, que pode ser o ativo-objeto à vista ou uma opção deep in the money.

É importante lembrar que, se optarmos por neutralizar o delta com uma opção deep in the money, esta opção também possui vega, logo, também deverá entrar na equação de neutralização do vega.

Uma posição vega neutra é theta e gama quase neutras para opções de mesmo vencimento.

A gama neutralidade da posição unida à sua theta neutralidade faz com que a operação de arbitragem possa ser virtualmente "esquecida" pelo operador, que precisa dedicar pouco esforço ao seu ajuste.

Quais são os riscos envolvidos na operação de arbitragem de volatilidade?

- Alteração no valor das gregas com a mera passagem do tempo;
- Variação severa da volatilidade implícita das opções;
- Mudança de at the moneyness das opções, que alteram os patamares das gregas.

A operação de arbitragem de volatilidade pode ser feita com duas calls de mesmo vencimento e com a neutralização do delta com ativo-objeto à vista. Observando a Figura 8.9 a seguir, a call do lado direito, E_2, de strike maior, está out of the money, enquanto que a call do lado esquerdo E_1, de strike menor, está at the money. Podemos observar que o smile está flat, logo, iremos comprar a opção de strike E_2 e vender a opção de strike E_1, apostando no aumento da concavidade do smile, para curva pontilhada, e

---

consequentemente, que a diferença, em termos de volatilidade, entre E₂ e E₁, também aumente.

Figura 8.9 | Arbitragem de volatilidade vega neutra
![img-85.jpeg](img-85.jpeg)
Fonte: Elaborada pelos autores.

Logo, iremos comprar a opção E₂ e vender a E₁ de forma que se neutralize o vega, e o delta será neutralizado com o ativo-objeto à vista, conforme a seguinte estrutura:



[ - V_(E₂) C_(E₁), + V_(E₁) C_(E₂), (Delta_(E₁) - Delta_(E₂)) S₀ ] 



## Concavidade do smile de volatilidade

Podemos monitorar a concavidade do smile por meio do coeficiente quadrático de uma regressão polinomial das volatilidades implícitas em relação aos strikes de opções de mesmo vencimento. A regressão pode ser feita pelo método de mínimos quadrados ordinários.

O coeficiente do componente quadrático indicará a concavidade do smile, identificando possibilidades de arbitragem. Na equação seguinte, os valores de x são os preços de exercício, enquanto que o valor de y são as volatilidades implícitas de opções de um mesmo vencimento:



y = a x² + b x + c + ε 



Quanto mais positivo for o coeficiente a, maior será a concavidade do smile, se o coeficiente estiver próximo de zero, indica que o smile está flat.

---

Exemplo 8.5 - Operação de arbitragem de volatilidade

Vamos partir da premissa de que o sorriso de volatilidade está flat, e que surgiu uma oportunidade para montar uma estratégia de arbitragem, que consistirá em se posicionar, apostando no aumento de inclinação da volatilidade entre duas opções, call₁ e call₂. Desejamos montar a estratégia de tal forma que ganhemos R$ 15.000 para cada ponto percentual de abertura no diferencial de volatilidade entre essas opções.

A call₁ está at the money, negociada a R$ 1,89, com delta igual a 0,50 e vega igual a 0,058. A call₂ está out of the money, negociada a R$ 0,65, com delta igual a 0,23 e vega igual a 0,045, e a ação, ativo-objeto dessas calls, está negociada a R$ 39,29 por ação. Ambas opções possuem volatilidades implícitas iguais a 35% a.a.o.

A tabela a seguir apresenta todas as gregas das opções que serão utilizadas na estratégia de arbitragem:

Tabela 8.4 | Gregas das opções utilizadas na arbitragem

|   | call₁ | call₂  |
| --- | --- | --- |
|  Posição | Vendida | Comprada  |
|  Delta | 0,50 | 0,23  |
|  Gama | 0,078 | 0,060  |
|  Vega (1%) | 0,058 | 0,045  |
|  Theta (1 du) | -0,034 | -0,025  |

Fonte: Elaborada pelos autores.

Suponha também que queiramos montar uma estratégia que fique neutra em movimentos de nível na superfície de volatilidade implícita, ou seja, o vega da carteira deve ficar neutralizado. Como podemos montar essa estratégia?

O primeiro passo será determinar quantas opções precisamos comprar e vender para que o vega fique neutro, porém, essa quantidade deverá permitir que ganhemos R$ 15.000 para cada ponto percentual de abertura no diferencial de volatilidade implícita entre as opções.

---

Devemos determinar as quantidades das call₁ e call₂ para obtermos um vega neutro, mas que proporcione o ganho esperado no diferencial. A quantidade Q₁ da call₁ pode ser obtida dividindo-se o lucro esperado pelo seu vega:



Q₁ = 15.000/0,058 = 258.621



Logo, teremos de vender 258.621 opções call₁, que arredondaremos para 258.600 opções.

A quantidade Q₂ da call₂ também pode ser obtida dividindo-se o lucro esperado pelo seu vega:



Q₂ = 15.000/0,045 = 333.333



Logo, teremos de comprar 333.333 opções call₂, que arredondaremos para 333.300 opções.

Resta apenas calcular a quantidade de ativo-objeto necessário para neutralizar o delta. O delta resultante da carteira é igual à soma dos deltas das duas opções e do ativo-objeto:



Delta_Π = Q₁ Delta₁ + Q₂ Delta₂ + Q_s(1) = 0 



Sendo:

- Delta₁: delta da call₁
- Delta₂: delta da call₂
- Q₂: quantidade de ativo-objeto
- Delta_Π: delta total da carteira, nesse caso, igual a zero. Vamos substituir as respectivas quantidades das calls e obter a quantidade do ativo-objeto:



-258.600(0,5) + 333.300(0,23) + Q_s(1) = 0





Q_s = 52.641



Logo, para realizar o delta hedge, teremos de comprar 52.641 ações.

Conforme o resultado dos cálculos, devemos ficar vendidos em 258.600 calls de delta igual a 0,50, comprados em 333.300 calls de delta igual a 0,23 e comprados em 52.600 ações (ativo-objeto), arredondados em múltiplos de 100.

O valor marcado a mercado da carteira é igual à posição das opções e das ações, multiplicada pelos seus respectivos valores:

---



MtM = -258.600(1,89) + 333.300(0,65) + 52.600(39,29) = 1.179.4545



A posição marcada a mercado resultou em um financeiro de R$ 1.794.545. Ficou um pouco maior do que estratégias que usam somente opções, porque utilizamos o ativo-objeto para o delta hedge. Alternativamente, poderíamos ter usado uma opção deep in the money, no lugar do ativo-objeto. Dessa maneira, poderíamos dispendêr menos caixa e alavancar mais a posição. Em contrapartida, a opção deep in the money também possui vega, e teríamos de a incluir na equação de neutralização do vega.

Com relação ao depósito de garantias, nessa estratégia estamos vendidos na opção de strike menor, logo, haverá chamada de margem para essas opções.

Agora, vamos ver as gregas da carteira em nosso exemplo, o delta da carteira estará praticamente neutralizado e será igual a:



Deltaₙ = -258.600(0,5) + 333.300(0,23) + 52.600(1) = -41



O vega estará neutralizado:



Vₙ = -258.600(0,058) + 333.300(0,45) = 0



Assim como o gama e o theta estarão em valores próximo de zero, dada a dimensão da posição e o volume de opções:



{l}
Gammaₙ = -258.600(0,078) + 333.300(0,06) = -172 

Thetaₙ = -258.600(-0,034) + 333.300(-0,025) = -460 





Um theta negativo de R$ 460 significa que perderemos R$ 460 para cada dia de carregamento da posição, que é relativamente pequeno, dado que montamos uma estratégia que resulta em R$ 15.000 para cada ponto percentual de abertura no diferencial da volatilidade.

---

# 8.4.6 Spread gama neutro

Operação de spread gama neutro permite manter uma carteira mais estável, principalmente na abertura do pregão no dia seguinte. Carregar uma posição gama negativa de um dia para o outro pode provocar perdas inesperadas na abertura do pregão do dia seguinte. A estratégia gama neutra pode evitar esse tipo de risco.

Vamos relembrar que uma posição gama negativa poderá ficar direcional se houver um movimento brusco no preço do ativo-objeto, e, como consequência, haverá custos para realização do delta hedge.

Uma posição com gama neutralidade é praticamente vega neutra e theta neutra, o que permite certa tranquilidade no carregamento da posição.

## Posições de bancos com clientes e o efeito gama

As carteiras de opções feitas pelos bancos no mercado de balcão, geralmente, precisam ser carregadas até o vencimento, pois são estratégias que fizeram para seus clientes, que, na maioria dos casos, mantêm essas opções até o vencimento.

Quando o banco vende uma opção para um cliente, na verdade, este banco está operando volatilidade e deverá manter esta carteira delta hedgeada, mas não obrigatoriamente, gama neutralizada.

É importante lembrar que o gama "explode" próximo ao vencimento nas opções at the money e, dessa forma, é aconselhável a neutralização do gama, se este estiver negativo.

Esse procedimento tornará o carregamento da carteira muito mais estável próximo ao vencimento.

## Estratégia gama neutra

---

Uma posição de gama neutralidade pode ser feita com duas ou mais opções, na qual utilizamos uma das opções para a zeragem do gama e, consequentemente, ficaremos expostos no delta, que pode ser neutralizado com o ativo-objeto. Nessa estratégia, o gama da carteira deve ser neutralizado, conforme a seguinte equação:



Gamma_Π = Σ(j=1 até n) Gamma_j Q_j = 0   (8.11)



Sendo:

- Gamma_Π: gama da carteira
- n: número de opções na carteira
- Gamma_j: gama da j-ésima opção
- Q_j: quantidade da j-ésima opção

Agora, podemos realizar a zeragem do delta, que pode ser com o ativo-objeto ou, alternativamente, com um contrato futuro no ativo-objeto:



Delta_Π = Σ(j=1 até n) Delta_j Q_j + Delta_S Q_S = 0   (8.12)



Sendo:

- Delta_Π: delta da carteira
- n: número de opções na carteira
- Q_j: quantidade da j-ésima opção Delta_j: delta da j-ésima opção
- Delta_S: delta do ativo-objeto, que é sempre igual a 1
- Q_s: quantidade do ativo-objeto

## Exemplo 8.6 - Spread gama neutro

Vamos realizar uma operação de spread calendário, gama neutra, na qual estaremos comprados em uma call de vencimento mais longo E₂ e vendidos na call de vencimento mais curto E₁, conforme a seguinte figura, que representa a superfície de volatilidade:

---

Figura 8.10 | Spread gama neutro
![img-86.jpeg](img-86.jpeg)
Fonte: Elaborada pelos autores.

Em suma, iremos comprar call de vencimento e strike iguais a E₂ e vender a call igual a E₁ de forma que se neutralize o gama, e o delta será neutralizado com o ativo-objeto à vista, conforme a seguinte estrutura:



- Gamma_(E ₂) C_(E ₁), + Gamma_(E ₁) C_(E ₂), (Delta_(E ₁) - Delta_(E ₂)) A ₀ tag {8.13}



Sabendo que o preço da ação é R$ 39,29, as gregas e os preços das opções que serão utilizados na estratégia estão apresentadas na tabela a seguir:

Tabela 8.5 | Gregas e outras informações das opções

|   | E₁ | E₂  |
| --- | --- | --- |
|  Posição | Vendida | Comprada  |
|  Preço | 1,89 | 2,53  |
|  Strike | 40 | 40  |
|  Prazo (dias úteis) | 35 | 56  |
|  Delta | 0,50 | 0,53  |
|  Gama | 0,078 | 0,061  |
|  Vega | 0,058 | 0,074  |
|  Theta | -0,034 | -0,028  |

Fonte: Elaborada pelos autores.

Vamos supor que queremos um ganho de R$ 15.000 para cada ponto percentual de abertura na volatilidade da opção de vencimento mais longo, E₂. Logo, podemos determinar a quantidade dessa opção, dividindo o lucro da operação pelo seu vega:

---



Q ₂ = 1 5 . 0 0 0/0 , 0 4 5 = 3 3 3. 3 3 3



Portanto, devemos comprar 203.435 opções de vencimento mais longo E₂ e arredondaremos a quantidade para 203.400 opções.

Em seguida, obteremos a quantidade da opção mais curta, pela neutralização do gama, conforme a seguinte equação:



Gamma_Π = Q ₁ Gamma₁ + Q ₂ Gamma₂ = 0 tag {8.14}



Sendo:

Gamma₁: gama da call - E₁

Gamma₂: gama da call - E₂

Gamma_Π: gama total da carteira, nesse caso, igual a zero. Substituindo os valores, teremos a quantidade da opção E₁, da seguinte forma:



Q ₁ (0, 0 7 8) + 2 0 3. 4 0 0 (0, 0 6 1) = 0





Q ₁ = - 2 0 3 . 4 0 0 (0 , 0 6 1)/0 , 0 7 8 - 1 5 9. 0 9 6



Logo, a quantidade de calls E₁, de vencimento mais curto, será vendida em 159.096 opções, arredondaremos a quantidade para 159.100.

Agora, determinaremos a quantidade de ativos-objetos que deverá ser utilizada para o delta hedge, conforme a seguinte equação:



Delta_Π = Q ₁ Delta₁ + Q ₂ Delta₂ + Q _s (1) = 0 tag {8.15}



Sendo:

Delta₁: delta da call - E₁

Delta₂: delta da call - E₂

Q_s: quantidade de ativo-objeto

Delta_Π: delta total da carteira, nesse caso, igual a zero. Substituindo as quantidades obtidas e os deltas na equação, teremos:



- 1 5 9. 1 0 0 (0, 5 0) + 2 0 3. 4 0 0 (0, 5 3) + Q _S (1) = 0





Q _S = - 2 8. 2 5 2



---

Teremos de vender a descoberto 28.252 ações, podendo arredondar a quantidade para 28.300. É importante lembrar que o aluguel das ações tem um custo, e deverá haver depósito de margem, na venda a descoberto. Também devemos nos lembrar que podemos usar, em substituição à ação, uma opção deep in the money. Caso optemos pela opção deep in the money, devemos considerá-la também na equação de neutralização do gama.

A posição marcada a mercado dessa estratégia é a seguinte:



-159.100(1,89) + 203.400(0,53) - 28.300(39,29) = -898.004



Portanto, o valor financeiro da posição é de -R$ 898.004,00. O valor negativo é resultante, principalmente, da venda a descoberto das ações (ativo-objeto). É importante lembrar que em uma posição geradora de caixa, geralmente teremos de depositar margem.

Além da margem necessária para a venda de call de vencimento mais curto E_1, teremos de depositar margem para o aluguel (BTC) das ações, vendidas a descoberto.

Agora, vamos analisar as gregas dessa estratégia, ao final, temos de estar com o gama e o delta hedgeados.

Vamos calcular o delta e gama da carteira:



Delta_Π = -159.100(0,50) + 203.400(0,53) + 28.300(1) = -48





Gamma_n = -159.100(0,078) + 203.400(0,061) = -2,4



Com delta e gama neutralizados, vamos calcular o vega e theta:



V_Π = -159.100(0,058) + 203.400(0,074) = 5.824





Theta_Π = -159.100(-0,034) + 203.400(-0,028) = -285,80



Com base nos resultados expostos anteriormente, estaremos comprados em volatilidade, principalmente devido a posição comprada na opção de vencimento mais longo E_2, e pagaremos um theta diário de R$ 285,80.

---

# 8.4.7 Volatilidade a termo

Nas operações calendário ou horizontais devemos monitorar a inclinação da superfície de volatilidade, com base nas volatilidades a termo. É mais usual calcularmos as volatilidades implícitas das opções de mesmo strike, porém de vencimentos distintos, e a volatilidade a termo entre elas.

Porém, é mais aconselhado, quando possível, calcular a volatilidade a termo de opções de vencimentos distintos, com base na similaridade do delta, por exemplo, duas opções que tenham delta próximo de 0,50. Na figura a seguir podemos observar o conceito da volatilidade a termo:

Figura 8.11 | Volatilidade a termo
![img-87.jpeg](img-87.jpeg)
Fonte: Elaborada pelos autores.

A definição de volatilidade à vista é aquela que começa na data de hoje e termina em uma data futura, como é o caso, na figura, das volatilidades sigma_1 e sigma_2. A volatilidade a termo pode ser definida como uma volatilidade que começa no futuro e termina em um futuro mais distante, que é a volatilidade sigma_(termo), uma volatilidade intermediária, compreendida entre as volatilidades sigma_1 e sigma_2.

Vamos calcular a volatilidade partindo da premissa de que essas são independentes e identicamente distribuídas, dentro dos períodos n_1 e n_2, medidos em dias úteis. Podemos supor que a volatilidade no período possa ser calculada com base na raiz quadrada da variância, ajustada pelo tempo:



sigma_(1,n_1) = √{sigma_(1,n_1)^2} = √(n_1/252 sigma_1^2) 



---

Logo, a volatilidade a termo pode ser calculada da seguinte forma:



sigma_(termo) = √( ( n_2/252 sigma_2^2 - n_1/252 sigma_1^2 ) ( 252/(n_2 - n_1) ) ) 



Podemos cortar o 252 da equação da seguinte forma:



sigma_(termo) = √(  ( n_2 sigma_2^2 - n_1 sigma_1^2 ) / ( n_2 - n_1 )  ) 



A volatilidade sigma_2 é uma média ponderada das duas volatilidades sigma_1 e sigma_(termo). Se a superfície de volatilidade estiver com uma inclinação negativa, significa que sigma_1 > sigma_(termo),

logo, sigma_2 > sigma_(termo). Se a superfície de volatilidade estiver com inclinação positiva, teremos sigma_1 < sigma_(termo) e, consequentemente, sigma_2 < sigma_(termo).

Com base na análise das volatilidades a termo, podemos elaborar estratégias calendário, comprando ou vendendo essas volatilidades.

## Exemplo 8.7 – Cálculo de volatilidade a termo

Vamos calcular a volatilidade a termo de duas volatilidades implícitas, a primeira, de 28% a.a.o., com vencimento em 21 dias úteis, e a segunda, em 32% a.a.o., com vencimento em 40 dias úteis.

O resultado do cálculo da volatilidade a termo é o seguinte:



sigma_(termo) = √(  ( 40(0,32^2) - 21(0,28^2) ) / (40 - 21)  ) = 35,91\%



---

Podemos entender que a superfície de volatilidade está com inclinação positiva, o que poderia sugerir uma estratégia de venda de volatilidade a termo por meio de um spread calendário.

## RESUMO

Neste capítulo apresentamos as operações com volatilidade e as exposições nas letras gregas, assim como as operações de spread e arbitragem de volatilidade.

## EXERCÍCIO PROPOSTO

1. Utilizando as seguintes opções de ação e suas gregas, prepare as seguintes estratégias, fornecendo o número de contratos:

|  Código OPT | Prazo du | Strike | Delta | Gama | Vega (1%) | Theta dia | Rô (1%)  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  G32 | 22 | 32,00 | 0,9355 | 0,0395 | 0,0134 | (0,0274) | 0,0220  |
|  G36 | 22 | 36,00 | 0,5643 | 0,0795 | 0,0419 | (0,0557) | 0,0137  |
|  G38 | 22 | 38,00 | 0,3597 | 0,1032 | 0,0398 | (0,0384) | 0,0091  |
|  G40 | 22 | 40,00 | 0,0909 | 0,0672 | 0,0174 | (0,0110) | 0,0024  |
|  H36 | 42 | 36,00 | 0,6007 | 0,0831 | 0,0568 | (0,0336) | 0,0278  |
|  H38 | 42 | 38,00 | 0,3952 | 0,1136 | 0,0566 | (0,0239) | 0,0192  |
|  H40 | 42 | 40,00 | 0,2826 | 0,0743 | 0,0497 | (0,0243) | 0,0135  |
|  Ação |  |  | 1,0000 |  |  |  |   |

a. Comprada em 350 vols de G40 com delta hedge à vista.
b. Vendida em 676 vols de G36 com spread delta neutro utilizando a G32.
c. Arbitragem de vol com spread vega neutro vendido em 20.000 contratos de G36 e comprado em X contratos de G38. Faça o delta hedge à vista.
d. Spread calendário gama neutro vendido em 20.000 contratos de G36 e comprado em X contratos de H38. Faça o delta hedge à vista.

---

CAPITULO 9

# Derivativos de commodities

---

Decidimos dedicar um capítulo exclusivo ao mercado de commodities pela sua relevância na economia brasileira e pela lacuna deste assunto na literatura nacional sobre derivativos. Começaremos explicando os conceitos e variáveis necessários para a compreensão da formação de preços das commodities à vista e futura. Na segunda parte do capítulo, mostraremos o uso de técnicas econométricas na modelagem de preços das commodities.

Os modelos de formação de preços de derivativos de commodities envolvem múltiplos conceitos teóricos. Por isso, tentamos tratar o tema com a abrangência necessária, desenvolvendo os conceitos imprescindíveis com maior profundidade.

A abordagem sobre o mercado de derivativos de commodities foi feita da seguinte forma:

a. Conceitos fundamentais: apresentamos as características dos mercados de commodities e os papéis de seus participantes.

b. Teoria da estocagem: definimos as regras que regem a estrutura de preços peculiar aos mercados à vista e futuro de commodities.

c. Modelagem dos preços: mostramos a evolução dos modelos de formação de preços de commodities.

## 9.1 Conceitos fundamentais do mercado de commodities

Commodity pode ser definida como um ativo físico que possui características padronizadas, de ampla negociação em diversas localidades, que pode ser transportado e armazenado por um longo período de tempo.

Commodity ainda pode ser definida como um tipo de produto no qual não há diferenças qualitativas entre os mercados onde é negociado, ou seja, entre negócios de um mesmo produto em mercados diferentes, não existe preferência, em termos de qualidade, por parte dos compradores do produto. Pode haver pequenas

---

diferenças

de qualidade entre cada lote negociado, essas diferenças devem estar dentro de limites aceitáveis e previamente especificados em contratos de fornecimento.

Ainda sobre a definição da terminologia – de acordo com Geman (2005, p. 1), o termo *commodity* pode ser atribuído a um bem de consumo cuja escassez, na forma de exaustão na extração, ou na redução de estoques globais, causará um impacto no preço em âmbito mundial. Dadas as volatilidades das diferentes moedas no mundo, uma *commodity* terá o mesmo valor em termos relativos, nas diferentes moedas, podendo ser utilizada como referência de valor.

É comum que a terminologia *commodity* seja atribuída aos insumos ou matérias-primas. Isso ocorre porque os insumos ainda não foram industrialmente transformados, o que facilita a padronização. Quando um produto sofre transformação na indústria, ganha características particulares que o distinguem, dificultando a padronização e a negociação em larga escala.

A *commodity* é um ativo cuja padronização permite a execução de maior número de negociações, o que favorece a liquidez.

Em mercados organizados, como as bolsas de valores, é importante que as modalidades de ativos negociadas permitam a presença de liquidez, que, nesse caso, pode ser entendida como a facilidade de entrar e sair de uma posição, comprada ou vendida. Se um determinado agente do mercado está em uma posição comprada em determinado ativo, ele conseguirá, em um mercado líquido, sair da posição rapidamente, vendendo seu ativo. Uma condição necessária para a presença de liquidez em mercados organizados é a padronização, que permite agilidade nas negociações, partindo-se da premissa de que as contrapartes envolvidas na operação saibam previamente as características da mercadoria negociada.

A *commodity*, para permitir liquidez nas negociações em um mercado organizado, deve possuir, simultaneamente, segundo Kaldor (1939, p. 3), uma série de atributos, descritos a seguir:

a. o ativo deve ser totalmente padronizado em suas características;

---

b. deve ser um bem de demanda generalizada;
c. deve ser um bem não perecível, ou seja, o ativo não deve perder valor com a mera passagem do tempo;
d. o valor do ativo deve ser proporcional ao volume.

Há apenas duas classes de ativos que satisfazem a condição necessária para negociação em larga escala. A primeira classe são as commodities, negociadas em mercados organizados; a segunda classe de ativos são os financeiros, como títulos e ações, que possuem, em grau máximo, todos os atributos anteriormente descritos.

As commodities podem ser negociadas em diferentes tipos de mercados: no mercado à vista, que envolve entrega física imediata da mercadoria, ou ser negociada como referência nos mercados derivativos.

# 9.2 Mercado à vista, termo e futuro de commodity

## 9.2.1 Mercado à vista

Um produto físico padronizado deve sempre ser negociado no mercado à vista. O mercado à vista é a negociação de compra e venda de um determinado ativo com entrega imediata. No caso dos ativos financeiros, esse processo ocorre de forma simples e ágil, pois eles são escriturais e a liquidação ocorre em curtíssimos espaços de tempo.

Com commodities a negociação à vista é um pouco menos trivial. A liquidação de uma operação à vista com commodities envolve as condições de entrega física do produto, documentação para transporte, contratação de frete, logística na estocagem, seguros, e, no caso de exportação, procedimentos aduaneiros. Além disso, para que a entrega física da mercadoria ocorra, é necessário que o produtor tenha disponibilidade de

---

estoque, no volume, no local e na qualidade exigidas pelo comprador. Por esses motivos, na negociação à vista no mercado de commodities, sempre haverá uma defasagem mínima entre o momento de negociação e a entrega efetiva da mercadoria.

Os custos de frete, de logística e de seguros podem ser assumidos pelo comprador ou pelo vendedor. A venda é classificada como FOB (Free on Board) se o comprador arcar com as despesas de frete e seguro. Se o custo da entrega for responsabilidade do vendedor, é classificada como CIF (Cost, Insurance and Freight). Essas terminologias, comuns no comércio internacional, também são utilizadas no mercado doméstico de commodities físicas.

A entrega da commodity, como explicado anteriormente, depende da disponibilidade dos estoques e de uma relação de fornecimento entre o produtor vendedor e a indústria compradora da mercadoria. O fornecimento de commodity é a etapa inicial na cadeia produtiva e a escassez de estoques pode provocar a interrupção desse processo.

Durante a negociação, o comprador da indústria sempre deseja pagar o menor preço possível para ampliar suas margens, em contrapartida, depende do fornecimento contínuo para manter sua atividade.

O produtor vendedor, por outro lado, deseja obter o maior preço possível por sua mercadoria. Se o mercado fornecedor em questão não for monopolista e se a commodity for armazenável, o produtor pode aguardar para obter o melhor preço de venda, retendo o fornecimento.

Essa estratégia será eficiente apenas se o incremento nos preços for superior ao custo marginal de armazenagem.

O poder monopolista ocorre apenas quando o vendedor tem a habilidade de incrementar os preços acima de seu custo marginal. Em um mercado competitivo de commodity, isso não ocorrerá se o comprador tiver a opção de comprar de outros fornecedores.

Em consequência do descompasso nas necessidades entre compradores e vendedores, o mercado à vista de commodities favorece a presença de intermediários, ou **trading**, que facilitam a negociação e a entrega física

---

entre a indústria e os produtores de commodities, evitando a interrupção no fornecimento.

As commodities negociáveis podem ser provenientes do agronegócio, como é o caso da soja, do milho, do algodão, do açúcar e do álcool, ou provenientes da atividade de extração, como no caso do petróleo, do gás, do minério de ferro, dos metais não ferrosos e dos minerais não metálicos.

As commodities provenientes do agronegócio diferenciam-se das do mercado extrativista por possuírem sazonalidade, devido aos períodos de safra e entressafra.

A sazonalidade na produção das commodities agrícolas dificulta a adequação temporal do fornecimento do agronegócio às necessidades da demanda na indústria.

A relação de interdependência entre os fornecedores e compradores de commodities físicas favorece a adoção de contratos de fornecimento entre os membros da cadeia produtiva, o que representa uma vantagem não só para o comprador, pois mantém a continuidade no fornecimento, mas também para o vendedor, pois garante a venda da mercadoria.

Os contratos de fornecimento são comuns em negociações com commodities de agronegócio. Eles estabelecem a data, as características da mercadoria e o volume negociado. No contrato também pode ser estipulado antecipadamente o preço que será pago pela mercadoria na entrega futura, um preço a termo.

O contrato de fornecimento é o primeiro passo para a introdução dos participantes do mercado de commodities nos contratos derivativos em sua modalidade mais simples, que é o contrato a termo.

## 9.2.2 Mercado a termo

O contrato a termo de commodities é tipicamente negociado no mercado de balcão, também conhecido como OTC (Over-The-Counter). Nesse mercado, os contratos a termo são negociados diretamente entre as partes, as operações não são padronizadas e as contrapartes podem assumir o risco

---

de crédito da operação ou, alternativamente, contratar um seguro de crédito ou os serviços de uma câmara de liquidação.

Em um contrato a termo de commodity há duas partes envolvidas: o comprador, que assume o compromisso de comprar o ativo físico, com entrega em data futura e pagar por ele a um preço preestabelecido e o vendedor, que se compromete a entregar a mercadoria na data estabelecida.

No contrato a termo, as contrapartes assumem o risco de liquidação, que é dividido em liquidação física e liquidação financeira. A liquidação física consiste na entrega da mercadoria e a financeira, no pagamento pela mercadoria entregue. Em ambos os casos, pode ocorrer inadimplência, tanto na liquidação física quanto na financeira.

No contrato a termo de commodity, a liquidação pode ser física ou por ajuste por diferença. Na liquidação do tipo ajuste por diferença, não há entrega física da mercadoria, apenas liquidação financeira, na qual as contrapartes acordam em pagar a diferença entre o preço a termo e o preço de mercado.

Algumas instituições divulgam o preço de mercado que serve como referência para as liquidações de contratos por diferença. No Brasil, entre as instituições mais referenciadas está o Centro de Estudos Avançados em Economia Aplicada (Cepea) – entidade criada por docentes da Escola Superior de Agricultura Luiz de Queiroz (Esalq-USP).

O quadro a seguir mostra algumas das mercadorias cujos preços são divulgados pelo Cepea:

Quadro 9.1 | Indicadores de preços divulgados pelo Cepea

|  Mercadoria | Volume | Periodicidade  |
| --- | --- | --- |
|  Açúcar Cristal | Saco de 50 kg | Diária  |
|  Etanol anidro e hidratado | Litro | Semanal  |
|  Algodão | Arroba | Diária  |
|  Café arábica | Saca de 60 kg | Diária  |
|  Milho | Saca de 60 kg | Diária  |

---

Soja
Saca de 60 kg
Diária

Fonte: Cepea.

# 9.2.3 Mercado futuro de commodity

Mais padronizado do que o mercado a termo, o mercado futuro de commodity está presente em mercados organizados de bolsas. Os contratos futuros possuem, de maneira geral, maior volume de negociação do que o contrato a termo, portanto são mais líquidos, mais transparentes para as partes envolvidas e publicamente divulgados, servindo como referência na formação de preços.

A liquidação do contrato futuro também pode ser física ou por diferença. Nas negociações do mercado futuro, as contrapartes não se conhecem, são anônimas, porém as operações são publicamente divulgadas. No Brasil, a bolsa de maior expressão na negociação de contratos futuros de commodities é a B3, antiga BM&FBOVESPA.

A estrutura moderna de negociação em mercados futuros, de acordo com Geman (2005, p. 9), surgiu nos Estados Unidos, na segunda metade do século 19. Em 1848, foi fundada a Chicago Board of Trade (CBOT), que, desde o início, operava commodities agrícolas. Atualmente, existem diversas bolsas de negociação de commodities ao redor do mundo. No quadro a seguir, estão listadas as principais bolsas de negociação de contratos futuros de commodities:

Quadro 9.2 | Bolsas de negociação de commodities

|  Commodities negociadas | Bolsas | Siglas  |
| --- | --- | --- |
|  Açúcar, etanol, boi gordo, café arábica, milho, soja | Brasil, Bolsa, Balcão | B3  |
|  Açúcar, cacau, café e algodão | New York Mercantile Exchange | NYMEX  |
|  Açúcar, cacau, café robusta e batata | London International Financial | LIFFE  |

---

|   | Futures Exchange |   |
| --- | --- | --- |
|  Açúcar, cacau e café | Coffe, Sugar and Cocoa Exchange | CSCE  |
|  Petróleo, gasolina e gás propano | New York Mercantile Exchange | NYMEX  |
|   |  International Petrol Exchange (Londres) | IPE  |
|   |  Hong Kong Futures Exchange | HKEX  |
|   |  Philadelphia Board of Trade | PBOT  |
|  Trigo, milho, soja, prata e ouro | Chicago Board of Trade | CBOT  |
|  Toucinho de porco, celulose, ouro e clima | Chicago Mercantile Exchange | CME  |
|  Algodão e arroz | Chicago Rice and Cotton Exchange | CRCE  |
|  Trigo, milho e suco de laranja | Minneapolis Grain Exchange | MGE  |
|   |  New York Cotton Exchange | NYCE  |
|   |  New York Mercantile Exchange | NYMEX  |
|  Metais | New York Mercantile Exchange | NYMEX  |
|   |  London Metal Exchange | LME  |
|   |  Commodity Exchange | COMEX  |
|  Eletricidade | Nordic Power Exchange | NORDPOOL  |
|   |  European Energy Exchange | EEX  |
|   |  Amsterdam Power Exchange | APX  |
|   |  Paris Power Exchange | POWERNEXT  |

Fonte: Elaborado pelos autores.

# 9.2.4 Mercados de açúcar e etanol

---

Os principais mercados de negociação de contratos futuros de açúcar estão localizados em Nova Iorque, na NYMEX, e em Londres, na LIFFE. Os contratos futuros de açúcar são negociados também em São Paulo, na B3. As características dos contratos futuros negociados nas bolsas são as seguintes:

a. NYMEX: o contrato de açúcar n. 11, foi o primeiro contrato de commodity agrícola negociado em bolsa, desde 1936. O tamanho do contrato é de 112 mil libras-peso, o equivalente a 50 toneladas, a cotação é feita em centavos de dólar por libra-peso. O tipo de liquidação é financeiro, por meio de ajuste por diferença, sem entrega física. Os vencimentos dos contratos ocorrem nos meses de março, maio, julho e outubro.

b. LIFFE: são negociados dois tipos de contrato: o contrato de açúcar bruto e o açúcar branco – raw sugar e white sugar. O açúcar cristal branco n. 407, o mais negociado, possui as mesmas características do contrato da NYMEX, com 50 toneladas por contrato e cotado em centavos de dólar por libra-peso, com vencimentos nos mesmos meses da NYMEX. A diferença é que o contrato da LIFFE permite a entrega física FOB (Free On Board), em locais designados pela bolsa e dentro das especificações por ela determinadas.

c. B3: o contrato futuro de açúcar negociado conforme as regras da B3 é o açúcar cristal especial com mínimo de 99,7 graus de polarização, máximo de 0,08% de umidade e máximo de 0,07% de cinzas. O tamanho do contrato é de 508 sacas de 50 quilos e cotado em centavos de real por saca. Os vencimentos ocorrem nos meses de fevereiro, abril, julho, setembro e dezembro. A liquidação do contrato é financeira.

O contrato futuro de etanol é negociado na B3, cotado em reais por metro cúbico.

O tamanho do contrato é de 30 metros cúbicos, com vencimentos em todos os meses do ano. A liquidação do contrato pode ser apenas financeira.

Tanto o contrato de etanol quanto o de açúcar atualmente possuem tímida negociação na B3.

---

Conforme visto anteriormente, os preços à vista, que servem como referência para os ajustes financeiros nos vencimentos dos contratos futuros de açúcar da B3, são divulgados em base diária pelo Cepea. Os preços do etanol são divulgados também pelo Cepea, porém em base semanal.

## 9.2.5 Mercados de petróleo

O petróleo é um tipo de commodity não padronizada, por isso os principais contratos futuros no mundo utilizam um pequeno número de tipos de petróleo como referência de produto físico para as negociações dos contratos futuros. As principais bolsas em que os contratos futuros de petróleo são negociados são a NYMEX, em Nova Iorque, e a IPE, em Londres. O primeiro vencimento do contrato futuro de petróleo negociado em Nova Iorque é referência mundial de formação de preços dessa commodity.

As características dos contratos futuros de petróleo negociados em bolsa são as seguintes:

a. NYMEX: o futuro de petróleo tipo WTI (West Texas Intermediate) negociado na NYMEX é o contrato futuro sobre commodity mais negociado no mundo. Quase 300 mil contratos de petróleo são negociados diariamente.

O tamanho do contrato é de mil barris de petróleo, podendo ser liquidado no vencimento por entrega física, cujo local de referência é Cushing, no estado de Oklahoma. O contrato, também denominado de light, sweet crude oil, possui baixo teor de enxofre, portanto, mais fácil de ser refinado para obtenção de derivados.

b. IPE: a International Petroleum Exchange, em Londres, é a bolsa de negociação de petróleo tipo Brent, também conhecido como Brent blend ou Brent de Londres. Entretanto, desde 2005 tem sido negociado eletronicamente na ICE (Intercontinental Exchange). O petróleo tipo Brent não é tão leve quanto o WTI e possui mais enxofre, sendo ideal para a produção de gasolina e outros derivados

---

intermediários, como querosene e diesel. A liquidação do contrato futuro pode ser física ou financeira. A cotação do contrato é feita em dólares por barril e o lote de negociação é de 1.000 barris de petróleo.

Até aqui apresentamos os conceitos fundamentais sobre as características dos contratos de commodities e seus principais mercados de negociação. Nas seções seguintes serão apresentadas algumas das abordagens teóricas que discutem o processo de formação de preços entre os mercados à vista e o mercado futuro de commodities.

Os preços formados nos mercados à vista e futuro deveriam, supostamente, seguir trajetórias paralelas. Uma queda no preço à vista deveria ser acompanhada por uma queda proporcional no preço do contrato futuro, devido aos princípios de arbitragem que regem a formação de preços futuros.

No mercado de commodities, o processo de formação de preços futuros pode romper as regras de arbitragem, causando fenômenos denominados como contango e backwardation. Na seção seguinte será discutida uma das teorias que tenta explicar os fenômenos de formação de preços das commodities em relação aos contratos futuros, denominada de teoria da estocagem.

## 9.3 Teoria da estocagem

A teoria da estocagem procura explicar a diferença de preços entre os mercados à vista e futuro de commodities. Em certas ocasiões, o preço à vista da mercadoria pode ficar acima do preço no mercado futuro. Isso ocorre porque o detentor da mercadoria física possui o benefício de reter os estoques e, em busca de melhores preços, aguardar um melhor momento para realizar a venda. O detentor do estoque, ao tomar essa decisão, deve levar em consideração algumas variáveis relevantes, tais como as taxas de juros, a sazonalidade nos preços, o custo de armazenagem e o benefício esperado com o aumento do preço de venda.

---

9.3.1 Princípios da teoria da estocagem

A premissa da teoria da estocagem é a de que o detentor da mercadoria física tem o benefício de reter o produto quando o preço de mercado estiver baixo e liberá-lo quando o preço à vista atingir patamares mais favoráveis. Essa estratégia somente é vantajosa para o detentor da commodity se o benefício marginal do aumento de preços exceder o custo de estocagem.

Existe uma relação entre o aumento dos preços da commodity e o volume global de estoques. Quando os estoques de uma determinada commodity são excepcionalmente grandes não há vantagem em reter o produto, pois não haverá escassez no fornecimento e o custo de estocagem, nesse caso, será maior do que o benefício em termos de preço.

Por outro lado, se os estoques são moderados e há alguma probabilidade de escassez, a competitividade da demanda pelo produto pode render ao detentor do estoque físico algum tipo de retorno. Nesse caso, o benefício da estocagem será maior do que o custo de armazenagem.

Esse comportamento na formação dos preços à vista da commodity interfere na relação de preços com o mercado futuro. Em certas ocasiões, o preço à vista pode ficar acima do preço no mercado futuro, devido à escassez de estoques. Para quantificar a diferença entre esses preços, Working (1948, p. 1258) sugere uma variável definida como price of storage.

Preço da estocagem ou price of storage é uma variável calculada pela diferença entre o preço futuro e o preço à vista, ou a diferença entre dois contratos futuros com vencimentos distintos. Pode ser um valor positivo ou negativo. O preço de estocagem negativo ocorre quando existe a probabilidade de escassez no fornecimento da commodity. O preço da estocagem, representado por F_t - S_t na equação a seguir, deve ser igual aos juros no período S_t r mais o custo marginal de armazenagem, menos o ganho marginal de conveniência para uma unidade adicional no estoque:

---



F_t - S_t = S_t r + W_t - C_t 



Sendo:

- S_t: preço do ativo à vista no tempo t
- F_t: preço do contrato futuro no tempo t, com vencimento em T, posterior a t
- r: taxa de juros livre de risco
- W_t: custo marginal de armazenagem no tempo t
- C_t: valor do ganho marginal de conveniência no tempo t

O ganho marginal pela conveniência é um valor financeiro que mede o ganho obtido pelo detentor da mercadoria física com o aumento do preço da commodity, em um momento em que os estoques globais estão baixos.

Nessa relação, o proprietário do estoque tem custos de taxa de juros livre de risco e de armazenagem, porém tem um ganho de conveniência compensatório, devido aos melhores preços de venda.

Quanto maior o ganho de conveniência de uma determinada commodity, mantidos constantes os custos de armazenagem e as taxas de juros, maior será o preço à vista, em relação ao preço do contrato futuro.

Se o ganho de conveniência for maior do que os juros e o custo de armazenagem, C_t > S_t r + W_t, o preço à vista da commodity será maior do que o preço futuro, resultando no fenômeno denominado de backwardation. Por outro lado, se C_t < S_t r + W_t, o preço futuro será maior do que o à vista, resultando no fenômeno denominado contango.

## 9.3.2 Custo de carregamento

O custo de carregamento é a soma de todos os custos para manutenção dos estoques da mercadoria física, é uma variável que determina a diferença de preços entre o mercado à vista e o mercado futuro da commodity. O custo de carregamento é calculado a partir do custo de financiamento -

---

representado pela taxa livre de risco, custo de armazenagem, custo de depreciação primária e retorno de conveniência. O custo de depreciação primária é a perda de valor do ativo com a mera passagem do tempo. Por exemplo, quando a mercadoria, ao longo do tempo, estraga no armazém no qual foi estocada.

Working (1948, p. 1) define o custo de carregamento como uma medida da "[...] diferença, em um dado momento, entre os preços de uma commodity para duas diferentes datas de entrega". O custo de carregamento deve ser uma variável que mede a relação entre os preços de mercadorias que tenham essencialmente a mesma qualidade, entregues no mesmo local, porém em diferentes datas.

Eventualmente, se os preços no mercado futuro estiverem excessivamente elevados, um agente do mercado pode, para obter ganho com a diferença de preços, comprar mercadoria física e, simultaneamente, vendê-la no mercado futuro. Nessa operação de arbitragem, o agente deve carregar a mercadoria física até o vencimento do contrato futuro, incorrendo no custo de carregamento. Essa operação é conhecida como cash and carry.

Se o inverso ocorrer, ou seja, o preço futuro estiver relativamente baixo, o agente pode vender o ativo à vista e, simultaneamente, comprá-lo no mercado futuro, realizando a operação denominada reverse cash and carry. Quando o mercado está em condição de não arbitragem, o agente de mercado não tem possibilidade de obter lucros sem assumir riscos. Uma operação reverse cash and carry pode ser feita em quatro etapas simultâneas:

i. o arbitrador toma o ativo à vista por arrendamento, pagando o retorno de conveniência  delta_r ;

ii. vende o ativo à vista pelo preço  S_r ;

iii. com os recursos provenientes da venda, aplica na taxa do ativo livre de risco  r ;

iv. para proteger-se contra oscilações do preço, adquire contratos futuros pelo preço  F_r .

Dessa forma, o resultado da operação, em condição de não arbitragem, é:

---



S _t e^(r (T - t)) = F _t e^(delta_t (T - t)) tag {9.2}



De acordo com a Equação 9.2, a diferença entre o preço futuro e o preço à vista da mercadoria é determinada pela taxa livre de risco, pelo retorno de conveniência e pelo prazo T - t até o vencimento do contrato futuro.

Em alguns trabalhos disponíveis na literatura, o custo de carregamento foi generalizado, e a variável delta_t foi definida apenas como retorno de conveniência, ou seja, os custos de armazenagem e depreciação primária foram omitidos na equação.

## 9.3.3 Contango e backwardation

Working (1948, p. 3) analisou, nos Estados Unidos, nas décadas de 1930 e 1940, as diferenças de preços à vista e futuro no mercado de trigo. Nos dados observados, identificou dois fenômenos, que definiu como contango e backwardation. O primeiro, ocorre quando os preços à vista estão abaixo dos preços futuros; o segundo, quando o preço à vista da commodity está acima do preço futuro.

Backwardation é o valor, medido em termos financeiros, da diferença entre o preço à vista e o preço no mercado futuro de determinada commodity. Logo, ocorre se S_t - F_t for um número positivo. É conveniente ressaltar que, mesmo na presença de backwardation, os preços à vista e futuro são intimamente relacionados. O preço à vista reflete todas as alterações ocorridas no preço futuro, ou seja, existe certo paralelismo na formação de preços.

A existência de backwardation nos preços das commodities tem base nas seguintes teorias:

a. a primeira teoria define o fenômeno como um prêmio pelo risco que o especulador merece por assumir o risco do hedger, que assume uma

---

posição predominantemente vendida no mercado futuro, no caso, o produtor que deseja garantir o preço de venda de sua commodity;

b. a segunda teoria justifica a existência de backwardation como resultante do retorno de conveniência;

c. uma terceira teoria explica o fenômeno de backwardation como resultante de erros de medida ou variável não observável;

d. e, ainda, uma quarta teoria procura defender o argumento de que o backwardation é causado pela distância dos estoques dos produtores em relação ao centro de consumo.

A primeira teoria tem base no trabalho de Johnson (1960, p. 140), que se referiu à presença de backwardation no mercado de commodities como consequência das operações de hedge. Os produtores de commodities, que usualmente assumem posição vendida no mercado futuro, pagam um prêmio pelo risco assumido pelos especuladores, fazendo, dessa forma, com que os preços futuros fiquem abaixo dos preços à vista.

A segunda teoria sugere que a existência do backwardation pode ocorrer, segundo Working (1948, p. 1), em decorrência de faltas momentâneas de estoque no mercado à vista, momento no qual o retorno de conveniência é máximo.

Frechette e Fackler (1999, p. 761) questionaram a explicação do fenômeno de backwardation pelas faltas momentâneas de estoque, pois é difícil justificar a existência de backwardation em períodos de safra das commodities agrícolas, quando não há falta de estoque. Os autores sugerem uma terceira teoria, ao afirmar que o fenômeno é mais afetado por erros de medida e variáveis não observáveis. Os autores explicam que os preços à vista são calculados pela média de preços de commodities negociadas em localidades diferentes, o que causa distorções em relação aos preços futuros. Essas distorções de preços são causadas porque, quando a média do preço à vista é calculada, pode haver falta de estoque em alguma das localidades,

---

fazendo com que o preço à vista médio seja mais elevado do que o preço futuro.

A quarta teoria, sugerida por Benirschka e Binkley (1995, p. 515), em seu trabalho com o mercado de milho nos Estados Unidos, assume que a existência de *backwardation* nos preços é causada pela distância dos estoques dos grandes centros de consumo, onde o preço da *commodity* é formado. Os modelos desenvolvidos pelos autores mostram que a distribuição espacial dos estoques, e não seu nível, é determinante da diferença dos preços. Para eles, em um mercado geograficamente disperso, o custo de oportunidade de estocar uma *commodity* aumenta com a distância do mercado comprador, ou seja, áreas produtoras mais distantes do mercado consumidor têm mais vantagens em estocar a *commodity* e o *backwardation* também aumenta com a distância.

Não se descarta a hipótese do *backwardation* dos preços de *commodity* ser explicado por mais de uma das teorias mencionadas. Acredita-se, ainda, que possam existir outras variáveis não identificadas, que também possam explicar o fenômeno.

## 9.3.4 Backwardation forte e fraco

O *backwardation* pode ser classificado de acordo com sua intensidade, fraco ou forte. *Backwardation* forte ocorre quando o preço à vista é maior do que os preços futuros, e o *backwardation* fraco, ocorre quando se consideram os preços futuros descontados a valor presente pela taxa livre de risco. O cálculo do *backwardation*, segundo a intensidade, pode ser feito da seguinte forma:



B_t^w = S_t - F_t e^(-r(T-t)) 





B_t^s = S_t - F_t



---

Sendo:

R̄_M: backwardation fraco

B_t^r: backwardation forte

Litzenberger e Rabinowitz (1995, p. 1520) verificaram a presença de backwardation nos preços dos contratos futuros de petróleo do WTI na NYMEX, no período de fevereiro de 1984 a abril de 1992. Observaram que, quanto mais longos os vencimentos dos contratos futuros, maiores os valores de backwardation, tanto para B_t^r quanto para B_t^r. Identificaram que no contrato WTI de vencimento mais curto, houve 81,80% de presença de backwardation fraco e 71,09% de backwardation forte. Para o contrato futuro mais longo, os valores percentuais subiram para 93,88% e 76,91%, respectivamente, para backwardation fraco e forte.

De acordo com a teoria da estocagem, a presença de backwardation é resultante de uma taxa de retorno de conveniência relativamente elevada.

## 9.3.5 Retorno de conveniência

O retorno de conveniência pode ser definido como uma remuneração, medida em termos de taxa de juros no ativo, que o detentor da commodity física recebe pela possibilidade de escassez de estoques. Segundo Frechette e Fackler (1999, p. 761), é um “[...] fluxo de benefícios não pecuniários [...]” que o dono da commodity física recebe e pode ser comparado como o retorno de dividendos de ativos do mercado financeiro. Retorno de conveniência e backwardation não são sinônimos. Backwardation é uma variável observável, verificada pela diferença de preços entre o mercado à vista e o futuro, enquanto o retorno de conveniência é um conceito econômico não observável.

O retorno de conveniência é um prêmio que faz jus ao proprietário do ativo físico, mas não ao proprietário do contrato futuro. Retorno de conveniência é como a opção de tempo embutida na commodity que o proprietário do ativo físico detém, que permite ao produtor vender a commodity quando os preços estiverem altos e segurar quando os preços estiverem baixos.

---

O retorno marginal de conveniência deve ser inversamente proporcional ao volume de estoque da commodity. No entanto, o volume de estoques pode ser tão grande que o retorno de conveniência seja, no limite, igual a zero.

O retorno de conveniência é expresso em termos de taxa delta_r, que aqui será tratada líquida do custo de armazenagem e depreciação primária.

Dessa maneira, a formação de preços de ativos, em condição de não arbitragem, sugere que a diferença entre o preço à vista e o futuro é decorrente da taxa livre de risco menos o retorno de conveniência:



F_t = S_t e^((r - delta_t)(T - t))   (9.4)



Sendo:

- S_t: preço do ativo à vista no tempo t
- F_t: preço do contrato futuro no tempo t
- T: vencimento do contrato futuro, posterior a t
- r: taxa livre de risco
- delta_t: retorno de conveniência

Nesse caso específico, o retorno de conveniência é representado pela taxa de arrendamento conhecida e não aleatória, ou seja, constante no tempo. Nesse caso, a formação de preços dependeria do processo estocástico de apenas uma variável, o preço do ativo S_t.

Partindo da premissa de que a volatilidade do retorno de conveniência é igual a zero, a volatilidade do preço à vista passa ser igual à volatilidade do preço do contrato futuro:



sigma_δ = 0 ⇒ sigma_s = sigma_F   (9.5)



A volatilidade no mercado de commodities possui um comportamento um pouco distinto comparado ao do mercado de ativos financeiros. Os níveis de estoque interferem na volatilidade dos preços das commodities. Algumas

---

dessas características sobre volatilidade nesse mercado são apresentadas a seguir:

- A volatilidade de preços de uma commodity tende a ser inversamente relacionada ao volume global de estoques. Quando não há estoque excedente para amortecer a demanda, os preços à vista tendem a oscilar mais.
- O preço de uma commodity e sua volatilidade são positivamente correlacionados, e ambos são negativamente correlacionados aos níveis de estoque. Essa característica distingue o comportamento dos preços de commodities e de ações. No mercado de ações, há aumento de volatilidade quando os preços caem. A volatilidade dos preços futuros de commodities tende a reduzir-se com o aumento do prazo para vencimento do contrato. Esse efeito é explicado pelo fato de que as notícias que afetam os níveis globais de estoque têm efeito imediato apenas nos contratos futuros de curto prazo. Os contratos de maturidades mais longas não sofrem tanto o efeito de notícias, pois o volume de produção tem tempo para ajustar-se antes do vencimento do contrato mais longo.

## 9.4 Modelagem de preços de commodities

### 9.4.1 Modelo com base no CAPM

Existem duas abordagens gerais para os modelos de formação de preços de commodity. A primeira, baseia-se no prêmio de risco sistemático da commodity e é medida por meio do beta do modelo de formação de preços de ativos de capital sugerida por Dusak (1973, p. 1393) e tem como base a teoria do Capital Asset Pricing Model (CAPM).

---

A outra abordagem baseia-se no retorno de conveniência e na teoria da estocagem.

O modelo de formação de preços de commodity com base no CAPM considera que o preço do contrato futuro de uma commodity é formado pelo valor esperado do preço à vista mais um prêmio pelo risco, que pode ser medido em termos de risco sistemático, ou seja, há um beta referente à commodity (βi). O retorno esperado da commodity pode ser calculado conforme a fórmula do CAPM:



E(R_i) = r + beta_i [ E(R_m) - r ] 



Sendo:

- E(R_i): retorno esperado da commodity i
- r: taxa de juros livre de risco
- E(R_m): retorno de mercado esperado

Dusak (1973, p. 1393) define a fórmula do retorno do preço de commodity para determinar o preço de contratos futuros também com base no CAPM. Partindo de beta_i = Cov(R_i, R_m) / σ^2(R_m), tem-se:



E(R_i) = r + [ E(R_m) - r/σ(R_m) ] Cov(R_i, R_m)/σ(R_m) 



Sendo:

- σ(R_m): desvio-padrão dos retornos da carteira teórica de mercado
- Cov(R_i, R_m): covariância esperada dos retornos da commodity e da carteira de mercado

O retorno esperado de uma commodity i para uma determinada data no futuro, representada por T, dependerá do valor esperado da commodity no

---

futuro, da seguinte forma:



E (R ᵢ) = E (S _T) - S _t/S _t tag {9.8}



Sendo:

E(S_T): preço esperado da commodity na data T

S_t: preço atual no mercado à vista de commodity

Dessa forma, pode-se obter o preço à vista da commodity por meio da seguinte equação:



S _t = E (R ᵢ) - S _t betaᵢ [ E (R _m) - r ]/(1 + r) tag {9.9}



O preço do contrato futuro com vencimento em T de uma determinada commodity pode ser estimado apenas por meio do preço à vista e pela taxa livre de risco, e supõe que F_t = S_t(1 + r). Sendo assim, o preço do contrato deverá ser:



F _t = S _t (1 + r) = E (R ᵢ) - S _t betaᵢ [ E (R _m) - r ] tag {9.10}



Portanto, é possível estimar a diferença percentual entre o preço esperado da commodity e o preço efetivo do contrato futuro com base no prêmio de risco sistêmico da commodity, conforme a seguinte equação:

---



E (R ᵢ) - F ᵢ/S ᵢ = betaᵢ [ E (R _m) - r ] tag {9.11}



O coeficiente de risco sistemático (betaᵢ) pode ser estimado de duas formas distintas: pode-se tomar o preço do ativo no mercado à vista ou o preço do contrato futuro, se o primeiro não estiver disponível para observação.

O modelo CAPM para commodities considera o risco sistemático como variável relevante, mas desconsidera variáveis importantes da teoria da estocagem, como o retorno de conveniência. Copeland e Weston (1988, p. 319) argumentam em favor do modelo com base no CAPM, pois afirmam que "por outro lado, a abordagem tradicional, com base na teoria da estocagem, ignora a possibilidade de que o risco sistêmico possa afetar os preços de equilíbrio dos contratos futuros de commodity". Pode ser levada em consideração a possibilidade de combinação das duas teorias, ou seja, levar em conta não apenas o prêmio de risco sistemático, mas também o retorno de conveniência e as premissas da teoria de estocagem em um modelo híbrido.

A seguir serão abordados os principais modelos que utilizam como base o retorno de conveniência e a teoria da estocagem.

## 9.4.2 Modelos de um, dois e três fatores

Os modelos de formação de preços de commodities evoluíram com inclusão de mais variáveis, tendo por objetivo explicar melhor o comportamento dos preços. As variáveis consideradas ou fatores adicionados ao modelo, foram as seguintes: o preço do ativo, o retorno de conveniência e as taxas de juros.

A modelagem de preços de commodities, com base em processos estocásticos dos preços, é abordada inicialmente no trabalho de Brennan e Schwartz (1985, p. 138). Os autores estudam a trajetória do preço da commodity para avaliar a viabilidade de investimentos de capital na

---

exploração de minas de cobre. O foco inicial da abordagem era introduzir o preço da commodity como variável determinante na decisão de investimento, teoria conhecida na literatura financeira como opções reais.

De acordo com a definição de Copeland e Antikarov (2001, p. 6), "uma opção real é o direito, mas não a obrigação, de empreender uma ação (por exemplo, diferir, expandir, contrair ou abandonar) a um custo predeterminado, que se denomina preço de exercício, por um período preestabelecido – a vida da opção", comumente utilizada em projetos de investimento de capital nos quais o preço de uma commodity é decisivo para a viabilidade econômica do projeto.

A opção real permite aos administradores tomarem decisões de investimento de capital com base na avaliação econômico-financeira e na maximização de valor para o proprietário do negócio. É um procedimento comumente utilizado em projetos de exploração de commodities não renováveis, como o petróleo. De acordo com o preço esperado da commodity, o administrador pode tomar decisões de expansão, retração, postergação, antecipação, ou mesmo de abandono de um projeto de exploração.

Brennan e Schwartz (1985, p. 139) estudaram a formação de preços de commodities com base no modelo de um fator, no qual utilizam como única variável aleatória do modelo o preço do ativo à vista, descrevendo um movimento browniano, de acordo com a seguinte equação:



d S/S _t = μ d t + σ d z   (9.12)



Em que dz é o choque aleatório de um processo de Wiener padrão, μ é o componente determinístico que representa a tendência no preço da commodity e σ é a volatilidade dos retornos.

Brennan e Schwartz (1985, p. 139), em seu trabalho, não incluíram o retorno de conveniência como variável aleatória. Os autores definiram o retorno de conveniência como o prêmio ao qual o detentor do ativo à vista

---

tem direito, considerando que o produtor pode obter ganhos ao controlar o processo produtivo ou aproveitando-se da falta do produto no mercado à vista. O retorno de conveniência é determinado pelos volumes de estoque do produto no mercado. A taxa de juros livre de risco foi considerada constante no modelo, restando apenas uma variável aleatória, o preço S_t da commodity.

Em trabalho posterior, Gibson e Schwartz (1990, p. 960) definem o modelo de dois fatores aplicado aos preços do barril de petróleo e assumem que o preço à vista e o retorno de conveniência seguem um processo estocástico conjunto. O preço da commodity segue um processo de passeio aleatório em tempo contínuo e o retorno de conveniência, um processo de reversão à média, conforme as seguintes equações:



d S/S _t = mu_S d t + sigma_S d z _S tag {9.13}





d δ = varphi_δ (mu_δ - delta_t) d t + sigma_δ d z _δ



Sendo:

δ_t: retorno de conveniência

μ_δ: valor de equilíbrio médio estimado para o retorno de conveniência

φ_δ: velocidade de reversão à média do retorno de conveniência

d z_S  e  d z_δ: são choques aleatórios correlacionados, d z_S d z_δ = ρ dt

Em seus resultados com os preços futuros de petróleo WTI na New York Mercantile Exchange, Gibson e Schwartz (1990, p. 974) verificaram que o retorno de conveniência possui mais volatilidade do que o preço à vista e que, quanto maior a maturidade, menor a volatilidade do preço do contrato.

Utilizando uma técnica econométrica chamada de filtro de Kalman, Schwartz (1997, p. 925) comparou os modelos: (i) um fator, no qual considera apenas o preço como variável aleatória, seguindo um processo de passeio aleatório em tempo contínuo; (ii) dois fatores, utilizando, além do

---

movimento browniano do preço à vista, um processo de reversão à média para o retorno de conveniência; e o (iii) modelo de três fatores, que agrega a taxa de juros r como variável aleatória, seguindo um processo de reversão à média.

O modelo de três fatores possui a seguinte estrutura:



{l}
dS/S_t = (r_t - delta_t) dt + sigma_s dz_s 

dδ = varphi_δ (mu_δ - delta_t) dt + sigma_δ dz_δ   (9.14) 

dr = varphi_r (mu_r - r_t) dt + sigma_r dz_r 





Sendo:

- r_t: taxa de juros em t
- mu_r: valor de equilíbrio médio estimado para as taxas de juros
- varphi_r: velocidade de reversão à média para as taxas de juros
- dZ_s, dZ_δ, dZ_r: choques aleatórios correlacionados:



{l}
dz_s dz_δ = rho_1 dt 

dz_δ dz_r = rho_2 dt   (9.15) 

dz_s dz_r = rho_3 dt 





# 9.4.3 Modelos de curto e de longo prazos

---

Em trabalho mais recente, Schwartz e Smith (2000, p. 895) desenvolveram um modelo distinto de dois fatores para preço de commodity, utilizando os preços do petróleo para os testes. Diferentemente dos trabalhos anteriores, supõem que o preço à vista sofre um processo de reversão à média e os preços dos contratos futuros de maturidades mais longas tendem a um preço de equilíbrio. Consideram que os choques de curto prazo, definidos como a diferença entre o preço spot e o preço de equilíbrio, têm reversão a zero, seguindo um processo Ohrnstein-Uhlenbeck.

Para Schwartz e Smith (2000, p. 894), os choques aleatórios de curto prazo são "consequência de mudanças na demanda de curto prazo, causadas por alterações climáticas ou interrupções de fornecimento intermitentes". Essas irregularidades de fornecimento são compensadas pela habilidade dos participantes do mercado de ajustar seus estoques.

Por exemplo, em determinada região pode haver falta momentânea de estoque de determinada commodity agrícola e consequente interrupção no fornecimento. Esse fenômeno poderia causar um aumento de curto prazo no preço da commodity na região. Esse choque aleatório faria com que a safra no período seguinte fosse compensada com um aumento na produção, motivada pela alta nos preços da commodity. Maior oferta na safra seguinte faria com que o preço revertesse a seu equilíbrio original.

No modelo curto prazo/longo prazo, Schwartz e Smith (2000, p. 894) definem que:

[...] mudanças nos preços dos contratos futuros de longo prazo de maturidade oferecem informações sobre as mudanças no preço de equilíbrio, e as mudanças nas diferenças de preços entre os futuros de curto e longo prazos, oferecem informação sobre os desvios (choques) de curto prazo.

O preço à vista da commodity é decomposto em dois fatores:



ln (S _t) = chi_t + omega_t tag {9.16}



Sendo:

---

chi_t: variações nos preços de curto prazo no tempo t

omega_t: nível do preço de equilíbrio no tempo t

Os desvios de curto prazo seguem um processo de reversão à média e o preço de equilíbrio segue um processo de movimento browniano:



{l}
d chi_t = - varphi_(chi) chi_t dt + sigma_(chi) dz_(chi)   (9.17) 

d omega_t = mu_ω dt + sigma_ω dz_ω




Em que dZ_x e dZ_ω são incrementos aleatórios correlacionados de um movimento browniano padronizado, sendo dz_x.dz_ω = rho_(xω) dt. O coeficiente de reversão à média varphi_x representa a velocidade cujos desvios de curto prazo irão desaparecer, dado que mu_x = 0.

Mudanças de curto prazo nos preços, de acordo com Schwartz e Smith (2000, p. 895), são resultantes, por exemplo, de mudanças climáticas, e não persistem com o tempo. Por outro lado, mudanças no preço de equilíbrio são mudanças fundamentais que persistem com o tempo. Em seu trabalho, os autores definem uma versão risco-neutra para formação de preços de opções do tipo europeia para commodities. Utilizaram o filtro de Kalman para formular o modelo de curto prazo/ longo prazo, trabalhando com as variáveis em tempo discreto, com base no relacionamento das variáveis de estado e os preços dos contratos futuros da commodity.

# 9.4.4 Teoria da paridade de duas commodities de Walras

Para desenvolver as premissas necessárias para a especificação de modelos de formação de preços de commodity, parte-se da teoria apresentada por Walras (2003, p. 87) de que uma commodity, em um mercado perfeitamente competitivo, pode ser representada, em termos de valor, pela

---

quantidade de outra commodity. Duas commodities (a) e (b) podem ser representadas em termos de quantidades uma da outra. Isso ocorre porque um indivíduo que possui a commodity (a) deseja vendê-la para adquirir uma determinada porção de commodity (b); enquanto outro indivíduo que tem a (b) deseja comprar a commodity (a). Partindo da equivalência de preços, é possível determinar um valor relativo de uma commodity pela outra. Walras (2003, p. 87) define a seguinte equação de troca:



m v _a = n v _b tag {9.18}



Sendo:

- m: quantidade de commodity (a)
- n: quantidade de commodity (b)
- v_a: valor unitário da commodity (a)
- v_b: valor unitário da commodity (b)

O preço de uma commodity pode ser representado pela razão de troca, ou seja, o preço de (b) pode ser representado em termos da commodity (a) por p_b, e o preço de (a) pode ser representado em termos de (b) por p_a, e os quocientes das quantidades podem ser representados, respectivamente por m/n = q e n/m = 1/q, resultando na relação de preços para as commodities conforme as seguintes equações:



v _a/v _b = p _a = n/m = 1/q tag {9.19}





v _b/v _a = p _b = m/n = q



Sendo:

- q: quociente da relação de troca entre as commodities (a) e (b)
- p_b: preço da commodity (b) representado em termos da commodity (a)

---

p_a: preço da commodity (a) representado em termos da commodity (b)

Partindo-se dessa teoria, chega-se à relação de preços de duas commodities:



p_a = 1/p_b,   p_b = 1/p_a 



Walras (2003, p. 87) sugere que "o preço de qualquer commodity, em termos de outra, é a reciprocidade de preço de uma segunda em termos da primeira". Partindo-se dessa teoria, é possível, portanto, representar os preços de todas as commodities, negociadas em mercados competitivos, em termos de preços relativos de apenas uma commodity, ou seja, é possível representar o preço de todas as commodities em termos do petróleo, por exemplo.

A teoria proposta por Walras (2003, p. 87) descreve uma relação instantânea de preços relativos entre commodities. Essa relação pode modificar-se com o tempo e atingir outros preços relativos com o equilíbrio dos mercados, de acordo com as forças de oferta e demanda por cada uma das commodities.

## 9.4.5 Relação do preço do petróleo com outras commodities

O petróleo, por definição, é um líquido inflamável, encontrado no subsolo em formações rochosas, primordialmente composto por hidrocarbonetos, material orgânico, enxofre, nitrogênio e oxigênio. Utilizado principalmente para produção de óleos combustíveis, gasolina, querosene de aviação, óleo para aquecimento, óleo diesel e Gás Liquefeito de Petróleo (GLP), fontes primárias de energia. Graças à sua alta concentração de energia, fácil transporte e relativa abundância, o petróleo tornou-se a principal fonte de energia desde a década de 1950. Além disso, é também matéria-prima de

---

outros subprodutos não combustíveis, como farmacêuticos, solventes, fertilizantes, pesticidas, plásticos e polímeros em geral.

O consumo de petróleo na data de publicação deste livro gira em torno de 100 milhões de barris por dia e cresce à medida que aumenta a demanda de energia pelas novas economias, como a China e a Índia. O consumo crescente do petróleo provoca uma redução no EROEI (Energy Return Over Energy Invested), ou seja, com a redução das reservas de fácil exploração, torna-se necessário explorar petróleo de difícil acesso ou com menor concentração de hidrocarbonetos, a um maior custo. O EROEI ou EROI é o ganho líquido de energia, é o quociente de toda a energia obtida, divido pela energia gasta na exploração e transporte do petróleo, conforme a seguinte equação:



k_e = E_o/E_s 



Sendo:

- k_e: ganho líquido de energia
- E_o: total de energia obtida
- E_s: energia despendida no processo de exploração

À medida que o ganho líquido de energia na exploração de petróleo diminui, algumas fontes alternativas de energia tornam-se viáveis economicamente. Portanto, a partir do momento que o EROI dos combustíveis alternativos fica maior do que o do petróleo, estes tornam-se fontes viáveis de energia substituta aos combustíveis fósseis.

Entre a lista das principais fontes alternativas de energia estão os biocombustíveis, que podem ser definidos como combustíveis sólidos, líquidos ou gasosos produzidos a partir de material biológico, fontes de carbono, em sua maioria de origem vegetal. Os biocombustíveis surgem como alternativa renovável, pois, por meio da fotossíntese, as plantas podem converter energia solar em material orgânico.

---

A vantagem ambiental dos biocombustíveis é que, além de serem uma fonte de energia renovável, permitem a captação de carbono da atmosfera. A desvantagem, apresentada pelos ambientalistas, é que a cultura de vegetais com destino à produção de biocombustível pode ampliar as áreas plantadas e promover o desmatamento de florestas tropicais. O intuito deste livro não é discutir os impactos ambientais da produção dos biocombustíveis, apesar de ser um tópico de extrema relevância, apenas a formação de preços destes.

Grande parte das commodities de origem vegetal podem ser destinadas à produção de biocombustível, como milho, soja, canola, mamona, beterraba e cana-de-açúcar. Todos esses vegetais possuem a capacidade de serem convertidos em biocombustíveis, porém, de acordo com a União da Indústria de Cana-de-açúcar (ÚNICA), a cana-de-açúcar é a mais eficiente na produção de energia, pois produz maior ganho líquido de energia do que os outros vegetais.

## 9.5 Condição de não arbitragem do preço futuro

Os preços no mercado futuro de commodities devem estar em condição de não arbitragem em relação aos preços no mercado à vista. Sugerir que os preços estão em condição de não arbitragem significa afirmar que nenhum participante do mercado consegue obter lucros anormais sem assumir riscos, simplesmente aproveitando diferenças de preços entre os mercados à vista e futuro. Significa dizer também que, em condição de não arbitragem, a diferença entre o preço futuro e o preço à vista da commodity será apenas a diferença entre a taxa livre de risco e o retorno de conveniência no período.

Se o retorno de conveniência é maior, em termos nominais, do que a taxa livre de risco, o preço futuro ficará abaixo do preço à vista, resultando no fenômeno de backwardation, caso contrário, se a taxa do retorno de

---

conveniência for menor do que a livre de risco, haverá a presença de contango.

Partindo-se da premissa de que o preço da commodity no mercado futuro é igual ao preço à vista acrescido da taxa de juros livre de risco menos o retorno de conveniência, a seguinte equação pode ser adotada, assumindo-se taxas de juros em forma contínua:



F _t = S _t e^((r - delta_t) (T - t)) tag {9.22}



Sendo:

- S_t: preço do ativo à vista no tempo t
- F_t: preço do contrato futuro no tempo t, com vencimento em T, posterior a t
- r: taxa de juros do ativo livre de risco
- delta_t: taxa de retorno de conveniência no tempo t

Após a aplicação do logaritmo dos dois lados de equação, o resultado fica da seguinte maneira:



ln (F _t) = ln (S _t) + (r - delta_t) (T - t) tag {9.23}



E, finalmente, a equação que determina a relação de preços, fica nesta forma:



ln (F _t) = r (T - t) + ln (S _t) - delta_t (T - t) tag {9.24}



---

# 9.6 Reversão à média do retorno de conveniência

O retorno de conveniência, cuja trajetória é descrita por um processo Ohrnstein-Uhlenbeck de reversão à média, é um conceito econômico não observável, por isso deve receber tratamento de variável de estado, ou seja, variável não observável.

O retorno de conveniência é um valor medido em termos de taxa de juros aplicado sobre o preço do ativo à vista. Tem como base a teoria da estocagem e pode ser entendido como uma vantagem econômica que o detentor da commodity física possui, por ter o benefício de poder esperar o melhor momento para vender sua mercadoria a um preço que maximize sua receita. Em momentos em que os estoques globais da commodity estão baixos, o retorno de conveniência é máximo.

O processo de reversão à média considera que desvios de curto prazo provocados por choques aleatórios não persistentes são corrigidos por um fator de reversão que faz com que a variável convirja para uma média de longo prazo. De forma que, quanto maior for o choque aleatório, mais rápido será o efeito de correção.

Esse processo é coerente para o retorno de conveniência no mercado de commodities. Supondo que ocorra falta momentânea de estoques provocada por um fenômeno aleatório não previsível, o detentor da commodity física será beneficiado pela distorção de curto prazo nos preços, fazendo com que o retorno de conveniência seja máximo nesse momento. Nos momentos seguintes, à medida que os estoques são regulados novamente, o retorno de conveniência é corrigido para seus níveis médios de longo prazo.

O processo de reversão à média em tempo contínuo para o retorno de conveniência pode ser descrito pela seguinte equação:



ddelta_t = φ(mu_δ - delta_t) dt + sigma_δ √(dt) z   , i.i.d. 



---

Sendo:

δ_t: taxa de retorno de conveniência no termo t
φ: velocidade de reversão à média do retorno de conveniência
μ_δ: média de longo prazo do retorno de conveniência
σ_δ: desvio-padrão do retorno de conveniência

A Equação 9.25, quando convertida para variações de tempo discretas, para Δ t = 1, pode ser representada da seguinte maneira:



delta_t - delta_(t-1) = φ(mu_δ - delta_(t-1)) + sigma_δ z   t = 1 



A equação anterior apresenta o processo de reversão à média do retorno de conveniência para uma unidade de tempo. O componente sigma_δz representa o choque aleatório que é corrigido no período subsequente.

Para obter uma equação na forma de espaço de estado, deve-se isolar o delta_t, obtendo-se:



delta_t = φ(mu_δ - delta_(t-1)) + delta_(t-1) + sigma_δ z 



E, finalmente, a equação de reversão à média do retorno de conveniência é apresentada da seguinte forma:



delta_t = φ mu_δ + (1 - φ) delta_(t-1) + sigma_δ z 



A equação anterior será utilizada na especificação de modelos na forma de equações de estado. Na etapa seguinte, o processo estocástico do preço à vista é especificado e, em seguida, são incluídos o componente sazonal e a interdependência linear com o preço do petróleo e a volatilidade.

---

# 9.7 Movimento browniano do preço à vista

A trajetória do preço à vista de uma commodity pode ser descrita por meio de um processo de passeio aleatório em tempo contínuo, ou seja, um movimento browniano. Para isso, é necessário assumir que os retornos do preço à vista da commodity possuam distribuição normal, são independentes e identicamente distribuídos no tempo para qualquer instante de tempo t, R_t^S sim N(mu_s, sigma_s^2).

O movimento descreve a trajetória dos preços à vista da commodity, cujo componente determinístico pode ser composto pela relação linear com variáveis exógenas.

Conforme descrito anteriormente, a seguinte equação representa o movimento browniano adotado para descrever os preços da commodity:



R_t^S = mu_s dt + sigma_s √(dt) z   , i.i.d. 



Sendo:

- B_t^∞: retorno contínuo do preço à vista da commodity no tempo t
- infty_s: média dos retornos do preço à vista
- sigma_s: desvio-padrão dos retornos do preço à vista

Convertida para tempo discreto, para a variação de uma unidade de tempo Δ t = 1, a equação de passeio aleatório para o retorno do preço fica da seguinte maneira:



R_t^S = mu_s + sigma_s z   , Δ t = 1 



---

Substituindo-se o retorno contínuo pela diferença dos logaritmos dos preços, R_t^S = ln (S_t) - ln (S_(t - 1)), obtém-se:



ln (S _t) - ln (S_(t - 1)) = mu_S + sigma_S z tag {9.31}



O que permite, assim, isolar o logaritmo do preço à vista:



ln (S _t) = mu_S + ln (S_(t - 1)) + sigma_S z tag {9.32}



O componente determinístico μ é um parâmetro estimado e pode ser escrito por meio da relação linear com variáveis exógenas observáveis.

# 9.8 Relação do petróleo com o preço da commodity

O processo estocástico que descreve a trajetória dos retornos do preço à vista da commodity possui um componente determinístico mu_S, que define a tendência dos retornos, e um componente aleatório sigma_Sz. O componente determinístico mu_S pode não ser apenas um parâmetro estimado no modelo. Esse argumento parte da premissa de que há outras variáveis que podem antecipar informações sobre a tendência de preços à vista da commodity.

No caso das commodities agrícolas, essa relação com o petróleo pode apresentar certa persistência no tempo. Ou seja, havendo aumento nos preços do petróleo, provocado, por exemplo, por uma queda nos estoques globais. Essa relação pode ser total ou parcialmente restabelecida com o tempo, o que resultaria em consequente aumento nos preços da commodity agrícola.

---

Partindo dessa premissa, tem-se que a tendência mu_S dos retornos dos preços da commodity pode ser descrita por outras variáveis, entre elas, os retornos do preço do petróleo com defasagem de uma unidade de tempo. Inicialmente, tem-se que o retorno do preço à vista da commodity segue um processo de passeio aleatório. Dado que o componente aleatório sigma_S z = varepsilon_t pode ser considerado um ruído branco, é possível descrever o processo do retorno para uma unidade de tempo de acordo com a seguinte equação:



R_t^S = mu_S + varepsilon_t 



Partindo-se da premissa de que o componente determinístico pode ser expresso por meio de uma relação linear com variáveis exógenas observáveis, ou seja, sendo mu_S = β' x_t, tem-se que:



R_t^S = β' x_t + varepsilon_t 



Sendo:

- x_t: matrix n × t de variáveis exógenas observáveis
- boldsymbol{β}: vetor n × 1 de coeficientes lineares

A equação anterior pode ser reescrita da seguinte forma:




R_t^S &= beta_0 + beta_1 x_(1,t) + beta_2 x_(2,t) + ... + beta_n x_(n,t) + varepsilon_t 

R_(t+1)^S &= beta_0 + beta_1 x_(1,t+1) + beta_2 x_(2,t+1) + ... + beta_n x_(n,t+1) + varepsilon_(t+1) 




...

Ao assumir que a média dos retornos da commodity pode ser representada por uma constante mais o retorno defasado do petróleo, obtém-se a seguinte relação linear de retornos:

---



R _t ^S = beta₀ + beta₁ R_(t - 1) ^P + varepsilon_t tag {9.36}



Sendo:

B_t^∞: retorno do preço à vista da commodity no tempo t

R_(t - 1)^P: retorno do petróleo defasado em uma unidade de tempo, em t - 1

β₀, β₁: coeficientes lineares

ε_t: ruído branco

Com base na relação anterior, supõe-se que o retorno do petróleo pode antecipar informação sobre a trajetória do retorno de uma determinada commodity.

# 9.9 Relação da volatilidade do mercado com o preço da commodity

As commodities, por serem ativos reais e possuírem valor econômico na cadeia produtiva, podem ser utilizadas pelos investidores como alternativas seguras para preservação do valor real do capital. As commodities, por definição, são ativos que possuem o mesmo valor em qualquer moeda e podem ser, portanto, referência de valor.

Cenários econômicos turbulentos, provocados por surtos inflacionários, ou crises econômicas, podem provocar uma distorção momentânea no valor relativo das moedas. Nessas situações, os investidores acabam buscando a segurança do mercado de commodities para proteger seu capital. Essa corrida pela preservação do valor do capital provoca alta momentânea nos preços dessas mercadorias, que não está diretamente relacionada à demanda

---

física para utilização na cadeia produtiva. Essa demanda é provocada apenas pela migração do capital em busca de ativos reais de conservação de valor dos investimentos financeiros.

Com base nessa teoria, um aumento na volatilidade do mercado, resultante de uma crise econômica ou surto inflacionário, pode provocar alteração na tendência dos preços das commodities, devido ao fluxo de recursos destinados a investimentos dessa natureza. Geman (2005, p. 28) sugere que um aumento na volatilidade provoca um aumento nos preços relativos das commodities, diferentemente do que acontece com o mercado de ações, no qual a volatilidade alta ocorre nos momentos de queda nos preços.

A busca pela segurança das commodities no mercado financeiro não é sustentável economicamente no longo prazo, pois logo após o fim da volatilidade provocada pela crise econômica, os investidores retiram o capital e os preços da commodity tendem a voltar para patamares normais de equilíbrio entre oferta e demanda.

Portanto, o componente determinístico mu_s do retorno do preço da commodity deve sofrer alterações persistentes no tempo provocadas pela volatilidade dos mercados. Essa relação pode ser captada pela adição de mais um coeficiente linear relacionado à volatilidade contemporânea. O retorno do preço à vista da commodity, portanto, pode ser descrito em função da primeira diferença da volatilidade e do retorno do petróleo, adicionado a um ruído branco, conforme a seguinte equação:



R_t^S = beta_0 + beta_1 R_(t-1)^P + beta_2 Δ σ̂_t^M + varepsilon_t 



Sendo:

- Δ σ̂_t^M: primeira diferença da volatilidade condicional do mercado no tempo t
- beta_0, beta_1, beta_2: coeficientes lineares
- varepsilon_t: ruído branco

A volatilidade dos mercados, nessa equação, é o desvio-padrão dos retornos contínuos da carteira que representa todos os ativos do mercado, um índice

---

representativo do mercado de ações.

# 9.10 Sazonalidade

Os preços das commodities agrícolas possuem sazonalidade decorrente dos períodos de safra e entressafra. Os preços de commodities agrícolas seguem padrões cíclicos: em períodos de entressafra, nos quais a oferta é menor, os preços tendem a ser maiores em relação aos períodos de safra, quando a oferta é maior. O efeito de sazonalidade pode ser explicado pela teoria da estocagem.

Como foi mencionado anteriormente neste capítulo, existe uma relação negativa entre o volume de estoques e o preço da commodity. Isso ocorre porque quando o benefício marginal de retenção dos estoques é maior do que o custo marginal de carregamento, é mais vantajoso para o produtor reter estoques para obter melhores preços de venda, levando em consideração os custos de armazenagem da mercadoria. Logo, quando os volumes de estoques estão baixos, no período imediatamente anterior ao da safra, o preço da mercadoria é máximo e o retorno de conveniência também.

Existem diversas formas para modelar o componente sazonal em séries de tempo, a abordagem mais tradicional é por meio de dummies de sazonalidade aditivas, normalmente utilizando-se coeficientes para cada um dos meses do ano, menos um.

Em uma outra abordagem, utilizamos componentes trigonométricos, que permitem identificar ciclos, amplitude e frequência da sazonalidade. Sorensen (2002, p. 414) adicionou um componente sazonal ao modelo de Schwartz e Smith (2000, p. 895).

O componente de sazonalidade implementado foi o seguinte:



lambda_t = Σ(k=1 até K) [ beta_(c,k) cos (2π kθ) + beta_(s,k) sin (2π kθ) ] 



---

Sendo:

θ: tempo, medido em anos
K: frequência dos ciclos sazonais anuais
β_(c,k), β_(s,k): coeficientes estimados cosseno e seno, para cada um dos K ciclo.

A Equação 9.38 permite identificar a amplitude do efeito sazonal nos preços dos períodos de safra das culturas agrícolas. Em alguns casos, a commodity pode ter mais do que um período de safra durante o ano. Nesses casos, quando a série de dados possui mais do que um ciclo, é possível ajustar o modelo aumentando o número de K parâmetros estimados no somatório.

A figura a seguir mostra a representação gráfica dos componentes cíclicos na sazonalidade em um período de 12 meses:

Figura 9.1 | Componentes sazonais seno e cosseno para período de 12 meses
![img-88.jpeg](img-88.jpeg)
Fonte: Elaborada pelos autores.

As commodities agrícolas sofrem oscilações de preço provocadas pelos períodos de safra e entressafra da lavoura. Isso ocorre porque, imediatamente antes dos períodos de safra, os estoques da commodity estão baixos, fazendo com que, de acordo com a teoria da estocagem, os detentores da mercadoria física obtenham melhores preços de venda do que em períodos imediatamente posteriores à safra.

---

O efeito sazonal nos preços das commodities agrícolas não está relacionado com a volatilidade dos mercados ou com o petróleo, portanto, um componente deve ser adicionado exclusivamente para descrever esse efeito cíclico na formação de preços.

Com base nessa teoria, podemos adicionar o componente sazonal determinístico lambda_t à equação que descreve o processo estocástico do preço à vista da commodity:



R_t^S = beta_0 + beta_1 R_(t-1)^P + beta_2 Δ σ̂_t^M + lambda_t + varepsilon_t 



Sendo:

- lambda_t: componente sazonal determinístico no tempo t
- beta_0, beta_1, beta_2: coeficientes lineares
- varepsilon_t: ruído branco

O componente determinístico do preço à vista pode ser descrito pelo retorno defasado do petróleo, pela volatilidade dos mercados e pelo efeito cíclico da sazonalidade, conforme a seguinte equação:



mu_S = beta_0 + beta_1 R_(t-1)^P + beta_2 Δ σ̂_t^M + lambda_t 



De acordo com a equação anterior, tem-se que o logaritmo do preço à vista deve ser dado da seguinte forma:



ln(S_t) = mu_S + ln(S_(t-1)) + sigma_S z 



Sendo assim, a forma final da equação que descreve o processo estocástico do preço à vista de uma commodity é representada pela seguinte equação:

---



ln (S _t) = beta₀ + beta₁ R_(t - 1) ^P + beta₂ Δ hat {σ} _t ^M + lambda_t + ln (S_(t - 1)) + sigma_S z tag {9.42}



Na próxima seção, disporemos as equações na forma de espaço de estado, o que permitirá especificar o modelo em um único sistema de equações.

# 9.11 Modelo com variáveis exógenas para precificação de commodities

O modelo sugerido por Pereira, Ribeiro e Securato (2012, p. 550), na forma de espaço de estado, é composto por equações de estado e equações de sinal, conforme a seguinte estrutura:



{ {l} y _t = A + B x _t + varepsilon_t 
 x _t = C + D x_(t - 1) + v _t   tag {9.43}



Sendo:

x_t: vetor n × 1 de variáveis de estado

y_t: vetor m × 1 de variáveis de sinal

A, C: vetores estimados no processo, incluindo os parâmetros relativos às variáveis exógenas

B, D: matrizes estimadas no processo, referentes aos coeficientes lineares das variáveis de estado

ε_t, v_t: vetores de ruídos brancos serialmente independentes

---

Para especificar o modelo de formação de preços de commodities na forma de espaço de estado é necessário adequar os processos estocásticos das variáveis analisadas em tempo discreto. O modelo deverá seguir a seguinte estrutura:

a. As equações de sinal devem ser especificadas em função do vetor x_t de variáveis de estado em sua forma contemporânea, sem defasagem, cujos parâmetros farão parte da matriz B. Se forem adicionadas variáveis exógenas às equações de sinal, essas variáveis e os parâmetros relacionados a elas, estarão no vetor A. As variáveis exógenas podem ser defasadas, ou não.

b. As equações de estado devem ser especificadas em função do vetor de variáveis de estado com defasagem de uma unidade de tempo x_(t-1), os parâmetros relacionados a esse vetor estão na matriz D. As equações de estado também podem ser escritas em função de variáveis exógenas, defasadas ou não, cujas variáveis e seus parâmetros devem ser alocados no vetor C.

Partindo da estrutura anteriormente descrita, o modelo de formação de preços de commodities na forma de espaço de estado sugerido por Pereira, Ribeiro e Securato (2012), utilizando um sistema com três equações em tempo discreto, definem os processos estocásticos das variáveis, conforme segue:



{ {l}
ln (F _t) = r (T - t) - (T - t) delta_t + ln (S _t) 

delta_t = φ mu_δ + (1 - φ) delta_(t - 1) + sigma_δ z 

ln (S _t) = beta₀ + beta₁ R_(t - 1) ^P + beta₂ Δ hat {σ} _t ^M + lambda_t + ln (S_(t - 1)) + sigma_S z
  tag {9.44}



A primeira equação é de sinal, que define a condição de não arbitragem para o logaritmo do preço futuro da commodity. Essa equação possui a taxa livre de risco r como variável exógena. O logaritmo do preço à vista e o retorno

---

de conveniência são as variáveis de estado na forma contemporânea. Não há componente aleatório.

A segunda é uma equação de estado, que define o processo de reversão à média da taxa do retorno de conveniência, variável de estado. Possui um componente aleatório cuja variância é representada por sigma_δ². Essa equação não possui variáveis exógenas, apenas parâmetros estimados no processo.

A terceira e principal equação do modelo é uma equação de estado, que representa o movimento browniano do logaritmo do preço à vista. Na equação estão presentes as variáveis exógenas que descrevem a tendência do retorno no preço à vista, que são: o retorno defasado do petróleo, a primeira diferença da volatilidade do mercado e o componente sazonal. Essa equação também possui o logaritmo do preço à vista com defasagem e um componente aleatório, que possui variância representada por w_j.

O sistema de equações anterior também pode ser representado na forma matricial, sendo seus componentes dados por:



y_t = [ ln (F_t) ]; x_t = [ {c} delta_t 
 ln (S_t)  ]; x_(t-1) = [ {c} delta_(t-1) 
 ln (S_(t-1))  ];





A = [ r(T - t) ]; B = [ - (T - t) 1 ]; C = [ {c} φ mu_δ 
 beta_0 + beta_1 R_(t-1)^p + beta_2 Δ σ̂_t^M + lambda_t  ] 





D = [ {cc} (1 - φ) & 0 
 0 & 1  ]; varepsilon_t = [0]; v_t = [ {c} sigma_δ z 
 sigma_s z  ]



A forma matricial é utilizada na estimação de parâmetros por meio do filtro de Kalman.

O filtro de Kalman é um dos inúmeros recursos que podem ser utilizados na estimação dos parâmetros de modelos de formação de preços de commodities.

---

A justificativa por essa opção é a possibilidade de inferência de variáveis não observáveis. Dada uma distribuição de probabilidade da variável de estado e um modelo descrevendo o processo estocástico das variáveis observadas, o filtro de Kalman gera distribuições atualizadas, um passo à frente, para as variáveis de estado.

O filtro de Kalman torna-se mais relevante quando a variável que se quer modelar, ou não é diretamente observável, ou sua observação direta é distorcida por variáveis exógenas não controláveis. Este é o caso do preço à vista de commodities. Os preços negociados no mercado à vista de uma commodity são variáveis que, apesar de serem facilmente observadas nos negócios realizados entre os produtores e a indústria compradora, podem ter problemas de observação ou distorções.

## Exemplo 9.1 Aplicação do modelo para o mercado futuro de açúcar

Para aplicação do modelo completo para o mercado de açúcar, utilizamos séries de dados históricas do mercado futuro de açúcar na B3. O quadro a seguir mostra a origem dos dados coletados:

Quadro 9.3 | Origem e periodicidade das séries de dados coletadas

|  Sigla | Dados coletados | Origem | Periodicidade da série  |
| --- | --- | --- | --- |
|  Acucarbr | Preço à vista do açúcar | Site do CEPEA | Diária  |
|  Etanol | Preço à vista do álcool anidro – etanol | Site do CEPEA | Semanal  |
|  Fut | Preço do contrato futuro de açúcar cristal (cód. ISU) | Sistema de recuperação de informações da B3 | Diária  |
|  Petr | Preço futuro de petróleo WTI (cód. CL1 Comdty) | Bloomberg | Diária  |
|  R | Taxa dos fed funds (Federal funds effective rate) | Site do Federal Reserve | Diária  |

---

Fonte: Elaborado pelos autores.

A seguir são apresentados os resultados dos parâmetros do modelo completo, estimados por meio do filtro de Kalman. O filtro de Kalman é um processo de estimação de variáveis de estado não observáveis em um sistema dinâmico linear, perturbado por um ruído branco com distribuição normal. O estimador resultante do processo é ótimo, em termos de erro quadrático de estimação.

O preço do açúcar à vista foi tratado como variável não observável, portanto, as cotações de preços do açúcar divulgadas pelo Cepea foram omitidas no processo de filtragem. Foram utilizadas as cotações do açúcar no mercado futuro divulgadas pela B3.

O processo foi executado para obter os parâmetros estimados do modelo proposto e do modelo de dois fatores de Gibson e Schwartz (1990, p. 960), para que os resultados fossem comparados.

A Tabela 9.1 apresenta os resultados dos parâmetros estimados dos dois modelos para dados diários e mensais por meio do filtro de Kalman. A tabela é dividida em duas partes: nas colunas da esquerda estão os parâmetros estimados com os dados diários e à direita estão os estimadores com dados mensais. Paralelamente, pode-se comparar os estimadores para o modelo completo e o de dois fatores, isso é possível porque o modelo de dois fatores também possui parâmetros de movimento browniano para o preço à vista e reversão à média para o retorno de conveniência.

Tabela 9.1 | Resultados do modelo completo e modelo de dois fatores

|   | Dados diários |   | Dados mensais  |   |
| --- | --- | --- | --- | --- |
|  Parâmetro | Modelo completo | Dois fatores | Modelo completo | Dois fatores  |
|  ∅ | 0,008398 | 0,008339 | 1,112879 | 0,124878  |
|  μ_δ | 0,116495 | 0,111897 | 0,143086 | 0,083884  |
|  exp(σ_δ) | -6,556159 | -6,588269 | -39,29111 | -39,29111  |

---

|   | Dados diários |   | Dados mensais  |   |
| --- | --- | --- | --- | --- |
|  Parâmetro | Modelo completo | Dois fatores | Modelo completo | Dois fatores  |
|  β₀ | 0,000311 | 0,000254 | 0,011527 | 0,006749  |
|  β₁ | 0,022868 | - | 0,049383 | -  |
|  β₂ | 1,069168 | - | 1,187362 | -  |
|  βc,1 | 0,001367 | - | 0,002386 | -  |
|  βs,1 | -0,001836 | - | -0,035554 | -  |
|  exp(σs) | -8,686838 | -8,661802 | -4,934495 | -4,793600  |
|  Log likelihood | 4555,53 | 4548,11 | 64,31 | 60,32  |

Fonte: Elaborada pelos autores.

Com base nos resultados apresentados no quadro anterior, há uma relação positiva entre o retorno defasado do petróleo e o logaritmo do preço à vista do açúcar, tanto para dados diários quanto para dados mensais, pois o coeficiente do petróleo β₁ é positivo. O estimador do coeficiente β₂ da volatilidade também é positivo. Esse resultado deve-se ao fato de que quando há aumento da volatilidade, os preços do açúcar também aumentam.

Em termos de verossimilhança (likelihood), o modelo completo possui maior verossimilhança do que o de dois fatores, tanto para dados diários quanto mensais. Analisando os parâmetros estimados, verificou-se que a taxa média anual de longo prazo do retorno de conveniência μδ é de 11,64% a.a. e 14,31% a.a., para dados diários e mensais, respectivamente, no modelo completo. A taxa média do retorno de conveniência é superior à taxa de juros média anual dos fed funds de 2,81% (taxa contínua). Esse resultado é coerente com a presença significante de backwardation forte na amostra. Observando os resultados com dados mensais, verificou-se que o coeficiente de velocidade de reversão à média σ é substancialmente maior no modelo completo do que no modelo de dois fatores.

RESUMO

---

Neste capítulo, analisamos os principais modelos de precificação de commodities, que consideram o retorno de conveniência, sazonalidade e a relação dos preços com variáveis exógenas, tais como o preço do petróleo.

Os modelos de precificação de commodities também dependem dos preços observados nos contratos futuros, como sendo a forma mais líquida e a melhor formação de preços de referência para esse tipo de ativo.

# EXERCÍCIOS PROPOSTOS

1. Quais as diferenças entre os mercados à vista, termo e futuro de commodities?
2. Explique a teoria da estocagem.
3. Assuma que você é um pequeno produtor de soja, sem muitos recursos e que deseja fixar o preço da saca de soja da próxima safra. Qual derivativo é mais apropriado para a sua situação, termo ou futuro? Justifique.
4. O que é o custo de carregamento no mercado de commodities?
5. Descreva a operação de cash and carry. Em qual circunstância ela deve ser realizada?
6. Descreva a operação de reverse cash and carry. Em qual circunstância ela deve ser realizada?
7. Descreva o retorno de conveniência.
8. Defina backwardation e contango.
9. Quais as condições para que ocorra backwardation no mercado de commodities?

---

10. Como o efeito da sazonalidade pode ser explicado pela teoria da estocagem?

11. Discorra sobre os principais modelos de preços de commodities.

---

CAPITULO 10

XVA - Ajustes na avaliação de derivativos

---

# 10.1 Introdução

Até a crise financeira de 2007-2008, o risco mais evidente associado a um derivativo era o de mercado, ou seja, as oscilações de preços ou taxas do ativo-objeto daquele derivativo. O risco de crédito, assim como outros tipos de riscos, era, de certa forma, subestimado.

Para demonstrar o papel do risco de crédito nos derivativos, e as consequências de negligenciá-lo, vamos utilizar o caso da maior seguradora do mundo, a American International Group (AIG), que teve dificuldades em honrar as contrapartes dos credit default swaps (CDS) que emitiu, contribuindo para o agravamento da crise financeira dos Estados Unidos e que se espalhou pelo mundo.

O CDS é um derivativo no qual o ativo-objeto pode ser a solvência de um país, de uma empresa ou até mesmo de fluxos de pagamentos, de uma cesta de ativos securitizados.

Quando utilizados adequadamente, os CDS funcionam como um seguro do risco de crédito. O credor da dívida, ao fazer o seguro de crédito via CDS, paga um prêmio ao emissor do CDS. Se o devedor da dívida não honrar a obrigação de um empréstimo ou de uma cesta de hipotecas, por exemplo, o emissor do CDS assume o papel do devedor, garantindo o pagamento ao credor da dívida.

Uma das práticas que fomentaram a crise financeira de 2007-2008 foi a venda, ou emissão, de CDS para contrapartes que não eram detentoras da dívida do ativo-objeto daquele CDS. Seria como se você fizesse um seguro de crédito da hipoteca da casa do seu vizinho. Como você não é o banco que concedeu a hipoteca ao seu vizinho, você não está fazendo um hedge, mas especulando com a capacidade de seu vizinho honrar os pagamentos da hipoteca. Para agravar a situação, qualquer pessoa poderia fazer um seguro de crédito da hipoteca da casa do seu vizinho. Suponha que 80 pessoas fizessem o seguro daquela mesma hipoteca. A seguradora, em um primeiro momento, receberia um bom montante em prêmios – gerando um lucro no curto prazo e recompensando seus diretores na forma de bônus. Essa prática incentivava os diretores da seguradora a emitir mais e mais seguros,

---

alavancando cada vez mais a seguradora. Se o seu vizinho deixasse de pagar a hipoteca, os diretores que decidiram pela emissão dos seguros não devolveriam os bônus recebidos. Na pior das hipóteses, a seguradora quebraria e os acionistas arcariam com o prejuízo. Caso o governo resolvesse salvar a seguradora honrando os seus compromissos, os contribuintes é que acabariam arcando com o prejuízo.

Voltando ao caso da AIG, de acordo com o relatório do Federal Reserve Bank of Chicago – AIG in Hindsight, a seguradora tinha uma exposição de US$ 500 bilhões em CDS no mercado de balcão em 2007. Parte dessa exposição era composta de produtos securitizados que continham hipotecas. Quando a bolha imobiliária estourou nos Estados Unidos, as perdas acumuladas da AIG em setembro de 2008 chegavam a US$ 50 bilhões, contribuindo para a quase falência dessa empresa, que só não ocorreu devido à ajuda do governo americano.

O que deu errado? Podemos elencar algumas causas:

- Os mercados de derivativos de balcão não eram suficientemente regulados nos Estados Unidos;
- Empresas como a AIG e instituições financeiras não precisavam alocar capital em função dos CDS e de outros derivativos de balcão.
- As posições das contrapartes da AIG nesses CDS tinham valor de mercado positivo, porém não era requerido o capital dessas contrapartes fosse suficientemente alocado para cobrir possíveis perdas em função da AIG não honrar as liquidações desses derivativos. Ou seja, o risco de crédito de contraparte dos CDS não requeria alocação de capital, assim como não estava sensibilizado no resultado das instituições financeiras dado que a contraparte era a AIG.
- Incentivos perversos aos diretores das empresas, tanto da AIG quanto de suas contrapartes nesses CDS. Do ponto de vista dos diretores da AIG, os prêmios recebidos em função das emissões dos CDS eram, de certa forma, traduzidos em bônus. Quanto mais emissões de CDS, maior a receita, pelo menos no curto

---

prazo, e maiores os bônus para seus diretores. Do ponto de vista das entidades financeiras que eram detentoras dos CDS, o resultado positivo não realizado – ou seja, enquanto as operações não fossem liquidadas – também era convertido em robustos bônus aos funcionários das mesas de operações desses produtos.

Tendo o caso da AIG como exemplo e generalizando sob o contexto da crise de 2007-2008, podemos elencar importantes lições, dentre as quais gostaríamos de destacar duas em relação ao risco de crédito de contraparte de um derivativo de balcão:

1. Este risco deveria estar refletido no balanço, especificamente no resultado das entidades financeiras que tinham essas operações em seus livros. A deterioração da qualidade creditícia da contraparte deveria afetar negativamente o resultado daquela operação – análogo à provisão para devedores duvidosos em um empréstimo. O racional aqui é que, mesmo com ganhos positivos expressivos em função da marcação a mercado de um derivativo de balcão, caso houvesse a deterioração da qualidade creditícia da contraparte, o resultado deveria ser penalizado. Isso acabaria inibindo que outras operações similares fossem feitas – evitando que o resultado da entidade fosse artificialmente "inflado". Consequentemente, os traders das mesas de operações desses derivativos tenderiam a agir com mais parcimônia.

2. O capital deveria ser alocado com o objetivo de oferecer um “colchão” caso a contraparte do derivativo de balcão não honrasse a liquidação, da mesma forma que há alocação de capital em função do risco de default de um empréstimo. O racional aqui é que, caso a contraparte do derivativo não honrasse a liquidação, a entidade financeira teria solidez suficiente para suportar o calote.

Como veremos neste capítulo, a **qualidade creditícia da contraparte** passará a compor a precificação e o risco de um derivativo de balcão. A resposta regulatória à crise de 2007-2008 também exigirá que outros componentes sejam incorporados na precificação e no risco dos derivativos de balcão: o custo de **funding** e o impacto no capital da instituição financeira para a manutenção da posição em derivativos. Esses componentes são denominados XVAs. O "X" representa, de forma genérica, esses

---

componentes. Já o "VA" refere-se a valuation adjustment, ou seja, ajustes necessários na precificação e no valor dos derivativos de balcão.

# 10.2 Premissas pré-crise de 2007-2008

Sabemos que muitas das premissas aceitas na precificação de derivativos não são verdadeiras. Os modelos, como o de Black e Scholes, reduzem a realidade a um mundo imaginário, extremamente simplificado. Façamos uma analogia com o ensino de Física no ensino médio. Os modelos ensinados funcionavam muito bem com premissas irrealistas, em que é possível, por exemplo, eliminar o atrito e até realizar testes no vácuo. Essa simplificação da realidade é necessária para obter modelos inteligíveis, que capturam a essência da realidade modelada. Esses modelos simplificados funcionam bem quando as condições encontradas na natureza, ou no mundo real, são parecidas com as de laboratório, ou com as premissas idealizadas — o que normalmente não acontece. Na prática, os modelos simplificados são pontos de partida para criação de modelos mais completos, mais aderentes ao mundo real.

A realidade imposta pela crise de 2007-2008 estressou algumas das assunções adotadas na precificação de derivativos, sobretudo dos derivativos de balcão. Até então, algumas premissas eram toleradas de tal forma que até se criava uma ilusão de serem verdadeiras:

- Existência de uma taxa livre de risco;
- Liquidez infinita de ativos: para cada derivativo, poderíamos negociar em qualquer quantidade aquele derivativo e o respectivo ativo-objeto sempre que quiséssemos;
- Funding irrestrito;
- Mercado sem "fricções": não existem custos de transação;
- Premissa de não arbitragem;
- Normalidade dos retornos dos ativos;

---

- Os riscos podem ser hegeados.

Porém, a crise de 2007-2008 tornou evidente que:

- Não existe uma proxy de ativo livre de risco, logo, não existe uma taxa livre de risco. Até mesmo a nota de crédito do governo americano passou de AAA para AA em 2011;
- A taxa Libor deixa de ser vista como uma proxy da taxa livre de risco, como vimos no Capítulo 4;
- Os bancos ficaram receosos ao emprestar recursos entre si, resultando em uma grave crise de liquidez em 2007-2008, aumentando consideravelmente os custos de funding das instituições financeiras;
- Ficou claro que a distribuição dos retornos ficou longe de ser normal em alguns períodos;
- Nem todos os riscos são possíveis de serem hedgeados.

Como no caso da AIG, identificamos a necessidade de considerar, por exemplo, o risco de crédito da contraparte do derivativo de balcão, assim como outras variáveis, cuja importância não era tão evidente na composição do preço de um derivativo: são os XVAs. Neste capítulo, apresentaremos os mais relevantes.

# 10.3 Credit Value Adjustment (CVA)

O CVA considera o risco de crédito da contraparte na precificação e marcação a mercado do derivativo. Aqui, o escopo é fundamentalmente o derivativo de balcão na modalidade sem garantia, já que o risco de crédito da contraparte não é relevante para os derivativos negociados em bolsa ou os registrados em balcão na modalidade com garantia.

---

O BACEN define o CVA como o "ajuste associado à variação do valor dos derivativos em decorrência de variação da qualidade creditícia da contraparte". Pykhtin e Rosen (2010) definem o CVA como "o valor de mercado do risco de crédito da contraparte". Ruiz (2015), na mensuração do CVA, parte da premissa de que este é a diferença entre o valor do derivativo livre de risco e um outro de mesmas características, só que com risco de crédito de contraparte.

# 10.3.1 Risco de crédito de contraparte versus risco de crédito

Podemos nos perguntar por que não tratar o risco de crédito da contraparte no valor de um derivativo da mesma forma que tratamos o risco de crédito tradicional. O motivo é que o tratamento e complexidade são diferentes entre o risco de crédito inerente aos derivativos comparado ao de um empréstimo.

Risco de crédito ou lending risk refere-se à cash credit products, ou seja, não derivativos, como empréstimos e títulos (tipicamente classificados no banking book). Aqui, o risco é o devedor não conseguir honrar o valor devido do empréstimo nos prazos estabelecidos. Nos empréstimos é possível estimar o valor devido nos seus vencimentos, ou seja, a exposição na liquidação. Mesmo nos empréstimos pós-fixados é possível estimar um intervalo de valores dos seus fluxos de caixa com alto grau de confiança. No risco de crédito, somente uma das partes está exposta ao risco, por exemplo, quem comprou um título ou a parte que concedeu o empréstimo.

O risco de crédito de contraparte que se refere aos derivativos de balcão, são classificados no trading book. A exposição do valor devido é muito mais imprevisível do que a de um empréstimo. E, ao contrário do risco de crédito de um empréstimo, ambas as contrapartes podem estar expostas ao risco de default, pois, dependendo do tipo de derivativo, o valor do contrato pode ser

---

positivo ou negativo, ou seja, não se sabe qual será a parte pagadora e, consequentemente, a parte credora na liquidação do contrato.

O risco de crédito da contraparte pode ser visto como a intersecção entre o risco de crédito, em função da qualidade creditícia da contraparte, e o risco de mercado:

Figura 10.1 | Risco de crédito de contraparte
![img-89.jpeg](img-89.jpeg)
Fonte: Adaptada a partir de Franzén e Sjoholm (2014).

A explicação é que, no derivativo de balcão, quanto maior for o valor da marcação a mercado, ou seja, quanto maior o ganho esperado, maior a exposição de crédito que a parte terá em relação à contraparte. Então, o valor da marcação a mercado, ou a estimação do valor da exposição do derivativo, tem um papel muito relevante na mensuração do risco de crédito de contraparte.

# 10.3.2 Wrong way risk

Wrong Way risk é a quando ocorre uma relação inversa entre a qualidade de crédito da contraparte e a exposição àquela contraparte, indicados pelas setas pretas na figura a seguir:

Figura 10.2 | Risco de crédito de contraparte e Wrong Way Risk

---

![img-90.jpeg](img-90.jpeg)
Fonte: Adaptada a partir de Franzén e Sjoholm (2014).

Para exemplificar o Wrong Way risk, vamos supor um derivativo de balcão sem garantia entre o Banco A e a Contraparte B. Se durante a vigência do contrato a exposição à Contraparte B aumentar e, simultaneamente, a situação creditícia da Contraparte B deteriorar, teremos um caso de Wrong Way risk. Ou seja, quanto mais o Banco A ganha na posição em função das variáveis financeiras do contrato, maior a perda potencial em função do risco da Contraparte B não ter capacidade de honrar o contrato. Foi o que aconteceu na crise de 2007-2008, por exemplo, com as contrapartes da AIG nos CDS.

# 10.3.3 O CVA Contábil

O CVA no contexto contábil refere-se ao impacto no resultado do derivativo de balcão sem garantia, em função da qualidade creditícia da contraparte. O CVA é um ajuste feito no valor e, consequentemente, no resultado do derivativo. É importante mencionar que a qualidade creditícia da contraparte pode variar no tempo. As normas contábeis (IFRS e US GAAP) requerem que o risco de crédito de contraparte do derivativo esteja refletido no resultado da instituição financeira, sendo atualizado de acordo com as mudanças na qualidade de crédito da contraparte.

De acordo com Ruiz (2015), podemos considerar o CVA como um ajuste que tem como referência um derivativo livre de risco de mesmas

---

características ao de balcão:



V = P_(CreditRiskFree) - CVA \ (10.1)



Sendo V o valor do derivativo e P_(CreditRiskFree) o preço do mesmo derivativo, só que levando em conta uma contraparte livre de risco de crédito.

Para facilitar o racional da Equação 10.1, suponha que você trabalhe na mesa de operações de uma instituição financeira e receba duas cotações de uma mesma operação de derivativo de balcão sem garantia – de mesmas especificações contratuais, parâmetros financeiros e vencimento. Uma das cotações é de uma contraparte que tem baixíssimo risco de crédito, de rating AAA. A outra cotação é de uma empresa classificada como BBB, ou seja, de maior risco de crédito.

Você concorda que, mesmo se tratando do mesmo derivativo, as cotações devem ser diferentes? Assumindo que as cotações refletissem todas as informações disponíveis no mercado e que não houvesse distorções, como você explicaria a diferença de preço da contraparte AAA da BBB? Concorda que o valor cotado pela contraparte de rating AAA deve ser mais alto, ou seja, fechar o contrato com essa contraparte será mais caro do que a contraparte de rating BBB? O motivo é que você provavelmente não deverá se preocupar tanto com a capacidade dessa contraparte em honrar a liquidação no seu vencimento. Do ponto de vista da contraparte com rating BBB, esta deverá cotar um preço mais barato, ou mais atrativo, de forma a compensar a sua qualidade creditícia inferior. Caso contrário, se ambas as cotações fossem iguais, poderíamos instantaneamente descartar a proposta da contraparte de rating BBB.

Podemos dizer que a diferença entre as cotações reflete exatamente o CVA. Alternativamente, o valor do CVA pode ser visto como o custo de fazer o hedge, ou seguro, de crédito da contraparte. Ou seja, o custo do CDS para fazer o seguro do risco da contraparte classificada como BBB. Infelizmente, especialmente no Brasil, não existe um mercado líquido de CDS que permita usar esse instrumento como parâmetro de estimativa do CVA.

---

O CVA coloca desafios à mesa de operações, pois não é fácil de ser quantificado nem hedgeado, não é apurado por transação, mas por carteiras de mesma contraparte. Imaginemos a seguinte situação:

- Uma posição de derivativo de balcão está devidamente hedgeada do ponto de vista dos fatores de risco de mercado;
- Porém, em um determinado dia, apresenta um resultado negativo significativo devido à deterioração da qualidade creditícia da contraparte e aumento do respectivo spread de crédito, ou seja, em função do CVA;
- Como na maioria dos casos não é possível hedgear o risco de crédito de contraparte, o CVA pode aumentar a volatilidade do resultado da operação.

Para auxiliar no gerenciamento do CVA, surgem as mesas de CVA, ou o CVA desk. A mesa de CVA cobrará um prêmio pelo seguro da trading desk (dealing desk) no início da operação, que deverá será repassado à contraparte, ou seja, embutido no preço ou spread do contrato. O objetivo do CVA desk é gerenciar o risco de crédito de contraparte e a volatilidade do CVA nos resultados da instituição.

# 10.4 DVA: o outro lado do CVA

Da mesma maneira que quantificamos o valor de mercado da contraparte, a contraparte o fará em relação à instituição na qual trabalhamos. O Debt Value Adjustment (DVA) é o valor a mercado do risco de crédito de contraparte da nossa própria instituição. Assumindo que essa informação fosse transparente ao mercado, o DVA representaria o custo do seguro de default da nossa própria instituição, impactando o custo de funding: o DVA sinalizaria ao mercado a situação creditícia da nossa instituição.

---

Como o objetivo deste capítulo é apresentar as variáveis adicionais que afetam a precificação e o risco das operações de derivativos de balcão sob a ótica da instituição financeira que trabalhamos, não dedicaremos mais detalhes ao DVA, visto que o DVA é basicamente o CVA que a contraparte do derivativo de balcão mensurará em função da qualidade creditícia da nossa instituição.

# 10.5 Funding Value Adjustment (FVA)

Antes da crise que se iniciou em 2007, havia grande confiança entre os bancos de honrarem suas obrigações. Durante 2007, conforme a crise se agravava, a desconfiança entre os bancos aumentava. A consequência foi que os custos de funding dos bancos aumentaram substancialmente, bem acima da taxa livre de risco. Por exemplo, o aumento do Libor-OIS spread, como vimos no Capítulo 4.

Da mesma maneira que calculamos o CVA para os derivativos de balcão, podemos calcular o impacto do custo de funding para a manutenção desses contratos de derivativos. Um tipo de FVA pode ser resultante do custo de obter garantias, ou collateral, para a manutenção do contrato derivativo. A porção do FVA que resulta das assimetrias de chamadas de margem entre a posição de derivativo e seu respectivo hedge é denominada Collateral Value Adjustment ou CollVA.

Podemos explicar o CollVA pelo exemplo da figura a seguir:

Figura 10.3 | Exemplo de operação de derivativo impactada pelo CollVA

---

![img-91.jpeg](img-91.jpeg)
Fonte: Adaptada a partir de Ruiz (2015).

Vamos nos imaginar trabalhando no Banco A, que no contexto retratado na Figura 10. 3 faz o papel do derivatives dealer:

- No fluxo 1, a empresa exportadora procura o Banco A para fazer um NDF de dólar para proteger a receita de uma exportação com liquidação futura. Ou seja, a empresa exportadora tem um recebível em dólar e contratará uma posição vendida a termo de dólar com o Banco A. Consequentemente, o Banco A ficará em posição comprada em dólar a termo com a empresa exportadora.
- No fluxo 2, ao fechar o NDF com a empresa, o Banco A faz um hedge na B3, utilizando o contrato de dólar futuro, ou seja, o Banco A vende dólar futuro na bolsa.

Vamos analisar a situação até aqui. Você, leitor, consegue identificar quais os possíveis problemas que o Banco A poderá enfrentar ao estruturar as operações descritas? A liquidação do NDF ocorrerá somente no vencimento definido no contrato. Porém, ao fazer o hedge do NDF na B3, o Banco A passa a ter de depositar garantias e honrar os ajustes diários solicitados pela bolsa. Vamos supor que os ativos depositados em margem são títulos públicos, e que possuam uma rentabilidade inferior ao custo de funding do Banco A.

O pior cenário em termos de liquidez para o Banco A é de alta do dólar frente ao real. Por estar vendido em dólar na B3, o Banco A teria custos de funding para arcar com as demandas da bolsa, representados pelo fluxo 3,

---

no qual o Banco B fornece o funding necessário para o Banco A adquirir os ativos a serem depositados em bolsa. Contabilmente, o Banco A estaria com um resultado positivo, pois estaria ganhando no NDF – assumindo um spread embutido, teoricamente travando o resultado da operação. Porém, você concorda que esses custos adicionais de funding para conseguir honrar as chamadas de margem e ajustes da B3 podem comprometer o resultado do Banco A? Aqui, para facilitar o entendimento do papel do custo de funding nesse exemplo, vamos imaginar o Banco A buscando funding no mercado para comprar ativos para depositar em bolsa como garantias – ou o banco tendo de alocar recursos em ativo depositáveis com garantias em bolsa em detrimento de alocá-los em operações mais rentáveis ao banco.

Em um caso extremo, dependendo da magnitude do valor das garantias exigidas pela bolsa, o custo de funding poderia até ser maior que o ganho oriundo do spread da operação.

O racional do FVA em função do colateral na precificação do derivativo de balcão – no nosso exemplo, o NDF – é embutir no preço do derivativo de balcão os custos de funding associados ao atendimento das demandas de garantias exigidas para a manutenção da operação de balcão. Ao cotar o NDF com a empresa exportadora, o Banco A deveria considerar esse custo potencial.

Então, para adequadamente precificar um derivativo de balcão, um novo componente dever ser considerado, o CollVA:



V = P_(CreditRiskFree) - CVA - CollVA × (10.2)



O FVA tem outro componente que deve ser considerado na precificação de derivativos de balcão, o Hedge Value Adjustment (HVA). O HVA tem o mesmo propósito do CollVA, considerar os custos de funding para a manutenção do contrato de derivativo de balcão. A diferença é que, enquanto o CollVA considera os custos de funding associados às garantias, o HVA considera o custo de funding para a compra do hedge da operação:

Figura 10.4 | Exemplo de operação de derivativo impactada pelo HVA

---

![img-92.jpeg](img-92.jpeg)

Fonte: Adaptada a partir de Ruiz (2015).

Vamos supor que em vez de o Banco A fazer o hedge da venda de dólar do NDF utilizando o contrato futuro de dólar, este o fizesse com uma compra de uma opção de dólar, conforme a Figura 10.4. Você concorda que a compra da opção de dólar acarretaria em uma saída de caixa logo no início da operação, sem nenhuma outra contrapartida de caixa? Portanto, o custo de funding para adquirir esse hedge, a opção de dólar, deveria ser considerado no preço do NDF.

Podemos nos perguntar se os ajustes diários das operações de dólar futuro estariam classificados sob o CollVA ou o HVA? Na nossa opinião, classificaríamos no HVA, pois consideramos que os ajustes diários dizem respeito ao preço do hedge propriamente dito e não às garantias exigidas por esse hedge, aqui entendendo garantias como collateral.

Voltando à precificação do derivativo de balcão considerando o CVA, temos:



V = P_(CreditRiskFree) - CVA - (CollVA + HVA) × 10.3



Sabemos que:



FVA = CollVA + HVA × 10.4



Então, temos que o valor do derivativo será dado pela seguinte equação:

---



V = P_(CreditRiskFree) - CVA - FVA \ (10.5)



Com o que vimos até agora, podemos concluir que a complexidade na precificação de derivativos de balcão aumenta consideravelmente.

Em uma estrutura ideal, a instituição financeira terá uma área para gerenciar os custos e riscos de funding dessas operações de derivativos, a mesa de FVA. A mesa de FVA será responsável por quantificar e cobrar um prêmio pelo seguro do funding do trading desk no início da operação. Um dos objetivos da mesa de FVA é gerenciar o risco de funding. Assim como a mesa de CVA, a mesa de FVA pode optar por não fazer o seguro, dado as restrições de mercado (o produto para fazer o hedge não existe ou tem um custo proibitivo), ou seja, esse seguro simplesmente não existe.

A mensuração do FVA é muito complexa, gerando debates entre o universo acadêmico (HULL; WHITE, 2012) e o pessoal de mercado, alguns argumentam que esse ajuste não deve ser considerado, outros argumentam que sim, mas discordam de como o quantificar. Nosso objetivo neste capítulo é explicar o seu racional, justificando o FVA como uma variável a ser incorporada na precificação do derivativo de balcão.

# 10.6 Capital Value Adjustment (KVA)

Antes de entrarmos na definição do KVA, vamos entender o papel do capital no contexto de risco. O capital próprio do banco pode ser visto como a "musculatura" que o banco tem para enfrentar crises financeiras. É importante salientar que a estabilidade e robustez financeira são fundamentais para o setor bancário e para a economia.

Existem várias definições de capital. Para fins de gestão de risco, tanto gerencial quanto regulatório, podemos simplificadamente definir o capital como o montante de ativos líquidos que o banco tem em seu balanço. Esses

---

ativos líquidos representam um “colchão” que ajuda o banco a absorver impactos nas crises financeiras e eventos adversos não esperados.

A diferença entre os valores das perdas não esperadas e as esperadas na visão da entidade financeira é chamada de capital econômico, como podemos ver no exemplo da figura a seguir:

Figura 10.5 | Capital econômico
![img-93.jpeg](img-93.jpeg)
Fonte: Adaptada a partir de Ruiz (2015).

No contexto do risco de crédito, a perda esperada é calculada em função da probabilidade de default (o não pagamento de todo o valor devido) das contrapartes, da exposição e das taxas de recuperação (recovery rates):



EL = PD × EAD × (1 - RR) 



Onde:

- EL: perda esperada, “expected loss”
- PD: probabilidade de default;
- RR: taxa de recuperação do crédito.

A perda esperada deve estar sensibilizada no resultado da instituição.

Já a perda não esperada é uma medida do tipo Value at risk (VaR), no qual se estima a pior perda com base no nível de confiança definido, não afetando

---

diretamente o resultado, seja gerencial ou contábil, da instituição financeira. O seu propósito é auxiliar na mensuração da “musculatura” que a instituição deve ter para suportar perdas extremas. Por exemplo, poderia ser algo como “a pior perda estimada para o nível de confiança de 95% é R$ 90 milhões”. É uma medida gerencial, definida pela instituição.

Outra medida que vem a reboque do capital econômico e importante métrica na decisão dos negócios da instituição financeira é o Retorno Ajustado ao Risco no Capital (RAROC), que mede uma relação entre risco e retorno, por exemplo, de uma operação, carteira ou da ponderação dos ativos da instituição:



RAROC = Lucro esperado/Capital econômico   (10.7)



Um dos principais objetivos de uma instituição financeira é maximizar o valor para o acionista. Para isso, é preciso promover as linhas de negócios mais lucrativas, considerando o consumo dos recursos e de capital da instituição.

É necessário compreender que o capital do banco é limitado e que cada negócio que a instituição faz consome parte do capital, seja o regulatório ou o gerencial. No contexto regulatório, a instituição é obrigada pelos órgãos reguladores a alocar parte do capital para cobrir potenciais perdas de uma operação. No Brasil, o BACEN define a metodologia de cálculo do capital mínimo, ou o patrimônio exigido para os bancos. A magnitude de quanto capital o banco deverá alocar, depende dos riscos das operações em seu balanço.

Então, é preciso gerenciar esse custo de capital e considerá-lo na precificação de derivativos. O capital da instituição é um recurso escasso e disputado por várias linhas de negócios. Portanto, faz sentido cobrar, ou embutir no preço das operações, o custo de oportunidade em alocar o capital naquela operação em detrimento de outras. Esse custo é o KVA. Logo, segundo Ruiz (2015), é necessário incluir também este componente na precificação de derivativos:

---



V = P_(CreditRiskFree) - CVA - FVA - KVA \ (10.8)



- Logo, ao cotar um derivativo a um cliente, deveremos considerar também as seguintes variáveis:
- Custo de proteção de crédito da contraparte;
- Quanto precisaremos tomar emprestado para cumprir as obrigações estimadas de saídas de caixa que esse contrato imporá à instituição, assim como as margens, garantias e ajustes diários e o custo de funding;
- Impacto no consumo de capital do banco;
- E, claro, o spread de ganho da operação.

# 10.7 Considerações finais

Podemos concluir que, na prática, a precificação e o gerenciamento de risco de operações que envolvam derivativos, principalmente os de balcão, são tarefas altamente complexas. O pacote de normas imposto pelos órgãos reguladores em função das diretrizes definidas pelo Comitê de Basileia impõe aos bancos novos controles e estruturas para atendê-lo.

## RESUMO

Os xVA são ajustes na avaliação dos derivativos em relação a perdas relativas com risco de crédito da contraparte, custos de funding e uso de capital. Neste capítulo abordamos as diversas variáveis que afetam o valor dos derivativos para os bancos.

## EXERCÍCIOS PROPOSTOS

1. Qual a diferença entre o CollVA e o HVA? Explique o racional de cada um deles

---

na precificação de derivativos.

2. Explique o que é wrong way risk. Dê um exemplo real no qual o wrong way risk foi observado no mercado brasileiro.

3. Qual a diferença entre risco de crédito e risco de contraparte?

4. Assuma que você trabalha na mesa de operações de um banco e que uma empresa (cliente) solicite a cotação de uma operação de NDF para fazer um hedge de uma importação. Liste as variáveis na precificação da NDF que você consideraria ao cotar a operação para o cliente. Elenque os riscos que também devem ser considerados pelo banco em função da operação de NDF com a empresa.

5. O que é capital econômico?

---

CAPITULO 11

# Certificado de Operações Estruturadas (COE)

---

# 11.1 Introdução

Alguns investidores desejam obter retornos de renda variável, mas não estão dispostos a correr risco de retornos negativos. O Certificado de Operações Estruturadas (COE) surgiu no mercado brasileiro para atender esse público que tem menos apetite ao risco, pois permite obter ganhos de renda variável, protegendo o valor do principal investido.

O COE é emitido por um banco e pode ser distribuído por corretoras, que popularizaram essa modalidade de investimento, que usa derivativos para transformar a renda fixa tradicional em um instrumento com ganhos em renda variável.

Neste capítulo, além de apresentar as principais estruturas de COE, abordaremos os seus precursores: os fundos de capital protegido e as structured notes, estas que também possuem uma modalidade com derivativos de crédito, a credit link note.

# 11.2 Características do COE

O Certificado de Operações Estruturadas (COE) é um título único, indivisível e híbrido, composto por um título de renda fixa e por derivativos, que proporcionam ao investidor um rendimento diferente da renda fixa tradicional. O resultado para o investidor pode ser uma renda variável, índices de ações, moedas ou outros fatores de risco preestabelecidos.

O COE, emitido por instituições financeiras para seus clientes, é indicado para investidores que querem obter ganhos em renda variável, mas não estão dispostos a perder o capital investido. Por exemplo, no COE um investidor poderá receber 100% da alta do IBOVESPA nos próximos dois anos, limitado a um IBOVESPA a 140.000 pontos. Porém, se nesse período o IBOVESPA tiver um retorno negativo, o investidor receberá o seu capital inicial investido de volta. É importante mencionar que existe um percentual

---

do capital inicial que é protegido no COE. Em geral, as instituições oferecem 100% de proteção do capital, para que seja atrativo para o investidor, porém esse percentual, em teoria, pode ir de 0% a 100%.

# 11.3 COE para o emissor

O COE é uma modalidade alternativa de captação de recursos para a instituição financeira emissora, assim como as Letras Financeiras ou os CDBs.

O COE permite que o banco emissor obtenha uma captação de longo prazo. A utilização desse instrumento como forma de captação auxilia a instituição emissora em sua gestão de ativos e passivos, conhecida como Asset Liability Management (ALM).

Em geral, os bancos possuem carteiras de ativos pré-fixados de longo prazo, como financiamentos de veículos. Reciprocamente, a emissão de COE permite que, em seu passivo, o banco obtenha uma captação pré-fixada de longo prazo.

Vamos considerar o seguinte exemplo: um determinado banco possui em seu ativo recebíveis referentes a financiamento de veículos em parcelas fixas mensais, a taxa pré-fixada. Geralmente esses financiamentos são relativamente longos.

Caso esse banco opte por captar recursos utilizando CDBs pós-fixados de liquidez diária, haveria risco de descasamento de prazos entre ativos e passivos, pois o banco terá um ativo pré-fixado de longo prazo e um passivo pós-fixado de curto prazo.

Em modalidades de captação como o COE, o banco obterá um passivo pré-fixado mais adequado ao prazo médio do ativo.

# 11.3.1 COE como alternativa de lucros

---

Além de ser uma modalidade eficiente de captação, o COE ainda pode permitir um ganho para a instituição financeira com os derivativos que o compõem.

No momento da emissão, em sua área Comercial, o gerente de relacionamento apresenta a estrutura e potenciais ganhos do COE para o investidor, cliente do banco. Essa estrutura, na verdade, é composta por um título de renda fixa e derivativos.

Esses derivativos, além de proporcionar uma proposta de investimento diferenciada para o cliente, podem também se tornar uma estratégia lucrativa para a instituição emissora, desde que esses derivativos sejam devidamente precificados no momento da emissão e gerenciados em um livro específico para derivativos de COE.

Para proporcionar lucros, os derivativos devem ser delta hedgeados, ou seja, o emissor terá um livro de posição em volatilidade que será composto pelas opções integradas nos COEs.

## 11.3.2 Responsabilidades do emissor do COE

Na comercialização do COE, a instituição precisa verificar a adequação desse título com o perfil do investidor, seus objetivos, compreensão do instrumento, ou seja, seguindo boas práticas de suitability, das quais, deverá:

- Verificar a situação econômica do investidor e sua possibilidade de investir em um ativo ilíquido de longo prazo;
- Informar ao investidor que o COE possui risco de crédito da instituição emissora e risco de mercado dos derivativos;
- Verificar se o nível de complexidade do COE é adequado a experiência do investidor e compreensão dos fatores risco do instrumento;

---

- Obter uma declaração do investidor, na qual ele atesta que está ciente dos riscos envolvidos, principalmente se o percentual de proteção do capital investido for inferior a 100%;
- O procedimento de suitability do COE dever ser um processo claro e documentado, para uma eventual auditoria.

A instituição que participe do processo de distribuição do COE deve fornecer informações ao investidor, seja por meio eletrônico ou documento físico, em linguagem clara, objetiva e adequada a complexidade desse instrumento.

O distribuidor de COE pode ser uma outra instituição que não o emissor, mesmo assim deverá esclarecer ao investidor sobre o funcionamento do instrumento, o prazo de pagamento e os riscos incorridos, sejam estes de crédito da instituição emissora ou dos fatores de risco do ativo subjacente, em decorrência da posição com derivativos.

# 11.4 Características do COE na emissão

O COE pode ser registrado na Cetip, agora parte da B3 após a fusão, com as seguintes características, conforme Res. n. 4.263/2013 do BACEN:

- Deve-se identificar a instituição financeira emissora, que pode ser um banco, a Caixa Econômica, ou o Banco Nacional do Desenvolvimento (BNDES);
- Indicar também o titular do COE, ou seja, o cliente do banco. O título é emitido individualmente para cada investidor, não é um condomínio, como um fundo, por exemplo;
- Data de emissão e de vencimento do COE;
- Valor nominal total, do qual se deve especificar a parcela de capital protegido e do capital em risco (não protegido);
- O ativo subjacente (ativo-objeto) utilizado como referência;

---

- Condições de remuneração do certificado, como barreiras, limites, percentuais de ganho e outras condições para o titular;
- Deve-se especificar a possibilidade de entrega física do ativo subjacente. Por exemplo, entrega de ações ou títulos de renda fixa no vencimento;
- Deve-se especificar as condições de recompra ou resgate antecipado. É possível solicitar o resgate antecipado do COE com um deságio sobre o capital investido.

# 11.5 Os ativos subjacentes do COE

O COE pode utilizar como referência a variação de preços de uma diversidade de ativos subjacentes. As condições necessárias para que um ativo seja elegível para ser objeto de um COE é que seus preços sejam regularmente divulgados por uma instituição de referência – como é o caso do dólar oficial divulgado pelo BACEN – ou, caso seja negociado em mercado secundário, possuam liquidez necessária que permita a precificação diária dos COEs emitidos.

Além disso, mensalmente, o emissor precisa informar ao BACEN o valor de sua carteira de COE marcada a mercado, logo, deverá haver preços de referência regulares para o COE.

Os ativos aceitos como referência para os COEs emitidos são os seguintes:

- Índices de preços, como o IPCA-IBGE ou IGPM-FGV;
- Índices de títulos, como o IMA, IMA-B, IRF-M, da Anbima;
- Índices de Valores Mobiliários, como o IBOVESPA e os diversos índices divulgados pela B3, como IBrX100, IDIV, IGC e outros;
- Taxas de juros, como o DI ou a taxa Selic, ou percentuais dessas taxas, ou ainda adicionadas de taxa pré-fixada;

---

- Taxas de câmbio em diversas moedas cuja cotação seja divulgada pelo BACEN;
- Cotações de ações líquidas negociadas em bolsa brasileira, ou cesta de ações;
- Cotações de ações líquidas negociadas em bolsa no exterior, ou cesta de ações;
- Preço de commodities, cujo preço seja regularmente divulgado, podendo ser cotado em dólares ou reais.

As regras para utilizar ativos subjacentes como referência para o COE no exterior são basicamente as mesmas utilizadas para o Brasil, ou seja, tem de ser um ativo líquido, divulgado por bolsa ou entidade plenamente reconhecida.

A seleção do ativo subjacente e verificação se este se enquadra nos requisitos mínimos exigidos pelo BACEN é de responsabilidade do emissor do COE.

Não é permitida a emissão de COE no Brasil referenciado em operações de crédito, títulos de crédito, instrumentos de securitização e derivativos de crédito, como o Credit Default Swap (CDS).

# 11.5.1 Fundos de capital protegido

Os fundos de capital protegido anteriormente eram denominados como fundos de capital garantido. Para evitar interpretação equivocada da denominação antiga por parte dos investidores, essa modalidade de investimento passou a ser denominada como fundo de investimento de capital protegido.

O fundo de capital protegido é um fundo multimercado, que tem o intuito de simular uma nota estruturada e foi amplamente utilizado antes da autorização do BACEN para emissão de COE.

O fundo de capital protegido é estruturado da seguinte maneira:

---

1. Primeiro, uma proposta do fundo é divulgada aos clientes em potencial pelo distribuidor, suas características e riscos incorridos, como o prazo de duração, ativo subjacente e estrutura com derivativos.
2. Posteriormente, o fundo é aberto para captação durante um curto intervalo de tempo, até que se atinja o montante prospectado pelo distribuidor.
3. Após a captação, o fundo é fechado para resgates.
4. Durante o período operacional do fundo, que pode ser dois anos, por exemplo, são feitas operações similares a uma nota estruturada. Nesse período, os cotistas não devem resgatar, pois a execução da operação a contento depende que todo o período até o encerramento do fundo seja cumprido.
5. Após decorrido o período operacional do fundo, este se encerra e ocorre o pagamento do resgate simultâneo aos cotistas.

No início do período operacional do fundo, o gestor adquire títulos de renda fixa com quase a totalidade dos recursos financeiros do fundo. O objetivo do gestor ao comprar um título de renda fixa no início é o de recompor o capital investido ao longo do período operacional. Com o caixa remanescente, o gestor compra as opções necessárias para a montagem da estratégia proposta no momento inicial de constituição do fundo.

É importante que o vencimento das opções seja igual ao vencimento do título de renda fixa, para que haja sincronia entre o resultado da estratégia e o período de vigência do fundo.

O investidor deve permanecer com seu investimento até o encerramento do fundo, quando a estratégia atinge sua plenitude. O administrador e o gestor do fundo recebem, em contrapartida pelos serviços prestados, uma taxa de administração cobrada no fundo.

O fundo de investimento de capital protegido é similar a um COE. Na verdade, antes de 2013, a única alternativa disponível para se investir em uma operação parecida com uma nota estruturada era o fundo de investimento de capital protegido. A desvantagem dessa modalidade de investimento em relação ao COE consiste no fato de que os investidores têm

---

de entrar ao mesmo tempo no fundo, no momento de captação. Enquanto, no COE, a emissão do título é feita para cada investidor individualmente, conforme sua disponibilidade e interesse por esse tipo de investimento, o que torna o COE mais flexível às demandas dos clientes investidores.

# 11.6 Surgimento do COE

O COE teve como referência as structured notes no mercado internacional, uma solução que permite ao investidor de renda fixa assumir algum outro fator de risco, utilizando para isso uma combinação de um título de renda fixa e derivativos. O COE no Brasil foi regulamentado apenas em 2010 pela Lei n. 12.249/2010, porém, apenas em 2013 o Banco Central promulgou a Resolução n. 4.263, que regulamentou as condições para que as instituições financeiras emitissem o COE.

O COE é registrado na Cetip, que se fundiu com a B3, e possui grande diversidade e possibilidades de registros com várias estratégias possíveis.

Inicialmente, o COE era oferecido apenas para o segmento de pessoa física de alta renda dos bancos. Com a automatização na emissão e o conhecimento mais detalhado desse produto pelos profissionais da área comercial dessas instituições, atingiu mais segmentos de varejo dos bancos, investidores da tradicional renda fixa, ou de fundos DI, que não estavam dispostos a arriscar o principal investidor, mas poderiam fazer um investimento menos líquido, porém com uma proposta de resultado diferenciado.

# 11.6.1 Structured notes

As structured notes surgiram muito antes do COE e foram a inspiração para a regularização deste. São basicamente um título de renda fixa combinado com contratos de derivativos, assim como o COE. O resultado da structured note dependerá dos juros da renda fixa e do resultado da operação com os derivativos. Atualmente, o volume de emissão de structured notes atingiu

---

aproximadamente 100 bilhões de dólares, o que a torna uma modalidade relevante no mercado financeiro internacional.

A structured note possui diversas possibilidades de ganhos em seus derivativos, inclusive na modalidade credit-linked note, cujo derivativo é um credit default sWap, ou seja, um derivativo de crédito.

# 11.6.2 Credit-Linked Notes (CLN)

A Credit-linked Note (CLN) é emitida por um banco, de forma que, caso ocorra eventual default da empresa objeto da CLN, o investidor receberá um percentual preestabelecido do seu capital inicial protegido. O objetivo da CLN é o de permitir que o investidor obtenha parte dos ganhos referente ao risco de crédito e, consequentemente, consiga resultados maiores no seu investimento acima da taxa risk-free dos títulos públicos americanos.

A proteção parcial ou integral do capital do investidor titular da CLN é possível porque parte dos recursos é investida em títulos de emissão do governo americano, o ganho adicional para o investidor acontece porque este possuirá uma posição vendida e receberá o prêmio do CDS pelo banco. Como essa operação tem lastro em títulos públicos, não é uma posição alavancada em CDS.

A vantagem para o banco emissor é que este pode transferir o risco de crédito de seus ativos de forma diluída aos seus clientes, oferecendo um excedente em termos de rentabilidade.

Logo, essa modalidade de investimento possui duas fontes distintas de risco de crédito: i) risco de crédito da instituição emissora da CLN e ii) risco de crédito da empresa cujo credit default sWap está relacionado. O titular da CLN deve ficar ciente dos dois riscos de crédito no qual está envolvido. Se por acaso a instituição emissora entrar em default, todo o principal da operação pode ficar comprometido, enquanto, se a empresa subjacente do credit default sWap entrar em default, fica valendo a regra de proteção do capital principal da CLN.

---

Vamos supor o seguinte exemplo: um banco empresta dinheiro a uma empresa, no momento do empréstimo emite uma CLN ligada ao crédito dessa empresa por um credit default swap, que, por consequência, é comprado pelos clientes do banco. A taxa de juros sobre a CLN é determinada pelo risco de crédito da empresa. Os recursos que o banco obtém com a emissão da CLN para os investidores são investidos títulos do governo americano. Se a empresa não entrar em default, o banco pagará as CLNs na íntegra para os investidores. Se a empresa referida do CLN for a falência, os titulares das notas tornam-se credores da empresa, devido ao credit default swap, e recebem apenas o percentual protegido do capital. O banco, por sua vez, reduz o risco global de crédito em seu balanço com a emissão de notas vinculadas a crédito.

Por enquanto, no Brasil, a emissão do equivalente a esse tipo de título na forma de COE não é autorizada pelo BACEN.

# 11.7 Tipos mais comuns de COEs

A Cetip permite o registro de diversos tipos de COEs. Basicamente, o que determina o resultado no vencimento do COE é a estrutura com opções e o tipo de ativo-objeto, a seguir mostraremos alguns tipos de COEs e as estratégias relacionadas a esses.

# 11.7.1 COE com call

Nessa modalidade, o investidor recebe um percentual da variação do ativo-objeto a partir de um determinado preço, definido pelo preço de exercício da opção, por exemplo, o investidor receberá 80% da variação do IBOVESPA a partir dos 102.000 pontos do índice. Se o IBOVESPA ficar abaixo dos 102.000, o investidor receberá 90% do principal investidor.

---

A seguir, um exemplo de resultado de COE comprado em call. É possível perceber que os ganhos para o investidor começam a partir de um determinado ponto, que é o strike da opção, o eixo horizontal representa a variação do preço do ativo-objeto e o eixo vertical o resultado do COE ao final do período:

Figura 11.1 | Resultado de COE com call
![img-94.jpeg](img-94.jpeg)
Fonte: Elaborada pelos autores.

# 11.7.2 COE com put

Nesse instrumento, o investidor começa a ganhar a partir do momento em que o preço do ativo fica abaixo de um preço de exercício, por exemplo, o investidor receberá 120% da variação cambial para dólar abaixo de R$ 5,30, que é o strike da opção. Veja a seguir um exemplo de resultado de um COE com put.

Figura 11.2 | Resultado de COE com put

---

![img-95.jpeg](img-95.jpeg)
Fonte: Elaborada pelos autores.

# 11.7.3 COE com call spread

Nessa modalidade de COE o investidor recebe um percentual da alta do ativo-objeto, porém os ganhos estão limitados a um preço de exercício. Consiste na compra de uma call de strike menor e a venda de uma call com strike maior. Por exemplo, o investidor recebe 100% do retorno do IBOVESPA acima de 102.000 pontos (strike 1), porém o ganho está limitado para o IBOVESPA a 140.000 pontos (strike 2). Se o IBOVESPA ficar abaixo dos 102.000 (strike 1) o investidor receberá 98% do principal investido.

Esse tipo de COE com ganhos limitados permite que o titular do COE receba um percentual maior de retorno sobre o ativo-objeto comparado com o COE com call, ou ainda um percentual maior sobre o capital protegido.

Veja a seguir um exemplo do COE com call spread:

Figura 11.3 | Resultado de COE com call spread

---

Figura 11.4 | Resultado de COE com call knock out
![img-96.jpeg](img-96.jpeg)
Fonte: Elaborada pelos autores.

# 11.7.4 COE com call knock out

O intuito dessa estratégia no COE também é o de permitir a redução do custo da operação e, consequentemente, oferecer um percentual maior do retorno do ativo quando comparado com a versão mais simples do COE com call.

Nesse tipo de COE o investidor recebe um percentual do retorno do ativo-objeto, limitado a uma barreira, porém quando o preço do ativo atinge a barreira, o ganho no ativo-objeto é cancelado e o titular passa a receber um retorno preestabelecido. Por exemplo, o investidor recebe 100% do retorno do IBOVESPA acima de 102.000 pontos, ao atingir a barreira de 130.000 pontos, o investidor passa a receber uma taxa de retorno de 4% ao ano pré-fixada. Se o IBOVESPA ficar abaixo dos 102.000 pontos o investidor receberá 100% do principal investido.

Veja a seguir o gráfico representativo do resultado do COE com call knock out, o eixo horizontal representa a variação do preço do ativo-objeto e o eixo vertical o resultado do COE ao final do período:

---

![img-97.jpeg](img-97.jpeg)
Fonte: Elaborada pelos autores.

# 11.7.5 COE com call knock in

Essa estratégia também possui uma barreira, e tem o objetivo de permitir a redução do custo da operação e, consequentemente, oferecer um percentual maior sobre o retorno do ativo quando comparado com o COE com call.

Diferentemente do knock out, nesse COE o investidor receberá um percentual do retorno do ativo-objeto somente quando o preço do ativo-objeto atingir a barreira. Enquanto o preço do ativo não atingir essa barreira, o ganho está limitado a um retorno preestabelecido. Por exemplo, o investidor receberá 100% do retorno do IBOVESPA acima de 102.000 pontos, a partir do momento que o IBOVESPA atingir a barreira de 110.000 pontos. Caso não se atinja esta barreira, o investidor receberá uma taxa de retorno de 4% ao ano pré-fixada. Se o IBOVESPA ficar abaixo dos 102.000 pontos, o investidor receberá 100% do principal investidor.

Veja a seguir o gráfico representativo do resultado do COE com call knock in:

Figura 11.5 | Resultado de COE com call knock in

---

![img-98.jpeg](img-98.jpeg)
Fonte: Elaborada pelos autores.

# 11.7.6 COE com straddle

Essa modalidade de COE consiste na compra de uma call e compra de uma put de mesmo strike e mesmo vencimento, de tal forma que o investidor ganhe na alta ou na baixa do ativo-objeto. Essa é uma estrutura de custo elevado, portanto, o investidor poderá receber um percentual menor do retorno do ativo-objeto. Por exemplo, o investidor terá 70% dos ganhos que superarem os 102.000 pontos do IBOVESPA ou 70% do retorno abaixo dos 102.000 pontos do IBOVESPA. Ou seja, o titular ganha se o IBOVESPA subir ou cair, mas não ganhará se o IBOVESPA ficar exatamente em cima dos 102.000 pontos. Veja a seguir o gráfico representativo do resultado do COE com straddle:

Figura 11.6 | Resultado de COE com straddle

---

![img-99.jpeg](img-99.jpeg)
Fonte: Elaborada pelos autores.

# 11.7.7 COE com strangle

Assim como o straddle, esta modalidade consiste na compra de uma call e na compra de uma put, porém de strikes diferentes, de tal forma que o investidor ganhe na alta ou na baixa do ativo-objeto, porém existe um intervalo no qual o investidor não ganha. Essa modalidade tem um custo um pouco menor do que o straddle, portanto, pode oferecer retornos maiores. Por exemplo, o investidor terá 80% dos ganhos que superarem os 105.000 pontos do IBOVESPA ou 80% do retorno abaixo dos 100.000 do IBOVESPA. Ou seja, o titular ganha se o IBOVESPA subir ou cair, mas não ganhará se o IBOVESPA ficar no intervalo entre 100.000 e 105.000 pontos. Veja a seguir o gráfico representativo do resultado do COE com strangle, o eixo horizontal representa a variação do preço do ativo-objeto e o eixo vertical o resultado do COE ao final do período:

Figura 11.7 | Resultado de COE com strangle

---

![img-100.jpeg](img-100.jpeg)
Fonte: Elaborada pelos autores.

# 11.7.8 COE com call digital

O resultado dessa modalidade de COE é tudo ou nada, é uma resposta binária ao comportamento do preço do ativo-objeto, se o preço do ativo ficar acima do strike acordado, o investidor receberá uma taxa pré-fixada, se ficar abaixo, o titular do COE receberá o percentual do capital investido. Por exemplo, se o IBOVESPA ficar acima dos 110.000 pontos, o investidor receber uma taxa de 15% ao ano, se ficar abaixo, receberá 100% do capital investido. O resultado depende do comportamento do preço do ativo-objeto, porém, o resultado do COE não será o retorno do ativo-objeto, mas sim uma taxa pré-fixada. Pode-se emitir também um COE com put digital, nesse caso o retorno pré-fixado é obtido se o preço do ativo ficar abaixo do strike da put. A seguir temos um gráfico representativo do resultado de uma COE com call digital.

Figura 11.8 | Resultado de COE com call digital

---

![img-101.jpeg](img-101.jpeg)
Fonte: Elaborada pelos autores.

# 11.7.9 COE com range accrual

Nessa modalidade, o investidor ganha uma taxa pré-fixada se o preço do ativo permanecer dentro de um intervalo preestabelecido. O investidor pode também receber um resultado parcial, dependendo do número de dias nos quais o ativo ficou dentro do intervalo. Por exemplo, o investidor receberá uma taxa pré-fixada de 15% ao ano se o IBOVESPA permanecer dentro do intervalo entre 100.000 e 110.000 pontos até o vencimento do COE, definida como zona de ganho, se o IBOVESPA ficar fora desse intervalo será contado o número de dias que o ficou fora, com isso, determina-se o percentual da taxa pré-fixada que o titular receberá ao final do período. Se o preço do ativo ficou 100% dos dias fora da zona de ganho, o investidor receberá 100% do capital inicial, por exemplo. A seguir temos um gráfico com a representação de um COE com range accrual:

Figura 11.9 | Resultado de COE com range accrual

---

![img-102.jpeg](img-102.jpeg)
Fonte: Elaborada pelos autores.

É possível montar uma infinidade de operações de COE, o resultado dependerá da estrutura montada com opções, ou seja, não há limites, principalmente com mecanismos de barreiras, limitadores, knock in e out.

# 11.8 Exemplo de operação com o COE

Exemplificaremos a construção de um COE desde a estruturação com opções e a precificação até a colocação de spread. O objetivo é mostrar o resultado do COE, tanto para o banco emissor quanto para o cliente titular do COE.

Vamos montar um COE com **call spread** com vencimento em dois anos, o ativo-objeto será o IBOVESPA. Neste COE, o investidor ganha se o IBOVESPA ficar acima dos 105.000 pontos, e terá os ganhos limitados aos 130.000 pontos.

No exemplo, o prazo até o vencimento do COE é de 503 dias úteis, o IBOVESPA está em 101.320 pontos e a taxa de juros pré-fixada livre de risco no período é de 6,14% a.a.o. (base 252), vamos supor que esse será também o custo de captação do banco.

---

O investimento inicial será de R$ 200 mil, com 100% de proteção ao capital inicial.

## 11.8.1 Precificação da operação

Antes de mais nada, devemos determinar qual é o capital disponível para a compra das opções. Para isso, descontamos o investimento inicial pela taxa pré-fixada de 6,14% a.a.o., considerando que teremos de devolver o principal inicial ao investidor, no mínimo, no vencimento do COE:



P = 200.000/(1 + 0,0614)^(503/252) = 177.572,02



Logo, teremos um total de R$ 22.427,98 para gastar com as opções, que é a diferença entre o capital inicial e o valor presente calculado de R$ 177.572,02.

Agora vamos precificar as duas opções de IBOVESPA, são duas calls de strikes diferentes, a primeira de strike 105.000 pontos e a segunda de strike 130.000 pontos.

No nosso exemplo, o IBOVESPA à vista está atualmente a 101.320 pontos.

A precificação pode ser feita de duas maneiras distintas, projetando o IBOVESPA para uma curva no futuro e precificando as opções com o modelo de Black (1976), ou pela forma mais trivial, por meio do modelo de Black e Scholes (1973), considerando o IBOVESPA à vista. Pode-se também utilizar o primeiro vencimento do contrato futuro de IBOVESPA, ajustando-se os prazos da opção.

### Spread na operação de COE

O spread para o banco emissor na operação de COE será colocado na volatilidade das opções, sendo que a de strike menor será precificada, por exemplo, com uma volatilidade de 35% ao ano enquanto a de strike maior

---

será precificada usando uma volatilidade de 30% ao ano. Dessa maneira, teremos um spread de cinco pontos percentuais de volatilidade entre a opção que o banco venderá e a opção que irá comprar do seu cliente. Dessa forma, venderá uma call mais cara e comprará a outra mais barata.

## Precificação das opções

Vamos precificar a opção de strike igual a 105.000 pontos, com a volatilidade de 35% ao ano.

O primeiro passo é converter a taxa de juros para a forma contínua:



r = ln(1 + 0,0614) = 0,059589



Calculamos d1 e d2:



d1 = ln(101.315/105.000) + (503/252)(0,35^2/2 + 0,059589)/0,35 √(503/252) = 0,415629





d2 = 0,415629 - 0,35 √(503/252) = -0,078855



Em seguida, obtemos os valores de N(d1) e N(d2), pela função densidade de probabilidade acumulada da normal padronizada (função disponível no Excel) que são, respectivamente: 0,66116 e 0,46857. Logo, o preço da call de strike 105.000 pontos será:



C = 101.315(0,66116) - 105.000/e^(0,059589(503/252)) (0,46857) = 23.305,68



Obtivemos um valor de R$ 23.305,68 para cada call de IBOVESPA de strike igual a 105.000. Calcularemos agora a opção de strike igual a 130.000

---

pontos, porém agora com volatilidade igual a 30% ao ano. Calculamos d1 e d2:



d1 = ln(101.315/130.000) + (503/252)(0,30^2/2 + 0,059589)/0,30 √(503/252) = -0,068704





d2 = -0,068704 - 0,30 √(503/252) = -0,492547



Os valores de N(d1) e N(d2) são 0,47261 e 0,31117, respectivamente, desse modo, o preço da opção de strike igual a 130.000 pontos será:



C = 101.315 (0,47261) - 130.000/e^(0,059589 (503/252)) (0,31117) = 11.969,73



Logo, a call de strike maior terá um valor de R$ 11.969,73.

No COE com call spread, o banco emissor ficará vendido na opção de strike igual a 105.000 pontos e comprado na opção de strike igual a 130.000 pontos, o titular do COE, consequentemente, estará em posição inversa, desse modo, o custo unitário das opções será de R$ 23.305,68 - R$ 11.975,89 = R$ 11.329,79.

O custo unitário da opção é equivalente ao IBOVESPA atual de 101.320 pontos, como o valor do investimento inicial do titular é de R$ 200.000, iremos precisar do equivalente a 1,9739 opções de IBOVESPA. Essa quantidade foi obtida pela divisão do valor do investimento inicial pelo IBOVESPA atual, da seguinte forma: R$ 200.000 / 101.320 = 1,9739.

# 11.8.2 Resultado do COE para o titular

Supondo que na emissão do COE o IBOVESPA estivesse exatamente a 101.320 pontos, para que o IBOVESPA atinja o preço de exercício de 105.000 pontos seria necessário que este subisse 3,63% até o vencimento

---

do COE, em dois anos. Contudo, o IBOVESPA teria de subir 28,31% para atingir os 130.000 pontos e o ganho do titular do COE estaria limitado nesse patamar. No vencimento do COE, se o IBOVESPA ficasse acima ou igual aos 130.000 pontos, o titular receberia o ganho máximo de 24,67% sobre o capital inicial, esse ganho é calculado pelo retorno de 28,31% para atingir o strike maior de 130.000 pontos, menos os 3,63% do strike menor de 105.000 pontos, que resulta no ganho máximo de 24,67%. Se o IBOVESPA ficar acima dos 130.000 pontos, por exemplo, 145.000 pontos, o ganho do titular ficará limitado a 24,67%.

A tabela a seguir apresenta o resultado potencial para o titular no vencimento do COE, ao final do período de dois anos.

Tabela 11.1 | Resultado do COE para o titular

|  IBOVESPA no vencimento do COE | Resultado na call de strike 105.000 | Resultado na call de strike 130.000 | Resultado total das opções | Retorno para o titular | Resgate no vencimento  |
| --- | --- | --- | --- | --- | --- |
|  100.000 | 0,00 | 0,00 | 0,00 | 0,00% | 200.000,00  |
|  105.000 | 0,00 | 0,00 | 0,00 | 0,00% | 200.000,00  |
|  110.000 | 9.869,72 | 0,00 | 9.869,72 | 4,93% | 209.869,72  |
|  120.000 | 29.609,16 | 0,00 | 29.609,16 | 14,80% | 229.609,16  |
|  130.000 | 49.348,60 | 0,00 | 49.348,60 | 24,67% | 249.348,60  |
|  140.000 | 69.088,04 | -19.739,44 | 49.348,60 | 24,67% | 249.348,60  |
|  150.000 | 88.827,48 | -39.478,88 | 49.348,60 | 24,67% | 249.348,60  |

Fonte: Elaborada pelos atores.

Conforme a tabela anterior, o valor de resgate máximo será de R$ 249.348,60 no vencimento do COE, se o IBOVESPA estiver maior ou igual aos 130.000 pontos, ou, alternativamente, o titular receberá 100% do capital investido, se estiver menor ou igual aos 105.000 pontos. Se o

---

IBOVESPA estiver entre os 105.000 e 130.000 pontos, o investidor receberá um retorno proporcional, por exemplo, se o IBOVESPA estiver aos 110.000 pontos, o investidor obterá um retorno de 4,93%, e resgatará R$ 209.869,72 no vencimento.

# 11.8.3 Hedge do COE para o emissor

Vamos imaginar que o emissor consiga emitir 100 COEs exatamente iguais ao acima descrito, o que representaria uma captação de R$ 20 milhões para o banco, a um custo de 6,14% ao ano. O banco teria ainda em sua carteira uma posição vendida em 197,39 unidades de calls de strike igual a 105.000 pontos do IBOVESPA e uma posição comprada na mesma quantidade de calls de strike igual a 130.000 pontos. É conveniente lembrar que o banco vendeu a call com uma volatilidade de 35% a.a.o., enquanto comprou a outra call com volatilidade de 30% a.a.o., esse spread lhe proporcionará ganhos, se forem bem administrados.

A tabela a seguir apresenta as gregas de cada uma das opções e as gregas totais da carteira:

Tabela 11.2 | Gregas da carteira de opções

|  Gregas | Call 105.000 | Call 130.000 | Carteira Total  |
| --- | --- | --- | --- |
|  Delta | 0,6612 | 0,4619 | -39,32  |
|  Gama | 0,0000073 | 0,0000092 | 0,000384  |
|  Vega | 523,8143 | 568,4699 | 8.814,75  |
|  Theta | -28,5536 | -25,1881 | 664,33  |
|  Rô | 821,4866 | 654,9769 | -32.868,08  |

Fonte: Elaborada pelos autores.

---

Calculamos as gregas da carteira multiplicando a quantidade de opções pela grega unitária de cada opção. O banco emissor está vendido na quantidade de 197,39 da call de strike igual a 105.000 pontos e comprado na mesma quantidade na call de strike 130.000, isso resulta no seguinte delta total da carteira:



Delta = 0,6612 × (-197,39) + 0,4619 × (197,39) = -39,32



Logo, o delta da carteira é negativo em R$ 39,32, ou seja, para cada ponto em reais que o IBOVESPA suba, a carteira perderá R$ 39,32. Portanto, o banco tem de fazer o delta hedge da carteira comprando aproximadamente 197 minicontratos de futuro de IBOVESPA. A quantidade de contratos foi obtida dividindo-se o delta por R$ 0,20, logo 39,32/0,20 = 196,62 minicontratos de IBOVESPA.

## Hedge de rô

O rô negativo das opções significa que a carteira está vendida em taxa de juros; o que poderá ser hedgeado por meio da compra de contratos futuros de DI com vencimento próximo a dois anos (vencimento do COE), consequentemente, zerando o DV01 da carteira.

Cada rô equivale a 100 unidades de DV01, isso significa que o DV01 da carteira de opções pode ser calculado dividindo-se o rô total por 100, resultando em um valor negativo de DV01 de R$ 328,68.

Para fazer o hedge de taxa de juros, vamos utilizar um contrato futuro de DI com vencimento mais próximo ao do COE, que vence em 538 dias úteis e está sendo negociado à taxa de 6,16% a.a.o. Primeiro, calculamos o preço unitário do contrato, cujo valor de face é de R$ 100.000:



PU = 100.000/(1 + 0,0616)^(538) = 88.018,82



---

Com o PU, podemos calcular o DV01 do contrato futuro de DI da seguinte forma:



DV01 = (538/252)/(1 + 0,0616) · 88.018,82 · (0,01/100) = 17,701



Para determinar a quantidade de contratos futuros de DI que devemos comprar, dividimos o DV01 total da carteira de opções pelo DV01 unitário do futuro de DI, que resulta em 328,68/17,701=18,57, ou seja, ou seja, aproximadamente 19 contratos futuros de DI.

Ao realizar o delta hedge, e hedge do ró, o resultado para o banco emissor será decorrente da posição resultante da carteira de opções.

Theta

O theta da carteira de opções é de R$ 624,33, o que significa que o banco ganhará esse valor para cada dia útil, até o vencimento do COE. É importante lembrar que o theta aumenta na medida em que a opção se aproxima do vencimento. Por exemplo, a 100 dias antes do vencimento do COE, o theta será de R$ 6.156,34 ao dia, o que incrementará substancialmente os ganhos do banco emissor.

Vega

A posição em vega é positiva em R$ 8.814,75, significa que haverá ganho para cada ponto percentual de incremento na volatilidade, e vice-versa.

Resumo da análise das gregas

---

A posição com gregas da carteira está favorável para o banco emissor em consequência do spread de volatilidade aplicado nas opções que compuseram o COE no momento da emissão.

Neste exemplo de COE podemos observar que é possível emitir um COE que seja favorável tanto para o investidor titular quanto para o banco emissor. Para o titular, porque permite que este consiga obter ganhos em renda variável, protegendo 100% do capital investido e para o emissor, porque permite uma captação pré-fixada de longo prazo e a obtenção de ganhos com o spread de volatilidade.

## RESUMO

Neste capítulo apresentamos as operações de COE, que é a versão brasileira das structured notes. Vimos que é um título híbrido, formado pela composição de derivativos e renda fixa. Apresentamos também as credit linked notes, que permitem maiores retornos para o titular com o uso de derivativos de crédito. Foram apresentados os tipos mais comuns de COEs, e um exemplo detalhado, com os resultados para o titular e para o emissor, por meio de uma operação de spread de volatilidade.

## EXERCÍCIOS PROPOSTOS

1. A seguinte operação de COE pode ser classificada como:

---

![img-103.jpeg](img-103.jpeg)

a. Straddle b. Strangle c. Call spread d. Call digital

2. Com relação a credit linked note responda corretamente:
a. O investidor possui risco de crédito do emissor e risco de mercado da empresa objeto.
b. O investidor possui risco de mercado do emissor e risco de mercado da empresa objeto.
c. O investidor possui risco de crédito do emissor e risco de crédito da empresa objeto.
d. O investidor possui risco de crédito do emissor e risco de mercado dos títulos públicos americanos.

3. Na operação de COE com range accrual, é correto afirmar:
a. O ganho será proporcional ao número de dias que o ativo estiver dentro da zona de ganho.
b. O investidor possui uma região de ganho, do tipo tudo ou nada.
c. O retorno será positivo apenas se o preço do ativo-objeto ficar acima de um strike predefinido.
d. Possui dois limitadores de ganho, um inferior e outro superior

4. Em um COE com call spread de IBOVESPA com vencimento em dois anos, cujo limite superior seja 150.000 pontos, e o limite inferior é de 112.000 pontos, sabendo que na emissão o IBOVESPA está a 109.512 pontos, qual será o retorno para o investidor se o IBOVESPA no vencimento estiver a 120.000 pontos? E

---

qual será o retorno para 160.000 pontos?

5. Quais são as desvantagens do fundo de capital protegido em relação ao COE? Explique por que esses fundos eram usuais antes de 2013.

---

# CAPITULO 12

# Hedge de empresas

---

# 12.1 Introdução

As empresas utilizam o mercado de derivativos para se protegerem contra os riscos de preços de moedas, do mercado de commodities e de taxas de juros. O intuito do hedge para as empresas é minimizar riscos que não são diretamente inerentes à atividade operacional, permitindo maior previsibilidade nos resultados.

Algumas empresas acabam não se protegendo contra esses riscos porque desconhecem os procedimentos para adoção do hedge, por questões culturais ou mesmo pela ausência de capital humano qualificado para tal.

A elaboração de uma política de hedge detalhada que defina os procedimentos para o hedge pode permitir que a empresa identifique os riscos no qual está exposta, mensure-os e defina quais são os derivativos adequados para mitigá-los.

Este capítulo busca abordar o processo de adoção do hedge em empresas, com exemplos de casos práticos e estrutura para a política de hedge.

# 12.2 Fazer hedge ou não?

O objetivo de se fazer uma operação de hedge é o de tornar o fator que era imprevisível em um fator mais previsível, ou menos imprevisível. Em uma empresa, quando se torna as receitas mais previsíveis, uma dívida, ou mesmo uma despesa, o impacto final ocorrerá no resultado da empresa e, consequentemente, para os acionistas.

Logo, a decisão de fazer ou não o hedge, está intimamente ligada à decisão de criar ou não valor para os acionistas.

Vamos partir da premissa fundamental de que o hedge possui um custo, e esse custo resultará em um impacto negativo no fluxo de caixa esperado da empresa. Uma perda no fluxo de caixa provoca uma redução de valor para os acionistas. Por outro lado, vamos supor que esse hedge tenha o intuito de neutralizar um fator de risco que possua uma probabilidade p de resultar em

---

um prejuízo futuro 200 vezes maior do que o custo do hedge em questão, ou uma probabilidade (1-p) de dar um resultado positivo no mesmo montante.

Suponhamos que ao fazer o hedge retiramos essa incerteza, mas incluímos o custo do hedge no fluxo de caixa. Ao tomar essa decisão, criamos ou não valor para o acionista?

Se a empresa tiver uma capacidade de financiamento ilimitada a uma taxa constante, e que p seja igual a (1-p), podemos estar destruindo valor para o acionista ao decidir fazer o hedge. Porém, essa situação não é realista. Sabemos que essas probabilidades podem ser apenas estimadas e, em geral, as empresas possuem uma capacidade limitada de financiamento. À medida que se aumenta a alavancagem financeira, consequentemente haverá aumento no custo de capital próprio da empresa, ou seja, na taxa de retorno exigida pelos acionistas.

Ao retirar a incerteza do fluxo de caixa futuro, a empresa poderá investir os recursos que deveriam ser contingenciados para cobrir o déficit de caixa no caso da ocorrência de perda. Mesmo que esse déficit seja financiado com dívidas, a empresa poderá utilizar essa capacidade de financiamento para investir em outros projetos de investimento, gerando valor incremental ao acionista.

O que temos de avaliar é se a disponibilidade de caixa com a eliminação da incerteza, com uma probabilidade de p, compensa o custo do hedge. De certa forma, o gestor deve optar por fazer o hedge se o benefício marginal da previsibilidade no resultado for maior do que o custo marginal de fazer o hedge.

Ainda analisando a decisão de fazer ou não o hedge, vamos supor que o administrador da empresa não tenha uma remuneração alinhada aos interesses do acionista, como a remuneração baseada em ações, mencionada neste livro. A decisão de fazer ou não o hedge pode ser uma causa de conflito de agência, que é o conflito de interesses entre o administrador e o acionista.

Se o intuito do administrador for o de maximizar a própria riqueza, deverá preservar a sua estabilidade de emprego na empresa. Ao decidir fazer o hedge, retirará a imprevisibilidade do fluxo de caixa futuro, mesmo destruindo valor para o acionista, logo, diminuirá a probabilidade de resultados negativos e, consequentemente, preservará o seu emprego.

---

Contudo, ao longo deste capítulo vamos partir da premissa de ausência de conflito de agência, ou seja, o administrador tomará decisões de hedge que maximizem valor para os acionistas.

Uma empresa possui diversos riscos em sua atividade, de fornecimento, das vendas, da qualidade do produto, de atendimento, pós-venda, entre outros. Todos esses riscos fazem parte da atividade operacional da empresa. Adicione-se a esses os riscos de variação cambial, taxas de juros, preços de commodities e de ativos financeiros.

O objetivo do hedge é o de mitigar alguns riscos que não fazem parte diretamente da atividade operacional da empresa, porém, podem impactar o resultado da empresa ou, até mesmo, colocar em risco a sua existência.

## 12.2.1 Vantagens do hedge

A execução de um hedge tem como objetivo oferecer proteção e segurança. A melhor analogia para o hedge é o seguro de bens. Nesse caso, entenda o hedge como um seguro para preços de ativos financeiros ou commodities.

Smith e Stultz (1985) argumentam que o hedge é uma das formas de reduzir a volatilidade dos lucros de uma companhia e, dessa forma, também reduzir a probabilidade de a empresa entrar em dificuldades financeiras.

Quando uma empresa faz hedge, o perfil de crédito dessa empresa deveria melhorar, pois a empresa diminuiu a probabilidade de entrar em falência.

Além de aumentar a previsibilidade dos resultados e reduzir a probabilidade de entrar em dificuldades financeiras, o hedge permite melhor gestão dos ativos e passivos da empresa ao torná-los menos voláteis. Assim como torna o fluxo de caixa mais previsível, principalmente em se tratando de recebíveis e exigíveis que não estão representados na moeda funcional da empresa.

Para instaurar um procedimento de hedge, a empresa deverá utilizar um método para mensurar os diversos fatores de riscos financeiros aos quais esteja exposta. A mensuração dos riscos é uma das vantagens da adoção de procedimento de hedge, pois traz à tona riscos que possivelmente não eram medidos, ou nem mesmo identificados.

---

Após mensurar os riscos, o gestor deverá avaliar as diversas alternativas de operações com derivativos para determinar quais são as mais adequadas para mitigar cada risco específico no qual a empresa está exposta, e apenas depois disso, tomar a decisão de fazer ou não o hedge.

Após a decisão do hedge, recomenda-se que o administrador avalie os impactos dos fatores de risco em uma situação extrema, que denominamos teste de stress, e mensure o potencial desgaste financeiro que esses fatores possam causar no resultado ou no fluxo de caixa da empresa.

Outra vantagem das operações de hedge está relacionada à imagem para o mercado da empresa que realiza esse tipo de operação. Dão indicação aos bancos, que são aqueles que lhe concedem empréstimos e financiamentos, que existe preocupação com a gestão e que houve uma decisão de não ficar exposto a uma situação de risco financeiro relevante. Também demonstra aos acionistas e credores que a gestão da companhia possui capacidade de mensurar e de executar os mecanismos necessários de proteção.

# 12.3 Desvantagens do hedge

Assim como um seguro, o hedge possui um custo e geralmente é realizado entre uma empresa e um banco. Para que isso ocorra, o banco precisa aprovar um limite de crédito para operações com derivativos tendo a empresa como contraparte, somente depois do limite aprovado que se promove a assinatura do Contrato Global de Derivativos (CGD). A empresa tem duas opções, poderá fazer o hedge com o banco, dessa maneira incorrerá em um custo relativo ao spread da operação; ou poderá realizar o hedge em bolsa, tendo a bolsa como contraparte. Para fazer na bolsa, a empresa deve abrir uma conta em corretora, e incorrerá em custos de corretagem, emolumentos, registro, liquidação e custódia. Ao realizar a operação em bolsa, a empresa deverá comprar ativos, geralmente títulos públicos, para depositar em garantia na clearing, ou seja, deverá investir seu caixa em ativos financeiros. Além disso, deverá administrar o fluxo de caixa

---

diário decorrentes dos ajustes, se as operações forem feitas com contratos futuros.

Não bastasse os custos e processos operacionais, a empresa deverá marcar a mercado as operações com derivativos, recolher tributos e contabilizá-los.

Quando a empresa é um novo entrante no mercado de derivativos, ainda deve passar por uma curva de aprendizado, com adoção de novos processos e política de hedge. Nesse caso, o maior entrave para as empresas adotarem derivativos para o hedge é a falta de capital humano qualificado para realizar essas operações, ainda mais se as operações forem realizadas em bolsa.

# 12.4 Hedge ou especulação?

Existe uma linha tênue que separa o intuito da empresa em fazer hedge ou especulação, observamos alguns casos recentes de empresas que utilizavam os derivativos para fazer hedge, e atraídas pelo resultado positivo que os derivativos proporcionaram, começaram a aumentar as posições além da necessidade de hedge em situações que denominamos como over-hedge. Na verdade, o over-hedge, ou qualquer operação com derivativos cujo intuito não seja o de proteção, terá cunho especulativo.

Por que as empresas que começam a especular geralmente acabam perdendo, em algum momento, nas operações com derivativos?

As operações especulativas com derivativos geralmente provocam perdas. O especulador profissional consegue administrar essas perdas, pois sabe que na soma das perdas e ganhos, no longo prazo, deverá ter um saldo positivo.

A empresa não consegue administrar as perdas, pois o impacto será direto no seu fluxo de caixa, ou seja, no seu capital de giro, que possui outras obrigações operacionais que precisam ser administradas. Além disso, as empresas não possuem estrutura e a agilidade necessárias para as operações especulativas. As intenções especulativas geralmente acabam em perdas

---

inesperadas para as empresas e devem ser evitadas. A empresa deve manter o foco em seu core business.

# 12.5 Fatores de risco

Antes de iniciar o processo de implantação do hedge, a empresa precisa identificar os fatores de risco aos quais está exposta. Vamos entender os fatores de risco como variáveis financeiras cuja oscilação impacta diretamente o resultado da empresa, vamos citar alguns exemplos de negócios e os fatores de risco envolvidos em cada um deles.

Por exemplo, uma empresa importadora de derivados de petróleo, gasolina e diesel possui três fatores de risco distintos, o preço de cada um dos dois derivados no mercado internacional e a variação do câmbio, em consequência do contas a pagar com a importação.

Uma empresa aérea possui receitas em reais, em decorrência da venda de passagens aéreas. Porém, possui muitas despesas em dólar, como o leasing, a manutenção das aeronaves e o querosene de aviação. Geralmente, as empresas aéreas conseguem repassar parcialmente o custo da variação cambial no preço de suas passagens, contudo, isso acontece com certa defasagem, não é instantâneo. Logo, as empresas aéreas possuem dois fatores de risco: o preço do petróleo e derivados no mercado internacional e a variação cambial para as contas a pagar em dólares de curto prazo.

Após identificar os riscos, a empresa deverá mensurá-los e identificar a sua necessidade de hedge.

# 12.6 Hedge de fluxo de caixa e de balanço

Vamos supor que uma montadora de veículos possui contas a pagar em dólar referente a importações, no montante de US$ 10 milhões que vencerá

---

em sete meses. Sabemos que a moeda funcional dessa empresa é o real. Para se proteger contra a variação cambial, essa empresa decide tomar um empréstimo em reais e fazer uma aplicação financeira em dólar, recebendo variação cambial em contrapartida.

A situação inicial da empresa pode ser representada por meio de um balanço, sendo que o lado direito representa o passivo, em que se encontra as contas a pagar em dólar:

Figura 12.1 | Representação do balanço em dólar
![img-104.jpeg](img-104.jpeg)
Fonte: Elaborada pelos autores.

Vamos adicionar a essa representação de balanço o empréstimo em reais e a aplicação em dólar, a aplicação é um ativo, e deve ficar do lado esquerdo, enquanto o empréstimo é um passivo e ficará do lado direito. O ativo é hedge natural do passivo, ou seja, o passivo do contas a pagar em dólares é hedgeado pela aplicação financeira em dólares e anulam-se, o que sobra é o empréstimo em reais, como vemos na figura a seguir.

Figura 12.2 | Representação do balanço em dólar

---

![img-105.jpeg](img-105.jpeg)

Fonte: Elaborada pelos autores.

Os pagamentos e recebimentos das figuras anteriores podem ser representados na forma de fluxos de caixa, sendo que a seta para cima indica recebimento, e para baixo, pagamento. Nas contas a pagar em dólares, teremos uma saída de caixa de US$ 10 milhões em sete meses. No empréstimo em reais teremos um recebimento de reais e pagamento do principal mais os juros ao final de sete meses. Na aplicação em dólares, teremos uma saída de dólares no momento inicial, exatamente no mesmo montante da entrada de reais, e teremos, por consequência, um recebimento de US$ 10 milhões, também em sete meses, que coincidirá com o pagamento em dólares. A representação dos fluxos de caixa pode ser verificada na figura a seguir.

Figura 12.3 | Fluxo de caixa em dólar e reais

---

![img-106.jpeg](img-106.jpeg)
Fonte: Elaborada pelos autores.

O primeiro fluxo no topo da figura representa a saída de caixa em dólares, o segundo fluxo é o empréstimo em reais, com a entrada de caixa inicial, a saída de caixa posterior com o pagamento do empréstimo e o terceiro fluxo de caixa representa a aplicação em dólares, na qual é possível observar que o fluxo de caixa inicial é igual ao fluxo de caixa inicial do empréstimo, com sentidos opostos. A operação do exemplo poderia ser estruturada por meio de um swap dólar x Pré, que possui fluxo de caixa ativo em dólar e passivo em taxa pré-fixada em reais, o efeito seria similar.

# 12.6.1 Exemplo de net exposure

Suponha que uma empresa possua US$ 850 milhões de passivos em dólar, e US$ 150 milhões em ativos. O net exposure (exposição cambial líquida) deve ser calculado pela diferença entre ativos e passivos em dólar, logo, nosso exemplo será igual a uma posição passiva de US$ 600 milhões, conforme representado pelo seguinte balanço:

---

Figura 12.4 | Representação do balanço em milhões de dólares
![img-107.jpeg](img-107.jpeg)
Fonte: Elaborada pelos autores.

Devemos fazer o hedge apenas do net exposure de US$ 600 milhões, pois o ativo de US$ 150 milhões é hedge natural do passivo de US$ 850 milhões. Um net exposure passivo em dólares é equivalente a uma posição vendida em dólares, por isso, ao fazer o hedge, devemos ficar comprados em contratos derivativos de dólar em um notional equivalente a US$ 600 milhões.

Agora vamos adicionar mais informações a esse exemplo: suponha que o prazo médio de recebimento (PMR) do ativo é de 30 dias, e que o prazo médio de pagamento (PMP) do passivo é de 120 dias, o net exposure continua sendo os mesmos US$ 600 milhões?

A resposta é sim. Para o cálculo do net exposure, o prazo do ativo e do passivo não é relevante, pois o exposure é calculado pelas contas de saldo e não de movimento.

Nesse caso, como o PMR é menor do que o PMP, receberemos as contas a receber em dólar antes do que iremos pagar as contas a pagar, ou seja, haverá uma diminuição do hedge natural. Quando o ativo em dólar diminui, ou o passivo aumenta, teremos um aumento do net exposure, nesse caso teremos de aumentar marginalmente a necessidade de hedge.

---

A administração do hedge é dinâmica e tem como base o fluxo de pagamentos e recebimentos em dólar.

O valor nocional das operações de hedge deve ser aproximadamente igual ao net exposure. Com a inclusão do hedge, o saldo gerencial do exposure deve sempre se manter o mais próximo de zero.

Se os prazos médios dos ativos e passivos em dólar são diferentes, qual o prazo que devemos adotar para o hedge? 30 ou 120 dias?

Na administração do hedge, os prazos até vencimento dos contratos de derivativos devem ser preferencialmente mais reduzidos, mesmo que o administrador tenha mais trabalho para fazer a rolagem das posições. Prazos mais curtos são mais indicados, pois permitem melhor administração do hedge, que torna o processo de neutralização do exposure relativamente mais preciso.

Sempre que possível podemos coincidir o vencimento do contrato de derivativo com o fluxo de recebimento ou pagamento em dólar que está gerando o exposure. Por exemplo, uma determinada empresa deve realizar pagamentos de US$ 50 milhões no dia 15 de cada mês, relativos a parcelas de um inter-company loan. Se o fluxo e o valor da parcela são previsíveis, é possível realizar um hedge que se adeque perfeitamente a esses pagamentos.

A administração do net exposure, por meio das contas de saldo, geralmente é indicada para empresas altamente ativas no comércio internacional, com múltiplos fechamentos de câmbio, e, portanto, que possuem baixa previsibilidade dos fluxos de recebimentos e pagamentos, nesse caso, a gestão por contas de saldo é a mais eficiente.

Em geral, a posição com derivativos de balcão fica fragmentada, pois, a cada fechamento de câmbio, o saldo do hedge deverá se modificar.

Uma alternativa à fragmentação dos contratos derivativos é a administração do hedge com uso de contratos futuros de dólar, que permite certa flexibilidade na gestão do hedge com um único tipo de contrato. O hedge com futuros torna a neutralização do exposure mais precisa, não necessita de múltiplas cotações, como no mercado de balcão, pois a negociação é feita de forma eletrônica em bolsa. A cotação do contrato futuro é justa, possui alta liquidez, o que traz agilidade na administração do hedge. Nada impede que a

---

administração do hedge seja feita por meio de operações de balcão, como o NDF ou o swap de dólar, porém, haverá menos agilidade no processo de cotação e execução do hedge, mas o hedge terá a mesma eficiência comparado aos futuros.

Para avaliar se o hedge está adequado ao exposure, é necessário calcular o resultado com variação cambial, com e sem o efeito do hedge.

O resultado com variação cambial é feito pela variação da moeda sobre cada uma das contas de ativos e passivos, se o hedge foi feito de forma precisa ao longo do tempo, sempre com intuito de neutralizar o exposure, o resultado com variação cambial deverá ser sempre próximo a zero.

## Exemplo 12.1 - Cálculo de exposure e hedge de moeda

Uma empresa possui fluxos de recebimento e pagamentos em dólar, e deseja calcular o exposure, ou seja, a exposição cambial para os próximos sete dias úteis. Essa empresa possui, atualmente, contas a pagar no montante de US$ 700 milhões, no quarto dia fará um pagamento de US$ 80 milhões, reduzindo, assim, o saldo das contas a pagar para US$ 620 milhões a partir dessa data. A empresa possui uma dívida em dólar, cujo saldo é de US$ 900 milhões e pagará uma parcela de US$ 60 milhões dessa dívida no terceiro dia. Também possui recebíveis em dólar, que atuam como hedge natural, cujo saldo atual é de US$ 200 milhões. Sabe-se, porém, que receberá US$ 40 milhões no sexto dia. O saldo do exposure está na coluna direita da tabela a seguir, é possível notar que o saldo diminui no terceiro e quarto dias, e aumenta no sexto dia.

Tabela 12.1 | Cálculo do exposure em milhões de dólares

|  Dias úteis | Contas a pagar | Dívida | Contas a receber | Exposure  |
| --- | --- | --- | --- | --- |
|  1 | -700 | -900 | 200 | -1.400  |
|  2 | -700 | -900 | 200 | -1.400  |
|  3 | -700 | -840 | 200 | -1.340  |
|  4 | -620 | -840 | 200 | -1.260  |
|  5 | -620 | -840 | 200 | -1.260  |
|  6 | -620 | -840 | 160 | -1.300  |

---

|  7 | -620 | -840 | 160 | -1.300  |
| --- | --- | --- | --- | --- |

Fonte: Elaborada pelos autores.

A empresa decide fazer o hedge sobre o saldo do exposure por meio de operações de balcão com derivativos. A tabela a seguir apresenta mais duas colunas: a penúltima coluna à direita é o saldo das operações de hedge, e a última coluna à direita é o net exposure, nessa coluna é possível verificar que o saldo não está completamente zerado, ou seja, o resultado negativo indica um passivo em dólar, equivalente a uma posição vendida em dólar, e o saldo positivo uma posição ativa.

Tabela 12.2 | Cálculo do hedge em milhões de dólares

|  Dias úteis | Contas a pagar | Dívida | Contas a receber | Exposure | Posição de hedge | Net exposure  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | -700 | -900 | 200 | -1.400 | 1.390 | -10  |
|  2 | -700 | -900 | 200 | -1.400 | 1.390 | -10  |
|  3 | -700 | -840 | 200 | -1.340 | 1.390 | 50  |
|  4 | -620 | -840 | 200 | -1.260 | 1.390 | 130  |
|  5 | -620 | -840 | 200 | -1.260 | 1.260 | 0  |
|  6 | -620 | -840 | 160 | -1.300 | 1.300 | 0  |
|  7 | -620 | -840 | 160 | -1.300 | 1.300 | 0  |

Fonte: Elaborada pelos autores.

Verificamos que o hedge não foi perfeito, logo, o ativo e passivo não foram totalmente neutralizados, o que resultará em perdas ou ganhos com variação cambial. A tabela a seguir apresenta as cotações diárias do dólar na segunda coluna à esquerda. O cálculo com variação cambial é feito diariamente com base no saldo de cada uma das contas, e somado ao final da coluna. Verificou-se que o resultado com variação cambial ficou com o saldo positivo em R$ 7,2 milhões de reais, se o hedge não fosse feito, haveria perda com variação cambial em um total de R$ 248 milhões, dado apresentado ao final da coluna "Exposure". O intuito de apresentar o

---

resultado é o de demonstrar, gerencialmente, a eficiência da operação de hedge. O resultado com variação cambial deve ficar aproximadamente igual a zero, sempre:

Tabela 12.3 | Resultado com variação cambial em milhões de reais

|  Dias úteis | Cotação R/US | Contas a pagar | Dívida | Contas a receber | Exposure | Posição de hedge | Net exposure  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0 | 4,04 |  |  |  |  |  |   |
|  1 | 4,05 | -7,00 | -9,00 | 2,00 | -14,00 | 13,90 | -0,10  |
|  2 | 4,07 | -14,00 | -18,00 | 4,00 | -28,00 | 27,80 | -0,20  |
|  3 | 4,09 | -14,00 | -16,80 | 4,00 | -26,80 | 27,80 | 1,00  |
|  4 | 4,14 | -31,00 | -42,00 | 10,00 | -63,00 | 69,50 | 6,50  |
|  5 | 4,16 | -12,40 | -16,80 | 4,00 | -25,20 | 25,20 | 0,00  |
|  6 | 4,18 | -12,40 | -16,80 | 3,20 | -26,00 | 26,00 | 0,00  |
|  7 | 4,23 | -31,00 | -42,00 | 8,00 | -65,00 | 65,00 | 0,00  |
|   |  | -121,80 | -161,40 | 35,20 | -248,00 | 255,20 | 7,20  |

Fonte: Elaborada pelos autores.

Verificamos que no exemplo anterior a operação de hedge demonstrou sua eficácia, ao evitar o impacto negativo da variação cambial no fluxo de caixa e, consequentemente, no resultado da empresa.

# 12.7 Efetividade do hedge

A efetividade do hedge mede as mudanças do valor justo (fair value) do hedge em relação as mudanças no valor justo do objeto de hedge ou item protegido. Por outro lado, um hedge será ineficiente na medida em que a mudança no valor justo não compensa a mudança do objeto de hedge. O

---

objeto de hedge é aquilo que será protegido, por exemplo, um passivo ou ativo em moeda estrangeira ou um estoque de commodities. Nesse caso, o objeto de hedge pode ter um ou mais fatores de risco. A efetividade do hedge avalia se as mudanças no valor justo do hedge compensam as mudanças do valor justo do objeto de hedge.

# 12.7.1 Índice de efetividade do hedge

O índice de efetividade do hedge (IEH) é calculado dividindo-se as mudanças no valor justo do hedge pelas mudanças no valor justo do objeto de hedge, pode ser calculado pontualmente ou cumulativamente. Se o hedge é 100% efetivo, as mudanças no valor justo do hedge e do seu objeto serão as mesmas, porém com sinais inversos. Se as mudanças forem diferentes, ou seja, valor justo do objeto de hedge variar relativamente mais ou menos, teremos inefetividade do hedge. O índice de efetividade do hedge deve ser calculado periodicamente. O resultado da efetividade do hedge deve ser analisado conforme o seguinte quadro:

Quadro 12.1 | Índice de efetividade do hedge

|  Efetividade do hedge Índice de Efetividade do hedge  |   |
| --- | --- |
|  Não efetivo | IEH < 80%  |
|  Efetivo | 80%< IEH< 125%  |
|  Não efetivo | IEH> 125%  |

Fonte: Elaborado pelos autores.

O IEH deve ser calculado periodicamente, sendo que um índice inferior a 80% e superior a 125% são considerados inefetivos. Cada empresa pode definir os seus próprios limites de efetividade, logo, os limites da tabela anterior são apenas sugestões. Se as variações do valor justo do hedge forem menores do que a do objeto de hedge, ou seja, índice menor que 80%,

---

indica que o a posição está under-hedge, ou seja, insuficiente para cobrir a exposição ao risco provocada pelo objeto de hedge. Em contrapartida, se o indicador for maior que 125%, a posição está over-hedge, ou seja, mais do que necessária para proteger o risco.

Nas duas situações, under ou over-hedge, podemos obter resultados inesperados, pois, de certa forma, a empresa está deliberadamente exposta ao risco de variações do ativo-objeto.

# 12.8 Gerenciamento de risco de mercado

Em uma política de hedge é necessário definir a mensuração do risco para verificar o impacto dos diversos fatores de risco em situações extremas ou em cenários com probabilidade esperada, a seguir explicaremos brevemente dois métodos conhecidos para o cálculo do risco, o Value at Risk (VaR) e o Teste de Stress.

# 12.8.1 Value at Risk (VaR)

Value at Risk é uma mensuração de risco que permite calcular uma perda esperada para um cenário com probabilidade e intervalo de tempo definidos. O VaR procura responder à pergunta: quanto vamos perder se ocorrer um cenário mais adverso do que o esperado?

É uma medida de risco que pode ser facilmente implementada quando se tem apenas um fator de risco, por exemplo, o risco de moeda única. Vamos implementar um exemplo para este caso.

Para o cálculo do VaR, inicialmente devemos calcular o valor a mercado, definido como marcação a mercado.

A marcação a mercado (mark to market) pode ser feita de duas formas: pelo valor de mercado (market value), que pode ser o último preço negociado do

---

ativo a mercado, e pelo valor justo (fair value), que é utilizado quando o ativo em questão não é negociado a mercado, dessa forma, determinamos o valor do ativo por comparação com ativos ou fatores de risco similares.

No exemplo anterior temos uma posição em dólar, e a cotação do dólar é diariamente divulgada pelo Banco Central, que utilizaremos como o valor a mercado.

No VaR paramétrico para ativos diversificados é comum que cada um dos ativos seja desmembrado em fatores primitivos de risco, como vértices de curvas de juros, cupom cambial, risco de mercado de ações e outros, para determinar a volatilidade da carteira.

O VaR determina, com certo nível de significância estatística, ou nível de confiança, a perda esperada. O VaR paramétrico parte da premissa de que os retornos discretos possuem distribuição conhecida, geralmente uma distribuição normal. Essa é uma premissa fraca, porque uma variável aleatória x que possui distribuição normal, seus valores devem estar no intervalo -∞ < x < ∞, o que não acontece com os retornos discretos.

No gráfico de distribuição normal a seguir podemos verificar o VaR para 95\% de confiança, ou seja, com perda esperada igual ou inferior a 5\%:

Figura 12.5 | VaR de 5\%
![img-108.jpeg](img-108.jpeg)
Fonte: Elaborada pelos autores.

O VaR paramétrico pode ser calculado de forma simples, utilizando a volatilidade e o período de manutenção da posição – holding period – que é o período necessário para se desfazer do risco, liquidando os ativos e

---

passivos. O VaR de n dias úteis para um nível de significância de k pode ser calculado na data t da seguinte maneira:



VaR_((k,n,t)) = P_t z' sigma_t √(n) 



Sendo:

P_t: valor marcado a mercado na data t z': variável normal padronizada crítica, logo, z para 95% é de 1,645

sigma_t: volatilidade dos retornos, na base 252 dias úteis

n: holding period, tempo considerado para o VaR

## 12.8.2 Exemplo de VaR de variação cambial

Suponha que uma empresa tenha um passivo em dólar de US$ 90 milhões e decida não fazer o hedge. Qual deve ser a perda esperada com a variação cambial com 95% de confiança, ou com 5% de probabilidade, para um prazo de 21 dias úteis, sabendo que a volatilidade do dólar é de 15% a.a.o. (base 252 d.u.) e a cotação do dólar na data de hoje é de R$ 4,15?

O VaR é calculado sempre em unidade monetária, neste caso, reais, logo, devemos determinar o valor da carteira multiplicando a cotação do dólar pelo valor do passivo, que resulta em R$ 375 milhões:



P_t = 90.000.000 × (4,15) = 375.000.000



O VaR(5\%, 21d.u.) deve ser calculado da seguinte forma:



VaR_((5\%, 21d.u.)) = 375.000.000 × 1,645 × 0,15 × √(21/252) = 26.604.625



---

Logo, com um nível de significância de 5%, para um prazo de 21 dias úteis, a perda esperada seria de aproximadamente R$ 26,6 milhões, para um passivo de US$ 90 milhões.

## 12.8.3 Análise de Stress

O Teste de Stress é uma ferramenta muito importante na gestão de risco e que complementa o VaR, pois analisa cenários potencialmente extremos, ou específicos, que não são tratados naquele método.

O Teste de Stress consiste na avaliação dos impactos no resultado da empresa por meio de simulações não estocásticas nos fatores de risco. Simulações não estocásticas são simulações que utilizam cenário definidos, por exemplo, por um comitê macroeconômico da firma. A seguir alguns exemplos destes cenários:

- Aumento de 15% na taxa de câmbio BRL/USD;
- Queda de 15% na taxa de câmbio BRL/USD;
- Aumento no nível das taxas de juros em 2%;
- Queda no nível das taxas de juros em 2%;
- Deterioração do rating de crédito da empresa;
- Deterioração do rating de crédito dos credores da empresa;
- Perda estimada devido a um cenário político;
- Perda estimada devido a um cenário jurídico;
- Perda estimada devido ao processamento ou controle manual de operações complexas.

Observamos que os cenários de estresse vão além de cenários relacionados ao risco de mercado, englobando, por exemplo, cenários de crédito, operacional e legal. Uma crítica a esse tipo de metodologia é que os cenários são definidos arbitrariamente.

Além da definição de cenários discricionários, é possível utilizar no Teste de Stress simulações que utilizam dados históricos, por exemplo, se ocorressem

---

variações nos fatores de risco como as que ocorreram na crise de 2007-2008, qual seria o impacto nos resultados da empresa?

Uma metodologia interessante para a realização de Testes de Stress foi apresentada no artigo "Um Modelo de Teste de Stress Menos Subjetivo e Mais Abrangente", de Cícero Augusto Vieira Neto e Fabio Urban. O artigo recomenda a criação de faixas de variações em cada um dos fatores de risco. Para cada faixa é calculado o impacto no resultado. Uma conclusão importante do artigo é que as piores perdas não necessariamente ocorrem nos cenários extremos, por isso é fundamental analisar também o que ocorre nos cenários intermediários.

Os cenários de estresse poderiam, quando utilizados e analisados corretamente, ter alertado algumas empresas brasileiras durante a crise, principalmente no ano de 2008, sobre a vulnerabilidade dessas firmas em relação à sua exposição cambial.

# 12.9 Política de hedge

A política de hedge tem como objetivo principal definir as diretrizes para que o processo de decisão, execução e acompanhamento do hedge seja realizado adequadamente para mitigar ou neutralizar os riscos a que sejam direcionados. Uma política de hedge pode ser isoladamente elaborada, ou ser parte integrante da Política de Gestão de Riscos.

A política de hedge deve ser elaborada dentro do contexto no qual a empresa esteja inserida, logo, as empresas que atuam em diferentes atividades podem possuir políticas de hedge distintas, mas, geralmente, possuem uma estrutura similar. A seguir iremos apresentar os principais itens que devem constituir uma política de hedge bem elaborada:

- Propósito: geralmente uma política de hedge tem o propósito de definir procedimentos e medidas para proteger o fluxo de caixa da empresa e seu lucro contra riscos de preços e de mercado com o uso de operações com derivativos. Geralmente, pode-se incluir que a política tem o propósito de proteger o valor para o acionista.

---

- Escopo: a política deve limitar o escopo de sua atuação. Se a política de hedge é elaborada de forma isolada, e não é parte integrante da política de risco, é conveniente limitar o escopo apenas para os riscos de mercado, não envolvendo os riscos de crédito e outros riscos, tais como: riscos de liquidez e de concentração por emissor. Pode-se ainda fechar mais o escopo, definindo quais os fatores de risco que serão monitorados. Por exemplo, uma importadora de derivados de petróleo talvez queira limitar o escopo em dois fatores de risco: risco do preço da commodity petróleo e risco da variação cambial.

- Origens dos fatores de risco: na política de hedge devemos identificar cada um dos fatores de risco e quais são as origens desses riscos. Por exemplo: uma empresa aérea possui risco cambial em decorrência de pagamentos de parcelas de leasing de aeronaves importadas e do querosene de aviação. Outra empresa, possui risco de preço de grãos, mais especificamente do preço de milho, pois faz parte dos insumos de algum produto alimentício específico que produz.

- Responsabilidades: a adequada segregação de responsabilidades evita que se excedam os limites de risco e previne contra eventuais fraudes e conflitos de interesse. O intuito é definir quem serão os responsáveis pela tríade do hedge: i) decisão, ii) execução e iii) monitoramento. Geralmente, as decisões pertinentes ao hedge são feitas de forma colegiada por um comitê. A política deve estabelecer quais os membros que compõem o comitê de hedge, quais as atribuições e a frequência das reuniões do comitê.

- Comitê de hedge: dentre as principais atribuições do comitê de hedge está a revisão da política de hedge, que geralmente ocorre a cada um ou dois anos. Outras atribuições do comitê são: definição dos limites aceitáveis de risco, delegar a execução do hedge a uma equipe, supervisionar a execução dentro dos limites de risco definidos e monitorar a eficácia do hedge. Usualmente, as reuniões ordinárias ocorrem uma vez por mês, ou a cada trimestre.

---

Equipe de execução: a equipe é definida pelo comitê e deverá gerenciar e administrar transações de acordo com a política de hedge, mas possui diversas outras atribuições, tais como: - Manter registros de todas as transações;

- Reconciliar os registros das transações com os registros enviados pela contraparte (banco ou bolsa); - Calcular preços indicativos para derivativos de hedge; - Garantir preços competitivos para as operações com derivativos;
- Executar transações conforme necessário;
- Registrar e valorizar os derivativos;
- Fornecer relatórios regulares para o comitê de hedge.

- Medição do risco e limites: pode-se utilizar diversas formas para mensurar o risco no qual a empresa está exposta. Discutimos algumas formas de mensurar o risco, desde um cálculo de exposure, cálculo de VaR, Teste de Stress e por meio do índice de efetividade do hedge. Por exemplo, o cálculo de exposure depende da disponibilidade das contas de saldo e do prazo no qual essa conta de saldo está disponível. Vamos imaginar o exemplo de uma empresa exportadora de açúcar, que é uma commodity cujo preço é determinado em dólares e oscila no mercado internacional. Talvez a empresa decida hedgear parte do seu forecast de exportação, ou seja, queira utilizar as projeções de suas receitas de exportação. Nesse caso, para definir o risco de preço e a variação cambial, deve-se determinar qual o prazo de forecast que se deseja hedgear. Outra variável que se deve definir, além do prazo, é o percentual da exposição que se deve hedgear, que pode estar intimamente ligada ao prazo. A tabela a seguir é um exemplo de limites para operações de hedge de exposição para o preço do açúcar e da variação cambial:

Quadro 12.2 | Exemplo de limites de hedge do exposure

|   | Açúcar |   | Dólar  |   |
| --- | --- | --- | --- | --- |
|  Período | Mínimo | Máximo | Mínimo | Máximo  |
|  6 meses | 90% | 110% | 95% | 105%  |

---

|  12 meses | 80% | 100% | 95% | 105%  |
| --- | --- | --- | --- | --- |
|  18 meses | 50% | 60% | 90% | 110%  |
|  24 meses | 30% | 40% | 90% | 110%  |

Fonte: Elaborado pelos autores.

No exemplo apresentado no quadro anterior observamos que no período até seis meses tanto o exposure de açúcar quanto o cambial devem ser praticamente 100% hedgeados, com pequenos limites. Para prazos posteriores, acima de 12 meses, o limite de hedge diminui, para em torno de 50% do exposure causado pela exportação prevista de açúcar, enquanto a exposição cambial continua com o limite desejável em torno de 100%.

- Instrumentos autorizados: na política de hedge devem estar definidos os instrumentos derivativos autorizados e qual instrumento é indicado para cada um dos fatores de risco. Por exemplo, para exposição em dólar fica autorizado NDF e opção de compra de dólar com preço de exercício pelo menos 10% superior a cotação atual do dólar.
- Instruções finais: toda política de hedge deve mencionar as normas de compliance da companhia, como também os aspectos regulatórios, tais como normas contábeis e as normas divulgadas pelas instituições reguladoras, como a CVM e o Banco Central.

# 12.10 Hedge de taxas de juros

Até o momento, tratamos predominantemente do risco com variação cambial e de commodities, agora vamos apresentar também o hedge de taxas

---

de juros.

A exposição em taxas de juros ocorre quando se possui um ativo ou passivo pré-fixado e a marcação a mercado desse ativo pode impactar o resultado da companhia ou da instituição financeira em questão.

O risco ocorre porque, quando a taxa de juros sobe, o valor presente dos títulos diminui, em decorrência de fatores diversos, provavelmente macroeconômicos. Ao descontarmos o valor de face do título a valor presente, utilizamos a taxa de juros de mercado, conforme a seguinte equação:



P = F/(1 + i) ^t tag {12.2}



Sendo:

- P : valor presente do título de renda fixa
- F : valor de face ou valor futuro
- i : taxa de juros discreta, pré-fixada e exponencial
- t : tempo até vencimento do título

É importante lembrar que quando a taxa de juros sobe, o valor presente do título diminui. Ou seja, existe um risco da taxa de juros em relação ao valor presente do título, que pode ser protegido com derivativos de taxas de juros, como o contrato futuro de DI ou o swap DI/Pré.

Suponha que uma entidade tenha em seu ativo títulos pré-fixados, se, porventura, a taxa de juros subir, essa entidade terá um resultado negativo na marcação a mercado dos seus títulos. Logo, ao perder quando a taxa de juros sobe, concluímos que está vendida em taxa de juros, portanto, deverá comprar taxas de juros para fazer o hedge.

Consideremos agora outro cenário, no qual a entidade emitiu títulos pré-fixados, logo, possui um passivo pré-fixado, caso a taxa de juros suba, o valor dos títulos e, consequentemente, do seu passivo, será menor, ou seja, será benéfico para a empresa. Quando a taxa de juros sobe e a empresa ganha dinheiro, significa que está comprada em taxa de juros, e para fazer o hedge terá de vender taxa de juros.

---

O primeiro passo para fazer o hedge de taxa de juros é mensurar o risco por meio do DV01, medida de risco já apresentada no Capítulo 3.

Apenas para relembrar, o DV01 é uma medida que fornece a variação do valor presente do título para uma variação de um ponto base na taxa de juros (0,01% a.a.o.), pode ser representado pela seguinte equação:



DV01 = t/(1 + i) × P × (0,01\%) 



Sendo:

P: o valor presente atual marcado a mercado do título objeto do hedge

Quando se quer neutralizar o risco de taxas de juros, devemos zerar o DV01 da carteira, ou seja, se tivermos um ativo pré-fixado, teremos de comprar taxa nos contratos futuros de DI ou de swap, de forma a neutralizar o risco de renda fixa, conforme a seguinte equação:



DV01_(II) = Σ(j=1 até n) DV01_j Q_j 



Sendo:

DV01_(II): DV01 total da carteira de títulos e derivativos de renda fixa, deve ser igual a zero

Q_j: quantidade do j-ésimo instrumento de renda fixa na carteira DV01_j: DV01 do j-ésimo instrumento de renda fixa na carteira

É importante lembrar que o instrumento derivativo utilizado para hedge deverá ter prazo de maturidade próximo ao do título (ou títulos) objeto de hedge de renda fixa. Isso ocorre porque existem movimentos distintos ao longo da curva de juros. Dessa forma, fazer o hedge de um título de maturidade longa utilizando um derivativo de vencimento curto, pode não ser eficiente.

Se a curva de juros tivesse apenas movimentos de nível, ou seja, deslocamento paralelo nas taxas de juros, hedges de prazos distintos seriam eficientes. Entretanto, a curva de juros possui outros movimentos, como o

---

de inclinação, em que as taxas longas se movimentam de forma diferente das curtas, e movimento de curvatura, que indica que os movimentos podem inclusive ter direções diferentes no curto e longo prazos da curva de juros.

Em suma, utilizar um ou mais derivativos com vencimentos próximos ao objeto de hedge pode ser mais eficiente para o resultado do hedge.

## Exemplo 12.2 - Hedge de taxa de juros

Vamos fazer um exemplo simples de hedge de um título de renda fixa utilizando mercado futuro de DI. Suponha que empresa emitiu um título pré-fixado, cujo valor atual a mercado é de R$ 10.923.014, com um prazo de 720 dias úteis até o vencimento, descontado a taxa de 5,70% a.a.o.

Antes de mais nada, vamos calcular o valor o DV01 desse título, utilizando as informações fornecidas:



DV01 = 720/252/(1 + 0,057) × 10.923.014 × (0,01\%) = 2.952,56



O resultado significa que se a taxa de juros subir um ponto base, o passivo dessa empresa ficará menor em R$ 2.952,56, ou seja, o valor do título ficará menor.

O risco para essa empresa ocorre se a taxa de juros cair, nesse caso, seu passivo ficará maior, para evitar esse risco, poderá realizar um hedge com taxa de juros.

Vamos utilizar como instrumento de hedge um contrato futuro de DI que vence em 742 dias úteis, negociado a taxa de 5,72% a.a.o. Antes de mais nada, vamos calcular o PU desse contrato que sempre tem valor de face igual a R$ 100.000:



P = 100.000/(1 + 0,0572)^(742/252) = 84.892,75



Após obter o PU do contrato, calculamos o DV01 do futuro de DI:



DV01 = 742/252/(1 + 0,0572) × 84.892,75 × (0,01\%) = 23,64



---

O resultado indica que, se a taxa de juros subir um ponto base, o valor presente do contrato futuro reduzirá R$ 23,64. É importante lembrar que nos contratos futuros de DI podemos nos posicionar comprados ou vendidos em taxas de juros.

Se a empresa possui um passivo em títulos pré-fixados, significa que está comprada em taxas de juros. Logo, para fazer o hedge, deverá vender contratos futuros de DI.

O hedge de taxa pressupõe que o somatório do DV01 dos instrumentos deve ser igual a zero para neutralizar o risco de taxa pré-fixada. Logo, vamos determinar a quantidade de contratos que devemos vender para neutralizar a taxa:



2.952,56 + 23,64 × Q_(DI) = 0



Na equação acima, Q_(DI) representa a quantidade de contratos de DI necessária para neutralizar o risco de renda fixa, isolando-se o Q_(DI) na equação teremos:



Q_(DI) = - 2.952,56/23,64 = -124,90



Teremos de vender aproximadamente 125 contratos de futuro de DI para proteger essa empresa contra as variações das taxas de juros.

É importante lembrar que o risco de taxa de juros deve ser neutralizado se a posição de instrumentos de renda fixa, objeto de hedge, representa um risco de marcação a mercado material para a entidade, e o prazo do título seja diferente do horizonte de investimento da entidade.

Isso significa que, por exemplo, se a entidade comprou um título de cinco anos para utilizar os recursos exatamente no mesmo prazo, significa que o risco de renda fixa deixa de ser relevante.

## Exemplo 12.3 - Hedge com muitos vencimentos

Suponha que a entidade seja um banco de montadora de veículos. Geralmente esse tipo de banco possui em sua carteira recebíveis referentes a financiamentos de veículos, que são pré-fixados em sua grande maioria.

Ou seja, o banco possui uma carteira de títulos pré-fixados com múltiplos vencimentos, praticamente em todos os dias úteis nos próximos cinco anos.

Quando a taxa de juros sobe, o valor dessa carteira de recebíveis marcada a mercado fica menor, ou seja, impactando negativamente o resultado do banco.

---

Vamos observar na figura a seguir uma representação da carteira de recebíveis do banco nos próximos cinco anos:

Figura 12.6 | Recebimentos pré-fixados com múltiplos vencimentos
![img-109.jpeg](img-109.jpeg)
Fonte: Elaborada pelos autores.

Podemos notar que existe um fluxo de recebíveis pré-fixados, não apenas um único vencimento como no exemplo anterior. Nesse caso, devemos fragmentar a carteira em partes, preferivelmente anuais, ou seja, vamos neutralizar o DV01 dos títulos apenas do primeiro ano, em seguida do segundo ano, assim sucessivamente. O hedge pode ser feito de uma só vez, na forma de bullets anuais. Geralmente, na operação de balcão cada ano deve ser feito por um notional diferente, ou seja, a empresa informará ao banco cinco valores nocionais com cinco vencimentos diferentes, ou seja, cinco bullets, e a cotação de compra de taxa de juros fica mais ágil.

Ao dividir a carteira em tranches anuais, o hedge ficará mais eficiente, pois ficará protegido quanto aos movimentos da curva de juros.

# RESUMO

Neste capítulo apresentamos os conflitos do administrador na execução do hedge para criação de valor para os acionistas, tratamos das vantagens e desvantagens de executar o hedge. Abordamos a mensuração do exposure cambial e formas práticas de realizar o hedge para empresas exportadoras e importadoras. Definimos os principais componentes de uma política de hedge e, por fim, abordamos o hedge de renda fixa para entidades que possuem risco de marcação a mercado de títulos

# EXERCÍCIOS PROPOSTOS

1. Entende-se por hedge natural: a. Um passivo em reais que protege um ativo em

---

dólares.

b. Um passivo em dólares que protege um ativo em reais.
c. Um ativo em dólares que protege um ativo em dólares.
d. Um ativo em dólares que protege um passivo em dólares.

2. Dentre as desvantagens do hedge é correto afirmar: a. O custo do hedge é superior ao de um seguro.
b. Hedge não pode ser contabilizado.
c. Se for feito em bolsa, deve-se depositar garantias.
d. O hedge não possui custo apenas se for negociado com um banco.

3. Uma empresa possui US$ 500 milhões de contas a pagar dólar, com vencimento em 5 meses, US$ 150 milhões contas a receber com vencimento em 17 semanas, e uma aplicação em dólares de US$ 50 milhões, que poderá resgatar em 12 meses, logo, o exposure em dólar dessa empresa será de: a. US$ 250 milhões
b. US$ 300 milhões
c. US$ 350 milhões
d. Não possui exposure, pois os pagamentos ocorrerão apenas no futuro

4. Utilizando a tabela a seguir, calcule o resultado com variação cambial:

|  Cotação do dólar | Dias úteis | Contas a pagar | Divida | Contas a receber | Exposure | Posição de hedge | Netexposure  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  4,32 | 1 | -900 | -600 | 200 | -1.300 | 1.300 | 0  |
|  4,35 | 2 | -900 | -600 | 200 | -1.300 | 1.300 | 0  |
|  4,31 | 3 | -900 | -550 | 200 | -1.250 | 1.300 | 50  |
|  4,37 | 4 | -720 | -550 | 200 | -1.070 | 1.300 | 230  |

5. No exercício anterior a empresa está over-hedge ou under-hedge? Quais as consequências de uma posição que não está 100% hedgeada?

6. Uma empresa emitiu um título pré-fixado e possui um passivo de R$ 45.320.000, marcado a mercado a taxa de 5,30% a.a.o. Sabendo que esse

---

passivo vence daqui a 2.397 dias úteis, quantos contratos futuro de DI serão necessários para hedgear esse risco de renda fixa, sabendo que o futuro de DI com vencimento em 2.402 dias úteis é negociado a taxa de 5,28% a.a.o? A posição do hedge é comprada ou vendida em taxa?

---

CAPITULO 13

# Planos de opções para executivos: stock option plan

---

As opções para executivos são uma forma de remuneração baseada em ações, utilizadas como mecanismo de atração e retenção de pessoas importantes para a empresa. Geralmente, faz parte do pacote de remuneração oferecido pela companhia e é também uma forma do beneficiário do plano tornar-se sócio.

O plano de opções de compra de ações tem como objetivo alinhar os interesses dos administradores, beneficiários do plano, com os interesses dos acionistas e mitigar o conflito de agência, ao vincular os ganhos desses administradores com o aumento de valor da ação da companhia.

Os planos de opções de ações possuem uma estrutura muito similar a das opções de compra de ações, as calls, pois também possuem preço de exercício e prazo para vencimento.

É conveniente lembrar que o plano de opções é um benefício adicional ao pacote de remuneração dos executivos, ou seja, não é excluente aos planos de bônus ou participação nos resultados.

Entretanto, algumas críticas têm sido feitas aos planos de opções, entre elas é que essa modalidade de remuneração pode premiar o beneficiário do programa por consequência de condições do mercado de ações, e não pelo seu resultado gerencial. Em contrapartida, o plano pode não premiar o bom administrador, mesmo que este tenha desempenhado bom trabalho, caso o mercado não lhe seja favorável no momento de exercício das opções. Devemos considerar que o acionista também está sujeito a intempéries de mercado, quando o acionista ganha, o beneficiário do plano de opções também ganha.

Neste capítulo, apresentaremos a estrutura dos planos de opções de compra de ações utilizados como forma de remuneração de longo prazo e discutiremos o cálculo de fair value dessas opções.

# 13.1 Plano de opções da compra de ações

---

O plano de opções consiste no direito de compra de certa quantidade de ações da companhia, cedido ao funcionário beneficiário do programa, a um determinado preço de exercício por ação – ou preço de compra da ação – que deve ser exercido em um período, ou prazo de exercício.

Na data do exercício do direito, as ações alienadas ao beneficiário do plano devem ser objeto de uma nova subscrição ou devem estar em tesouraria.

Os demais acionistas da empresa não têm direito de subscrição sobre as ações destinadas aos planos de opções. Dessa forma, ocorre a diluição do capital da companhia proporcional à quantidade das novas ações subscritas.

O beneficiário do plano pode exercer o direito de compra das ações disponibilizadas a partir de cada uma das datas de maturação (vesting) do plano, podendo exercer o direito de compra até a data de expiração do direito.

## 13.2 Aprovação do plano de opções

Via de regra, os planos de opções são aprovados em Assembleia Geral de Acionistas (AGE) em pauta extraordinária, o texto do plano de opções deve ser adicionado como anexo à ata da AGE, e publicamente divulgado, no caso de companhias abertas.

Em assembleia, deve ser estipulado o percentual máximo do capital social da companhia, que será objeto das outorgas de opções de compra de ações. Haverá diluição do capital, por isso é conveniente estipular um limitador em quantidade de ações ou em percentual.

Geralmente, o texto do plano define as regras gerais das opções que serão concedidas. O instrumento de outorga descreve maiores detalhes em relação às opções concedidas para cada beneficiário, como a quantidade individual, as datas de maturação e de vencimento das opções.

Com o decorrer do tempo, podem ser aprovados vários planos, com características e regras distintas para concessão das opções. Cada opção

---

outorgada pela companhia deve fazer parte de um plano previamente aprovado pelos acionistas.

No texto do plano de opções de compra de ações, deverão constar, entre outros, os seguintes itens:

a. tipo de ações objeto do plano;
b. se haverá entrega de instrumentos patrimoniais, ou se a liquidação ocorrerá em caixa;
c. quem será responsável pela administração do plano e pelas outorgas decorrentes dele – geralmente, a administração do plano é feita pelo conselho de administração (CA) da companhia;
d. regras para o cálculo do preço de exercício e eventual correção por inflação;
e. regras para pagamentos de dividendos, agrupamento e desdobramento das ações objeto do plano;
g. período de caducidade do plano – geralmente é um período longo, por exemplo, dez anos;
h. forma de exercício da opção e prazos para pagamento;
i. efeitos no desligamento do funcionário beneficiário do plano – por exemplo: falecimento, demissão com ou sem justa causa;
j. procedimento em eventos extraordinários, tais como:
i. alienação de controle da companhia;
ii. abertura ou fechamento de capital;
iii. direito e obrigação de venda conjunta, tag e drag along;
iv. regras para antecipação dos direitos do beneficiário.

# 13.3 Modalidades de planos

---

Os planos de opções podem ser classificados pela entrega ou não de instrumentos patrimoniais: equity plan, quando o pagamento ao beneficiário é feito com entrega de instrumentos patrimoniais, por exemplo, entrega de ações; e liability plan, quando o pagamento é feito em caixa, ou seja, o instrumento patrimonial é utilizado apenas como referência para o cálculo do pagamento da remuneração, mas não é entregue ao beneficiário. Existe, ainda, uma terceira modalidade mista, na qual o beneficiário do plano recebe parte em ações e parte em caixa.

As duas modalidades de remuneração diferenciam-se porque, na primeira, o beneficiário, efetivamente, torna-se sócio da empresa e, na segunda modalidade, não há participação societária, nem mesmo diluição das ações.

Outra importante diferença é que o equity plan é considerado um mecanismo de remuneração baseado em ações que envolvem participação societária. A segunda modalidade, o liability plan, com pagamento feito em caixa, é considerado como remuneração e será incluído no cálculo de salário do executivo. É importante lembrar que em ambas operações existem fatos geradores de remuneração e devem ser interpretados como tal.

Há algumas modalidades de planos de opções que são liquidados com entrega de ações, porém possuem cláusulas de recompra dessas ações por parte da empresa, esta possui uma call contra o beneficiário, com preço de exercício maior do que o da opção concedida a ele. A regra para esse tipo peculiar de plano será a mesma adotada no liability plan, ou seja, deve ser reconhecido como um passivo liquidado em caixa.

Se o equity plan for concedido por uma empresa com ações negociadas em bolsa, o executivo poderá vender suas ações a mercado, adquiridas por meio do exercício de suas opções. Se auferir ganhos com a venda das ações, deverá recolher o imposto sobre renda variável.

Alguns planos incluem cláusulas de lock up, no qual os beneficiários devem permanecer por um período preestabelecido em posse das ações, antes de realizar a venda a mercado.

Os planos de opções podem ser classificados, ainda, como primário ou secundário. No plano primário, é a empresa quem concede o benefício. Nesse caso, quando houver exercício do direito de compra de ações por parte do beneficiário, deverão ser emitidas novas ações pela companhia ou

---

deverão ser vendidas ações que estão em tesouraria.

No plano do tipo secundário, é o acionista controlador quem concede o direito de compra de ações de sua propriedade, como objeto do plano de opções.

Em ambos os casos, a empresa deverá reconhecer as despesas do plano, mesmo sendo o acionista controlador concedente das opções. Isso acontece, pois a despesa deve ser reconhecida onde o serviço é prestado.

É comum ocorrer emissão de ações para empresas de um mesmo grupo, por exemplo, os administradores de uma empresa controlada recebem opções de ações concedidas pela controladora. Nesse caso, a contabilização deve ser feita pela empresa outorgante e pela empresa onde o serviço é prestado.

# 13.4 Datas de outorga, maturação e vencimento do plano de opções

A data de outorga é a data na qual o beneficiário assina com a companhia o instrumento particular de outorga, podendo também fazê-lo, em alguns casos, com efeito retroativo.

O instrumento particular de outorga é um contrato que tem efeito de adesão ao plano, anteriormente aprovado pelos acionistas em assembleia.

Após a outorga, o beneficiário, que é titular da opção, ainda não possui o direito adquirido, ou seja, deverá aguardar o período de vesting ou o período de maturação dessa opção. Decorrido o período de vesting, a opção é considerada madura, ou seja, a partir da data de maturação, o beneficiário adquire o direito de compra das ações.

A aquisição do direito pode ser condicionada pela mera permanência do funcionário na companhia ou podem ser adicionadas cláusulas de atingimento de indicadores de performance, por exemplo, índices financeiros, como é feito geralmente na concessão de bônus. É importante

---

não confundir o plano de opções com o pagamento de bônus, são modalidades de remuneração distintas.

Sugerimos que a estrutura do plano de opção seja simples e de fácil entendimento pelos executivos, beneficiários do plano.

Entre a data de maturação e o vencimento, o beneficiário poderá, ou não, exercer o direito de compra da ação pelo preço de exercício da opção. Geralmente, as opções possuem características do tipo americano após a data de maturação, pois o beneficiário pode adquirir as ações a qualquer momento, entre a data de maturação e o vencimento da opção, desde que as ações estejam disponíveis em tesouraria, ou seja feita uma nova emissão de ações. A Figura 10.1 a seguir mostra a estrutura mais comum das opções para executivos, representa a linha do tempo após a data de outorga, decorre o período de vesting, que se encerra na data de maturação. O período de exercício, no qual o beneficiário pode comprar as ações, expira-se na data de vencimento da opção.

Figura 10.1 | Datas de outorga, de maturação e de vencimento das opções
![img-110.jpeg](img-110.jpeg)
Fonte: Elaborada pelos autores.

# 13.5 Instrumento de outorga

O instrumento de outorga é um contrato particular firmado entre a companhia e o beneficiário selecionado para receber as opções de compra de ações. No plano do tipo secundário, o contrato é firmado entre o acionista controlador e o beneficiário.

---

O administrador do plano, geralmente o conselho de administração, é quem define as condições de outorga individual. Devem ser registrados em ata de reunião do conselho de administração as seguintes informações: o beneficiário selecionado, a quantidade de opções a serem concedidas e o preço de exercício da opção.

No instrumento de outorga, as seguintes informações devem estar explicitadas:

a. citar o plano de opções previamente aprovado, no qual o instrumento faz referência;
b. dados do beneficiário;
c. data de outorga;
d. quantidade de opções de ações concedidas;
e. preço de exercício;
f. prazos de maturação (vesting) e datas de expiração do direito;
g. condições para aquisição do direito (vesting conditions), por exemplo, permanência na empresa;
h. efeitos do desligamento do funcionário.

O instrumento de outorga deve ser complementar ao plano, em que as características gerais das opções já foram previamente definidas. No instrumento de outorga devem ser definidos os detalhes, tais como as quantidades, os prazos e o preço de exercício, e deve mencionar que o beneficiário está ciente das características do plano previamente aprovado pelos acionistas.

Um mesmo beneficiário pode receber múltiplas outorgas, pois algumas empresas adotam a concessão de novas opções anualmente, e cada uma delas com datas de maturação distintas e dívidas em tranches, de tal forma que o beneficiário possuirá um estoque de opções para acompanhar. As opções de uma mesma outorga podem ser concedidas com diferentes datas de maturidade.

Exemplo 10.1 - Outorga de opções

---

Nesta seção, vamos exemplificar uma outorga de opções feita por uma companhia para um executivo, na modalidade equity plan. Suponha que foram concedidas 5.000 opções de compra de ações a um beneficiário selecionado pelo conselho de administração, sendo que destas, 1.000 opções ficarão maduras após um ano, mais 1.000 após dois anos e assim sucessivamente, nos próximos cinco anos.

Após cada data de maturação, o beneficiário terá mais um ano para exercer seu direito de compra das ações, decorrido o período de um ano, o direito expira.

Nesse exemplo, cada data de maturação é considerada uma tranche distinta, esse benefício pode ser definido como um graded vesting award, ou seja, à medida que o tempo passa, o beneficiário adquire uma parcela do direito, conforme pode ser observado na tabela a seguir.

Tabela 10.1 | Exemplo de outorga de 5.000 opções de compra de ações

|  Data-base | Quantidade de opções concedidas | Quantidade de opções maturadas cumulativamente | Quantidade de opções expiradas cumulativamente | Quantidade de opções maduras remanescentes  |
| --- | --- | --- | --- | --- |
|  Data de outorga | 5.000 | 0 | 0 | 0  |
|  Ano 1 | 0 | 1.000 | 0 | 1.000  |
|  Ano 2 | 0 | 2.000 | 1.000 | 1.000  |
|  Ano 3 | 0 | 3.000 | 2.000 | 1.000  |
|  Ano 4 | 0 | 4.000 | 3.000 | 1.000  |
|  Ano 5 | 0 | 5.000 | 4.000 | 1.000  |
|  Ano 6 | 0 | 5.000 | 5.000 | 0  |

Fonte: Elaborada pelos autores.

Na tabela anterior, é possível notar que a cada ano o beneficiário adquire o direito de compra de 1.000 ações de opções que se tornam maduras. Porém, ele terá apenas mais um ano, após a maturação, para exercer o direito de compra da ação, se não exercer o direito, este expirar-se-á.

No exemplo a seguir apresentaremos um caso de concessão de opções, no qual se define apenas uma data de maturação para todas as tranches concedidas. Por exemplo, a data de expiração de todas as tranches ocorrerá um ano após a última data de maturação da última tranche, nesse caso, o direito de compra de ações acumular-se-á com o tempo.

No exemplo mostrado na tabela a seguir ocorre a acumulação do direito de compra das ações:

Tabela 10.2 | Exemplo de outorga de 5.000 opções com acumulação do direito adquirido

---

|  Data-base | Quantidade de opções concedidas | Quantidade de opções maturadas cumulativamente | Quantidade de opções expiradas cumulativamente | Quantidade de opções maduras remanescentes  |
| --- | --- | --- | --- | --- |
|  Data de outorga | 5.000 | 0 | 0 | 0  |
|  Ano 1 | 0 | 1.000 | 0 | 1.000  |
|  Ano 2 | 0 | 2.000 | 0 | 2.000  |
|  Ano 3 | 0 | 3.000 | 0 | 3.000  |
|  Ano 4 | 0 | 4.000 | 0 | 4.000  |
|  Ano 5 | 0 | 5.000 | 0 | 5.000  |
|  Ano 6 | 0 | 5.000 | 5.000 | 0  |

Fonte: Elaborada pelos autores.

Na Tabela 10.2, o direto de compra das ações acumulou-se à medida que as opções se tornaram maduras. Essa condição permite ao beneficiário postergar a decisão de exercício de compra das ações, aguardando condições mais favoráveis.

Se uma opção concede mais tempo de exercício para o beneficiário, acarretará em um aumento do seu fair value e, consequentemente, na despesa que deverá ser reconhecida pela empresa.

# 13.6 O preço de exercício

O preço de exercício pode ser similar ao de uma opção de compra de ação negociada em bolsa, ou seja, pode ser um preço fixo, determinado pelo conselho de administração.

Geralmente, usa-se uma regra preestabelecida para definir o preço de exercício e simplificar a decisão do CA. Por exemplo, pode-se considerar que o preço de exercício da opção seja um percentual da média dos últimos n pregões com negociação da ação em bolsa, sendo esse percentual geralmente menor do que 100\%. Essa regra, para determinar o preço de exercício da opção, pode ser adotada por companhias de capital aberto, com ações negociadas em bolsa.

Os preços de exercício devem ser ajustados na ocorrência de grupamento e desdobramento das ações da companhia, de tal forma que o beneficiário não seja prejudicado, nem beneficiado.

---

Para empresas de capital fechado, sem ações listadas em bolsa, o preço de exercício também pode ser determinado como valor fixo, para tal, pode-se usar um múltiplo de valor da empresa.

Por exemplo, o preço de exercício da opção pode ser determinado como um percentual do valor por ação referente a um número de vezes o Ebitda¹ ou Ebit² da empresa.

É importante considerar que, se o preço de exercício for muito elevado, o beneficiário pode não se sentir suficientemente estimulado para participar do plano de opções, porque dificilmente essas opções serão exercidas. Se o preço de exercício for muito baixo, o beneficiário entenderá como uma doação de ações, o que não se alinharia com os interesses dos acionistas. É necessário encontrar um meio termo para que o plano não perca seu propósito de motivar o beneficiário. Também é importante que as opções não sejam entendidas como doação.

Porém, em alguns casos peculiares, as opções são concedidas com preço de exercício simbólico, quando o objetivo do plano é que o beneficiário se torne sócio, praticamente sem desembolso de caixa, após um determinado período de vesting.

Algumas empresas fazem outorgas com prazos muito longos, com muitos tranches, por exemplo, com prazos iguais ou superiores a cinco anos. Nesses casos, é possível adotar um índice de inflação para correção do preço de exercício, para evitar que a opção se torne exercível com a mera desvalorização do strike.

Algumas medidas podem ser adotadas para que as opções se tornem atrativas novamente, quando ocorre a queda no valor da ação. Pode-se reduzir o preço de exercício ou alterar as condições de vesting para favorecer o beneficiário. Por exemplo, quando o preço da ação cai por conta de uma condição de mercado, pode-se aplicar um fator redutor do preço do exercício, para que o plano volte motivar o beneficiário.

É importante lembrar que o recurso de redução do preço de exercício ou redução do período de vesting aumentará o valor remanescente das opções e essa despesa adicional deve ser reconhecida pela empresa.

---

# 13.7 Procedimentos para o exercício da opção

Durante o período de exercício, o beneficiário pode, a qualquer momento, expressar o seu interesse pela compra das ações, com pagamento realizado em moeda corrente.

O pagamento em dinheiro pela ação é uma regra bastante comum nos planos de opções, mas pode não ser suficiente motivante para o beneficiário, que, eventualmente, pode não possuir os recursos financeiros necessários para pagar pelas ações, perdendo uma boa oportunidade.

Algumas empresas de capital aberto com ações negociadas em bolsa oferecem algumas facilidades para o exercício do direito de compra das ações, tais como oferecer prazo para pagamento pelas mesmas. Por exemplo, algumas empresas oferecem o prazo de 60 dias para pagamento pelas ações, por consequência do exercício das opções.

Nesse caso, o beneficiário poderá receber as ações sem ter de desembolsar caixa de imediato. Terá tempo suficiente para vender parte ou totalidade das ações no mercado e com os recursos recebidos pela venda, pagar o preço de exercício à empresa, dentro do prazo previamente estabelecido. Em alguns casos, a empresa pode exigir que o beneficiário assine uma nota promissória, ou similar, ao receber as ações, no valor referente ao total do exercício de compra.

A empresa poderá estabelecer que a data de exercício que coincida com o pagamento de bônus, de forma que se possa abater do bônus o valor a ser pago pela compra das ações.

O beneficiário deve expressar o seu desejo de adquirir as ações, sobre as quais tem direito de compra, por meio do preenchimento e assinatura de um termo de exercício, especificando a quantidade, a tranche, e a data na qual deseja adquirir as ações.

O termo de exercício faz parte do rol de documentos que constituem o plano de opções, aprovado pelos acionistas em assembleia.

---

Além dos mecanismos anteriormente apresentados, a empresa poderá exigir condições adicionais para a aquisição do direito de compra das ações, tais como: estipular um prazo para que a tesouraria disponibilize as ações para venda, mediante a recompra de ações a mercado, ou ainda, definir uma data anual para emissão de ações, para que todos os beneficiários interessados exerçam o direito de compra ao mesmo tempo.

Adicionalmente, o plano de opções deve estabelecer regras para ocorrência de eventos de cunho societário, tais como: alienação do controle da companhia, abertura ou fechamento de capital. Essas regras podem determinar a antecipação ou o encerramento do direito de compra das ações.

Quando ocorre alienação de controle, por exemplo, alguns planos definem que os beneficiários podem comprar as ações referentes às opções maduras e exercer o direito de venda conjunta com o controlador, pois possui regras de tag along. Alguns planos, um pouco mais generosos em sua estrutura, permitem que os beneficiários adquiram as ações referentes a todas as opções outorgadas, inclusive as ainda não maduras, para participarem da venda conjunta.

Em outros casos, os detentores de ações obtidas em decorrência do exercício de opções serão obrigados a realizar a venda conjunta das ações, no caso de ocorrência de alienação de controle, quando o plano possui regras de drag along.

Alguns planos condicionam a aquisição do direito de compra das ações na ocorrência de abertura de capital da companhia e consequente IPO² das ações.

Em outros casos, as regras do plano determinam que na ocorrência de fechamento de capital em uma OPA⁴ de totalidade das ações negociadas em bolsa, os beneficiários perderão o direito sobre as opções ainda não maduras, sendo que as maturadas devem ser exercidas antes da divulgação do fato relevante de interesse em aquisição de ações.

---

# 13.8 Despesas do plano de opções

No pronunciamento técnico, CPC 10 (Comitê de Pronunciamentos Contábeis), relativo a pagamento baseado em ações, estão definidas as regras de avaliação, divulgação e contabilização dos planos de opções de compra de ações.

Devemos entender que, o plano de opções de compra de ações é uma contrapartida a um serviço prestado pelo beneficiário do plano, que pode ser um funcionário, um conselheiro, ou um prestador de serviços.

Para a contabilidade, as opções devem ser avaliadas na data-base da outorga e o tratamento contábil deve ser feito a partir dessa data. Se for um liability plan, as opções deverão ser reavaliadas a cada publicação de balanço.

A empresa deverá reconhecer as despesas referentes aos serviços recebidos por meio do plano de opções à medida que esses serviços são prestados. Em contrapartida, a empresa outorgante das opções deve reconhecer o correspondente aumento no patrimônio líquido, se as opções se qualificarem como equity plan; se as opções forem provenientes de um liability plan, com liquidação em caixa, deverá reconhecer a contrapartida como um passivo.

Apesar do CPC 10 definir que o valor das opções deve ser determinado, primordialmente, pelo valor do serviço prestado, também reconhece que é muito difícil segregar o valor do serviço prestado por um executivo, referente ao stock option plan, inclusive porque ele também recebe salário e, talvez, bônus. Na maioria dos casos, na impossibilidade de avaliar o serviço, o pronunciamento do CPC 10 sugere calcular o valor justo das opções. Logo, a companhia deve mensurar o valor dos serviços que serão prestados, e pode fazer isso por meio do cálculo de fair value das opções de compra de ações.

O liability plan deve ser avaliado na data de outorga e em todas as datas de reporte subsequentes, enquanto que o equity plan deve ter o seu fair value

---

calculado apenas na data de outorga, e a despesa contabilizada a partir de então.

Existem empresas de consultoria especializadas nesses tipos de cálculos de fair value para dar apoio à administração da companhia. Inclusive, existem softwares para controle do estoque de opções.

# 13.8.1 Reconhecimento de opções com entrega de instrumentos patrimoniais

Quando houver entrega de ações, ou outros instrumentos patrimoniais, em um equity plan, a empresa deverá avaliar os serviços prestados em contrapartida pelas opções. Se não for possível mensurar os serviços – e geralmente não é – a empresa deverá calcular o fair value das opções concedidas e o correspondente aumento no patrimônio líquido da empresa. O fair value das opções deve ser mensurado tendo como data-base a data de outorga das opções. Em seguida, o valor deve ser reconhecido de forma gradativa até a data do direito adquirido, ou seja, até a data de maturação, proporcional ao tempo decorrido. A empresa deve reconhecer essa despesa mesmo que as opções não sejam exercidas.

No caso de cancelamento da opção, por um motivo que não seja o preço de mercado da ação, o reconhecimento deverá ser imediatamente acelerado.

No caso particular de uma opção na qual não se tenha um período de maturação e o direito de compra das ações seja imediatamente concedido, o valor das opções deve ser integralmente e imediatamente reconhecido.

Suponha que uma empresa decida reduzir o preço de exercício das opções, o fair value deverá ser recalculado na data da redução do strike, de tal forma que o valor referente ao benefício deva ser reconhecido a partir de então, se resultar em aumento de valor justo da opção.

---

# 13.8.2 Reconhecimento de opções com liquidação em caixa

Para opções de ações com liquidação em caixa, denominadas como liability plan, a empresa deverá realizar o cálculo de fair value na data de outorga, a cada data de reporte e na data de liquidação das opções. Esse valor, então, será lançado como um passivo e qualquer mudança no valor justo das opções deve ser reconhecida no resultado do período.

Da mesma forma que o caso anterior, a empresa deverá reconhecer o valor das opções, como contrapartida dos serviços prestados pelo funcionário, ao longo do período de vesting (maturação) da opção.

# 13.9 Divulgação do plano de opções

As notas explicativas da empresa devem servir de apoio para os analistas de ações avaliarem o stock option plan da companhia. As informações contidas nas notas explicativas devem ser suficientes para que os analistas possam avaliar o plano, tomando como base que eles vão mensurar o valor do plano utilizando um modelo conhecido de precificação de opções.

Em geral, nas notas explicativas devem conter uma breve explicação do plano, as motivações para a companhia ter adotado esse tipo de remuneração e a modalidade dos planos, equity ou liability plan, ou misto. Devem ser descritas também as regras gerais do plano. Deve ser apresentada uma tabela com as informações relativas ao movimento que ocorreu no estoque de opções durante o período do reporte, como apresentado no seguinte quadro:

Quadro 10.1 | Quadro de movimentação das opções

---

|  Início do período | Movimento  |
| --- | --- |
|  Início do período | Saldo inicial de opções em circulação  |
|  Durante o período | (+) Opções outorgadas  |
|   |  (-) Opções exercidas  |
|   |  (-) Opções expiradas  |
|   |  (-) Opções canceladas  |
|  Fim do período | Saldo final de opções em circulação  |
|   |  Saldo final de opções exercíveis  |

Fonte: Elaborado pelos autores.

A companhia deve informar o preço de exercício médio ponderado de cada uma das subdivisões do quadro anterior e se houve exercício de opções durante o período, deverá divulgar também o preço médio ponderado das ações da empresa referente aos exercícios de opções.

Adicionamente, relativo ao saldo de opções em circulação ao final do período, deverá informar o intervalo de preços de exercício das opções remanescentes, e o prazo médio da vida remanescente das opções.

Essas informações devem auxiliar o analista a avaliar, pelo menos de forma aproximada, o quanto a empresa deverá ter de dispêndios com o exercício do saldo remanescente de opções.

Em nota explicativa, a companhia deverá deixar explícito qual o modelo utilizado para o cálculo de *fair value* das opções e as premissas das variáveis de entrada do modelo referentes às opções outorgadas no período. As premissas que devem ser divulgadas são as seguintes:

a. preço médio da ação no período de outorga;
b. preço de exercício das opções;
c. volatilidade esperada, breve explicação de como foi feito o cálculo da volatilidade e o tamanho da amostra de retornos utilizada no cálculo de volatilidade histórica;
d. vida remanescente da opção;
e. dividendos esperados e a taxa de *dividend yield* esperada;
f. taxa de juros livre de risco projetada;

---

g. valor intrínseco das opções.

A companhia deve apresentar também o valor de despesas reconhecidas no período, referente às opções outorgadas no plano de opções, de forma que o analista de ações consiga segregar do resultado da companhia os valores referentes ao plano.

# 13.10 Cálculo de fair value das opções de compra de ações para executivos

Como mencionamos anteriormente, na ausência de possibilidade de avaliar o valor do serviço prestado, é possível determinar o valor justo das opções de compra de ações concedidos aos executivos.

Quando um plano de opções possui uma estrutura mais simplificada, com preço de exercício fixo, um período de maturação e outro de exercício, é possível adotar um modelo como o de Black e Scholes ou Merton (1973).

Geralmente, os planos de opções possuem regras de correção no preço de exercício, ou regras adicionais, dependentes do trajeto dos preços – path dependent – que geralmente impedem o uso desses modelos na forma tradicional. Em alguns casos, teremos de usar um método mais flexível, como a Simulação de Monte Carlo. Os modelos de precificação de opções foram detalhadamente explicados nos capítulos anteriores.

Ao avaliar qual o melhor modelo de precificação do plano, teremos de considerar que existe uma probabilidade de abandono do plano e um fator de diluição das ações da companhia.

# 13.10.1 Cálculo da volatilidade para precificação de opções

---

# para executivos

Para o cálculo de fair value devemos considerar uma estimativa para a volatilidade.

O método de estimação mais utilizado é o cálculo da volatilidade com base em amostra histórica de retornos contínuos das cotações de fechamento das ações da companhia, a volatilidade é sempre expressa na base 252 dias úteis.

Deve-se calcular o desvio-padrão considerando uma distribuição de probabilidade uniforme, sem decaimento exponencial ou heterocedastidade, da forma mais trivial.

É possível calcular a volatilidade diretamente se as opções forem de uma companhia aberta com ações negociadas em bolsa, com uma amostra histórica de cotações disponível e liquidez diária. Na ausência de liquidez ou no caso de a companhia não possuir ações negociadas em bolsa, pode-se, alternativamente, utilizar um índice de ações setorial representativo do setor-econômico onde a empresa atua.

Se ainda não tivermos um índice de ações representativo, pode-se utilizar a cotação de ações de uma ou mais empresas, com liquidez em bolsa, do mesmo setor que a empresa atua.

Se mesmo assim não tivermos empresas que atuam no mesmo setor – geralmente isso ocorre com setores ainda não negociados em bolsa, porque a nossa bolsa é bem restrita no número de empresas negociadas – podemos utilizar um cálculo de volatilidade com base no CAPM.

# 13.10.2 Estimar volatilidade com base no CAPM

Essa metodologia utilizada para o cálculo da volatilidade utiliza como proxy a volatilidade do mercado, representado pela carteira teórica do IBOVESPA, ponderada por meio de um fator de ajuste. Com base na teoria do CAPM,

---

o risco de um ativo pode ser escrito por meio do seu beta, conforme Bodie, Kane e Marcus (2009, p. 281):



β = c o v (R _A , R _M)/sigma_M ² = rho_(A, M) sigma_A/sigma_M (1 0. 1)



Sendo:

β: beta da ação, representativo do risco sistemático da ação

rho_(A,M): correlação entre os retornos do mercado e os retornos da ação

sigma_A: volatilidade da ação

sigma_M: volatilidade do mercado, representada pela volatilidade do IBOVESPA

O fator de ajuste da volatilidade k pode ser escrito, portanto, dividindo-se o beta pela correlação entre ação e o mercado:



k = β/rho_(A , M),  logo  Z sim N (0, 1) (1 0. 2)



O fator de ajuste da volatilidade deve ser obtido por meio do beta das ações do setor no qual a companhia atua. Por exemplo, um fator de volatilidade calculado que resultou no valor 1,56 equivale dizer que, no período analisado, a volatilidade da companhia foi 56% superior à volatilidade do mercado. Apenas para exemplificar, a tabela a seguir contém os betas do setor de Computer software and services obtidos a partir do mercado norte-americano de ações:

Tabela 10.3 | Exemplo de beta setorial – Computer software and services

|  Ano | Beta  |
| --- | --- |
|  2011 | 1,06  |
|  2012 | 1,04  |

---

2013 0,98
2014 0,92

Fonte: Elaborada pelos autores.

A volatilidade histórica pode ser calculada com base no desvio-padrão amostral dos retornos contínuos das cotações diárias. A volatilidade expressa em base diária pode ser convertida para a base anual pela seguinte relação:



sigma_(anual) = sigma_(diária) √(252)   (10.3)



Sendo:

sigma_(anual): volatilidade anual

sigma_(diária): volatilidade por dia útil (assume-se um ano de 252 dias úteis)

Sugerimos também que a série histórica de dados a ser analisada – janela temporal – para estimação da volatilidade futura esperada pode ser igual ao prazo T da opção a qual será aplicada na precificação. Exemplificando, se o prazo da opção é de dois anos, devem ser utilizados os preços diários do ativo observados nos dois anos passados que antecedem a data-base da avaliação.

# 13.10.3 Fator de diluição

O modelo tradicional de precificação de opções é válido para a precificação de opções sobre ações já em circulação no mercado secundário, enquanto opções de executivos de equity plans implicam emissão de novas ações ou cessão de ações em tesouraria pela companhia, ou seja, em mercado primário de ações. Neste caso, podemos considerar que o prêmio de uma

---

opção sobre ação primária é similar ao preço da opção sobre ação secundária, multiplicado pelo seguinte fator de diluição do capital:



F_d = N/N + M   (10.4)



Sendo:

- F_d: fator de diluição do capital a ser aplicado ao preço calculado da opção
- N: número corrente de ações da empresa em poder do mercado
- M: número de ações emitidas em decorrência do exercício das opções de compra

Se a opção for decorrente de um liability plan, não haverá efeito de diluição, pois a liquidação será feita em caixa.

# 13.10.4 Taxa de abandono esperada do plano

Os executivos perdem o direito de exercício das opções caso ocorram eventos como falecimento, demissão ou desligamento da companhia a pedido. Não se pode considerar como abandono a desistência de exercício por conta da ação no mercado, ou seja, quando a opção "vira pó", porque esse evento já está precificado na opção. A taxa de abandono de direitos (forfeiting) deve ser considerada igual à taxa histórica para efeito de avaliação das opções. O fair value da opção, nesse caso, será o valor calculado da opção, multiplicado pelo coeficiente de abandono, da seguinte forma:



F_V = C(1 - a)   (10.5)



---

Sendo:

F_c: fair value da opção

c: valor calculado da opção, já considerando o efeito de diluição, se houver

(1 - a): coeficiente de abandono, sendo a a taxa de abandono histórica

# 13.10.5 Prazo esperado de exercício de compra da ação

A opção pode ser exercida até a data de vencimento, durante todo o período de exercício. Sendo assim, a opção possui característica do tipo americana, pois o beneficiário pode exercer o direito de compra da ação a qualquer momento até o vencimento da opção, a partir da data de maturação e após o término do período de vesting.

Nesse caso, deve-se considerar, para fins de precificação, que o prazo esperado de exercício da opção será igual ao prazo médio histórico obtido pela amostra de exercício do direito de compra de ações exercidas pelos executivos da companhia, ocorrido durante o período de maturação. Na ausência de amostra histórica desse tipo de evento, deve-se considerar o prazo total de exercício da opção, pois considera-se que o executivo pode esperar até o último dia da vida da opção para tomar sua decisão. Quanto maior o prazo considerado para fins de precificação, maior será o fair value da opção.

# RESUMO

Neste capítulo, abordamos um tema pouco tratado na literatura nacional. Vimos que as opções para executivos são uma forma de remuneração baseada em ações, utilizadas como mecanismo de atração e retenção de pessoas importantes para a companhia. O plano de opções de compra de ações tem como objetivo alinhar os interesses dos administradores, dos beneficiários do plano, com os interesses dos acionistas e mitigar o conflito de agência, ao vincular os ganhos desses administradores com o aumento de valor da ação da companhia. Neste capítulo,

---

mostramos as peculiaridades das opções para executivos em relação às opções vistas em capítulos anteriores.

# EXERCÍCIOS PROPOSTOS

1. Quais as diferenças entre o equity plan e os liability plans?
2. Quais as diferenças entre os planos de opções primários e secundários?
3. O que é o período de vesting?
4. O que é o instrumento de outorga?
5. O que é o graded vesting award?
6. Quais os procedimentos para o beneficiário do plano para exercer as opções?
7. O que é o termo de exercício?
8. Quais os benefícios dos planos de opções para executivos do ponto de vista do funcionário?
9. Em quais circunstâncias os planos de opções para executivos não são atrativos para o funcionário?
10. Quais os benefícios dos planos de opções para executivos do ponto de vista do empregador?

1 Ebitda – Earnings before interest, taxes, depreciation, and amortization.
2 Ebit – Earnings before interest, and taxes.

---

3 IPO – Initial Public Offering.
4 OPA – Oferta Pública de Aquisição de Ações.

---

# REFERÊNCIAS

BENIRSCHKA, M.; BINKLEY, J. K. Optimal storage and marketing over space and time. *American Journal of Agricultural Economics*. v. 77, n. 3, p. 512-524, Aug. 1995.

BLACK, F. The pricing of commodity contracts. *Journal of Financial Economics*. v. 3, p. 167-179, Mar. 1976.

BLACK, F.; SCHOLES, M. S. The pricing of options and corporate liabilities. *Journal of Political Economy*. v. 81, n. 3, p. 637-654, May. 1973.

BODIE, Z.; KANE A.; MARCUS, A. J. *Investments*. 8th. ed. New York: McGraw-Hill Irwin, 2009.

BRENNAN, M. J.; SCHWARTZ, E. S. Evaluating natural resource investments. *The Journal of Business*. v. 58, n. 2, p. 135-157, Apr. 1985.

COCHRANE, J. H. *Asset pricing*. New Jersey: Princeton, 2005.

COPELAND, T. E.; ANTIKAROV, V. *Opções reais: um novo paradigma para reinventar a avaliação de investimentos*. Tradução Maria José Cyhlar. Rio de Janeiro: Campus, 2001.

COPELAND, T. E.; WESTON, J.F. *Financial theory and corporate policy*. 3. ed. New York: Addison Wesley, 1988.

DUSAK, K. Futures trading and investor returns: an investigation of commodity market risk premiums. *The Journal of Political Economy*. v. 81, n. 6, p. 1387-1406, Nov. 1973.

ENDERS, W. *Applied econometric time series*. 2. ed. New Jersey: Wiley, 2004.

FRANZÉN, D.; SJOHOLM, O. *Credit Valuation Adjustment: In theory and practice*. 2014. Thesis (Master of Science)– Royal Institute of Technology, Stockholm, 2014.

FRECHETTE, D. L.; FACKLER, P. L. What causes commodity price backwardation? *American Journal of Agricultural Economics*. v. 81, n. 4, p. 761-771, Nov. 1999.

GALDI, F. C.; PEREIRA, L. M. Value at risk using volatility forecasting models: EWMA, GARCH and stochastic volatility. *Brazilian Business Review*. v. 4, n. 1, p. 74-94, Jan. 2007.

GASTINEAU, G. L. *The options manual*, 3. ed. New York: McGraw-Hill, 1979.

GEMAN, H. *Commodities and commodity derivatives: modeling and pricing for agriculturals, metals and energy*. Chichester: Wiley, 2005.

GIBSON, R.; SCHWARTZ, E. S. Stochastic convenience yield and the pricing of oil contingent claims. *The Journal of Finance*. v. 45, n. 3, p. 959-976, July. 1990.

GREENE, W. H. *Econometric analysis*. 5. ed. New Jersey: Prentice Hall, 2003.

HAMILTON, J. D. *Time series analysis*. New Jersey: Princeton, 1994.

HAUG, E. G. *The complete guide to option pricing formulas*. New York: McGraw-Hill Education, 2007.

HULL, J. C. *Opções, futuros e outros derivativos*. Tradução Bolsa de Mercadorias & Futuros. 3. ed. São Paulo: Bolsa de Mercadorias & Futuros, 1998.

____. *Options, futures, and other derivatives*. 8th. ed. New Jersey: Prentice Hall, 2012.

HULL, J. C.; WHITE, A. LIBOR vs. OIS: The derivatives discounting dilemma. *Journal of Investment Management*. v. 11, n. 3, p. 14-27, Apr. 2013.

---

HULL, John; WHITE, Alan. The FVA debate. Risk, v. 25, n. 7, p. 83-85, 2012.

ITÔ, K. On stochastic differential equations. Memoirs of the American Mathematical Society. v. 4, n. 1, p. 1-51, 1951.

JENSEN, M. C. The performance of mutual funds in the period 1945-1964. The Journal of finance. v. 23, n. 2, p. 389-416, 1968.

JOHNSON, L. L. The theory of heging and speculation in commodity futures. The Review of Economic Studies. v. 27, n. 3, p. 139-151, June. 1960.

KALDOR, N. Speculation and economic stability. The Review of Economic Studies. v. 7, n. 1, p. 1-27, Oct. 1939.

LITZENBERGER, R. H.; RABINOWITZ, N. Backwardation in oil futures markets: theory and empirical evidence. The Journal of Finance. v. 50, n. 5, p. 1517-1545, Dec. 1995.

MCDONALD, R.; PAULSON, A. AIG in Hindsight. Journal of Economic Perspectives, Pittsburgh, v. 29, n. 2, p. 81-106, Spring 2015.

MERTON, R. C. Theory of rational option pricing. The Bell Journal of Economics and Management Science. v. 4, n. 1, p. 141-183, Spring. 1973.

MORETTIN, P. A.; TOLOI, C. M. C. Análise de séries temporais. 2. ed. São Paulo: Edgar Blücher, 2006.

PEREIRA, L. M.; RIBEIRO, C. O.; SECURATO, J. R. Agricultural commodities pricing model applied to the Brazilian sugar market. Australian Journal of Agricultural and Resource Economics, v. 56, n. 4, p. 542-557, 2012.

PYKHTIN, Michael; ROSEN, Dan. Pricing counterparty risk at the trade level and CVA allocations. 2010.

REINER, E.; RUBINSTEIN, M. Breaking down the barriers. Risk, v. 4, n. 8, p. 28-35, 1991.

RUIZ, I. XVA Desks – A New Era for Risk Management: Understanding, Building and Managing Counterparty, Funding and Capital Risk. Basingstoke: Palgrave Macmillan, 2015.

SCHOUCHANA, F.; MICELI, W. M. Introdução aos mercados futuros e de opções agropecuárias no Brasil. 3. ed. São Paulo: Bolsa de Mercadorias & Futuros, 2004.

SCHWARTZ, E. S. The stochastic behavior of commodity prices: implications for valuation and hedging. The Journal of Finance. v. 52, n. 3, p. 923-973, July. 1997.

SCHWARTZ, E. S.; SMITH, J. E. Short-term variations and long-term dynamics in commodity prices. Management Science. v. 46, n. 7, p. 893-911, July. 2000.

SECURATO, J. R. Decisões financeiras em condições de risco. São Paulo: Atlas, 1996.

SMITH JR, C. W.; STULTZ, R. M. The Determinants of Firms' Hedging Policies. Journal of Financial and Quantitative Analysis, vol. 20, issue 4, 391-405, 1985

SORENSEN, C. Modeling seasonality in agricultural commodity futures. The Journal of Futures Markets. v. 22, n. 5, p. 393-426, Mar. 2002.

VIEIRA NETO, Cícero A.; URBAN, Fábio. Um modelo de teste de stress menos subjetivo e mais abrangente. Finance Lab, Insper Instituto de Ensino e Pesquisa, 2000.

WALRAS, L. Elements of pure economics: or the theory of social wealth. Tradução William Jaffe. London: Routledge, 2003.

---

WILMOTT, P. Derivatives: the theory and practice of financial engineering. Chichester: John Wiley, 1998.

WORKING, H. Theory of the inverse carrying charge in futures markets. Journal of Farm Economics. v. 30, n. 1, p. 1-28, Feb. 1948.

---

ANEXO A

# Processo ARMA/GARCH para volatilidade heterocedástica

Anexo A – Processo ARMA/GARCH para volatilidade heterocedástica

Para poder adotar um processo GARCH é necessário testar a hipótese de que a volatilidade do mercado siga um processo heterocedástico, ou seja, que a variância possa ser diferente para qualquer tempo t. Para identificar a presença de processo GARCH na série, deve ser aplicada a estatística Q Ljung-Box no correlograma dos resíduos quadráticos resultantes de uma regressão ARMA dos retornos do ativo-objeto.

## Estimando o Modelo ARMA

Um processo GARCH é utilizado em séries econômicas que apresentem volatilidade elevada, seguida por períodos de tranquilidade. Nesses casos, é inapropriado assumir volatilidade constante. Um modelo do tipo GARCH consegue captar a trajetória da volatilidade no tempo, por meio da regressão dos resíduos quadráticos de um modelo autorregressivo ARMA. Esses dois modelos, ARMA / GARCH, apesar de serem diferentes, têm seus parâmetros estimados simultaneamente, pela minimização da soma dos resíduos quadráticos de uma regressão MQO. A equação seguinte é de modelo ARMA de ordem um, AR(1):



y_t = varphi_0 + varphi_1 y_(t-1) + v_t   (A.1)



Sendo:

- y_t: retorno do ativo no tempo t
- v_t: resíduo da regressão no tempo t, com variância igual a sigma_v^2
- varphi_0, varphi_1: coeficientes lineares do processo AR(1)

## Teste Q Ljung Box de autocorrelação dos resíduos quadráticos

Os resíduos resultantes da regressão ARMA são testados para identificar a presença de um processo GARCH na série. Segundo Enders (2004, p. 119), devem-se

---

calcular as autocor-relações dos resíduos quadráticos, para defasagens i = 1, 2, 3, ..., da seguinte forma:



rhoᵢ = Σ(t=+1 até N) (v_t² - sigma_v²) (v_(t-t)² - sigma_v²)/Σ(i=1 até N) (v_t² - sigma_v²)²   (A.2)



Sendo:

rhoᵢ: autocorrelação dos resíduos quadráticos para a defasagem i

N: número de resíduos da série

v_t²: resíduo quadrático resultante do processo ARMA (p, q)

sigma_v²: variância dos resíduos v_t

Os valores da correlação rhoᵢ significativamente diferentes de zero indicam a presença de um processo GARCH; rejeitar a hipótese nula de que v_t² são serialmente não correlacionados é equivalente a rejeitar a hipótese nula de ausência de processo GARCH. O teste utilizado para verificar a hipótese é a estatística Q Ljung Box, que possui uma distribuição chi², com n graus de liberdade, conforme a seguinte equação:



Q = N (N + 2) Σ(i=1 até n) rhoᵢ / (N - i)   (A.3)



## Especificação do processo GARCH

A variável de interesse é a volatilidade condicional do ativo um passo à frente σ̂_t, que pode ser obtida por meio da modelagem dos resíduos v_t resultantes da regressão ARMA dos retornos do preço do ativo. A volatilidade condicional é obtida por meio dos resíduos quadráticos condicionais, conforme a seguinte equação:



σ̂_(t(t-1)) = √{v̂_(sigma_(t-1))²}   (A.4)



Sendo:

σ̂_t: volatilidade condicional em t

v̂_(sigma_(t-1)): resíduo condicional

O resíduo condicional esperado v̂_(sigma_(t-1)) pode ser calculado pela variância condicional h_t, tal que v̂_(sigma_(t-1)) = √{h_t}. A seguir está a equação que descreve a variância condicional h_t, resultante de um processo GARCH (1,1):



h_t = alpha₀ + alpha₁ v_(t-1)² + beta₁ h_(t-1)   (A.5)



Sendo:

h_t: variância condicional no tempo t

---

alpha_0, alpha_1: coeficientes lineares do processo GARCH (1,1)

Após obter a variância condicional, calcula-se a volatilidade varphi_(condicional), que será utilizada no modelo de precificação de opções.
