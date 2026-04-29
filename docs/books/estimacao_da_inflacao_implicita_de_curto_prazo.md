---
title: "Estimacao_Da_Inflacao_Implicita_De_Curto_Prazo"
source_pdf: "Estimacao_da_Inflacao_Implicita_de_Curto_Prazo.pdf"
converter: "mistral-ocr-latest"
date_converted: "2026-03-27T18:26:19Z"
pages: 24
category: "books"
sanitized: true
reviewed: false
---
Estimação da Inflação Implícita de Curto Prazo
(Estimation of Implicit Short-Term Inflation)

Gustavo Silva Araújo *
José Valentim Machado Vicente **

Resumo

A inflação implícita é a diferença entre as taxas de juros nominal e real. No mercado brasileiro, ela pode ser obtida facilmente a partir de títulos públicos prefixados e indexados à inflação. No entanto, quando tratamos da inflação implícita de curto prazo, tal tarefa apresenta duas dificuldades: a) os títulos indexados à inflação possuem defasagem de indexação; b) a sazonalidade da inflação implica sazonalidade da taxa real. O objetivo deste trabalho é propor uma metodologia para estimação da inflação implícita de curto prazo que trate desses dois problemas. Assumindo que o prêmio de risco da inflação é pequeno no curto prazo, avaliamos a capacidade de previsão da inflação implícita confrontando-a com expectativas baseadas em pesquisas. Os resultados mostram que a inflação implícita é competitiva em relação às previsões de analistas de mercado divulgadas no Boletim Focus. Uma vantagem da inflação implícita é o fato de ela permitir um acompanhamento mais estreito das expectativas do que as pesquisas, uma vez que ela é atualizada continuamente.

Palavras-chave: Inflação Implícita, Previsão de Inflação IPCA, DAP, NTN-B.
Códigos JEL: E31, E43, E44.

Submetido em 26 de maio de 2017. Reformulado em 14 de agosto de 2017. Aceito em 8 de setembro de 2017. Publicado on-line em 18 de julho de 2017. O artigo foi avaliado segundo o processo de duplo anonimato além de ser avaliado pelo editor. Editor responsável: Marcio Laurini.

* Banco Central do Brasil e IBMEC-RJ, Rio de Janeiro, RJ, Brasil. E-mail: 00araujogs@gmail.com
** Banco Central do Brasil e IBMEC-RJ, Rio de Janeiro, RJ, Brasil. E-mail: jose.valentim@bcb.gov.br

Rev. Bras. Finanças (Online), Rio de Janeiro, Vol. 15, No. 2, June 2017, pp. 227-250
ISSN 1679-0731, ISSN online 1984-5146
©2017 Sociedade Brasileira de Finanças, under a Creative Commons Attribution 3.0 license - http://creativecommons.org/licenses/by/3.0

---

Araújo, G. S., Vicente, J. V. M.

# Abstract

Implicit inflation or break-even inflation rate (BEIR) is the difference between nominal and real interest rates. In the Brazilian market, we can obtain it from indexed government bonds. However, when dealing with short-term BEIR, this task presents two difficulties: a) inflation-indexed bonds have indexation lags; b) inflation seasonality implies real interest rate seasonality. The aim of this paper is to propose a methodology to estimate the short-term BEIR that addresses these two issues. Assuming a negligible inflation risk premium in the short run, we evaluate the predictive ability of the BEIR by confronting it with expectations based on the market analysts' forecasts published on the Focus Survey. The results show that the BEIR is competitive when compared to the Focus Survey. An advantage of the BEIR is that it allows monitoring of expectations better than surveys, since it is continuously updated.

Keywords: Implicit Inflation, Inflation Forecasts, IPCA, DAP, NTN-B.

# 1. Introdução

A inflação implícita é a diferença entre as taxas de juros nominal e real. No mercado brasileiro, ela pode ser obtida facilmente a partir de títulos públicos prefixados (LTN e NTN-F) e indexados à inflação (NTN-B). No entanto, quando tratamos da inflação implícita de curto prazo, tal tarefa apresenta duas dificuldades. Primeiramente, as NTN-Bs possuem uma defasagem de indexação: elas vencem no décimo quinto dia do mês, porém são corrigidas pela inflação (IPCA) até o mês anterior. Em segundo lugar, a sazonalidade da inflação implica sazonalidade da taxa real. Portanto, a inflação implícita não é necessariamente *flat* até o vértice mais curto disponível. O objetivo desse trabalho é propor uma metodologia para estimação da inflação implícita de curto prazo que trate desses dois problemas.

A motivação para a estimação da inflação implícita de curto prazo reside no fato de que ela é um bom previsor da inflação futura, sendo, portanto, de extrema utilidade para bancos centrais e participantes do mercado financeiro. A inflação implícita representa a expectativa de inflação no mundo neutro ao risco. Ela pode ser decomposta da seguinte forma (veja Vicente e Graminho, 2015):

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

B

---

Estimação da Inflação Implícita de Curto Prazo

Inflação Implícita = Expectativa de Inflação + Prêmio de Risco da Inflação - Prêmio de Liquidez + Convexidade.

O prêmio de liquidez é uma compensação pela diferença de liquidez entre os ativos nominais e reais. Já o termo de convexidade é apenas uma correção matemática advinda da transformação de preços em taxas via uma função convexa. Vicente e Graminho (2015) mostraram que o prêmio de liquidez e o termo de convexidade são desprezíveis no mercado brasileiro. O prêmio de risco da inflação é uma remuneração exigida pelos investidores de títulos nominais como proteção contra perdas reais do valor pago por esses títulos. Como a incerteza em relação ao índice de preço futuro é baixa no curto prazo, espera-se que o prêmio de risco da inflação também seja pequeno para horizontes curtos. Uma vasta literatura demonstra empiricamente essa hipótese (veja, por exemplo, Vicente e Guillén (2013) ou Kubudi e Vicente (2016)). Portanto, a inflação implícita de curto prazo pode ser usada como um indicador da variação de preços no futuro próximo.

O mercado financeiro brasileiro possui ativos que permitem negociar a inflação implícita. Por exemplo, um investidor pode assumir uma posição comprada em inflação via a compra de uma NTN-B casada com a venda de uma LTN de prazo correspondente. Já a venda de inflação pode ser obtida invertendo as operações nos títulos públicos. Recentemente, a bolsa de valores brasileira passou a oferecer contratos futuros de cupom de IPCA (o código de negociação na bolsa é DAP). O cupom de IPCA é a taxa de juros embutida na NTN-B. O DAP facilitou a negociação de inflação futura uma vez que eliminou a operação de venda do título público a qual restringia o mercado a poucos investidores.¹ No entanto, características contratuais e especificidades do mercado impedem a estimação direta da inflação de curto prazo a partir tanto do DAP quanto das NTN-Bs.

Índices de inflação são calculados em base mensal e com atraso. O IPCA de um dado mês é publicado até o dia 15 do mês seguinte. Portanto, taxas de instrumentos indexados ao IPCA não representam perfeitamente taxas de juros reais. Evans (1998) propõe um método para correção da defasagem. A taxa real é igual à diferença entre a taxa dos títulos indexados

¹ Por exemplo, com a compra de contratos futuros de D1 e venda de contratos de DAP, o investidor assume uma posição comprada em inflação.

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.

à inflação e a taxa nominal a termo do período de defasagem acrescida de uma compensação. Essa compensação é dada pela covariância entre a inflação futura e a variação dos preços dos títulos nominais. Logo, o processo de obtenção da taxa real se resume ao cálculo dessa covariância. Evans (1998) estima a compensação via um vetor autoregressivo entre a inflação e os preços dos títulos.

Neste artigo, nós propomos uma solução alternativa e mais simples para contornar o problema da defasagem. Em vez de corrigir as taxas reais pelo período de defasagem, nós consideramos como variável de interesse a inflação acumulada entre o último mês que se conhece o IPCA e o mês anterior ao vencimento da NTN-B. Por exemplo, no dia 07/12/2016 a NTN-B de prazo mais curto era a com vencimento em 15/05/2017. O último IPCA divulgado era o de outubro de 2016. Portanto, essa NTN-B negociava a inflação entre novembro de 2016 e abril de 2017. Assim, embora a data de negociação do título seja 07/12/2016, o primeiro vértice observado da curva de inflação implícita se refere à taxa acumulada entre 01/11/2016 e 30/04/2017. Uma característica da inflação implícita extraída dessa maneira é o fato de lidarmos diretamente com os instrumentos que negociam inflação, sem utilizarmos taxas interpoladas. Portanto, não estamos sujeitos a erros de ajuste das curvas, que podem ser uma fonte de imprecisão para estimação da inflação de curto prazo.

A inflação implícita extraída até o primeiro vértice não deve ser distribuída mensalmente de maneira uniformemente por duas razões. A primeira é que, a taxa de inflação mensal apresenta sazonalidade. No início e no fim do ano os índices de preço apresentam variações maiores do que no meio do ano. Como a taxa nominal é aproximadamente fixa no curto prazo, essa sazonalidade deve ser transmitida para a taxa real. Portanto, no exemplo anterior, a inflação implícita extraída entre outubro de 2016 e abril de 2017 deve ser dividida mensalmente de forma ponderada tomando como pesos alguma medida da sazonalidade. Entretanto, se distribuirmos essa inflação somente pela sazonalidade, esse ajuste ficaria incompleto, uma vez que não incorporaria as informações de especialistas sobre eventos que podem influenciar a inflação de curto prazo. Dessa forma, visando contemplar não somente a sazonalidade, mas também informação corrente sobre a inflação, nós calculamos os pesos proporcionalmente à

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

B

---

Estimação da Inflação Implícita de Curto Prazo

distribuição das expectativas Focus Top 5 Curto Prazo no período considerado.²

Como exercício empírico, nós aplicamos o procedimento descrito acima para estimar a inflação implícita de curto prazo de novembro de 2014 a março de 2017. Comparamos a inflação implícita com a mediana das previsões do Boletim Focus e com a mediana das previsões do Top 5 de curto prazo. Os resultados revelam que a inflação implícita obtida é competitiva em relação às previsões do Focus. A diferença entre os erros de previsão da inflação implícita e os dessas duas previsões do Focus não é estatisticamente significante.

De acordo com Söderlind (2011), o uso da inflação implícita como indicador do nível de preços no futuro possui diversas vantagens em relação a métodos baseados em surveys. Ela está disponível em base diária, foca nas crenças do mercado e é baseada em decisões que envolvem ganhos e perdas financeiras. Um exemplo recente ilustra a alta velocidade de atualização da inflação implícita. Em 28/3/2017 foi aprovado pela Aneel o ajuste nas tarifas de energia elétrica com o objetivo de ressarcir o consumidor por uma cobrança extra indevida ocorrida decorrente da contratação da usina de Angra III em 2016. Como consequência foi feito um reajuste de cerca de -10% nas contas de energia do mês de abril, impactando negativamente a expectativa do IPCA para esse mês. A inflação implícita de abril respondeu imediatamente, apresentando uma queda de 21 pontos-base do dia 27 para o dia 28, enquanto que a mediana das previsões do Focus caiu apenas 1 ponto-base nesse mesmo período.

O restante deste artigo está organizado da seguinte forma. A Seção 2 discute os problemas que ocorrem ao tentar calcular a inflação implícita usando preços de títulos públicos. Na Seção 3 apresentamos uma metodologia parcimoniosa para o cálculo da inflação implícita que corrige o problema da defasagem. Na Seção 4 propomos um modo para a distribuição da inflação implícita de acordo com a sua sazonalidade. Na Seção 5 apresentamos um exercício empírico que compara o poder de preditivo da inflação implícita às expectativas do Boletim Focus. Na Seção 6 oferecemos as nossas considerações finais.

² O Boletim Focus é um relatório semanalmente divulgado pelo Banco Central do Brasil que contém projeções sobre indicadores da economia brasileira coletadas junto a economistas que atuam no Brasil. Ver http://www.bcb.gov.br/pec/GCI/PORT/readout/readout.asp.

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.

# 2. Problemas ao se Calcular a Inflação Implicita a partir de Títulos Públicos

Nesta seção, a fim de tornar os problemas do cálculo da inflação implícita mais claros, usaremos como parâmetros as curvas estimadas pela Anbima, uma vez que são as mesmas utilizadas por instituições financeiras para marcação a mercado de diversos ativos.³ A Anbima divulga diariamente a estrutura a termo da taxa prefixada (taxas nominais extraídas de LTNs e NTN-Fs) e do cupom de IPCA (extraída das NTN-Bs), bem como a estrutura a termo de inflação implícita.⁴,⁵ Essas curvas são estimadas usando o modelo de interpolação de Svensson (1995). Esse modelo é amplamente usado por bancos centrais ao redor do mundo. No entanto, ele não garante a ausência de arbitragem, ou seja, a curva gerada não necessariamente passa nos pontos conhecidos.

Há dois problemas com as curvas de juros estimadas pela Anbima:

1) O cupom de IPCA, utilizado pela Anbima para calcular a inflação implícita, não é a taxa de juros real do momento da negociação da NTN-B até o seu vencimento. Isso ocorre porque as NTN-Bs não negociam a inflação entre o momento da compra e o vencimento, e sim a inflação com 15 dias de defasagem. A seguir, detalhamos o problema.

Para qualquer título de renda fixa zero-cupom, temos que



P_(t,T) = VNA_T/(1 + R_(t,T)), 



Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

232

---

Estimação da Inflação Implícita de Curto Prazo

em que P_(t,T) é o preço do título na data t com vencimento em T, VNA_T é o valor nominal atualizado na data de vencimento T e R_(t,T) é a taxa nominal de t a T.

Vamos utilizar uma NTN-B zero-cupom para exemplificar o problema. Suponha que estejamos em um dia em que o VNA é conhecido.⁶ O VNA no vencimento (VNA_T) será o VNA na data t (VNA_t) reajustado pela inflação defasada de 15 dias corridos:



VNA_T = VNA (1 + \pi_(t-15,T-15)),



em que \pi_(t-15,T-15) denota a inflação de 15 dias corridos antes do momento em que se está apreçando o título até 15 dias corridos antes do vencimento do título. Podemos decompor também a taxa nominal em taxa real mais inflação. Desta forma, a Equação 1 pode ser reescrita como:



P_(t,T) = VNA (1 + \pi_(t-15,T-15))/(1 + r_(t,T))(1 + \pi_(t,T)),



em que r_(t,T) é a taxa real de t a T. Note que, por causa da defasagem da inflação no cálculo do VNA, as inflações no numerador e no denominador não correspondem ao mesmo período. Decompondo as inflações da equação anterior, temos que:



P_(t,T) = VNA (1 + \pi_(t-15,T)) (1 + \pi_(t,T-15))/(1 + r_(t,T))(1 + \pi_(t,T-15))(1 + \pi_(T-15,T)),   ou



⁶ Para as NTN-Bs, o VNA do dia 15 de cada mês é conhecido.

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.



P_(t,T) = VNA(1 + \pi_(t-15,t))/(1 + r_(t,T))(1 + \pi_(T-15,T)).



O cupom de IPCA (C_IPCA) é definido como a solução da seguinte equação:



P_(t,T) = VNA/(1 + C_-IPCA_(t,T)).



Portanto,



1 + C_-IPCA_(t,T) = (1 + r_(t,T))(1 + \pi_(T-15,T))/(1 + \pi_(t-15,t)).



(2)

Assumindo que



\pi_(t-15,t) ≈ \pi_(T-15,T),



o cupom de IPCA iguala-se à taxa real. Essa hipótese é usada pela Anbima para o cálculo da inflação implícita. Quando o intuito é apenas o apreçamento de títulos, utilizar essa aproximação não causa dano algum. Para prazos longos, também não há problemas, mesmo que as duas inflações sejam bastante diferentes, uma vez que a taxa de juros real incidirá em um período muito maior que 15 dias corridos.

Por outro lado, para prazos mais curtos essa diferença pode não ser desprezível. O seguinte exemplo ilustra esse ponto. Os dados são referentes ao último semestre de 2016 e a um título zero-cupom com prazo de 1 mês.

Suponha que hoje seja dia 15 de um dado mês e que haja uma NTN-B zero-cupom vencendo no próximo dia 15. Admita ainda que a inflação esperada para 1 mês à frente (de hoje até o vencimento) seja 0,40% e a taxa prefixada de 1 mês para o período seja 1,1163% (14,25% a.a). Vamos assumir que, como o prazo é muito curto, o prêmio de risco embutido nas taxas seja irrisório.

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

B

---

Estimação da Inflação Implícita de Curto Prazo

Dessa forma, a taxa de juros real verdadeira para um mês a frente é 0,7135% (8,91% a.a).

Assuma que as inflações esperadas para o cálculo do cupom de IPCA por meio da Equação 2 (essas inflações podem ocorrer por uma queda generalizada dos preços ou por causa da própria sazonalidade da inflação) sejam:

i) Inflação esperada de 15 dias antes de hoje:


E_0(\pi_(t-15,t)) = 0,25\%,  e



ii) Inflação esperada de 15 dias antes do vencimento:


E_0(\pi_(T-15,T)) = 0,16\%.



Assim, o cupom de IPCA é igual a 0,6231% (7,74% a.a). Ao se calcular a inflação implícita pela diferença entre a taxa prefixada e o cupom de IPCA ela é igual a 0,49% para o próximo mês, com 9 pontos-base de diferença para a inflação esperada para 1 mês a frente (0,40%).

2) O segundo problema é relacionado à sazonalidade da inflação. A metodologia de interpolação utilizada para o cupom de IPCA pela Anbima, baseada em Svensson (1995), pressupõe que haja no máximo duas curvaturas diferentes na curva de juros. Entretanto, por causa do comportamento padrão das taxas nominais e da grande sazonalidade da inflação, a curva de juros real pode apresentar curvaturas intra-anuais. Desta forma, ao não considerar a sazonalidade para o cupom de IPCA, a Anbima acaba por não considerar a sazonalidade para a inflação implícita.

Por esses dois problemas serem relevantes, a Anbima não divulga as curvas de cupom de IPCA e de inflação implícita para o curto prazo. Na próxima seção, nós delineamos um procedimento parcimonioso para solução dessas duas questões.

# 3. Metodologia Proposta para o Cálculo da Inflação Implícita

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.

Para um título de renda fixa zero-cupom, temos que (Equação 1):



P_(t,T) = VNA_T/(1 + R_(t,T)).



Vamos mais uma vez utilizar uma NTN-B zero-cupom. Seja o último VNA conhecido o da data t^* (VNA_(t^*)). O VNA_T pode ser descrito como o último VNA conhecido reajustado pela inflação até o vencimento defasada de 15 dias corridos. Desta forma,



P_(t,T) = VNA_(t^*)(1 + II_(t^* - 15,T - 15))/(1 + R_(t,T)),   ou





II_(t^* - 15,T - 15) = P_(t,T)(1 + R_(t,T))/VNA_(t^*) - 1 



em que II_(t^* - 15,T - 15) é a inflação implícita embutida no título com 15 dias corridos de defasagem entre t^* e o vencimento T. A inflação implícita de um título zero-cupom pode ser extraída da Equação 3.

Os vencimentos das NTN-Bs ocorrem em 15 de maio ou em 15 de agosto e os VNAs das NTN-Bs no dia 15 de cada mês são conhecidos assim que a inflação do mês anterior é divulgada.⁸ Portanto, a inflação implícita calculada será do dia primeiro do mês do último VNA conhecido até o último dia do mês anterior ao vencimento da NTN-B (abril ou julho).

⁸ Mais especificamente, as NTN-Bs com vencimento em ano ímpar vencem dia 15 de maio. As que possuem vencimento em ano par vencem em 15 de agosto.

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

B

---

Estimação da Inflação Implícita de Curto Prazo

## 3.1 Metodologia com NTN-Bs que pagam cupons, mas não têm mais pagamentos intermediários

Atualmente, o mercado secundário das NTN-Bs que não pagam cupons não tem liquidez. Em consequência a Anbima não divulga o preço unitário (PU) desses títulos. Podemos utilizar então um título com cupons, mas que não tenha mais pagamento intermediário. Nesse caso, como a taxa do cupom da NTN-B é 6% a.a (efetiva) com pagamento semestral (ou seja, 2,956301% ao semestre), temos que



P_(t,T) = VNA_(t^*) (1 + II_(t^*-15,T-15)) + 2,956301\% × VNA_(t^*) (1 + II_(t^*-15,T-15))/(1 + R_(t,T)),  e





II_(t^*-15,T-15) = P_(t,T) (1 + R_(t,T))/VNA_(t^*) (1 + 2,956301\%) - 1. 



A seguir apresentamos um exemplo para tornar a metodologia mais clara. Em 2/1/2017, o último VNA conhecido é o do dia 15/12/2016. A NTN-B com vencimento em 15/5/2017 (96 d.u. até o vencimento) não tem mais pagamentos intermediários (o último pagamento ocorreu dia 16/11/2016). Então, basta utilizarmos a Equação 4 para encontrarmos a inflação implícita.



II_(1/12/2016,30/4/2017) = P_(2/1/2017,15/5/2017) (1 + R_(2/1/2017,15/5/2017))/VNA_(15/12/2016) (1 + 2,956301\%) - 1.



Observe que, por essa metodologia, a inflação gerada sempre tem início a partir da inflação que não conhecemos. Por exemplo, neste caso, apesar de estarmos em 2 de janeiro, a inflação de dezembro ainda não foi divulgada e ela faz parte da inflação implícita gerada.

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.

A taxa prefixada até o vencimento, segundo a curva da Anbima, é 12,62% a.a, o que no período (96 dias úteis) corresponde a 4,630818%. O preço desta NTN-B consultado na página da Anbima na Internet é 2977,390405 e o VNA de 15/12/2016 é 2948,941546. Desta forma, a inflação implícita de dezembro a abril (inclusive) é 2,61%.

## 3.2 Metodologia com NTN-Bs que pagam cupons e ainda têm pagamentos intermediários

A Equação 3 não poderá ser utilizada em uma data em que não há NTN-B sem pagamentos intermediários até seu vencimento. Como observado anteriormente, as NTN-Bs com vencimento em ano ímpar vencem dia 15 de maio e as que vencem em ano par, 15 de agosto. Portanto, há períodos em que a NTN-B mais curta ainda tem pagamento intermediário. Existem 4 casos:

a) Para as NTN-Bs com vencimento em ano ímpar:

i. Quando se está entre novembro do ano anterior e a data de vencimento (15 de maio).

ii. Quando se está entre maio e novembro do ano anterior. Neste caso há um pagamento intermediário (no dia 16 de novembro).⁹

b) Para as NTN-Bs com vencimento em ano par:

i. Quando se está entre fevereiro do ano de vencimento e a data de vencimento (15 de agosto).

ii. Quando se está em uma data anterior a fevereiro do ano de vencimento. Neste caso existe um ou mais pagamentos intermediários.¹⁰

⁹ 15 de novembro é feriado nacional no Brasil.

¹⁰ Por exemplo, em setembro de um ano ímpar, como a NTN-B mais curta vence em agosto do ano seguinte, há apenas um pagamento intermediário (fevereiro do ano seguinte). Entretanto, antes de agosto de um ano ímpar, essa NTN-B possui ainda dois pagamentos intermediários (agosto do ano corrente e fevereiro do ano seguinte).

238 Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Estimação da Inflação Implícita de Curto Prazo

Para os casos a.i) e b.i) podemos utilizar a metodologia já apresentada.¹¹ Os itens a.ii) e b.ii) são diferentes, uma vez que os títulos possuem pagamento intermediário. Quando estamos nesses casos, para se extrair a inflação implícita utilizando a NTN-B é necessário realizar a técnica denominada bootstrapping para a extração das taxas à vista (taxas de títulos zero-cupom). Para isso, é necessário que haja um instrumento sem cupom com vencimento na data do pagamento intermediário. Após realizarmos o bootstrapping, utilizaremos a Equação 3 para encontrar a inflação implícita do período.

Nós utilizamos o futuro de cupom de IPCA (DAP) como instrumento “zero” auxiliar do bootstrapping. O DAP é oferecido pela bolsa brasileira e vem ganhando liquidez nos últimos meses.¹² O DAP possui as mesmas características da NTN-B, uma vez que um dos intuitos desse instrumento é hedgear esses títulos.¹³ Desta forma, o DAP tem a mesma defasagem de 15 dias corridos para a inflação assim como o VNA da NTN-B. Assim, a taxa negociada no DAP é o próprio cupom de IPCA. O DAP vence no 15º dia do mês e há vencimentos disponíveis em todos os meses.

A seguir apresentamos um exemplo de utilização do DAP em conjunto com uma NTN-B para a extração da inflação implícita.

Em 7/11/2016, a NTN-B mais curta vencia em 15/5/2017 (prazo de 129 dias úteis). Esse título tinha, além do fluxo de caixa no vencimento, um pagamento intermediário em 16/11/2016 (prazo de 6 dias úteis) igual à taxa do cupom multiplicada pelo valor de face deste dia.

O preço utilizado na Equação 4 é o preço de um título zero-cupom com vencimento em 15/05/2017. Entretanto, o título em questão não é zero-cupom. Para obtermos o preço precisamos do cupom de IPCA até o vencimento para trazermos a valor presente o valor de face do dia

¹¹ Nesses casos encontraremos uma inflação implícita do mês do último VNA divulgado até o mês anterior ao vencimento da NTN-B. Todavia, nada impede de acharmos taxas mais curtas se tivermos outros instrumentos financeiros com liquidez que negociem o cupom de IPCA, tais como o swap IPCA x DI e o DAP.

¹² A liquidez do DAP aumentou a partir de maio de 2016 com a contratação de market makers pela bolsa brasileira. Ver Bertinat (2016).

¹³ Ver http://www.bmfbovespa.com.br/pt_br/produtos/listados-a-vista-e-derivativos/juros/futuro-de-cupom-ipca.htm.

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.

7/11/2016. Para encontrarmos essa taxa precisamos realizar o bootstrapping.

Como citado anteriormente, a taxa até o pagamento intermediário pode ser encontrada via DAP. O preço unitário (PU) no vencimento deste contrato, como no mercado de DI-futuro, é 100.000. O PU de ajuste para contratos abertos é divulgado pela bolsa todos os dias úteis. Nesse caso, o PU de ajuste para o contrato de DAP com vencimento em 16/11/2016 era 99.786,32. Assim, o cupom de IPCA até essa data é 0,214138%.

A TIR divulgada pela Anbima para este título era 6,5395% a.a, taxa esta que foi calculada a partir do preço do título (3.019,131593) e do VNA projetado pela Anbima para 7/11/2016 (2.941,96).

A partir desses dados podemos calcular o cupom de IPCA até o vencimento (C_(IPCA_(t,T))) usando a técnica de bootstrapping:



3.019,131593 = 2,956301\% × 2941,96/(1 + 0,214138\%) + 2,941,96(1 + 2,956301\%)/(1 + C_(IPCA_(t,T)))



Resolvendo a equação, encontra-se C_(IPCA_(t,T)) = 3,293912\%. Com este valor podemos calcular o preço de um título zero-cupom com vencimento em 15/05/2017 que será utilizado na Equação 3:



P_(t,T) = 2941,96/(1 + 3,293912\%) = 2.848,14.



O último VNA conhecido é o VNA de 15/10/2016 que é igual a 2.936,00. A taxa de juros nominal até o vencimento é 13,15% a.a (129 dias úteis para o vencimento). A partir desses valores, podemos resolver a Equação 3:



H_(1/10/2016,30/4/2017) = (1 + 13,15\%)^(129/252) × 2.848,14/2.936,00 - 1 = 3,34\%.



Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

CC BY NC

---

Estimação da Inflação Implícita de Curto Prazo

Na metodologia proposta nesta seção não há subjetividade, uma vez que não estamos utilizando nenhuma hipótese para extrair a inflação implícita do período. Além disso, se considerarmos o prêmio de risco no curto prazo próximo de zero, a inflação implícita aproxima a inflação esperada pelos participantes do mercado embutida em instrumentos financeiros.

## 3.3. Metodologia utilizando apenas o Mercado Futuro de Cupom de IPCA (DAP)

Na Seção 3.2 utilizamos o mercado futuro de cupom de IPCA (DAP) para o cálculo da inflação implícita quando não há uma NTN-B sem pagamentos intermediários no mercado. Nesse caso, utilizamos a metodologia de bootstrapping para a extração das taxas à vista.

Podemos calcular também a inflação implícita para qualquer vencimento de DAP. Para esse contrato, que negocia o cupom de IPCA à vista, devemos resolver a Equação 3 para encontrar a inflação implícita:



II_(t^*-15,T-15) = PU_(t,T)(1 + R_(t,T))/VNA_(t^*)-1,



onde II_(t^*-15,T-15) é a inflação implícita embutida nos contratos de DAP com 15 dias corridos de defasagem entre t^* e o vencimento T, R_(t,T) é a taxa nominal de t a T e PU_(t,T) é o preço unitário corrente do contrato de DAP que vence em T. Se estivéssemos utilizando uma NTN-B sem pagamentos intermediários, o VNA_(t^*) seria o último VNA conhecido. Entretanto, para os contratos de DAP, esse valor não é imediato.

Como em um contrato de DAP com vencimento em T, o PU em t vale

CC BY NC

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.



P U_(t, T) = 100.000/(1 + C _- I P C A_(t , T)),



temos que o VNA_t do DAP é 100.000. Desta forma, o VNA_(t+) do contrato de DAP é igual a 100.000 descontado pela inflação com 15 dias de defasagem da data corrente:



V N A_(t +) = 100.000/1 + I I_(t ^* - 15 , t - 15).



A inflação no denominador dessa equação, apesar de ser uma inflação já ocorrida, ainda não é conhecida. Entretanto, como os ajustes diários do DAP consideram a projeção de inflação do IPCA divulgada pela Anbima, o cupom de IPCA utilizado no cálculo do seu PU leva em conta essa expectativa. Desta forma, essa inflação pode ser calculada a partir dos VNA divulgados pela ANBIMA.



I I_(t ^* - 15, t - 15) = V N A _t^(A n b i m a)/V N A_(t ^+)^(A n b i m a) - 1.



A partir dessa inflação, podemos calcular o VNA_(t+) do contrato de DAP e calcular a inflação implícita I I_(t^*-15,t-15).

A seguir apresentaremos um exemplo do cálculo da inflação implícita por meio do contrato de DAP.

No dia 05/10/2016, o PU de ajuste do contrato de DAP com vencimento em 16/11/2016 (27 d.u. para o vencimento) vale 99.010,08. O VNA da NTN-B deste dia (divulgado pela ANBIMA) é 2.937,566118. O último VNA da NTN-B conhecido é o de 15/09/2016 (embutido o IPCA de agosto) e é igual a 2.933,656216. Neste caso, I I_(t^*-15,t-15) se refere à I I_(1/9/2016,20/9/2016). Dessa forma,

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

CC BY NC

---

Estimação da Inflação Implícita de Curto Prazo



II_(t^*-15,t-15) = VNA_t^(Anbima)/VNA_(t^*)^(Anbima) - 1 = 2.937,566118/2.933,656216 - 1 = 0,133277\%.



Vale observar que a inflação implícita neste período depende da projeção da ANBIMA, ou seja, não pode ser considerado um valor embutido no contrato de DAP. A partir desta inflação podemos encontrar o VNA_(t^*) para o contrato de DAP:



VNA_(t^*) = 100.000/1 + 0,133277\% = 99.866,89994.



Com o VNA_(t^*) do DAP já calculado e com a taxa nominal até o vencimento (13,012760% a.a.), podemos calcular, a partir da Equação 3, a inflação implícita de 1/9/2016 a 31/10/2016 em 5/12/2016:



II_(1/9/2016,31/10/2016) = 99.010,08 × (1 + 13,012360\%)^(27/252)/99.866,89994 - 1 = 0,45\%.



Pode-se calcular a inflação implícita a partir da metodologia acima para qualquer vencimento de DAP. Todavia, é possível extrair as inflações implícitas dos períodos (defasados de 15 du) entre os vencimentos de DAP de uma maneira mais imediata. Suponha que haja dois DAPs negociados na data t, um que vence na data T_i e outro que vence em T_j, com T_j > T_i. Seja R_(T_i,T_j) a taxa de juros nominal a termo entre T_j > T_i em t. Combinando-se a Equação 3 para os vencimentos T_i e T_j chega-se à inflação implícita a termo entre T_i - 15 e T_j - 15:

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.



H_(T_i - 15, T_j - 15) = P U_(t, T_i)/P U_(t, T_i) (1 + R_(T_i, T_j)) - 1



# 4. Distribuição da Inflação Implícita Considerando a Sazonalidade e as Informações Correntes

Para os *policy makers* e outros participantes de mercado pode também ser interessante saber a inflação implícita de cada mês à frente. Para isso devemos distribuir a inflação implícita encontrada pela metodologia da seção anterior entre os meses em que ela incide.¹⁴ Não é adequado distribuir uniformemente a inflação implícita, uma vez que a taxa de inflação apresenta sazonalidade e não se consideraria informações correntes sobre choques de curto prazo na inflação.

Uma sugestão para se realizar a distribuição entre os meses seria empregar a sazonalidade histórica da inflação. Entretanto, esse ajuste estaria incompleto, uma vez que não incorporaria informações de eventos que podem afetar a inflação no curto prazo. Outra alternativa consiste em utilizar as previsões do relatório Focus do Banco Central do Brasil. Dessa forma, além de distribuir sazonalmente a inflação implícita, informações correntes sobre a evolução futura dos preços são incorporadas na estimação. Por esse motivo, essa abordagem foi escolhida neste trabalho. Como estamos interessados em obter a inflação implícita de curto prazo, nós usamos a mediana das previsões do Top 5 Curto Prazo para o IPCA, que se baseia nas previsões dos participantes que mais acertaram no passado recente.¹⁵

Vamos voltar ao exemplo da Seção 3.1 em que estamos em 2/1/2017 e a inflação implícita gerada de dezembro a abril (inclusive) é 2,61% ou 2,57% em taxa contínua. A Tabela 1 apresenta as medianas das previsões de IPCA do Top 5 Curto Prazo na última data disponível (30/12/2016), os respectivos pesos para a divisão da inflação para cada mês (o peso de dez/16 é igual a razão entre a previsão de dezembro e a soma de

¹⁴ Observe que a inflação implícita mensal não é observável. Portanto, o cálculo da inflação implícita mensal depende do critério de distribuição.

¹⁵ As medianas das previsões do relatório Focus podem ser encontradas em http://www.bcb.gov.br.

244 Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Estimação da Inflação Implícita de Curto Prazo

todas as previsões) e o IPCA em taxa contínua em cada mês (que é o peso multiplicado por 2,57%). A última linha mostra a distribuição da inflação implícita entre os meses para a qual foi calculada.

Tabela 1 – Distribuição da Inflação Implícita do período de dezembro de 2016 a abril de 2017 (2,57%) entre os meses do período por meio da sazonalidade embutida nas previsões de IPCA do Top 5 Curto Prazo divulgadas no Relatório Focus do Banco Central do Brasil

|   | dez/16 | jan/17 | fev/17 | mar/17 | abr/17  |
| --- | --- | --- | --- | --- | --- |
|  Mediana das Previsões (Focus) | 0,37% | 0,50% | 0,60% | 0,43% | 0,52%  |
|  Pesos | 15,29% | 20,46% | 24,22% | 17,08% | 20,43%  |
|  Inflação Implícita em Taxa Contínua | 0,393% | 0,532% | 0,638% | 0,457% | 0,553%  |
|  Inflação Implícita | 0,394% | 0,533% | 0,640% | 0,458% | 0,555%  |
|  Nota 1 - o peso de cada mês é igual a razão entre a previsão do mês e a soma de todas as previsões)
Nota 2 - A inflação implícita em taxa contínua em cada mês é o peso de cada mês multiplicado pela inflação implícita em taxa contínua de todo o período.
Nota 3 - A última linha mostra a inflação implícita em taxa discreta que é o exponencial da taxa contínua subtraído da unidade.
Nota 4 – Os valores nessa tabela estão arredondados.  |   |   |   |   |   |

# 5. Exercício Empírico

A amostra utilizada no exercício empírico compreende o período de novembro de 2014 a março de 2017. As NTN-Bs com mais liquidez pagam cupons semestrais e têm seus PUs de fechamento divulgados pela Anbima. As NTN-Bs que vencem em ano ímpar têm vencimento em maio e as que vencem em ano par, em agosto. Desta forma, em alguns períodos, precisamos dos contratos de DAP para realizar o bootstrapping e extrair as taxas à vista. Entretanto, o DAP apenas ganhou liquidez em maio de 2016 quando a bolsa brasileira contratou formadores de mercado para alguns

CC BY NC

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.

vencimentos deste contrato. Assim sendo, utilizaremos os seguintes instrumentos para extração da inflação implícita no período estudado:

- de 15/11/2014 a 7/5/2015: NTN-B com vencimento em 15/5/2015. Neste caso podemos calcular as inflações implícitas mensais de novembro de 2014 a abril de 2015 por meio do método da Seção 3.1;
- de 15/02/2016 a 9/8/2016: NTN-B com vencimento em 15/8/2016. Neste caso podemos calcular as inflações implícitas mensais de fevereiro de 2016 a julho de 2016 por meio do método da Seção 3.1;
- de 15/8/2016 a 7/11/2016: DAP com vencimento em 16/11/2016 e/ou NTN-B com vencimento em 15/5/2017. Neste caso podemos calcular as inflações implícitas mensais de agosto de 2016 a outubro de 2016 por meio dos métodos da Seção 3.2 (utilizando o DAP e a NTN-B) ou da Seção 3.3 (utilizando apenas o DAP). Nesta seção apresentaremos os resultados utilizando o método da Seção 3.2. Os resultados ao empregarmos o método da Seção 3.3 se encontram no Apêndice e são semelhantes aos aqui mostrados; e
- de 16/11/2016 a 31/03/2017: NTN-B com vencimento em 15/5/2017. Neste caso podemos calcular as inflações implícitas mensais de 11/2016 a 03/2017 por meio do método da Seção 3.1.

Observe que não podemos calcular a inflação implícita de maio de 2015 a janeiro de 2016 porque neste período não há uma NTN-B sem cupons vencendo e o contrato de DAP ainda não possuía liquidez. Deste modo, se considerarmos, por exemplo, as previsões de inflação nas últimas sextas-feiras antes das divulgações do IPCA, teremos 20 observações em nossa amostra.

Comparamos o erro, em relação ao IPCA realizado, da inflação implícita com o da mediana das previsões do IPCA publicadas no Boletim Focus e também com a mediana das previsões do TOP 5 de Curto Prazo (também publicadas no Boletim Focus). A maioria das atualizações no Focus é realizada às sextas-feiras. Além disso, os analistas costumam aprimorar suas previsões nas datas críticas utilizadas para apuração do ranking Top 5 do Boletim Focus.¹⁶ As correlações entre os erros da

¹⁶ A data crítica para apuração do ranking Top 5 do Boletim Focus ocorre na véspera da divulgação do IPCA-15 pelo IBGE.

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Estimação da Inflação Implícita de Curto Prazo

inflação implícita e das expectativas divulgadas no Focus se situam ao redor de 0,84 para as previsões na 1ª sexta-feira antes da divulgação do IPCA e de 0,91 para as previsões na data crítica imediatamente antes da divulgação do IPCA.

Fazemos seis exercícios comparando os erros absolutos (i) da primeira sexta-feira mais próxima da divulgação do IPCA; (ii) da segunda sexta-feira mais próxima da divulgação do IPCA; (iii) da quarta sexta-feira mais próxima da divulgação do IPCA; (iv) da oitava sexta-feira mais próxima da divulgação do IPCA; (v) da primeira data-crítica mais próxima da divulgação do IPCA; e (vi) da segunda data-crítica mais próxima da divulgação do IPCA.

O Gráfico 1 mostra as previsões divulgadas no Boletim Focus (Mediana e Top 5 Curto Prazo) e a inflação implícita gerada pelo nosso modelo para março de 2017 desde 16/11/2016 até 31/03/2017. Observe que a inflação implícita possui velocidade de atualização maior, representada pelo perfil "recortado" da série. Essa é a uma vantagem da inflação implícita: ela é atualizada permanentemente, permitindo um acompanhamento mais estreito das expectativas de inflação. Além disso, podemos notar pelo gráfico que a inflação implícita é mais relacionada à previsão de inflação do Top 5 do que à mediana do Focus.

![img-0.jpeg](img-0.jpeg)

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.

A Tabela 2 apresenta o resultado do teste de amostras relacionadas para as diferenças médias entre os erros absolutos das “previsões” e o IPCA realizado. A diferença entre as medidas corresponde à subtração entre o erro absoluto da inflação implícita e o erro absoluto da previsão divulgada no Focus (Top 5 Curto Prazo e Mediana). A hipótese nula do teste é que a diferença entre os erros absolutos das previsões é zero.

Tabela 2 – Teste de Amostras Relacionadas para as Diferenças Médias entre os Erros Absolutos em Relação ao IPCA realizado. As Diferenças Médias são entre a Inflação Implícita (II) e o Top 5 de Curto Prazo (Top 5 CP) e entre a Inflação Implícita (II) e a Mediana (Med).

|   |  | II - Top 5 CP |   |  | II - Med  |   |
| --- | --- | --- | --- | --- | --- | --- |
|  Data da Previsão | n° de Obs | Dif. Média | Estat. t |   | Dif. Média | Estat. t  |
|  1ª sexta antes do IPCA | 20 | 0,003% | 0,33 |   | -0,003% | -0,30  |
|  2ª sexta antes do IPCA | 20 | -0,002% | -0,15 |   | -0,007% | -0,66  |
|  4ª sexta antes do IPCA | 17 | -0,005% | -0,38 |   | -0,028% | -1,99  |
|  8ª sexta antes do IPCA | 14 | -0,009% | -0,76 |   | -0,019% | -1,45  |
|  1ª data crítica antes do IPCA | 20 | 0,010% | 1,11 |   | 0,005% | 0,52  |
|  2ª data crítica antes do IPCA | 16 | 0,007% | 0,72 |  | -0,025% | -1,93  |

Valores negativos das estatísticas t indicam que os erros absolutos médios da inflação implícita em relação ao IPCA realizado são menores do que os das previsões do Boletim Focus. Os resultados mostram que as diferenças entre os modelos na maioria das vezes não são estatisticamente significantes. Há apenas dois resultados que indicaram um desempenho melhor da inflação implícita em relação à mediana do Boletim Focus ao nível de significância de 10% e nenhum resultado com desempenho superior do Focus. Portanto, os resultados do exercício empírico revelam que a inflação implícita obtida é competitiva em relação às previsões do Focus.

## 6. Considerações Finais

A inflação implícita guarda forte relação com a inflação esperada, especialmente para horizontes inferiores a seis meses. No entanto, duas questões dificultam a aplicação desse resultado como método de previsão

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Estimação da Inflação Implícita de Curto Prazo

da inflação futura. A primeira concerne à especificação da forma de correção da NTN-B pelo IPCA, a qual é sempre defasada de quinze dias. A segunda questão se refere a sazonalidade da inflação que não é capturada pelos modelos tradicionais de construção de curvas de juros. Esses dois problemas são amplificados no curto prazo. Neste trabalho nós apresentamos uma metodologia parcimoniosa para extração de expectativa de inflação de curto prazo que trata diretamente desses dois problemas. Os resultados revelaram que a inflação implícita assim obtida apresenta poder preditivo da inflação futura equivalente ao Focus. Tal achado é relevante por pelo menos dois motivos: (i) superar pesquisas de expectativa de inflação não é uma tarefa trivial, especialmente no curto prazo; (ii) a inflação implícita é atualizada permanentemente, permitindo um acompanhamento mais estreito das expectativas por parte dos policy makers e agentes de mercado.

## Referências

Bertinat, N. (2016). Futuro de Cupom de IPCA: Uma Nova Ferramenta no Mercado de Derivativos de Juros no Brasil. *Resenha da Bolsa* Vol. 4.

Evans, M. D. (1998). Real rates, expected inflation, and inflation risk premia. *Journal of Finance*, 53 (1): 187-218.

Kubudi, D. e Vicente, J. (2016). A Joint Model of Nominal and Real Yield Curves. Working Paper Central Bank of Brazil, 452.

Söderlind, P. (2011). Inflation Risk Premia and Survey Evidence on Macroeconomic Uncertainty. *International Journal of Central Banking*, 7 (2): 113-133.

Svensson, L (1995). Estimating forward interest rates with the Extended Nelson and Siegel Method. Sveriges Riksbank Quarterly Review 1995:3: 13-26.

Vicente, J. e F. Graminho (2015). Decompondo a inflação implícita. *Revista Brasileira de Economia*, 69 (2): 263-284.

CC BY NC

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

---

Araújo, G. S., Vicente, J. V. M.

Vicente, J. e Guillen, O. (2013). Do inflation-linked bonds contain information about future inflation? Revista Brasileira de Economia, 67 (2): 277–286.

# Apêndice – Resultados do Exercício Empírico Utilizando somente o DAP

A Tabela A.1 apresenta os resultados do exercício empírico ao se utilizar somente o DAP (método da Seção 3.3) para se calcular a inflação implícita no período de 15/8/2016 a 7/11/2016 (inflações dos meses de agosto a outubro de 2016) em vez de se utilizar o método da Seção 3.2.

Tabela A.1 – Teste de Amostras Relacionadas para as Diferenças Médias entre os Erros Absolutos em Relação ao IPCA realizado. As Diferenças Médias são entre a Inflação Implícita (II) e o Top 5 de Curto Prazo (Top 5 CP) e entre a Inflação Implícita (II) e a Mediana (Med).

|   |  | II - Top 5 CP |   | II - Med  |   |
| --- | --- | --- | --- | --- | --- |
|  Data da Previsão | n° de Obs | Dif. Média | Estat. t | Dif. Média | Estat. t  |
|  1ª sexta antes do IPCA | 20 | 0,001% | 0,06 | -0,005% | -0,58  |
|  2ª sexta antes do IPCA | 20 | -0,007% | -0,55 | -0,012% | -1,11  |
|  4ª sexta antes do IPCA | 17 | -0,010% | -0,66 | -0,032% | -2,25  |
|  8ª sexta antes do IPCA | 14 | 0,000% | 0,02 | -0,010% | -0,48  |
|  1ª data crítica antes do IPCA | 20 | 0,007% | 0,76 | 0,001% | 0,16  |
|  2ª data crítica antes do IPCA | 16 | 0,001% | 0,10 | -0,031% | -2,51  |

Revista Brasileira de Finanças (Online), Rio de Janeiro, Vol. 15, N. 2, June 2017

250