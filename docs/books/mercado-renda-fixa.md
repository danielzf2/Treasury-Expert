---
title: "O Mercado de Renda Fixa no Brasil"
source_pdf: "O Mercado de Renda Fixa no Brasil.pdf"
converter: "mistral-ocr-latest"
date_converted: "2026-03-27T18:51:09Z"
category: "books"
sanitized: true
reviewed: false
---
JOSÉ MONTEIRO VARANDA NETO

JOSÉ CARLOS DE SOUZA SANTOS

EDUARDO MORATO MELLO

# O MERCADO

# DE RENDA

# FIXA NO

# BRASIL

CONCEITOS,

PRECIFICAÇÃO

E RISCO

Saint Paul

Editora

---

# O Mercado de Renda
Fixa no Brasil

---

.

---

José Monteiro Varanda Neto
José Carlos de Souza Santos
Eduardo Morato Mello

# O Mercado de Renda
## Fixa no Brasil

Conceitos, precificação e risco

Saint Paul
Editora

---

.

---

© 2019 by Saint Paul Editora Ltda.

1ª Edição – 2019

Depósito legal na Biblioteca Nacional conforme Decreto n. 1.825, de 20 de dezembro de 1907.

Todos os Direitos Reservados – É proibida a reprodução total ou parcial de qualquer forma ou por qualquer meio. A violação dos direitos do autor (Lei n. 9.160/1998) é crime estabelecido pelo artigo 184 do Código Penal.

Coordenação editorial: José Cláudio Securato
Supervisora editorial: Deise Anne Rodrigues
Revisão: Bárbara Piloto Sincerre
Capa e Diagramação: Karina Tenório Silva
Imagem da capa: Freepik.com

Dados Internacionais de Catalogação na Publicação (CIP)
(Câmara Brasileira do Livro, SP, Brasil)

Varanda Neto, José Monteiro

O mercado de renda fixa no Brasil: conceitos, precificação e risco / José Monteiro Varanda Neto, José Carlos de Souza Santos, Eduardo Morato Mello. – São Paulo : Saint Paul Editora, 2019.

Bibliografia.

ISBN: 978-85-8004-149-1

1. Investimentos em renda fixa 2. Opções (Finanças) 3. Risco - Administração 4. Títulos de renda fixa 5. Valor (Economia) - Fatores de risco I. Santos, José Carlos de Souza. II. Mello, Eduardo Morato. III. Título.

19-24458

CDD-332.645

Índices para catálogo sistemático:

1. Brasil: Mercado de renda fixa: Taxa de juros: Economia 332.645

Saint Paul Editora Ltda.
R. Pamplona, n. 1616, portão 3, Jardim Paulista | São Paulo, SP | Brasil | CEP 01405-002
www.saintpaul.com.br | editora@saintpaul.com.br
Saint Paul Editora Ltda. é uma empresa do Grupo Saint Paul Institute of Finance S. P. Ltda.

Os autores deste livro são os exclusivos responsáveis por seu conteúdo, bem como pelas opiniões neste expressas, as quais refletem

---

seus posicionamentos. As visões, opiniões e conteúdo deste trabalho não refletem, necessariamente, o posicionamento de seus atuais ou ex-empregadores, os quais não tiveram nenhum envolvimento, contribuição ou participação, seja direta ou indiretamente, na elaboração deste trabalho, de modo que não poderá os comprometer. Os exemplos contidos neste livro foram preparados e apresentados para fins exclusivamente didáticos, tendo por objetivo a fixação da teoria apresentada. Sendo assim, de maneira nenhuma deverão ser interpretados com o objetivo de sugerir ao leitor que aplique as estratégias ipsis litteris, pois outras variáveis devem ser consideradas, tais quais, mas não se limitando, as condições de mercado, spreads, taxas e impostos.

---

Agradecimentos

Várias pessoas nos ajudaram na produção deste livro. Gostaríamos de agradecer ao Ricardo Pires S. Santos por ler e comentar diversas partes do texto e ao Rubem Mendonça Pimentel por nos conceder explicações sobre *swaps* no mercado internacional. O Renato Uzun nos auxiliou na montagem das planilhas de cálculo de debêntures, sendo estas muito úteis para o entendimento e para a validação dos cálculos de precificação e marcação a mercado. O Prof. Dr. Leonel Molero, gentilmente, cedeu material referente ao *swap* de Libor. À equipe da editora Saint Paul, que realizou um trabalho de editoração excelente e minucioso. A todos os nossos agradecimentos, isentando-os, naturalmente, de erros e omissões remanescentes.

---

# Sumário

## Apresentação

### CAPÍTULO 1

Conceitos gerais sobre renda fixa

- 1.1 Definição de renda fixa
- 1.2 Títulos
- 1.3 Investidores (credores)
- 1.4 Emissores (devedores)

### CAPÍTULO 2

Ferramental básico para o cálculo de títulos de renda fixa

- 2.1 Esquemas de amortização
- 2.2 Taxas de juros
- 2.3 Precificação de títulos ao valor de mercado e na curva
- Exercícios propostos

### CAPÍTULO 3

Rentabilidade de títulos de renda fixa

- 3.1 Retorno de títulos sem cupom de juros
- 3.2 Retorno de títulos com pagamento de cupons
- Exercícios propostos

### CAPÍTULO 4

Estrutura a termo de taxas de juros (ETTJ)

- 4.1 Definição
- 4.2 Taxa DI versus taxa Selic
- 4.3 Formação das taxas de juros
- Exercícios propostos

### CAPÍTULO 5

Técnicas de estimação da ETTJ

- 5.1 Conceito de interpolação
- 5.2 Flat forward exponencial
- 5.3 Interpolação linear
- 5.4 Interpolação por cubic spline
- 5.5 Outras técnicas de estimação da ETTJ
- Exercícios propostos

---

CAPÍTULO 6

Títulos públicos federais brasileiros

6.1 Definição
6.2 Precificação

Exercícios propostos

CAPÍTULO 7

Precificação de títulos de dívida externa brasileira

7.1 Definição
7.2 Global bonds
7.3 Precificação de global bonds

CAPÍTULO 8

Títulos privados

8.1 Definição
8.2 Certificados de depósitos
8.3 Debêntures

CAPÍTULO 9

Introdução ao risco de mercado em títulos de renda fixa

9.1 Risco pré
9.2 Spreads de crédito/liquidez
9.3 G-Spread
9.4 Z-Spread

CAPÍTULO 10

O cálculo do spread de crédito

10.1 Spread sobre a curva pré da B3

CAPÍTULO 11

Arbitragem entre instrumentos de renda fixa

11.1 Instrumentos de captação em instituições financeiras
11.2 Arbitragem entre indexadores
11.3 Arbitragem entre instrumentos via diferença de tributação
11.4 Taxa nominal e real líquidas

CAPÍTULO 12

Duration e convexidade

12.1 Hipóteses

---

12.2 Modelagem da duration
12.3 Duration de Macaulay
12.4 Duration modificada
12.5 Convexidade

Exercícios propostos

CAPÍTULO 13

Derivativos de taxas de juros: futuros

13.1 Introdução aos derivativos
13.2 Contratos futuros
13.3 Contrato futuro de DI
13.4 Contrato futuro de DDI
13.5 Contrato futuro de dólar
13.6 Paridade descoberta de taxas de juros
13.7 Paridade coberta das taxas de juros

CAPÍTULO 14

Derivativos de taxas de juros: swaps

14.1 Definição
14.2 Principais modalidades de swap locais
14.3 O swap libor x fixed

CAPÍTULO 15

Bootstrapping

15.1 Definição
15.2 Motivação para o uso do bootstrapping
15.3 O procedimento do bootstrapping
15.4 Implementação do bootstrapping na prática

Exercícios propostos

CAPÍTULO 16

Imunização e hedge de carteiras de renda fixa

16.1 Definição de imunização
16.2 Equação de imunização pela duration
16.3 Hedge
16.4 Hedge de fluxo de caixa
16.5 Imunização de uma carteira de títulos prefixados via DI futuro

CAPÍTULO 17

---

VaR de renda fixa

17.1 Definição
17.2 O VaR paramétrico
17.3 Resumindo a carteira de renda fixa pelos vértices
17.4 Estimação das volatilidades
17.5 A matriz de variância-covariância
17.6 O cálculo do VaR de renda fixa
17.7 O cálculo do VaR de acordo com a carta-circular N. 3.498 do Bacen
Exercícios propostos

CAPÍTULO 18

O risco de crédito de uma carteira de renda fixa

18.1 Definição
18.2 Fundamentos para mensuração
18.3 Estimação da perda esperada de uma carteira prefixada
18.4 Estimação da distribuição das perdas esperadas de uma carteira
18.5 Introduzindo o spread de crédito no VaR
Exercícios propostos

CAPÍTULO 19

O risco pré em operações com percentual do DI

19.1 Utilização do percentual do DI
19.2 Duration de uma exposição em percentual do DI
19.3 Inclusão do percentual do DI no modelo de VaR
19.4 Alternativa à forma algébrica com a utilização do DVO1
19.5 Oscilação da capacidade de crédito da contraparte
19.6 Derivação da duration de uma exposição em percentual de DI

Conclusão

Extra: Exercícios avançados resolvidos

Referências

Apêndice A

A.1 Conceito de total return pelas quotas
A.2 Duration do portfólio em função da duration dos títulos que o compõem
A.3 Hedge de um portfólio com duration e convexidade
A.4 Capitalização contínua
A.5 Valorização de fundos de investimento
A.6 Imposto de renda em fundo de investimento

---

A.7 Gross up de imposto de renda em fundos de investimento
A.8 Butterfly com futuros de DI ou trava de FRA de três pontas

Glossário com termos traduzidos do inglês

---

# Apresentação

O texto desta obra foi criado com base em apostilas e materiais de aulas de disciplinas que ministramos em cursos de pós-graduação, que eram distribuídos aos alunos como material auxiliar no entendimento dos assuntos discutidos, facilitando a consolidação do conteúdo visto em aula, e suprindo uma lacuna na literatura sobre renda fixa brasileira.

Este trabalho trata de temas ligados, principalmente, ao universo de renda fixa e de derivativos de renda fixa lineares no mercado brasileiro, em reais e em dólares, abordando temas como precificação, cálculo de risco, desempenho e hedge.

O livro traz exemplos numéricos para ilustrar conceitos teóricos mais complexos, com a preocupação de estabelecer conexão entre a teoria e a prática.

É uma iniciativa para que os alunos tenham uma fonte e alternativa de pesquisa consolidada em um livro para consulta, antes de enveredarem por artigos científicos ou livros mais densos, como a bibliografia indicada ao final do texto.

É um livro aplicado ao mercado de renda fixa brasileiro, que, como professores de renda fixa que somos, verificamos essa lacuna por não haver material disponível do tema aos nossos alunos.

A seção Apêndice A contém demonstrações matemáticas referentes a algumas operações e procedimentos ou estratégias do mercado financeiro citados, rapidamente, ao longo do texto.

Aproveitem a leitura.

---

# Capítulo 1
Conceitos gerais sobre renda fixa

Antes de iniciar o estudo mais aprofundado de renda fixa e derivativos de taxas de juros é necessário apresentar alguns conceitos básicos. Ao longo do texto outros serão introduzidos, sempre que possível com a utilização de exemplos numéricos.

## 1.1 Definição de renda fixa

Renda fixa é um tipo de investimento em que rendimentos reais, nominais ou indexados às taxas flutuantes são recebidos em intervalos de tempo regulares e definidos em documentos formais.

## 1.2 Títulos

O investimento mais comum de renda fixa é o título. Os títulos são emitidos pelos governos federais, municipais – mais comuns nos Estados Unidos, instituições financeiras e empresas não financeiras.

Possuem como característica fundamental de poderem ser negociados no mercado secundário, uma vez que têm a menor fração divisível (unidade) com valores acessíveis a maior parte dos investidores, como pode ser visto na plataforma tesouro direto do Tesouro Nacional¹, em que, inclusive, os valores unitários dos títulos têm a possibilidade de serem fracionados para aquisição do investidor.

Essa pulverização que os títulos apresentam conferem maior liquidez a eles, ou seja, mais facilidade de trocar de mãos, que outros instrumentos de dívida, como empréstimos, por exemplo.

## 1.3 Investidores (credores)

Os investidores são credores dos emissores dos títulos e, em troca de remuneração, ou juros, emprestam seus recursos, temporariamente, a um tomador.

O investidor não é obrigado a manter o título em carteira durante todo o

---

período de vigência deste, basta vendê-lo no mercado secundário sempre que lhe convier.

## 1.4 Emissores (devedores)

Os emissores de títulos oferecem um fluxo futuro de recursos em troca de um adiantamento financeiro. Trata-se de uma modalidade de empréstimo, porém com vários credores espalhados pelo mercado.

Essa estrutura permite, em tese, que uma quantidade maior de recursos seja levantada por um custo inferior ao que se conseguiria se, em vez de utilizar um título, fossem solicitados empréstimos diretamente às instituições financeiras.

A emissão de um título bem como a abertura de capital de uma companhia é realizada com a assessoria de bancos de investimento, o que também envolve custos de subscrição.

Na hipótese de um evento de inadimplência da companhia emissora, os credores têm preferência legal de receber seus recursos sobre os acionistas ou donos da companhia, que, nessa situação, podem perder todo o recurso investido.

|  Resumo  |
| --- |
|  Este capítulo aborda conceitos gerais sobre renda fixa, tais como a definição de renda fixa e títulos e o papel dos devedores e emissores.  |

1 TESOURO DIRETO. Tesouro Nacional. Disponível em: <http: tesouro-direto="" www.tesouro.fazenda.gov.br="">. Acesso em: 12 dez. 2018.</http:>

---

# Capúulo 2

Ferramental básico para o cálculo de títulos de renda fixa

## 2.1 Esquemas de amortização

Há vários esquemas de amortização. No Brasil, são bem comuns a tabela Price, o sistema SAC e o Sistema Americano. Em todos eles, os juros são exponenciais e o devedor paga juros sobre juros e amortização. O que varia é como ele serve os juros e liquida o principal ao longo do tempo.

Na tabela Price, as parcelas são iguais. É o sistema utilizado no Brasil em empréstimos pessoais (aquisição de veículos, por exemplo).

No sistema SAC, as amortizações são iguais. É o sistema utilizado em financiamentos habitacionais.

Neste livro, teremos como enfoque o Sistema Americano.

No Sistema Americano, existem fluxos de caixa pagos periodicamente ao credor até o vencimento do título, sendo a semestralidade a periodicidade mais comum. A taxa de juros contratual desses pagamentos periódicos, definida na emissão do título, define o montante desses fluxos de caixa periódicos ou cupons de juros.

> O termo cupom de juros tem origem na época em que os títulos eram em papel. Esses títulos continham cupons destacáveis, que eram destacados pelos detentores dos títulos para serem trocados por dinheiro nas datas e termos especificados na emissão do título.

Além dos cupons de juros, existe o valor de face, que é o valor no qual os juros incorrerão ao longo do período do título. Esse valor é equivalente ao principal do título, uma vez que nesse sistema não existem amortizações (pagamentos do principal) periódicas, como em debêntures. No Sistema Americano, a amortização é feita em uma única vez, no vencimento do título.

A figura a seguir ilustra os fluxos de pagamento de um título emitido de

---

acordo com o Sistema Americano, com principal de R$ 100 e taxa de cupom fixa de 3% ao ano – o que representa pagamentos periódicos de R$ 3 pelo emissor –, vencendo em sete anos. Observe que o último fluxo de caixa contém o pagamento do principal mais o último pagamento de cupom de juros.

Figura 2.1 – Sistema Americano com cupom fixo de 3% a. a.
![img-0.jpeg](img-0.jpeg)
Fonte: Elaborada pelos autores.

Adiante, aprenderemos a precificar títulos com essa característica.

## 2.2 Taxas de juros

Taxa de juros é o que define o valor do custo do dinheiro no tempo, expresso como um percentual em relação a um valor de referência, como o capital investido ou o principal do título.

Dessa maneira, ela fornece a velocidade com que um montante cresce ao longo do tempo, daí que é expressa em um percentual por unidade de tempo.

Essa unidade de tempo pode ser o dia, o mês, o período e, mais comumente, o ano.

É importante não confundir o intervalo para o qual a taxa é cotada com o prazo de capitalização, por exemplo, a taxa DI é cotada em percentual ao ano, porém ela é convertida em um fator de capitalização diário e aplicada ao principal todos os dias.

> O fator de capitalização é obtido quando somamos “1” à taxa de juros, ponderando pelo tempo. Por exemplo, assumindo juros compostos, o fator de capitalização é obtido por (1+i)^t. Ou, se assumirmos juros simples, (1+i× t), sendo i a taxa de juros e t o prazo. Desta forma, para corrigir o valor de referência do título basta multiplicá-lo pelo fator de capitalização acumulado no período.

## 2.2.1 Exemplo: montante da dívida em função do fator de capitalização

O montante de uma dívida é o valor corrigido do empréstimo pelos juros

---

incorridos até um determinado prazo ou liquidação do empréstimo.

Vamos calcular o montante corrigido de um empréstimo com as seguintes características:

- Principal (ou valor emprestado): R$ 100.000,00
- Prazo: 1 dia útil
- Correção: taxa DI da Central de custódia e liquidação financeira de títulos (Cetip)

Vamos assumir também que a taxa DI apurada foi de 6,39% a. a.

Qual será o valor que a contraparte nos pagará na liquidação do empréstimo?

Podemos calcular o fator de capitalização conforme observado a seguir:



(1 + 6,39\%  a.a.)^(1/252) = 1,00024583



Observe que como a taxa de juros do DI está dada na forma anual, precisamos converter o prazo t na forma anual também, por isso dividimos 1 dia útil por 252 dias úteis.

Agora, podemos calcular o montante da dívida bastando corrigir o valor emprestado pelo fator de capitalização:



R\100.000,00 × 1,00024583 = R\100.024,58



Veremos que o fator de capitalização será muito conveniente no cálculo dos montantes tanto dos títulos privados quanto dos swaps de Libor.

## 2.2.2 Conversão de taxas

Converter taxas é alterar o prazo de referência para o qual essas são cotadas.

Por exemplo, pode-se querer apresentar uma taxa semestral em forma de taxa anual e vice-versa.

Para fazer isso, basta relacionar quantos períodos de um período "cabem" no outro, por exemplo, convertendo taxa semestral para anual, em capitalização composta:



(1 + i_a)^2 = (1 + i_a) 



---

## 2.2.3 Exemplo: cálculo de conversão de taxa

Uma taxa de cupom de 10% a. a. equivale a que taxa semestral em capitalização composta?



(1 + i_s)^2 = (1 + 10\%)





i_s = √(1,1) - 1 = 4,88\%  a. s.



Como existem dois semestres em um ano, a taxa semestral é capitalizada duas vezes para se obter a taxa anual.

## 2.2.4 Exemplo: cálculo de conversão de taxa (252 dias úteis)

Da mesma forma, se quisermos obter a taxa anual a partir da taxa diária:



(1 + i_d)^(252) = (1 + i_a) 



Note que em um ano tem 252 dias úteis na convenção do mercado financeiro brasileiro. Assim, como são 252 dias úteis em um ano, para obter a taxa anual equivalente a uma dada taxa diária, nós a capitalizamos 252 vezes.

Uma taxa anual de 10% a. a. equivale a que taxa diária?



(1 + i_d)^(252) = (1 + 10\%)



Elevando os dois lados da equação por 1/252:



[(1 + i_d)^(252)]^(1/252) = (1 + 10\%)^(1/252)



Desta forma, livramo-nos do expoente do lado esquerdo da equação, permitindo isolar a nossa incógnita:



i_d = 1,1^(1/252) - 1 = 0,0378\%  a. d.



## 2.2.5 Taxa interna de retorno (TIR)

A TIR é um conceito muito utilizado em avaliação de projetos de investimento², servindo como um dos indicadores utilizados para tomar a decisão sobre a aceitação do projeto ou não.

A partir de um dado fluxo de caixa originado pelas estimativas de custo versus receita oriundos do projeto de implantação de um negócio é possível gerar um número que mede a rentabilidade desse projeto.

---

Esse número é a TIR e ele é calculado fazendo com que a soma dos fluxos de caixa descontados a ela seja igual a zero.

Matematicamente, temos de criar uma função f = f(y), em que:



f(y) = Σ(k=1 até n) FC_k/(1 + y)^k 



Onde:

f(y): corresponde ao preço ou a soma dos valores presentes dos fluxos de caixa descontados pela TIR

FC_k: é o valor do fluxo de caixa do prazo k

y: é a TIR ou Yield to maturity (YTM)

## 2.2.6 Exemplo: cálculo da TIR

Um projeto de negócio tem o seguinte fluxo de caixa projetado para os próximos cinco anos:

Figura 2.2 – Fluxo de caixa de um determinado projeto
![img-1.jpeg](img-1.jpeg)
Fonte: Elaborada pelos autores.

Então, criamos a função f = f(y), em que:



f(y) = Σ(k=1 até n) FC_k/(1 + y)^k



Substituindo com os dados do exemplo anterior, temos:



f(y) = -800/(1 + y)^9 + 300/(1 + y)^1 + 400/(1 + y)^3 + -200/(1 + y)^3 + 150/(1 + y)^4 + 500/(1 + y)^5



O gráfico dessa função é dado a seguir:

Gráfico 2.1 – f(y) ou Valor Presente Líquido

---

![img-2.jpeg](img-2.jpeg)
Fonte: Elaborado pelos autores.

Assim:

Quando f(y) → 0, y → TIR.

Ou seja, o valor da TIR é aquele em que o gráfico da função f(y) corta o eixo das abscissas.

O gráfico anterior é o resultado da plotagem da função f(y) para vários valores de taxas internas de retorno.

Tabela 2.1 – F(y) ou NPV em função das taxas (y)

|  y | f(y)  |
| --- | --- |
|  5% | 190,93  |
|  6% | 163,54  |
|  7% | 137,42  |
|  8% | 112,49  |
|  9% | 88,69  |
|  10% | 65,96  |
|  11% | 44,22  |
|  12% | 23,42  |
|  13% | 3,51  |
|  14% | -15,55  |
|  15% | -33,82  |
|  16% | -51,35  |
|  17% | -68,16  |
|  18% | -84,29  |
|  19% | -99,79  |
|  20% | -114,69  |
|  21% | -129,01  |
|  22% | -142,79  |

---

|  y | f(y)  |
| --- | --- |
|  23% | -156,05  |
|  24% | -168,82  |
|  25% | -181,12  |

Fonte: Elaborada pelos autores.

Examinando a Tabela 2.1. é possível verificar que o valor da TIR está entre os valores de 13% e 14% a. a., destacados em negrito.

Não existe solução analítica para uma equação como essa. O cálculo é feito por meio da utilização de algoritmos numéricos, como Newton-Raphson ou Bissecção, por exemplo.

Para nossas aplicações, utilizaremos o MS Excel e o adaptaremos para situações reais do mercado de títulos.

Tabela 2.2 – Resultado de y

|  t (anos) | FC | VP  |
| --- | --- | --- |
|  0 | -800 | -800,00  |
|  1 | 300 | 265,06  |
|  2 | 400 | 312,26  |
|  3 | -500 | -344,86  |
|  4 | 150 | 91,41  |
|  5 | 500 | 269,22  |
|   |  | -206,92  |
|   | y | 13,181%  |

Fonte: Elaborada pelos autores.

Em projetos de investimento, pode haver uma situação em que exista mais de uma TIR. Isso leva a uma indeterminação no método e a uma impossibilidade na utilização do processo.

Para avaliação de títulos de renda fixa, o gráfico sempre será monotônico, como o Gráfico 2.1., uma vez que só pagamos o título uma única vez, assim só existirá uma única TIR.

## 2.3 Precificação de títulos ao valor de mercado e na curva

Os agentes que utilizam os títulos de renda fixa para acumular sua poupança financeira têm de registrar o valor desses instrumentos ao longo

---

do tempo.

Fundos de investimento, bancos, fundos de pensão e seguradoras têm de seguir métodos contábeis para fazê-lo, obedecendo a legislação vigente.

De maneira geral, há duas formas de fazer isso:

1. Marcação a mercado: quando o valor do papel é contabilizado pela cotação atual em mercado. A ideia é refletir seu valor provável de realização, ou seja, caso o título fosse vendido no mercado.
2. Contabilização na curva: quando a entidade que detém o título tem a prerrogativa de contabilizar o papel pela taxa de juros de aquisição, ou seja, a TIR.

Os fundos de investimento e tesouraria de bancos marcarão o papel a mercado, ou seja, irão registrá-lo com preço equivalente ao seu valor no mercado.

Os fundos de pensão e os bancos comerciais têm a opção de contabilizar os papéis na curva, ou seja, utilizando a taxa de aquisição do papel. É o caso de títulos nos quais a instituição financeira define que manterá em carteira até o vencimento, sem intenção de negociá-los no mercado secundário.

A contabilização na curva segue a regra de amortização de qualquer instrumento que paga juros. A cada instante você tem um saldo devedor, um valor devido como amortização, uma despesa de juros (serviço da dívida) e o valor total da parcela, que é a soma das duas últimas.

## 2.3.1 Exemplo: cálculo da marcação a mercado de um título

Vamos supor que o título da tabela a seguir está sendo emitido, sem ágio ou deságio³. Como ficará o fluxo de amortização desse papel?

Tabela 2.3 – Esquema de amortização no Sistema Americano

|  t (anos) | Saldo devedor | Amortização | Juros | Parcela ou fluxos de caixa  |
| --- | --- | --- | --- | --- |
|  0 | 100 | 0 | 0 | 0  |
|  1 | 100 | 0 | 3 | 3  |
|  2 | 100 | 0 | 3 | 3  |
|  3 | 100 | 0 | 3 | 3  |
|  4 | 100 | 0 | 3 | 3  |
|  5 | 100 | 0 | 3 | 3  |

---

|  6 | 100 | 0 | 3 | 3  |
| --- | --- | --- | --- | --- |
|  7 | 0 | 100 | 3 | 103  |

Fonte: Elaborada pelos autores.

Há muitas informações interessantes na Tabela 2.3:

Você percebe que a amortização do título só é feita no vencimento e que o serviço da dívida – juros é pago anualmente com uma taxa de cupom fixa de 3% a. a. sobre um valor de face de R$ 100.

Quando a taxa de cupom é igual à TIR de negociação do título, dizemos que o título está sendo negociado ao par, que, neste caso, é R$ 100.

Agora, vamos supor que na sua emissão a taxa de juros de negociação do título fosse 4% a. a. Dessa maneira, o preço do título vai ter de refletir esse nível de juros médio, ou seja, o valor do papel vai ter de ser tal que seja possível obter o mesmo fluxo de caixa futuro com essa taxa de juros de 4% a. a.

Na verdade, não existe nenhuma teoria na equação anterior. A TIR e o preço do título são os dois lados da mesma moeda, que está relacionada ao cronograma de pagamentos do título e à curva de juros da economia. Essa relação será melhor estudada adiante.

Para calcular o preço desse papel, basta executar o seguinte cálculo:



P = Σ(k=1 até 7) 3/(1 + 4\%)^k + 100/(1 + 4\%)^7 = 94



A Tabela 2.4 contém os dados dessa conta:

Tabela 2.4 – Cálculo do preço para a TIR de 4%

|  t (anos) | Parcela ou fluxos de caixa | Valor Presente  |
| --- | --- | --- |
|  0 | 0 | 0  |
|  1 | 3 | 2,88  |
|  2 | 3 | 2,77  |
|  3 | 3 | 2,67  |
|  4 | 3 | 2,56  |
|  5 | 3 | 2,47  |
|  6 | 3 | 2,37  |
|  7 | 103 | 78,27  |

---

t (anos)
Parcela ou fluxos de caixa Valor Presente
Preço: 94

Fonte: Elaborada pelos autores.

O valor de mercado deste título é R$ 94, considerando que a taxa de negociação é de 4% a. a. Esse papel está sendo negociado com um deságio, dado que a taxa de juros atual é superior à taxa de cupom do papel⁴, conforme pode ser visto na tabela a seguir:

Tabela 2.5 – Zonas de ágio e deságio em função da TIR do papel

|  y | P | Observação  |
| --- | --- | --- |
|  1,0% | 113,46 |   |
|  1,5% | 109,90 | Região de  |
|  2,0% | 106,47 | ágio  |
|  2,5% | 103,17 |   |
|  3,0% | 100,00 | Emissão  |
|  3,5% | 96,94 |   |
|  4,0% | 94,00 | Região de  |
|  4,5% | 91,16 | deságio  |
|  5,0% | 88,43 |   |

Fonte: Elaborada pelos autores.

Que também pode ser representada graficamente:

Gráfico 2.2 – Preço como função da TIR do papel
![img-3.jpeg](img-3.jpeg)
Fonte: Elaborado pelos autores.

Por meio do Gráfico 2.2 pode-se observar o risco de mercado que está presente em instrumentos de renda fixa prefixados. Como o fluxo de caixa prometido é fixo, ao aumentar a taxa de juros da economia, o valor

---

presente necessário para se conseguir o mesmo fluxo futuro de recebimentos diminui, ou seja, houve uma perda a mercado no valor desse título.

O fluxo de amortização para esse papel que não está sendo transacionado ao par agora é diferente. Precisamos de uma nova variável, que são os juros apropriados, ou seja, os juros que serão provisionados entre um período e outro no esquema de marcação na curva.

Tabela 2.6 – Esquema de amortização no esquema americano para título com TIR diferente da taxa de cupom

|  t (anos) | Saldo | Juros apropriados | Amortização | Juros | Parcela ou fluxos de caixa  |
| --- | --- | --- | --- | --- | --- |
|  0 | 94,0 | 0 | 0 | 0 | 0  |
|  1 | 94,8 | 3,76 | 0 | 3 | 3  |
|  2 | 95,5 | 3,79 | 0 | 3 | 3  |
|  3 | 96,4 | 3,82 | 0 | 3 | 3  |
|  4 | 97,2 | 3,85 | 0 | 3 | 3  |
|  5 | 98,1 | 3,89 | 0 | 3 | 3  |
|  6 | 99,0 | 3,92 | 0 | 3 | 3  |
|  7 | 0,0 | 3,96 | 100 | 3 | 103  |

Fonte: Elaborada pelos autores.

Perceba que ao final do terceiro ano (depois do pagamento do cupom de juros) esse título estará sendo registrado na Contabilidade ao valor de R$ 96,40, independente de seu preço de mercado. O que você acha disso?

Normalmente, este tipo de autorização é dado em condições particulares, específicas ao modelo de negócio da entidade.

## Resumo

Este capítulo apresenta os diferentes esquemas de amortizações, a definição de taxas de juros, a conversão de taxas, o cálculo da taxa interna de retorno e uma introdução à marcação a mercado.

2 Investimento no sentido econômico do termo, por exemplo, projetos de construção de plantas, criação de negócios etc.

3 O título pode ter ágio ou deságio na emissão, isso ocorre quando a curva de juros do mercado é diferente da taxa de cupom ou o risco de crédito percebido pelo mercado é

---

diferente do que está precificado no título.

4 É importante esclarecer que a taxa de cupom definida pelo emissor do papel não afeta a sua rentabilidade, apenas define o valor do fluxo de caixa. Detalharemos mais adiante que a rentabilidade do papel depende, principalmente, da TIR de compra do papel e das taxas pelas quais seus fluxos de caixa intermediários são reinvestidos, caso o papel seja mantido na carteira até o seu vencimento.

---

# Exercícios propostos

1. Um título que paga cupons anuais de 4% a. a. fixos vence em cinco anos. O preço pago em sua aquisição foi de R$ 77,25528.
a. Calcule o valor da TIR desse título.
b. Crie uma planilha com o esquema de amortização do título.
c. Ele está sendo descontado com ágio ou deságio?
d. Qual o preço desse título para uma TIR de 3% a. a.?
e. Nessa hipótese, ele está sendo negociado com ágio ou deságio?

2. Defina o que é o cupom de juros de um título.

3. Defina o que é o principal de um título.

---

# Capítulo 3
Rentabilidade de títulos de renda fixa

Dada a característica de volatilidade⁵ nos preços dos títulos de renda fixa, é interessante que tenhamos métricas para medir a rentabilidade de um título em um dado horizonte de tempo.

Isso se faz necessário, porque a rentabilidade de um título se relaciona com a sua TIR ou à sua taxa de juros subjacente, mas não é inteiramente correlacionada com essas. As razões disso são as **oscilações de mercado** (alterações nas expectativas sobre as taxas de juros ao longo do tempo) e os **pagamentos dos cupons de juros**, como exemplificado no Capítulo 2.

## 3.1 Retorno de títulos sem cupom de juros

A rentabilidade de uma aplicação financeira é dada pela variação do seu valor entre as datas em que se quer calcular.

Assim, chamando-se o instante inicial de 0 e o final de t, o retorno ao período para títulos sem pagamento de cupom é dado por:



r_(0,t)^a = (P_t/P₀ - 1) × 100\% 



Que é o retorno no período em questão (daí o sobrescrito p) entre 0 e t.

Pode ser interessante calcular o retorno em termos anuais, para efeito de comparação. Para calcular o retorno em taxa anual para o mercado brasileiro, pode-se utilizar a expressão a seguir, considerando-se que t é o número de dias úteis entre “hoje” e a data de avaliação do retorno:



(1 + r_(0,t)^a)^(1/22) = P_t/P₀ 



Desenvolvendo, temos:



r_(0,t)^a = [(P_t/P₀)^(2/22) - 1] × 100\% 



## 3.1.1 Exemplo: cálculo da rentabilidade de uma LTN

Qual a rentabilidade ao ano de uma LTN de vencimento 1/7/2020

---

adquirida em 11/7/2016 por R$ 637,445 e vendida em 13/1/2007 por R$ 703,91, dado que entre as duas datas se passaram 130 dias úteis?

Utilizando-se a Equação 3.3, temos:



r_(0,130)^a = [ (703,91/637,45)^(252/130) - 1 ] × 100\% = 21,20\%



a. a.

A rentabilidade ao período é dada pela Equação 3.1:



r_(0,t)^p = (703,91/637,45 - 1) × 100\% = 10,43\%



em 130 dias úteis.

O Gráfico 3.1 ilustra o comportamento do retorno desse título em função do período. Observe que o retorno do papel varia ao longo do tempo, devido às mudanças nas expectativas do mercado em relação às taxas de juros. No caso a seguir a manutenção do título em carteira gerou um retorno total acima da taxa DI acumulada no período em questão.

![img-4.jpeg](img-4.jpeg)
Gráfico 3.1 – Retorno total ao longo do tempo de um título
Fonte: Elaborado pelos autores.

Por meio do exemplo anterior é possível observar que, se o título for do tipo zero cupom, o retorno total será idêntico à TIR do papel se o título for mantido até o vencimento.

É por isso que, em programas de televisão, ao discorrer sobre rentabilidades de títulos, os especialistas dizem que ao comprar papéis de renda fixa, o

---

investidor tem de ter a disponibilidade de manter os papéis até o vencimento, uma vez que a TIR estará garantida.

Esse raciocínio, na verdade, está parcialmente correto, pois um problema que a TIR apresenta é exatamente a taxa de reinvestimento desses cupons de juros pagos periodicamente.

Certamente, a taxa de reinvestimento não será a TIR calculada ao início da operação, o que invalida o raciocínio subjacente à recomendação em relação à sua precisão, embora o conceito seja adequado e valha no caso de títulos sem pagamentos de cupons.

Adiante, estudaremos meios de estimar o retorno total de papéis com pagamentos de cupons.

Estamos utilizando o termo estimar, pois como não sabemos o que será ou foi feito com o dinheiro dos cupons, qualquer exercício do tipo é uma ferramenta teórica para avaliação de performance, não devendo ser utilizados para propósitos contábeis ou fiscais, por exemplo.

Para os fins anteriormente citados, o mais adequado seria calcular o resultado da carteira de títulos, o que é feito caso a caso pelos controllers do fundo, fundo de pensão ou instituição financeira.

## 3.2 Retorno de títulos com pagamento de cupons

O título LTN é um título federal que não paga cupons de juros, logo o cálculo do retorno de seu detentor ao longo do tempo é simples de realizar.

Entretanto, existem papéis que pagam juros periódicos (e amortizações também) ao detentor dos mesmos.

Nessas circunstâncias, se usarmos as equações vistas anteriormente, estaremos negligenciando o fluxo de caixa que foi pago pelo emissor, o que distorce o valor da rentabilidade de possuir aquele papel.

Em função disso, foi criado o conceito de retorno total (total return, em inglês) do papel, ou seja, um cálculo que considera não somente os preços de compra e venda do papel, mas também fluxos de caixa intermediários recebidos pelo detentor do papel.

Esse cálculo pode ser realizado de duas formas. Ambas envolvem a hipótese de que os valores financeiros recebidos ao longo do período, sendo eles

---

juros ou amortizações, são reinvestidos na aquisição de papéis iguais ao preço vigente no mercado.

## 3.2.1 Cálculo do retorno pela TIR

Calcula-se a TIR do papel em função dos valores recebidos ao longo do período. O conceito de TIR, automaticamente, usa a hipótese de reinvestimento dos cupons à taxa interna de retorno. Chamando a TIR desse fluxo de caixa de y, o valor do retorno total em taxa anualizada para o período será:



T R g _x = y tag {3.4}



## 3.2.2 Cálculo de quotas de títulos equivalentes

Ao receber o valor dos cupons, estes são reinvestidos na compra de mais títulos iguais ao preço de mercado. Esse valor é incorporado ao seu "portfólio" de títulos equivalentes, ou seja, aumenta a quantidade possuída de títulos. Ao final, o retorno total será dado pela equação do retorno total ao ano para títulos com pagamento de cupom:



T R g _x = [ (P ₁ × Q ₁/P ₀ × Q ₀)^(252/1) - 1 ] × 100 \% 



A fórmula anterior é similar à de cálculo da TIR, porém os preços iniciais e finais do papel são ponderados pelas quantidades iniciais e finais do papel, para garantir o efeito de valorização do papel como se não tivesse havido pagamento de juros periódicos.

## 3.2.3 Exemplo: cálculo da rentabilidade de um título com cupom

Uma NTN-F com vencimento em 1/1/2027 foi adquirida em 19/1/2016 por R$ 692,774 e vendida em 13/1/2017 por R$ 946,084. Calcule o retorno total da NTN-F sabendo que se passaram 130 dias úteis.

Entre a aquisição e a venda desse papel houve duas datas de pagamento de cupons: 1/7/2016 e 2/1/2017. O valor dos cupons de juros é fixo e igual a R$ 48,808.

Esquema:

Figura 3.1 – Fluxos de caixa projetados do papel

---

![img-5.jpeg](img-5.jpeg)
Fonte: Elaborada pelos autores.

Resolução pela TIR:

A taxa de retorno do fluxo demonstrado na Figura 3.1 é o valor de y que é solução da equação a seguir:



692,774 = 48,808/(1 + y)^(113/252) + 48,808/(1 + y)^(240/252) + 946,084/(1 + y)^(249/252)



A TIR resulta em y = 53,37\% a. a.

Resolução pelas quotas, utilizando o conceito de total return:

Diferentemente do cálculo da rentabilidade assumindo a TIR, que admite que os fluxos de caixa intermediários são reinvestidos pela própria TIR original, aqui, partimos da premissa, mais realista, de que os cupons de juros são reinvestidos pelos preços, ou taxas, vigentes no mercado nas datas em que são pagos.

Desta forma, temos:



TR_(t,t+1) = (P_(t+1)/P_t Q_(t+1)/Q_t) - 1 



A quantidade de quotas em t + 1 é atualizada por:



Q_(t+1) = Q_t + D_(t+1)/P_(t+1) Q_t 



Sendo que D pode representar dividendos de investimentos em renda variável, ou, no escopo deste livro, cupom de juros intermediários de títulos de renda fixa.

Para calcular o retorno do investimento pela metodologia do total return, utilizando os mesmos dados do exemplo anterior, temos:

Tabela 3.1 – Esquema de cálculo por quotas

|  Data | Dias úteis | Fluxo de caixa | Preço | Quantidade atualizada | P x Q  |
| --- | --- | --- | --- | --- | --- |
|  19/1/2016 | 0 | 48,809 | 692,774 | 1.000,00000 | 692.774,00  |
|  1/7/2016 | 113 | 48,809 | 880,711 | 1.000,00 + 48,809 / 880,711 × 1.000,00 = 1.855,42 | 929.520,00  |

---

|  2/1/2017 | 240 | 48,809 | 932,790 | 1.055,42 + 48,809 / 932,790 = 1.055,42 = 1.110,65 | 1.036.003,21  |
| --- | --- | --- | --- | --- | --- |
|  13/1/2017 | 249 | 946,084 | 946,084Resgate Total (venda): 0.946,084×1.110,65 = 1.050.768,20  |   |   |

Fonte: Elaborada pelos autores.

Aplicando a fórmula, temos:



TR_(0,249) = 1.050.768,20/692.774,00 - 1 cong 51\%  a.p.



Anualizando, temos:



TR_(0,249) = (1 + 0,51)^(552) - 1 cong 52\%  a.a.



Verificamos que as rentabilidades calculadas pelos dois métodos, TIR e total return, são distintos, porque utilizam premissas distintas.

Na TIR, os fluxos de caixa são reinvestidos à única TIR. No cálculo por quotas, os cupons de juros intermediários são reinvestidos pelas taxas (preços) vigentes de mercado no momento do reinvestimento.

O mercado financeiro e os estudos acadêmicos utilizam mais o segundo método para avaliação do retorno total, que pode ser estendido para ações e fundos de investimento.

O gráfico do retorno total no período é dado a seguir:

![img-6.jpeg](img-6.jpeg)

Gráfico 3.2 – Retornos
Fonte: Elaborado pelos autores.

Observe que o gráfico foi muito acima da taxa DI acumulada do período. Isso ocorre porque houve grande deslocamento para baixo de toda a curva de juros nesse intervalo.

---

Resumo

Este capítulo demonstra como calcular a rentabilidade de um investimento em renda fixa, tanto pela taxa interna de retorno quanto pelo conceito de total return.

5 Volatilidade é a medida do padrão de oscilação nos preços de ativos financeiros.

---

# Exercícios propostos

1. Calcule o retorno total de uma compra de NTN-F com vencimento 1/1/2027 em 4/2/2014 a R$ 905,356 e venda final em 5/7/2017 por R$ 1018,790 (857 dias úteis). Os fluxos de pagamento de cupons com os respectivos preços são dados a seguir:

|  Data | Cupom | Preço | Dias úteis  |
| --- | --- | --- | --- |
|  2/4/2014 |  | 905,356 |   |
|  7/1/2014 | 48,80885 | 944,922 | 99  |
|  1/2/2015 | 48,80885 | 925,274 | 230  |
|  7/1/2015 | 48,80885 | 922,966 | 252  |
|  1/4/2016 | 48,80885 | 859,803 | 480  |
|  7/1/2016 | 48,80885 | 958,421 | 604  |
|  1/2/2017 | 48,80885 | 986,561 | 731  |
|  7/3/2017 | 48,80885 | 1.017,479 | 855  |
|  7/5/2017 |  | 1.018,790 | 857  |

2. Analise a afirmação a seguir.

"O cupom de juros de uma NTN-F é definido pelo Tesouro em 1% a. a., pagos semestralmente. Logo, podemos concluir que a rentabilidade deste título é 1% a. a., em qualquer circunstância".

Essa afirmação é verdadeira? Justifique sua resposta.

3. Explique quais são as diferenças entre os cálculos da rentabilidade de um título pela TIR e por quotas.

---

# Capítulo 4

## Estrutura a termo de taxas de juros (ETTJ)

### 4.1 Definição

Neste capítulo, trataremos da estrutura a termo de taxas de juros.

A estrutura a termo de taxas de juros (ETTJ) é a curva que relaciona as taxas de juros de um mesmo risco de crédito para diferentes prazos.

Como existem taxas de juros para diferentes níveis de risco de crédito e para diferentes indexadores, existem diversas ETTJs diferentes, uma para cada mercado analisado.

Há, por exemplo, ETTJs de taxa prefixada para diferentes riscos de crédito, ETTJ de cupom cambial⁶, de cupom de IPCA, cupom de IGPM etc.

Essas curvas de juros servem para, entre outros usos, “descobrir” os preços de ativos que, porventura, não estejam sendo negociados em mercado, determinando-se qual deveria ser o seu preço de negociação.

Exemplos de ETTJs podem ser vistos no gráfico a seguir:

Gráfico 4.1 – ETTJ Pré x DI da B3 (data de referência 5/7/2017)
![img-7.jpeg](img-7.jpeg)
Fonte: Elaborado pelos autores.

### 4.2 Taxa DI versus taxa Selic

---

4.2.1 Taxa DI

Antes de iniciarmos a discussão de como as taxas de juros são formadas no mercado de renda fixa, é importante conhecermos as taxas que são relacionadas às operações de um dia e que têm estreita relação com a Meta Selic, taxa de referência divulgada pelo Comitê de política monetária (Copom) do Conselho monetário nacional (CMN).

A taxa dos Depósitos interfinanceiros (DI) é resultado da taxa média de operações entre instituições financeiras nas quais um banco toma recursos de outra instituição financeira, normalmente, por 1 dia útil, para cobrir suas necessidades momentâneas de caixa. Essas operações são registradas na Central de títulos privados (Cetip) e não possuem garantia.

São os Certificados de depósitos interfinanceiros (CDIs) que lastreiam o mercado interbancário e só podem ser negociados entre instituições financeiras, sendo vedada a sua negociação a uma instituição financeira não bancária.

A maior parte das operações tem prazo de 1 dia útil e a média das operações prefixadas realizadas entre instituições financeiras de grupos econômicos diferentes serve de amostra para o cálculo da taxa DI, utilizada como referência de remuneração pós-fixada no mercado financeiro brasileiro, para indexação de Certificados de depósitos bancários (CDBs), empréstimos, contratos derivativos etc.

4.2.2 Taxa Selic

A Selic, por sua vez, é a taxa média de financiamento no mercado interbancário para operações de um dia, as quais possuem lastro (garantia) em títulos públicos federais.

Os títulos que lastreiam a formação da taxa Selic são registrados no Sistema especial de liquidação e de custódia (Selic).

A Selic registra, diariamente, as operações de empréstimos entre instituições financeiras garantidas por títulos públicos, sendo utilizada para obtenção de recursos de curtíssimo prazo entre as instituições, que, ao tomar recursos emprestados, oferecem títulos públicos como garantia.

Diariamente, as instituições financeiras tomam e doam recursos de outras instituições financeiras, normalmente, pelo prazo de um dia útil. Para

---

conceder maior segurança à instituição doadora de recursos ocorre uma venda de títulos públicos federais pela instituição tomadora de recursos e a compra dos mesmos títulos pela instituição doadora dos recursos.

Ao mesmo tempo, ambas as instituições assumem o compromisso de recompra e revenda dos títulos no dia útil seguinte, sendo a diferença no valor das transações igual aos juros pactuados. São operações conhecidas como compromissadas (em inglês, repurchase agreement ou, simplesmente, repo).

A média desse tipo de operação serve para o cálculo da taxa Selic, a taxa de juros média das operações entre instituições financeiras por 1 dia útil e garantidas por títulos públicos. Essa é a taxa que o Banco Central precisa monitorar de forma a deixá-la próxima da meta do Copom.

## 4.3 Formação das taxas de juros

O Copom reúne-se oito vezes ao ano para definir a meta da taxa Selic.

Na definição da meta Selic, o Copom leva em consideração aspectos como inflação (regime de metas de inflação), crescimento econômico, liquidez da economia, taxa de câmbio e risco soberano⁷, entre outras.

O Copom discute, à luz dos seus modelos, qual será o valor da meta Selic de sorte a garantir que a taxa de inflação se situe dentro do intervalo do regime de metas.

Ao fim do processo de discussão, que dura dois dias, o Copom define a meta de taxa de juros Selic para 1 dia útil. O Banco Central do Brasil (Bacen) monitora a taxa Selic de forma a deixá-la próxima da taxa do Copom, e o mercado financeiro determina as taxas de juros prefixadas para outros prazos.

Essas taxas de juros de outros prazos são determinadas pelo mercado financeiro a partir da negociação de títulos públicos federais prefixados (LTNs e NTN-Fs) e de contratos de derivativos de taxa de juros, normalmente, contratos futuros de DI e swap pré x DI.

Essas taxas de juros prefixadas de prazo superior ao de 1 útil, reveladas pelos participantes do mercado na negociação de títulos públicos federais dependem de uma série de fatores:

---

- Expectativas de taxas de juros;
- Preferência pela liquidez desses agentes;
- Segmentação de mercado em função dos prazos das taxas.

Se for assumida a hipótese de expectativas, ou seja, a não existência de prêmio de risco associado à curva de juros, o valor esperado pelo mercado das taxas DI_k ao longo do tempo é dado pela curva prefixada a cada instante de tempo.

Se as expectativas sobre as taxas a termo, que são aplicadas sobre os vértices de taxas subjacentes, forem serialmente correlacionadas, essa hipótese pode-se mostrar inadequada.

A partir da determinação dessa ETTJ prefixada básica de títulos públicos federais, as ETTJs de taxas de juros acima dos indexadores de títulos, conhecidas como cupom cambial, cupom de IPCA, cupom de IGPM, cupom de TBF etc. são determinadas a partir da expectativa dos agentes econômicos do comportamento futuro desses indexadores. Da mesma forma, as ETTJs com risco de crédito são determinadas.

Uma vez que os contratos futuros DI e os contratos de swap DI x Pré permitem prefixar as taxas futuras de DI por arbitragem, as negociadas nesses contratos revelam, a cada instante, a ETTJ prefixada da economia. Desta forma, podemos calcular a taxa pré em função da expectativa do acumulado das taxas DI.



(1 + i)^(du/2.62) = ∏(k=0 até du-1) (1 + E[DI_k])^(1/2.62) 



Na Equação 4.1, a chamada taxa pré para du, prazo em dias úteis, é o produtório da taxa DI esperada⁸ ao longo de cada dia útil. Nessa equação foi utilizado o conceito de expectativa de taxas futuras de juros. Um termo de prêmio pelo risco em função do prazo poderia ser acrescentado, para generalização.

De forma linearizada, pode-se escrever a equação anterior como:



i^* = Σ(k=0 até du-1) E[DI_k^*] 



Que é a equação da taxa pré em função da expectativa do acumulado das

---

taxas DI linearizadas. Onde o asterisco refere-se à taxa linearizada.

Assim, a taxa pré acaba revelando o resultado das expectativas que o mercado financeiro faz, a cada instante, sobre qual será a taxa DI em cada dia útil do período analisado.

Dessa maneira, observa-se que o valor de i, que é a taxa pré para o vencimento du, muda a cada instante, resultado das diferentes percepções que o mercado tem sobre o termo DI_k, ou seja, qual a trajetória da taxa DI ao longo do tempo, a partir da data presente.

## 4.3.1 Exemplo: cálculo da estimativa de variação nas taxas de juros

Suponha que a próxima reunião do Copom ocorrerá daqui a dez dias úteis. A taxa Selic encontra-se em 7,25% a. a. e a taxa DI encontra-se no mesmo patamar, não sendo esperadas diferenças entre essas duas taxas. Qual o valor do ajuste esperado pelo mercado na taxa Selic se o futuro de DI, que vence em 25 dias úteis, é transacionado, atualmente, à taxa de 8% a. a.?

Usando a equação:



(1 + i) du/252 = ∏(k=0 até du-1) (1 + E[DI_k])^(1/252)



Como a expectativa em relação ao CDI não será alterada até a próxima reunião do Copom, temos:



(1 + 8\%)^(25/252) = (1 + 7,25\%)^(10/252) × (1 + E[DI_(média)])^(15/252)



O que resulta em uma expectativa para a taxa DI no período logo após a reunião do Copom de 8,50% a. a. Assim, verifica-se que o mercado financeiro espera hoje que a decisão do comitê seja pelo aumento da taxa de juros na magnitude de 1,25% a. a.

Ou seja, a taxa de juros que o mercado observa na prática, conhecida como taxa spot, é a média geométrica da expectativa das taxas de juros ao longo do tempo.

## Resumo

Este capítulo explica o processo de formação de taxas de juros, assim como a definição da ETTJ, a estrutura temporal de taxas de juros.

---

6 Aqui, os cupons significam a diferença de remuneração entre as curvas prefixadas e os seus respectivos indexadores. É importante não confundir com as taxas de cupom dos títulos públicos de longa duração.

7 Risco soberano: risco de solvência do país ao longo do tempo.

8 O operador esperança é um operador linear. A Equação 4.1 é um produto, mas não existe perda de generalidade no conceito, uma vez que é possível fazer a conta da maneira como indicado.

---

# Exercícios propostos

1. Supondo que a Selic corrente seja 8% a. a. e que a próxima reunião do Copom seja em 20 dias úteis, precifique uma LTN que vence em 30 dias úteis e é esperada uma redução da taxa Selic de 50 p.b.

Dado:



P_(LTN) = 1.000/(1 + i)^(dn/252)



2. Defina o que é a ETTJ.

3. Quais as diferenças entre as taxas Selic e DI?

4. Descreva o processo de formação das taxas de juros.

---

# Capúulo 5 Técnicas de estimação da ETTJ

## 5.1 Conceito de interpolação

Apesar de os jornais e os noticiários econômicos publicarem a ETTJ como uma curva contínua, para se chegar a esse resultado passa-se, necessariamente, por um processo um pouco mais complexo, chamado de interpolação de taxas de juros.

Os contratos futuros de DI e os títulos públicos negociados no mercado para fazer apostas sobre o acumulado da taxa DI têm vencimentos em datas determinadas.

Isso faz com que a liquidez entre o vencimento de instrumentos líquidos fique comprometida, uma vez que as apostas são sobre o caminho do DI e a meta Selic só se altera oito vezes por ano.

Isso exige que as taxas para outros prazos sejam estimadas de alguma forma. Essa exigência é dada tendo em vista que:

- As mesas de operação são obrigadas a estimar quais seriam as taxas entre os vencimentos de instrumentos negociados para poderem cotar operações aos seus clientes.

- As áreas de risco têm de precificar ativos não negociados e estimar as volatilidades⁹ das taxas para usar em seus modelos de VaR (Value at Risk) e mensuração de risco.

- As contabilidades das instituições financeiras têm de calcular o resultado das operações de negociação de títulos.

Para tornar a ETTJ contínua, determinando-se as taxas para todas as maturidades, lança-se mão da interpolação de taxas de juros.

A interpolação de taxas é o procedimento para calcular as taxas de juros para prazos nos quais não existem instrumentos financeiros que possam ser usados como referência para aquele determinado prazo da curva de juros.

---

A seguir, serão apresentados alguns métodos de interpolação de taxas de juros.

## 5.2 Flat forward exponencial

A interpolação *flat forward* apresenta uma intuição econômica forte.

O modelo consiste em tomar dois pontos (prazos) no tempo em que as taxas são conhecidas.

Entre esses pontos, admite-se que a taxa a termo diária (que, no nosso caso, é a Selic ou a CDI) permanecerá constante, (por isso o nome *flat forward* ou taxa incremental a termo constante).

Matematicamente, podemos definir a equação da taxa *forward* conforme a seguir:



(1 + Fwd)^(du_2 - du_1/222) = (1 + i_2)^(du_2/222)/(1 + i_1)^(du_1/222) 



Onde:

- i_1: taxa prefixada a. a. para o vencimento du_1
- i_2: taxa prefixada a. a. para o vencimento du_2, sendo du_2 > du_1
- Fwd: taxa *forward* ou a termo, prefixada a. a.

Com o cálculo anterior, são obtidos dois subprodutos:

1. A inclinação da ETTJ. Se a taxa a termo for maior que a taxa prefixada do período 1, a curva é crescente, ou seja, os agentes esperam aumento de juros no período analisado. Se a taxa a termo for menor que a taxa pré do período 1, a curva é decrescente, ou seja, os agentes esperam corte de juros no período analisado;
2. O suporte para o traçado da curva ETTJ resultado da interpolação para todas as maturidades desejadas. Para tanto, basta assumir (como na hipótese do modelo) que essa taxa é constante nesse intervalo da interpolação. Obviamente, essa é uma hipótese audaciosa, dado que podem ocorrer reuniões do Copom nesse período, mas o mercado sabe desse detalhe e vai mapear o período com novas séries de derivativos de taxas de juros.

Então, a taxa pré-interpolada resulta do rearranjo da Equação 5.1:

---



(1 + i_*)^(du_*/252) = (1 + i₁)^(du_*/252) × (1 + Fwd)^(du_* - du_*/252) 



Onde:

i_*: taxa prefixada interpolada para o prazo du_*.

A taxa *forward* é, em sentido mais amplo, a expectativa do mercado sobre qual será a taxa vigente entre dois vencimentos à frente.

Assim, podemos definir a taxa *forward* como expectativa do mercado pela equação a seguir:



Fwd_(1,2) = E[i_(1,2)] 



## 5.2.1 Exemplo: cálculo da interpolação *flat forward* exponencial

Dado que a taxa prefixada para cinco anos é igual a 8% a. a. e a taxa pré para dez anos é 9% a. a., vamos determinar, por meio do método *flat forward*, qual o valor da taxa prefixada para o prazo de sete anos.

O primeiro passo é calcular a taxa a termo *forward* por meio da equação:



(1 + fwd)^(2.520 - 1.260/252) = (1 + 9\%)^(2.520/252)/(1 + 8\%)^(1.260/252)}



Fwd = 10\% a. a.

Considerando correta a Hipótese de Expectativas Puras (sem prêmios de risco), os participantes do mercado esperam que, daqui a dez anos, a taxa de juros anual para maturidades de cinco anos seja igual a 10%, um aumento de 2% em relação à taxa de juros de cinco anos que vale hoje na economia, 8% a. a. Isso significa que entre o quinto e o décimo ano é esperado um aumento na Selic de 2% a. a.

Para o cálculo da taxa interpolada, usa-se a outra equação:



(1 + i_*)^(1.764/252) = (1 + 10\%)^(1.764 - 1.1260/252) × (1 + 8\%)^(1.260/252)



i_* = 8,57\% a. a.

A tabela a seguir ilustra o conceito para o período inteiro:

Tabela 5.1 – Exemplo de taxas *spot* x taxas *forward*

|  t (anos) | Taxa spot | Taxa forward  |
| --- | --- | --- |
|  1 |  | 8%  |

---

|  t (anos) | Taxa spot | Taxa forward  |
| --- | --- | --- |
|  2 |  | 8%  |
|  3 |  | 8%  |
|  4 |  | 8%  |
|  5 | 8,00% | 8%  |
|  6 | 8,33% | 10%  |
|  7 | 8,57% | 10%  |
|  8 | 8,75% | 10%  |
|  9 | 8,88% | 10%  |
|  10 | 9,00% | 10%  |

Fonte: Elaborada pelos autores.

Graficamente, temos:

![img-8.jpeg](img-8.jpeg)
Gráfico 5.1 – Exemplo de taxas spot x taxas forward
Fonte: Elaborado pelos autores.

Ou seja, o modelo flat forward interpola taxas entre dois períodos conhecidos, assumindo que as taxas forward, entre esses períodos, sejam as mesmas e que a taxa forward do período inicial seja equivalente à taxa à vista do período inicial.

# 5.3 Interpolação linear

Embora pouco utilizada no Brasil, a interpolação linear ou aritmética de taxas é padrão nos mercados internacionais.

A interpolação linear simplesmente une os dois pares ordenados (du₁;i₁) e (du₂;i₂) por um segmento de reta.

---

Dessa maneira, a equação para i_* seria:



i_* = i_1 + (i_2 - i_1)/(du_2 - du_1) × (du_* - du_1) 



## 5.3.1 Exemplo: cálculo da interpolação linear

Dado que a taxa prefixada para cinco anos é 8% a. a. e a taxa pré para dez anos é 9% a. a., determine por meio do método *flat forward* qual o valor da taxa pré para o prazo de sete anos.

Substituindo na fórmula da interpolação linear, temos:



i_* = 8\% + (9\% - 8\%)/(2.520 - 1.260) × (1.764 - 1.260)



i_* = 8,40\% a. a.

## 5.4 Interpolação por *cubic spline*

A interpolação por *cubic spline* é uma técnica que permite melhor suavização da curva entre os vértices observados. Em contrapartida, é difícil de ser calculada manualmente. Felizmente, a interpolação por *cubic spline* está implementada em vários pacotes computacionais. Para o MS Excel, é possível achar os códigos em VBA na internet. É recomendável utilizar códigos prontos com parcimônia, sempre validando os cálculos antes de serem usados na prática. Mostraremos, no final deste capítulo, uma implementação do *cubic spline* na linguagem Python.

Aqui fazemos um exemplo, passo a passo, dessa técnica de interpolação. Desta forma, podemos validar os cálculos de interpolação por *cubic spline* implementados em diferentes softwares, ou até mesmo criar nossos próprios códigos.

O fundamento matemático da interpolação por *cubic spline* é gerar uma aproximação polinomial *piecewise*, ou por partes. A função genérica do *cubic spline* parte de uma equação do terceiro grau:



f(x) = a + bx + cx^2 + dx^3 



Como o próprio nome diz, essa interpolação utiliza-se de uma função cúbica. Esse é um requerimento para obter uma função que tenha uma derivada de primeira e segunda ordem, que nos auxiliarão no cálculo dos coeficientes das funções de interpolação por *cubic spline*, como veremos a

---

seguir.

A maior diferença entre essa técnica de interpolação em relação às apresentadas anteriormente é que não existe uma fórmula única de interpolação por cubic spline. A fórmula de interpolação por cubic spline, S(x) varia de acordo com os vértices anterior e posterior, permitindo que a função se ajuste ao longo dos vértices:



S(x) = 
a_0 + b_0(x - x_0) + c_0(x - x_0)^2 + d_0(x - x_0)^3 & se  x_0 ≤ x ≤ x_1 

a_1 + b_1(x - x_1) + c_1(x - x_1)^2 + d_1(x - x_1)^3 & se  x_1 ≤ x ≤ x_2 

a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3 & se  x_i ≤ x ≤ x_(i+1) 

a_(n-1) + b_(n-1)(x - x_(n-1)) + c_(n-1)(x - x_(n-1))^2 + d_(n-1)(x - x_(n-1))^3 & se  x_(n-1) ≤ x ≤ x_n
 



No contexto de interpolação de taxas S(x) é a taxa interpolada para o prazo x. Aqui, é importante relembrar que o eixo das abcisas corresponde aos prazos e o eixo das ordenadas às taxas. Na implementação do cálculo da interpolação do cubic spline os prazos observados nos vértices estão em ordem cronológica, ou seja, x_0 < x_1 < x_2 < ... < x_n.

Agora, faremos o procedimento, passo a passo, de como obter as funções de interpolação por cubic spline, assumindo as taxas de juros spot nos prazos conforme a tabela a seguir:

Tabela 5.2 – Exemplo de vértices para interpolação via cubic spline

|  t (anos) | Taxa spot  |
| --- | --- |
|  x_0 = 1 | 14,00%  |
|  x_1 = 2 | 15,00%  |
|  x_2 = 3 | 13,50%  |

Fonte: Elaborada pelos autores.

Como temos três vértices, podemos concluir que obteremos duas funções de interpolação por cubic spline, de x_0 à x_1 e de x_1 à x_2:



S(x)0̂ = a_0 + b_0(x - x_0) + c_0(x - x_0)^2 + d_0(x - x_0)^3





S(x)1̂ = a_1 + b_1(x - x_1) + c_1(x - x_1)^2 + d_1(x - x_1)^3



Substituindo, temos:



S(x)0̂ = a_0 + b_0(x - 1) + c_0(x - 1)^2 + d_0(x - 1)^3





S(x)1̂ = a_1 + b_1(x - 2) + c_1(x - 2)^2 + d_1(x - 2)^3



Podemos observar que temos oito coeficientes que devemos calcular para

---

obter as duas equações de interpolação por cubic spline do nosso exemplo, S(x)δ e S(x)δ̃. Para conseguir obter os oito coeficientes, precisamos de um sistema de oito equações.

Mostraremos a seguir como obter as oito equações para montar o sistema e a sua resolução na forma matricial.

Sabemos que os valores das funções de interpolação devem passar pelos pontos dos vértices. Logo, ao substituirmos o x_0 = 1 em x na função S(x)δ̃, obtemos:



S(1)δ = a_0 = 14,00\%



E, ao substituirmos o x_1 = 2 em x na função S(x)δ:



S(2)δ = a_0 + b_0(2 - 1) + c_0(2 - 1)^2 + d_0(2 - 1)^3



Temos:



S(2)δ = a_0 + b_0 + c_0 + d_0 = 15,00\%



Também sabemos que existe continuidade das funções S(x)δ e S(x)δ̃. Ou seja, x_1 também passa pela função S(x)δ̃. Logo, podemos substituir o x_1 = 2 em x na função S(x)δ̃:



S(2)δ̃ = a_1 = 15,00\%



Como existe mais um vértice, podemos substituir x_2 = 3 em x na função S(x)δ̃:



S(3)δ̃ = a_1 + b_1(3 - 2) + c_1(3 - 2)^2 + d_1(3 - 2)^3



Logo:



S(3)δ̃ = a_1 + b_1 + c_1 + d_1 = 13,50\%



Então, até este momento, obtivemos um sistema de quatro equações com oito incógnitas:



{ {l}
a_0 = 14,00\% 

a_0 + b_0 + c_0 + d_0 = 15,00\% 

a_1 = 15,00\% 

a_1 + b_1 + c_1 + d_1 = 13,50\%
 



Precisamos de mais equações para calcular os coeficientes. Sabemos que os resultados da primeira e da segunda derivadas das funções S(x)δ e S(x)δ̃ devem ser iguais no vértice compartilhado, em x_1 = 2. Logo, precisamos da primeira e da segunda derivadas de S(x)δ̃:

---



S'(x)_0^2 = b_0 + (x - 1)(2c_0 + 3d_0(x - 1))





S''(x)_0^2 = 2c_0 + 6d_0(x - 1)



E também da primeira e da segunda derivadas de S(x)_1^2:



S'(x)_1^2 = b_1 + (x - 2)(2c_1 + 3d_1(x - 2))





S''(x)_1^2 = 2c_1 + 6d_1(x - 2)



Agora, basta calcular os valores da primeira e da segunda derivadas de S(x)_0^2 e S(x)_1^2 no vértice compartilhado, ou seja, substituir x por x_1 = 2:



S'(x)_0^2 = b_0 + 2c_0 + 3d_0





S''(x)_0^2 = 2c_0 + 6d_0





S'(x)_1^2 = b_1





S''(x)_1^2 = 2c_1



Conforme mencionado, sabemos que S'(x)_0^2 = S'(x)_1^2 e que S''(x)_0^2 = S''(x)_1^2. Então, podemos adicionar mais duas equações ao nosso sistema:



{ {l}
a_0 = 14,00\% 

a_0 + b_0 + c_0 + d_0 = 15,00\% 

a_1 = 15,00\% 

a_1 + b_1 + c_1 + d_1 = 13,50\% 

b_0 + 2c_0 + 3d_0 - b_1 = 0 

2c_0 + 6d_0 - 2c_1 = 0
 



Agora, só faltam mais duas equações para calcular os valores dos coeficientes. Na interpolação por cubic spline podemos assumir que S''(x_0)_0^2 = 0 e que S''(x_2)_1^2 = 0. Essa premissa é chamada de natural boundary conditions. Portanto, assumindo que as segundas derivadas nos pontos de fronteira, x_0 e x_2 no nosso exemplo, são iguais a zero, temos:



S''(1)_0^2 = 2c_0 = 0





S''(3)_1^2 = 2c_1 + 6d_1 = 0



Finalmente, podemos completar o nosso sistema de oito equações e oito incógnitas:



{ {l}
a_0 = 14,00\% 

a_0 + b_0 + c_0 + d_0 = 15,00\% 

a_1 = 15,00\% 

a_1 + b_1 + c_1 + d_1 = 13,50\% 

b_0 + 2c_0 + 3d_0 - b_1 = 0 

2c_0 + 6d_0 - 2c_1 = 0 

2c_0 = 0 

2c_1 + 6d_1 = 0
 



---

E agora, como resolver o sistema anterior? A maneira mais simples é resolver o sistema por matrizes. Para aqueles que não estão acostumados a trabalhar com matrizes, é útil reescrever o sistema anterior da seguinte forma:



{ {l} 1a_0 + 0b_0 + 0c_0 + 0d_0 + 0a_1 + 0b_1 + 0c_1 + 0d_1 = 14,00\% 
 1a_0 + 1b_0 + 1c_0 + 1d_0 + 0a_1 + 0b_1 + 0c_1 + 0d_1 = 15,00\% 
 0a_0 + 0b_0 + 0c_0 + 0d_0 + 1a_1 + 0b_1 + 0c_1 + 0d_1 = 15,00\% 
 0a_0 + 0b_0 + 0c_0 + 0d_0 + 1a_1 + 1b_1 + 1c_1 + 1d_1 = 13,50\% 
 0a_0 + 1b_0 + 2c_0 + 3d_0 + 0a_1 - 1b_1 + 0c_1 + 0d_1 = 0,00\% 
 0a_0 + 0b_0 + 2c_0 + 6d_0 + 0a_1 + 0b_1 - 2c_1 + 0d_1 = 0,00\% 
 0a_0 + 0b_0 + 2c_0 + 0d_0 + 0a_1 + 0b_1 + 0c_1 + 0d_1 = 0,00\% 
 0a_0 + 0b_0 + 0c_0 + 0d_0 + 0a_1 + 0b_1 + 2c_1 + 6d_1 = 0,00\%  



Assim fica mais fácil preencher a matriz A, que corresponde ao lado esquerdo das equações do sistema:

![img-9.jpeg](img-9.jpeg)

Matriz A

E vamos gerar a vetor B, que corresponde ao lado direito das equações do sistema:



{c}
boxed{14,00\%} 

boxed{15,00\%} 

boxed{13,50\%} 

boxed{0,00\%} 

boxed{0,00\%} 

boxed{0,00\%} 

boxed{0,00\%}




Matriz B

A resolução do sistema de equações ocorre quando calculamos os valores dos coeficientes das funções dos cubic splines, dispostos no vetor C a seguir:



{c}
a_0 

b_0 

c_0 

d_0 

a_1 

b_1 

c_1 

d_1




Matriz C

E como resolvemos o sistema? Por meio da multiplicação da matriz inversa de A, A^(-1), com o vetor C, ou seja, C = A^(-1)B.

No MS Excel é simples calcularmos a matriz A^(-1):

---

|  1 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  -1,25 | 1,25 | 0,25 | -0,25 | -0,25 | -0,08333 | -0,29167 | 0,041667  |
|  0 | 0 | 0 | 0 | 1 | 0 | 0,5 | 0  |
|  0,25 | -0,25 | -0,25 | 0,25 | 0,25 | 0,08333 | -0,20833 | -0,04167  |
|  0 | 1 | 0 | 0 | 0 | 0 | 0 | 0  |
|  -0,5 | 0,5 | -0,5 | 0,5 | -0,5 | 0,16667 | 0,08333 | -0,08333  |
|  0,75 | -0,75 | -0,75 | 0,75 | 0,75 | -0,25 | -0,125 | -0,125  |
|  -0,25 | 0,25 | 0,25 | -0,25 | -0,25 | 0,08333 | 0,04167 | 0,20833  |

## Matriz A^(-1)

Ainda utilizando o MS Excel multiplicamos as matrizes A^(-1) e B. Então, obtemos o vetor C, solucionando o nosso sistema de equações:



{ {l l} a ₀ = & 0, 1 4 0 0 0 
 b ₀ = & 0, 0 1 6 2 5 
 c ₀ = & 0, 0 0 0 0 0 
 d ₀ = & - 0, 0 0 6 2 5 
 a ₁ = & 0, 1 5 0 0 0 
 b ₁ = & - 0, 0 0 2 5 0 
 c ₁ = & - 0, 0 1 8 7 5 
 d ₁ = & 0, 0 0 6 2 5  



## Matriz C resolvida

Desta forma, conseguimos as duas funções de interpolação por *cubic spline* deste exemplo:



S (x) = { {l l} 0, 1 4 + 0, 0 1 6 2 5 (x - 1) + 0 (x - 1) ² - 0, 0 0 6 2 5 (x - 1) ³ & se  x ₀ ≤ x ≤ x ₁ 
 0, 1 5 - 0, 0 0 2 5 (x - 2) - 0, 0 1 8 7 5 (x - 2) ² + 0, 0 0 6 2 5 (x - 2) ³ & se  x ₁ ≤ x ≤ x ₂  



A pergunta que podemos nos fazer neste momento é: vale a pena utilizar a interpolação por *cubic spline*, dado que é um processo muito mais complexo do que a interpolação exponencial *flat forward*? Depende. Vamos comparar as interpolações por *cubic spline* e *flat forward* com os dados do nosso exemplo:

Para referência, a Tabela 5.3 traz os dados interpolados do exemplo:

**Tabela 5.3 – Comparação da interpolação via cubic spline e flat forward exponencial**

|  t (anos) | Cubic spline | Flat forward | Vértices  |
| --- | --- | --- | --- |
|  1,0 | 14,0000% | 14,0000% | 14,00%  |
|  1,1 | 14,1619% | 14,1812% |   |
|  1,2 | 14,3200% | 14,3324% |   |
|  1,3 | 14,4706% | 14,4605% |   |
|  1,4 | 14,6100% | 14,5704% |   |
|  1,5 | 14,7344% | 14,6657% |   |
|  1,6 | 14,8400% | 14,7492% |   |
|  1,7 | 14,9231% | 14,8229% |   |

---

|  t (anos) | Cubic spline | Flat forward | Vértices  |
| --- | --- | --- | --- |
|  1,8 | 14,9800% | 14,8885% |   |
|  1,9 | 15,0069% | 14,9472% |   |
|  2,0 | 15,0000% | 15,0000% | 15,00%  |
|  2,1 | 14,9569% | 14,7845% |   |
|  2,2 | 14,8800% | 14,5890% |   |
|  2,3 | 14,7731% | 14,4107% |   |
|  2,4 | 14,6400% | 14,2475% |   |
|  2,5 | 14,4844% | 14,0976% |   |
|  2,6 | 14,3100% | 13,9594% |   |
|  2,7 | 14,1206% | 13,8316% |   |
|  2,8 | 13,9200% | 13,7131% |   |
|  2,9 | 13,7119% | 13,6028% |   |
|  3,0 | 13,5000% | 13,5000% | 13,50%  |

Fonte: Elaborada pelos autores.

## Graficamente, temos:

Gráfico 5.2 – Comparação da interpolação via cubic spline e flat forward exponencial
![img-10.jpeg](img-10.jpeg)
Fonte: Elaborado pelos autores.

No Gráfico 5.2, observamos um formato mais “natural” das funções geradas pela interpolação por cubic spline. Observem que o gráfico da interpolação flat forward tem um formato de “bico”, não muito aderente ao que esperaríamos ver no mundo real para uma curva spot de taxa de juros.

Nossa experiência indica que, ao optar pelo tipo de interpolação utilizada, devemos observar as convenções que o mercado usa para aquele tipo de curva. A interpolação flat forward continua sendo muito popular no Brasil pela sua simplicidade, fundamentação econômica e, de maneira geral, não gera diferenças significativas na prática em relação às taxas obtidas pela

---

interpolação por cubic spline.

## 5.4.1 Exemplo: implementação do cubic spline no python

O objetivo desta seção é encorajar o usuário a buscar soluções em programas que contêm pacotes já prontos e que podem ser aplicados em Finanças e renda fixa. Mostraremos como os softwares atuais permitem a implementação de procedimentos intricados, como a interpolação via cubic spline, exigindo pouco conhecimento de programação do usuário.

Até, aproximadamente, meados dos anos 2000, o paradigma para solucionar problemas computacionalmente complexos, como alguns cálculos relacionados à Finanças, era o usuário criar o seu próprio código "do zero". Isso exigia uma longa curva de aprendizado, demandando muita dedicação do usuário, que, além de ser especialista em na sua área, era preciso dominar alguma linguagem de programação, que, muitas vezes, não era intuitiva.

Uma pletora de linguagens de programação mais amigáveis vem sendo difundidas ao longo dos últimos anos. Viabilizado pelo acesso à internet, as comunidades open source disponibilizam gratuitamente pacotes, ou bibliotecas, com soluções prontas, que atendem uma enorme gama de problemas, como a da interpolação via cubic spline.

Vamos voltar ao problema de como interpolar as taxas de juros a partir dos vértices da Tabela 5.2, vista anteriormente:

|  t (anos) | Taxa spot  |
| --- | --- |
|  x₀ = 1 | 14,00%  |
|  x₁ = 2 | 15,00%  |
|  x₂ = 3 | 13,50%  |

Na seção anterior, fizemos a interpolação de forma manual e utilizamos o MS Excel para plotar o gráfico. Agora, demonstraremos ao leitor como é simples fazer a interpolação via cubic spline no Python. Escolhemos o Python por ser uma linguagem simples, que possui programas de desenvolvimento gratuitos, e um pacote de interpolação pronto.

É importante revelar aos leitores que os autores deste livro têm pouco conhecimento na linguagem Python, mas que, graças aos pacotes já implementados pela comunidade, é possível interpolar os vértices da tabela

---

anterior em poucos minutos, bastando algumas consultas via sites de busca, como o Google.

Esse foi o código desenvolvido pelos autores importando os pacotes já desenvolvidos pela comunidade do Python:

Figura 5.1 – Exemplo de código para interpolação via cubic spline no Python
```python
#Bloco 1: importa os pacotes necessários
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
#Bloco 2: atribui valores aos vetores dos eixos "x" e "y", são os inputs
x=np.array([1,2,3])
y=np.array([14,15,13.5])
#Bloco 3: utiliza a função CubicSpline do pacote importado
cs = CubicSpline(x, y)
#Bloco 4: passa os inputs definidos o cálculo das taxas interpoladas no gráfico
xs = np.arange(1, 3.1, 0.1)
plt.figure(figsize=(10, 10))
plt.plot(x, y, 'o', label='vertices')
plt.plot(xs, cs(xs), label="CubicSpline")
plt.xlim(1, 3)
plt.legend(loc='lower left', ncol=3)
plt.show()
```

Fonte: Elaborada pelos autores.

O primeiro bloco do programa importa os pacotes necessários para o tratamento de vetores de dados, no caso, os dos eixos x e y, o cálculo da interpolação via cubic spline e de alguns recursos para plotarmos o gráfico das taxas interpoladas.

---

Aos que estão familiarizados com programação, podem observar que, no segundo bloco do código, os prazos 1, 2 e 3 são passados ao vetor “x” e as taxas dos vértices, 14, 15 e 13,5 designadas ao vetor “y”. O terceiro bloco do código demonstrado anterior simplesmente utiliza a função “CubicSpline” que já está implementada pelo pacote importado. Finalmente, o quarto bloco do código passa os parâmetros para gerar e formatar o gráfico a seguir:

Gráfico 5.3 – Gráfico do exemplo de interpolação via cubic spline no Python
![img-11.jpeg](img-11.jpeg)
Fonte: Elaborado pelos autores.

Esperamos que esse exemplo faça com que o estudante de renda fixa compreenda como a computação é uma aliada fundamental na solução de problemas da área.

# 5.5 Outras técnicas de estimação da ETTJ

Em certas situações é virtualmente impossível traçar uma ETTJ totalmente arbitrada por meio de técnicas de interpolação, como aquelas aqui apresentadas anteriormente. Podemos tratar de um mercado em que os instrumentos não dispõem de liquidez.

Também podemos estar interessados em formas de parametrização da curva de juros para utilização em hedge de carteiras, modelagem econométrica, trading quantitativo etc.

Para essas situações, existe o que chamamos de estimação da curva de

---

juros, que vem a ser a aplicação de técnicas de regressão para obtenção de parâmetros que descrevem o formato da curva em um determinado momento.

A seguir, veremos alguns métodos importantes de estimação da ETTJ, sem, no entanto, esgotar o rol de modelos disponíveis.

## 5.5.1 Nelson Siegel

O modelo de Nelson e Siegel consegue ajustar a ETTJ por meio da resolução de uma equação diferencial para as taxas forward¹⁰ e integrá-la para obter a curva spot de juros. O ajuste de curvatura característico das curvas de juros reais é conseguido com a introdução de um parâmetro de formato¹¹, que é calculado de modo a maximizar a estatística R² da regressão em MMQO do modelo a seguir.

A curva spot que representa a ETTJ no modelo de Nelson e Siegel (1987)¹² é:



R(m) = beta_0 + beta_1 [1 - exp(-m/τ)] / (m/τ) + beta_2 [[1 - exp(-m/τ)] / (m/τ) - exp(-m/τ)] 



Como pode ser visto da equação, fixado o parâmetro τ, todos os termos que acompanham os regressores podem ser calculados para uma determinada data.

Esse modelo parcimonioso consegue, com a utilização do parâmetro τ, descrever a curva forward de maneira simples, diferentemente do que existia até então, com modelos altamente não lineares.

Como os limites da segunda e da terceira parcelas tendem a zero quando o prazo tende ao infinito, o termo beta_0 é chamado de fator de longo prazo, uma vez que é para essa taxa que o modelo está convergindo naquele momento.

A segunda parcela tende a zero quando o prazo tende ao infinito, logo, beta_1 é chamado de fator de curto prazo.

A terceira parcela tem um comportamento interessante. Ela atinge um pico em algum prazo intermediário e depois decresce monotonicamente até zero, no infinito. Logo, é um fator de médio prazo.

Uma forma alternativa de escrever a equação apresentada anteriormente é utilizando o parâmetro λ = 1/τ:

(5.8)

---



y ₖ (m) = beta₁ + beta₂ (1 - e^(- λ m)/λ m) + beta₃ (1 - e^(- λ m)/λ m - e^(- λ m))



O parâmetro λ é a taxa de decaimento exponencial. Valores pequenos de λ geram decaimentos lentos, logo, ajustarão melhor a curva para prazos longos. Valores mais altos de λ geram decaimentos rápidos e ajustarão melhor a curva de juros no curto prazo. O valor de λ também serve para definir o ponto de máximo do efeito de médio prazo capturado por beta₃.

Ocorre que, em algumas situações, o ajuste não é muito bom. Em seu artigo, Nelson e Siegel argumentam que algumas datas podem ter cotações tomadas em momentos distintos, o que faz com que surjam distorções na dinâmica do modelo.

## 5.5.2 Svensson

Svensson, em seu artigo de 1994, inclui um outro termo na equação de Nelson e Siegel com o intuito de melhorar a aderência do último em certas situações, como em curvas com formatos em S bem pronunciados, por exemplo. Esse termo beta₃ é o regressor de uma parcela que contém o quarto termo da equação, com inclusão do parâmetro nu₂.

A equação do modelo de Svensson (1994) é:



{l}
i (m; b) = beta₀ + beta₁ 1 - exp (- m/nu₁)/m/nu₁ + beta₂ (1 - exp (- m/nu₁)/m/nu₁ - exp (- m/nu₁)) tag {5.9} 

+ beta₃ (1 - exp (- m/nu₂)/m/nu₂ - exp (- m/nu₂))




A função de Svensson é estimada com Método de Máxima Verossimilhança, embora o Método dos Mínimos Quadrados Não Lineares ou Método dos Momentos Generalizados também possam ser utilizados.

## 5.5.3 Super-Bell

O modelo Super-Bell foi desenvolvido pela Bell Canada Limited nos anos 1960.

Esse modelo utiliza uma regressão linear múltipla de taxas e retorno (YTM) contra uma lista de variáveis que são potências diversas do prazo e dois termos com as taxas de cupom do título.



Y_(M, C) = beta₀ + beta₁ (M) + beta₂ (M ²) + beta₃ (M ³) + beta₄ (M^(0. 5)) + beta₅ (log M) + beta₆ (C) + beta₇ (C. M) + ε tag {5.10}



---

O que se busca é gerar a TIR dos títulos ao par.

Uma primeira rodada de regressão calcula os coeficientes betas para uma cesta razoável de títulos e quantidade de vencimentos.

Essa regressão é realizada em *cross section*, ou seja, vários títulos cujos preços são tomados no mesmo instante de tempo.

A partir desse vetor de parâmetros β, um vetor de YTM ao par é calculado fazendo-se na equação anterior que Y(C,M) = C^(13).



Y_(M,C) = beta_0 + beta_1(M) + beta_2(M^2) + beta_3(M^3) + beta_4(M^(0.5)) + beta_2(log M)/1 - + beta_6 + beta_7(M) + ε 



De posse do vetor Y_M resultante da regressão "alisada" pelo modelo da Equação 5.6 e os dados de vencimento dos títulos em questão, roda-se o modelo sem os termos de cupons de juros, conforme a equação a seguir:



Y_M = beta_0 + beta_1(M) + beta_2(M^2) + beta_3(M^3) + beta_4(M^(0.5)) + beta_5(log M) + ε 



A partir do modelo anterior, chega-se à curva "ao par" suavizada.

As taxas calculadas são taxas de retorno, logo, é necessário o procedimento de bootstrapping para cálculo das curvas forward e spot.

## Resumo

Este capítulo mostra os cálculos para as diferentes formas de interpolações de taxas de juros. A interpolação é um processo que permite estimar uma taxa de juros não observada.

9 Medida do padrão de oscilação da taxa.

10 As taxas forward são as taxas de juro estimadas pelo mercado para períodos que se iniciam e terminam no futuro. Exemplo: se o mercado espera que entre as próximas reuniões do Copom a taxa de juros vai ser de 12% a. a., essa é a taxa forward nesse período. A curva pré nada mais é então que o acumulado das taxas forward mais um prêmio de risco.

11 T = 1/4, para facilitar a álgebra e as regressões, muda-se a variável tau por lambda.

12 A notação utilizada na equação é análoga àquela dos artigos originais.

13 Tudo se passa como se os títulos estivessem sendo emitidos naquele exato momento. Assim, para t = 0, admitindo que não houvesse ágio ou deságio no leilão, o cupom de juros do título seria a sua YTM.

---

# Exercícios propostos

1. Dados os prazos de 252 e 504 dias úteis e as respectivas taxas de 8% e 7% a. a., interpole a taxa para 300 dias úteis pelos métodos flat forward e por interpolação linear.
2. Descreva o procedimento do cálculo da interpolação via cubic spline.

---

# Capítulo 6
Títulos públicos federais brasileiros

Da mesma forma que para outros instrumentos financeiros, os títulos de renda fixa são precificados de acordo com um modelo que consiste no desconto do valor dos fluxos de caixa que o título (instrumento) oferece. O cálculo do preço teórico de um título genérico pode ser representado pela equação a seguir:



P = Σ(k=1 até n) FC_k/(1 + I_k)^k 



A seguir, são listadas possíveis equações de apreciação que, invariavelmente, cairão na estrutura da equação anterior, sendo adaptada para incorporar o universo dos títulos de renda fixa, que, em regra, incorpora os títulos:

- prefixados: que apresentam fluxo de pagamento constante;
- indexados à inflação;
- com taxa flutuante: no Brasil, a taxa flutuante mais comum é a Selic, que varia diariamente.

## 6.1 Definição

São os títulos emitidos por órgãos da administração pública, como governo central, estados e municípios.

Os títulos públicos federais são os títulos emitidos pelo Tesouro Nacional e têm por finalidade o financiamento das atividades do Governo.

A partir do momento em que o consolidado do Governo apresenta déficit, este deve poder ser financiado com a emissão desses papéis.

A Secretaria do Tesouro Nacional (STN) é o órgão central do sistema de administração financeira nacional e também de controle interno do Ministério da Fazenda.

Os objetivos da STN são os seguintes:

---

a) controle da administração da dívida pública federal, seja monetária ou contratual, interna ou externa;
b) gerenciamento de todos os compromissos do governo federal em uma única unidade governamental.

A emissão primária dos títulos públicos, que corresponde à venda inicial dos títulos no mercado, é realizada, principalmente, por meio de leilões competitivos, nos quais os bancos e outras instituições participantes do mercado colocam suas propostas de compra.

Após a oferta inicial no mercado primário, com a venda dos títulos do Tesouro para instituições financeiras, esses papéis passam a ser transacionados no mercado secundário, que é o mercado em que os títulos são transacionados entre bancos, fundos etc.

No Brasil, diferentemente do que ocorre em diversos países, os títulos são transacionados no mercado por uma taxa de juros ou um spread de taxa de juros. Spread é compreendido como um adicional de taxa cobrado sobre uma taxa de referência.

Nos itens adiante são descritos os títulos federais mais comuns e as suas equações de precificação, seguindo o modelo teórico de não arbitragem utilizado na teoria.

## 6.1.1 Letras do tesouro nacional (LTN)

Características principais:

- Título escritural, nominativo e negociável;
- Prefixado e sem pagamento de cupom de juros (zero-coupon bond);
- Valor de resgate é o valor de face previamente definido (R$ 1.000);
- Taxa de juros é efetiva na base de 252 dias por ano.

Preço de mercado:



P_(LTN) = 1.000/(1 + i)^(dtu/252) 



Onde:

P_(LTN): preço de mercado da LTN

i: taxa de juros prefixada para esse vencimento

---

du: Quantidade de dias úteis até o vencimento

As LTNs são títulos de curto prazo e são negociadas no mercado financeiro pela taxa de juros i de mercado.

## 6.1.2 Nota do tesouro nacional série f (NTN-F)

Características principais:

- Título escritural, nominativo e negociável;
- Título com taxa de cupom prefixada de 10% a. s.;
- Juros são pagos semestralmente;
- Taxa de juros de mercado de negociação é uma taxa efetiva anual, na base de 252 dias por ano.

Preço de mercado:



P_(NTN-F) = Σ(k=1 até n) FC_k/(1 + i_k)^(du_k/252) 



Com:

FC_k = r × 1.000 para k ≠ n e FC_k = r × 1.000 + 1000 para k = n.

Onde:

P_(NTN-F): preço da NTN-F

du_k: fluxo de caixa do vencimento k

i_k: taxa de juros do mercado de NTN-Fs para o vencimento k

r: taxa de cupom da NTN-F trazida para a forma de cotação semestral

Para as NTN-Fs com taxa de cupom de 10% a. s. o cupom semestral é igual a √(1,10) - 1 = 4,88\% a. s.

As NTN-Fs são negociadas no mercado financeiro por uma taxa interna de retorno y, ou yield, que substitui, nesse processo, as taxas de juros i_k:



P_(NTN-F) = Σ(k=1 até n) FC_k/(1 + i_k)^(du_k/252) = Σ(k=1 até n) FC_k/(1 + y)^(du_k/252) 



## 6.1.3 Letra financeira do tesouro (LFT)

Características principais:

---

- Título escritural, nominativo e negociável;
- Rendimento pós-fixado (flutuante) indexado à taxa Selic;
- Resgate é o valor nominal (R$ 1.000 na data de emissão) acrescido ao acumulado da taxa Selic observada entre o dia da emissão e o dia útil anterior ao resgate;
- É negociado com ágio ou deságio, dependendo das condições do mercado de dívida pública federal e risco de crédito percebido pelos credores dessa dívida;
- Não apresenta pagamento de cupom de juros, são pagos só no vencimento;
- Taxa de juros de negociação é uma taxa efetiva na base de 252 dias por ano.

Preço de mercado:



P_(LFT) = 1000 × ∏(k=0 até n-1) (1 + Selic_k)^(1/252)/(1 + TD)^(du_r/252) 



Onde:

P_(LFT): preço da LFT na data n

TD^(14): taxa anual de deságio (positiva) ou ágio (negativa) ao ano (base 252 dias úteis) na negociação em mercado

du_r: dias úteis restantes até o vencimento do papel

Selic_k = taxa Selic é uma taxa ao ano, base 252 dias úteis, calculada pelo Bacen, representando a média das taxas de mercado das operações de empréstimo de 1 dia útil, entre instituições financeiras, as chamadas operações overnight, garantidas por títulos públicos federais. Tais operações são conhecidas no mercado internacional como operações repurchase agreement¹⁵ ou, simplesmente, operações repo. No Brasil, essas operações também são chamadas de compromissadas.

n = número de dias úteis entre a data de emissão e o dia do vencimento

## 6.1.4 Nota do tesouro nacional série b (NTN-B)

Características principais:

---

- Título escritural, nominativo e negociável;
- Pós-fixado com valor de face atualizado pela variação do IPCA;
- Paga juros semestrais sobre o valor nominal atualizado, em geral 6% a. s.;
- A taxa de juros de negociação, chamada de taxa de cupom de IPCA é uma taxa efetiva, exponencial e com base em 252 dias por ano.

Preço de mercado:



P_(NTN-B) = IPCA_t/IPCA_0 Σ(k=1 até n) FC_k/(1 + i_k)^(du_s/252) 



Com:

FC_k = r × 1.000 para k = n e FC_k = r × 1.000 + 1000 para k = n.

Onde:

P_(NTN-B): preço da NTN-B na data t

FC_k: fluxo de caixa do vencimento k

i_k: taxa de juros^(16) do mercado de NTN-Bs para o vencimento k

r: taxa de cupom semestral da NTN-B

Para uma taxa de cupom de 6% a. s. tem-se um cupom semestral de √(1,06) - 1 = 2,9563\% a. s.

IPCA_t: Índice de preços ao consumidor amplo divulgado pelo Instituto Brasileiro de Geografia e Estatística (IBGE), atualizado e projetado pela Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais (Anbima), ou seja, é feito um pró-rata com base na inflação esperada no mês corrente^(17).

IPCA_0: índice IPCA da data-base, definida pelo Tesouro em 15 de julho de 2000, definida em R$ 1.000,00 para todas as NTN-Bs

n = número de pagamento de cupom de juros até o vencimento

A equação pode ser escrita tanto com a utilização das taxas spot quanto com a utilização da TIR:

(6.7)

---



P_(NTN-U) = IPCA_t/IPCA_0 Σ(k=1 até n) FC_k/(1 + i_k) du_k/252 = IPCA_t/IPCA_0 Σ(k=1 até n) FC_k/(1 + y) du_k/252



Na prática, o mercado negocia o título pela TIR. Para precificar esse título por meio de taxas spot, é necessário o bootstrap, que abordaremos adiante. Assumindo a condição de não arbitragem, o preço do papel calculado pela TIR deve ser o mesmo do que o preço calculado por taxas spot de cupom de IPCA.

## 6.1.5 Nota do tesouro nacional série c (NTN-C)

Características principais:

- Título escritural, nominativo e negociável;
- Pós-fixado com valor de face atualizado pela variação do IGP-M;
- Paga juros semestrais sobre o valor nominal atualizado, normalmente de 6% a. a.¹⁸;
- A taxa de mercado de negociação, conhecida como taxa de cupom de IGPM, é uma taxa efetiva, exponencial e com base em 252 dias por ano.

Preço de mercado:



P_(NTN-C) = IGPM_t/IGPM_0 Σ(k=1 até n) FC_k/(1 + i_k) du_k/252 



FC_k = r × 1.000 para k = n e FC_k = r × 1.000 + 1000 para k = n.

Onde:

P_(NTN-C): preço da NTN-C na data t

du_r: fluxo de caixa do vencimento k

i_k: taxa de juros¹⁹ do mercado de NTN-Cs para o vencimento

r: taxa de cupom da NTN-C ao semestre, 2,9563% para as NTN-Cs com taxa de cupom de 6% a. a.

IGPM_t: índice geral de preços divulgado pela Fundação Getulio Vargas, atualizado e projetado pela Anbima, ou seja, é feito um pró-rata do IGP-M com base no IGP-M esperado do mês corrente²⁰

---

IGPM_0: Índice IGP-M da data-base, definida pelo Tesouro em 1 de julho de 2000.

n: número de pagamentos de cupom de juros até o vencimento

A Equação 6.7 pode ser escrita tanto com a utilização das taxas spot quanto com a utilização da TIR:



P_(NTN-B) = IGPM_0/IGPM_0 Σ(k=1 até n) FC_k/(1 + i_k)^(dalpha_k/252) = IGPM_0/IGPM_0 Σ(k=1 até n) FC_k/(1 + y)^(dalpha_k/252) 



## 6.1.6 Nota do tesouro nacional série d (NTN-D)

Características principais:

- Título escritural, nominativo e negociável;
- Pós-fixado com valor de face atualizado pela variação do dólar dos Estados Unidos;
- Paga juros semestrais sobre o valor nominal atualizado;
- A taxa de mercado de negociação desse papel é uma taxa interna de retorno ao ano, nominal, capitalização semestral, conhecida como taxa de cupom cambial de NTN-D.

Preço de mercado:



P_(NTN-D) = USD_(t-1)/USD_(t=0) Σ(k=1 até n) FC_k/(1 + y/2)^(dc_k/100) 



Com:

FC_k = r × 1.000 para k ≠ n e FC_k = r × 1.000 + 1000 para k = n.

Onde:

P_(NTN-D): preço da NTN-D da data t

FC_k: fluxo de caixa do vencimento k

i_k: taxa de juros²¹ do mercado de cupom cambial de NTN-Ds para o vencimento k

r: taxa de cupom semestral da NTN-D, em geral, 6% a. a. ou 3% a. s.

dc_k: dias corridos entre o dia de avaliação do preço e a data de pagamento do cupom k de juros

---

USD_(t-1): PTAX de venda no dia útil anterior à precificação

USD_(t=0): PTAX de venda no dia útil anterior à emissão

Note que, por questões operacionais, a correção cambial desse papel é dada pela variação da taxa de câmbio PTAX observada entre o dia anterior ao da emissão e o dia do cálculo. Assim, a taxa de juros associada a esse tipo de correção cambial recebe o nome de cupom cambial sujo, de forma a diferenciá-la da taxa de juros de papéis corrigidos pela variação cambial sem essa defasagem de um dia.

O Tesouro Nacional resgatou a totalidade das NTN-Ds em circulação. O título foi mantido no texto por questões didáticas.

Da mesma forma que os outros papéis, é possível também expressar a NTN-D por uma TIR, da seguinte forma:



P_(NTN-D) = USD_(t-1)/USD_(t=0) Σ(k=1 até n) FC_k/(1 + i_k dC_k/360) = USD_(t-1)/USD_(t=0) Σ(k=1 até n) FC_k/(1 + Σ(i=2 até n) dc_k/180) 



## 6.2 Precificação

Como já mencionado anteriormente, a precificação de títulos de renda fixa é realizada por meio do desconto de seu fluxo de caixa esperado pelas taxas de juros vigentes na economia (ETTJ ou curva de juros, no jargão do mercado).

As equações anteriores, que foram introduzidas com menção ao preço de mercado, são, na verdade, equações de não arbitragem²².

Vamos explorar o conceito por meio de exemplos práticos.

## 6.2.1 Exemplo: precificação de uma NTN-F

Considere uma NTN-F com o seguinte cronograma de vencimentos:

Figura 6.1 – Fluxos de caixa de uma NTN-F

---

![img-12.jpeg](img-12.jpeg)
Fonte: Elaborada pelos autores.

E dada a estrutura a termo de taxas de juros (curva de juros) para esse dia:

Gráfico 6.1 – Exemplo de ETTJ
![img-13.jpeg](img-13.jpeg)
Fonte: Elaborado pelos autores.

Vamos calcular os itens a seguir:

a) Qual o valor dos cupons de juros semestrais recebidos pelo detentor do papel se a taxa de cupom é de 10% a. a.?
b) A partir dos valores desses cupons de juros, mostre quais são os valores de du_1, FC_2, FC_2 e FC_4.
c) Com base na resposta da alternativa b) e na curva de juros, qual o preço máximo que você pagaria por esse papel?
d) Qual a TIR correspondente?

## Solução

a) Como visto anteriormente, a NTN-F paga cupons de juros semestrais, com taxa anual de juros de 10%.

Fazendo a conversão das taxas semestrais para anuais:



(1 + i_s)^2 = (1 + i_a)



Assim:

---



(1 + i_x)^2 = (1 + 10\%)



Então:



i_x = √(1,1) - 1 = 4,88\%  a. s.



b) Para um valor de face de R$ 1000, os cupons de juros serão dados por 4,88\% × 1000 = 48,8805, e o fluxo de caixa no vencimento será de 4,88\% × 1000 + 1000 = 1.048,8805.

c) O preço de mercado teórico será obtido pelo fluxo de caixa descontado do papel:



P_(NTN-F) = 48,81/(1 + 14.5\%)^(75) + 48,81/(1 + 15\%)^(201) + 48,81/(1 + 15,6\%)^(227) + 1048,81/(1 + 16\%)^(453) = 934,18



Esquematicamente, em uma planilha MS Excel:

Tabela 6.1 – Cálculo do preço da NTN-F pela ETTJ

|  Dias úteis | Fluxo de caixa | ETTJ | VP ETTJ  |
| --- | --- | --- | --- |
|  75 | 48,81 | 14,50% | 46,88  |
|  201 | 48,81 | 15,00% | 43,66  |
|  327 | 48,81 | 15,60% | 40,44  |
|  453 | 1048,81 | 16,00% | 803,20  |
|   |  | Preço | 934,18  |

Fonte: Elaborada pelos autores.

d) O mercado utiliza como referência (inclusive para apregoação) a TIR do papel. Como foi visto anteriormente, precisamos construir uma função do tipo:



f(y) = 934,18 - 48,81/(1 + y)^(100/252) + 48,81/(1 + y)^(201/252) + 48,81/(1 + y)^(327/252) + 1048,81/(1 + y)^(453/252)



Quando f(y) → 0, y → TIR

Essa equação não tem solução analítica. Para resolvê-la temos de usar o Solver do MS Excel, formatando o problema na planilha.

Tabela 6.2 – Cálculo do preço da NTN-F pela TIR

|  Dias úteis | Fluxo de caixa | ETTJ | VP ETTJ | VP TIR  |
| --- | --- | --- | --- | --- |
|  75 | 48,81 | 14,50% | 46,88 | 46,71  |

---

|  201 | 48,81 | 15,00% | 43,66 | 43,37  |
| --- | --- | --- | --- | --- |
|  327 | 48,81 | 15,60% | 40,44 | 40,28  |
|  453 | 1048,81 | 16,00% | 803,20 | 803,82  |
|   |  | Preço | 934,18 | 934,18  |
|   |  |  | y | 15,95%  |
|   |  |  | f(y) | 0,00  |

Fonte: Elaborada pelos autores.

## 6.2.2 Exemplo: precificação de uma NTN-B

Em 18/10/2017 a NTN-B de vencimento em 15/8/2020 fechou o dia sendo negociada a R$ 3.221,40.

**Responda:**

a) Qual a taxa de cupom semestral da NTN-B?
b) Esboce o fluxo de caixa desse papel no tempo.
c) Dado que o IPCA acumulado até essa data mais o pró-rata da inflação esperada é 3,01309, calcule a TIR desse papel.

## Solução

a)



(1 + i_s)^2 = (1 + i_a)





(1 + i_s)^2 = (1 + 6\%)





i_s = 2,9563\%  a. s.



b)

![img-14.jpeg](img-14.jpeg)
Figura 6.2 – Fluxograma real NTN-B 2020 considerando os feriados previstos em 18/10/2017

---

Fonte: Elaborada pelos autores.

c)

O cálculo da TIR é análogo aos exercícios anteriores, porém com a inclusão do IPCA acumulado:

Vamos criar uma função:



f(y) = P_(mercado) - P_(modelo)





f(y) = P_(mercado) - IPCA_t/IPCA_0 Σ(k=1 até n) FC_k/(1 + y)^(dn_k/252)



Quando f(y) → 0 y → TIR

Aplicando a equação aos dados do enunciado, teremos:



P_(mercado) = IPCA_t/IPCA_0 Σ(k=1 até n) FC_k/(1 + y)^(dn_k/252)





3.221,4009 = 3,01309 × [ Σ(k=1 até 6) 29,5630/(1 + y)^(dn_k/252) + 1000/(1 + y)^(709/252) ]



Em uma tabela MS Excel simples, como a que está abaixo, podemos construir o modelo com os dados apresentados anteriormente e, através do recurso Atingir Metas do Excel, verificar que a TIR do papel é 3,75\% a.a., ou seja, a taxa que faz com que o valor do "Preço modelo" da tabela abaixo convirja com o PU da Anbima.

Tabela 6.3 – Exemplo de modelo de precificação da NTN-B

|  Data dos fluxos de caixa | Fluxo de caixa | Dias úteis | Valor Presente  |
| --- | --- | --- | --- |
|  15/2/2018 | 29,56 | 80 | 29,22  |
|  15/8/2018 | 29,56 | 206 | 28,69  |
|  15/2/2019 | 29,56 | 332 | 28,17  |
|  15/8/2019 | 29,56 | 456 | 27,67  |
|  17/2/2020 | 29,56 | 585 | 27,15  |
|  17/8/2020 | 1029,56 | 709 | 928,65  |
|   |  | Soma | 1.069,5483  |
|   |  | PU Anbima | 3.221,4009  |
|   |  | IPCA acumulado | 3,0106  |
|   |  | IPCA projetado | 0,45%  |
|   |  | IPCA pró-rata | 301%  |

---

Preço modelo 3.221,4
VPL 0

Fonte: Elaborada pelos autores.

## Resumo

Este capítulo apresenta os diferentes títulos públicos no mercado brasileiro, assim como as formas de precificá-los.

14 As LFTs são negociadas no mercado financeiro pela taxa de ágio ou deságio. Esse ágio ou deságio representa a remuneração acima ou abaixo da taxa Selic a ser recebida por um investidor que fique com o papel até o vencimento. Assim, por exemplo, uma LFT com vencimento em 530 dias, negociada a uma taxa de 0,10% a. a. vai render ao investidor uma remuneração igual à taxa Selic média dos próximos 530 dias mais 0,10% a. a., aproximadamente.

15 As operações compromissadas são realizadas pelo Bacen de modo a fazer um ajuste fino da política monetária, ou seja, garantir que a taxa Selic gravite ao redor da meta Selic ao longo do dia por meio de captações ou empréstimos realizados junto às instituições financeiras.

16 Esse papel é negociado em mercado com uma taxa interna de retorno y acima da variação acumulada do IPCA, taxa essa de juros conhecida como cupom de IPCA. A correção do valor principal das NTN-Bs pelo IPCA dá-se sempre no dia 15 de cada mês. Nas datas intermediárias faz-se uma correção pró-rata com base em um consenso de IPCA divulgado.

17 A estimativa usada pelo mercado é a da Anbima.

18 A exceção é a NTN-C, que vence em 1º de janeiro de 2031, que tem a taxa de juros semestrais definida em 12% a. a.

19 Esse papel é negociado em mercado com uma taxa interna de retorno y, acima da variação acumulada do IGPM, taxa essa de juros conhecida como cupom de IGPM. A correção do valor principal das NTN-Cs pelo IGPM dá-se sempre no dia 1 de cada mês. Nas datas intermediárias faz-se uma correção pró-rata com base em um consenso de IGPM divulgado pela Anbima. O resgate das NTN-Cs ocorre no primeiro dia útil do mês de seu vencimento.

20 A estimativa usada pelo Mercado é a da Anbima.

21 Esse papel é negociado em mercado com uma taxa interna de retorno y, nominal, com capitalização semestral, acima da variação cambial, taxa essa de juros conhecida como cupom cambial ou cupom de dólar.

22 Pela teoria de não arbitragem, o valor futuro de um instrumento financeiro que oferece o mesmo risco que outro tem de ser igual ao valor futuro desse outro, independente dos indexadores de ambos.

---

# Exercícios propostos

1. Para uma NTN-F vencendo em 720 dias úteis:

a. Preencha a tabela a seguir:

|  Dias úteis | ETTJ | Fluxo de caixa | Valor Presente do fluxo de caixa  |
| --- | --- | --- | --- |
|  90 | 9,03% |  |   |
|  216 | 8,60% |  |   |
|  342 | 8,71% |  |   |
|  468 | 9,02% |  |   |
|  594 | 9,37% |  |   |
|  720 | 9,70% |  |   |

Preço:

b. Calcule a TIR dessa NTN-F para essa data.
c. Este papel está sendo negociado com ágio ou deságio? Por quê?
d. Esboce um gráfico do preço desse papel em relação à TIR (preço nas ordenadas e TIR nas abscissas).

2. Em 18/10/2017 a NTN-B de vencimento em 15/8/2022 fechou o dia sendo negociada a R$ 3.250,386409. A tabela de fluxos de caixa com os dados de fluxos de caixa do papel é dada a seguir:

|  Data cupons | Fluxo de caixa | Dias úteis | Valor Presente  |
| --- | --- | --- | --- |
|  15/2/2018 |  | 80 |   |
|  15/8/2018 |  | 206 |   |
|  15/2/2019 |  | 332 |   |
|  15/8/2019 |  | 456 |   |
|  15/2/2020 |  | 585 |   |
|  15/8/2020 |  | 709 |   |
|  15/2/2021 |  | 834 |   |
|  15/8/2021 |  | 959 |   |

---

|  15/2/2022 | 1.086  |
| --- | --- |
|  15/8/2022 | 1.210  |

Responda:

a. Esboce o fluxo de caixa desse papel no tempo.
b. Dado que o IPCA acumulado até essa data mais o pró-rata da inflação esperada é 3,01309 (301,309% no período, desde a data de referência definida pelo Tesouro, 15/7/2000), calcule a TIR desse papel.

---

Capítulo 7
Precificação de títulos de dívida externa brasileira

## 7.1 Definição

Apesar de todos os títulos públicos federais serem soberanos na acepção da palavra, que se refere ao fato de ser uma república ou estado nacional que os está emitindo, o jargão título soberano consagrou-se como sendo aplicado aos títulos de dívida externa.

Os títulos de dívida externa são aqueles emitidos e liquidados em moeda estrangeira fora do país. No Capítulo 6, introduzimos de um título indexado à moeda estrangeira (NTN-D), porém liquidado no Brasil, em reais.

Essa diferença é crucial, uma vez que pode existir uma situação em que a moeda estrangeira tenha cotação, mas seja inacessível naquela localidade, naquele momento.

Isso não acontece com os títulos de dívida externa, que têm de ser liquidados fora do país, com a moeda constante de sua escritura²³. Na hipótese de o país não possuir essa divisa em quantidade suficiente, um evento de inadimplência estará caracterizado.

## 7.2 Global bonds

Nos anos 1990, o Brasil e outros países em desenvolvimento foram forçados a reestruturar suas dívidas externas. O plano Brady²⁴ foi a estratégia formal utilizada por esses países para executar a troca de dívida antiga, inadimplida, por títulos novos.

Os países que aderiram ao plano foram, na ordem, Argentina, Brasil, Bulgária, Costa Rica, República Dominicana, Equador, México, Marrocos, Nigéria, Filipinas, Polônia e Uruguai.

Os papéis Par Bond, Discount Bond, Front Loaded Interest Reduction

---

Bond (FLIRB), Front Loaded Interest Reduction Bond with Capitalization (C-Bond), Debt Conversion Bond, New Money Bond e Eligible Interest Bond foram emitidos na época, em abril de 1994. Posteriormente, foram substituídos pelos Globals, que permanecem até hoje.

Os globals são títulos com características bem semelhantes com o padrão observado em títulos emitidos pelos países desenvolvidos. São denominados, principalmente, em dólares, podendo ser também denominados em euros e reais. Seguem o padrão americano de amortização com frequência semestral de pagamento de juros.

## 7.3 Precificação de global bonds

A precificação de global bonds segue o mesmo fundamento observado na precificação de títulos domésticos, com algumas diferenças importantes. As principais são a contagem de dias e a apregoação pelo preço limpo.

No caso dos títulos emitidos internamente, a contagem de dias, como já visto anteriormente, é feita em anos de 252 dias úteis (DU/252), enquanto a contagem de dias para títulos emitidos externamente é feita pela convenção (30/360).

## 7.3.1 Apropriação de juros

Para os títulos da dívida externa brasileira, a apropriação de juros é realizada na forma linear. Assim, a curva do papel cresce até o dia anterior à data de pagamento do cupom.

## 7.3.2 Preço limpo

No Brasil, os títulos são negociados pela taxa interna de retorno. Já os títulos emitidos fora do país são negociados pelo preço limpo. O preço limpo é igual ao preço do título (também chamado de "sujo") descontado dos juros apropriados em percentual do valor de face. A razão disso é que por meio desse desconto é possível avaliar exatamente tanto a qualidade de crédito do emissor quanto o nível das taxas de juros, sem o ruído dos pagamentos intermediários de cupom e de amortizações.

O título é apregoado pelo preço limpo, mas é liquidado pelo preço com juros, logo, o detentor do título recebe a remuneração por ter carregado o papel até aquela data intermediária.

Assim, o preço em moeda estrangeira (USD é a mais comum) de um global

---

é relacionado com sua taxa interna de retorno por meio da seguinte equação:



P_(G l o b a l) = Σ(k = 1) ^n F C ₖ/(1 + Y/2)^(d c ₖ/1 0 0) tag {7.1}



A Equação 7.1 mostra o cálculo do preço de um global em função da yield to maturity.

Com:

FCₖ = r × 100 para k ≠ n e FCₖ = r × 100 + 100 para k = n.

Onde:

x₁ = 2: preço do global em USD

P_(LPT): fluxo de caixa do título na posição k

y: yield to maturity (taxa interna de retorno)

du₁: dias corridos (com a convenção 30/360)

Os juros apropriados serão calculados linearmente:



J u r o s A c r u a d o s = d c_(p a s s a d o s)/d c_(t o t a l) × 1 0 0 × r/2 tag {7.2}



Onde:

dc_(passados): dias corridos entre a data de pagamento do último cupom pago e a data atual

dc_(total): dias corridos entre a data de pagamento do último cupom pago e a data de pagamento do próximo cupom

O preço limpo ou de apregoação será a diferença entre o preço sujo e os juros apropriados:



P_(L i m p o) = P_(S u j o) - J u r o s A c r u a d o s/V a l o r d e F a c e tag {7.3}



## 7.3.3 Spread over treasury

É a remuneração que o papel apresenta acima de um título de vencimento próximo emitido pelo governo dos Estados Unidos.

É uma medida de risco soberano. Quanto maior o risco (de crédito e

---

outros) percebido, maior deve ser a remuneração paga pelo país para obter recursos no estrangeiro.

## 7.3.4 Exemplo: precificação de um global 2016

Precifique um global 2026 emitido pela República Federativa do Brasil para o dia 7/7/2017.

As características dadas a seguir foram extraídas do boletim “Informe da Dívida”, divulgado pela STN em março de 2017:

Figura 7.1 – Dados do global 2026

|  Data da emissão | 10/3/2016 | 7/3/2017  |
| --- | --- | --- |
|  Prazo | 10 anos | 10 anos  |
|  Vencimento | 7/4/2026 | 7/4/2026  |
|  Cupom de juros | 6,0% a.a. | 6,0% a.a.  |
|  Preço de emissão | 99,066% do valor de face | 107,213% do valor de face  |
|  Yield | 6,125% a.a. | 5,000% a.a.  |
|  Spread sobre US Treasury | 419,6 pbs | 248,4 pbs  |
|  Pagamento do principal | em parcela única, no vencimento | em parcela única, no vencimento  |
|  Pagamento dos juros | em parcelas semestrais | em parcelas semestrais  |
|  Valor total da emissão | US$ 1,5 bilhão | US$ 1,0 bilhão  |

Fonte: Tesouro Nacional – CODIP.

Trata-se de uma emissão que foi realizada, inicialmente, em março de 2016 e reaberta em março de 2017.

Observe que, na primeira emissão, a TIR²⁵ foi de 6,125% a. a., maior, portanto, que a taxa de cupom de 6% a. a., logo, o título foi emitido com deságio em relação ao valor de face, o que pode ser visto na linha “preço de emissão”, que tem o valor de 99,066%²⁶.

Na segunda janela, a curva de juros em USD para o Brasil havia se movido para baixo, fazendo com que o preço do título aumentasse para 107,213% do valor de face, ou seja, apurando um ágio, o que também pode ser visto

---

pela TIR que foi para 5% a. a. naquele momento.

O spread over treasury também caiu no período, mostrando que o movimento da curva também foi motivado pela queda percebida no risco soberano do Brasil.

Feitas as considerações, vamos aos cálculos, considerando:

|  Data atual | 07/07/2017  |
| --- | --- |
|  Data liquidação | 12/07/2017  |
|  Taxa de cupom | 6,000%  |
|  YTM (linear) | 5,0417%  |
|  YTM (exponencial) | 5,1050%  |

Nesse dia, a YTM do título foi 5.0417% a. a.

Para conciliar os preços com a YTM publicada, precisamos do fluxo de pagamentos do título:

Tabela 7.1 – Exemplo de fluxo de pagamentos

|  Data | Fluxo de caixa | Dias corridos | Valor Presente  |
| --- | --- | --- | --- |
|  7/10/2017 | 3 | 85 |   |
|  7/4/2018 | 3 | 265 |   |
|  7/10/2018 | 3 | 445 |   |
|  7/4/2019 | 3 | 625 |   |
|  7/10/2019 | 3 | 805 |   |
|  7/4/2020 | 3 | 985 |   |
|  7/10/2020 | 3 | 1165 |   |
|  7/4/2021 | 3 | 1345 |   |
|  7/10/2021 | 3 | 1525 |   |
|  7/4/2022 | 3 | 1705 |   |
|  7/10/2022 | 3 | 1885 |   |
|  7/4/2023 | 3 | 2065 |   |
|  7/10/2023 | 3 | 2245 |   |
|  7/4/2024 | 3 | 2425 |   |

---

|  7/10/2024 | 3 | 2605 |   |
| --- | --- | --- | --- |
|  7/4/2025 | 3 | 2785 |   |
|  7/10/2025 | 3 | 2965 |   |
|  7/4/2026 | 103 | 3145 |   |
|   |  | Preço | 108,27833  |
|   |  | Preço meta | 108,27833  |
|   |  | f(y) | 0,00000  |

Fonte: Elaborada pelos autores.

O MS Excel contém uma função que gera a convenção 30/360, que foi usada para gerar a coluna dias corridos da Tabela 7.1.

A coluna "Fluxo de caixa" segue a ideia do Sistema Americano. O valor de R$ 3 é igual à taxa de cupom sobre 2 (semestral) vezes o valor de face de R$ 100.

Podemos trocar a YTM reportada e calcular o preço sujo ou estabelecer o preço sujo e utilizar o "Atingir meta" para calcular a TIR.

Os dois são válidos para checarmos a mecânica de precificação desse papel.

O cálculo dos juros apropriados é dado conforme a seguir:

|  Data anterior | 7/4/2017  |
| --- | --- |
|  Próxima data | 7/10/2017  |
|  Total de dias corridos | 180  |
|  Total de dias passados | 95  |
|  Juros apropriados | 1,58333  |

E o preço limpo é o valor do preço sujo menos os juros apropriados, logo:



P_(Limpo) = 108.27833 - 1.58333 = 106.6950



Dadas as características do título global 45 do Brasil, verificar as características do apreciação do papel.

|  Papel | Global 45  |
| --- | --- |
|  Vencimento | 27/7/2045  |
|  Data | 09/10/2017  |
|  Prazo para liquidação | 2  |

---

|  Data liquidação | 11/10/2017  |
| --- | --- |
|  Coupon | 5,00%  |
|  YTM (linear) | 5,49%  |
|  YTM (exponencial) | 5,57%  |

O cálculo dos juros apropriados é dado por:

|  Juros apropriados  |   |   |
| --- | --- | --- |
|  Data anterior | 27/7/2017 |   |
|  Próxima data | 27/1/2018 |   |
|  Total dias corridos | 180 | (30/360)  |
|  Dias corridos passados | 74 | ACT  |
|  Juros apropriados | 10,28 |   |

E a planilha com detalhes do cálculo é:

Tabela 7.2 – Valor Presente fluxo de pagamentos

|  Data | Fluxo de caixa | Dias corridos | VP  |
| --- | --- | --- | --- |
|  27/1/2018 | 25 | 106 | 24,60  |
|  27/7/2018 | 25 | 286 | 23,95  |
|  27/1/2019 | 25 | 466 | 23,31  |
|  27/7/2019 | 25 | 646 | 22,68  |
|  27/1/2020 | 25 | 826 | 22,08  |
|  27/7/2020 | 25 | 1.006 | 21,49  |
|  27/1/2021 | 25 | 1.186 | 20,91  |
|  27/7/2021 | 25 | 1.366 | 20,35  |
|  27/1/2022 | 25 | 1.546 | 19,81  |
|  27/7/2022 | 25 | 1.726 | 19,28  |
|  27/1/2023 | 25 | 1.906 | 18,76  |
|  27/7/2023 | 25 | 2.086 | 18,26  |
|  27/1/2024 | 25 | 2.266 | 17,77  |
|  27/7/2024 | 25 | 2.446 | 17,30  |
|  27/1/2025 | 25 | 2.626 | 16,84  |
|  27/7/2025 | 25 | 2.806 | 16,39  |
|  27/1/2026 | 25 | 2.986 | 15,95  |
|  27/7/2026 | 25 | 3.166 | 15,52  |
|  27/1/2027 | 25 | 3.346 | 15,11  |
|  27/7/2027 | 25 | 3.526 | 14,70  |

---

|  Data | Fluxo de caixa | Dias corridos | VP  |
| --- | --- | --- | --- |
|  27/1/2028 | 25 | 3.706 | 14,31  |
|  27/7/2028 | 25 | 3.886 | 13,93  |
|  27/1/2029 | 25 | 4.066 | 13,46  |
|  27/7/2029 | 25 | 4.246 | 13,19  |
|  27/1/2030 | 25 | 4.426 | 12,84  |
|  27/7/2030 | 25 | 4.606 | 12,50  |
|  27/1/2031 | 25 | 4.786 | 12,16  |
|  27/7/2031 | 25 | 4.966 | 11,84  |
|  27/1/2032 | 25 | 5.146 | 11,52  |
|  27/7/2032 | 25 | 5.326 | 11,21  |
|  27/1/2033 | 25 | 5.506 | 10,91  |
|  27/7/2033 | 25 | 5.686 | 10,62  |
|  27/1/2034 | 25 | 5.866 | 10,34  |
|  27/7/2034 | 25 | 6.046 | 10,06  |
|  27/1/2035 | 25 | 6.226 | 9,79  |
|  27/7/2035 | 25 | 6.406 | 9,53  |
|  27/1/2036 | 25 | 6.586 | 9,28  |
|  27/7/2036 | 25 | 6.766 | 9,03  |
|  27/1/2037 | 25 | 6.946 | 8,79  |
|  27/7/2037 | 25 | 7.126 | 8,55  |
|  27/1/2038 | 25 | 7.306 | 8,32  |
|  27/7/2038 | 25 | 7.486 | 8,10  |
|  27/1/2039 | 25 | 7.666 | 7,88  |
|  27/7/2039 | 25 | 7.846 | 7,67  |
|  27/1/2040 | 25 | 8.026 | 7,47  |
|  27/7/2040 | 25 | 8.206 | 7,27  |
|  27/1/2041 | 25 | 8.386 | 7,07  |
|  27/7/2041 | 25 | 8.566 | 6,89  |
|  27/1/2042 | 25 | 8.746 | 6,70  |
|  27/7/2042 | 25 | 8.926 | 6,52  |
|  27/1/2043 | 25 | 9.106 | 6,35  |
|  27/7/2043 | 25 | 9.286 | 6,18  |
|  27/1/2044 | 25 | 9.466 | 6,01  |
|  27/7/2044 | 25 | 9.646 | 5,85  |
|  27/1/2045 | 25 | 9.826 | 5,70  |

---

|  Data | Fluxo de caixa | Dias corridos | VP  |
| --- | --- | --- | --- |
|  27/7/2045 | 1,025 | 10.006 | 227,27  |
|   |  | Preço sujo | 940,28  |
|   |  | Juros apropriados | 10,28  |
|   |  | Preço limpo | 930,00  |

Fonte: Elaborada pelos autores.

## Resumo

Este capítulo apresenta alguns dos títulos da dívida externa brasileira, assim como as formas de precificá-los.

23 Escritura é o documento que descreve o funcionamento do título, como indexadores, riscos associados ao emissor, cronograma de amortizações e pagamento de juros etc.
24 O nome do plano tem sua origem no nome do secretário do Tesouro dos Estados Unidos, Nicholas F. Brady. Os títulos brasileiros foram lançados em 1994.
25 A TIR também é conhecida como YTM (Yield to Maturity) na terminologia do mercado em inglês.
26 Neste momento, como não houve contagem de dias, os juros apropriados são iguais a zero e, portanto, o preço limpo é igual ao preço sujo.

---

# Capítulo 8
Títulos privados

## 8.1 Definição

Os títulos privados são títulos emitidos por empresas não governamentais. Há uma enorme gama de instrumentos da dívida privada. Abordaremos neste capítulo alguns dos títulos comuns no mercado brasileiro.

## 8.2 Certificados de depósitos

### 8.2.1 Certificado de depósito bancário (CDB)

O certificado de depósito bancário é um instrumento de renda fixa pelo qual o investidor empresta dinheiro ao banco em troca de uma rentabilidade. Essa rentabilidade pode ser pré ou pós-fixada.

Na modalidade pós-fixada, a rentabilidade do certificado pode ser atrelada à indexadores, por exemplo, a taxa DI ou o IPCA. Pode-se acrescer um percentual à variação do indexador, também denominado de *spread*, por exemplo: DI + 2% a. a. ou IPCA + 5% a. a. Também é possível atribuir um percentual a ser multiplicado pela variação do indexador, por exemplo: 102% do DI.

### 8.2.2 Depósito Interbancário (DI)

O Depósito interbancário é um instrumento de renda fixa pelo qual os bancos financiam uns aos outros. É muito parecido com o CDB, a diferença é que se trata de um instrumento no qual o emissor é um banco e o investidor é uma instituição financeira.

### 8.2.3 O cálculo da correção de um investimento indexado ao DI

Para melhor compreender como o valor desses certificados são corrigidos, é válida a consulta ao Caderno de Fórmulas da Cetip para CDBs, DIs, DPGE, LAM, LC, LF, LFS, LFSC, LFSN, IECI e RDB.

De qualquer forma, desenvolveremos os cálculos de correção baseados no

---

DI como indexador.

O primeiro passo é calcular o TDI_k, que é a taxa diária da taxa DI. Over divulgada pela Cetip:



TDI_k = [ (1 + DI_k)^(1/252) ] - 1 



Sendo que DI_k é a taxa DI. Over divulgada pela Cetip, uma taxa média expressa ao ano, com base 252 dias úteis, das operações de DI de 1 dia útil.

Uma vez calculadas as taxas diárias, precisamos acumulá-las por meio do seu produtório:



{
{l l}
Fator  DI_k = 1 & se  k = 0  (dia da aplicação) 

Fator  DI_k = ∏(k=1 até n) (1 + TDI_(k-1) × p) & caso contrário, a partir de  k = 1

 



Sendo que p é o percentual aplicado sobre o DI.

Também precisamos calcular o efeito do spread na atualização do investimento. Isso é feito por meio do cálculo do Fator de Spread:



{
{l l}
Fator de Spread_k = 1 & se  k = 0  (dia da aplicação) 

Fator de Spread_k = [ (1 + spread)^(dut/252))^(dup/252) ] & caso contrário, a partir de  k = 1

 



Sendo que:

- spread: é uma taxa prefixada, expressa ao ano, adicionada à correção do DI
- dut: prazo total da aplicação em número de dias úteis até a data de resgate ou vencimento
- dup_k: é o número de dias úteis desde a data da aplicação até a k-ésima data para a qual estamos calculando a correção do investimento

Agora, tudo que precisamos é calcular o Fator de Correção, considerando tanto o Fator DI quanto o Fator de Spread:



Fator de Correção_k = Fator  DI_k × Fator de Spread_k 



O Fator de Correção é o fator de capitalização acumulado, considerando a modalidade percentual do DI e a adição do spread, se houver. Na prática, o instrumento será emitido ou com spread ou com um percentual do DI diferente de 100%, mas nunca com os dois (um percentual diferente de 100% do DI mais um spread).

## 8.2.4 Exemplo: cálculo da correção de um investimento do tipo DI +

---

2%

Primeiro, mostraremos o cálculo de correção de um investimento indexado à taxa DI mais um spread de 2% a. a. para os quatro primeiros dias de uma aplicação.

Vamos assumir os seguintes dados da aplicação:

|  Valor inicial | 10.000.000  |
| --- | --- |
|  Prazo | 78 dias úteis  |
|  Spread a. a. | 2,00%  |
|  Percentual do DI | 100,00%  |

Vamos calcular, primeiro, o Fator DI:

Tabela 8.1 – Exemplo de cálculo do fator DI

|  Data | DIₖ | 1 + TDIₖ×p | Fator DIₖ  |
| --- | --- | --- | --- |
|  Dia 0 (k=0) | 12,87% | (1 + 12,87%×100%)^(1/265) = 1,00048054 | 1,00000000 (não há correção do “dia 0” ao “dia 0”)  |
|  Dia 1 (k=1) | 12,87% | (1 + 12,87%×100%)^(1/265) = 1,00048054 | Fator DI_(k+0)×(1 + TDI_(k+0)×p) = 1,00048054  |
|  Dia 2 (k=2) | 12,87% | (1 + 12,87%×100%)^(1/265) = 1,00048054 | Fator DI_(k+1)×(1 + TDI_(k+1)×p) = 1,00096131  |
|  Dia 3 (k=3) | 12,86% | (1 + 12,86%×100%)^(1/265) = 1,00048019 | Fator DI_(k+3)×(1 + TDI_(k+3)×p) = 1,00144231  |

Fonte: Elaborada pelos autores.

Neste exemplo, p = 100\% do DI.

Agora que calculamos o Fator DI, precisamos calcular o Fator de Spread, e depois acumulá-lo para cada data:

Tabela 8.2 – Exemplo de cálculo do valor bruto corrigido

|  Data | Fator DIₖ | Fator de Spreadₖ | Fator Correçãoₖ | Valor Bruto Corrigido  |
| --- | --- | --- | --- | --- |

---

|  Data | Fator DIₖ | Fator de Spreadₖ | Fator Correçãoₖ | Valor Bruto Corrigido  |
| --- | --- | --- | --- | --- |
|  Dia 0
(k = 0) | 1,00000000 (não há correção do “dia 0” ao “dia 0”) | 1,00000000 (não há correção do “dia 0” ao “dia 0”) | 1,00000000 (não há correção do “dia 0” ao “dia 0”) | 10.000.000,00  |
|  Dia 1
(k = 1) | 1,00048054 | [(1 + 2%)^(1/n)(n)]^(1/2*n* = 1.00007859) | Fator DI_(k=0) = Fator de Spread_(k=1) = 1.00055916 | 10.005.591,60  |
|  Dia 2
(k = 2) | 1,00096131 | [(1 + 2%)^(1/n)(n)]^(1/2*n* = 1.00015718) | Fator DI_(k=0) = Fator de Spread_(k=2) = 1.00111863 | 10.011.186,30  |
|  Dia 3
(k = 3) | 1,00144231 | [(1 + 2%)^(1/n)(n)]^(1/2*n* = 1.00023577) | Fator DI_(k=0) = Fator de Spread_(k=3) = 1.00167842 | 10.016.784,20  |

Fonte: Elaborada pelos autores.

Calculado o Fator de Correção, basta multiplicá-lo ao valor investido, neste caso, R$ 10.000.000. Neste exemplo, assumimos que não houve resgates parciais nestes quatro primeiros dias.

## 8.2.5 Exemplo: cálculo da correção de um investimento tipo 102% do DI

Agora, mostraremos o cálculo de correção de um investimento indexado à 102% do DI, sem spread, para os quatro primeiros dias de uma aplicação.

Vamos assumir os seguintes dados da aplicação:

|  Valor inicial | 10.000.000  |
| --- | --- |
|  Prazo | 78 dias úteis  |
|  Spread a. a. | 0,00%  |
|  Percentual do DI | 102,00%  |

Vamos calcular primeiro o Fator DI:

Tabela 8.3 – Exemplo de cálculo do fator DI

|  Data | DIₖ | 1 + TDIₖ×p | Fator DIₖ  |
| --- | --- | --- | --- |
|  Dia 0
(k = 0) | 12,87% | (1 + 12,87%×102%)^(1/2*n* = 1,0004901508) | 1,00000000 (não há correção do “dia 0” ao “dia 0”)  |
|  Dia 1
(k = 1) | 12,87% | (1 + 12,87%×102%)^(1/2*n* = 1,0004901508) | Fator DI_(k=0)×(1 + TDI_(k=0))×p) = 1,00049015  |

---

|  Data | Dlₖ | 1 + TDlₖ×p | Fator Dlₖ  |
| --- | --- | --- | --- |
|  Dia 2 (k=2) | 12,87% | (1 + 12,87%×102%)^(1/285) = 1,0004901508 | Fator Dl_(k+1)×(1 + TDl_(k+1)×p) = 1,00098054  |
|  Dia 3 (k=3) | 12,86% | (1 + 12,86%×102%)^(1/285) = 1,0004897938 | Fator Dl_(k+1)×(1 + TDl_(k+1)×p) = 1,00147117  |

Fonte: Elaborada pelos autores.

Agora que calculamos o Fator DI, precisamos calcular o Fator de Spread, e depois acumulá-lo. Como não há spread neste exemplo, o Fator de Spread será sempre 1,00, ou 100%:

Tabela 8.4 – Exemplo de cálculo do valor bruto corrigido

|  Data | Fator Dlₖ | Fator de Spreadₖ | Fator Correçãoₖ | Valor Bruto Corrigido  |
| --- | --- | --- | --- | --- |
|  Dia 0 (k=0) | 1,00000000 (não há correção do "dia 0" ao "dia 0") | 1,00000000 | 1,00000000 (não há correção do "dia 0" ao "dia 0") | 10,000,000.00  |
|  Dia 1 (k=1) | 1,00049015 | 1,00000000 | Fator Dl_(k+1)×Fator de Spread_(k+1) = 1,00049015 | 10.004.901,50  |
|  Dia 2 (k=2) | 1,00098054 | 1,00000000 | Fator Dl_(k+1)×Fator de Spread_(k+1) = 1,00098054 | 10.009.805,40  |
|  Dia 3 (k=3) | 1,00147117 | 1,00000000 | Fator Dl_(k+1)×Fator de Spread_(k+1) = 1,00147117 | 10.014.711,70  |

Fonte: Elaborada pelos autores.

Calculado o Fator de Correção, basta multiplicá-lo ao valor investido, neste caso, R$ 10.000.000. Neste exemplo, assumimos que não houve resgates parciais nestes quatro primeiros dias.

## 8.3 Debêntures

### 8.3.1 Definição

As debêntures são títulos privados emitidos por instituições não financeiras, do tipo sociedades anônimas. É um instrumento de captação que as empresas usam para financiar projetos, em geral, de longo prazo.

Atualmente, há três tipos principais de correção desses papéis:

---

- IPCA + spread
- DI + spread
- Percentual do DI

Embora exista certo grau de padronização desses instrumentos²⁷, para entender como esses papéis são precificados é necessário ler minuciosamente a sua escritura de emissão da debênture analisada. A escritura de emissão contém as fórmulas de cálculos dos fluxos de caixa, cronograma de amortizações, se houver, e também se a debênture é *plain vanilla* ou contém opções embutidas. O sítio eletrônico da Anbima (http://www.debentures.com.br/) consolida informações das diversas debêntures.

## 8.3.2 Exemplo: marcação a mercado de uma debênture do tipo percentual do DI

Mostraremos como marcar a mercado uma debênture na qual a correção contratual é definida em 110,80% do DI. Nos baseamos neste exemplo em uma debênture de características iguais à CSNA15. A seguir, as principais características deste papel:

![img-15.jpeg](img-15.jpeg)
Figura 8.1 – Debênture CSNA15: resumo das características

---

Fonte: Anbima.

A partir das informações da Figura 8.1 e do fato de que estamos precificando esta debênture em 17 de agosto de 2018, podemos resumir os dados conforme a seguir:

|  Emissão: | 01/09/2017  |
| --- | --- |
|  Data: | 17/08/2018  |
|  VNE: | 10.000.000,00  |
|  VNA: | 3.340.000,00  |
|  PU Par: | 3.358.242,11  |
|  DI ×: | 110,80%  |
|  Taxa de Mercado (DI ×): | 112,00  |

Sendo que:

- Emissão é a data de emissão da debênture;
- Data é a data na qual estamos marcando a mercado a debênture, neste exemplo, estamos calculando qual o seu preço de mercado em 17 de agosto de 2018;
- VNA é o valor nominal atualizado do papel, ou seja, é o valor nominal da emissão (VNE) descontadas as amortizações, se houver;
- PU Par é o valor nominal de emissão da debênture, descontadas as amortizações, acrescido da remuneração acumulada desde o último evento de pagamentos de juros até a data de referência pelos parâmetros contratuais da emissão. Aqui, assumimos esse valor como input do nosso exemplo;
- DI × refere-se ao percentual da taxa DI pelo qual o detentor desta debênture será remunerado;
- Taxa de mercado refere-se à taxa atual de mercado referente ao percentual da taxa DI para esta debênture.

A seguir, o cronograma das próximas amortizações:

|  Data de pagamento | Percentual do valor nominal unitário atualizado (remanescente) a ser amortizado  |
| --- | --- |
|  22 de julho de 2019 | 33,30%  |

---

|  Data de pagamento | Percentual do valor nominal unitário atualizado (remanescente) a ser amortizado  |
| --- | --- |
|  22 de julho de 2019 | 100,00%  |

A Anbima define o calculo dos juros das debêntures indexadas ao DI:



J = V N E × T e r m o _j tag {8.5}



Sendo que o fator de capitalização a Termo do  j -ésimo período é calculado pela segunte formula para as debêntures indexadas ao DI:



T e r m o _j = F a t C _j/F a t C_(j - 1) tag {8.6}



Onde  FatC  é o fator de capitalização acumulado nos periodos, calculado conforme a Equação 8.7 para as debêntures do tipo X% do DI:



F a t C _j = {[ (1 + E x p D I _j)^(1 / 2 5 2) ] × p + 1 }^(d u _j) tag {8.7}



Sendo que:

ExpDI_j  é definida pela Anbima como os juros prefixados, base 252 dias úteis, para cada data de evento. Essa taxa é obtida a partir das taxas de ajuste dos contratos de DI futuro com vencimentos em aberto, divulgadas, diariamente, pela BM&FBovespa, e, quando necessário, é interpolada exponencialmente via flat forward para as respectivas datas de pagamentos

p : refere-se ao percentual do DI, conforme definido contratualmente na emissão da debênture

du_j : é o número de dias úteis entre a data-base de precificação, ou da marcação a mercado, e a data do evento (pagamento de juros ou amortização)

Desta forma, podemos calcular os values dos fluxos de caixa conforme aabela a seguir:

Tabela 8.5 - Debênture CSNA15: calculo dos fluxos de caixa

|  Data fluxo | Tipo do fluxo | du | Saldo a amortizar (VNA) | ExpDI | Fator de capitalização acumulado (FatC) | Termo | Fluxo de caixa  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  22/10/2018 | J | 44 | 3.340.000 | 6,47% | 1,0122023 | 1,0122023 | 59.220,41  |
|  21/1/2019 | J | 105 | 3.340.000 | 6,87% | 1,0311494 | 1,0187186 | 62.520,26  |
|  22/4/2019 | J | 167 | 3.340.000 | 7,38% | 1,0536728 | 1,0218431 | 72.955,80  |

---

|  Data fluxo | Tipo do fluxo | du | Saldo a amortizar (VNA) | ExpDI | Fator de capitalização acumulado (FatC) | Termo | Fluxo de caixa  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  22/7/2019 | J | 230 | 3.340.000 | 7,85% | 1,0794176 | 1,0244334 | 81.607,45  |
|  22/7/2019 | A | 230 | 3.340.000 | 7,85% | 1,0794176 | 1,0244334 | 3.330.000,00  |
|  22/7/2019 | V | 230 | 0 | 7,85% | 1,0794176 | 1,0244334 | 10.000,00  |

Fonte: Elaborada pelos autores.

A coluna “Tipo do fluxo” da Tabela 8.5 apenas indica se o fluxo de caixa refere-se aos juros (J), à amortização (A) ou ao vencimento (V), que não deixa de ser um caso particular de amortização.

Sabemos que o valor de mercado da debênture será a soma dos valores presentes de seus fluxos de caixa. Aqui, para facilitar, podemos calcular os fatores de desconto, FatD_j, para trazer os fluxos de caixa aos valores presentes:



FatD_j = 1/{1 + [ (1 + ExpDI_j )^(1/252) - 1 ] × p_(mercado) }^(du_j) 



Sendo que p_(mercado) é o percentual do DI cotado pelo mercado para essa debênture na data de marcação a mercado. Neste exemplo, definimos p_(mercado) em 112,00% do DI.

Podemos, então, convenientemente, calcular o valor presente do j-ésimo fluxo de caixa, VP do Fluxo, pela fórmula a seguir:



VP  do Fluxo_j = Fluxo de Caixa_j × FatD_j 



Desta forma, podemos completar a Tabela 8.5 e verificar que o valor de mercado desta debênture é R$ 3.355.553,02:

Tabela 8.6 – Debênture CSNA15: cálculo dos valores presentes dos fluxos de caixa

|  Data fluxo | Tipo do fluxo | Termo | Fluxo de caixa | Fator de desconto (FatD) | Valor Presente do fluxo  |
| --- | --- | --- | --- | --- | --- |
|  22-10-18 | J | 1,0122023 | 59.220,41 | 0,9878151 | 58.498,81  |
|  21-7-19 | J | 1,0187186 | 62.520,26 | 0,9694695 | 60.611,49  |
|  22-4-19 | J | 1,0218431 | 72.955,80 | 0,9485241 | 69.200,34  |
|  22-7-19 | J | 1,0244334 | 81.607,45 | 0,9256592 | 75.540,69  |
|  22-7-19 | A | 1,0244334 | 3.330.000,00 | 0,9256592 | 3.082.445,10  |

---

22-7-19 V 1,0244334 10.000,00 0,9256592 9.256,59

Σ = 3.355.553,02

Fonte: Elaborada pelos autores.

Podemos conferir o cálculo com a calculadora da B3²⁸, que é muito útil para a validação:

Figura 8.2 – Debênture CSNA15: validação do cálculo de marcação a mercado
![img-16.jpeg](img-16.jpeg)
Fonte: B3.

Verificamos que o PU da operação está de acordo com o que calculamos em planilha.

## 8.3.3 Exemplo: marcação a mercado de uma debênture do tipo DI + spread

Agora, mostraremos como marcar a mercado a debênture GASP13. A seguir, algumas das características deste papel:

Figura 8.3 – Debênture GASP13: resumo das características

---

![img-17.jpeg](img-17.jpeg)
Fonte: Anbima.

A partir das informações da Figura 8.3 e do fato de que estamos precificando esta debênture em 17 de agosto de 2018, podemos resumir os dados pela seguinte tabela:

|  Emissão: | 15/9/2013  |
| --- | --- |
|  Data: | 17/8/2018  |
|  VNE: | 1.000,00  |
|  VNA: | 666,70  |
|  PU Par: | 687,30  |
|  DI + | 0,90%  |
|  Taxa de Mercado (DI +): | 0,4104%  |

Sendo que:

- Emissão é a data de emissão da debênture;
- Data é a data na qual estamos marcando a mercado a debênture neste exemplo, estamos calculando qual o seu preço de mercado em 17 de agosto de 2018;
- VNA é o valor nominal atualizado do papel, ou seja, é o valor nominal da emissão (VNE) descontadas as amortizações, caso houver;
- PU Par é o valor nominal de emissão da debênture, descontadas as

---

amortizações, acrescido da remuneração acumulada desde o ultimo evento de pagamentos de juros até a data de referencia. Aqui, assumimos esse valor como input do nosso exemple;

- DI + refere-se ao spread adicionado à taxa DI pelo qual o detentor esta debênture está remunerado, definido, contratualmente, na emissão do papel;
- Taxa de mercado refere-se à taxa atual de mercado do spread da taxa DI.

A seguir, o cronograma das proximas amortizações:

|  Data de pagamento | Percentual do valor nominal unitário atualizado a ser amortizado  |
| --- | --- |
|  17 de setembro de 2018 | 33,33%  |
|  16 de setembro de 2019 | 100,00%  |

Relembrando que a Anbima define o calculo dos juros das debêntures indexadas ao DI:



J = V N E × T e r m o _j



Sendo que a taxa a Termo do  j -ésimo periodo é calculada pela segunte formula para as debêntures indexadas ao DI:



T e r m o _j = F a t C _j/F a t C_(j - 1)



Onde  FatC  é o fator de capitalização acumulado nos periodos, calculado conforme a Equação 8.10 para as debêntures do tipo DI + spread:



F a t C _j = [ (1 + E x p D I _j)^(1 / 2 5 2) × (1 + s)^(1 / 2 5 2) ]^(d u _j) tag {8.10}



Sendo que:

ExpDI_j : é definida pela Anbima como a expectativa de juros, base 252 dias úteis, para cada data de evento. Essa taxa é obtida a partir das taxas de ajuste dos contratos de DI futuro com vencimentos em aberto, divulgadas diariamente pela BM&FBovespa, e, quando necessário, é interpolada exponentialmente para as respectivas datas de pagamentos

s: refere-se ao spread contratual adcionado ao DI, conforme definido na

---

emissão da debênture

duᵢ: é o número de dias úteis entre a data-base de precificação, ou da marcação a mercado, e a data do evento (pagamento de juros ou amortização)

Dessa forma, podemos calcular os valores dos fluxos de caixa conforme tabela a seguir:

Tabela 8.7 – Debênture GASP13: cálculo dos fluxos de caixa

|  Data fluxo | Tipo do fluxo | du | Saldo a amortizar (VNA) | ExpDI | Fator de capitalização acumulado (FatC) | Termo | Fluxo de caixa  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  17/9/2018 | J | 20 | 666,70 | 6,40% | 1,0056504 | 1,0056504 | 24,48  |
|  17/9/2018 | A | 20 | 333,30 | 6,40% | 1,0056504 | 1,0056504 | 333,30  |
|  15/3/2019 | J | 142 | 333,30 | 7,05% | 1,0443943 | 1,0385262 | 12,84  |
|  16/9/2019 | J | 270 | 333,40 | 7,88% | 1,0951232 | 1,0485725 | 16,19  |
|  16/9/2019 | V | 270 | 0 | 7,88% | 1,0951232 | 1,0485725 | 333,40  |

Fonte: Elaborada pelos autores.

Sabemos que o valor de mercado da debênture será a soma dos valores presentes de seus fluxos de caixa. Aqui, podemos calcular os fatores de desconto, FatD_j, para trazer os fluxos de caixa aos valores presentes:



FatD_j = 1/[ (1 + ExpDI_j)^(1/252) × (1 + s_(mercado))^(1/252) ]^(du_j) 



Sendo que s_(mercado) é o spread do DI cotado pelo mercado para essa debênture na data de marcação a mercado. Neste exemplo, s_(mercado) = 0,4104\%.

Então, podemos calcular os valores presentes dos fluxos de caixa, VP do Fluxo, pela fórmula a seguir, conforme visto anteriormente:



VP  do Fluxo_j = Fluxo de Caixa_j × FatD_j



Dessa forma, podemos completar a Tabela 8.7 e verificar que o valor de mercado desta debênture é R$ 689,14:

Tabela 8.8 – Debênture GASP13: cálculo dos Valores Presentes dos fluxos de caixa

|  Data fluxo | Tipo fluxo | Termo | Fluxo de caixa | Fator de desconto | Valor Presente do fluxo  |
| --- | --- | --- | --- | --- | --- |
|  17-9-18 | J | 1,0056504 | 24,48 | 0,9947653 | 24,36  |

---

|  17-9-18 | A | 1,0056504 | 333,30 | 0,9947653 | 331,56  |
| --- | --- | --- | --- | --- | --- |
|  15-3-19 | J | 1,0385262 | 12,84 | 0,9601208 | 12,33  |
|  16-9-19 | J | 1,0485725 | 16,19 | 0,9179106 | 14,86  |
|  16-9-19 | V | 1,0485725 | 333,40 | 0,9179106 | 306,03  |



Σ =   689,14



Fonte: Elaborada pelos autores.

Podemos conferir o cálculo com a calculadora da B3 (https://calculadorarendafixa.com.br/#/navbar/calculadora), que, mais uma vez, é muito útil na validação:

Figura 8.4 – Debênture GASP13: validação do cálculo de marcação a mercado
![img-18.jpeg](img-18.jpeg)
Fonte: B3.

Observamos que o preço que calculamos está de acordo com a calculadora demonstrada na Figura 8.4.

## 8.3.4 Exemplo: marcação a mercado de uma debênture do IPCA + spread

Mostraremos como marcar a mercado a debênture AGRU11. A seguir, algumas das características deste papel:

Figura 8.5 – Debênture AGRU11: resumo das características

---

![img-19.jpeg](img-19.jpeg)
Fonte: Anbima.

Mesmo com as informações anteriores, precisamos ler a escritura de emissão, que precisa os cálculos da rentabilidade da debênture, assim como seu cronograma de amortizações. A seguir, um resumo das características deste papel que serão importantes na sua marcação a mercado. Vamos assumir que estamos em 17 de agosto de 2018:

|  Emissão: | 15/2/2014  |
| --- | --- |
|  Data: | 17/8/2018  |
|  Último pagamento: | 15/3/2018  |
|  VNA: | 1.190,650301  |
|  IPCA + | 7,86% a. a.  |
|  Taxa de mercado: | 9,218% a. a.  |

Sendo que:

- Emissão é a data de emissão da debênture;
- Data é a data na qual estamos marcando a mercado a debênture neste exemplo, estamos calculando qual o seu preço de mercado em 17 de agosto de 2018;
- Último pagamento é a data na qual ocorreu o último pagamento de

---

fluxo de caixa, seja juros ou amortização;

- VNA é o valor nominal atualizado do papel, ou seja, é o valor nominal da emissão (VNE) atualizado pelas amortizações;
- IPCA + é o cupom de juros contratual que a debênture paga além da variação do IPCA. É análogo ao cupom de juros da NTN-B, só que nesta debênture os fluxos de caixa são anuais, e não semestrais;
- Taxa de mercado é o cupom de IPCA cotado pelo mercado em 17 de agosto de 2018. Assumimos essa taxa como input no modelo de marcação a mercado, já que é publicamente divulgada.

A tabela a seguir mostra o cronograma de amortizações remanescentes, resumido da escritura de emissão:

|  Data de pagamento | Percentual do valor nominal unitário atualizado a ser amortizado  |
| --- | --- |
|  15 de março de 2019 | 8,00%  |
|  15 de março de 2020 | 10,00%  |
|  15 de março de 2021 | 12,00%  |
|  15 de março de 2022 | 15,00%  |
|  15 de março de 2023 | 15,00%  |
|  15 de março de 2024 | 15,00%  |
|  15 de março de 2025 | 100,00%  |

A escritura de emissão também apresenta o cálculo dos juros anuais dessa debênture:



J = VNA × (Fator de Juros - 1) 



O fator de juros é calculado por:



Fator de juros = (1 + Taxa)^(dp/j_(252)) 



Sendo que a Taxa é de 7,86%, definida na escritura de emissão e dp é o número de dias úteis entre a data de emissão ou a data de pagamento de juros remuneratórios imediatamente anterior à data que estamos precificando o papel.

O fluxo de caixa referente às amortizações é calculado conforme a Equação 8.14:



Amortização = VNA × Percentual de Amortização 



---

Dessa forma, podemos calcular os valores dos fluxos de caixa conforme a seguir:

Tabela 8.9 – Debênture AGRU11: cálculo dos fluxos de caixa

|  Data fluxo | Tipo fluxo | Dias úteis entre pagamentos (dp) | Taxa de amortização do saldo remanescente | Fluxo de caixa | Saldo após amortização (VNA)  |
| --- | --- | --- | --- | --- | --- |
|  15/3/2019 | J | 250 | 0% | 1.190,650301×[(1 + 7,86%)^(240)/251 - 1] = 92,814153 | 1.190,650301  |
|  15/3/2019 | A | 250 | 8% | 1.190,650301×8% = 95,252024 | 1.190,650301 - 95,252024 = 1.095,398277  |
|  16/3/2020 | J | 253 | 0% | 1.095,398277 × [(1 + 7,86%)^(240)/251 - 1] = 86,453106 | 1.095,398277  |
|  16/3/2020 | A | 253 | 10% | 1.095,398277×10% = 109,539828 | 1.095,398277 - 109,539828 = 985,858449  |
|  15/3/2021 | J | 249 | 0% | 985,858449 × [(1 + 7,86%)^(240)/251 - 1] = 76,531084 | 985,858449  |
|  15/3/2021 | A | 249 | 12% | 985,858449 ×12% = 118,303014 | 985,858449 - 118,303014 = 867,555435  |
|  15/3/2022 | J | 252 | 0% | 867,555435 × [(1 + 7,86%)^(240)/251 - 1] = 68,189857 | 867,555435  |
|  15/3/2022 | A | 252 | 15% | 867,555435×15% = 130,133315 | 867,555435 - 130,133315 = 737,422120  |
|  15/3/2023 | J | 252 | 0% | 737,422120 × [(1 + 7,86%)^(240)/251 - 1] = 57,961379 | 737,422120  |
|  15/3/2023 | A | 252 | 15% | 737,422120×15% = 110,613318 | 737,422120 - 110,613318 = 626,808802  |
|  15/3/2024 | J | 250 | 0% | 626,808802 × [(1 + 7,86%)^(240)/251 - 1] = 48,861305 | 626,808802  |
|  15/3/2024 | A | 250 | 15% | 626,808802×15% = 94,021320 | 626,808802 - 94,021320 = 532,787482  |
|  17/3/2025 | J | 253 | 0% | 532,787482 × [(1 + 7,86%)^(240)/251 - 1] = 42,049667 | 532,787482  |
|  17/3/2025 | V | 253 | 100% | 532,787482×100% = 532,787482 | 532,787482 - 532,787482 = 0,000000  |

Fonte: Elaborada pelos autores.

Uma vez calculados os fluxos de caixa, a marcação a mercado será simplesmente a soma dos seus valores presentes pela taxa de mercado,

---

definida em 9,2181% a. a.:



M t M = Σ(j = 1) ^k Fluxo de Caixa _j/(1 + Taxa_(Mercado))^(d a_(j j) / 2 5 2) tag {8.15}



Aplicando a Fórmula 8.15 de marcação a mercado, calculamos o preço da debênture a partir da taxa de mercado em R$ 1.173,12:

Tabela 8.10 – Debênture AGRU11: cálculo dos Valores Presentes dos fluxos de caixa

|  Data fluxo | Fluxo de caixa | Dias úteis remanescentes (DU) | Valor Presente do fluxo  |
| --- | --- | --- | --- |
|  15/3/2019 | 92,814153 | 142 | 88,315253  |
|  15/3/2019 | 95,252024 | 142 | 90,634955  |
|  16/3/2020 | 86,453106 | 395 | 75,293231  |
|  16/3/2020 | 109,539828 | 395 | 95,399782  |
|  15/3/2021 | 76,531084 | 644 | 61,090666  |
|  15/3/2021 | 118,303014 | 644 | 94,434961  |
|  15/3/2022 | 68,189857 | 896 | 49,838224  |
|  15/3/2022 | 130,133315 | 896 | 95,111114  |
|  15/3/2023 | 57,961379 | 1.148 | 38,787096  |
|  15/3/2023 | 110,613318 | 1.148 | 74,021175  |
|  15/3/2024 | 48,861305 | 1.398 | 29,958725  |
|  15/3/2024 | 94,021320 | 1.398 | 57,648048  |
|  17/3/2025 | 42,049667 | 1.651 | 23,597970  |
|  17/3/2025 | 532,787482 | 1.651 | 298,996490  |
|   |  | Σ = | 1.173,12  |

Fonte: Elaborada pelos autores.

Mais uma vez, é possível conferir o valor com a calculadora da B3 (https://calculatorarendafixa.com.br/#/nvbar/calculadora), novamente é muito útil na validação:

Figura 8.6 – Debênture AGRU11: validação do cálculo de marcação a mercado

---

![img-20.jpeg](img-20.jpeg)
Fonte: B3.

Também é importante mostrar que a taxa de mercado é publicada diariamente pela Anbima, na coluna “Taxa indicativa”:

Figura 8.7 – Debênture AGRU11: taxas do mercado secundário
![img-21.jpeg](img-21.jpeg)
Fonte: Anbima.

O preço marcado a mercado aparece na Figura 8.7, na coluna PU, R$ 1.173,120598.

Nos cálculos das debêntures deste capítulo, optamos por calcular até a segunda casa decimal, sem nos preocuparmos com as regras de arredondamento definidas na Deliberação N° 3 do Conselho de Regulação e Melhores Práticas de Mercado Aberto.

Apresentamos nesta seção de debênture os três tipos mais comuns no mercado brasileiro na modalidade plain vanilla (sem opções embutidas).

Resumo

---

Este capítulo mostra como calcular a correção de investimentos indexados à taxa DI, assim como a demonstração dos cálculos de marcação a mercado dos tipos de debêntures mais comuns no Brasil.

27 A Deliberação N° 3 do Conselho de Regulação e Melhores Práticas de Mercado Aberto, uma iniciativa conjunta da Anbima, STN, Banco Central, Cetip e B3 (então BM&FBovespa) é extremamente útil para entender os cálculos de correção, precificação e marcação a mercado das debêntures.

28 CALCULADORA DA B3. Disponível em: <https: calculadora="" calculadora. com.br="" naubar="" #="">.</https:>

---

# Capítulo 9

Introdução ao risco de mercado em títulos de renda fixa

## 9.1 Risco pré

A melhor forma de entender o risco que existe em operações com títulos de renda fixa é imaginá-los como instrumentos que têm preço no mercado, antes de pensar na renda que eles podem estar sinalizando ao longo do tempo, ou seja, sua taxa de retorno.

Quando se compra um título ou se realiza uma operação de crédito, paga-se um valor inicial por um fluxo de caixa futuro, com uma distribuição predefinida em contrato.

Como visto anteriormente, o preço dessa transação relaciona-se à taxa interna de retorno dessa, usando como referência as taxas de juros de mercado e aplicando-se spreads de risco onde existe a necessidade para tanto.

Dessa maneira, de forma simplificada, pode-se escrever:



P = f(y) 



Como a função anterior é montonicamente descrescente com a taxa interna de retorno em todo seu domínio, temos que f(y), ou seja, quando a taxa de juros aumenta o valor presente do título (seu preço) diminui e vice-versa.

A explicação financeira é que se o título tem um valor futuro fixo constante, no momento em que a curva de juros se move para cima e as taxas crescem, cada R$ 1 de valor futuro daquele título fica mais barato de ser atingido com a aplicação no presente, logo, quem comprou o título com uma taxa de retorno menor vai precisar de menos recurso hoje para retirar o mesmo R$ 1 no futuro. Isso é um ganho na data de hoje.

## 9.1.1 Exemplo: o impacto da taxa pré na marcação a mercado de uma LTN

---

Imagine um gestor de um fundo de investimento que acredita que a taxa de juros cairá em dois anos. Então, ele resolve adquirir uma LTN de dois anos de prazo.

O preço que ele vai pagar está relacionado com as taxas de juros da economia de acordo com a relação:



P_(LTN) = 1.000/(1 + y)^(du/252) 



Como a LTN é um zero coupon bond, a taxa à vista e a taxa de retorno são análogas. Supondo que a taxa esteja em 9% a. a. para dois anos, o preço do papel deve ser:



P_(LTN) = 1.000/(1 + 9\%)^(504/252) = 841,68



O balanço do fundo de investimento vai ficar:

|  Balanço do fundo | 841,68  |
| --- | --- |
|   | 841,63 PL (quotas)  |

Vamos supor que em vez de cair a taxa para dois anos aumente 1 p. p.²⁹ ao longo do dia. O novo preço do papel será:



P_(LTN) = 1.000/(1 + 10\%)^(504/252) = 826,45



E o balanço do fundo de investimento ficaria:

|  Balanço do fundo | 826,45  |
| --- | --- |
|   | 841,63 PL (quotas)  |
|   | -15,18 Resultado  |

Ou seja, o prejuízo vai ter de refletir nas quotas dos clientes no dia seguinte. Esse processo é chamado de marcação a mercado e garante que os quotistas tenham o valor do seu patrimônio avaliado, diariamente, em função do valor corrente dos ativos que compõem a carteira do fundo.

---

Esse risco de oscilação no valor dos títulos de renda fixa é chamado de risco pré estará presente em papéis prefixados ou com algum componente prefixado.

## 9.2 Spreads de crédito/liquidez

Os emissores de títulos podem ser empresas e governos (federais, estaduais e municipais). Cada qual com seu nível de risco de crédito percebido pelos agentes. Se assumirmos uma referência para o melhor risco de crédito, veremos que é possível observar que quanto maior o risco de crédito percebido, menor a classificação de crédito do emissor³⁰ e maior a diferença entre a remuneração que papéis emitidos por cada um desses emissores oferecem em relação ao emissor de referência.

## 9.3 G-Spread

O tipo de spread mais comum é o G-Spread, ou seja, a diferença simples entre a taxa de retorno do título em questão e o título de referência.

O SoT (Spread over Treasury) é um G-Spread. Serve como uma referência para se avaliar o comportamento do risco de crédito de um determinado emissor, dado que separa a taxa de retorno do papel em duas parcelas, a taxa de retorno da referência e um prêmio de risco.

No caso do SoT, a relação para um título brasileiro é:



y_(Brasil) = y_(US) + SoT 



Em que du_1 é a taxa de retorno de um título com características semelhantes ao do título brasileiro.

A ideia por trás dos spreads é sempre medir as condições de crédito e liquidez daquele papel específico de determinada empresa/governo.

No caso do G-Spread isso é feito de maneira informativa, sem muita preocupação com a precisão matemática do cálculo.

Tanto é que na hipótese de não haver títulos de referência com prazo³¹ similar, usam-se papéis com prazos próximos.

O Z-Spread fornece um cálculo mais adequado do ponto de vista quantitativo, porque relaciona as variáveis de interesse e promove um fechamento algébrico efetivo entre essas.

---

# 9.4 Z-Spread

Para calcular o Z-Spread para um papel identificaremos qual é a sua curva de juros de referência e calcular o spread anual que faz essa curva à vista mais esse spread resultar no preço de mercado do papel.

Algebricamente:



P_(papel) = Σ(k=1 até n) FC_k/[(1 + i_k) × (1 + z)]^(dn_k/252) 



Onde:

i_k: taxa de juros para o vencimento k

z: Z-spread

Esse cálculo é similar ao cálculo da TIR, ou seja, não possui solução analítica.

A saída é a mesma utilizada no cálculo da TIR. Envolve a criação de uma função f(z):



f(z) = P_(papel) - Σ(k=1 até n) FC_k/[(1 + i_k) × (1 + z)]^(dn_k/252) 



Quando f(z) → 0, z → Z-Spread

## 9.4.1 Exemplo: cálculo do Z-Spread

Calcular o Z-Spread para uma NTN-F de vencimento 1/1/2027 em 21/9/2016 por R$ 902,198975.

A seguir, as ETTJs da B3 (referência) e da NTN-F resultante do cálculo do Z-Spread:

Gráfico 9.1 – Z-Spread NTN-F
![img-22.jpeg](img-22.jpeg)
Fonte: Elaborado pelos autores.

---

A seguir, a estrutura em MS Excel necessária para o cálculo, com os valores dos fluxos de caixa ao longo do tempo, a ETTJ da B3 no momento da aquisição e os prazos.

Tabela 9.1 – Cálculo dos Valores Presentes dos fluxos de caixa

|  Datas | Dias úteis | Cupom de juros | ETTJ B3 | Valor Presente  |
| --- | --- | --- | --- | --- |
|  2/1/2017 | 70 | 48,809 | 13,87% | 47,07  |
|  3/7/2017 | 194 | 48,809 | 13,05% | 44,4  |
|  2/1/2018 | 319 | 48,809 | 12,36% | 42,09  |
|  2/7/2018 | 443 | 48,809 | 12,02% | 39,95  |
|  2/1/2019 | 569 | 48,809 | 11,87% | 37,85  |
|  1/7/2019 | 692 | 48,809 | 11,82% | 35,87  |
|  2/1/2020 | 822 | 48,809 | 11,82% | 33,86  |
|  1/7/2020 | 945 | 48,809 | 11,85% | 32,02  |
|  4/1/2021 | 1073 | 48,809 | 11,87% | 30,22  |
|  1/7/2021 | 1196 | 48,809 | 11,92% | 28,55  |
|  3/1/2022 | 1324 | 48,809 | 11,97% | 26,89  |
|  1/7/2022 | 1448 | 48,809 | 12,02% | 25,37  |
|  2/1/2023 | 1575 | 48,809 | 12,05% | 23,91  |
|  3/7/2023 | 1699 | 48,809 | 12,07% | 22,57  |
|  2/1/2024 | 1824 | 48,809 | 12,09% | 21,3  |
|  1/7/2024 | 1948 | 48,809 | 12,12% | 20,1  |
|  2/1/2025 | 2078 | 48,809 | 12,13% | 18,92  |
|  1/7/2025 | 2200 | 48,809 | 12,14% | 17,88  |
|  2/1/2026 | 2331 | 48,809 | 12,17% | 16,81  |
|  1/7/2026 | 2453 | 48,809 | 12,20% | 15,86  |
|  4/1/2027 | 2581 | 1,048,800 | 12,22% | 320,71  |
|   |  |  | Preço | 902,199  |
|   |  |  | Meta | 902,199  |
|   |  |  | f(z) | 0  |
|   |  |  | z (%a. a.) | 0,0411%  |

Fonte: Elaborada pelos autores.

O spread da NTN-F, atualmente, é pequeno em relação à curva de referência, porém é possível tomar títulos corporativos em que essa diferença será mais pronunciada.

---

Resumo

Este capítulo traz uma introdução aos riscos de títulos de renda fixa.

29 Oscilações dessa ordem de grandeza são raras durante o dia, mas podem ocorrer. Esse valor exacerbado foi usado para fins didáticos.

30 A classificação de crédito de um emissor é feita por agências especializadas que, por meio da análise de vários aspectos quantitativos e qualitativos dos emissores, atribui a eles notas de crédito. As três agências mais famosas são Fitch, Standard e Poor's and Moody's.

31 Mais adiante, mostraremos que maior prazo em renda fixa significa maior risco de oscilação de preços e que a melhor definição de prazo para esse fim não é o vencimento do papel.

---

# Capítulo 10

## O cálculo do spread de crédito

Como visto no início do livro, os títulos de renda fixa são, na verdade, instrumentos de crédito emitidos por bancos, empresas ou governos para utilização em suas atividades corriqueiras.

Apresentamos anteriormente maneiras de se medir o risco de crédito por meio de spreads de crédito que são adicionados às taxas de juros vigentes com o intuito de se atribuir ao papel uma probabilidade de inadimplência.

Para papéis emitidos localmente, os spreads de crédito mais comuns são aqueles atribuídos à taxa pré (que não são observáveis em contrato) e o percentual da taxa DI (que é formalizado em contrato).

## 10.1 Spread sobre a curva pré da B3

Apesar de não ser formalizado em contrato e, portanto, não ser observado na prática, o spread em formato prefixado é muito simples de ser calculado e é utilizado por bancos e fundos para medir a qualidade de crédito do emissor e as condições de liquidez do mercado, uma vez que essa variável muda ao longo do tempo.

Então, podemos escrever:



(1 + i_(operação)) = (1 + i_(B3))(1 + s) 



Ou seja, é possível quebrar a taxa de mercado instantânea de um título em sua componente de mercado e sua componente de crédito/liquidez sendo que ambas variam no tempo.

Por exemplo, um CDB prefixado teria seu valor a mercado dado em um instante t qualquer dado por:



MtM_(CDB-Pré) = VAX (1 + i_(emissão))^(dur/292)/(1 + i_(mercado))^(dua/292) 



Onde:

i_(emissão): taxa de juros ao ano de emissão do CDB

---

i_(mercado): taxa de juros atual de mercado para vencimento em questão

du_T: prazo em dias úteis total da operação

du_B: prazo em dias úteis restante da operação



t + du_B = du_T



Alguma manipulação algébrica pode ser acrescentada para entendermos as nuances técnicas e operacionais dessa abordagem, por exemplo, podemos quebrar as taxas de emissão e de mercado atual em taxa da B3 e spread:



MtM_(CDB-Pré) = VA × [(1 + i₀)(1 + s₀)]^(du_T/252)/[(1 + i_t)(1 + s_t)]^(du_B/252) 



Se s_0 = s_t, a qualidade de crédito do emissor não se altera ao longo do tempo e a oscilação de valor do CDB só será devida ao risco de mercado (oscilação da ETTJ).

## 10.2 Spread em percentual da taxa DI

Para os participantes do mercado que desejam uma exposição pós-fixada, o mercado financeiro brasileiro criou o percentual do CDI.

Dadas as historicamente altas taxas de juros e sua tradicional volatilidade, o percentual do CDI foi a ferramenta utilizada para atrelar o poder de barganha do investidor, o risco de crédito do emissor e o prêmio de liquidez das mais diversas operações financeiras à taxa DI, de modo a eliminar o risco de mercado (oscilação) que a taxa prefixada carregaria para remunerar operações similares.

Na próxima seção, serão discutidas as relações de arbitragem entre os diversos indexadores e como o percentual da taxa DI se relaciona com a curva de juros instantânea da economia.

No gráfico a seguir é possível observar como as curvas de emissores variam com o percentual do CDI:

Gráfico 10.1 – ETTJ em função do percentual da taxa DI

---

![img-23.jpeg](img-23.jpeg)

Fonte: Elaborado pelos autores.

Quanto maior o risco de crédito do emissor, maior a probabilidade de inadimplência e maior o spread que o emissor terá de pagar para se financiar.

## 10.2.1 Exemplo: cálculo do spread de crédito

Um cliente de seu banco deseja comprar um CDB prefixado de um ano de prazo com taxa de emissão de 10.90% a. a.

Se o valor aplicado no CDB da questão anterior for de R$ 1.000.000 e a taxa de mercado na B3 é de 9.5% a. a., calcule:

a) Valor de resgate
b) Valor “na curva” depois de 6 meses.
c) Spread de crédito/ liquidez na emissão.
d) Valor a mercado depois de 6 meses se a taxa na BM&F para o vencimento é de 10,5% a. a., mantendo o risco de crédito/ liquidez do emissor igual ao da emissão.
e) Esse CDB está gerando perda ou ganho market to market ao banco? E ao cliente?
f) Valor a mercado depois de 6 meses se a taxa para o vencimento é de 10,5% a. a., supondo que o spread de crédito/ liquidez do emissor aumentou em 0,5% a. a.

Dado: modelo de marcação a mercado do CDB pré:



MtM_(CDB-Pre) = VA × (1 + i_(emissão))^(dur/252)/(1 + i_(B3))^(dug/252) × (1 + s)^(dus/252)



---

# Solução

a) O valor de resgate é o principal mais os juros acumulados ao longo do contrato:



Accrual_(CDB-Pre) = VA × (1 + i_(emissão)) du_e/252





Accrual_(CDB-Pre) = 1.000.000 × (1 + 10,90\%) 252/252 = 1.108.999



b) O valor na curva em 6 meses é o principal mais os juros acumulados em 6 meses, pela taxa do contrato:



Accrual_(CDB-Pre) = 1.000.000 × (1 + 10,90\%) 252/252 = 1.108.999



c) Usando o modelo de marcação a mercado sugerido:



(1 + i_(emissão)) = (1 + i_(BS))(1 + s)





(1 + 10,90\%) = (1 + 9,5)(1 + s)





s = 1,28\%  a.a.



d) A marcação pelo modelo sugerido fica:



MtM_(CDB-Pre) = 1.000.000 × (1 + 10,90\%) 252/252/(1 + 10,50\%) 126/252 × (1 + 1,28\%) 126/252 = 1.048.314



e) Como o valor a mercado é menor que o valor na curva, esse CDB está gerando perda *mark to market* ao cliente e ganho (dado que é um passivo) ao banco.

f) Ainda usando a marcação pelo modelo sugerido:



MtM_(CDB-Pre) = 1.000.000 × (1 + 10,90\%) 252/252/(1 + 10,50\%) 126/252 × (1 + 1,78\%) 126/252 = 1.045.736



---

**Resumo**

Este capítulo demonstra os cálculos dos *spreads* de crédito.

---

# Capúulo 11

# Arbitragem entre instrumentos de renda fixa

Um conceito muito difundido no mercado financeiro é o de arbitragem entre instrumentos de níveis de risco similares.

Nos itens a seguir introduziremos e modelaremos o conceito por meio da utilização do mercado de captação de recursos em bancos no Brasil.

# 11.1 Instrumentos de captação em instituições financeiras

Noções:

- Certificado de Depósito Bancário (CDB): título emitido por instituições financeiras para financiar sua carteira de empréstimos.
- Os indexadores mais comuns são taxa pré, DI e IPCA.
- Todas as rentabilidades, a princípio, são arbitradas, ou seja, o valor futuro esperado do CDB é igual para os três indexadores no momento inicial, a não ser que a instituição esteja privilegiando algum em detrimento dos outros propositalmente.
- O imposto de renda sobre os ganhos segue uma tabela de alíquotas que varia conforme o prazo da aplicação.

Tabela 11.1 – Tabela de imposto de renda na renda fixa

|  Prazo | Alíquota  |
| --- | --- |
|  Até 180 dias | 22,50%  |
|  De 181 até 360 dias | 20,00%  |
|  De 361 até 720 dias | 17,50%  |
|  Acima de 720 dias | 15,00%  |

Fonte: Elaborada pelos autores.

- LCI e LCA também são instrumentos de captação similares ao CDB, porém com um benefício fiscal, não existe IR para elas.

---

- Assim, as taxas que elas oferecem terão de ser arbitradas, a não ser que a instituição queira diminuir ou aumentar a captação nesses instrumentos por alguma razão.

## 11.2 Arbitragem entre indexadores

Os valores futuros de cada indexador são dados por:

- CDB-Pré:


V F_(C D B - P r é) = V A × (1 + i_(p r é))^(d u/2 5 2) tag {11.1}



- CDB DI:

Chamando di_k a taxa CDI ao dia e de α o percentual do CDI do CDB, teremos:



V F_(C D B - C D I) = V A × prod_(k = 0)^(d u - 1) {[ (1 + D I ₖ)^(1/2 5 2) - 1 ] × α + 1 } tag {11.2}





V F_(C D B - C D I) = V A × prod_(k = 0)^(d u - 1) (1 + α × d i ₖ) tag {11.3}



- CDB IPCA:


V F_(C D B - I P C A) = V A × I P C A _t/I P C A ₀ × (1 + i_(I P C A))^(d u/2 5 2) tag {11.4}



Pelo critério de arbitragem, o valor esperado de todos eles devem ser iguais no instante zero. Assim, a arbitragem entre taxa Pré e taxa DI é dada por:



V A × (1 + i_(p r é))^(d u/2 5 2) = E [ V A × prod_(k = 0)^(d u - 1) (1 + α × d i ₖ) ] tag {11.5}



Desenvolvendo a equação anterior:



(1 + i_(p r é))^(d u/2 5 2) = prod_(k = 0)^(d u - 1) (1 + α × E (d i ₖ))



Como a expectativa sobre a taxa DI é a curva de juros da B3, o valor de E(di_k) = i_(B3), ou seja, para o caminho das taxas CDI (note que aqui ela está em taxa diária) é a própria taxa pré da curva B3 para aquele vencimento.

Continuando:



(1 + i_(p r é))^(d u/2 5 2) = (1 + α × i_(B 3))^(d u)



---

Isolando o percentual do CDI:



α = (1 + i _ {p r acute {e}})^(1/2 5 2) - 1/i_(B 3)



Como i_(B3) está em base diária, podemos escrever em taxa ano:



α = (1 + i _ {p r acute {e}})^(1/2 5 2) - 1/(1 + i_(B 3) ^α)^(1/2 5 2) - 1 tag {11.6}



Que é o percentual do CDI desse CDB. Note que se o percentual do CDI for 100%, a taxa Pré do CDB será a própria taxa da B3.

Por outro lado, a arbitragem entre a curva Pré e o cupom de IPCA será dada por:



V A × (1 + i _ {p r acute {e}})^(d u/2 5 2) = E [ V A × I P C A _t/I P C A ₀ × (1 + i_(I P C A))^(d u/2 5 2) ] tag {11.7}



Desenvolvendo:



(1 + i _ {p r acute {e}})^(d u/2 5 2) = E (I P C A _t)/I P C A ₀ × (1 + i_(I P C A))^(d u/2 5 2)



O operador esperança é aplicado somente nas variáveis aleatórias (taxa DI e IPCA, nos exemplos anteriormente citados).

A equação desenvolvida anteriormente mostra-nos que o juro real será dado pelo quociente entre o juro nominal e a expectativa de inflação do período.

É possível escrever a equação desenvolvida anteriormente na forma de inflação esperada em IPCA:



(1 + i _ {p r acute {e}})^(d u/2 5 2) = (1 + pi_e)^(d u/2 5 2) × (1 + i_(I P C A))^(d u/2 5 2)



Como o expoente é igual para todos os termos, teremos:



(1 + i _ {p r acute {e}}) = (1 + pi_e) × (1 + i_(I P C A)) tag {11.8}



Ou seja, o juro real ex-ante^(32) será o juro nominal menos a inflação esperada, a consagrada Relação de Fischer.

## 11.3 Arbitragem entre instrumentos via diferença de tributação

Pelo já exposto, o valor futuro de um CDB indexado à taxa DI:

(11.9)

---



V F_(C D B - C D I) = V A × (1 + α × i_(B 3))^(d u)



O imposto de renda retido na fonte será:



I R = (V F_(C D B - C D I) - V A) × a l i q I R tag {11.10}



Assim, o valor líquido do CDB será dado por:



V L_(C D B - C D I) = V F_(C D B - C D I) - [ (V F_(C D B - C D I) - V A) × a l i q I R ]



Desenvolvendo, teremos:



V L_(C D B - C D I) = V A × [ (1 + α × i_(B M \& F))^(d u) (1 - a l i q I R) + a l i q I R ]



Observe que quando a alíquota de IR é zero, o valor líquido é o próprio valor futuro do CDB. Esse é o caso das LCIs e LCAs. Logo:



V L_(L C I - C D I) = V A × (1 + β × i_(B 3))^(d u)



Para calcular as taxas de arbitragem, temos de igualar os dois valores líquidos futuros:



V L_(C D B - C D I) = V L_(L C I - C D I)





V A × [ (1 + α × i_(B 3))^(d u) (1 - a l i q I R) + a l i q I R ] = V A × (1 + β × i_(B 3))^(d u)



Ou seja:



[ (1 + α × i_(B 3))^(d u) (1 - a l i q I R) + a l i q I R ] = (1 + β × i_(B 3))^(d u) tag {11.11}



Onde α é a taxa percentual do CDI paga no CDB e β a taxa percentual do CDI paga na LCI.

## 11.4 Taxa nominal e real líquidas

Imaginando um CDB Pré, o valor de resgate (líquido) será:



V F = V A × {(1 + i)^(d u/2 3 2) × (1 - a l i q I R) + a l i q I R }



Dividindo os dois lados pelo valor aplicado inicial, teremos:



V F/V A = {(1 + i)^(d u/2 3 2) × (1 - a l i q I R) + a l i q I R }



Expressando em termos de taxa líquida:



(1 + i_(l i q))^(d u/2 3 2) = {(1 + i)^(d u/2 3 2) × (1 - a l i q I R) + a l i q I R }



Isolando a taxa líquida, chega-se a:

---



i_(liq) = {(1 + i)^(du/252) × (1 - aliqIR) + aliqIR}^(252/dw) - 1



Ou seja, pela equação anterior pode-se, de antemão, saber qual a taxa líquida obtida em um instrumento de renda fixa prefixado.

Para um CDB IPCA, podemos quebrar a remuneração em um fator relativo à taxa real de juros e outro fator relativo à taxa de inflação.

Assim, a taxa nominal líquida do CDB será:



i_(liq) = { [ (1 + r) × (1 + π) ]^(du/252) (1 - aliqIR) + aliqIR }^(252/dw) - 1



E a taxa real líquida será dada por:



[ 1 + r_(liq) ]^(du/252) =  { [ (1 + r) × (1 + π) ]^(du/252) (1 - aliqIR) + aliqIR } / [ 1 + π ]^(du/252)  - 1



Desenvolvendo:



r_(liq) = {  { [ (1 + r) × (1 + π) ]^(du/252) (1 - aliqIR) + aliqIR } / [ 1 + π ]^(du/252)  }^(252/dw) - 1 



Onde:

r_(liq): taxa real líquida em % a. a.

r: taxa real bruta em % a. a. (equivalente ao cupom da NTN-B, por exemplo)

π: inflação do período expressa em % a. a.

Vamos supor uma taxa de juro real de 5% a. a. e um prazo de 252 dias úteis. Deixando a inflação variar, teremos o seguinte gráfico:

Gráfico 11.1 – Efeito IR sobre taxa real líquida

---

![img-24.jpeg](img-24.jpeg)

Fonte: Elaborado pelos autores.

Ou seja, embora o título seja corrigido pela inflação, o efeito do pagamento do imposto de renda sobre o ganho nominal corrói o ganho real, levando-o para zero em determinadas situações, da mesma forma que em títulos puramente prefixados.

No exemplo do Gráfico 11.1, para uma inflação IPCA de 25% a. a., o ganho real será de 0%.

## 11.4.1 Exemplo: análise de investimento (CDB pré x CDB DI x LCI)

Responda as questões a seguir referentes a um CDB prefixado:

a) Calcule o valor líquido de um CDB Pré de valor aplicado R$ 1.000.000 com prazo de 730 dias corridos (508 úteis) e taxa de emissão de 16% a. a.

b) Se a taxa da curva de juros Pré da BM&F para 508 dias úteis é 15% a. a., qual o percentual do CDI que esse CDB está pagando?

c) Se você acha que a curva de juros vai cair, você prefere um CDB Pré ou um CDB CDI? E se você acha que vai subir?

d) Dado que as LCIs não pagam imposto de renda, qual o valor do percentual do CDI que esse banco vai oferecer para captar nesse instrumento?

## Solução

a)

|  Valor aplicado | 1.000.000  |
| --- | --- |
|  Dias úteis | 508  |

---

|  Taxa pré | 16% a. a.  |
| --- | --- |
|  Valor futuro bruto | 1.348.774  |
|  Alíquota IR | 15%  |
|  Ganho bruto | 348.774  |
|  IR | 52.316  |
|  Valor futuro líquido | 1.296.548  |
|  Ganho líquido | 296.458  |

b)

|  Taxa pré B3 | 15%  |
| --- | --- |
|  Taxa diária B3 | 0,055%  |
|  Taxa pré banco | 16%  |
|  Taxa diária banco | 0,059%  |
|  Percentual do DI | 106,20%  |

c) Se você acredita que a taxa de juros para aquele prazo vai cair ("fechar"), o melhor a fazer é adquirir o instrumento prefixado, porque o ganho será maior do que aquele obtido no acumulado das taxas diárias overnight (CDI).

d) O valor das taxas equivalentes entre CDBs e LCIs pode ser calculado fazendo as taxas líquidas esperadas iguais para os dois investimentos e alterando a taxa pré da LCI na planilha a seguir:

|   | CDB | LCI  |
| --- | --- | --- |
|  Valor aplicado | 1.000.000 | 1.000.000  |
|  Dias úteis | 508 | 508  |
|  Taxa pré | 16% a. a. | 13,75%  |
|  Taxa pré B3 | 15% | 15%  |
|  Taxa diária | 0,055% | 0,051%  |
|  Taxa diária B3 | 0,055% | 0,055%  |
|  Percentual do DI | 106,20% | 92,15%  |
|  Valor Futuro bruto | 1.348.774 | 1.296.458  |
|  Alíquota IR | 15% | 0%  |
|  Ganho bruto | 348.774 | 296.458  |
|  IR | 52.316 | 0,00  |
|  Valor Futuro líquido | 1.296.548 | 1.296.458  |
|  Ganho líquido | 296.458 | 296.458  |

---

Ou seja, um CDB emitido por esse banco a 106.20% do CDI é equivalente a uma LCI emitida por esse banco para esse prazo a 92.15% do CDI. Se o CDB for prefixado, a taxa de 16% a. a. é equivalente a uma LCI pré a 13.75% a. a.

|  Resumo  |
| --- |
|  Este capítulo introduz o conceito de arbitragem entre instrumentos de renda fixa.  |

32 É ex-ante porque você não sabe quanto é antes do término do período. É por isso que estamos utilizando o conceito de valor esperado ou esperança matemática para as variáveis aleatórias.

---

# Capítulo 12

## Duration e convexidade

Dentro da literatura existente sobre renda fixa e também da prática diária de mercado nas instituições financeiras e outros intermediários que lidam com carteiras de títulos, o tema *duration* e convexidade e seus usos têm sempre lugar garantido.

Entre as utilizações desses, estão o controle de risco de mercado e a criação de estrutura de *hedge* para papéis e carteiras.

Nas seções a seguir, são modelados tanto *duration* quanto convexidade a partir da equação de precificação de títulos geral com que temos trabalhado ao longo do texto.

## 12.1 Hipóteses

De modo a facilitar a modelagem da *duration*, são feitas algumas hipóteses:

- A taxa de juros para desconto do papel é a TIR;
- A curva de juros é, portanto, *flat*, ao longo de todo o prazo do papel;
- Os deslocamentos da curva de juros são paralelos.

Pelas hipóteses descritas anteriormente, percebe-se que para propiciar uma facilitação no cálculo, incorre-se em simplificações que não comprometem a utilização prática do modelo, mas devem ser conhecidas para que não sejamos surpreendidos por eventos inesperados, como uma elevação da curva de juros no longo prazo sem um *hedge* adequado.

## 12.2 Modelagem da *duration*

Isso posto, vamos recuperar o preço do título no mercado brasileiro como:



P = Σ(k=1 até n) FC_k/(1 + y)^(dn_k/2n^2)



Onde y é a TIR em cotação anual do título em questão.

Como buscamos a sensibilidade do título a variações na taxa de juros,

---

derivaremos a expressão anterior em relação a y.

Reescrevendo a equação anterior:



p = Σ(k=1 até n) FC_k × (1 + y)^(-du_k/252)



Derivando em relação à y:



dP/dy = Σ(k=1 até n) FC_k × (-du_k/252) × (1 + y)^(-du_k/252-1)





dP/dy = Σ(k=1 até n) -FC_k × (du_k/252)/(1 + y)(1 + y)^(du_k/252)





dP/dy = -1/(1 + y) Σ(k=1 até n) FC_k × (du_k/252)/(1 + y)^(du_k/252)



A equação anterior fornece a perda ou o ganho em reais em função de uma perturbação na taxa interna de retorno do papel.

No entanto, a ideia é modelar a *duration* como uma elasticidade do preço do papel em relação à taxa de juros. Para isso, é interessante eliminar a dimensão preço do cálculo, o que se faz dividindo os dois lados da equação anterior por P.



1/P dP/dy = -1/(1 + y) Σ(k=1 até n) 1/P FC_k × (du_k/252)/(1 + y)^(du_k/252)



## 12.3 Duration de Macaulay

A *duration* de Macaulay é a parte final da equação anterior. O termo FC_k/(1 + y)^(du_k/252) é o valor presente de cada fluxo de caixa do papel e será representado por P_k.

A *duration* de Macaulay é o prazo médio dos valores presentes dos fluxos de caixa do papel ponderados pelo prazo de cada um desses fluxos de caixa:



M = Σ(k=1 até n) P_k × du_k/252/P 



A dimensão da *duration* é alguma unidade de tempo. Como estamos modelando para a taxa de juros em % a. a., M será dado em anos. Para o mercado local, um ano tem 252 dias úteis.

---

A duration de Macaulay representa o instante no tempo em que um único fluxo de caixa convenientemente pode ser introduzido para representar todos os demais.

O valor desse fluxo é dado por s''(x_2)_1^2 = 0 e será muito importante para hedge de carteiras de renda fixa.

## 12.4 Duration modificada

Continuando a modelagem, chega-se à definição de duration modificada:



D = 1/P dP/dy = -M/(1 + y) 



Para efeitos de praticidade, a Equação 12.2 foi escrita com duas igualdades para indicar que:

- O cálculo da duration modificada é precedido pelo cálculo da duration de Macaulay;
- A duration modificada mede a sensibilidade do preço do papel a oscilações da taxa de juros.

Ou seja, se um papel tem duration modificada de D, quando a TIR variar 1 p.p., o preço do papel vai variar D%.

## 12.4.1 Exemplo: cálculo da duration de Macaulay e duration modificada

Calcule a duration de Macaulay e a duration modificada para uma NTN-F com o fluxo a seguir, dada as taxas de juros do mercado NTN-F de cada um dos prazos. Explique o conceito das duas métricas.

Figura 12.1 – Exemplo de fluxos de caixa de uma NTN-F
![img-25.jpeg](img-25.jpeg)
Fonte: Elaborada pelos autores.

Dados ETTJ:

---



i(100) = 7.5\%





i(226) = 8.0\%





i(352) = 8.5\%





i(478) = 9.0\%



## Solução



P_(NTN-F) = Σ(k=1 até n) FC_k/(1 + i_k)^(dn_k/252)





FC_k = r × 1.000   para  k ≠ n   e   FC_k = r × 1.000 + 1.000   para  k = n



Assim, para r = 10\% a. a.:



P_(NTN-F) = 48,8/(1 + 7,5\%)^(100/252) + 48,8/(1 + 8,0\%)^(250/252) + 48,8/(1 + 8,5\%)^(352/252) + 48,8/(1 + 9,0\%)^(478/252) = 1027,15



Como o título foi descontado utilizando as taxas *spot*, é necessário achar a TIR para o cálculo da *duration*.

Assim, temos uma função:



f(y) = P_(mercado) = - Σ(k=1 até n) FC_k/(1 + y)^(dn_k/252)



A TIR é a taxa y que faz f(y) igualar zero.

Ou seja:



P_(NTN-F) = 48,8/(1 + y)^(100/252) + 48,8/(1 + y)^(226/252) + 48,8/(1 + y)^(352/252) + 48,8/(1 + y)^(478/252) = 1027,15



Para calcular o valor de y, será necessário um método numérico.



y = 8,94\%  a. a.



As parcelas resultantes do desconto pela TIR também são necessárias (vide modelagem):



P_(NTN-F) = 47,17 + 45,19 + 43,30 + 891,49 = 1027,15



Para o cálculo da *duration* de Macaulay:

---



M = Σ(k=1 até n) P_k × (du_k/252)/P





M = 47,17 × (100/252) + 45,19 × (226/252) + 43,30 × (352/252) + 891,49 × (478/252)/1027,15



M = 1,76 anos ≈ 444 dias úteis

A *duration* de Macaulay é o prazo médio que substitui todo o fluxo de recebimentos desse papel em termos de sensibilidade ao risco de mercado. É nesse ponto que um contrato futuro de DI ou *swap* pré x DI teriam de vencer para *hedgear* o risco de taxa de juros.

A *duration* modificada resulta:



D = -M/(1 + y)





D = -1,76/(1 + 8,94\%) = -1,62



> A duration modificada mede a sensibilidade do papel a oscilações na curva de juros. A duration modificada calculada no exemplo anterior, -1,62, significa que para cada 1% de aumento na TIR, o preço do papel cairá, aproximadamente, 1,62%.

## 12.5 Convexidade

Como visto anteriormente, a abordagem utilizada para cálculo da elasticidade do preço dos títulos de renda fixa em função de alterações na taxa de juros é calcular a primeira derivada do preço em relação à taxa interna de retorno do título.

Nessa abordagem, está sendo utilizado o conceito de diferencial da função r = 10\%, o qual é dado pela equação a seguir:



D = 1/P dP/dy



Para uma aproximação do preço final de um título sujeito a uma perturbação na TIR, podemos rearranjar os termos da equação anterior:



dP = D × P × dy





P - P_0 = D × P_0 × (y - y_0)



P = P_0 × [1 + D × (y - y_0)], que é a aproximação de 1. a ordem da função: P = Σ(k=1 até n) FC_k/(1 + y)^(2k) ao redor de P_0.

---

A duration modificada, então, é a diferencial do preço ao redor de P_0. Essa aproximação será melhor quanto menor for a perturbação na TIR. A gráfico a seguir ilustra o conceito:

Gráfico 12.1 – Aproximação duration x reprecificação
![img-26.jpeg](img-26.jpeg)
Fonte: Elaborado pelos autores.

No exemplo anterior, quanto mais afastada de y_0 = 8,94\%, mais o valor do preço indicado pela aproximação de 1.ª ordem diverge da realidade.

Para refinar essa aproximação, pode-se usar a aproximação de segunda ordem, por meio do método numérico conhecido como Expansão de Taylor.

A Expansão de Taylor consiste em aproximar uma função qualquer ao redor de um ponto por um polinômio de ordem tão superior quanto se queira.

Sua fórmula genérica é:



P(x) = Σ(k=1 até ∞) f^k(x - x_0)/k! 



A aproximação fornecida pela convexidade é aquela correspondente à ordem 2:



P(x) = f(x_0) + f'(x_0)(x - x_0) + f'(x_0)/2(x - x_0)^2



Onde P(x) é o polinômio de Taylor que fornece a aproximação de 2.ª ordem para a função f(x).

Com uma pequena adaptação de variáveis e notações, a equação anterior

---

pode ser modificada para representar a aproximação de 2.^a ordem para o preço de um papel em relação à TIR.



P(y) = P(y_0) + dP/dy(y - y_0) + 1/2 d^2P/dy^2(y - y_0)^2





dP = dP/dy(y - y_0) + 1/2 d^2P/dy^2(y - y_0)^2



Dividindo por P dos dois lados:



dP/P = 1/P dP/dy(y - y_0) + 1/2 1/P d^2P/dy^2(y - y_0)^2



E, finalmente:



dP/P = D × dy + 1/2 × C × dy^2



Aproximação de 2.^a ordem para a variação no preço de um título em função da variação em sua TIR. Onde C é a convexidade, definida por:



C = 1/P d^2P/dy^2 



Como esse valor ainda está no campo teórico, é necessário fazer a segunda derivada para achar uma equação para aplicação ao mercado brasileiro.

Recuperando a primeira derivada do preço em relação à taxa de juros:



dP/dy = Σ(k=1 até n) FC_k × (-du_k/252) × (1 + y)^(-du_k/252-1)



Deriva-se novamente:



d^2P/dy^2 = Σ(k=1 até n) FC_k × (-du_k/252) × (-du_k/252 - 1) × (1 + y)^(-du_k/252-2)





d^2P/dy^2 = 1/(1 + y)^2 Σ(k=1 até n) FC_k × (du_k/252) × (du_k/252 + 1)/(1 + y)^(du_k/252)



Dividindo por P dos dois lados:



1/P d^2P/dy^2 = 1/(1 + y)^2 Σ(k=1 até n) 1/P FC_k × (du_k/252) × (du_k/252 + 1)/(1 + y)^(du_k/252)



Assim, chegamos na equação da convexidade de um título local na base 252 dias úteis:



C = 1/P d^2P/dy^2 = 1/(1 + y)^2 Σ(k=1 até n) P_k × (du_k/252) × (du_k/252 + 1)/P 



---

Agora, por meio da Expansão de Taylor ao redor da TIR inicial do título, temos uma parábola que aproxima a função de apreciação do título.

A título de comparação, vejamos como a aproximação por meio da Expansão de Taylor melhora em relação à aproximação pela duration modificada e com a aproximação via convexidade:

Gráfico 12.2 – Aproximação duration x convexidade x reprecificação
![img-27.jpeg](img-27.jpeg)
Fonte: Elaborado pelos autores.

## 12.5.1 Exemplo: cálculo da convexidade (1)

Dada a NTN-F com o fluxo de caixa a seguir:

Figura 12.2 – Exemplo de fluxos de caixa de uma NTN-F
![img-28.jpeg](img-28.jpeg)
Fonte: Elaborada pelos autores.

Dados ETTJ:


i(100) = 7,5\%




i(226) = 8,0\%




i(352) = 8,5\%




i(478) = 9,0\%



Calcule:
a) A convexidade.

---

b) A aproximação de 1.^a ordem para a perda no papel devido a um aumento de 1 p. p. na TIR.
c) A aproximação de 2.^a ordem para a perda no papel devido a um aumento de 1 p. p. na TIR.
d) A variação real teórica para a perda no papel devido a um aumento de 1 p. p. na TIR.

## Solução

a) Convexidade



C = 1/(1 + y)^2 Σ(k=1 até n) P_k × (du_k/252) × (du_k/252 + 1)/P





C = 1/(1 + 8.94\%)^2 47.17 × 100/252 × (100/252 + 1) + 45.19 × (226/252) × (226/252 + 1) + 43.30 × (352/252) × (352/252 + 1) + 891.49 × (478/252) × (478/252 + 1)}{1027.15} = 4.2



b) Aproximação de 1.^a ordem:



dP/P = D × dy





dP/P = -1,62 × 1\% = -1,62\%



c) Aproximação de 2.^a ordem:



dP/P = D × dy + 1/2 × C × dy^2





dP/P = -1,62 × 1\% + 1/2 × 4,2 × 1\%^2 = -1,60\%



d) Variação real:

Reprecificando o papel com uma variação de 1\% (1 basis point) na TIR.



P_(NTN-F) = frac{48,8/(1 + 8,94\% + 1.p.p)^(162) + 48,8/(1 + 8,94\% + 1.p.p)^(252) + 48,8/(1 + 8,94\% + 1.p.p)^(352){+ 48,8/(1 + 8,94\% + 1.p.p)^(252) + 48,8/(1 + 8,94\% + 1.p.p)^(352)}{162}





P_(NTN-F) = 48,8/(1 + 9,94\%)^(252) + 48,8/(1 + 9,94\%)^(252) + 48,8/(1 + 9,94\%)^(352) + 48,8/(1 + 9,94\%)^(352) = 1.010,74



Assim:



dP/P_0 = P - P_0/P_0 = 1.010,74 - 1.027,15/1.027,15 = -1,60\%



Utilizando-se precisão de duas casas depois da vírgula, em porcentagem, o erro ainda não aparece, sugerindo que a convexidade faz com que a

---

aproximação do preço seja bem refinada.

## 12.5.2 Exemplo: cálculo da convexidade (2)

Dado o fluxo de caixa esperado de uma carteira de recebíveis e as taxas de juros atuais:

Tabela 12.1 – Fluxos de caixa da carteira
|  t (anos) | Fluxo de caixa | Taxa pré (ETTJ)  |
| --- | --- | --- |
|  1 | 30 | 8.10%  |
|  2 | 45 | 8.35%  |
|  3 | 27 | 8.55%  |
|  4 | 45 | 9.25%  |
|  5 | 63 | 10.00%  |

Fonte: Elaborada pelos autores.

## Calcular:

a) O Valor Presente da carteira.
b) A TIR.
c) A duration de Macaulay.
d) A duration modificada.
e) A convexidade.
f) Tabela com preço final de repercificação, com aproximação de 1.ª ordem (duration modificada) e 2.ª ordem (duration e convexidade).

## Solução

|  t (anos) | Fluxo de caixa | Taxa pré ETTJ | VP ETTJ | VP TIR | P(k)×t(k) |   | P(k)×t(k)×[t(k)+1]  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |  P |  | P |   |
|  1 | 30 | 8,10% | 27,75 | 27,46 | 0,17 |  | 0,35 |   |
|  2 | 45 | 8,35% | 38,33 | 37,70 | 0,48 |  | 1,43 |   |
|  3 | 27 | 8,55% | 21,11 | 20,70 | 0,39 |  | 1,57 |   |
|  4 | 45 | 9,25% | 31,59 | 31,58 | 0,80 |  | 4,00 |   |
|  5 | 63 | 10,00% | 39,12 | 40,46 | 1,28 |  | 7,69 |   |
|   |  | Preço | 157,90 | 157,90 | 3,13 |  | 15,04 |   |
|   |  | y | 9,26% |  | M |  | 3,13 |   |
|   |  | Δ | 0,00 |  | D |  | -2,86 |   |
|   |  |  |  |  | C |  | 12,60 |   |

---

Com os valores de duration e convexidade é possível elaborar a tabela a seguir:

|  y (TIR) | Δy | P |   | ΔP |   |   | ΔP(%)  |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |   |  Equação | 1.ª ordem | 2.ª ordem | Equação | 1.ª ordem | 2.ª ordem | Equação | 1.ª ordem | 2.ª ordem  |
|  4,76% | -4,5% | 180,43 | 178,23 | 180,24 | 22,53 | 20,33 | 22,34 | 14,27% | 12,87% | 14,15%  |
|  5,26% | -4,0% | 177,69 | 175,97 | 177,56 | 19,79 | 18,07 | 19,66 | 12,53% | 11,44% | 12,45%  |
|  5,76% | -3,5% | 175,01 | 173,71 | 174,93 | 17,12 | 15,81 | 17,03 | 10,84% | 10,01% | 10,79%  |
|  6,26% | -3,0% | 172,40 | 171,45 | 172,35 | 14,50 | 13,55 | 14,45 | 9,18% | 8,58% | 9,15%  |
|  6,76% | -2,5% | 169,85 | 169,19 | 169,82 | 11,95 | 11,29 | 11,92 | 7,57% | 7,15% | 7,55%  |
|  7,26% | -2,0% | 167,35 | 166,93 | 167,33 | 9,45 | 9,04 | 9,43 | 5,98% | 5,72% | 5,97%  |
|  7,76% | -1,5% | 164,91 | 164,68 | 164,90 | 7,01 | 6,78 | 7,00 | 4,44% | 4,29% | 4,43%  |
|  8,26% | -1,0% | 162,52 | 162,42 | 162,52 | 4,62 | 4,52 | 4,62 | 2,93% | 2,86% | 2,92%  |
|  8,76% | -0,5% | 160,18 | 160,16 | 160,18 | 2,28 | 2,26 | 2,28 | 1,45% | 1,43% | 1,45%  |
|  9,26% | 0,0% | 157,90 | 157,90 | 157,90 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00%  |
|  9,76% | 0,5% | 155,66 | 155,64 | 155,67 | -2,23 | -2,26 | -2,23 | -1,41% | -1,43% | -1,41%  |
|  10,26% | 1,0% | 153,48 | 153,38 | 153,48 | -4,42 | -4,52 | -4,42 | -2,80% | -2,86% | -2,80%  |
|  10,76% | 1,5% | 151,34 | 151,12 | 151,35 | -6,56 | -6,78 | -6,55 | -4,15% | -4,29% | -4,15%  |
|  11,26% | 2,0% | 149,25 | 148,86 | 149,26 | -8,65 | -9,04 | -8,64 | -5,48% | -5,72% | -5,47%  |
|  11,76% | 2,5% | 147,20 | 146,61 | 147,23 | -10,70 | -11,29 | -10,67 | -6,78% | -7,15% | -6,76%  |
|  12,26% | 3,0% | 145,19 | 144,35 | 145,24 | -12,71 | -13,55 | -12,66 | -8,05% | -8,58% | -8,02%  |
|  12,76% | 3,5% | 143,23 | 142,09 | 143,31 | -14,67 | -15,81 | -14,59 | -9,29% | -10,01% | -9,24%  |
|  13,26% | 4,0% | 141,31 | 139,83 | 141,42 | -16,59 | -18,07 | -16,48 | -10,51% | -11,44% | -10,44%  |
|  13,76% | 4,5% | 139,43 | 137,57 | 139,58 | -18,47 | -20,33 | -18,32 | -11,70% | -12,87% | -11,60%  |

## Resumo

Este capítulo define e demonstra como calcular as medidas de sensibilidade às oscilações de taxas de juros dos instrumentos de renda fixa.

---

# Exercícios propostos

1. Uma carteira de recebíveis de um banco tem a seguinte distribuição aproximada:

|  t (anos) | Fluxo de caixa | Taxa pré (ETTJ)  |
| --- | --- | --- |
|  1 | 90 | 8,50%  |
|  2 | 120 | 8,70%  |
|  3 | 170 | 9,00%  |
|  4 | 40 | 9,30%  |
|  5 | 35 | 10,00%  |

Calcular:

a. Valor Presente.
b. TIR.
c. Duration de Macaulay.
d. Duration modificada.
e. Convexidade.
f. Aproximação de 1.ª ordem para a perda na carteira se a TIR aumentar 1 p. p.
e. Aproximação de 2.ª ordem para a perda na carteira se a TIR aumentar 1 p. p.

2. Supondo um título com as seguintes características:

- cupons semestrais de juros com taxa de cupom r ao semestre
- com n semestres de prazo
- taxa interna de retorno y

E outro título com o mesmo prazo de vencimento e taxa de retorno, porém sem pagamento de cupons.

a. Qual a razão entre a duration modificada desses títulos?
b. Supondo que o título sem cupom vença em um prazo m, qual deve ser o valor da TIR desse segundo título para que a duration modificada dos dois seja a mesma?

---

# Capúulo 13

# Derivativos de taxas de juros: futuros

Um conceito muito difundido no mercado financeiro é o de arbitragem entre instrumentos de níveis de risco similares.

## 13.1 Introdução aos derivativos

Neste capítulo, abordaremos uma linhagem de instrumentos financeiros chamada derivativos. Focaremos em alguns dos principais derivativos de taxas de juros no Brasil.

O derivativo é um instrumento financeiro cujo preço depende ou é derivado de um ou mais ativos. Esses ativos que influenciam o preço do derivativo são chamados de ativo-objeto, que podem ser preços, índices, taxas etc.

O derivativo é um contrato que contém todas as características abaixo³³:

1. Seu preço oscila em resposta às variações dos preços ou taxas do ativo-objeto;
2. Normalmente, não requer nenhum investimento inicial. Quando existe um pagamento para entrar no contrato, o valor é significativamente menor do que o investimento requerido para comprar o ativo-objeto;
3. Líquida em uma data futura.

Os contratos de derivativos mais padronizados, normalmente são negociados em bolsa. Neste caso, a bolsa é a contraparte central, ou seja, a bolsa é contraparte do comprador e do vendedor do contrato.

Tipicamente, os derivativos não padronizados são operados no mercado de balcão, ou seja, não necessariamente haverá uma contraparte central que garantirá a liquidação do contrato – a não ser que ambas as partes optem por registrar o contrato “com garantia”. Ao optarem pela modalidade “com garantia” no registro do contrato no mercado de balcão, a clearing, ou câmara de compensação, garantirá a liquidação do contrato. Para isso, a clearing solicitará garantias das contrapartes para viabilizar a liquidação do contrato caso uma das partes não seja capaz de honrá-lo.

As características principais das bolsas são:

---

- Disponibilização de contratos padronizados com parametrização específica, como tamanho do lote, datas de vencimento, tipo específico de cada mercadoria etc.;
- Existência de uma câmara de compensação central, que realiza as liquidações entre os clientes;
- Mecanismos de salvaguardas de operações, como depósitos de margens de garantia e ajustes diários.

Já os derivativos de balcão, Over the counter (OTC), têm as seguintes características principais:

- São contratos customizados entre as partes envolvidas;
- Apresentam risco de crédito de contraparte;
- Podem incluir mecanismos de mitigação de risco de crédito, que será definido entre as partes envolvidas.

Os grandes grupos de derivativos existentes são: futuros, termos, swaps e opções.

Neste texto, serão estudados os derivativos cujos ativos subjacentes são taxas de juros disponíveis no mercado local, notadamente, os swaps e os contratos futuros negociados na B3.

## 13.2 Contratos futuros

O contrato futuro é um contrato negociado em uma bolsa de futuros para comprar ou vender uma commodity ou um instrumento financeiro por um preço predefinido em uma data previamente determinada no futuro.

Os contratos futuros são padronizados para facilitar a sua negociação e, com isso, aumentar o volume e a liquidez.

As duas partes envolvidas no contrato são:

- Comprador (“comprado”), que assume a posição comprada (long position);
- Vendedor (“vendido”), que assume a posição vendida (short position).

Ambas as partes têm obrigação de cumprir sua parte no contrato.

O comprado tem a obrigação de comprar em uma data futura enquanto o

---

vendido tem a obrigação de vender em uma data futura.

Neste livro, nosso enfoque será mais na parte técnica (financeira) e quantitativa do que em detalhes operacionais do mercado de futuros, que podem ser obtidos facilmente em bibliografia especializada.

## 13.3 Contrato futuro de DI

O contrato futuro de DI é o derivativo mais importante do mercado brasileiro, visto que reflete instantaneamente as condições do mercado de juros e a curva de juros da economia (ETTJ) para os diversos prazos disponíveis.

Características gerais:

- Objeto do contrato: taxa de juros de CDI-Cetip entre data negociação e vencimento;
- Cotação: taxa média de 1 dia expressa ao ano, base 252 dias úteis;
- Vencimento: 1.º dia útil do mês de vencimento;
- Contrato não permite a entrega física.

Preço teórico:



P U_(D I) = 1 0 0 . 0 0 0/(1 + i _b)^(d u _b/2 5 2) tag {13.1}



Onde:

PU_(DI): preço unitário de um contrato futuro de DI;

i_b: taxa de juros para o vencimento k.

## 13.3.1 Convenções

Neste tópico, mostraremos algumas convenções considerando o jargão de mercado.

### Compra de DI:

- Compra de taxa, que equivale a venda de PU;
- Recebe ajuste com a alta do DI acumulado para aquele dado vencimento;

---

- Para contabilidade, P&L e risco, o controle é feito como se o comprador de DI tivesse emitido um título prefixado;
- No jargão do mercado, a contraparte que assume uma posição comprada em DI está "tomada".

Figura 13.1 – Comprado em DI
![img-29.jpeg](img-29.jpeg)
Fonte: Elaborada pelos autores.

Observe a Figura 13.1. Tudo se passa como se o comprador do DI tivesse emitido um título prefixado com a taxa 1/8 de referência inicial.

## Venda de DI:

- Venda de taxa, que equivale a compra de PU;
- Recebe ajuste com a baixa do CDI acumulado para aquele dado vencimento;
- Para contabilidade, P&L e risco, o controle é feito como se o comprador de DI tivesse adquirido um título prefixado;
- No jargão do mercado, a contraparte que assume uma posição vendida em DI está "dada".

Figura 13.2 – Vendido em DI
![img-30.jpeg](img-30.jpeg)
Fonte: Elaborada pelos autores.

É possível mostrar que o dispositivo de ajuste diário do futuro de DI é tal que faz com que a taxa do agente que comprou ou vendeu o contrato receba ou pague fluxos de caixa que tornam o seu resultado final a diferença entre a taxa DI acumulada e a taxa de referência da entrada no contrato.

---

O resultado final do ajuste diário do período de uma posição em futuro de DI é dado por:



AjusteTotal = q × PU_B^k × [ (1 + iₖ)^(dqₖ/252) - prod_(j=0)^(dqₖ-1) (1 + DI_j)^(1/252) ] 



Onde:

- q: quantidade de contratos, expressos na ótica de PU (e não de taxa)
- iₖ: taxa de juros atual (ETTJ) do contrato futuro vencendo na data k
- PU_B^k: PU na data inicial para o futuro de DI vencendo na data k
- DI_j: taxa DI de cada dia útil j

## 13.3.2 Exemplo: cálculo do ajuste diário do DI futuro (1)

Em 27/3/2014, o contrato de DI futuro com vencimento em 2/1/2015 foi negociado a 92.152.

Quem vendesse esse contrato (vendedor de taxa) e ficasse com ele até o vencimento, estaria apostando na queda das taxas de juros para 195 dias úteis.

A posição desse agente pode ser representada como:

|  PRÉ | 92.152 | 92.152 DI  |
| --- | --- | --- |

Em sua ponta ativa, esse agente receberá no vencimento o valor prefixado de R$ 100.000. Em sua ponta passiva, esse agente receberá no vencimento o valor de:



92.152 × (1 + Acumulado\ do\ CDI)\ entre\ 27/3/2014\ e\ 2/1/2014



Por meio do PU do contrato e sabendo que o valor no vencimento é de R$ 100 mil, pode-se determinar qual a taxa de juros de CDI "embutida no contrato":



PU_(DI) = 100.000/(1 + iₖ)^(dqₖ/252)



Substituindo pelos valores do problema:

---



92.152 = 100.000/(1 + i_k)^(195/252)



i_k = 11,14\% a. a.

Alterando moderadamente a Equação 13.2, teríamos:



AjusteTotal = q × [ PU_0^k × (1 + i_k)^(du_k/252) - PU_0^k × prod_(j=0)^(du_(k-1)) (1 + DI_j)^(1/252) ]



Desenvolvendo:



AjusteTotal = q × [ 100.000 - PU_0^k × prod_(j=0)^(du_(k-1)) (1 + DI_j)^(1/252) ]



Para efeitos didáticos, podemos reescrever o produtório anterior em função da taxa DI média do período:



AjusteTotal = q × [ 100.000 - PU_0^k × (1 + DĪ)^(dn/252) ]



Caso ocorresse a taxa média de 11.14% a. a. relativa aos 195 dias úteis do contrato, então quem tivesse comprado ou vendido por 92.152 não pagaria/receberia nada.

Como a taxa que prevaleceu no mercado foi diferente, então ocorreram ajustes refletindo pagamentos e recebimentos dos agentes.

Supondo que a taxa média tenha ficado acima de 11.14% a. a., por exemplo, em 13% a. a.:

Perda do vendido (= - ganho do comprado)



{l}
V = 100.000 - 92.152x(1 + 0,13)(195/252) 

V = 100.000 - 101.292,52 = -1.292.52 





Supondo que a taxa média tivesse ficado abaixo de 11.14% a. a., por exemplo, em 10% a. a.:

Ganho do vendido (= - compra do comprado)



{l}
V = 100.000 - 92.152x(1 + 0,10)(195/252) 

V = 100.000 - 94.634,01 = 794,71 





## 13.3.3 Exemplo: cálculo do ajuste diário do DI futuro (2)

Preencha a tabela a seguir com os dados diários de uma posição comprada

---

(em taxa) de 50 contratos de DI de 1 dia com vencimento em 195 dias úteis:

|  Data | Taxa pré | Dias úteis | PU | MtM | DI | Ajuste | P&L acumulado  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0 | 11,14% |  |  |  | 10,70% |  |   |
|  1 | 11,23% |  |  |  | 10,69% |  |   |
|  2 | 11,07% |  |  |  | 10,72% |  |   |
|  3 | 11,45% |  |  |  | 10,68% |  |   |

Solução

|  Data | Taxa pré | Dias úteis | PU | MtM | DI | Ajuste | P&L acumulado  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0 | 11,14% | 195 | 92.152 | -4.607.603 | 10,70% | 0 | 0  |
|  1 | 11,23% | 194 | 92.133 | -4.606.663 | 10,69% | 2.799 | 2.799  |
|  2 | 11,07% | 193 | 92.274 | -4.613.693 | 10,72% | -5.173 | -2.373  |
|  3 | 11,45% | 192 | 92.072 | -4.603.620 | 10,68% | 11.937 | 9.564  |

Equações utilizadas:



Ajuste_t = MtM_t - MtM_(t-1) × (1 + CDI_(t-1))





P&L_t = P&L_(t-1) × (1 + CDI_(t-1)) + Ajuste_t



O ajuste é calculado pela BM&F, enquanto o P&L é calculado pela instituição financeira.

## 13.4 Contrato futuro de DDI

O contrato futuro de DDI é o equivalente ao contrato futuro de DI, porém referenciado ao dólar, USD.

A mecânica básica do contrato é análoga ao futuro de DI, porém com as seguintes diferenças:

- O valor do ativo subjacente está em USD e é apregoado em reais, BRL, logo, existe uma taxa de câmbio BRL/USD multiplicando o nocional em USD;
- A referência é o money market americano, em que as taxas de juros são em USD e a capitalização é linear.

Características gerais:

- Objeto do contrato: cupom cambial, no período compreendido entre a data de operação, inclusive, e a data de vencimento, exclusive;

---

- Cotação: PU igual a USD 100.000, descontado pela taxa de cupom cambial (taxa de juros em USD para liquidação no Brasil);
- Vencimento: 1.º dia útil do mês de vencimento;
- Contrato não permite a entrega física.

## Preço teórico



P U_(D D I) = 1 0 0 . 0 0 0/(1 + C ₖ × d c ₖ/3 6 0) × M × S tag {13.3}



Onde:

C_k: cupom cambial para a data k

dc_k: dias corridos até a data k

S: USD PTAX

M: valor em USD de cada ponto de PU atribuído pela B3

Como na prática M = 2, a equação anterior do PU teórico de DDI vai ficar:



P U_(D D I) = 5 0 . 0 0 0/(1 + C × d c/3 6 0) × S tag {13.4}



## 13.4.1 O cupom cambial

O cupom cambial é a taxa de juros em USD para instrumentos liquidados em reais no Brasil.

É equivalente à taxa de juros americana acrescida de um prêmio pelo risco:



C = i ^* + r p tag {13.5}



Onde:

C: taxa de cupom cambial

i^*: taxa de juros dos Estados Unidos para o mesmo prazo

rp: risco-país percebido pelos agentes

## 13.5 Contrato futuro de dólar

O contrato futuro de USD é um derivativo muito importante transacionado na B3. Seu ativo subjacente é a taxa de câmbio BRL/USD.

Características gerais:

---

- Objeto do contrato: USD;
- Cotação: BRL/USD;
- Lote: USD 50.000;
- Vencimento: 1.º dia útil do mês de vencimento;
- Contrato não permite a entrega física.

## Preço teórico



f_(USD) = S × (1 + i)^(du/252)/(1 + C × dC/360) 



Onde:

f_(USD): futuro da taxa de câmbio de BRL/USD

S: taxa de câmbio de BRL/USD à vista

i: taxa prefixada em reais

C: cupom cambial

## 13.6 Paridade descoberta de taxas de juros

Supondo livre movimentação de capitais no país e indiferença entre ativos (mesmo emissor, por exemplo), em equilíbrio, os títulos doméstico e estrangeiro devem apresentar a mesma rentabilidade.

Dessa maneira, podemos escrever a relação de (não) arbitragem:



(1 + i_t) = E_t S_(t+1)/S_t × (1 + i_t^*) 



A equação 13.7 expressa que o valor futuro esperado de um real aplicado à taxa doméstica tem de ser igual ao valor futuro do mesmo um real, convertido para dólar e aplicado na taxa externa. A paridade é descoberta, porque não existe nenhuma operação extra realizada que garanta que isso vai ocorrer.

É uma equação de equilíbrio e, portanto, envolve a percepção dos agentes sobre o comportamento da taxa de câmbio no instante seguinte.

A equação anterior pode ser reescrita para:



(1 + i_t) = (1 + i_t^*) × (1 + E_t S_(t+1)/S_r - S_t/S_t)



---

Aplicando o logaritmo dos dois lados, teremos:



i _t ≈ i _t ^* + (E _t S_(t + 1) - S _t)/S _t tag {13.8}



Quando um agente acredita que essa paridade não vai se verificar na prática, ou seja, que a taxa de câmbio não vai sofrer essa desvalorização indicada na Equação 13.8, ele faz o que se chama de *carry-trade*, ou seja, toma USD emprestado na moeda externa e aplica S_t × 1 = S_t na moeda local. Como a desvalorização cambial esperada é baixa, a estratégia geraria um resultado positivo.

## 13.7 Paridade coberta das taxas de juros

Quando se usa o mercado de derivativos cambiais, notadamente, o USD futuro, consegue “travar” o valor da expectativa para a desvalorização cambial naquele momento.

Partindo-se da equação do preço teórico do USD futuro:



f_(U S D) = S × (1 + i)^(d u/2 5 2 2)/(1 + C × d c/3 6 0)



Para simplificar a álgebra, usaremos as taxas de juros ao período:



f_(U S D) = S × (1 + i)/(1 + C)



Aplicando o logaritmo em ambos os lados:



i ≈ C + ln (f_(U S D)/S)



Substituindo, chega-se a equação da paridade coberta de taxas de juros:



i _t ≈ i _t ^* + r p + ln (f_(U S D)/S) tag {13.9}



Onde o termo ln(f_(USD)/S) é a expectativa de variação cambial de moeda doméstica. Logo, a taxa de juros doméstica é igual à taxa de juros internacional, mais um prêmio de risco e mais a expectativa de valorização cambial.

## 13.7.1 Exemplo: cálculo do preço teórico de contratos futuros

Calcule o preço teórico dos contratos futuros a seguir:

---

a) DI de 1 dia com vencimento em 195 dias úteis e taxa de 11.14% a. a.
b) Ibovespa futuro com Ibovespa à vista a 49.646 pontos, vencimento em 23 dias úteis e taxa pré de 10.76% a. a.
c) DDI futuro com vencimento em 96 dias corridos, taxa de câmbio à vista de BRL/USD 2.2621 e cupom cambial de 0.78% a. a.
d) USD futuro com os dados do item c) e taxa pré de 10.84% a. a.

# Solução

a)



P U_(D I) = 1 0 0 . 0 0 0/(1 + i)^(d u/2 6 2)





P U_(D I) = 1 0 0 . 0 0 0/(1 + 1 1 , 1 4 \%)^(9 6/2 6 2) = 9 2. 1 5 2, 0 6



b)



F_(I b o v e s p a) = I b o v e s p a × (1 + i)^(d u/2 6 2)





F_(I b o v e s p a) = 4 9. 6 4 6 × (1 + 1 0, 7 6 \%)^(2 3/2 6 2) = 5 0. 1 1 1, 2 3



c)



P U_(D D I) = 5 0 . 0 0 0/(1 + C × d c/3 6 0) × S





P U_(D D I) = 5 0 . 0 0 0/(1 + 0 , 7 8 \% × 9 6/3 6 0) × 2, 2 6 2 1 = 1 1 2. 8 7 0, 2 3



d)



F_(U S D) = S × (1 + i)^(d u/2 6 2)/(1 + C × d c/3 6 0)





F_(U S D) = 2. 2 6 2 1 × (1 + 1 0 . 8 4 \%)^(6 3/2 6 2)/(1 + 0 . 7 8 \% × 9 6/3 6 0) = 2. 3 1 7 2



# 13.7.2 Exemplo: cálculo de uma posição em "kit Brasil"

Imagine um portfólio de um fundo multimercado muito agressivo, composto por 20.000 LFTs como lastro (PU= 6.033), posicionado em "kit Brasil": dado em 5.000 contratos futuros de DI, comprado em 1.500 contratos futuros de Ibovespa, vendido em 400 contratos de DDI futuro e vendido em 900 contratos de USD futuro.

---

Assuma dos dados calculados nos itens da questão anterior. Determine:

a) Qual o PL do fundo?
b) Qual o MtM (valor a mercado) da carteira off balance?
c) Qual a perda na carteira off balance se a bolsa cair 5%, a curva pré subir em paralelo 70 bps, o cupom cambial subir 30 bps e o USD subir 8%?
d) O PL do fundo depois dessa perda.

## Solução

PL do fundo

Os futuros não têm valor intrínseco associado e são contabilizados off-balance, só gerando resultados ao longo do tempo, por meio da variação dos valores das variáveis econômicas que são usadas para precificá-los.

Assim, o patrimônio (lastro) será dado pelo valor das LFTs.



MtM_(LFTs) = PU_(LFT) × Q = 6.033 × 20.000 = 120.660.000



MtM inicial da carteira



VL_(CDB-CDI) = VF_(CDB-CDI) - [(VF_(CDB-CDI) - VA) × aliqIR]



O valor da quantidade de contratos é positivo, porque ao vender o contrato futuro de DI (apostar na queda da taxa), estamos, ao mesmo tempo, vendendo a taxa CDI e comprando o PU. Como visto anteriormente, a contabilização de operações de DI é feita pelo PU, daí o sinal positivo na quantidade de contratos.



MtM_(Ibovespa) = F_(Ibovespa) × Q = 50.111,23 × 1.500 = 75.166.849





MtM_(DDI) = PU_(DDI) × Q = 112.870,23 × 400 = 45.148.092





MtM_(USD) = f_(USD) × Q = 2,3172 × (-900) × 50.000 = -104.273.371



Em relação ao futuro de USD, cada lote se refere a USD 50.000, por isso a multiplicação anterior.

MtM final da carteira

Se a taxa de juros subir 70 basis points em paralelo, a taxa para 195 dias úteis vai para 11.14% (taxa inicial) mais 0.70% (70 basis points), chegando a 11.84% a. a.

---



{l}
MtM_(DI) = 91.705,43 × 5.000 = 458.527.155 

P\&L_(DI) = 458.527.255 - 460.760.306 = -2.233.151 





Os outros valores são:



{l}
MtM_(Ibovespa) = 47.164.70 × 1.500 = 71.449.579 

MtM_(DDI) = 121.803.61 × 400 = 48.721.043 

MtM_(USD) = 2.3172 × (-900) × 50.000 = -112.705.465 





O ajuste total na carteira será R -10.809.564, o que levará o PL do fundo a R$ 109.850.436.

**Resumo**

Este capítulo apresenta os principais futuros do mercado brasileiro de renda fixa.

33 De acordo com o IAS 39.

---

# Capítulo 14

## Derivativos de taxas de juros: swaps

### 14.1 Definição

O swap é um contrato derivativo em que as duas contrapartes trocam remunerações (taxas de juros em moedas distintas, indexadores etc.) ou fluxos de caixa futuros.

Também podem ser entendidos como instrumentos em que se contrata um ativo e um passivo, simultaneamente, com indexadores diferentes, partindo de um mesmo valor inicial para ambas as pontas do swap, a ponta ativa e a ponta passiva.

**Características principais:**

- Operação de balcão. Pode-se negociar o indexador, valor do indexador (para adequá-lo ao ativo ou passivo do instrumento que a contraparte quer proteger), prazo, volume, pagamento de cupons;
- Mais caro do que os futuros;
- É usado pelo Bacen (na modalidade USD x Selic) para fazer política cambial.

### 14.2 Principais modalidades de swap locais

#### 14.2.1 O swap Pré x DI

Pré x DI: recebe (paga) taxa pré em uma ponta e recebe (paga) acumulado de um percentual α das taxas DI na outra.



(1 + i)^(du/252) = ∏(k=0 até α-1) {1 + α × [ (1 + E_t(DI_k))^(1/252) - 1 ] } 



Onde:

- i: taxa prefixada
- α: percentual do CDI

E_t(DI_k): esperança em t (presente) sobre o comportamento futuro da taxa DI

---

diária em base anual

Ou seja, a condição de não arbitragem característica da precificação de instrumentos derivativos requer que o valor futuro das duas pernas (ou pontas) do swap seja análogo. Daí a presença na Equação 14.1 do operador esperança dobre as taxas DI de cada dia útil futuro.

No contrato desse swap, vão estar discriminadas a taxa pré de referência e o percentual de CDI de emissão.

## 14.2.2 O swap Pré x IPCA

Pré x IPCA: recebe (paga) taxa pré em uma ponta e recebe ou paga variação da inflação mais cupom de IPCA³⁴ na outra.



(1 + i)^(du/252) = E_t(IPCA_(du))/IPCA_0 (1 + C_(IPCA))^(du/252) 



No contrato desse swap, o cupom de IPCA é definido por meio da expectativa do IPCA no vencimento. Ela se manifesta por meio do cupom de IPCA, a taxa de juros real para aquele respectivo vencimento.

## 14.2.3 Relação de Fischer

A equação de Fischer é usada em Economia para relacionar as taxas de juros nominal e real. Podemos fazê-lo por meio da Equação 14.2.

Em vez de escrever a variação do IPCA com os números índices, vamos fazê-lo com a introdução da inflação anual média esperada.



(1 + i)^(du/252) = (1 + π^e)^(du/252) (1 + C_(IPCA))^(du/252) 



Como todos os termos estão elevados a du/252, pode-se resumir:



(1 + i) = (1 + π^e)(1 + C_(IPCA))



E a taxa de juros real pode ser escrita como:



C_(IPCA) = (1 + i)/(1 + π^e) - 1 



Ou seja, a taxa de juros real é igual à taxa de juros nominal descontada da inflação esperada.

## 14.2.4 O swap Pré x dólar

Pré x USD: recebe (paga) taxa pré em uma ponta e recebe (paga) variação cambial mais um cupom cambial na outra.

---



E _t (P T A X_(d u - 1))/P T A X_(0 - 1) (1 + C × d c/3 6 0) = (1 + i)^(d u/2 5 2) tag {14.5}



Onde:

E_t(PTAX_(du - 1)): expectativa na data inicial sobre a taxa de câmbio medida pela PTAX de venda no dia anterior ao vencimento

PTAX_(0-1): taxa de câmbio medida pela PTAX no dia anterior à data de início do swap

NDF

A expectativa em t sobre a taxa de câmbio (medida pela PTAX de venda no dia anterior ao vencimento) é o USD futuro, logo:



f_(U S D)^(d u) = P T A X_(0 - 1) (1 + i)^(d u/2 5 2)/(1 + C × d c/3 6 0) tag {14.6}



Ou seja, um swap pré x USD tem o mesmo nível de risco, exposição e fluxo de caixa de um USD futuro. Na realidade, esse contrato tem o nome de NDF, non deliverable forward, que é um USD futuro transacionado no balcão.

## 14.2.5 O swap dólar x DI

USD x DI: recebe (paga) variação cambial mais cupom cambial e recebe (paga) o acumulado das taxas DI na outra.



E _t P T A X_(d u - 1)/P T A X_(0 - 1) (1 + C × d c/3 6 0) = prod_(k = 0)^(d - 1) {1 + α × [ (1 + E _t (D I ₖ))^(1/2 5 2) - 1 ] } tag {14.7}



## 14.2.6 O swap em percentual do DI

Quando um agente quer proteger um ativo ou passivo que apresenta um spread em relação às taxas básicas prefixadas de juros (curvas da B3), as taxas de swap não serão iguais às vigentes naquele momento.

Como as taxas devem ser arbitradas, se o ativo do cliente tem um spread em relação ao mercado de juros, o banco vai oferecer um swap que anule o efeito desse spread.

Pelo conceito de não arbitragem, o valor inicial desse swap (a menos do lucro do banco) deve ser igual a zero.

---

Assim, se existe um spread de crédito no título emitido ou adquirido por um dado emissor, as duas pontas devem sair arbitradas e com uma referência diferente dos 100% do DI.

Se o cliente quer uma das pontas em percentual do DI e a outra ponta apresenta um spread em relação ao mercado, surge o swap em percentual do DI.

Algebricamente:



(1 + i_(B3))^(du/252)(1 + s)^(du/252) = ∏(k=0 até d-1) {1 + α × [ (1 + E_t(DI_k))^(1/252) - 1 ] } 



Onde:

- i_(B3): taxa pré para o prazo du na B3
- S: spread de crédito/ liquidez na ponta pré
- α: correspondente ao spread da taxa pré, porém em percentual do DI

O spread aplicado na taxa pré para o período pode ser entendido como outra forma de cotação de spreads de crédito/ liquidez muito comuns em debêntures. O spread DI+.

Assim, existem duas maneiras de referenciar um instrumento pós-fixado em taxas flutuantes indexado ao DI, a forma % DI e a forma DI+.

Na forma percentual do DI, formaliza-se o valor de α no contrato do swap, CDB etc. Na forma DI+, o que é formalizado é o termo S, que é um spread em taxa fixa aplicado ao produtório do DI equivalente, conforme equação anterior.

## 14.2.7 Exemplo: cálculo do percentual do DI de um swap

Dado que a taxa pré para 178 dias úteis é 11.11% a. a., calcule o percentual do CDI de um swap em que o cliente quer trocar a remuneração de aplicação que ele tem à taxa de 13% a. a. por uma remuneração em DI. Mostre como fica o balanço do cliente com o ativo e o swap.

### Solução

O percentual do CDI incide sobre a taxa diária, logo:



(1 + i_a)^(du/252) - 1 = i_a



---



(1 + 11.11\%) 178/252 - 1 = 0,04183\%  a. a. (equivalente a  100\%  do CDI)





(1 + 13\%) 178/252 - 1 = 0,04851\%  a. a.



Dividindo uma pela outra, temos: 0,04183\%/0,04851\% = 116\%

**Balanço do cliente**

|  Aplicação | Pré | 13% |   |
| --- | --- | --- | --- |
|  Swap | CDI | 115,98% | 13% Pré  |

Nesse exemplo didático, estamos assumindo que o lucro da instituição financeira é zero no swap. Na verdade, 116% do CDI é o percentual mínimo necessário para equalizar a taxa de 13% a. a. (que é equivalente a 116% da taxa CDI naquele momento). O banco vai oferecer um percentual do CDI menor que 115.98%, de forma a obter seu lucro.

## 14.2.8 Exemplo: cálculo de um swap dólar x Pré

Um banco forneceu hedge cambial a um cliente por meio de um swap USD x Pré (banco passivo em USD e ativo em taxa pré). Esse swap teve 452 dias corridos (310 dias úteis), taxa pré de 11,60% a. a. e 1,45% a. a. Nesse momento, a taxa de câmbio estava R$ 2,26/USD. Supondo que um ano depois (passados 360 dias corridos e 252 dias úteis), a taxa pré para o vencimento do swap é 12,30% a. a., o cupom cambial é 2% a. a. e a taxa de câmbio é R$ 2,50/USD.

### Determine:

a) O ajuste MtM dessa operação para o banco.
b) O valor do ajuste na curva para o banco.
c) O razonete com a operação inicial e com a reversão do swap.

### Solução

a)



MtM_(CupomUSD) = 10.000.000 × 2,26 × (1 + 1,45\% 452/360)/1 + 2\% × 92/360 × 2,50/2,26 = 25.325.696





MtM_(Pré) = 22.600.000 × (1 + 11,60\%) 310/252/(1 + 12,30) 58/252 = 25.185.329



---

Balanço a mercado

|  Pré | 25.185.329 | 25.325.969 | Cupom  |
| --- | --- | --- | --- |
|   |  | -140.640 | P&L  |
|  Ativo | 25.185.329 | 25.185.329 | Passivo  |

b)



Accrual_(CupomUSD) = 10.000.000 × (1 + 1,45\% 360/360) × 2,50 = R\ 25.362.500





Accrual_(Pré) = 22.600.000 × (1 + 11,60\% )^(252/252) = 25.221.600



Ajuste curva = -140.900

c)

Balanço a mercado

|  Operação inicial | Pré | 25.185.329 | 25.185.329 | Cupom  |
| --- | --- | --- | --- | --- |
|  Reversão | Cupom | 25.185.329 | 25.185.329 | Pré  |
|  Resultado |  |  | -140.368 | P&L  |

Para acabar com o risco da operação, basta fechar outro swap com as pontas trocadas e as taxas de mercado. Esse expediente trava também o imposto de renda, que só será recolhido na data de vencimento.

## 14.2.9 Exemplo: cálculo de uma Non-Deliverable Forward (NDF)

Qual o valor de um NDF para 452 dias corridos e 310 dias úteis se a taxa pré para esse prazo é 11,60% a. a., o cupom cambial é 1,45% a. a. e a taxa de câmbio instantânea é R$ 2,2621/USD? Esse cupom é limpo ou é sujo? Qual o valor do cupom sujo se a taxa de câmbio do dia anterior fechou em R$ 2,30/USD?

## Solução



F_(USD) = 2,2621 × (1 + 11,60\%)^(310/252)/(1 + 1,45\% × 452/360) = 2.5427



O cupom é sujo, porque a taxa de câmbio de referência é a PTAX de venda. O cupom sujo é a taxa de câmbio que é escrita no contrato. Como não é possível formalizar uma taxa de câmbio no intradiário, os swaps saem com taxa de câmbio do dia anterior. Para que o custo do dinheiro seja refletido

---

no contrato, a taxa de juros em USD deve ser relacionada tanto à taxa de cupom quanto à taxa de câmbio do exato momento da operação. Essa taxa de cupom do exato momento é o cupom limpo, ou o real custo do dinheiro em USD. O cupom sujo existe para refletir em contrato essa tecnicalidade. Em outras palavras, a taxa de cupom sujo aplicada sobre os fluxos calculados com a taxa de câmbio do dia útil anterior é igual à taxa de cupom limpo sobre o fluxo calculado utilizando a taxa de câmbio do momento da operação.



P T A X V_(- 1)/S ₀ = (1 + C _S d c/3 6 0)/(1 + C _L d c/3 6 0) tag {14.9}



Ou



1 + C _S d c/3 6 0/S ₀/P T A X V_(- 1) = 1 + C _L d c/3 6 0 tag {14.10}



Substituindo:



2 , 3 0/2 , 2 6 2 1 = (1 + C _s 4 5 2/3 6 0)/(1 + 1 , 4 5 \% 4 5 2/3 6 0)



Cupom sujo = 2.81% a. a.

## 14.2.10 Exemplo: cálculo de um swap IPCA x Pré

Um fundo de pensão tem em sua carteira uma NTN-B principal 2024, que rende variação do IPCA mais um cupom de 6,60% a. a. Apesar de poder marcar esse título na curva, o gestor do fundo decidiu transferir a rentabilidade para CDI fazendo um swap com você.

Dados:

- Prazo: 2.607 dias úteis
- Cupom de IPCA BM&F: 6,45% a. a.
- Taxa pré B3: 12,90%

Determine:

a) Qual a inflação implícita no mercado de IPCA?
b) Qual o percentual do CDI do swap para hedgear a NTN-B do fundo de pensão?

---

c) Mostre a NTN-B e o swap no balanço do cliente.

## Solução

a) A equação de arbitragem entre juro nominal e juro real é:



(1 + i)^(du/252) = E_t (IPCA_(du))/IPCA_0 (1 + C_(IPCA))^(du/252)



Podemos resumir o termo de expectativa de IPCA(t)/IPCA(0) como uma inflação esperada média anual:



E (IPCA_(du))/IPCA_t = (1 + pi_e)^(du/252)



Substituindo na equação do swap:



(1 + i)^(du/252) = (1 + pi_e)^(du/252) × (1 + C_(IPCA))^(du/252)



Como os expoentes podem ser eliminados, a inflação implícita anual esperada será:



pi_e = (1 + i)^(du/252)/(1 + C_(IPCA))^(du/252) - 1





pi_e = (1 + 12,90\%)^(du/252)/(1 + 6,45\%)^(du/252) - 1 = 6,06\%  a.a.



b) Vamos calcular a taxa pré-equivalente à remuneração da NTN-B, uma vez que a inflação implícita é igual para a BM&F e para o mercado de NTN-Bs.



(1 + i)^(du/252) = (1 + 6,06\%)^(du/252) × (1 + 6,60\%)^(du/252)



Que dá uma taxa nominal pré de 13,06\% a. a., correspondendo a 101,16\% do CDI. Sempre lembrando que não estamos considerando o lucro do banco na definição do swap.

c)

|  Balanço do cliente  |   |
| --- | --- |
|  NTN-B | IPCA + 6,60%  |
|  Swap | 101,16% do DI  |

---

14.3 O swap libor x fixed

Aproveitamos este capítulo para apresentar uma modalidade de swap muito negociada internacionalmente. O foco deste livro é renda fixa nacional, porém optamos por mostrar o swap de Libor por ser extremamente importante, inclusive para as mesas de derivativos de taxas de juros no Brasil.

Para escrever este capítulo, utilizamos a literatura internacional sobre o assunto, Hull e Fabozzi e Mann, assim como a recente literatura nacional, Molero e Mello, que aborda os impactos neste swap pós-crise de 2007.

Para deixar os exemplos deste livro mais aderentes às práticas de mercado internacional, utilizamos dados reais extraídos do terminal Bloomberg.

14.3.1 As taxas Libor

A taxa London InterBank Offered Rate (Libor) é uma taxa média de juros contra a qual bancos estão dispostos a emprestar uns aos outros no mercado de internacional. É uma taxa referencial para transações internacionais. Fazendo uma anologia com o Brasil, a taxa Libor seria a taxa DI do mercado internacional.

Até a crise de crédito de 2007, a Libor era aceita como uma proxy da taxa de juros livre de risco. Como veremos adiante, a realidade mostrou que, sob determinadas condições de mercado, a Libor não é uma boa proxy da taxa de juros livre de risco, impactando profundamente a precificação de alguns derivativos.

14.3.2 O futuro de eurodólar

Para entendermos o mercado formador de taxas de swaps é necessário abordar o mercado futuro de eurodólar, ou, em inglês, Eurodollar Futures. Este mercado auxilia na formação de preço dos swaps de Libor para prazos mais longos que um ano, sendo um benchmark para os investidores em âmbito global e uma ferramenta para fazer o hedge das flutuações de taxas de juros de curto prazo em dólares norte-americanos.

O preço de ajuste final para os futuros de eurodólar é determinado pela taxa interbancária de três meses da Libor. Os eurodólares são dólares norte-americanos depositados em bancos comerciais fora dos Estados Unidos. Os

---

preços do mercado futuro de eurodólar refletem as expectativas de taxas de juros forward de três meses referentes aos depósitos de eurodólar para datas específicas no futuro.

## 14.3.3 Precificação de um swap de Libor

Para precificar um swap de Libor é necessário entender seus fluxos de caixa. Normalmente, observa-se fluxos trimestrais ou semestrais, sendo que a periodicidade de pagamentos de cada ponta do swap pode, ou não, ser a mesma.

A Libor do primeiro fluxo de caixa é fixada no início do swap. Na verdade, a convenção para swaps de Libor *plain vanilla* é que a taxa Libor é (re)definida no início do período de pagamento daquele fluxo de caixa, também chamadas de datas de reset. Ou seja, a taxa Libor do fluxo de caixa de t = 1 é definida em t = 0 e assim por diante. A figura a seguir exemplifica os possíveis fluxos de caixa de um swap Libor vs Fixed:

Figura 14.1 – Resumo do procedimento de cálculo dos fluxos indexados à Libor
![img-31.jpeg](img-31.jpeg)
![img-32.jpeg](img-32.jpeg)
Fonte: Elaborada pelos autores.

Optamos por mostrar os fluxos das pontas do swap como se fossem de títulos que pagam cupom intermediários. Notemos que o valor do último fluxo de caixa é maior, pois representa o pagamento do cupom de juros mais o principal.

Podemos calcular os fluxos de caixa da ponta Libor pelo seguinte procedimento:

1. Calcular a projeção dos valores de cada um dos fluxos de caixa da ponta Libor por meio das taxas Libor cotadas para os respectivos prazos. Aqui, é útil calcular o fator de capitalização de cada período;
2. Acumular os fatores de capitalização;

---

3. Depois, basta calcular o fator de desconto para trazer os fluxos de caixa ao valor presente.

Podemos resumir o procedimento pela figura a seguir:

Figura 14.2 – Resumo do procedimento de cálculo dos fluxos indexados à Libor
![img-33.jpeg](img-33.jpeg)
Fonte: Elaborada pelos autores.

Para calcular os fluxos de caixa da ponta prefixada, assumindo um swap sem spread, partimos de que o valor do swap no seu início tem de ser igual a zero. Ou seja, a soma dos valores presentes dos fluxos de caixa da ponta prefixada tem de ser igual, em módulo, aos da ponta Libor. Portanto, a taxa prefixada é obtida a partir da soma dos valores presentes dos fluxos de caixa da ponta Libor.

## 14.3.4 Exemplo: precificação de swap de Libor

O swap de Libor é cotado pela taxa da ponta prefixada. Mostraremos um exemplo de como calcular o preço, ou a taxa, de um swap a partir dos dados da tela da Bloomberg a seguir:

Figura 14.3 – Exemplo de precificação de um swap fixed vs Libor

---

![img-34.jpeg](img-34.jpeg)
Fonte: Bloomberg, 2017.

Podemos observar que a ponta prefixada, fixed, desse swap paga cupom de juros semestrais, e a ponta Libor, floating, paga cupom de juros trimestrais. Definimos o valor do nocional do swap em USD 10 milhões.

É importante atentar para o critério de contagem de dias para cada ponta: na ponta prefixada, a parametrização definida neste exemplo foi 30I/360. Esse critério define que cada mês tem trinta dias corridos. Já na ponta Libor, definimos o critério ACT/360 ou actual/360, que leva em consideração os dias corridos de fato no mês. É importante verificar as convenções de contagem de dias ao cotar um swap de Libor. Nesse exemplo, optamos por explorar duas das contagens de dias possíveis.

Na Figura 14.3 vemos que o terminal já calculou a taxa da ponta fixed ou prefixada – é a taxa do campo “Coupon”: 1,9389%. Como foi feito esse cálculo? É o que mostraremos nesta seção.

Podemos observar na figura a seguir que o terminal Bloomberg mostra as taxas Libor usadas nos trimestres, ou períodos de reset, neste exemplo.

Figura 14.4 – Exemplo de taxas Libor nas datas de Reset do swap

---

![img-35.jpeg](img-35.jpeg)
Fonte: Bloomberg, 2017.

O sistema também mostra o cronograma de fluxos de caixa de ambas as pontas do swap:

Figura 14.5 – Exemplo de cronograma dos fluxos de caixa do swap fixed vs Libor
![img-36.jpeg](img-36.jpeg)
Fonte: Bloomberg, 2017.

Agora, temos todas as informações para mostrarmos como o swap foi precificado.

Tabela 14.1 – Cálculo dos fatores de capitalização e de desconto

|  Data do fluxo de caixa | Dias corridos 301/ 360 | Dias corridos no trimestre Actual/ 360 | Libor (3 meses) | (Passo 1) Fator de capitalização no período | (Passo 2) Fator de capitalização acumulado | (Passo 3) Fator de desconto spot  |
| --- | --- | --- | --- | --- | --- | --- |
|  24-Jan.-18 | 90 | 92 | 1,36250% | 1,36250% | 1,003482 | 0,996530  |
|  24-Apr.-18 | 90 | 90 | 1,60267% | 1,004007 | 1,007503 | 0,992553  |
|  24-Jul.-18 | 90 | 91 | 1,69391% | 1,004282 | 1,011817 | 0,988321  |
|  24-Oct.-18 | 90 | 92 | 1,79704% | 1,004592 | 1,016463 | 0,983803  |

---

|  Data do fluxo de caixa | Dias corridos 30I/ 360 | Dias corridos no trimestre Actual/ 360 | Libor (3 meses) | (Passo 1) Fator de capitalização no período | (Passo 2) Fator de capitalização acumulado | (Passo 3) Fator de desconto spot  |
| --- | --- | --- | --- | --- | --- | --- |
|  24-Jan.-19 | 90 | 92 | 1,88382% | 1,004814 | 1,021357 | 0,979090  |
|  24-Apr.-19 | 90 | 90 | 1,96606% | 1,004915 | 1,026377 | 0,974301  |
|  24-Jul.-19 | 90 | 91 | 1,99677% | 1,005047 | 1,031557 | 0,969408  |
|  24-Oct.-19 | 90 | 92 | 2,00042% | 1,005112 | 1,036831 | 0,964477  |
|  24-Jan.-20 | 90 | 92 | 2,06511% | 1,005278 | 1,042303 | 0,959414  |
|  24-Apr.-20 | 90 | 91 | 2,12366% | 1,005368 | 1,047898 | 0,954291  |
|  24-Jul.-20 | 90 | 91 | 2,18096% | 1,005513 | 1,053675 | 0,949059  |
|  26-Oct.-18 | 92 | 94 | 2,23839% | 1,005845 | 1,059833 | 0,943545  |

Fonte: Elaborada pelos autores.

Os dias corridos e as taxas Libor de três meses são fornecidos pelo sistema Bloomberg, sendo variáveis de entrada nos nossos cálculos.

Nesta primeira parte da tabela, podemos calcular as três últimas colunas conforme as fórmulas a seguir.

Calculamos, então, o fator de capitalização dos períodos pela fórmula:



F a t C _t = I _t d c_(t - 1 , t)/3 6 0 + 1 tag {14.11}



Sendo Iₙ a libor do período entre t - 1 e t.

De posse dos fatores de capitalização dos períodos, calculamos os fatores de capitalização acumulados nos prazos:



F a t C_(A c u m u l a d o e m) · j^(prime) = prod_(t = 1) ^j F a t_(1, j) tag {14.12}



No nosso exemplo, o fator será acumulado até o 12.º período, pois temos 12 trimestres.

Com os fatores de capitalização acumulados, podemos calcular os fatores de desconto ou discount factors, conforme a seguir:



F a t D _j = 1/F a t C_(1 , j) tag {14.13}



Agora, podemos calcular o resto da tabela, calculando os valores presentes dos fluxos de caixa:

Tabela 14.2 – Cálculo dos fluxos de caixa e seus Valores Presentes

---

|  Fluxo de caixa pré (recebe) | Fluxo de caixa Libor (paga) | Valor Presente do fluxo prefixado | Valor Presente do fluxo Libor | NPV  |
| --- | --- | --- | --- | --- |
|  0 | -34,819 | 0 | -34,699 | -34,699  |
|  96,945 | -40,067 | 96,223 | -39,768 | 56,455  |
|  0 | -42,818 | 0 | -42,318 | -42,318  |
|  96,945 | -45,924 | 95,375 | -45,181 | 50,194  |
|  0 | -48,142 | 0 | -47,135 | -47,135  |
|  96,945 | -49,152 | 94,454 | -47,888 | 46,565  |
|  0 | -50,474 | 0 | -48,930 | -48,930  |
|  96,945 | -51,122 | 93,501 | -49,306 | 44,195  |
|  0 | -52,775 | 0 | -50,633 | -50,633  |
|  96,945 | -53,681 | 92,514 | -51,228 | 41,286  |
|  0 | -55,130 | 0 | -52,321 | -52,321  |
|  0 | -34,819 | 0 | -34,699 | -34,699  |
|  96,945 | -40,067 | 96,223 | -39,768 | 56,455  |
|  0 | -42,818 | 0 | -42,318 | -42,318  |
|  96,945 | -45,924 | 95,375 | -45,181 | 50,194  |
|  0 | -48,142 | 0 | -47,135 | -47,135  |
|  96,945 | -49,152 | 94,454 | -47,888 | 46,565  |
|  0 | -50,474 | 0 | -48,930 | -48,930  |
|  96,945 | -51,122 | 93,501 | -49,306 | 44,195  |
|  0 | -52,775 | 0 | -50,633 | -50,633  |
|  96,945 | -53,681 | 92,514 | -51,228 | 41,286  |
|  0 | -55,130 | 0 | -52,321 | -52,321  |
|  10,098,022 | -10,058,447 | 9,527,934 | -9,490,592 | 37,341  |
|   |  | Σ = 10,000,000 | Σ = -10,000,000 | Σ = 0  |

Fonte: Elaborada pelos autores.

Os fluxos de caixa prefixados foram calculados pela seguinte fórmula:



Fluxo Caixa Prét = Notional × pré × dc_(t-1,t)/360 



Sendo que no último fluxo T devemos considerar como se houvesse um pagamento de juros mais o principal:



Fluxo Caixa Prét = Notional + Notional × pré × dc_(T-1,T)/360 



Os fluxos de caixa indexados à Libor foram calculados conforme a equação a seguir:

---



F l u x o C a i x a L i b o r _t = N o t i o n a l × (F a t C _t - 1) tag {14.16}



Sendo que no último fluxo T devemos considerar como se houvesse um pagamento de juros mais o principal:



F l u x o C a i x a L i b o r _T = N o t i o n a l × F a t C _T tag {14.17}



Os valores presentes de ambos os fluxos foram calculados pela equação a seguir:



V P [ F l u x o C a i x a _t ] = F l u x o C a i x a _t × F a t D _t tag {14.18}



Para calcular o net present value (NPV), basta somar os valores presentes dos fluxos de caixa prefixados e indexados à Libor.

Vimos que a taxa calculada da taxa da ponta fixed é 1,9389% ("Coupon"). E como chegamos a esta cotação? No MS Excel, chegaríamos a essa taxa por meio da ferramenta "atingir meta", fazendo com que o NPV do swap seja zero.

## 14.3.5 O swap de Libor depois da crise de crédito de 2007/2008

Conforme mencionamos, a taxa Libor, além de popular indexadora de uma das pontas dos swaps de taxas de juros internacionais, interest rate swaps, era considerada uma taxa muito próxima de ser a livre de risco, sendo usada para calcular os valores presentes dos fluxos de caixa do swap. A figura a seguir mostra que essa premissa foi abalada durante a crise de 2007 e 2008:

Figura 14.6 – Libor-OIS Spread

---

![img-37.jpeg](img-37.jpeg)
Fonte: Bloomberg, 2017.

OIS é a sigla para overnight indexed swap, que é um indexador representado por uma taxa de juros computada diariamente. Nos Estados Unidos, é a effective Fed funds rate, equivalente à taxa DI overnight no Brasil.

O spread Libor-OIS é um indicador do risco de crédito e liquidez no setor bancário e é calculado em basis points, indicado no eixo "y" da figura anterior. Durante a crise, os bancos hesitaram em emprestar uns aos outros, ou seja, assumiu-se um risco de crédito entre os bancos até então inexistente, ou pelo menos não observados naquelas magnitudes.

A curva de juros da OIS passou a ser o padrão de mercado na precificação de derivativos, incluindo os swaps. Esta é a curva que as clearings usam para marcar a mercado os swaps e definirem as margens e garantias exigidas. Após o Dodd-Frank Act, em 2010, passou a ser padrão o registro de swaps em clearings e na modalidade "com garantia" (collateralized).

E o que mudou na precificação do swap de Libor? A curva spot usada para trazer os valores presentes dos fluxos de caixa de ambas as pontas do swap deixou de ser a curva spot de Libor. A curva spot para a marcação a mercado passou a ser uma curva de taxas OIS.

Vamos analisar o swap que vimos anteriormente. A tela a seguir mostra a opção na Bloomberg para precificar aquele mesmo swap, só que utilizando a curva OIS para marcar a mercado:

---

Figura 14.7 – Exemplo de precificação de um swap fixed vs Libor (collateralized)
![img-38.jpeg](img-38.jpeg)
Fonte: Bloomberg, 2017.

Podemos observar que os valores dos fluxos de caixa permanecem os mesmos do exemplo anterior:

Figura 14.8 – Exemplo de cronograma dos fluxos de caixa do swap fixed vs Libor (collateralized)
![img-39.jpeg](img-39.jpeg)
Fonte: Bloomberg, 2017.

Observamos, porém, que os valores presentes mudaram: estão maiores em relação aos calculados anteriormente. Qual o motivo? Ora, mencionamos que essa modalidade de swap com garantia utiliza uma curva de taxas OIS em vez de uma curva Libor spot para trazer os fluxos de caixa aos valores presentes. Como as taxas OIS são mais próximas da taxa livre de risco, ela é

---

menor ou igual à taxa Libor. Portanto, os valores dos fluxos de caixa são maiores.

Até aqui, vimos como o mercado se adequou após constatar que a taxa Libor não é uma boa proxy para a taxa livre de risco. O mercado passou a utilizar as taxas OIS como sendo as apropriadas para as taxas livres de risco. De acordo com o artigo de Hull e White, “LIBOR vs. OIS: The Derivatives Discounting Dilemma”, o racional utilizado pelo mercado para o uso das taxas OIS como proxy da taxa livre de risco para os derivativos com garantia, collateralized, é que o derivativo lastreado pela garantia, que tem um rendimento próximo da effective funds rate. Para derivativos sem garantia, ainda se assume a taxa Libor como sendo a taxa para calcular os fatores de desconto desses derivativos. Em seu estudo, Hull e White argumentam que a taxa OIS deveria ser usada como a proxy da taxa livre de risco em todas as situações, seja o derivativo com ou sem garantia.

|  Resumo  |
| --- |
|  Este capítulo mostra um mercado importante de derivativo de balcão, os swaps. Apresentamos os principais swaps de renda fixa do mercado brasileiro, assim como o swap de Libor.  |

34 O cupom de IPCA aqui é o jargão de mercado para o juro real de mercado vigente nesse momento.

---

# Capítulo 15
Bootstrapping

## 15.1 Definição

Bootstrapping é o procedimento que permite obter uma curva de juros spot a partir de instrumentos financeiros que contêm pagamentos de juros periódicos. Como vimos anteriormente, esses instrumentos financeiros são cotados por uma TIR ou YTM:



P_(NTN-F) = Σ(k=1 até n) FC_k/(1 + y)^(dn/252)



Verificamos na fórmula anterior que y é a TIR do papel, ou seja, é a mesma taxa de desconto usada para trazer ao valor presente todos os fluxos de caixa. Não podemos assumir que as taxas spots sejam iguais nos prazos de k = 1 à n.

## 15.2 Motivação para o uso do bootstrapping

Você, leitor, pode estar se perguntando em quais situações precisaríamos de uma curva spot se já temos as TIRs desses instrumentos que pagam juros intermediários. Em outras palavras, esse procedimento do bootstrapping é utilizado, na prática? Aqui mostraremos uma aplicação do bootstrapping adaptada ao mercado brasileiro, considerando suas peculiaridades e utilizando dados reais do nosso mercado.

Suponhamos que você tenha uma carteira que contém diversos tipos de instrumentos financeiros de renda fixa. Esses instrumentos financeiros podem ser resumidos pelas projeções dos seus fluxos de caixa. Sabemos que precisamos precificar ou marcar a mercado esses fluxos de caixa, trazendo-os ao seu valor presente de acordo com a taxa de juros apropriada vigente no mercado para aquele prazo.

Vamos assumir, ainda, que um desses fluxos da sua carteira é referente à ponta de um swap com pagamento final indexada ao IPCA mais um cupom de IPCA, definido contratualmente no swap. Podemos marcar a mercado

---

esse fluxo de caixa por uma taxa do tipo TIR observada no mercado secundário das NTN-Bs? Isso só seria correto se a curva spot de cupom de IPCA fosse flat, ou seja, se as taxas spot fossem iguais ao longo dos prazos. Como isso não é realista, é necessário obter uma curva spot de cupom de IPCA. Suponhamos que o único instrumento financeiro indexado ao IPCA que tenha liquidez sejam as NTN-Bs. Logo, precisamos gerar uma curva spot de cupom de IPCA a partir das TIRs desses títulos para marcar a mercado a ponta do nosso swap indexada ao IPCA. Eis aqui uma razão real para utilizarmos o bootstrapping.

## 15.3 O procedimento do bootstrapping

Neste momento, para facilitar o entendimento da mecânica do bootstrapping, vamos supor que tenhamos as seguintes NTN-Fs disponíveis no mercado secundário, e que desejamos gerar uma curva spot a partir das TIRs de mercado destes papéis³⁵, ou seja, preencher a coluna de taxas spot da tabela a seguir.

Tabela 15.1 – Cronograma de vencimentos de NTN-Fs fictícias

|  NTN-F | Valor de mercado | Prazo (em anos) | TIR (yield) | Taxa spot  |
| --- | --- | --- | --- | --- |
|  a | 1.023,53 | 0,5 | 5,00% | i₀,₅ =?  |
|  b | 1.036,85 | 1,0 | 6,00% | i₁,₀ =?  |
|  c | 1.040,39 | 1,5 | 7,00% | i₁,₅ =?  |

Fonte: Elaborada pelos autores.

Graficamente, temos:

Figura 15.1 – Cronograma dos fluxos de caixa das NTN-Fs fictícias
![img-40.jpeg](img-40.jpeg)
Fonte: Elaborada pelos autores.

Em relação às informações do título “a”, podemos verificar que, como o seu prazo é de 0,5 ano, só existe um fluxo de caixa remanescente deste papel. Assim, podemos concluir que a sua TIR, definida pelo mercado em 5,00% a. a. é, também, uma taxa spot, pois diz respeito à taxa de desconto de um

---

único fluxo de caixa.

Então, conseguimos encontrar a primeira taxa spot da tabela:

Tabela 15.2 – Taxa spot (Prazo = 0,5 ano)

|  NTN-F | Valor de mercado | Prazo (em anos) | TIR (yield) | Taxa spot  |
| --- | --- | --- | --- | --- |
|  a | 1.023,53 | 0,5 | 5,00% | 5,00%  |
|  b | 1.036,85 | 1,0 | 6,00% | i_(1,0) =?  |
|  c | 1.040,39 | 1,5 | 7,00% | i_(1,5) =?  |

Fonte: Elaborada pelos autores.

E agora, como obter a taxa spot para o prazo de um ano? Como o vencimento do primeiro cupom do título “b” é igual ao vencimento do título “a”, e como temos a taxa spot do fluxo de caixa do título “a”, vamos descontar o primeiro fluxo de caixa do título “b” pela taxa spot, 5% neste prazo de 0,5 ano:

Figura 15.2 – Encadeamento das NTN-Fs fictícias “a” e “b”
![img-41.jpeg](img-41.jpeg)
Fonte: Elaborada pelos autores.

Mas como encontrar a taxa spot do segundo fluxo de caixa do título “b”? Por não arbitragem: o preço do título “b”, R$ 1.036,85, deve ser o mesmo, tanto descontando os seus fluxos pela TIR quanto pelas taxas spot dos respectivos prazos:



P_(NTN-F) = Σ(k=1 até n) FC_k/(1 + y)^(1/2) = Σ(k=1 até n) FC_k/(1 + i_k)^(1/2)



Lembrando que na fórmula anterior, i_k é a taxa spot do prazo do k-ésimo fluxo de caixa.

Então, para calcular a taxa spot para o prazo de um ano, basta resolver a equação anterior:

---



1.036,85 = 48,80885/(1 + 5\%)^(0,5) + 1.048,80885/(1 + i_1)^1



Logo, i_1 = 6,02\%:

Figura 15.3 – Taxa spot (prazo = 1 ano)
![img-42.jpeg](img-42.jpeg)
Fonte: Elaborada pelos autores.

E a nossa tabela atualizada:

Tabela 15.3 – Taxa spot (prazo = 1 ano)

|  NTN-F | Valor de mercado | Prazo (em anos) | TIR (yield) | Taxa spot  |
| --- | --- | --- | --- | --- |
|  a | 1.023,53 | 0,5 | 5,00% | 5,00%  |
|  b | 1.036,85 | 1,0 | 6,00% | 6,02%  |
|  c | 1.040,39 | 1,5 | 7,00% | i_(1,5) =?  |

Fonte: Elaborada pelos autores.

Agora, precisamos calcular a taxa spot para o prazo de 1,5 ano. O procedimento é o mesmo que utilizamos para calcular a taxa spot i_1. Então, tudo o que precisamos é encontrar a taxa de desconto do terceiro fluxo de caixa do título "c", o i_(1,5):

Figura 15.4 – Taxas spot da NTN-F "c"
![img-43.jpeg](img-43.jpeg)
Fonte: Elaborada pelos autores.

Então, para calcular a taxa spot para o prazo de 1,5 ano, basta resolver a seguinte equação:



1.040,39 = 48,80885/(1 + 5\%)^(0,5) + 48,80885/(1 + 6,02\%)^1 + 1.048,80885/(1 + i_(1,5))^(1,5)



---

Logo,
i_(1,5) = 7,07
:

Figura 15.5 – Taxa spot (prazo = 1,5 ano)
![img-44.jpeg](img-44.jpeg)
Fonte: Elaborada pelos autores.

E, assim, completamos a nossa tabela com taxas spot a partir de instrumentos cotados por TIRs:

Tabela 15.4 – Taxa spot (prazo = 1,5 ano)

|  NTN-F | Valor de mercado | Prazo (em anos) | TIR (yield) | Taxa spot  |
| --- | --- | --- | --- | --- |
|  a | 1.023,53 | 0,5 | 5,00% | 5,00%  |
|  b | 1.036,85 | 1,0 | 6,00% | 6,02%  |
|  c | 1.040,39 | 1,5 | 7,00% | 7,07%  |

Fonte: Elaborada pelos autores.

O exemplo anterior é importante para entendermos a mecânica do bootstrapping. É um exemplo simplificado, muito parecido com os que vimos em livros de renda fixa norte-americanos. No Brasil, para obter uma curva spot a partir de instrumentos que são cotados por TIRs são necessários alguns procedimentos adicionais. É o que veremos a seguir.

# 15.4 Implementação do bootstrapping na prática

Agora, mostraremos como montar uma curva spot de cupom de IPCA a partir das NTN-Bs reais cotadas no mercado secundário utilizando o bootstrapping.

Vamos assumir que estamos no dia 27/7/2018 e observamos as seguintes informações no site da Anbima para as NTN-Bs negociadas no mercado secundário:

Figura 15.6 – Taxa do mercado secundário das NTN-Bs em 27/7/2018

---

ANBIMA

Mercado Secundário do Módulo Problema

|  ANBIMA |   |   |   |   |   |   |   |   | 15/10/2008  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Panel IPCA |   |   |   |   |   |   |   |   | NTN-B - Teste 2% p.a. (131)  |
|  Código OPLIC | Data Elasn/Emissão | Data da Vencimento | Ex. Compra | Ex. Venda | Ex. Indicalismo | etc | Informato Indicativo  |   |   |
|   |   |   |   |   |   |   |  Máximo (04) | Máximo (04) | Máximo (04+1)  |
|  780195 | 15/07/2008 | 15/08/2018 | 3,6596 | 2,45861 | 3,5128 | 0,314,812699 | 2,4460 | 5,2732 | 5,1390  |
|  780195 | 15/07/2008 | 15/05/2018 | 3,3563 | 2,10941 | 3,3080 | 0,155,417803 | 2,4079 | 5,7720 | 5,6500  |
|  780195 | 15/07/2008 | 15/08/2020 | 4,1516 | 3,12801 | 4,1490 | 0,102,614168 | 2,8420 | 5,8320 | 5,8020  |
|  780195 | 15/07/2008 | 15/06/2021 | 4,4812 | 3,45861 | 4,4090 | 0,386,834430 | 4,1925 | 5,5902 | 4,1222  |
|  780195 | 15/07/2008 | 15/06/2022 | 5,1220 | 3,1000 | 5,1100 | 0,311,303600 | 4,8618 | 5,6502 | 4,8210  |
|  780195 | 15/07/2008 | 15/03/2023 | ... | ... | 5,2830 | 0,287,279944 | 5,0194 | 5,7149 | 5,0031  |
|  780195 | 15/07/2008 | 15/03/2023 | 5,2898 | 3,36791 | 5,3659 | 0,266,149931 | 5,0231 | 5,7500 | 5,0000  |
|  780195 | 15/07/2008 | 15/08/2024 | 5,5196 | 3,3891 | 5,3000 | 0,325,416672 | 5,0671 | 5,7129 | 5,0337  |
|  780195 | 15/07/2008 | 15/08/2026 | 5,4988 | 3,4694 | 5,4692 | 0,319,542560 | 5,3674 | 5,8507 | 5,3240  |
|  780195 | 15/07/2008 | 15/08/2028 | 5,5397 | 3,35961 | 5,5230 | 0,326,699640 | 5,3333 | 5,8447 | 5,3542  |
|  780195 | 15/07/2008 | 15/08/2030 | 5,6411 | 3,3032 | 5,6222 | 0,316,845271 | 5,4708 | 5,9238 | 5,4302  |
|  780195 | 15/07/2008 | 15/05/2035 | 5,6818 | 3,3471 | 5,6672 | 0,381,117772 | 5,5143 | 5,9190 | 5,4873  |
|  780195 | 15/07/2008 | 15/06/2040 | 5,6940 | 3,44391 | 5,6690 | 0,344,433061 | 5,5130 | 5,9939 | 5,4920  |
|  780195 | 15/07/2008 | 15/05/2045 | 5,7521 | 3,7113 | 5,7286 | 0,286,448000 | 5,5686 | 5,9517 | 5,5632  |
|  780195 | 15/07/2008 | 15/08/2056 | 5,7426 | 3,7147 | 5,7282 | 0,341,273790 | 5,5656 | 5,8427 | 5,5542  |
|  780195 | 15/07/2008 | 15/05/2050 | 5,7496 | 3,7563 | 5,7281 | 0,301,793527 | 5,5607 | 5,9410 | 5,5549  |

Fonte: Anbima.

Para entendermos a mecânica do bootstrapping neste caso real, basta focarmos somente nas três primeiras NTN-Bs. Podemos resumir os dados da Anbima conforme a tabela a seguir, ordenada pelos vencimentos dos títulos:

Tabela 15.5 – Cronograma de vencimentos das NTN-Bs no mercado secundário

|  NTN-Bs mercado secundário  |   |   |
| --- | --- | --- |
|  Vencimento | Dias úteis | TIR  |
|  15/8/2018 | 13 | 3,5128%  |
|  15/5/2019 | 198 | 3,2000%  |
|  15/8/2020 | 516 | 4,1400%  |
|  ... | ... | ...  |

Fonte: Elaborada pelos autores.

Ao montarmos os fluxos de caixa das NTN-Bs, constatamos uma barreira para implementar o bootstrapping. As datas de vencimentos dos fluxos de caixa das NTN-Bs nem sempre são coincidentes.

O documento “Metodologia para a apuração de curvas de preços e de spreads teóricos de títulos públicos”, elaborado em 2004, pelo Departamento Técnico e de Desenvolvimento de Produtos da então BM&FBovespa aborda esse problema:

Uma exigência do modelo [bootstrapping] a ser aplicado é que para toda data de pagamento de cupom de um título sempre exista o resgate de um título com características semelhantes.

---

Este processo é conhecido como encadeamento [...] a emissão de títulos públicos no Brasil não apresenta um intervalo de datas com a regularidade que permita a aplicação imediata do modelo [bootstrapping] (BM&FBOVESPA, 2004).

Vamos montar os fluxos de caixa das duas primeiras NTN-Bs para ilustrar a questão do encadeamento dos fluxos:

Figura 15.7 – (A falta de) Encadeamento dos títulos no Brasil
![img-45.jpeg](img-45.jpeg)
Fonte: Elaborada pelos autores.

Partindo da NTN-B de vencimento 15/8/2018, observamos que primeiro fluxo de caixa da próxima NTN-B, a de 15/5/2019, não apresenta o encadeamento necessário para a aplicação direta do bootstrap.

Como resolver esse problema? A solução descrita no documento da BM&F referido anteriormente é por meio da criação de títulos virtuais. Se partirmos da NTN-B de vencimento em 15/8/2018 para fazer o bootstrap precisaríamos de uma NTN-B de vencimento em 15/2/2019:

Figura 15.8 – O encadeamento por meio da criação de um título virtual
![img-46.jpeg](img-46.jpeg)
Fonte: Elaborada pelos autores.

Só que essa NTN-B vencendo em 15/2/2019 não existe. O que fazer? Ora, vamos criá-la! É o que chamamos de títulos virtuais. E como fazer isso?

---

Bem, temos as TIRs da NTN-B 15/8/2018 e da NTN-B 15/5/2019. Como a NTN-B virtual 15/2/2019 vence entre estas duas NTN-Bs, podemos interpolar as TIRs pelo método flat forward exponential para calcular a TIR da NTN-B virtual 15/2/2019. Uma vez encontrada a TIR da NTN-B virtual, basta calcular o seu preço como se fosse qualquer NTN-B, da mesma forma que mostramos no Capítulo 6. O prazo da NTN-B 15/2/2019 é de 139 dias úteis. Então, calculamos a sua TIR pela interpolação flat forward:



T I R_(N T N B 1 5 / 0 2 / 2 0 1 9) = {(1 + 3, 5 1 2 8 \% )^(1 3) /_(2 5 2) × [ (1 + 3 , 2 0 0 0 \% )^(1 9 8) /_(2 5 2)/(1 + 3 , 5 1 2 8 \% )^(1 3) /_(2 5 2) ]^(1 3 9 - 1 3/1 9 8 - 1 3) }^(2 5 2/1 3 9) - 1



Logo:



T I R_(N T N B 1 5 / 0 2 / 2 0 1 9) = 3, 2 0 9 3 \% a. a.



Graficamente, temos que³⁶:

Figura 15.9 – Precificando o título virtual
![img-47.jpeg](img-47.jpeg)
Fonte: Elaborada pelos autores.

Uma vez devidamente encadeados os dois títulos, podemos prosseguir com o bootstrapping propriamente dito.

Graficamente, temos:

Figura 15.10 – Isolando a taxa spot i_1

---

![img-48.jpeg](img-48.jpeg)
Fonte: Elaborada pelos autores.

Sendo que i_0 e i_1 representam as taxas spot. Aplicando a técnica já vista no início deste capítulo, conseguimos calcular a taxa spot do cupom de IPCA para 139 dias úteis, o i_1. Para isso, é bom lembrarmos da fórmula genérica de precificação das NTN-Bs:



P_(NTN-B) = IPCA_0/IPCA_0 Σ(k=1 até n) FC_k/(1 + i_k)^(du_k)/252



Sendo que a variação do IPCA de acumulado de 15/7/2000^(37) até “hoje”, 27/7/2018 no nosso exemplo, nada mais é do que a variação percentual projetada do IPCA para “hoje”. O valor nominal projetado para as NTN-Bs em 27/7/2018 é dado pela Anbima, R$ 3.128,070660:

Figura 15.11 – VNA projetado das NTN-Bs em 27/7/2018
![img-49.jpeg](img-49.jpeg)
Fonte: Anbima.

Portanto, o IPCA acumulado projetado até “hoje” é 312.807066%. Aplicando a fórmula genérica de precificação da NTN-B no nosso exemplo, temos:



3.257,241209 = 3,12807066 × [ 1.000(1,06^(0.5) - 1)/(1 + 3,5128\%)^(13)/252} + 1.000(1,06^(0.5))/(1 + i_1)^(139)/252} ]



Resolvendo a equação anterior, temos que i_1 = 3,2083\%. Graficamente:

Figura 15.12 – Calculando a taxa spot i_1

---

![img-50.jpeg](img-50.jpeg)
Fonte: Elaborada pelos autores.

O procedimento é o mesmo para encontrar as outras taxas spot dos cupons de IPCA.

Podemos resumir o procedimento genérico para encontrar taxas spot a partir de instrumentos cotados por TIRs nos seguintes passos:

1. Identificar as datas necessárias de vencimentos dos títulos para o encadeamento.
2. Caso não exista no mercado um título com o encadeamento requerido para fazer o bootstrapping, criar um título virtual. Para encontrar a TIR deste título virtual, basta interpolar as TIRs dos títulos existentes no mercado, sempre considerando como “vértices” os vencimentos dos títulos reais mais próximos do título virtual.
3. Uma vez encontrada a TIR do título virtual, basta calcular o seu preço, como se fosse um título existente no mercado.
4. Agora que temos o encadeamento necessário, basta aplicar o procedimento bootstrapping, observando sempre que o preço do título calculado pela TIR deve ser igual ao preço calculado pelas taxas spots.

Aplicando o procedimento anterior, podemos gerar as primeiras taxas spot de uma curva de cupom de IPCA por meio do bootstrapping:

Tabela 15.6 – Obtendo as taxas spot na prática

|  Dias úteis | NTN-B: real ou virtual? | Passo 1: Vencimento requerido para o encadeamento | Passo 2: TIR | Passo 3: PU NTN-B | Passo 4: taxa spot  |
| --- | --- | --- | --- | --- | --- |
|  13 | Real | 15/8/2018 | 3,5128% | 3.214,812059 | 3,5128%  |
|  139 | Virtual | 15/2/2019 | 3,2093% | 3.257,241209 | 3,2083%  |

---

|  263 | Virtual | 15/8/2019 | 3,5759% | 3.287,599135 | 3,5817%  |
| --- | --- | --- | --- | --- | --- |
|  392 | Virtual | 15/2/2020 | 3,9542% | 3.303,624241 | 3,9699%  |
|  516 | Real | 15/8/2020 | 4,1400% | 3.322,014168 | 4,1606%  |

Fonte: Elaborada pelos autores.

## Resumo

Este capítulo mostra detalhadamente como utilizar a técnica do bootstrapping para obter uma curva de juros do tipo spot a partir de instrumentos que pagam cupom de juros intermediários.

35 No mundo real, não precisaríamos fazer o bootstrapping das NTN-Fs, dado que é possível construir uma curva spot por meio de outros instrumentos que não pagam cupom de juros intermediários, ou seja, que já são cotados por uma taxa spot. Porém, as NTN-Fs são instrumentos muito convenientes para entendermos de forma didática a mecânica do bootstrapping.

36 Caso o leitor replique os cálculos dos preços das NTN-Bs, é possível que haja pequenas diferenças nas casas decimais dos valores que estão expressas no livro, dependendo de como os preços foram arredondados e/ou truncados. Optamos aqui por utilizar as regras de arredondamento definidas pelo Tesouro, uma vez que estamos utilizando exemplos com dados reais da Anbima. Caso você tente replicar o cálculo sem utilizar as regras de “truncamento” e arredondamento do Tesouro, pode esperar pequenas diferenças com os valores demonstrados no livro.

37 O Tesouro Nacional definiu em R$ 1.000,00 o valor nominal das NTN-Bs em 15/7/2000.

---

# Exercícios propostos

1. Calcule as taxas spot dos prazos de 1 e 1,5 ano a partir das NTN-F fictícias a seguir:

|  Título | MtM | Prazo (anos) | TIR | Taxa spot  |
| --- | --- | --- | --- | --- |
|  a | 1.028,44 | 0,5 | 4% |   |
|  b | 1.036,85 | 1,0 | 6% |   |
|  c | 1.026,62 | 1,5 | 8% |   |

2. Assuma a curva spot de taxas de juros e que uma NTN-F está cotada conforme a seguir. Você compraria este título? Justifique sua resposta.

![img-51.jpeg](img-51.jpeg)

---

# Capítulo 16
Imunização e hedge de carteiras de renda fixa

## 16.1 Definição de imunização

Imunizar uma carteira de renda fixa é torná-la invariante em relação a variações na taxa de juros.

Vamos supor que a equação a seguir represente a *duration* modificada não de um título específico, mas de uma carteira de renda fixa, com vários recebimentos e, inclusive, captações e derivativos (contratos futuros de DI e swaps Pré x DI):



D = 1/V d V/d y = - M/(1 + y) tag {16.1}



V, neste caso, é o valor da carteira.

## 16.2 Equação de imunização pela duration

Para que o preço de uma carteira de renda fixa não varie com alterações das taxas de juros, a variação no valor do ativo para uma alteração na curva de juros dos instrumentos que compõem o passivo teria de ser equivalente à variação no valor do passivo para uma alteração na curva de juros dos instrumentos que compõem o passivo:



d V _A = d V _P tag {16.2}



Expandindo a variação no valor do ativo em relação à taxa de juros em primeira ordem pela *duration* modificada, temos:



D _A × V _A × d y _A = D _P × V _P × d y _P tag {16.3}



Onde:

- D: duration modificada (ativa ou passiva)
- V: valor presente da carteira (ativa ou passiva)
- dy: variação aditiva na TIR (ativa ou passiva)

---

A Equação 16.3 é uma forma mais geral de imunização para portfólios de renda fixa. Podemos fazer simplificações.

A primeira, é considerar que a variação paralela na curva de juros é igual para ativo e passivo. Essa alteração torna a equação anterior equivalente a:



D _A × V _A = D _P × V _P tag {16.4}



Ou seja, para imunizar, basta fazer o produto valor x duration modificada iguais no ativo e no passivo.

Sendo assim, a imunização é um hedge de valor presente, em que se busca proteger o valor a mercado do instrumento de oscilações de taxas de juros.

## 16.2.1 Exemplo: hedge por duration

Propor o hedge pelo conceito de duration para 5.000 NTN-Fs com o fluxo a seguir, dada as taxas de juros do mercado NTN-F de cada um dos prazos.

Figura 16.1 – Exemplo: fluxos de caixa da NTN-F
![img-52.jpeg](img-52.jpeg)
Fonte: Elaborada pelos autores.

**Dados ETTJ:**



i_(1 0 0) = 7, 5 \%





i_(2 2 6) = 8, 0 \%





i_(3 5 2) = 8, 5 \%





i_(4 7 8) = 9, 0 \%



**Utilizando:**

a) Um CDB pré vencendo em 478 dias úteis;
b) Um futuro de DI vencendo em 478 dias úteis;
c) Um swap prefixado vencendo em 352 dias úteis;
d) Um CDB prefixado vencendo em 352 dias úteis.

**Solução**

Os dados para resolver esse exercício já foram apresentados anteriormente. Propor o hedge é definir o instrumento, o prazo, o valor, a quantidade etc.

---

Essas características variam conforme o custo (para swaps e CDBs, por exemplo), liquidez, risco de crédito de contraparte (para swaps e CDBs) e condições de mercado em geral.

Para todas as contas, usaremos:



D_A × V_A = D_P × V_P



O sinal da duration modificada de um ativo é negativo, enquanto a de um passivo é positiva, mas o passivo em si é negativo de acordo com a convenção contábil aceita normalmente.

Dessa maneira, vamos fazer os cálculos em módulo para não complicar o raciocínio, tendo o cuidado de posicionar corretamente a exposição dos instrumentos.

a) CDB pré vencendo em 478 dias úteis

Dos exemplos anteriores, temos:



D_A = 1.62





V_A = 1027,15



A duration de Macaulay de um CDB é o seu prazo, dado que esse título não tem cupom de juros. Assim, a duration modificada desse CDB será:



D_P = (478/252)/(1 + 9\%) = 1,74



Aplicando a equação da imunização pela duration, chega-se a:



1,62 × 1027,15 = 1,74 × V_B





V_B = 956,20



Esse é o valor do principal de um CDB Pré vencendo em 478 dias úteis para hedgear 1 NTN-F. Para 5.000 NTN-Fs, o nocional desse swap seria R$ 4.780.993

b) Contratos futuros de DI

Se a opção é a utilização de contratos de DI, o tesoureiro deve buscar aqueles que vencem próximos à duration de Macaulay, de forma a diminuir o risco de base que surge do descasamento de prazos. É um hedge imperfeito e, portanto, deve ser rebalanceado e monitorado constantemente, devido a esse risco de base e ao risco que surge de todas as simplificações usadas no cálculo da duration.

---

Admitindo que haja um futuro de DI vencendo em 478 dias úteis, seu PU será:



P U_(D I) = 1 0 0 . 0 0 0/(1 + i)^(d u/2 5 2) = 1 0 0 . 0 0 0/(1 + 9 \%)^(4 7 8/2 5 2) = 8 4. 9 1 9, 7 0



E a quantidade de contratos será:



q = M t M/P U_(D I) = 4 . 7 8 0 . 9 9 3/8 4 . 9 1 9 , 7 0 = 5 6



É necessário comprar 56 contratos de DI para hedgear as 5.000 NTN-Fs anteriores.

c) Swap pré x DI

Essa opção remove o risco de base, porque seu vencimento é exatamente na duration de Macaulay (embora as outras imperfeições do modelo de duration permaneçam).



D _B = (3 5 2/2 5 2)/(1 + 8, 5 \% ) = - 1, 2 9



Aplicando a equação da imunização pela duration, chega-se a:



1, 6 2 × 1. 0 2 7, 1 5 = 1, 2 9 × V _B





V _B = 1. 2 9 2, 5 2



Esse é o valor do nocional de um swap pré x DI (passivo em taxa pré e ativo em taxa DI) vencendo em 352 dias úteis para hedgear 1 NTN-F. Para 5.000 NTN-Fs, o nocional desse swap seria R$ 6.462.589.

O valor para hedge de 5.000 NTN-Fs será R$ 5.138.547.

d) CDB Pré x DI

O valor é análogo ao item anterior. A diferença é que o derivativo não aumenta a alavancagem financeira e o CDB sim. Além disso, como já explicado anteriormente, os recursos oriundos do CDB Pré não podem ser investidos em títulos prefixados de modo a eliminar o risco de taxas de juros.

Naturalmente, se os recursos forem utilizados em outras modalidades de ativos ou indexadores, o risco geral de mercado da instituição ou fundo pode estar aumentando e não diminuindo.

---

16.3 Hedge

Hedge é uma operação realizada a fim de proteger uma transação anterior de riscos que a mesma incorre, sendo eles de mercado ou de crédito.

Usuários do hedge:

a) Tesourarias de bancos: para se proteger de exposições indesejadas e mitigar riscos oriundos de operações com clientes. É de valor presente no livro de negociação, mas pode ser de fluxo de caixa no livro banking.

b) Fundos de investimento: para proteger os investimentos realizados de oscilações adversas nas variáveis de mercado, sem precisar vender os ativos da carteira. Como o resultado do fundo aparece, em via de regra, na cota dele mesmo, o hedge executado terá o objetivo de proteger o valor presente da carteira.

c) Fundos de pensão: para proteger os fluxos de caixa futuros do plano de benefícios. O passivo do fundo tem de ser remunerado a uma meta atuarial. Como o horizonte é longo, poucos títulos serão usados para diminuir o risco de descasamento. Podem ser usados swaps ou futuros, atentando-se aos riscos de cada uma das modalidades.

d) Tesourarias de empresas: para proteger exportações, importações, emissões de papéis, captações de recursos etc. Normalmente, procura-se uma instituição financeira para realizar operações de balcão. Pode envolver opções³⁸.

O hedge pode ser de fluxo de caixa. quando é feito para proteger o valor de fluxos de caixa futuros de uma determinada transação ou de valor presente, quando se busca proteger o valor corrente de uma carteira ou ativo financeiro.

16.4 Hedge de fluxo de caixa

As estratégias de hedge podem ser de vários tipos, com vários instrumentos, a depender do custo, do risco, da exposição, da expertise de quem vai estruturar e assim por diante.

16.4.1 Hedge de fluxo de caixa com swaps

Nesse item vamos falar de hedge de fluxo de caixa com swaps, que

---

normalmente é utilizado para proteção de emissões no exterior por empresas locais, ou investimentos de pessoas físicas de grandes fortunas, por exemplo.

## Características:

- Feito com instrumentos de balcão de mesmo vencimento disponíveis ao hedger;
- Há que se considerar impostos na formatação do hedge. Quando há ganho no derivativo, a proteção perde efetividade se não for considerado o IR;
- Proteção pode ser feita com ativos ou passivos. Dificuldade: Envolve caixa. Solução mais comum envolve a utilização de derivativos;
- Swap (ou outro instrumento escolhido) pagam taxa com spread, que é a remuneração do intermediário financeiro;
- A operação que se quer hedgear (ativo ou passivo financeiro), vai ter uma ponta de risco equivalente no swap. A outra ponta corresponde a um indexador que o hedger considera de menor risco;
- O banco vai optar por se proteger na B3 ou manter o indexador em suas posições direcionais, se achar que é vantajoso para ele;

## Risco:

Risco de Crédito de Contraparte: como as transações desse tipo no Brasil são para liquidação no vencimento, o cenário ao fim do contrato pode ser tal que haja um ganho muito elevado em uma ponta do swap que gera a inadimplência da outra contraparte.

## 16.4.2 Hedge de fluxo de caixa com futuros

Feito por instituições financeiras para proteger emissões, estruturar produtos de investimento, aplicações proprietárias de bancos comerciais e fundos de pensão, por exemplo.

## Características:

- Feito com utilização de contratos futuros negociados na B3;
- Incorpora risco de base. Existência de descasamento de prazo e,

---

algumas vezes, até de taxa e indexador;

- Existência de risco de liquidez, dados os ajustes na B3;
- Demanda de balanceamento periódico;
- Utilização do conceito de duration.

Embora seja de fluxo de caixa, como é utilizada a técnica de duration, o que se protege na modelagem é o valor presente do ativo ou passivo. Assim, ajustes na modelagem são importantes.

## 16.4.3 Exemplo: hedge de uma NTN-F via swaps

Para este e os próximos exemplos, considere a seguinte NTN-F e a ETTJ vigente:

Figura 16.2 – Exemplo: fluxos de caixa da NTN-F
![img-53.jpeg](img-53.jpeg)
Fonte: Elaborada pelos autores.

Dados ETTJ:



i_(100) = 7,5\%





i_(226) = 8,0\%





i_(352) = 8,5\%





i_(478) = 9,0\%



Observação: assumir a ETTJ da NTN-F igual à da BM&F. Faça o hedge dos fluxos de caixa dessa NTN-F utilizando swaps.

## Solução

O hedge do fluxo de caixa dessa NTN-F poderia ser feito com futuros de DI ou com swaps. A dificuldade com os futuros de DI seria que os vencimentos teriam de estar sincronizados com os vencimentos dos pagamentos de juros do papel. A dificuldade com os swaps seria que eles tenderiam a ser mais caros que os futuros, uma vez que têm como contraparte alguma instituição financeira que precisa ser remunerada.

Isso posto, nesse hedge em particular, os valores futuros são os fluxos de

---

caixa, as taxas são aquelas da ETTJ e os valores presentes em contrato são os valores presentes descontados a essas taxas.

Assim, são quatro swaps Pré x DI com as seguintes características:



Notional5wap_1 = 48,80/(1 + 7,5\%)^(252) = 47,41



taxa de 7.5% a. a. contra 100%³⁹ do CDI.



Notional5wap_1 = 48,80/(1 + 7,5\%)^(252) = 47,41



, taxa de 8.0% a. a. contra 100% do CDI.



Notional5wap_1 = 48,80/(1 + 7,5\%)^(252) = 47,41



, taxa de 8.5% a. a. contra 100% do CDI.



(1 + i_a) du/252 - 1 = i_d



Assim, temos:

|  NTN-F | 1.027,13 |  |   |
| --- | --- | --- | --- |
|  CDI | 47,41 | 47,41 | Pré  |
|  CDI | 45,54 | 45,54 | Pré  |
|  CDI | 43,54 | 43,54 | Pré  |
|  CDI | 890,64 | 890,64 | Pré  |

Esse é um hedge perfeito em termos de fluxos de caixa. Os fluxos de caixa estão totalmente travados em 100% do DI com essa estrutura.

## 16.4.4 Exemplo: hedge de uma NTN-F via DI futuro (352 dias úteis)

Faça o hedge de valor presente para a NTN-F do exemplo anterior com um futuro de DI vencendo em 352 dias úteis.

## Solução

O hedge do valor presente supõe que a duration modificada do ativo seja igual a do passivo:



D_A V_A = D_P V_P



Como D é a duration modificada, podemos escrever:



M_A V_A/(1 + y_A) = M_P V_P/(1 + y_P)



Substituindo os valores:

---



444 × 1.027,15/(1 + 8,94\%) = 352 × V_p/(1 + 8,5\%)



O Valor Presente do futuro de DI será então R$ 1.290,38

Para saber a quantidade de contrato, basta dividir pelo PU:



PU_(DI) = 100.000/(1 + i)^(dv/252)





PU_(DI) = 100.000/(1 + 8,5\%)^(352/252) = 89.229,99



Assim,  q = MtM/PU = 1.290/89.229,99 = 0,014461  contratos para cada NTN-F.

Como se quer ficar ativo em DI a partir de uma posição prefixada, a posição nos DIs é comprada (ativo em taxa DI).

Esse exemplo é teórico e não é possível transacionar esse volume de futuros de DI.

Para o caso de 1.000 NTN-Fs iguais a essa, seriam necessários 14,46 ou 15 contratos de DI.

O balanço a mercado⁴⁰ para a posição com 1.000 NTN-Fs fica:

|  NTN-F | 1.027,15  |
| --- | --- |
|  Fut. DI CDI | 1.290,38 1.290,38 Pré  |

A diferença entre os valores presentes reflete o descasamento de prazo e taxa que existe na posição, ou seja, quando fazemos o hedge pela duration estamos fazendo uma aproximação linear da variação do preço do título com a variação da TIR, logo, esse cálculo deve ser checado com frequência.

Como a duration do DI é inferior à duration da NTN-F, o valor presente da posição em futuro de DI terá de ser superior à posição em NTN-F para contrabalançar o risco de mercado.

## 16.4.5 Exemplo: hedge de uma NTN-F via DI futuro (478 dias úteis)

Faça um hedge de valor presente dessa NTN-F com um swap pré x CDI vencendo em 478 dias úteis.

**Solução**

---

O hedge com o swap⁴¹ será análogo ao hedge com o futuro de DI, com a diferença de que teremos um contrato bilateral entre as partes e não uma transação na BM&F.

Assim, para um vencimento do swap de 478 dias úteis, teremos:



M _A V _A/(1 + y _A) = M _P V _P/(1 + y _P)



Substituindo os valores:



444 × 1.027,15/(1 + 8,94\%) = 478 × V _P/(1 + 9,0\%)



O Valor Presente do swap será então R$ 954,09.

O contrato será o de um swap pré x CDI com taxa ativa de 100% do DI contra uma taxa passiva de 9% a. a. valor presente de R$ 954,09 e vencimento em 478 dias úteis.

O balanço a mercado fica:

|   | NTN-F | 1027,15 |   |
| --- | --- | --- | --- |
|  Swap | CDI | 954,09 | 954,09 Pré  |

Indicando que também existe um descasamento de prazo e de taxas e que houve uso de um algoritmo de linearização que buscou equacionar as duas remunerações (duration).

Para melhor compreensão da questão, segue o balanço com o resumo da solução do primeiro exemplo, no qual utilizamos 4 swaps. Comparação:

|   | NTN-F | 1027,15 |   |
| --- | --- | --- | --- |
|  4 swaps | CDI | 1027,15 | 1027,15 Pré  |

Observe que quando o hedge é de fluxo de caixa com swaps tanto o valor presente quanto o valor futuro estão casados.

Onde não houve aproximação pela duration e, portanto, o descasamento resultante não ocorre.

16.4.6 Exemplo: hedge de título externo

---

Imagine um banco que consegue emitir um título externo de USD 100 milhões por 10 anos a 3,5% a. a., quando o cupom cambial é 2,5% a. a. Supondo que a curva pré (ETTJ) para 10 anos seja de 13% a. a. e a taxa de câmbio atual seja R$ 2,20, calcula:

a) Qual o valor da taxa pré equivalente à taxa de emissão do título externo? E o percentual do CDI equivalente?

b) Qual o swap que faz o hedge do fluxo de caixa futuro do título?

## Solução

a) As curvas de juros têm de estar arbitradas entre si.

Assim, o valor do USD futuro que elas sinalizam deve ser igual nos dois casos:

Dada a equação do preço teórico:



f = S × (1 + i)^(dn/262)/(1 + C × dc/360)



Chega-se a um forward rate premium de:



f/S = (1 + 13\%)^(3.620/262)/(1 + 2,5\% × 3.600/360) = 2,715654



Como o forward rate premium tem de ser o mesmo independente de ser operação de cliente ou não, repete-se o cálculo com o cupom cambial referente à captação do cliente:



f/S = (1 + i)^(2.520/262)/(1 + 3,5\% × 3.600/360) = 2,715654



Que resulta em uma taxa pré i = 13,87\% a. a.

Para determinar o percentual do CDI equivalente, basta calcular as taxas com spread e sem spread em base diária:



(1 + i_d)^(1/262) - 1 = i_n



Fazendo para as taxas com e sem spread, temos:



i = 0,04851\%  a.d. (B3)



i = 0,05157\% a.d. (captação externa cliente)

---

O percentual do CDI referente a essa captação será 106,3% do DI, que é um spread que reflete o custo do dinheiro para o tomador em questão.

b) O swap que faz o hedge do fluxo de caixa futuro do título é aquele que casa totalmente o valor futuro da captação com o valor futuro do derivativo. Seria a operação adequada para uma empresa não financeira.

Assim, será um swap USD x pré com a ponta pré apresentando a mesma taxa da captação.

No contrato, teremos:

Nacional: USD 10.000.000

Taxa ativa: USD + 3,5% a. a. (variação cambial mais 3,5% a. a.)

Taxa passiva: 13,87% a. a.

Como o exemplo é didático, não consideramos o IR sobre ganho de operações de swap na fonte. Assim, para que o hedge funcione quando a taxa de câmbio subir, precisamos aumentar o nocional em uma razão:



1/(1 - alíquota \ IR) = 1/(1 - 20\%) = 1,25.



Logo, para considerar esse efeito, a empresa vai fazer o swap com um nocional de USD 12.500.000.

## 16.4.7 Exemplo: hedge de importação

Um importador precisa liquidar um contrato de importação de USD 100.000.000, que vence em 360 dias corridos (252 dias úteis). Como ele não se sente confortável com as perspectivas sobre a taxa de câmbio, decide comprar um contrato de NDF de USD junto a uma IF.

Sabendo que a taxa pré e o cupom cambial para 1 ano são, respectivamente, 11% a. a. e 1% a. a. e que o USD à vista está sendo cotado a R$ 2.25, calcule:

a) Qual o valor do NDF para esse prazo?

b) Qual a operação que ele (importador) deve fazer de modo a "travar" o valor da taxa de câmbio?

c) Essa operação de NDF é equivalente a um swap. Que swap seria esse? Esquematize o swap definindo o nocional, a taxa da ponta ativa e da passiva.

---

d) Se a taxa de câmbio depois de um ano for de R$ 2.60/USD, qual será o resultado conjunto (importação + NDF) e a taxa de câmbio equivalente?

e) Idem para a taxa de câmbio depois de um ano de R$ 2.15/USD.

## Solução

a) O preço de arbitragem teórico do NDF de USD é igual ao do USD futuro:



f = S × (1 + i)^(255/1963)/(1 + C × dc/360)



Substituindo os valores:



f = 2,25 × (1 + 11\%)^(255/1963)/(1 + 1\% × 360/360) = 2,4728



b) Ele está exposto em USD por uma importação, logo, ele tem de comprar USD futuro ou NDF, de modo a zerar o risco cambial e "travar" uma taxa de câmbio, o que, na prática, significa prefixar a exposição.

Como cada NDF corresponde a um lote de USD 50.000, ele precisa comprar ^a = 100.000.000/50.000 = 2.000 contratos.

c) A compra de NDF corresponde a um swap USD x pré, ativo em USD e passivo em taxa pré. O nocional do swap é equivalente ao valor presente da posição em USD futuro.

Assim:



Notional_(USD) = 100.000.000/(1 + 1\% × 360/360) = 99.009.901



Em reais, na data 0:



Notional_(R\) = 99.009.901 × 2,25 = R\222.772.277



No contrato de swap, os dados serão:

Nocional: R$ 222.772.277

Ponta ativa: USD + 1% (variação cambial + 1% a. a.)

Ponta passiva: 11% a. a.

Lembrando que o lucro do banco pode ser obtido por meio de uma taxa

---

pré na ponta passiva (para o cliente) maior que 11% a. a. e um cupom cambial na ponta ativa menor que 1% a. a., que são as curvas de mercado na BM&F⁴².

d) Se a taxa de câmbio depois de um ano for de R$ 2,60/USD 1, teremos:

- O custo em reais da importação será - USD 100.000.000 x 2.60 = - R$ 260.000.000;
- O ajuste do NDF será a favor do cliente e dado por 50.000 x 2.000 x (2.60 - 2.4728) = R$ 12.722.772;
- O efeito combinado (caixa) do pagamento da importação com o ajuste do derivativo será de - R$ 247.277.228.

Ou seja, a taxa de câmbio futura foi travada em R$ 247.277.228 / USD 100.000.000 = R$ 2,4728, que era o valor indicado pelo NDF.

e) Se a taxa de câmbio depois de um ano for de R$ 2,15/USD 1, teremos:

- O custo em reais da importação será - USD 100.000.000 x 2,15 = - R$ 215.000.000;
- O ajuste do NDF será a favor do banco e dado por 50.000 x 2.000 x (2,15 - 2,4728) = - R$ 32.277.2228;
- O efeito combinado (caixa) do pagamento da importação com o ajuste do derivativo será de - R$ 247.277.228.

Ou seja, a taxa de câmbio futura foi travada em R$ 247.277.228 / USD 100.000.000 = R$ 2,4728, que era o valor indicado pelo NDF.

## 16.5 Imunização de uma carteira de títulos prefixados via DI futuro

Suponha que tenhamos uma carteira de títulos prefixados e desejamos protegê-la das oscilações das taxas de juros. Para imunizar a carteira, o primeiro passo é entender se a carteira está comprada ou vendida em taxa. Ora, quando estamos comprados em títulos prefixados, estamos comprados em preço. Ou seja, se o preço do título subir, o resultado da carteira aumenta. Mas qual a relação entre o preço e a taxa? Aqui, é útil revisitar a equação genérica de precificação de um título:

---



P = Σ(k=1 até n) FC_k/(1 + i_k)^k



Analisando a equação anterior, concluímos que se a taxa de juros, i, subir, o preço do título cai. Então, a carteira está exposta a uma alta de taxas de juros. Quando existe essa relação inversa entre um aumento no valor de uma variável na precificação (neste caso, i) de um ativo e o impacto no seu resultado, dizemos que estamos vendidos nessa variável. Especificamente, quando temos uma posição comprada em títulos prefixados, estamos vendidos em taxa de juros. Esse entendimento é importante para determinar como proteger a carteira. Neste caso, para imunizar a nossa carteira de títulos, precisamos de uma posição comprada em taxa de juros na mesma magnitude da carteira para compensar o efeito no resultado, caso haja um aumento nas taxas.

Uma medida útil que mede essa magnitude da exposição da carteira às taxas de juros é o DV01. O DV01 mede a variação em unidade monetária (por exemplo, reais) do valor da carteira dado uma variação nas taxas de juros de 1 basis point, ou 0,01%. O DV01 de uma carteira, ou de instrumento de renda fixa, pode ser calculado conforme a seguir:



DV01 = D × P × 0,01/100 



Onde D é a duration modificada e P o valor de mercado da carteira ou do instrumento de renda fixa.

## 16.5.1 Exemplo: cálculo do DV01

Suponha que a duration modificada de uma carteira prefixada seja 1,54 e o seu valor de mercado R$ 10.714.286. Calcule e interprete o DV01 da carteira.



DV01 = 1,54 × 10.714.286 × 0,01/100



Então, temos:



DV01 = R × 1.650,00



Ou seja, no caso de uma oscilação de 1 basis point (0,01%) na curva de juros, a carteira perderá, aproximadamente, R$ 1.650,00.

## 16.5.2 Utilizando o DV01 para calcular a quantidade de DI futuro

---

para imunizar a carteira

Continuando o exemplo anterior, suponha que exista um contrato de DI futuro de duration próximo ao da carteira, e que seu DV01 foi calculado em R$ 20,63 (dado). Você decide usar esse instrumento para proteger a carteira.

Descreva como você faria a imunização dessa carteira e calcule quantos contratos de DI futuro você precisaria para imunizar a carteira.

Como a nossa carteira está vendida em taxa de juros, precisamos fazer o hedge por meio de compra de taxa de juros no DI futuro.

Precisamos calcular quantos contratos devemos comprar. Já calculamos que a magnitude da exposição da carteira é R$ 1.650,00 para um aumento de 1 basis point nas taxas. Intuitivamente, podemos calcular a quantidade de contratos de DI futuro necessários para a imunização por uma regra de três: se para um aumento de 1 basis point nas taxas, 1 único contrato de DI futuro, comprado em taxa, ganha R$ 20,63, quantos contratos precisamos para compensar a perda da carteira, ou R$ 1.650,00? Formalmente, basta resolver a equação abaixo:



q = D V 0 1_(C a r t e i r a)/D V 0 1_(1 C o n t r a t o D I F u t u r o) tag {16.6}



Sendo q a quantidade de contratos necessários para fazer a imunização.

Substituindo, temos:



q = 1 . 6 5 0 , 0 0/2 0 , 6 3 ≈ 8 0



Como a nossa carteira de títulos prefixados está vendida em taxa, precisamos comprar taxa por meio deste contrato de DI para imunizar a carteira. Especificamente, 80 contratos.

## Resumo

Este capítulo mostra como imunizar uma carteira de renda fixa, ou seja, protegê-la das oscilações de taxas de juros.

38 Não serão discutidas estratégias de hedge neste texto, porém elas podem ser utilizadas para esse fim, apresentando, muitas vezes, características interessantes para o usuário,

---

como redução de custos e abrangência em alguns casos.

39 Na verdade, a taxa não será 100% do CDI, será menor, em função do lucro da IF contraparte dos swaps.

40 Na realidade, os derivativos são operações off-balance (fora do balanço) e a apresentação descrita é meramente didática. O que se observa na prática são as oscilações do resultado do portfólio, seja ele um fundo ou uma instituição financeira.

41 A quantidade de swaps para o hedge vai variar de acordo com o número de vencimentos em questão. Possivelmente, o ganho em eliminar o risco de base do hedge, nesse caso, é bem maior que o custo que ele acrescenta e provavelmente a solução adotada seria a da questão 2.

42 Naturalmente, a combinação de uma taxa pré maior que a de mercado com a de um cupom cambial menor que o de mercado originarão uma taxa de câmbio para o NDF maior que a de mercado, que equivale ao resultado da instituição financeira.

---

# Capítulo 17
VaR de renda fixa

Este capítulo versa sobre as características principais do VaR, do inglês Value at Risk, a métrica de risco de mercado de utilização mais difundida e sua utilização para controle de risco em instrumentos de renda fixa.

## 17.1 Definição

Na definição do banco JP Morgan, por meio da metodologia RiskMetrics™ (1994, p. 6), “o Valor em Risco é uma medida da máxima alteração potencial no valor de uma carteira de instrumentos financeiros com uma dada probabilidade e num intervalo de tempo pré-determinado”.

Segundo Jorion (1997, p. 82), “o VaR sintetiza a maior (ou pior) perda esperada dentro de determinados períodos de tempo e intervalo de confiança”.

Os parâmetros tempo e confiança são fundamentais na medida do VaR, pois correspondem à parte julgamental do processo, ou seja, à parte que depende do critério do analista.

O período de tempo utilizado é aquele que normalmente se levaria para se desfazer de determinada posição e a confiança representa o percentual máximo de eventos que sobrepujam o valor em risco correspondente.

Ainda segundo Jorion (1997, p. 81), para auxiliar na definição de VaR, define-se W_0 como investimento inicial e R como taxa de retorno. O valor de uma carteira ao final de um período t^* é W = W_0(1 + R).

O retorno esperado e a volatilidade de R são μ e σ. Definindo o retorno crítico como aquele para um dado nível de confiança c, como R^*, o valor da carteira nessa situação será dado por W = W_0(1 + R^*). O VaR é a perda ocorrida nessa situação, que pode ser dada por:



VaR = E(W) - W^* = -W_0(R^* - μ) 



Em sua forma mais genérica, o VaR pode ser obtido da distribuição de probabilidade do valor futuro da carteira, f(w). Para determinado nível de

---

confiança c, a pior realização possível, W^*, terá probabilidade p = 1 - c de ser excedida.



1 - c = int_(-∞)^(W^*) f(w)dw = P(w ≤ W^*) = p 



A integral entre menos infinito e W^* representa a probabilidade p de perda associada a essa distribuição. Nesse sentido, o parâmetro c é o intervalo de confiança que se requer.

O valor W^* é chamado quantil da distribuição e, no sentido amplo, o VaR da mesma.

## 17.2 O VaR paramétrico

No modelo de VaR paramétrico, a ideia é parametrizar a série de retornos por uma função distribuição de probabilidade conhecida de forma que seja possível obter informações estatísticas diretamente da distribuição.

Jorion (1997, pp. 85-87, 179-185) descreve os conceitos e definições principais de como realizar o cálculo do VaR pela metodologia de simulação paramétrica.

O cálculo do VaR pode ser simplificado de forma considerável se a distribuição das taxas de retorno das carteiras puder ser aproximada à normal.

Se esse for o caso, o VaR poderá ser derivado diretamente do desvio padrão da carteira, utilizando-se um fator multiplicativo que dependa do nível de confiança requerido.

O que se busca é transformar a distribuição geral f(w) em uma distribuição normal padronizada Phi(ε), em que ε possua média zero e desvio padrão 1.

Associa-se a W^* ao retorno crítico R^*, tal que W^* = W₀(1 + R^*). Pode-se associar R^* a um fator α > 0 proveniente de uma normal padronizada, por meio de:



α = R^* - μ/σ 



Que equivale a:



1 - c = int_(-∞)^(W^*) f(w)dw = int_(-∞)^(-[R^*]) f(r)dr = ∫(-∞ até -ε) Phi(ε)dε 



---

A determinação do risco de mercado fica restrita ao cálculo da área à esquerda de uma variável normal padronizada, com valor igual a d:



N(d) = ∫(-∞ até -π) Phi(ε) dε 



## 17.3 Resumindo a carteira de renda fixa pelos vértices

O cálculo do VaR paramétrico não é realizado simulando operação por operação.

Embora os sistemas de computação e as máquinas tenham evoluído muito ao longo dos últimos anos, permitindo simulações poderosas em curtos espaços de tempo, a metodologia de VaR demanda a agregação de exposições com vencimentos superiores a um dia nos chamados vértices. Isso faz-se necessário porque o cálculo de volatilidades para todos os vencimentos existentes na carteira seria muito audacioso computacionalmente e não teria informação adicional, uma vez que, como já visto anteriormente, a informação a respeito da expectativa dos agentes sobre as taxas de juros está nas taxas forward, que só se alterarão em função das datas de reunião do Copom.

Além disso, a matriz de fatores de risco apresentaria enorme quantidade de colunas, deixando o algoritmo de cálculo muito mais complexo.

Os vértices são intervalos de tempo móveis em que se alocam as posições marcadas a mercado, de acordo com a distância em tempo entre o vencimento do instrumento e os vértices em si.

Para a taxa pré, os vértices utilizados são os de 1, 21, 42, 63, 84, 126, 252, 504 e 756, 1.008, 1.260 e 2.520 dias úteis e assim por diante, varrendo todo o mercado de renda fixa que se está mapeando.

O principal algoritmo de distribuição dos valores em vértices é derivado do conceito de duration.

O raciocínio por trás do mapeamento é criar uma exposição equivalente entre vértices adjacentes à exposição.

Mas como sintetizar a carteira nos vértices predefinidos anteriormente?

Os valores marcados a mercado são alocados proporcionalmente nos vértices anteriores e posteriores ao seu prazo. As duas exceções são para os

---

prazos menores que 21 dias úteis e maiores que 2.520 dias úteis.

Para os instrumentos de prazos inferiores a 21 dias úteis, o valor alocado do MtM no vértice 21 será feito pela fórmula a seguir:



MtM_(21) = MtM_i × P_i/21,   para  P_i < 21 



Onde P_i é o prazo em dias úteis do instrumento.

Para os instrumentos de prazos superiores a 2.520 dias úteis, o valor alocado do MtM no vértice 2.520 será feito pela fórmula a seguir:



MtM_(2.520) = MtM_i × P_i/2.520,   para  P_i > 2.520 



Para os instrumentos vencendo em prazos entre 21 e 2.520 dias úteis, o valor do MtM será alocado no vértice anterior, V_a, e posterior, V_b, de forma inversamente proporcional à distância entre P_i e o vértice.

Alocação no vértice anterior:



MtM_(Va) = MtM_i × V_p - P_i/V_p - V_a,   para  21 ≤ P_i ≤ 2.520 



Alocação no vértice posterior:



MtM_(Vp) = MtM_i × P_i - V_a/V_p - V_a,   para  21 ≤ P_i ≤ 2.520 



Graficamente, podemos ilustrar como é alocado o MtM_i = R\1.625.656,12 para o prazo P_i = 376 dias úteis:

Figura 1.1 – Exemplo de alocação nos vértices
![img-54.jpeg](img-54.jpeg)
Fonte: Elaborada pelos autores.

## 17.3.1 Exemplo: cálculo de alocação nos vértices de uma posição de LTN

---

Decompor o valor a mercado de uma LTN vencendo em 8 meses nos vértices de 6 meses e 1 ano, usando o critério da duration. A ETTJ para LTNs indica taxa de 8% a. a. para 8 meses.

## Solução

O valor a mercado da LTN será:



P_(LTN) = 1.000/(1 + 8\%)^(168/252) = 949,99



Assim:



MtM_(126) = 949,99 × 252 - 168/252 - 126 = 633,32





MtM_(252) = 949,99 × 168 - 126/252 - 126 = 316,66



## 17.4 Estimação das volatilidades

Volatilidade é a medida da variabilidade dos retornos. Essa medida está associada ao nível de incerteza sobre o comportamento futuro do mercado.

Assim, exposições em mercados mais voláteis acarretam maiores riscos do que em mercados mais estáveis.

O retorno utilizado em cálculos de risco é o retorno log-normal (geométrico ou contínuo).

Quando se trata de calculá-lo para moedas ou preços, o cálculo é imediato:



r_t = ln (P_t/P_(t-1)) 



Onde P são preços de fatores de risco para dois períodos subsequentes.

A vantagem em utilizar o retorno geométrico em vez do retorno aritmético, em tempo discreto, r_t = P_t/P_(t-1) - 1 é que este tipo de álgebra permite a decomposição do retorno de um período determinado como a soma de retornos em períodos parciais, devido às propriedades matemáticas da função exponencial.

Assim:



r_(t,t-2) = ln (P_t/P_(t-2)) = ln (P_t/P_(t-1) × P_(t-1)/P_(t-2)) = ln (P_t/P_(t-1)) + ln (P_(t-1)/P_(t-2)) = r_(t,t-1) + r_(t,t-2) 



Para instrumentos de renda fixa, o retorno da observação i é calculado assumindo-se um papel sintético de valor futuro R$ 100, por exemplo:

---



r _t = ln (1 0 0 / (1 + i _t)^(d n/2 5 3)/1 0 0 / (1 + i_(t - 1))^(d n/2 5 3)) tag {17.12}



O termo du representa cada um dos vértices da curva de juros disponível com qual se espera que o modelo vai trabalhar.

A simplificação da expressão anterior resultará em:



r _t = ln (1 + i_(t - 1)/1 + i _t) cong i_(t - 1) - i _t tag {17.13}



Ou seja, o retorno do modelo é o valor residual que a oscilação da curva de juros apresenta em excesso à flutuação da taxa básica, que já está embutida no preço do papel, como já discutido anteriormente.

A seguir, alguns modelos de cálculo da volatilidade, com base na definição do retorno apresentado na Equação 17.13.

## 17.4.1 Modelo de média móvel

A estimativa da volatilidade por este método consiste em escolher um período de tempo fixo e calcular o desvio padrão da série de retornos do ativo.

À medida que um novo dado é inserido, elimina-se o dado mais antigo, mantendo-se fixo o número de observações.

Supondo uma amostra de observações no tempo, terminando em uma data t qualquer. Desta forma, o desvio padrão na data t, relativo a observações passadas será:



sigma_t = √ {1/n - 1 Σ(i = t - n) ^t (r ᵢ - bar {r}) ²} tag {17.14}



Onde:

- r_i é o retorno da observação i
- r é a média dos retornos

É relevante ressaltar que esse método pondera igualmente todas as observações passadas, assumindo que todas possuam o mesmo grau de importância para a estimação da volatilidade.

No entanto, principalmente em momentos de extrema instabilidade ou

---

estabilidade do mercado financeiro, essa estimativa pode estar subestimando ou superestimando a volatilidade esperada, pois pondera todos os dados com o mesmo peso.

## 17.4.2 Modelo de média móvel exponencial (EWMA)

O modelo de Média Móvel Exponencial é uma generalização do modelo de Média Móvel em que os dados da série de retornos não são ponderados uniformemente.

Dessa maneira, esse modelo reage mais rápido às oscilações do mercado do que o modelo de Média Móvel, dado que confere maior peso às observações mais recentes do que às mais antigas, ou vice-versa, o que não ocorre no modelo de desvio padrão, uma vez que todas as observações de retornos têm o mesmo peso na composição da média que dá a volatilidade.

A fórmula de recursão que é usada para o cálculo da volatilidade é dada a seguir:



sigma_t = √{λ sigma_(t-1)^2 + (1 - λ)(r_(t-1) - mu_(t-1))^2} 



Onde:

- r_t: retorno da observação i
- λ: fator de decaimento exponencial
- μ: média dos retornos até o dia t e sigma_t são as volatilidades diárias

O fator de decaimento λ deve ser estimado para cada mercado, sendo reavaliado de forma a garantir aderência às condições vigentes de mercado.

A metodologia RiskMetrics™ (1996, p. 39) proposta por J. P. Morgan & Co., sugere como fator de decaimento para retornos diários 94% e para mensais 97%.

## 17.4.3 Modelos ARCH/GARCH

Em modelos econométricos convencionais, assume-se que a variância do erro é constante.

No entanto, em vários casos práticos, as séries temporais apresentam períodos de alta volatilidade seguidas de período de relativa tranquilidade. Nessas situações, a hipótese de variância constante – conhecida como

---

homocedasticidade – é violada.

A sigla ARCH significa vetor autorregressivo com heterocedasticidade condicional (ARCH), o qual considera a volatilidade variando no tempo e condicionada às observações passadas:



sigma_t = √{alpha_0 Σ(i=1 até p) alpha_i (r_(t-i) - mu_t)^2} 



Sendo:

mu_t = média dos retornos calculados até o instante

r_(t-i) = é o retorno calculado até o instante

alpha_i = é o coeficiente referente ao instante

p = ordem do processo

Uma das variantes mais conhecidas do modelo ARCH é um modelo mais flexível denominado GARCH, que significa Generalized ARCH. Neste caso, as volatilidades condicionais passadas são incorporadas na volatilidade condicional atual:



sigma_t = √{alpha_0 + Σ(i=1 até p) alpha_i (r_(t-i) - mu_t)^2 + Σ(i=1 até q) beta_i sigma_(t-i)^2} 



Para impedir que a volatilidade assuma valores negativos, devemos respeitar as restrições:



alpha_0 ≥ 0, beta_1 ≥ 0, p ≥ 0  e  p ≥ 0.



A utilização ou não de um método em detrimento de outro é definida em função da complexidade computacional existente no cálculo e do tempo necessário para sua consecução vis-à-vis com os resultados práticos que o método oferece em termos de refinamento dos resultados.

O interessante é que a volatilidade não seja nem tão superestimada que acarrete diminuição de posições injustificada nem tão subestimada que aumente o risco potencial da carteira em demasia.

## 17.5 A matriz de variância-covariância

O cálculo do VaR pela abordagem paramétrica seria extremamente simplório se tratasse apenas de um fator de risco, dado que a distribuição

---

de probabilidade utilizada seria exatamente aquela definida pela normal da série de retornos do único ativo em questão.

No entanto, as carteiras reais têm maior complexidade em função da grande quantidade de instrumentos financeiros transacionados simultaneamente.

Os movimentos que os fatores de risco realizam não são sincronizados, podendo haver depreciação de alguns e apreciação de outros.

O relacionamento linear entre os retornos dos fatores de risco é capturado pela matriz de correlações.

Dado que, conforme já observado, o retorno de um fator de risco é o logaritmo natural do quociente entre os preços deste em dois eventos subsequentes, a correlação entre os retornos de dois fatores de risco é dada por:



rho_(X,Y) = cov(r_X, r_Y)/σ̂(r_X) σ̂(r_Y) 



Onde r_X é o retorno do primeiro fator de risco, r_Y é o retorno do segundo fator de risco, rho_(X,Y) é a covariância entre os retornos diários dos dois fatores de risco, assim calculada:



cov(r_X, r_Y) = 1/n Σ(i=1 até n) (r_(X_i) - r_X̄)(r_(Y_i) - r_Ȳ) 



Quanto mais próxima a correlação estiver de 1, maior o grau de associação linear existente entre os retornos, ou seja, quando o retorno do primeiro fator de risco cresce, na média o retorno do segundo fator de risco cresce também.

Se a correlação for nula, significa que não existe associação linear entre os retornos dos fatores de risco.

A matriz de correlação é a matriz n por n, que contém todas as correlações entre todos os fatores de risco existentes no mercado.

Para o VaR de renda fixa, os fatores de risco são os vértices da curva de juros.

A correlação entre os vértices fornecerá uma informação sobre o movimento médio da curva de juros ao longo do tempo.

Essa característica confere ao modelo de VaR uma vantagem em relação aos

---

modelos em que se assume um choque paralelo na ETTJ.

A hipótese de choque paralelo é substituída no modelo de VaR paramétrico pela matriz de correlações entre os vértices.

## 17.6 O cálculo do VaR de renda fixa

Com as volatilidades de cada vértice, a correlação entre eles e as posições de cada instrumento de renda fixa marcadas a mercado e alocadas entre os vértices para os quais se tenha mapeamento, o cálculo do VaR paramétrico pode ser assim resumido de forma matricial:



VaR = [ [ Z_1 MtM_1 sigma_1 ... Z_n MtM_n sigma_n ] [ {l} 1 ... rho_(12) ... ... ... rho_(1n) 
 ... ... ... ... ... ... ... ... ... ... 
 rho_(n2) ... ... ... ... 1  ] [ {l} Z_1 MtM_1 sigma_1 
 ... ... ... ... 
 Z_n MtM_n sigma_n  ] ] 



Os vértices em que se alocam os valores a mercado das posições podem ser 1, 21, 42, 63, 84, 126, 252, 504, 756 e assim por diante.

Cada vértice tem a distribuição de seus retornos cortada no percentil de probabilidade requerida e para esses são atribuídos os coeficientes Z_i = X(sigma_i)/σ_i, correspondentes à distribuição normal.

Se a confiança requerida para cada uma das distribuições nos vértices for de 99%, os termos Z_i serão tais que a cauda de cada uma das distribuições dos retornos diários nos vértices terão área igual a 1%, abrindo mão, dessa maneira, da suposição da normalidade para todos os vértices.

Os termos sigma_i são as volatilidades de cada ativo calculadas de acordo com algum dos métodos descritos anteriormente.

Os termos MtM_i são os valores a mercado de cada posição da carteira, alocados nos vértices i existentes.

Se todas as distribuições dos retornos nos vértices fossem perfeitamente normais, Z_1 = Z_2 = Z_3 = ... = Z_n = Z. Para 99% de confiança, o valor de Z é 2,33.

## 17.6.1 Exemplo: cálculo do VaR de renda fixa

Um portfólio de um fundo de renda fixa é composto por três ativos de renda fixa:

- 50.000 LTNs de 350 dias úteis de prazo;

---

- 800 contratos de DI futuro comprados vencendo em 400 dias úteis.
- Um CDB pré de valor de emissão R$ 14.000.000, adquirido há 30 dias com taxa de emissão de 8,5% a. a., vencendo em 300 dias úteis.

As taxas da ETTJ de swap pré x DI da BM&F são 8% a. a. para 252 dias úteis e 9% a. a. para 504 dias úteis.

As volatilidades para 1 ano e 2 anos são 0,5% a. d. e 0,7% ao dia e a correlação entre os retornos de 1 e 2 anos é 0,65.

Calcule o VaR desse portfólio sem considerar os spreads de crédito e liquidez da LTN e do CDB para horizonte de 1 dia e confiança de 99%.

# Solução

Para facilitar, o cálculo de interpolação de taxas na ETTJ será feito com utilização do método flat forward:



(1 + Fwd)^(504 - 252/252) = (1 + 9\%)^(504/252)/1 + 8\%^(252/252)



Fwd = 10\% a. a.

Como todos os instrumentos do portfólio vencem entre 1 e 2 anos, só é necessária essa taxa forward para conhecer as taxas spot relativas aos vencimentos desses.

Para calcular as taxas spot utilizando a taxa forward do trecho em questão, usamos:



(1 + i_*)^(du_*/252) = (1 + Fwd)^(du_* - du₁/252) × (1 + i₁)^(du₁/252)



Que aplicadas aos instrumentos que compõem o portfólio:

LTN:



(1 + i_*)^(350/252) = (1 + 10\%)^(350 - 252/252) × (1 + 8\%)^(252/252)



i_* = 8,56\% a. a.

DI:



(1 + i_*)^(400/252) = (1 + 10\%)^(400 - 252/252) × (1 + 8\%)^(252/252)



i = 8,74\% a. a.

CDB-pré:

---



(1 + i_*) 270/252 = (1 + 10\%) 270 - 252/252 × (1 + 8\%) 252/252



i = 8,13\% a. a.

A seguir, os preços teóricos para marcação a mercado:

LTN:



MtM_(LTN) = q × 1.000/(1 + i) du/252 = 50.000 × 1.000/(1 + i) du/252





MtM_(LTN) = 50.000 × 1000/(1 + 8,56\%) 350/252 = 44.609.624



DI:



MtM_(DI) = q × 100.000/(1 + i) du/252





MtM_(DI) = q × 100.000/(1 + i) du/252 = -800 × 100.000/(1 + 8,74\%) 480/252 = -70.037.260



A convenção de sinais é feita em relação à exposição prefixada. Quem compra um ativo de renda fixa está dado, de acordo com o jargão do mercado. Significa que se os juros aumentarem, perde-se dinheiro na estratégia. Uma exposição dada, ou comprada em PU, é representada nos modelos de VaR de renda fixa com sinal positivo.

Quem aplica em CDI (ou Selic), está apostando no aumento da taxa de juros, ou seja, assumindo uma posição tomada. Uma posição comprada em contratos futuros de DI é uma posição tomada (comprada na taxa de juros CDI e vendida em PU), tendo sinal negativo.

CDB-pré:



MtM_(CDB-Pre) = VA × (1 + i_(emissao)) dux/252/(1 + i_(atual)) dxu/252





MtM_(CDB-Pre) = 14.000.000 × (1 + 8,5\%) 500/252/(1 + 8,13\%) 270/252 = 14.188.463



Para alocar os valores a mercado nos respectivos vértices de 1 e 2 anos, usamos:



MtM_(252) = MtM × (252 - du)/(252 - 126)





MtM_(504) = MtM × (du - 504)/(504 - 252)



---

A seguir, tabela com as alocações:

Tabela 17.1 – Resumo dos dados do exemplo para o cálculo do VaR

|  Alocação nos Vértices  |   |   |   |   |
| --- | --- | --- | --- | --- |
|  Instrumento | MtM | MtM252 | MtM504 | Total  |
|  LTNs | 44.609.624 | 27.261.437 | 17.348.187 | 44.609.624  |
|  DI Futuro | -70.037.260 | -28.904.266 | -41.132.994 | -70.037.260  |
|  CDB | 14.188.463 | 13.175.002 | 1.013.462 | 14.188.463  |
|   | Total | 11.532.173 | -22.771.345 | -11.239.172  |
|   | s | 0,50% | 0,70% |   |
|   | MtM x s | 57.661 | -159.399 |   |
|   | r | 0,65 |  |   |
|   | Confiança | 99% |  |   |
|   | p=1-C | 1% |  |   |
|   | Z(1-p) | 2,326 |  |   |
|   | DP portfólio | 129.555 |  |   |
|   | VaR | 301.390 |  |   |

Fonte: Elaborada pelos autores.

Para facilitar o cálculo do VaR, multiplicamos os valores a mercado pelas volatilidades:

E, finalmente:



VaR = √{ | Z_1 MtM_1 sigma_1 ... Z_n MtM_n sigma_n | | {c} 1 ... rho_(11) ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... 
 ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... | } }



Pode ser escrita de forma não matricial para 2 vértices:



VaR = Z × √{ (MtM_(252) × sigma_(252))^2 + (MtM_(504) × sigma_(504))^2 + 2 × rho_(252,504) × (MtM_(252) × sigma_(252)) × (MtM_(504) × sigma_(504)) }





VaR = 2,33 × √((-113.857)^2 + (80.725)^2 + 2 × 0,65 × (-113.857) × (80.725)) = 202.207



## 17.7 O cálculo do VaR de acordo com a carta-circular N. 3.498 do Bacen

A regulação bancária brasileira, definida pelo Banco Central do Brasil, elegeu o VaR paramétrico como o modelo regulatório para as carteiras de

---

títulos prefixados do Trading Book⁴³. A seguir, a fórmula definida pelo Bacen para o cálculo do VaR de um ativo:



VaR_(i,t) = MtM_(i,t) × α × sigma_(i,t) × √(t) × P_i/252 



A fórmula do VaR do ativo i na Equação 17.21 é um pouco diferente da fórmula do VaR que apresentamos anteriormente e da que está descrita em outros livros sobre o tema. Portanto, algumas considerações são necessárias:

- A volatilidade sigma_(i,t) refere-se à volatilidade diária do ativo i;
- O prazo t é medido em dias úteis, mais especificamente, definido em 10 dias úteis pelo Bacen;
- O nível de confiança é definido pelo Bacen em 99%. Logo, α = 2,33;
- O termo adicional P_0 é o prazo em dias úteis do fluxo de caixa i. Portanto, o termo P_i / 252 representa o prazo em anos, ou duration do fluxo.

Então, a fórmula do VaR definida pelo Bacen para calcular o VaR de uma carteira prefixada pode ser reescrita conforme a seguir:



VaR_(i,t) = MtM_(i,t) × 2,33 × sigma_(i,t) × √(10) × P_i/252 



Agora, temos todo o arcabouço teórico necessário para calcularmos o VaR de uma carteira prefixada. Conforme mencionamos, faremos o cálculo de acordo com a metodologia definida pelo Bacen.

Descrevemos o procedimento, passo a passo, utilizando os dados do exemplo da Carta-Circular n. 3.498.

A carteira prefixada exemplificada pelo Bacen na Carta-Circular é conforme a tabela a seguir:

Tabela 17.2 – Exemplo de carteira prefixada

|  Prazo (dias úteis) | Valor no vencimento (R) | Taxa de mercado  |
| --- | --- | --- |
|  1.305 | -20.953.955,08 | 15,49%  |
|  1.131 | 10.291.911,70 | 15,50%  |
|  881 | 3.613.939,59 | 15,41%  |
|  376 | 2.000.000,00 | 14,90%  |
|  65 | 1.000.000,00 | 14,78%  |

---

|  Prazo (dias úteis) | Valor no vencimento (R) | Taxa de mercado  |
| --- | --- | --- |
|  1 | 10.000.000,00 | 15,18%  |
|  2.556 | 4.643.369,51 | 15,49%  |

Fonte: Carta-Circular n. 3.498 do Bacen.

Os valores negativos indicam posições passivas.

Vamos então às etapas de cálculo do VaR:

## 1.º passo: calcular o valor de mercado, MtM, de cada ativo da carteira

Tabela 17.3 – Marcação a mercado da carteira prefixada

|  Prazo (dias úteis) | Valor no vencimento (R) | Taxa de mercado | MtM (R)  |   |
| --- | --- | --- | --- | --- |
|  1.305 | -20.953.955,08 | 15,49% | -20.953.955,08
(1 + 15,49%)^(1.305)/262 = | -9.939.750,02  |
|  1.131 | 10.291.911,70 | 15,50% | 10.291.911,70
(1 + 15,50%)^(1.131)/262 = | 5.390.414,30  |
|  881 | 3.613.939,59 | 15,41% | 3.613.939,59
(1 + 15,41%)^(881)/262 = | 2.189.655,75  |
|  376 | 2.000.000,00 | 14,90% | 2.000.000,00
(1 + 14,90%)^(376)/262 = | 1.625.656,12  |
|  65 | 1.000.000,00 | 14,78% | 1.000.000,00
(1 + 14,78%)^(65)/262 = | 965.068,89  |
|  1 | 10.000.000,00 | 15,18% | 10.000.000,00
(1 + 15,18%)^1/262 = | 9.994.393,40  |
|  2.556 | 4.643.369,51 | 15,49% | 4.643.369,51
(1 + 15,49%)^(1.556)/262 = | 1.077.592,40  |

Fonte: Carta-Circular n. 3.498 do Bacen.

## 2.º passo: alocar os valores marcados a mercado, MtM, nos vértices ou prazos, definidos pelo Bacen

Cada instrumento de uma carteira prefixada é definido pela sua posição, ativa ou passiva, e pelo seu prazo. Como precisamos das correlações de todos os pares de retornos dos ativos para calcular o VaR da carteira, pode-se tornar uma tarefa árdua estimar a matriz de correlação para uma carteira de muitos instrumentos. Um outro inconveniente é que não haveria padronização dos prazos dos instrumentos, tornando difícil a replicação do cálculo do VaR pelo regulador, no caso, o Bacen.

---

Vimos anteriormente que o meio de contornar o problema descrito é resumir todas as posições das carteiras prefixadas sujeitas à regulação do Bacen em vértices predefinidos:

Tabela 17.4 – Prazos dos vértices para o VaR de uma carteira prefixada

|  Vértices, Pᵢ (dias úteis)  |
| --- |
|  21  |
|  42  |
|  63  |
|  126  |
|  252  |
|  504  |
|  756  |
|  1,008  |
|  1,260  |
|  2,520  |

Fonte: Carta-Circular n. 3.498 do Bacen.

Dessa forma, podemos fazer a alocação de toda a carteira nos vértices definidos pelo Bacen:

Tabela 17.5 – Alocação dos valores de mercado nos vértices

|  Prazo (dias úteis) | MtM (R) | Vértice anterior | Vértice posterior | Valor alocado no vértice anterior | Valor alocado no vértice posterior  |
| --- | --- | --- | --- | --- | --- |
|  1.305 | -9.939.750,02 | 1.260 | 2.520 | -9.584.758,95 | -354.991,07  |
|  1.131 | 5.390.414,30 | 1.008 | 1.260 | 2.759.378,75 | 2.631.035,55  |
|  881 | 2.189.655,75 | 756 | 1.008 | 1.103.516,99 | 1.086.138,76  |
|  376 | 1.625.656,12 | 252 | 504 | 825.730,09 | 799.926,03  |
|  65 | 965.068,89 | 63 | 126 | 934.431,78 | 30.637,11  |
|  1 | 9.994.393,40 | Não há | 21 | Não há | 475.923,50  |
|  2.556 | 1.077.592,40 | 2.520 | Não há | 1.092.986,58 | Não há  |

Fonte: Carta-Circular n. 3.498 do Bacen.

## 3.º passo: consolidar os valores dos MtM em um vetor de vértices, em ordem cronológica

A consolidação dos valores dos MtM organiza melhor os dados, facilitando,

---

mais adiante, o cálculo do VaR de cada posição da carteira. Então, podemos sintetizar a carteira nos vértices a seguir:

Tabela 17.6 – Consolidação da alocação dos valores de mercado nos vértices

|  Vértice (dias úteis) | MtM (R)  |
| --- | --- |
|  21 | 475.923,50  |
|  42 | 0,00  |
|  63 | 934.431,78  |
|  126 | 30.637,11  |
|  252 | 825.730,09  |
|  504 | 799.926,03  |
|  756 | 1.103.516,99  |
|  1,008 | 3.845.517,51  |
|  1,260 | -6.953.723,40  |
|  2,520 | 737.995,51  |

Fonte: Carta-Circular n. 3.498 do Bacen.

## 4.° passo: utilizando as volatilidades definidas pelo Bacen para o VaR padrão, calcular o VaR em cada vértice

Como estamos replicando os cálculos da Carta-Circular n. 3.498, estamos assumindo as volatilidades definidas pelo Bacen. No modelo regulatório, é importante sempre verificar quais são os parâmetros vigentes definidos pelo Bacen⁴⁴.

Então, já podemos aplicar a fórmula o VaR do Bacen para cada um dos vértices:

Tabela 17.7 – Demonstrativo do cálculo do VaR de cada posição da carteira

|  Vértice (dias úteis) | BACEN | MtM (R) | VaR (R)(10 dias úteis)  |
| --- | --- | --- | --- |
|  21 | 0.000552116 | 475.923,50 | 475.923,50×2,33×0.000552116×√10×21/252 = 161,34  |
|  42 | 0.000552116 | 0,00 | 0,00×2,33×0.000552116×√10×42/252 = 0,00  |
|  63 | 0.000552116 | 934.431,78 | 934.431,78×2,33×0.000552116×√10×63/252 = 950,33  |
|  126 | 0.001890952 | 30.637,11 | 30.637,11×2,33×0.001890952×√10×126/252 = 213,43  |
|  252 | 0.001890952 | 825.730,09 | 825.730,09×2,33×0.001890952×√10×252/252 = 11.504,68  |

---

|  Vértice (dias úteis) | °BACEN | MtM (R) | VaR (R)(10 dias úteis)  |
| --- | --- | --- | --- |
|  504 | 0.001890952 | 799.926,03 | 799.926,03×2,33×0.001890952×√10×504/252 = 22.290,31  |
|  756 | 0.001975563 | 1.103.516,99 | 1.103.516,99×2,33×0.001975563×√10×756/252 = 40.188,91  |
|  1.008 | 0.001975563 | 3.845.517,51 | 3.845.517,51×2,33×0.001975563×√10×1.008/252 = 223.903,85  |
|  1.260 | 0.001975563 | -6.953.723,40 | -6.953.723,40×2,33×0.001975563×√10×1.260/252 = -506.097,51  |
|  2.520 | 0.001975563 | 737.995,51 | 737.995,51×2,33×0.001975563×√10×2.520/252 = 107.423,80  |

Fonte: Carta-Circular n. 3.498 do Bacen.

Com isso, obtermos nossa matriz de VaR que utilizaremos no cálculo matricial mais adiante:

|161,34 0,00 950,33 213,43 11.504,68 22.290,31 48.188,91 223.903,85 -506.097,51 107.423,80|

Matriz VaR – Carta-Circular n. 3.498

## 5.° passo: obter a matriz de correlação dos retornos entre os vértices

Como estamos replicando os cálculos da Carta-Circular n. 3.498, estamos assumindo as correlações definidas pelo Bacen. No modelo regulatório, é importante sempre verificar quais os parâmetros vigentes definidos pelo Bacen⁴⁵.

Então, de acordo com o exemplo da Carta-Circular, temos:

17.8 – Matriz Correlação Var Padrão

|   | 21 | 42 | 63 | 126 | 252 | 504 | 756 | 1.008 | 1.260 | 2.520  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  21 | 1 | 0.90424 | 0.84112 | 0.7247 | 0.60592 | 0.49805 | 0.44556 | 0.41455 | 0.39434 | 0.35237  |
|  42 | 0.90424 | 1 | 0.94597 | 0.84112 | 0.7247 | 0.60592 | 0.54057 | 0.49805 | 0.46797 | 0.39434  |
|  63 | 0.84112 | 0.94597 | 1 | 0.90424 | 0.79379 | 0.675 | 0.60592 | 0.55899 | 0.52455 | 0.43357  |
|  126 | 0.7247 | 0.84112 | 0.90424 | 1 | 0.90424 | 0.79379 | 0.7247 | 0.675 | 0.6367 | 0.52455  |
|  252 | 0.60592 | 0.7247 | 0.79379 | 0.90424 | 1 | 0.90424 | 0.84112 | 0.79379 | 0.75601 | 0.6367  |
|  504 | 0.49805 | 0.60592 | 0.675 | 0.79379 | 0.90424 | 1 | 0.94597 | 0.90424 | 0.87008 | 0.75601  |
|  756 | 0.44556 | 0.54057 | 0.60592 | 0.7247 | 0.84112 | 0.94597 | 1 | 0.96226 | 0.93101 | 0.82399  |
|  1.008 | 0.41455 | 0.49805 | 0.55899 | 0.675 | 0.79379 | 0.90424 | 0.96226 | 1 | 0.97098 | 0.87008  |

---

1.260 0.39434 0.46797 0.52455 0.6367 0.75601 0.87008 0.93101 0.97098 1 0.90424
2.520 0.35237 0.39434 0.43357 0.52455 0.6367 0.75601 0.82399 0.87008 0.90424 1

Fonte: Carta-Circular n. 3.498.

# 6.° passo: calcular o VaR pela fórmula do VaR paramétrico do Bacen

Agora que temos a matriz de VaR e a matriz de correlação, podemos calcular matricialmente o VaR da carteira conforme resumido a seguir:



VaR_(Carteira) = √(|VaR| × |Correlações| × |VaR|^T)



Substituindo, temos:

![img-55.jpeg](img-55.jpeg)

Resolvendo no MS Excel:



VaR_(Carteira) = R\ 146.004



Então, a interpretação do VaR calculado é que a perda máxima estimada da carteira é R$ 146.004, com 99% de confiança e para um horizonte temporal de 10 dias úteis, sob condições normais de mercado.

A carta-circular ainda mostra como calcular o VaR estressado. O cálculo deste VaR segue os mesmos passos demonstrados para o VaR Padrão acima. A única diferença é que os parâmetros do VaR estressado são diferentes, notadamente as volatilidades e as correlação.

# Resumo

Este capítulo define o VaR e como calculá-lo para uma carteira de renda fixa prefixada.

43 De forma resumida, o Trading Book é composto por ativos negociáveis, que são

---

marcados a mercado. A carteira de um banco pode ser composta de ativos classificados no Trading Book ou no Banking Book. O Banking Book é tipicamente composto de empréstimos e recebíveis que não são negociados no mercado secundário e não estão no escopo do cálculo do VaR, sendo tipicamente muito mais vulneráveis ao risco de crédito do que ao de mercado.

44 Pode-se estimar as volatilidades por várias metodologias, como o EWMA e o GARCH.

45 Pode-se estimar as correlações por várias metodologias.

---

# Exercícios propostos

1. Utilizando os dados da Carta-Circular n. 3.498, calcule em MS Excel e interprete o VaR estressado da carteira utilizada como exemplo nesta carta-circular. Dica: não se esqueça de atualizar as volatilidades e as correlações.

2. Dados os preços de uma ação em quatro datas subsequentes, calcule a média e o desvio padrão dos retornos diários dessa ação.

P_0 = 50

P_1 = 52

P_2 = 51

P_3 = 49

---

# Capítulo 18

O risco de crédito de uma carteira de renda fixa

## 18.1 Definição

O risco de crédito pode ser definido como o risco de perdas devido ao não recebimento referente a um título, empréstimo ou outros instrumentos financeiros, caso a contraparte não honre seus compromissos.

O calote, ou default, é quando o devedor não cumpre as obrigações legais ou condições de um empréstimo. Basta que a contraparte não pague até a data acordada do contrato ou não pague todo o valor acordado. Ou seja, mesmo que a contraparte pague parte do valor devido na data acordada, temos um evento de default.

## 18.2 Fundamentos para mensuração

A mensuração do risco de crédito é muito mais complexa do que a mensuração do risco de mercado de uma carteira. Portanto, assumiremos que alguns parâmetros de entrada no modelo já foram dados. O objetivo aqui é transmitir a intuição quantitativa da mensuração do risco de crédito.

Uma vez definido o que é um default, podemos começar a mensurar qual seria a perda esperada, EL (expected loss), de um default.

Quando somos credores, seja de um título, debênture ou empréstimo, podemos vislumbrar dois cenários possíveis na data de recebimento: default ou não default. Caso não ocorra o default, a nossa perda em função do risco de crédito será zero. Porém, quando ocorre o default, precisamos estimar a nossa perda.

A perda esperada é uma função de três variáveis:

- Probabilidade de default, PD, definida tipicamente para o horizonte temporal de 1 ano;
- Valor devido na data de recebimento, EAD (exposure at default);
- Parcela não honrada do valor devido, LGD (loss given default).

Graficamente, podemos resumir a intuição do cálculo da perda esperada pela

---

figura a seguir:

Figura 18.1 – O racional do cálculo da perda esperada (EL, expected loss)

![img-56.jpeg](img-56.jpeg)

Fonte: Elaborada pelos autores.

Matematicamente, temos que a perda esperada é calculada de acordo com a equação a seguir⁴⁶:



EL = PD × EAD × LGD 



# 18.3 Estimação da perda esperada de uma carteira prefixada

Vimos, de maneira intuitiva, como mensurar a perda esperada de um único ativo. Mas como mensurar a perda esperada de uma carteira de ativos?

Vamos começar calculando a perda esperada da carteira composta pelos 15 ativos a seguir:

Tabela 18.1 – Exemplo de uma Carteira de Recebíveis Prefixadas

|  ATIVO | EAD (R) | PD | LGD  |
| --- | --- | --- | --- |
|  1 | 36.781,23 | 24% | 95%  |
|  2 | 386.719,17 | 2% | 16%  |
|  3 | 78.246,74 | 22% | 62%  |
|  4 | 621.569,69 | 18% | 43%  |
|  5 | 93.112,08 | 13% | 2%  |
|  6 | 330.781,56 | 5% | 64%  |
|  7 | 58.373,51 | 24% | 95%  |
|  8 | 681.754,51 | 13% | 18%  |
|  9 | 14.213,86 | 1% | 25%  |
|  10 | 476.480,09 | 10% | 15%  |
|  11 | 19.883,17 | 23% | 37%  |
|  12 | 521.504,22 | 22% | 24%  |
|  13 | 299.558,17 | 17% | 96%  |
|  14 | 550.151,12 | 1% | 50%  |
|  15 | 724.508,25 | 21% | 47%  |

---

Fonte: Elaborada pelos autores.

Partindo da mesma fórmula da perda esperada de 1 ativo, é simples adaptar a fórmula para calcular a perda esperada de uma carteira de k ativos:



EL = Σ(j=1 até k) PD_j × EAD_j × LGD_j 



Então, substituindo os dados da nossa tabela de ativos na Fórmula 18.2, temos:



EL = R\268,053.12



É relevante ressaltar que, tipicamente, o horizonte temporal para as perdas em função do risco de crédito é de 1 ano.

A maior dificuldade em mensurar a perda esperada no mundo real é a estimação da probabilidade de default e da parcela da perda dado o default. Nesse exemplo básico, assumimos que as probabilidades de default de cada ativo são independentes.

# 18.4 Estimação da distribuição das perdas esperadas de uma carteira

Uma pergunta mais relacionada à mensuração do risco do que “qual é o valor da minha perda esperada?”, é “como é a distribuição das perdas esperadas da minha carteira?”. Esta última pergunta permite-nos estimar a maior perda esperada para um determinado nível de confiança. Ou seja, o VaR do risco de crédito de uma carteira.

Há várias metodologias para mensurar o risco de crédito de uma carteira. Neste livro, optamos por fazê-lo por meio da implementação de um processo chamado Simulação de Monte Carlo (SMC).

A SMC pode ser definida como uma simulação de um processo estocástico que utiliza sorteios aleatórios para determinar o seu resultado ou desfecho.

Assumiremos a mesma carteira de ativos do exemplo anterior. Faremos 10 simulações de cenários que utilizarão sorteios aleatórios para determinar se houve ou não default. Sabemos que uma probabilidade pode assumir valores de 0 a 1. Então, para cada ativo e para cada cenário sorteamos uma probabilidade aleatória^(47):

Tabela 18.2 – Sorteios aleatórios para a Simulação de Monte Carlo

|   | Simul. 1 | Simul. 2 | Simul. 3 | Simul. 4 | Simul. 5 | Simul. 6 | Simul. 7 | Simul. 8 | Simul. 9 | Simul. 10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Ativo 1 | 0,4624 | 0,1379 | 0,5152 | 0,3161 | 0,8119 | 0,5165 | 0,8202 | 0,3676 | 0,4605 | 0,0163  |
|  Ativo 2 | 0,0512 | 0,6809 | 0,3719 | 0,7798 | 0,9735 | 0,3406 | 0,5292 | 0,8906 | 0,4001 | 0,0850  |

---

|   | Simul. 1 | Simul. 2 | Simul. 3 | Simul. 4 | Simul. 5 | Simul. 6 | Simul. 7 | Simul. 8 | Simul. 9 | Simul. 10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Ativo 3 | 0,9262 | 0,2176 | 0,2121 | 0,0252 | 0,4948 | 0,5129 | 0,8840 | 0,6789 | 0,0908 | 0,0916  |
|  Ativo 4 | 0,7129 | 0,5263 | 0,4936 | 0,0936 | 0,2816 | 0,8255 | 0,2908 | 0,3190 | 0,8371 | 0,1290  |
|  Ativo 5 | 0,3026 | 0,3605 | 0,3472 | 0,7292 | 0,1613 | 0,3446 | 0,6275 | 0,0399 | 0,0368 | 0,4601  |
|  Ativo 6 | 0,3845 | 0,6952 | 0,9841 | 0,1170 | 0,5348 | 0,0755 | 0,6323 | 0,8665 | 0,4785 | 0,4144  |
|  Ativo 7 | 0,2843 | 0,8741 | 0,8271 | 0,2948 | 0,4022 | 0,1599 | 0,1149 | 0,8567 | 0,4512 | 0,2067  |
|  Ativo 8 | 0,6082 | 0,5488 | 0,6156 | 0,1891 | 0,0657 | 0,2787 | 0,9949 | 0,5902 | 0,0007 | 0,1008  |
|  Ativo 9 | 0,7318 | 0,5098 | 0,5795 | 0,7630 | 0,0811 | 0,5362 | 0,0973 | 0,3308 | 0,4707 | 0,7626  |
|  Ativo 10 | 0,7267 | 0,0122 | 0,0259 | 0,4259 | 0,2782 | 0,2101 | 0,7445 | 0,1948 | 0,1513 | 0,8584  |
|  Ativo 11 | 0,7622 | 0,6750 | 0,6499 | 0,5858 | 0,7541 | 0,2925 | 0,0908 | 0,3240 | 0,3261 | 0,3780  |
|  Ativo 12 | 0,0609 | 0,2565 | 0,0644 | 0,5190 | 0,5520 | 0,5715 | 0,6558 | 0,4727 | 0,8701 | 0,2896  |
|  Ativo 13 | 0,3919 | 0,1873 | 0,1523 | 0,8810 | 0,9713 | 0,2378 | 0,9747 | 0,6582 | 0,6566 | 0,3395  |
|  Ativo 14 | 0,4172 | 0,4348 | 0,5485 | 0,7577 | 0,6834 | 0,5021 | 0,3128 | 0,2111 | 0,5624 | 0,7159  |
|  Ativo 15 | 0,8030 | 0,3673 | 0,1194 | 0,5543 | 0,4885 | 0,2611 | 0,0870 | 0,5441 | 0,0194 | 0,2258  |

Fonte: Elaborada pelos autores (com base nos númeroos gerados pelo MS Excel).

Denominaremos cada um dos sorteiros pela variavel  delta_(j,x) , sentido que "j" indica o  j -ésimo ativo e "S" a S-ésima simulação.

Uma vez sorteadas as probabilitidades,  delta_(j,x) , podemos verficar se ocorrre ou não um default.

E como faremos esta verificação?

É simples, basta aplicar a regra a seguir:



d_(j, s) = { {l l} 1 & se P D _j ≤ delta_(j, s) 
 0 & caso contrário   tag {18.3}



Onde  d_(j,s)  corresponde ao resultado da verificação: se a probabilitadé sorteada na simulação "S" do ativo "j" for menor ou igual à probabilitadé default do ativo "j", o desfecho da simulação resultou em default, portanto, assumiremos que a variavel  d_(j,s)  é igual a 1. Caso contrário  d_(j,s) , é igual a zero, ou seja, não ocorrre default.

Aplicando a regra anterior, podemos constatar em quais simulacoes de cada ativo em que ocorrreu o default, sinalizadas em cinza naabela a seguir:

Tabela 18.3 - Conversão dos númeroos sorteados em default (1) e não default (0)

|  ATIVO | EAD | PD | LGD | Simul. 1 | Simul. 2 | Simul. 3 | Simul. 4 | Simul. 5 | Simul. 6 | Simul. 7 | Simul. 8 | Simul. 9 | Simul. 10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  1 | 36.781,23 | 24% | 95% | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1  |
|  2 | 386.719,17 | 2% | 16% | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |

---

|  ATIVO | EAD | PD | LGD | Simul. 1 | Simul. 2 | Simul. 3 | Simul. 4 | Simul. 5 | Simul. 6 | Simul. 7 | Simul. 8 | Simul. 9 | Simul. 10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  3 | 78.246,74 | 22% | 62% | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1  |
|  4 | 621.569,69 | 18% | 43% | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1  |
|  5 | 93.112,08 | 13% | 2% | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0  |
|  6 | 330.781,56 | 5% | 64% | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |
|  7 | 58.373,51 | 24% | 95% | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1  |
|  8 | 681.754,51 | 13% | 18% | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1  |
|  9 | 14.213,86 | 1% | 25% | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |
|  10 | 476.480,09 | 10% | 15% | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |
|  11 | 19.883,17 | 23% | 37% | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0  |
|  12 | 521.504,22 | 22% | 24% | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |
|  13 | 299.558,17 | 17% | 96% | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |
|  14 | 550.151,12 | 1% | 50% | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  |
|  15 | 724.508.25 | 21% | 47% | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0  |

Fonte: Elaborada pelos autores.

Agora, estamos perto de obter a distribuição das perdas da nossa carteira obtida pela simulação anterior. Para isso, precisamos aplicar a fórmula da perda esperada para cada simulação de cada ativo:



E L_(j, s) = d_(j, s) × E A D_(j, s) × L G D_(j, s) tag {18.4}



Desta forma, completamos a nossa SMC e obtemos a tabela a seguir:

Tabela 18.4 – Perdas esperadas (EL) pela Simulação de Monte Carlo

|  ATIVO | Simul. 1 | Simul. 2 | Simul. 3 | Simul. 4 | Simul. 5 | Simul. 6 | Simul. 7 | Simul. 8 | Simul. 9 | Simul. 10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  1 | 0,00 | 34.942,17 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 34.942,17  |
|  2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00  |
|  3 | 0,00 | 48.512,98 | 48.512,98 | 48.512,98 | 0,00 | 0,00 | 0,00 | 0,00 | 48.512,98 | 48.512,98  |
|  4 | 0,00 | 0,00 | 0,00 | 267.274.97 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 267.274.97  |
|  5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1.862,24 | 1.862,24 | 0,00  |
|  6 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00  |
|  7 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 55.454,83 | 55.454,83 | 0,00 | 0,00 | 55.454,83  |
|  8 | 0,00 | 0,00 | 0,00 | 0,00 | 122.715,81 | 0,00 | 0,00 | 0,00 | 122.715,81 | 122.715,81  |
|  9 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00  |
|  10 | 0,00 | 71.472,01 | 71.472,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00  |
|  11 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 7.356.77 | 0,00 | 0,00 | 0,00  |
|  12 | 125.161,01 | 0,00 | 125.161,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00  |
|  13 | 0,00 | 0,00 | 287.575,84 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00  |

---

|  ATIVO | Simul. 1 | Simul. 2 | Simul. 3 | Simul. 4 | Simul. 5 | Simul. 6 | Simul. 7 | Simul. 8 | Simul. 9 | Simul. 10  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  14 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00  |
|  15 | 0,00 | 0,00 | 340.518,88 | 0,00 | 0,00 | 0,00 | 340.518,88 | 0,00 | 340.518,88 | 0,00  |
|  Σ = 125.161,01154.927,16873.240,73315.787,95122.715,8155.454,83403.330,481.862,24513.609,91528.900,76  |   |   |   |   |   |   |   |   |   |   |

Fonte: Elaborada pelos autores.

A distribuição das perdas nada mais é do que a soma das perdas esperadas de cada simulação, indicada pela última linha da Tabela 18.4.

De posse da distribuição das perdas, se quisermos, por exemplo, calcular o VaR de crédito dessa carteira para o intervalo de confiança de 90%, basta ordenar as perdas da menor para a maior e encontrar o percentil correspondente:

Tabela 18.5 – Distribuição das perdas esperadas (EL) pela Simulação de Monte Carlo

|  Percentil | EL  |
| --- | --- |
|  10% | 1.862,24  |
|  20% | 55.454,83  |
|  30% | 122.715,81  |
|  40% | 125.161,01  |
|  50% | 154.927,16  |
|  60% | 315.787,95  |
|  70% | 403.330,48  |
|  80% | 513.609,91  |
|  90% | 528.900,76  |
|  100% | 873.240,73  |

Fonte: Elaborada pelos autores.

Podemos concluir por meio desse exemplo básico de VaR de crédito via SMC que a perda máxima esperada para o horizonte temporal de 1 ano, com 90% de confiança, é R$ 528.900,76.

O nosso objetivo neste capítulo foi apresentar a intuição do cálculo de risco de crédito e suas variáveis importantes, dentro do contexto de uma carteira de renda fixa. O risco de crédito é um tema complexo. Há modelos muito mais sofisticados para o seu cálculo, que estão fora do escopo deste livro.

## 18.5 Introduzindo o spread de crédito no VaR

O risco de crédito em modelos de VaR de renda fixa é feito por meio da modelagem dos spreads que existem entre as curvas de juros de títulos que apresentam risco de crédito do emissor.

---

Uma vez que esse spread varia ao longo do tempo devido à percepção do mercado sobre a probabilidade de default daquele emissor, é possível incluir esse spread como variável aleatória no modelo de VaR, calcular sua volatilidade e correlação com os demais fatores de risco existentes.

Para exemplificar o fenômeno, tomaremos o mercado de LTNs.

Sabemos que as taxas de desconto usadas para precificar os títulos de renda fixa zero cupom do Tesouro Nacional não são análogas às taxas de swaps e futuros da BM&F.

Entre outras razões para isso, temos:

- Existência de risco soberano nas LTNs. Há risco de crédito na BM&F, porém a sua manifestação e os volumes envolvidos são menores em função dos mecanismos de mitigação de risco e do próprio mercado de derivativos.
- Existência de prêmio de liquidez nas LTNs, uma vez que para tomar uma posição na BM&F só é necessário alocar margem de garantia, a qual equivale a um percentual do valor da LTN.
- Possibilidade na BM&F de se posicionar na ponta ativa e na ponta passiva (dado e tomado) do mercado de juros. Na aquisição do título de renda fixa só existe a ponta dada (comprada em PU).

Todos esses motivos fazem com que surja um diferencial na taxa de desconto para precificação dos instrumentos que, a priori, seriam os mesmos fatores de risco.

Vamos analisar o caso a seguir:

Tabela 18.6 – Spread: taxas das LTNs x DI futuro BM&F

|  Dias Úteis | LTN | ETTJ BM&F | Spread  |
| --- | --- | --- | --- |
|  5 | 7.18% | 7.00% | 0.17%  |
|  68 | 7.19% | 7.15% | 0.04%  |
|  134 | 7.53% | 7.48% | 0.04%  |
|  198 | 7.84% | 7.77% | 0.06%  |
|  259 | 8.01% | 7.94% | 0.07%  |
|  320 | 8.23% | 8.16% | 0.07%  |
|  451 | 8.59% | 8.52% | 0.06%  |
|  512 | 8.77% | 8.67% | 0.09%  |
|  573 | 8.92% | 8.81% | 0.10%  |

---

|  Dias Úteis | LTN | ETTJ BM&F | Spread  |
| --- | --- | --- | --- |
|  701 | 9.15% | 9.05% | 0.09%  |
|  825 | 9.32% | 9.22% | 0.10%  |
|  952 | 9.35% | 9.37% | -0.02%  |

Fonte: Elaborada pelos autores.

O gráfico a seguir ilustra as taxas de LTNs e a curva de swap pré x DI da BM&F para uma mesma data (com a escala dos spreads no eixo à direita do gráfico).

Gráfico 18.1 – Spread: taxas das LTNs x DI futuro BM&F

![img-57.jpeg](img-57.jpeg)

Fonte: Elaborado pelos autores.

## Modelagem do spread de crédito/ liquidez

A seguir, uma possível modelagem do spread para utilização em modelos de VaR para renda fixa.

O retorno da taxa pré da posição em LTN dado por:



r_(t,t-1)^(LTN) = ln (P_t^(LTN)/P_(t-1)^(LTN))





r_(t,t-1)^(LTN) = ln (1.000/(1 + i_t^(LTN))^(dn/252)/1.000)





r_(t,t-1)^(LTN) = ln ((1 + i_(t-1)^(LTN))^(dn/252)/(1 + i_t^(LTN))^(dn/252))



Observe que há uma diferença entre o retorno da taxa e a remuneração do papel. O retorno da taxa é o diferencial além da remuneração em função das oscilações da ETTJ.

Continuando:



r_(t,t-1)^(LTN) = du/252 ln (1 + i_(t-1)^(LTN)/1 + i_t^(LTN))



Definindo o spread entre a LTN e a BM&F por S, teremos:

---



1 + s = 1 + i_(LTN)/1 + i_(BM\&F)



Substituindo:



r_(LTN_1)^(LTN) = du/252 × ln [ (1 + i_(LTN)^(LTN)) × (1 + s_(t-1))/(1 + i_(LTN)^(LTN)) × (1 + s_t) ]



Pela propriedade dos logaritmos, o logaritmo natural do produto é a soma dos logaritmos:



r_(LTN_1)^(LTN) = du/252 × [ ln (1 + i_(LTN)^(LTN)/1 + i_(LTN)^(LTN)) + ln (1 + s_(t-1)/1 + s_t) ]



Ou seja, o retorno da LTN é a soma dos retornos da taxa da BM&F e do spread entre elas.



r_(LTN_1)^(LTN) = r_(LTN-1)^(BM\&F) + s_(t,t-1)



Como todas são variáveis aleatórias, apresentarão média e desvio padrão, que é dado por:



sigma_(LTN)^2 = sigma_(BM\&F)^2 + sigma_S^2 + 2 × rho_(BM\&F,S) × sigma_(BM\&F) × sigma_S



Ou seja, para introduzir o fator de risco spread de crédito/ liquidez na modelagem do VaR da LTN, é necessário seguir estes passos:

1. Obter uma série histórica de taxas da LTN para os vértices de interesse;
2. Obter uma série histórica de taxas de swap pré x DI para esses mesmos vértices;
3. Calcular por resíduo o valor do spread, utilizando a fórmula 1 + s = 1 + i_(LTN)/1 + i_(BM\&F) para os vértices de interesse;
4. Calcular o desvio padrão ou qualquer outra métrica de volatilidade para as taxas da BM&F e o spread;
5. Aplicar ao modelo de VaR, considerando que essas volatilidades atuam no mesmo PU.

Esse tratamento pode ser dado inclusive para títulos privados, em que as taxas de desconto são maiores quanto maior o risco de crédito, fazendo com que esse spread não seja pequeno.

A modelagem é análoga, porém as taxas de juros são mais complexas de serem obtidas.

---

Resumo

Este capítulo provê a intuição necessária para o cálculo do risco de crédito, focado em carteiras de renda fixa, assim parte do arcabouço teórico para mensurá-lo.

46 Também podemos escrever a equação da perda esperada em função da taxa de recuperação, ou RR (recovery rate). Dado que RR = 1 - LGD, temos que EL = PD × EAD × (1 - RR).

47 No MS Excel, o sorteio de probabilidades aleatórias é implementado pela fórmula RAND(). Na verdade, não existe um sorteio puramente aleatório por meio de algoritmos, dado que o algoritmo possui uma lógica, portanto, não é aleatório. A função do MS Excel foi muito criticada no passado por não ser um bom gerador de números aleatórios. A partir de 2010, o MS Excel utiliza um algoritmo chamado Mersenne Twister, este gera números pseudoaleatórios de alta qualidade.

---

# Exercícios propostos

1. Um banco empresta R$ 100.000 à empresa XPTO a 8% a. a. o. no prazo de um ano. O modelo de crédito do banco estima que a empresa XPTO tem uma probabilidade de default, PD, no horizonte de um ano de 1,5%. A perda dado o não pagamento, LGD, é estimada em 40% do valor do pagamento (ou seja, caso ocorra um default, é esperado que o cliente deixe de pagar 40% do valor devido). Calcule a perda esperada.

2. Considere os dados do exercício anterior, mas agora assuma que o cliente XPTO tenha R$ 80.000 em garantias depositadas no banco. Recalcule a perda esperada. Dica: o valor do EAD deverá considerar as garantias depositadas.

---

# Capítulo 19

## O risco pré em operações com percentual do DI

### 19.1 Utilização do percentual do DI

O mercado financeiro brasileiro tem entre uma de suas características principais a criatividade de seus participantes.

A indexação de contratos derivativos, empréstimos e captações ao percentual da taxa DI (ou CDI) é uma das mais difundidas entre instituições financeiras e demais que gravitam ao redor das mesmas.

Ohanian (2005) resume a razão da grande utilização do percentual do DI como indexador de contratos financeiros em função da “flexibilidade que ele permite às instituições financeiras e empresas de fecharem contratos de swap a taxas equivalentes às praticadas pelo mercado, mesmo que uma das pontas do swap contenha uma determinada taxa de juros ou cupom descolada do nível justo de mercado”.

Já foram apresentados em seções anteriores alguns títulos de renda fixa que indicam o percentual do DI como indexador. No caso desses títulos, os aplicadores conseguem a prerrogativa de investir em um instrumento pós-fixado, indexado à taxa diária que representa o custo do dinheiro e, além disso, atrela a remuneração de prêmio de liquidez e risco de crédito do emissor à mesma taxa diária de referência.

Entretanto, o que nem todos os participantes do mercado sabem é que existe um risco de preço de natureza prefixada nessas operações.

Esse risco é originado do fato de que, apesar de se tratar de uma operação pós-fixada, o resultado financeiro da operação acaba ficando atrelado ao percentual do DI e, portanto, pode sofrer oscilação em seu valor, uma vez que a expectativa dessa taxa está sendo alterada ao longo do tempo e quando se marca o mercado o instrumento, esse excedente de remuneração tem sua magnitude alterada com os movimentos da ETTJ pré.

---

Matematicamente:

Como já visto anteriormente, o valor a mercado de um CDB DI com percentual do DI α é dado por:



MtM_(CDB-Pos) = VA × ∏(i=0 até n-1) (1 + α × CDI_i) × (1 + α × i_(mercado))^(dup)/(1 + i_(mercado))^(dup)



De imediato, nota-se por meio equação anterior que, para qualquer valor de α diferente de 100\%, o valor a mercado desse CDB DI (que poderia ser um empréstimo indexado ao CDI ou a ponta CDI de um swap qualquer) é afetado.

## 19.2 Duration de uma exposição em percentual do DI

Para simplificar a notação e os cálculos, é interessante fazer algumas mudanças de variáveis.



P = Accrual × (1 + α × i)^n/(1 + i)^n



Onde:



Accrual = VA × ∏(i=0 até n-1) (1 + α × CDI_i)



representa o valor na curva do CDI ID até a data t

P: valor a mercado do CDB DI na data t

i: taxa de juros pré para a data de vencimento em cotação base diária

n = T - t: tempo remanescente até a data de vencimento em dias úteis

É possível provar que a duration modificada dessa exposição é dada por:



D = 1/P dP/di = n × (α - 1)/(1 + α × i) × (1 + i)



A derivação da equação anterior está demonstrada no final deste capítulo.

## 19.3 Inclusão do percentual do DI no modelo de VaR

Para incluir os instrumentos indexados em percentual do CDI no modelo de VaR de renda fixa, basta igualar essa duration a uma de um título fictício zero cupom, de mesmo vencimento.

Vamos criar um título de renda fixa sintético que vence em n dias úteis e que tenha a mesma sensibilidade a variações da taxa de juros que a exposição em percentual do CDI mencionado.

---

Admitindo que o título tenha valor futuro VF, seu valor presente será igual a:



P = VF/(1 + i)^n



Derivando o valor presente do título em relação à taxa de juros:



dP/di = VF × (-n) × (1 + i)^(n-1)



Reescrevendo:



dP/di = VF × (-n)/(1 + i)^n × (1 + i)



Pela equação P = VF/(1 + i)^n, temos:



dP/di = P × (-n)/(1 + i)



E a *duration* modificada resulta em:



D = 1/P dP/di = -n/(1 + i)



Para obter a exposição equivalente prefixada no título fictício relacionada a uma exposição em percentual do CDI, basta igualar a perda financeira em reais nos dois títulos:

Para a exposição em percentual do CDI:



1/P dP/di = n × (α - 1)/(1 + α × i) × (1 + i) ⇒ dP/di = n × (α - 1)/(1 + α × i) × (1 + i) × P_(\%CDI)



Para a exposição em título pré de valor futuro VF:



D = 1/P dP/di = -n/(1 + i) ⇒ dP/di = -n/1 + i × P_(pré)



Assim:



n × (α - 1)/(1 + α × i) × (1 + i) × P_(\%CDI) = -n/(1 + i) × P_(pré)



Desenvolvendo os termos:



P_(pré) = (1 - α)/(1 + α × i) × Accrual × (1 + α × i)^n/(1 + i)^n



A equação anterior representa o valor presente de um título de renda fixa que gera a mesma sensibilidade às oscilações da taxa de juros que a

---

exposição em CDI.

Repare que esse raciocínio pode ser usado para a realização do hedge dessa exposição com contratos futuros. Ocorre que os contratos futuros não vencerão exatamente na data de vencimento do CDB DI ou do empréstimo indexado ao CDI.

## 19.4 Alternativa à forma algébrica com a utilização do DV01

Outra maneira de calcular a exposição pré equivalente a uma exposição em percentual do CDI é calculando o DV01 da operação indexada ao CDI e igualando o resultado ao DV01 de um título pré de vencimento análogo e valor futuro VF.

O DV01 de uma exposição em percentual do CDI parte do mesmo conceito já apresentado, logo:



DV01 = Accrual × (  [ (1 + i + ε)^(1/292) - 1 ] × α + 1 / (1 + i + ε)^(α/292)  -  [ (1 + i)^(1/292) - 1 ] × α + 1 / (1 + i)^(α/292)  )



Onde:

- i: taxa de juros da ETTJ pré em base anual
- ε: choque de 0,01%, de modo a obter o efeito numérico da derivada

Que será forçado a ser igual ao DV01 de um título pré com vencimento na mesma data.



DV01 = VF × [ 1/ (1 + i + ε)^(α/292) - 1/ (1 + i)^(α/292) ]



Resultando em:



VF = Accrual × (  [ (1 + i + ε)^(1/292) - 1 ] × α + 1 / (1 + i + ε)^(α/292)  -  [ (1 + i)^(1/292) - 1 ] × α + 1 / (1 + i)^(α/292)  ) / [ 1/ (1 + i + ε)^(α/292) - 1/ (1 + i)^(α/292) ] 



Esse valor de VF será inserido no modelo de VaR como exposição pré, recebendo todo o tratamento equivalente.

## 19.5 Oscilação da capacidade de crédito da contraparte

Apesar de termos usado a notação de derivadas totais nos modelos de

---

duration anteriores, essas seriam melhor definidas como derivadas parciais, já que na formulação do preço teórico dos instrumentos modelados existem outras variáveis condicionantes.

Uma variável importante que altera o valor a mercado dos instrumentos indexados a percentual do CDI é o próprio valor desse percentual, que pode sofrer alterações com o passar do tempo, dependendo da qualidade de crédito do emissor, da liquidez do mercado etc.

Na formulação feita, esse percentual do CDI é admitido constante para o papel, mais pelo benefício da simplicidade do cálculo do que por outra razão, já que dependendo do ambiente econômico vigente essa variável pode sofrer oscilações grandes ao longo do tempo.

Tais oscilações dizem respeito a manifestações de risco de crédito, mas podem ser mensuradas dentro do arcabouço analítico de risco de mercado em renda fixa, via VaR ou via stress test.

## 19.5.1 Exemplo: DV01 de um CDB indexado ao DI

Um banco está emitindo nesse exato momento um CDB indexado ao DI de valor inicial de R$ 10.000.000, com remuneração de 115% e prazo total de 300 dias úteis.

A curva pré da BM&F para o prazo da operação é 8% a. a.

Calcule:

a) Valor a mercado do CDB DI.
b) Duration modificada do CDB DI.
c) Exposição prefixada equivalente do CDB DI.
d) Número de contratos de DI requeridos para hedge, com vencimento 60 dias úteis depois do vencimento do CDB DI e taxa de mercado de 8,15% a. a.
e) Exposição prefixada equivalente usando o DV01.

## Solução

a) Valor a mercado do CDB DI

---



P = Accrual × (1 + α × i)^n/(1 + i)^n





P = -10.000.000 × {1 + 115\% × [(1 + 8\%)^(1/252) - 1]}^(300)/(1 + 8\%)^(300/252) = -10.138.355



O sinal negativo significa que se trata de uma captação de recursos da instituição. A taxa de juros nessa equação está expressa em base diária.

b) A duration modificada do CDB DI



D = 1/P dP/di = n × (α - 1)/(1 + α × i) × (1 + i)





D = 1/P dP/di = 300 × (115\% - 1)/{1 + 115\% × [(1 + 8\%)^(1/252) - 1]} × (1 + 8\%)^(1/252) = 44,97



c) Exposição prefixada equivalente do CDB DI



P_(pre) = (1 - α)/(1 + α × i) × Accrual × (1 + α × i)^n/(1 + i)^n





P_(pre) = (1 - 115\%)/(1 + 115\% × [(1 + 8\%)^(1/252) - 1]) × -10.000.000 × [1 + 115\% × [(1 + 8\%)^(1/252) - 1]]^(300)/(1 + 8\%)^(300/252) = 1.520.219



Pela equação anterior, a exposição é tomada em pré, ou seja, a instituição financeira ganha quando a taxa de juros aumenta.

d) Número de contratos de DI requeridos para hedge, com vencimento 60 dias úteis depois do vencimento do CDB DI e taxa de mercado de 8,15% a. a.

Cálculo do PU do futuro de DI:



PU = 100.000/(1 + i)^(60/252),  onde  i  é taxa ano.



Assim:



PU = 100.000/(1 + 8,15\%)^(300/252) = 89.410,94



A quantidade de contratos necessária para o hedge será dada pela relação:



n × (α - 1)/(1 + α × i) × (1 + i) × P_(\% CDI) = -n/(1 + i) × P_(pré)





n × (α - 1)/(1 + α × i) × (1 + i) × P_(\% CDI) = -n/(1 + i) × q × PU



Desenvolvendo:

---



q = Accrual × (1 + α × i) ^n/(1 + i) ^n × (1 - α)/(1 + α × i)



Que para o exercício apresentado resulta em:



q = - 10.000.000 × [ 1 + 115 \% × [ (1 + 8 \%)^(1/252) - 1 ] ]^(300)/(1 + 8 \%)^(300) × (1 - 1,15)/[ 1 + 115 \% × [ (1 + 8 \%)^(1/252) - 1 ] ]/89.410,94 = 17



Para hedgear a exposição pré originada pela cláusula de indexação ao percentual do CDI do CDB do exercício serão necessários 17 contratos futuros de DI.

Como a exposição é tomada em pré, tudo se passa como se fosse uma captação em pré, logo, o hedge tem de ser comprado em PU ou vendido em taxa. Na BM&F, será necessário vender 17 contratos futuros de DI, cujo objeto é a taxa DI.

e) Exposição prefixada equivalente usando o DV01.

Esse item serve para checar os resultados do item anterior.



VF = Accrual × ([ [ (1 + i + ε)^(1/252) - 1 ] × α + 1 ] ^n/(1 + i + ε)^(1/252) - [ [ (1 + i)^(1/252) - 1 ] × α + 1 ] ^n/(1 + i)^(1/252))/[ 1/(1 + i + ε)^(1/252) - 1/(1 + i)^(1/252) ]





VF = 10.000.000 × ([ (1 + 8 \% + 0.01 \%)^(1/252) - 1 ] × 115 \% + 1/(1 + 8 \% + 0.01 \%)^(1/252) - [ (1 + 8 \%)^(1/252) - 1 ] × 115 \% + 1/(1 + 8 \%)^(1/252) ]/(1 + 8 \% + 0.01 )^(1/252) )/1 - 1.666.687



E o seu valor presente será dado por:



P = VF/(1 + i) ^n = 1.666.687/(1 + 8 \%)^(300) = 1.520.315



O que comprova o resultado obtido pela duration modificada.

## 19.6 Derivação da duration de uma exposição em percentual de DI

Derivação da duration de uma exposição em percentual do CDI.

Dado que:



P = Accrual × (1 + α × i) ^n/(1 + i) ^n



---

Derivando-se P em relação a i, temos pela regra da derivada do quociente:



dP/dt = Accrual × n × (1 + α × i)^(n-1) × α × (1 + i)^n - (1 + α × i)^n × n × (1 + i)^(n-1)/[(1 + i)^n]^2



Que pode ser escrita como:



dP/dt = Accrual × n × (1 + α × i)^n × α × (1 + i)^n/(1 + α × i) - (1 + α × i)^n × n × (1 + i)^n/(1 + i)/[(1 + i)^n]^2



Colocando os termos comuns em evidência:



dP/dt = Accrual × n × (1 + α × i)^n × (1 + i)^n × [ α/(1 + α × i) - 1/(1 + i) ]/(1 + i)^n × (1 + i)^n



Desenvolvendo dentro do colchete:



dP/dt = Accrual × n × (1 + α × i)^n × (1 + i)^n × [ α × (1 + i) - (1 + α × i)/(1 + α × i) × (1 + i) ]/(1 + i)^n × (1 + i)^n





dP/dt = Accrual × n × (1 + α × i)^n × (1 + i)^n × [ α - 1/(1 + α × i) × (1 + i) ]/(1 + i)^n × (1 + i)^n



Cortando o termo (1 + i)^n no numerador e no denominador, teremos:



dP/dt = Accrual × n × (1 + α × i)^n × [ α - 1/(1 + α × i) × (1 + i) ]/(1 + i)^n



Mas, da equação inicial, sabemos que P = Accrual × (1 + α × i)^n/(1 + i)^n. Substituindo no desenvolvimento, temos:



dP/dt = P × n × [ α - 1/(1 + α × i) × (1 + i) ]



Que resulta na definição clássica de *duration* modificada para uma exposição em percentual do CDI:



D = 1/P dP/dt = n × (α - 1)/(1 + α × i) × (1 + i)



---

**Resumo**

Este capítulo trata de produtos da mensuração do risco de mercado de instrumentos corrigidos por um percentual do DI.

---

# Conclusão

Esperamos que o conteúdo deste livro tenha sido útil ao aprendizado dos leitores sobre os temas relacionados ao mercado de Renda Fixa no Brasil. Procuramos apresentar os tópicos em ordem crescente de complexidade, facilitando a construção do conhecimento dos leitores menos familiarizados com os fundamentos de Renda Fixa nacional. Acreditamos que este livro também possa ser usado para consultas específicas, assim, dependendo do grau de exposição prévia do leitor, aos assuntos tratados neste livro, poderá consultar capítulos específicos, sem que, obrigatoriamente, tenha de ler outros capítulos previamente.

Agradecemos a todos que dedicaram o seu tempo a este livro, nos sentimos muito honrados. Fizemos de tudo para entregar um trabalho preciso, principalmente nas partes mais quantitativas e dos exemplos implementados. De qualquer forma, caso o leitor tenha qualquer dúvida, ficaremos ainda mais agradecidos se enviarem um e-mail para editora@saintpaul.com.br.

Cordialmente,

Os autores.

---

Extra: Exercícios avançados resolvidos

1. Explique as três utilizações dos contratos de derivativos.

**Solução**

Especulação: quando o usuário assume uma posição acreditando que haverá valorização de sua parte do contrato.

- Hedge: quando o usuário assume uma posição para proteger alguma exposição que ele tenha previamente.
- Arbitragem: quando o usuário utiliza o contrato derivativo para, em conjunto com outros instrumentos, realizar uma operação financeira com lucro sem risco.

2. Qual a diferença entre dólar futuro e NDF

**Solução**

O dólar futuro é o contrato futuro transacionado na BM&F em que se negocia o valor do preço do USD americano para liquidação em reais na BM&F. O NDF é o mesmo derivativo, porém negociado no balcão.

3. Imagine uma importação no valor de USD 10.000.000. Pergunta-se:

a. Quantos contratos futuros de USD futuro são necessários para hedgear essa importação?

b. Compra ou venda?

c. Se a taxa de câmbio futura inicial (no momento do hedge) foi de R$ 3,10 e a taxa final (no momento da liquidação do contrato) foi de R$ 3,50. Determine o fluxo de caixa da liquidação da importação, o ajuste na BM&F e o efeito combinado das duas operações.

**Solução**

a. São necessários 10.000.000/50.000 = 200;

b. Compra.

c. Liquidação da importação = 10.000.000 * 3,50 = USD -35.000.000; Ajuste na BM&F = 200 * (3,50-3,10) * 50.000 = - 4.000.000; Efeito Combinado = USD -31.000.000 (que resulta em uma taxa de câmbio de R$ 3,1 por USD).

4. Imagine que a taxa pré para algum período seja 13% a. a. O que é melhor, receber 115% do CDI ou 15,09% a. a.?

**Solução**

---

Estão arbitradas em t=0. Se a taxa pré é 13% a. a. a taxa diária será 
(1 + 13\%)^(252) - 1 = 0,049\%
 a. d.

Aplicando o spread de 115% nessa taxa, teremos: 
0,049\% × 115\% = 0,056\%  a.d.
 que em taxa ano resulta em 
(1 + 0,056\%)^(252) - 1 = 15,09\%  a.a.


Você escolhe uma ou outra em função da sua percepção em relação ao acumulado da taxa DI ao longo do tempo.

5. O que significa dizer que duas curvas de juros estão arbitradas?

## Solução

Significa que qualquer operação de swap que se faça resulta em lucro nulo, ou seja, não dá para obter lucro tomando emprestado em uma curva e aplicando em outra.

6. Quais são os ativos subjacentes (objeto) dos seguintes derivativos: contrato futuro de DI, contrato futuro de USD, contrato futuro de Ibovespa e contrato duturo de DDI?

## Solução

Taxa de juros pré em reais, USD futuro, Ibovespa e cupom cambial (taxa de juros em USD).

7. Uma empresa tomou emprestado USD 10.000.000 quando a taxa de câmbio estava em R$ 3,00 por USD. A taxa desse empréstimo foi 1,5% a. a. para um ano. Com medo da desvalorização cambial, essa empresa planeja fazer um swap pré x USD com taxa de cupom de 1,5% a. a. e taxa pré de 13% a. a.

Pede-se:

a. Faça o razonete com o empréstimo e o swap.
b. Qual o valor da dívida em R se a taxa de câmbio for para R4,00/USD?
c. Nessa situação, qual o ajuste do swap?
d. Qual o efeito combinado da liquidação do empréstimo e da liquidação do swap?

## Solução

a. Razonete a seguir:

|   | 30.000.000 | Empréstimo (USD +1.5%)  |
| --- | --- | --- |
|  USD + 1.5% 30.000.000 | 30.000.000 | Swap (13% a. a.)  |

b. O valor da dívida será o valor do principal + juros em 
 USD.10.000.000 × (1 + 1,5\% × 360 / 360) = USD 10.150.000 . Se a taxa de câmbio terminou em R$ 4/USD, o valor da dívida em R no vencimento será de 
 EL_(j,s) = d_(j,s) × EAD_(j,s) × LGD_(j,s) 
.

c. O ajuste do swap será dado pela diferença em reais da ponta ativa (USD) e da ponta passiva (taxa pré).

---



10.000.000 * (1 + 1.5\% × 360 / 360) × 4 - 10.000.000 × 3 × (1 + 13\%) * (252 / 252) = BRL\ 6.700.000



d. O efeito combinado (fluxo de caixa das duas operações) será -40.600.000 (liquidação do empréstimo) + 6.700.000 (ajuste recebido) = -R$ 33.900.000.

8. Um fundo de investimento comprou 30.000 LTNs com vencimento em um ano. A taxa de juros para esse vencimento é 13% a. a. Preocupado com o risco de perda na cota caso a taxa de juros subisse, o gestor do fundo decidiu hedgear a posição com a utilização de um swap pré x DI.

Pergunta-se:

a. Qual o valor da posição em LTNs?

b. Qual a ponta comprada e qual a ponta vendida nesse swap?

c. Se a taxa de juros CDI acumulada média foi 14%, qual o valor no vencimento da LTN, do swap e o feito combinado de ambos?

d. Mostre o balanço desse fundo no vencimento com a LTN e com o swap.

## Solução

a. O preço dessa LTN é dado por P = 1000/1 + 13\% = 884,96. Como são 30.000, a posição total é 30.000 × 884.96 = BRL\ 26.548.672,57.

b. Como a LTN é pré e é um ativo do fundo, para hedgeá-la será necessário ficar passivo em taxa pré e ativo em taxa DI.

c. Valorização da Ponta CDI = 26.548.672,57 × (1+14%) = BRL 30.265.486,73.

Valorização da Ponta Pré = 26.548.672,57 × (1+13%) = BRL 30.000.000.

Ajuste swap = 30.265.486,73 - 30.000.000 = BRL 265.486,73.

O valor futuro da LTN é R$ 30.000.000 (igual ao valor de vencimento da ponta pré do swap).

d. O balanço do fundo conforme a seguir:

|  LTN | 30.000.000 |   |
| --- | --- | --- |
|  Swap | 30.265.487 | 30.000.000 Pré  |

9. Uma empresa emitiu uma debênture no valor de R$ 150.000.000, que paga 100% do CDI. O diretor financeiro quer prefixar o valor a ser pago no futuro, pois está preocupado com um aumento dos juros. O vencimento dessa debênture é um ano, período para o qual a taxa pré está sendo negociada a 13% a. a.

a. Que operação de swap esse diretor vai fazer para prefixar a operação?

b. Se a taxa DI acumulada média no final do período for 12%, qual o valor da dívida, do ajuste do swap e do efeito combinado de ambos?

---

c. Represente as duas operações no vencimento com um razonete.

## Solução

A debênture é um passivo em taxa DI. A empresa não financeira pode se sentir desconfortável em assumir um passivo com um indexador com base em taxa de juros flutuante.

a. Assim, para eliminar o risco de aumento de juros, a empresa vai contratar um swap passivo em taxa pré e ativo em taxa DI.

b. Depois de um ano, o saldo da debênture vai ser 150.000.000 × (1+12%) = BRL 168.000.000. o ajuste do swap será de 150.000.000 × (1+12%) - 150.000.000 × (1+13%) = - BRL 1.500.000 e o efeito combinado do pagamento da debênture mais o ajuste do swap resultará em uma saída de caixa de - BRL 168.000.000 - 1.500.000 = - BRL 169.500.000.

c. Veja a seguir:

|   | 168.000.000 | Debênture  |
| --- | --- | --- |
|  CDI 168.000.000 | 169.500.000 | Swap  |

10. Considere a carteira de títulos prefixados de um fundo de direitos creditórios a seguir:

|  t (anos) | Fluxo (R mil) | ETTJ  |
| --- | --- | --- |
|  1 | 50 | 13%  |
|  2 | 75 | 14%  |
|  3 | 35 | 15%  |

Pede-se:

a. O valor presente da carteira.

b. A taxa interna de retorno do fluxo.

c. A duration de Macaulay em anos e em dias úteis.

d. A duration modificada.

e. A taxa de juros referente ao prazo encontrado no item a) usando o método de interpolação flat forward.

## Solução

a. Para acharmos o valor presente do fluxo, é necessário descontar os valores pelas taxas de juros de mercado:



P = Σ(k=1 até n) FC_k/(1 + i_k)^k



Que, no exemplo dado resulta em:

---



P = 50/(1 + 13 \%)^1 + 75/(1 + 14 \%)² + 35/(1 + 15 \%)³ = 124,97



|  t (anos) | Fluxo (R mil) | ETTJ | VP  |
| --- | --- | --- | --- |
|  1 | 50 | 13% | 44,25  |
|  2 | 75 | 14% | 57,71  |
|  3 | 35 | 15% | 23,01  |
|  Preço: |   |   | 124,97  |

b. A taxa interna de retorno é aquela que faz com que o valor presente do fluxo descontado à TIR seja análogo ao valor presente do fluxo transacionado no mercado.

Assim, criamos uma função f(y) com o preço de mercado e o preço do modelo.



f(y) = P_(mercado) - Σ(k=1 até n) FC_k/(1 + y)^k



Quando f(y) = 0, y = TIR.

|  t (anos) | Fluxo (R mil) | ETTJ | VP ETTJ | VP TIR  |
| --- | --- | --- | --- | --- |
|  1 | 50 | 13% | 44,25 | 43,82  |
|  2 | 75 | 14% | 57,71 | 57,6  |
|  3 | 35 | 15% | 23,01 | 23,56  |
|  Preço: |   |   | 124,97 | 124,97  |
|   |   |   | y | 14,11%  |

c. A duration de Macaulay será dada pelo prazo médio da carteira ponderado pelos valores presentes dos fluxos de caixa descontados pela TIR:



M = Σ(k=1 até n) P_k × k/P



Assim:



M = 43.82 × 1/124.97 + 57.60 × 2/124.97 + 23.56 × 1/124.97 = 1.84



Ou seja, em 1,84 anos podemos substituir todos os fluxos de caixa por um só fluxo de modo a ter o mesmo risco que o portfólio correspondente.

|  t (anos) | Fluxo (R mil) | ETTJ | VP ETTJ | VP TIR | VP TIR  |
| --- | --- | --- | --- | --- | --- |
|  1 | 50 | 13% | 44,25 | 43,82 | 0,35  |
|  2 | 75 | 14% | 57,71 | 57,6 | 0,92  |
|  3 | 35 | 15% | 23,01 | 23,56 | 0,57  |
|  Preço: |   |   | 124,97 | 124,97 |   |
|   |   |   | y | 14,11% |   |
|   |   |   | M | 1,84 ano | ou 463 du  |

---

d. Dado que:



D = -M/(1 + y)



Substituindo os valores:



D = -M/(1 + y) = -1.84/(1 + 14,11\%) = -1,61



e. Usando o flat forward entre os vértices de 1 e 2 anos, teremos:



(1 + fwd)^(t_2 - t_1) = (1 + i_2)^(t_2)/(1 + i_1)^(t_1)



fwd = 15.01% a. a.

Para t = 1,84 anos:



(1 + 15,01\%)^(1.84 - 1) = (1 + i_*)^(1.84)/(1 + 13\%)^t



i_* = 13,91\% a. a.

11. O gestor quer mudar a remuneração da carteira anterior de fixa para flutuante, ou seja, de pré para di. Faça essa transformação (hedge) usando:

a. Contratos de DI futuro vencendo em 2 anos.

b. Swaps vencendo na duration de Macaulay (desconsiderar o lucro do banco que fornece o hedge).

## Solução

a. A equação de imunização é:



P_(ativo) × D_(ativo) = P_(derivativo) × D_(derivativo)



Com futuro de DI, a equação anterior fica:



124,97 × 1,61 = q × 100.000/(1 + 14\%)^2 × 2/(1 + 13,91\%)



q = 1489 contratos, vencimento em 2 anos comprados.

b. Com um swap vencendo na duration de Macaulay:



124,97 × 1,61 = Notional × 1,84/(1 + 13,91\%)



Swap pré x DI de Notional = R$ 124.559.161 e taxa pré de 13,91% a. a. contra 100% do DI.

12. Considere os dados a seguir:

- Taxa pré para primeiro vencimento: 14% a. a.
- USD casado: R$ 11/USD 1.000

---

- Primeiro USD futuro: R$ 3.570/USD 1.000
- Dias corridos até o primeiro vencimento: 11
- Dias úteis até o primeiro vencimento: 7

Calcule:

a. Spot sintético.
b. Cupom cambial limpo.
c. Dado que o FRA entre 11 e 41 dias corridos é 1% a. a., calcule o cupom cambial para 41 dias corridos.
d. Se uma empresa tomar um empréstimo em USD para 41 dias corridos a 2,0% a. a., quanto representa esse empréstimo em % do CDI se a taxa pré para esse vencimento é de 14,50% a. a. e o prazo em dias úteis é 27?

# Solução

a. O mercado de USD casado é o chamado mercado de forward points, ou seja, quantos pontos existem entre a taxa forward de USD e a cotação à vista. Assim, o casado é dado pela diferença entre a cotação do primeiro futuro e do câmbio à vista:



{l}
Casado = f - S 

11 = 3.570 - S 

11 = 3.570 - S 





Dessa forma, o spot sintético (sintético porque deriva do mercado futuro de USD, que é um mercado de derivativos) é:

S = 3.559 reais por mil USD

b. A equação que relaciona o casado, a taxa pré, a taxa de USD spot e o cupom limpo é:



C = [ (1 + i)^(dn/353)/(1 + Casado/S) - 1 ] × 360/dc



Substituindo os valores, teremos:



C = [ (1 + 14\%)^(dn/353)/(1 + 11/3559) - 1 ] × 360/11 = 1.81\%  a. a.



c. A equação do FRA de cupom cambial da BM&F é:



[ 1 + FRC × (dc_2 - dc_1)/360 ] = (1 + C_2 dc_1/360)/(1 + C_1 dc_1/360)



Substituindo:



[ 1 + 1\% × (41 - 11)/360 ] = (1 + C_2 41/360)/(1 + 1,81\% 11/360)



---

C_2 = 1,22\% a. a.

d. A arbitragem que é usada para equalizar os spreads é fazer o preço do NDF ser igual para 100% do DI e para outros valores.



f/S = (1 + i_s)^(dn/252)/(1 + C_s × dc/360) = (1 + i)^(dn/252)/(1 + C × dc/360)



Onde o termo s significa aquele que tem um spread em relação ao benchmark da BM&F.

Substituindo:



(1 + i_s)^(27/252)/(1 + 2,0\% × 41/360) = (1 + 14,50\%)^(27/252)/(1 + 1,22\% × 41/360)



Da equação de arbitragem anterior, chega-se a uma taxa pré com spread de 15.45% a. a. Para achar o valor equivalente em percentual do CDI basta dividir a taxa com spread pela taxa de referência em 100% do DI.



\%cdi = (1 + 15,45\%)^(1/252) - 1/(1 + 14,50\%)^(1/252) - 1 = 106\%



---

# Referências

ASSOCIAÇÃO BRASILEIRA DAS ENTIDADES DOS MERCADOS FINANCEIRO E DE CAPITAIS – ANBIMA. Deliberação nº 3 do Conselho de Regulação e Melhores Práticas de Mercado Aberto. Iniciativa conjunta da ANBIMA, STN, Banco Central, CETIP e BM&FBovespa.

BANCO CENTRAL DO BRASIL – BACEN. Carta-Circular n. 3.498 de 2011 do Banco Central do Brasil.

BOLSA DE MERCADORIAS E FUTUROS – BM&F. Diretoria Técnica e de Planejamento Departamento Técnico e de Desenvolvimento de Produtos. Metodologia para a Apuração de Curvas de Preços e de Spreads Teóricos de Títulos Públicos. São Paulo, 2004.

CENTRAL DE CUSTÓDIA E LIQUIDAÇÃO FINANCEIRA DE TÍTULOS – CETIP. Caderno de Fórmulas: CDBs, DIs, DPGE, LAM, LC, LF, LFS, LFSC, LFSN, IECI e RDB. Rio de Janeiro: CETIP, 2017.

FABOZZI, F. J.; MANN, S. V. Introduction to Fixed Income Analytics. 2nd edition. Wiley: 2010.

HULL, J. C. Options, Futures, & Other Derivatives. 3rd ed. New Jersey: Prentice Hall, 1997.

HULL, J.; WHITE, A. LIBOR vs. OIS: the derivatives discounting dilemma. Journal of Investment Management, v. 11, n. 3, p. 14-27, 2012.

JORION, P. Value at Risk. 2. ed. São Paulo: BM&F, 2003.

MOLERO, L.; MELLO, E. Derivativos: negociação e precificação. 1. ed. São Paulo: Saint Paul Editora, 2018.

NELSON, C. R.; SIEGEL, A. F. Parsimonious modelling of yield curves. The Journal of Business, v. 60, n. 4, p. 473-489, Oct. 1987.

OHANIAN, G. Operações indexadas ao percentual do CDI: Precificação e Hedge Dinâmico usando o contrato DI futuro da BM&F. In: 5º Encontro Brasileiro de Finanças, São Paulo, 2005.

RiskMetrics Group. Longrun Technical Document. 1st ed, 1999b.

Technical Document. 1st ed, 1999a.

SVENSSON, L. E. O. Estimating and Interpreting Forward Interest Rates: Sweden 1992-1994. The National Bureau of Economic Research. NBER Working Paper Series 4871, 1994.

Bibliografia recomendada

---

BODIE, V.; ALEX, K.; MARCUS, A. J. Investimentos. 10. ed. Porto Alegre: Bookman, 2016.

COCHRANE, J. H. Asset pricing: revised edition. Princeton University Press: New Jersey, 2005.

DE PAULA, R. F. Gerenciamento do risco de taxa de juro em fundo de pensão: redesenhando estratégia de imunização com o uso de derivativos. Resenha BM&F. n. 149. São Paulo, 2003.

DIEBOLD, F. X.; LI C. Forecasting the term structure of government bond yields. Journal of Econometrics, 130, p. 337-364, 2006.

ELTON, E. J.; BROWN, S. J.; GOETZMANN, W. N.; GRUBER, M. J. Moderna teoria de carteiras e análise de investimentos. 1. ed. Rio de Janeiro: Campus-Elsevier, 2012.

FABOZZI F. J. Fixed income analysis. 2nd ed. Wiley: New Jersey, 2007.

_____. Mercados, análise e estratégias de bônus: títulos de renda fixa. Rio de Janeiro: Qualitymark, 2000.

FAMA, E. F. Forward and spot rates. Journal of Monetary Economics, 14, p. 319-338, Chicago, 1984.

FRANKEL, J. A. "Quantifying international capital mobility in the 1980's". In: BERNHEIM, B. D.; SHOVERS, J. B. (Eds.). National Saving and Economic Performance, National Bureau of Economic Research, The University of Chicago Press, Chicago, 1991.

GARCIA, M. G. P. A macroeconomia do dólar futuro. Resenha BM&F, n. 118, p. 37-45, São Paulo, 1997.

HAYT, G.; SONG, S. Handle with sensitivity. Risk Magazine, v. 8, n. 9, p. 94-99, 1995.

HULL J. C. Options, futures, and other derivatives. 10th ed. Pearson: London, 2017.

LA ROCQUE, E.; LOWENKRON, A.; AMADEO, E.; JENSEN J. Cenários probilísticos: conjugando análise de riscos e projeção macroeconômica. Artigo Técnico Risk Control – Tendências, 2003.

LUENBERGER, D. G. Investment science. New York: Oxford University Press, 1998.

PHILIPPON, T.; ZETTELMEYER, J.; BORENSZTEIN, E. Monetary independence in emerging markets: does the exchange rate regime make a difference?. In: IMF Working Paper, Jan. 2001.

SECURATO, J. R. Cálculo financeiro das tesourarias: bancos e empresas. 3. ed. São Paulo: Saint Paul Editora, 2005.

SILVA, M. E.; MAIALI, A. C. Dimensão da duração e da convexidade. Resenha BM&F, n. 149, v. 83, 2002.

SUEN, A. S.; KIMURA, H.; NONAKA, K. P. A utilização do modelo da Duration na administração do risco de taxas de juros em carteiras de renda fixa em bancos brasileiros. In: Caderno de pesquisas em Administração. São Paulo: FEA/USP, v. 2, n. 1, 1997.

---

VARGA, G. Duração, convexidade e imunização. Resenha BM&F. p. 23-32, set. 1993.

VIEIRA NETO, C. A.; URBAN, F. Um modelo de teste de stress menos subjetivo e mais abrangente. Resenha BM&F, n. 139, p. 31-59, 2000.

WINKLEVOSS, H. E. Pension Mathematics with numerical illustrations. Philadelphia: University of Pennsylvania Press, 1993.

---

# Apêndice A

Neste tópico, contém algumas provas e demonstrações rápidas de conceitos e fórmulas vistos ao longo do texto.

## A.1 Conceito de total return pelas quotas

De acordo com o critério indicado, o retorno entre o período t e t + 1 é dado por:



T R_(t, t + 1) = [ P_(t + 1)/P _t Q_(t + 1)/Q _t ] - 1 tag {A}



A quantidade de quotas em t + 1 é dada por:



Q_(t + 1) = Q _t + D_(t + 1)/P_(t + 1) Q _t tag {B}



Onde o termo D_(t+1) refere-se aos fluxos de caixa oriundos da posse desse ativo, como cupons de juros sobre títulos de renda fixa ou dividendos sobre ações, por exemplo.

Substituindo (B) em (A), teremos:



T R_(t, t + 1) = [ P_(t + 1)/P _t Q _t + D_(t + 1)/P_(t + 1) Q _t/Q _t ] - 1



Desenvolvendo:



T R_(t, t + 1) = [ P_(t + 1)/P _t Q _t (1 + D_(t + 1)/P_(t + 1))/Q _t ] - 1





T R_(t, t + 1) = [ P_(t + 1) (1 + D_(t + 1)/P_(t + 1))/P _t ] - 1





T R_(t, t + 1) = [ P_(t + 1) + D_(t + 1)/P _t ] - 1



Ou seja, o retorno diário pelo conceito de quotas é exatamente equivalente ao conceito financeiro.

Para que o conceito valesse em um período mais extenso, entretanto, seria necessário que os valores financeiros obtidos com o ativo (seja ele títulos ou ações) fosse reinvestido em aquisição de frações de mais ativos iguais.

---

# A.2 Duration do portfólio em função da duration dos títulos que o compõem

Vamos assumir um portfólio de valor a mercado V, composto por dois papéis, de preços P1 e P2, conforme equação a seguir:



V(y_1, y_2) = P_1(y_1) + P_2(y_2)



Diferenciando em relação a y:



dV = ∂ V/∂ y_1 × dy_1 + ∂ V/∂ y_2 × dy_2



Que resulta em:



dV = -1/(1 + y_1) × Σ(k=1 até n) FC_1^k × du_k/252/(1 + y_1)^(du_k/252) × dy_1 + -1/(1 + y_2) × Σ(k=1 até n) FC_2^k × du_k/252/(1 + y_2)^(du_k/252) × dy_2



Dividindo tudo por V:




dV = & -1/(1 + y_1) × Σ(k=1 até n) FC_1^k × du_k/252/(1 + y_1)^(du_k/252) × dy_1 + -1/(1 + y_2) × Σ(k=1 até n) FC_2^k × du_k/252/(1 + y_2)^(du_k/252) × dy_2 

& dV/V = -1/(1 + y_1) × 1/V × Σ(k=1 até n) FC_1^k × du_k/252/du_k/252 × dy_1 + -1/(1 + y_2) × 1/V × Σ(k=1 até n) FC_2^k × du_k/252/(1 + y_2)^(du_k/252) × dy_2




Multiplicando a primeira parcela por P1/P1 e a segunda por P2/P2:




dV/V = & -1/(1 + y_1) × P_1/V × Σ(k=1 até n) FC_1^k × du_k/252/du_k/252 × dy_1 + -1/(1 + y_2) × P_2/V × Σ(k=1 até n) FC_2^k × du_k/252/du_k/252 × dy_2 

dV/V = & -1/(1 + y_1) × P_1/V × Σ(k=1 até n) P_1^k × du_k/252/P_1 × dy_1 + -1/(1 + y_2) × P_2/V × Σ(k=1 até n) P_2^k × du_k/252/P_2 × dy_2 

dV/V = & -1/(1 + y_1) × P_1/V × M_1 × dy_1 + -1/(1 + y_2) × P_2/V × M_2 × dy_2




Para S'(x)_0 = S'(x)_1^2:



1/V dV/dy = D = w_1 × D_1 + w_2 × D_2



Ou seja, a duration de um portfólio é igual a duration dos títulos que o compõem, ponderadas pelo valor presente dos títulos em relação ao valor presente total desse portfólio.

O raciocínio para a convexidade é análogo, logo, a equação que relaciona as

---

convexidades dos títulos individuais com a convexidade total da carteira é:



C = w ₁ × C ₁ + w ₂ × C ₂



## A.3 Hedge de um portfólio com *duration* e convexidade

Assim, para hedgear um portfólio, considerando os efeitos de segunda ordem (curvatura da função P = P(y)), basta resolver o sistema de equações:



w ₁ × D ₁ + w ₂ × D ₂ = D *





w ₁ × C ₁ + w ₂ × C ₂ = C *



Onde as incógnitas são os pesos W₁ e W₂ e os dados são os termos D₁, D₂, C₁, C₂ referentes aos contratos derivativos de taxas de juros que serão usados e os termos C₁^*D^*, característica da carteira a ser protegida.

Uma vez conhecidas as variáveis W₁ e W₂, chega-se à quantidade de contratos:



w = P U × Q/V



Onde PU é o preço do contrato de DI, Q a quantidade a ser negociada e V é o valor presente do portfólio a ser protegido.

## A.4 Capitalização contínua

Supondo um título global emitido pela República Federativa do Brasil, a frequência de capitalização deste é duas vezes por ano, porém ela não acontece exponencialmente, e sim linearmente. Para simplificar, calcularemos o valor futuro de um título ou empréstimo que se valoriza da mesma forma:



V F = V A (1 + r/f)^(f r)



Onde:

- VF: valor futuro do papel
- VA: valor atual do papel
- r: taxa de juros expressa em % a. a., capitalizada linearmente pela frequência f
- f: frequência de capitalização do papel em vezes por ano

---

t: período do cálculo em anos

A capitalização contínua consiste em fazer a frequência de capitalizações tender ao infinito.

Assim, pode-se fazer uma mudança de variáveis:



1/x = r/f





f = r x



Quando f→ ∞. xrightarrow ∞, logo:



V F = V A × lim_(x rightarrow ∞) [(1 + 1/x) ^x ]^(r x) = V A × e^(r x)



Que é conhecida como capitalização contínua e tem uma utilidade muito grande em Finanças.

## A.5 Valorização de fundos de investimento

Os fundos de investimento têm algumas nuances interessantes do ponto de vista do cálculo de renda fixa; a taxa de administração é uma delas.

Supondo um fundo de renda fixa que tenha o valor inicial dado por V₀ e a quantidade de quotas q, o valor dos ativos no dia seguinte será dado por:



V ₁ = q × V ₀ (1 + i ₁) - V ₁ × txadm/252



Como podemos observar da equação anterior, o valor da taxa de administração é provisionado diariamente de maneira linear.

Da equação anterior já é possível se obter uma relação interessante. Isolando V₁ na parte esquerda da equação, teremos:



V ₁ (1 + txadm/252) = q × V ₀ (1 + i ₁)



Dividindo por V₀, teremos:



V ₁/V ₀ = q × (1 + i ₁)/(1 + txadm/252)



Podemos definir uma rentabilidade diária líquida que será:



r_(i i q) = V ₁/V ₀ - 1 = q × (1 + i ₁)/(1 + txadm/252) - 1



---

Supondo que não entraram nem saíram cotistas (por isso o termo q constante). Esse termo é a variação do valor da cota que costumava sair em jornais de grande circulação antigamente.

Repetindo a conta para o dia seguinte, teremos:



V_2 = q × V_1 (1 + i_2) - V_2 × txadm/252



E, por extensão:



V_3 = q × V_2 (1 + i_3) - V_3 × txadm/252  e assim por diante.



Para expressar V_2 como função de V_0 temos de executar um raciocínio equivalente àquele do cálculo da taxa líquida:



V_1/V_0 = q × (1 + i_1)/(1 + txadm/252)





V_2/V_1 = q × (1 + i_2)/(1 + txadm/252)



E multiplicar as duas expressões anteriores:



V_1/V_0 × V_2/V_1 = q × (1 + i_1)/(1 + txadm/252) × q × (1 + i_2)/(1 + txadm/252)



Com isso, conseguimos calcular o rendimento acumulado no período 0-2:



r_(0-2) = V_2/V_0 - 1 = q^2 (1 + i_1)(1 + i_2)/(1 + txadm/252)^2 - 1



Sem perda de generalidade, podemos estender o raciocínio para o período n qualquer:



r_(0-n) = V_0/V_0 - 1 = ∏(k=0 até n) q_k × ∏(k=1 até n) (1 + i_k)/(1 + txadm/252)^n - 1



Que é a rentabilidade líquida de um fundo de investimento em função da rentabilidade diária das cotas e sua quantidade.

Assumindo rentabilidades diárias iguais a um valor i e mesma quantidade de cotas do princípio ao prazo n, teremos:



r_(0-n) = V_0/V_0 - 1 = ∏(k=0 até n) q_k × ∏(k=1 até n) (1 + i_k)/(1 + txadm/252)^n - 1 = q^n (1 + i)^n/(1 + txadm/252)^n - 1



Que é a rentabilidade líquida no período de n dias úteis desse fundo de investimento.

---

As alíquotas de IR são pagas em quotas, logo, o valor da rentabilidade das cotas não é influenciado pelo pagamento do imposto de renda semestral, o famoso "come-cotas".

A expressão anterior pode ser escrita em função da taxa de rentabilidade média anual do fundo em vez da diária.



r_(b-n) = V_n/V_a - 1 = ∏(k=0 até n) q_k × ∏(k=1 até n) (1 + i_k)/(1 + txadm/252)^n - 1 = q^n (1 + i_n)^(n/252)/(1 + txadm/252)^n - 1



Para uma quantidade de cotas constante (sem entrada de novos recursos, resgates ou amortizações), teremos:



(1 + r)^(n/252) = (1 + i_n)^(n/252)/(1 + txadm/252)^n



Desenvolvendo:



(1 + i_n)^(n/252) = (1 + r)^(n/252) (1 + txadm/252)^n





i_n = [ (1 + r)^(n/252) (1 + txadm/252)^n ]^(252/n) - 1





i_n = (1 + r) (1 + txadm/252)^(252) - 1



Assim, um fundo que rendeu 8% a. a. líquidos em um ano com uma taxa de administração de 2% a. a., teve rentabilidade dos ativos de:



i_n^(48) = (1 + 8\%) (1 + 2\%/252)^(252) - 1 = 10.18\%  a. a.



## A.6 Imposto de renda em fundo de investimento

Como o imposto de renda em fundos de investimento é calculado sobre as quotas, a álgebra para realizar a conta muda um pouco.

O patrimônio líquido do fundo vai crescer da seguinte forma:



PL_t = PL_(t-1)(1 + r_t) - IR_t



O patrimônio líquido, por sua vez, pode ser escrito como o produto da quantidade de quotas pelo valor da quota.



q_t V_t = q_(t-1) V_(t-1)(1 + r_t) - q_(t-1) aliq IR[V_t - V_(ant)]



---

Onde V_(ant) é o valor da quota quando do último recolhimento do imposto de renda.

Dividindo tudo por V_t, temos:



q_t = q_(t-1) V_(t-1) (1 + r_t)/V_t - q_(t-1) a l i q I R [V_t - V_(ant)]/V_t



Desenvolvendo:



q_t = q_(t-1) (1 + r_t)/(1 + r_t) - q_(t-1) a l i q I R (1 - V_(ant)/V_t)





q_t = q_(t-1) - q_(t-1) a l i q I R (1 - V_(ant)/V_t)



Ou seja, a quantidade de quotas vai diminuir no valor dado pela segunda parte da expressão anterior se essa for positiva. Em fundos multimercado pode não ser, então, a melhor expressão seria escrita como:



q_t = q_(t-1) [ 1 - min (0, a l i q I R (1 - V_(ant)/V_t)) ]



## A.7 Gross up de imposto de renda em fundos de investimento

Pode ser interessante para análise de fundos ter uma ideia de como foi seu desempenho médio eliminando da conta a remuneração do gestor do fundo (taxa de administração) e o imposto de renda, para ter um critério de comparação que simule o valor dos ativos da carteira.

O imposto de renda de fundos de renda fixa e multimercado no Brasil é cobrado, semestralmente, em forma de quotas, ou seja, em duas datas distintas no primeiro e no segundo semestre o fundo recolhe quotas à Receita Federal do Brasil.

Vamos admitir que este processo ocorra diariamente:



P L_t = P L_(t-1) - I R_t



Observe que o imposto é cobrado sobre a quota de hoje, ou seja, "por dentro", segundo o jargão do mercado.

Como vamos calcular uma taxa de provisionamento média ao longo do tempo, não é necessário o uso de quotas para cálculo do valor dos ativos, logo:

---



V_n = V_0 (1 + r)^n - x (V_n - V_0)



Onde:

V_0: valor dos ativos do fundo (menos a taxa de administração) no dia 0
x: valor da alíquota de IR
r: taxa de valorização (líquida de taxa de administração) do fundo

Desenvolvendo:



V_n (1 + x) = V_0 [ (1 + r)^n + x ]





V_n/V_0 = [ (1 + r)^n + x]/(1 + x)



Definindo a taxa x_2 como líquida de imposto de renda, teremos:



1 + r_L = V_n/V_0 = [ (1 + r)^n + x]/(1 + x)



Como estamos interessados na taxa bruta de IR, isolamos r:



(1 + r)^n + x = (1 + r_L)^n (1 + x)





(1 + r)^n = (1 + r_L)^n (1 + x) - x



Colocando em base anual/252:



(1 + r)^(n/252) = (1 + r_L)^(n/252) (1 + x) - x





r = [ (1 + r_L)^(n/252) (1 + x) - x ]^(252/n) - 1



Um fundo que tem rentabilidade líquida de IR de 9% a. a. no último ano e paga alíquota de IR de 15% teve a rentabilidade proporcionada pelos seus ativos (menos a remuneração do gestor) de, aproximadamente:



r = [ (1 + 9\%)^(252/252) (1 + 15\%) - 15\% ]^(252/252) - 1 = 10.35\%  a. a.



## A.8 Butterfly com futuros de DI ou trava de FRA de três pontas

Uma estratégia interessante que pode ser executada com contratos futuros de DI é a conhecida como fly de três pontas. Essa estratégia busca ganhar com alterações na convexidade do portfólio composto por três futuros de DI, que são hedgeados em primeira ordem com a duration modificada e autofinanciados, ou seja, a soma dos valores a mercado é nula.

---

Assim, o trader acredita que a curva vai alterar sua inclinação relativa entre os vencimentos solicitados, mas a variação nas taxas de juros será de forma paralela.

Supondo três derivativos 1, 2 e 3, teremos os inputs:

- Três taxas de juros t_1,t_2,t_3 em % a. a.
- Três vencimentos t_1,t_2,t_3 em dias úteis
- A quantidade de contratos de referência do terceiro DI, Q_3

A partir deles, podemos calcular:

- Três PUs: PU_1, PU_2, PU_3
- Três durations modificadas: D_1, D_2, D_3

E, finalmente, as quantidades Q_1, Q_2 que resolvem o problema juntamente com Q_3.

Resolvendo:

Para cada DI teremos a duration modificada dada por:



D = T/252 × 1/(1 + i)



E os PUs dados por:



PU = 100.000/(1 + i)^(T/252)



As restrições do problema são:

D_1Q_1 + D_2Q_2 + D_3Q_3 = 0, ou seja, risco de taxas de juros de primeira ordem igual a zero.

PU_1Q_1 + PU_2Q_2 + PU_3Q_3 = 0, ou seja, o MtM = 0.

Como Q_3 é dado, teremos:



 D_1 & D_2 
 PU_1 & PU_2   Q_1 
 Q_2  =  -D_3Q_3 
 -PU_3Q_3 



Que pode ser resolvida pela Regra de Kramer para sistemas lineares:




Q_1 &= (-Q_3D_3PU_2 + D_2PU_3Q_3)/(D_1PU_2 - PU_1D_2) 

Q_2 &= (-Q_3D_1PU_3 + D_3PU_1Q_3)/(D_1PU_2 - PU_1D_2)




---

O resultado será o derivativo ao centro com valor negativo em relação aos derivativos dos extremos.

Como exemplo, indicaremos a situação a seguir:

![img-58.jpeg](img-58.jpeg)
Fonte: Elaborado pelos autores.

Se acreditamos que a taxa de juros para o período intermediário vai aumentar e as taxas das extremidades vão cair, estamos assumindo que a curvatura da ETTJ está se alterando.

A trava (butterfly) de 3 pernas é a operação que se utiliza para arbitrar essa situação. Vamos às contas:

Usando as equações anteriores, teremos:

|  Dias úteis | Taxa a. a. | PU | D (anos)  |
| --- | --- | --- | --- |
|  46 | 7,28% | 8.725,28 | 0,1702  |
|  296 | 7,27% | 2.087,38 | 1,0950  |
|  549 | 8,25% | 84.138,81 | 2,0125  |

Para uma quantidade de contratos Q₃ = 1000, teremos:



[ {cc} 0,1702 & 1,0950 
 98.725,28 & 92.087,38  ] [ {c} Q₁ 
 Q₂  ] = [ {c} -170,1510 
 -1094,9969  ]



Os valores de Q₁ e Q₂ são tais que:



[ {c} Q₁ 
 Q₂  ] = [ {cc} 0,1702 & 1,0950 
 98.725,28 & 92.087,38  ]^(-1) [ {c} -170,1510 
 -1094,9969  ]



Que resulta em:



[ {c} Q₁ 
 Q₂  ] = [ {c} 1.008 
 -1.995  ]



Assim, para apostar em um aumento na taxa intermediária com diminuição das taxas nas extremidades, temos de comprar 1.995 contratos futuros de DI vencendo em 296 dias úteis, vender 1.008 contratos futuros, vencendo

---

em 46 dias úteis e vender 1.000 contratos futuros vencendo em 549 dias úteis.

Os valores da estratégia antes e depois de um movimento genérico da curva são:

|  Antes  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
|  Dias úteis | Taxa a. a. | Variação p. p. | PU | MtM | Resultado  |
|  46 | 7,28% | 0,00 | 98.725,28 | 99.540.353 | 0,00  |
|  296 | 7,27% | 0,00 | 92.087,38 | -183.679.160 | 0,00  |
|  549 | 8,25% | 0,00 | 84.138,81 | 84.138.807 | 0,00  |
|  Depois  |   |   |   |   |   |
|  Dias úteis | Taxa a. a. | Variação p. p. | PU | MtM | Resultado  |
|  46 | 7,28% | -0,10 | 98.743,10 | 99.557.301 | 16.947  |
|  296 | 7,27% | 0,10 | 91.986,65 | -183.478.236 | 200.924  |
|  549 | 8,25% | -0,10 | 84.308,39 | 84.308.388 | 169.581  |
|  Total: |   |   |   |   | 387.453  |

Fonte: Elaborado pelos autores.

![img-59.jpeg](img-59.jpeg)
Movimento curva

Fonte: Elaborado pelos autores.

Um fato importante a destacar é que, embora a trava seja desenhada para não apresentar resultado para deslocamentos paralelos da curva de juros, isso pode acontecer com a modelagem utilizada, no exemplo:

|  Depois  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
|  Dias úteis | Taxa a. a. | Variação p. p. | PU | MtM | Resultado  |
|  46 | 7,28% | 0,20 | 98.692,73 | 99.506.515 | -33.838  |
|  296 | 7,27% | 0,20 | 91.886,12 | -183.277.718 | 401.442  |
|  549 | 8,25% | 0,20 | 83.801,13 | 83.801.134 | 337.673  |
|  Total: |   |   |   |   | 29.931  |

---

Fonte: Elaborada pelos autores.

## Movimento curva

![img-60.jpeg](img-60.jpeg)

Fonte: Elaborado pelos autores.

Há uma maneira de corrigir o efeito visto. Ele ocorre porque forçamos a soma dos preços dos derivativos a ir para zero e quando derivamos o valor do portfólio, estamos partindo de um valor P diferente de zero.

Para corrigir, podemos fazer a conta com o DV01 ou usando, simplesmente, a noção de derivada do preço em relação à taxa de juros, dP/dy, evitando, assim, o cálculo da elasticidade, que é o conceito básico de duration, mas sem perder a generalidade de ter a sensibilidade do papel a alterações na taxa de juros.

Assim, criaremos uma variável DV que é a duration em valor:



P = 100.000/(1 + y)^(T/252) = 100.000 × (1 + y)^(T/252)



A derivada será:



DV = dP/dy = 100.000/(1 + y)^(T/252 + 1) × T/252



Cada derivativo terá a nova duration calculada dessa maneira na resolução do sistema linear.

O vetor com as quantidades será:



[ {l} Q_1 
 Q_2 
 Q_3  ] = [ {l} 846 
 -1820 
 1000  ]



E teremos para um deslocamento paralelo de 50 pontos base:

|  Antes  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
|  Dias úteis | Taxa a. a. | Variação p. p. | PU | MtM | Resultado  |

---

|  46 | 7,28% | 0,00 | 98.725,28 | 99.540.353 | 0,00  |
| --- | --- | --- | --- | --- | --- |
|  296 | 7,27% | 0,00 | 92.087,38 | -183.679.160 | 0,00  |
|  549 | 8,25% | 0,00 | 84.138,81 | 84.138.807 | 0,00  |

Depois

|  Dias úteis | Taxa a. a. | Variação p. p. | PU | MtM | Resultado  |
| --- | --- | --- | --- | --- | --- |
|  46 | 7,28% | 0,50 | 98.642,52 | 83.471.597 | -70.883  |
|  296 | 7,27% | 0,50 | 91.585,75 | -166.801.556 | 913.607  |
|  549 | 8,25% | 0,50 | 83.331,70 | 83.331.704 | 840.980  |

Total: 1.745

Fonte: Elaboradas pelos autores.

Movimento curva
![img-61.jpeg](img-61.jpeg)
Fonte: Elaborado pelos autores.

# Exemplo para conceito de preço teórico de não arbitragem

Imagine que alguém está negociando (comprando) contratos de dólar futuro por um valor superior ao valor indicado pela equação:



f_(Mismatch) > f_(US\) = S × (1 + i)^(d u/2 5 2)/(1 + C × d c/3 6 0)



Um operador pode realizar a seguinte operação:

a) Vender contratos de USD futuro para esse operador por esse valor, f_(Mismatch)
b) Comprar USD 1 à vista. O recurso para isso vem da operação a seguir.
c) Tomar USD 1 vezes S (taxa de câmbio em R por USD) emprestado no mercado financeiro brasileiro, ao custo de i% a. a.
d) Para não deixar o USD 1 parado, investir em taxa de juros em USD, o cupom cambial C.

Essa estratégia vai gerar um lucro em R no vencimento dado por:

---



L = -S × (1 + i)^(du/252) + 1 × (1 + C × dc/360) × S_T



Onde o valor S_T é o valor da taxa de câmbio (variável aleatória) observada no instante T.

Da mecânica operacional do mercado de derivativos, sabemos que, não importando o que ocorra com a taxa de câmbio em T, o valor do ajuste da venda de USD futuro faz com que a liquidação da operação no vencimento seja realizada com f_(Mismatch), independentemente do valor de S_T.

Assim, o valor de L fica:



L = -S × (1 + i)^(du/252) + 1 × (1 + C × dc/360) × f_(Mismatch)



Como f_(Mismatch) > f_(US), pela equação anterior é possível perceber que existe um lucro de arbitragem sem risco na estratégia. Sendo assim, os agentes vão realizar os passos de a) a d) seguidamente para obter esse ganho sem risco, o que faz com que:

a) f_(Mismatch) caia
b) S suba
c) i suba
d) C caia

Até que o lucro sem risco desapareça, ou seja, tenda a zero:



L = -S × (1 + i)^(du/252) + 1 × (1 + C × dc/360) × f_(Mismatch) rightarrow 0



Rearranjando a expressão:



f_(Mismatch) = f_(US) = S × (1 + i)^(du/252)/(1 + C × dc/360)



E o mercado de USD futuro converge para o equilíbrio pela equação de não arbitragem.

48 O cálculo está sujeito a imprecisões, porque estamos assumindo que r é constante, mas, na verdade, não é o caso, dado que o valor provisionado em taxa de administração varia diariamente.

---

# Glossário com termos traduzidos do inglês

Como boa parte da teoria financeira foi e é desenvolvida nos Estados Unidos, é importante saber os termos em inglês discutidos neste texto para facilitar o estudo posterior dos temas aqui abordados.

A seguir, elaboramos uma lista não exaustiva de termos técnicos e acadêmicos relacionados ao tema de renda fixa e derivativos de taxas de juros:

- Asset class: classe de ativo
- Asset: ativo
- Bonds: títulos
- Convexity: convexidade
- Derivatives: derivativos
- Duration: duração (prazo)
- Equity: ações (classe de ativo)
- Exposure: exposição
- Financial instruments: instrumentos financeiros
- Fixed income: renda fixa
- Forward premium: prêmio futuro
- Futures: futuros
- Hedge: hedge, proteção
- Interest rate: taxa de juros
- Internal Rate of Return (em projetos) e Yield to Maturity (para títulos): Taxa Interna de Retorno (TIR)
- Liability: passivo

---

- Long term: longo prazo
- Long: posição comprada, posição ativa
- Notional: valor de referência de um contrato de derivativos
- Off-balance: contas de compensação, só impactam as contas de resultado, não sendo evidenciadas no balanço patrimonial. É o caso dos derivativos, como swaps e futuros.
- Offset: compensar, contrabalançar
- Options: opções (stock options: sobre ações, fx options: sobre taxa de câmbio, interest rate options: sobre taxas de juros)
- Payoff: resultado líquido de uma operação, normalmente um derivativo
- Portfolio: portfólio, carteira
- Return: retorno (entre períodos em um ativo financeiro)
- Securities: papéis
- Short term: curto prazo
- Short: posição vendida, posição passiva
- Stocks: ações (em si)
- Swaps: swaps
- Tenor: vencimento
- Total return: retorno total
- Underlying asset: ativo subjacente ou ativo objeto
- Unwind: relaxar
- Volatility: volatilidade
- Yield: rendimento (implícito em um papel)
- Yield curve, term structure of interest rates: curva de juros, estrutura a termo de taxas de juros

---

Saint Paul Editora

Conteúdo em Administração, Contabilidade e Economia

# CONFIRA OUTROS TÍTULOS DA SAINT PAUL EDITORA

![img-62.jpeg](img-62.jpeg)

## DERIVATIVOS
NEGOCIAÇÃO E PRECIFICAÇÃO
Eduardo Morato Mello e
Leonel Molero Pereira

##
