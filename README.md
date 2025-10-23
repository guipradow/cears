# Localização dos Armazéns da CEARS

A CEARS - Cia. de Estoques Agrícolas do Estado do Rio Grande do Sul está avaliando uma série de localidades no estado do Rio Grande do Sul para construir três novos armazéns agrícolas. A empresa já possui uma série de armazéns, mas está precisando expandir sua capacidade devido ao crescimento expressivo das atividades agrícolas em sua região de atuação. Os armazéns a serem construídos serão graneleiros e poderão ser utilizados para estocar uma série de produtos a granel, como soja e milho.  
  
A figura acima apresenta as localidades escolhidas como possíveis armazéns, juntamente com as cinco regiões de clientes que foram selecionadas para atendimento. A tabela avaixo oferece detalhes adicionais em termos de clientes e armazéns. A capacidade de armazenagem é dinâmica, isto é, considera não só a capacidade estática como também a eficiência com que a CEARS consegue girar seu estoque ao longo de um ano. A demanda total também se refere a um ano. Os custos logísticos entre o armazém de origem e a cidade de destino referem-se aos custos incorridos quando uma tonelada de produto é encaminhada da origem para o destino. Por exemplo, estamos considerando que o custo de se enviar 1 t de produtos de Alegrete para Uruguaiana é equivalente a R$2,10.

<table border="1">
  <thead>
    <tr>
      <th rowspan="2">Cidade de Destino (j)</th>
      <th colspan="5">Custo Logístico entre Armazém e Cidade de Destino</th>
      <th rowspan="2">Custo de Construção [R$ milhões]</th>
      <th rowspan="2">Capacidade Potencial [kton]</th>
    </tr>
    <tr>
      <th>Uruguaiana (i=1)</th>
      <th>Pelotas (i=2)</th>
      <th>Caxias do Sul (i=3)</th>
      <th>Passo Fundo (i=4)</th>
      <th>Porto Alegre (i=5)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alegrete (j=1)</td>
      <td>2.1</td>
      <td>6.3</td>
      <td>7.8</td>
      <td>6.3</td>
      <td>7.5</td>
      <td>7</td>
      <td>600</td>
    </tr>
    <tr>
      <td>Caçapava do Sul (j=2)</td>
      <td>5.7</td>
      <td>2.7</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>3.78</td>
      <td>5</td>
      <td>750</td>
    </tr>
    <tr>
      <td>Tupanciretá (j=3)</td>
      <td>5.4</td>
      <td>5.58</td>
      <td>4.38</td>
      <td>2.88</td>
      <td>4.8</td>
      <td>9</td>
      <td>350</td>
    </tr>
    <tr>
      <td>Vacaria (j=4)</td>
      <td>10.2</td>
      <td>6.54</td>
      <td>1.14</td>
      <td>2.4</td>
      <td>3</td>
      <td>6</td>
      <td>450</td>
    </tr>
    <tr>
      <td>Santa Rosa (j=5)</td>
      <td>5.58</td>
      <td>7.86</td>
      <td>6</td>
      <td>3.48</td>
      <td>6.84</td>
      <td>4</td>
      <td>400</td>
    </tr>
  </tbody>
</table>
</br>  

A CEARS está interessada em encontrar as três localidades para construir seus armazéns de modo que o custo total de construção e logístico seja o mínimo. Considere a variável $x_j$ a presença do armazém na localidade $j$. Mais especificamente,

$$
\begin{equation*}x_j = \left\{\begin{matrix}
1 \\0
\end{matrix}\right.\quad\left(j=1, 2, 3, 4, 5\right)
\end{equation*}
$$
Vamos levar em conta os dois custos: de construção do armazém e de logística. Como o armazém $j$ pode encaminhar seus produtos para qualquer um dos clientes $i$, chamaremos $y_{ij}$ de quantidade de produtos enviadas de $j$ para $i$. Levando essas considerações em conta, podemos dizer que a função-objetivo é definida como

$$
\begin{align*}
\min z =\ & 7x_1 + 5x_2 + 9x_3 + 6x_4 + 4x_5 \\
& + 2.10y_{11} + 6.30y_{21} + 7.80y_{31} + 6.30y_{41} + 7.50y_{51} \\
& + \dots +\\
& + 5.58y_{15} + 7.86y_{25} + 6.00y_{35} + 3.48y_{45} + 6.84y_{55}
\end{align*}
$$

As quantidades enviadas dos armazéns não podem exceder as capacidades dos armazéns, ou seja:

$$
\begin{align*}
y_{11} + y_{21} + y_{31} + y_{41} + y_{51} \leq 600x_1 & \quad\text{(capacidade do armazém 1)} \\
y_{12} + y_{22} + y_{32} + y_{42} + y_{52} \leq 750x_2 & \quad\text{(capacidade do armazém 2)} \\
y_{13} + y_{23} + y_{33} + y_{43} + y_{53} \leq 350x_3 & \quad\text{(capacidade do armazém 3)} \\
y_{14} + y_{24} + y_{34} + y_{44} + y_{54} \leq 450x_4 & \quad\text{(capacidade do armazém 4)} \\
y_{15} + y_{25} + y_{35} + y_{45} + y_{55} \leq 400x_5 & \quad\text{(capacidade do armazém 5)}
\end{align*}
$$

O segundo grupo de restrições é relacionado com as demandas. As demandas são atendidas pelos envios conforme apresentado a seguir

$$
\begin{align*}
y_{11} + y_{12} + y_{13} + y_{14} + y_{15}  = 150 & \quad\text{(demanda de Uruguaiana)} \\
y_{21} + y_{22} + y_{23} + y_{24} + y_{25} = 450 & \quad\text{(demanda de Pelotas)} \\
y_{31} + y_{32} + y_{33} + y_{34} + y_{35} = 300 & \quad\text{(demanda de Caxias do Sul)} \\
y_{41} + y_{42} + y_{43} + y_{44} + y_{45} = 250 & \quad\text{(demanda de Passo Fundo)} \\
y_{51} + y_{52} + y_{53} + y_{54} + y_{55} = 500 & \quad\text{(demanda de Porto Alegre)}
\end{align*}
$$

O terceiro grupo de restrições estabelece que apenas três armazéns serão abertos, ou seja, $x_1$ + $x_2$ + $x_3$ + $x_4$ + $x_5$ = 3. O último grupo de restrições estabelece que os $x_j$ são binários, isto é, $x_j \in \left\{0, 1\right\} \left(j=1, 2, 3, 4, 5\right)$, e que os $y_{ij}$ são variáveis não negativas, $y_ij\geq 0 \left(i=1, 2, 3, 4, 5; j=1, 2, 3, 4, 5\right)$.
<br>
<br> 
  
## Referências
COLIN, Emerson Carlos. Pesquisa operacional: 170 aplicações em estratégia, finanças, logística, produção, marketing e vendas. Rio de Janeiro: LTC, 2007. p. 181-182.