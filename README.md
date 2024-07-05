<h1 align="center">Projeto de Leitura e Combinação de Arquivos CSV</h1>

<p align="center">Este projeto em Python foi desenvolvido para ler arquivos CSV, XLSX e JSON de diversas fontes de dados, combiná-los em um arquivo CSV e gerar insights utilizando o Power BI. Utiliza a biblioteca <code>pandas</code> para manipulação de dados.</p>

<h2>Funcionalidades</h2>

<h3>abrirArquivoCSV(caminho_arquivo)</h3>

<p>Função que lê um arquivo CSV e retorna um DataFrame.</p>

<strong>Parâmetros:</strong>
<ul>
  <li><code>caminho_arquivo</code> (str): O caminho completo do arquivo CSV.</li>
</ul>

<strong>Retorno:</strong>
<ul>
  <li><code>DataFrame</code>: O DataFrame contendo os dados do arquivo CSV.</li>
</ul>

<p>Exemplo de Uso:</p>
<pre><code>df = abrirArquivoCSV('caminho/do/arquivo.csv')
</code></pre>

<h3>abrirArquivoXLSX(caminho_arquivo)</h3>

<p>Função que lê um arquivo XLSX do Excel e retorna um DataFrame.</p>

<strong>Parâmetros:</strong>
<ul>
  <li><code>caminho_arquivo</code> (str): O caminho completo do arquivo XLSX.</li>
</ul>

<strong>Retorno:</strong>
<ul>
  <li><code>DataFrame</code>: O DataFrame contendo os dados do arquivo XLSX.</li>
</ul>

<p>Exemplo de Uso:</p>
<pre><code>df = abrirArquivoXLSX('caminho/do/arquivo.xlsx')
</code></pre>

<h3>abrirArquivoJSON(caminho_arquivo)</h3>

<p>Função que lê um arquivo JSON e retorna um DataFrame.</p>

<strong>Parâmetros:</strong>
<ul>
  <li><code>caminho_arquivo</code> (str): O caminho completo do arquivo JSON.</li>
</ul>

<strong>Retorno:</strong>
<ul>
  <li><code>DataFrame</code>: O DataFrame contendo os dados do arquivo JSON.</li>
</ul>

<p>Exemplo de Uso:</p>
<pre><code>df = abrirArquivoJSON('caminho/do/arquivo.json')
</code></pre>

<h3>juntarArquivos(df1, df2, df3, caminho_saida)</h3>

<p>Função que junta três DataFrames e salva o resultado em um novo arquivo CSV, substituindo o separador de ponto e vírgula por vírgula.</p>

<strong>Parâmetros:</strong>
<ul>
  <li><code>df1</code> (DataFrame): Primeiro DataFrame a ser juntado.</li>
  <li><code>df2</code> (DataFrame): Segundo DataFrame a ser juntado.</li>
  <li><code>df3</code> (DataFrame): Terceiro DataFrame a ser juntado.</li>
  <li><code>caminho_saida</code> (str): O caminho completo do arquivo de saída (por exemplo, <code>'caminho/do/arquivo_combinado.csv'</code>).</li>
</ul>

<strong>Retorno:</strong>
<ul>
  <li>None</li>
</ul>

<p>Exemplo de Uso:</p>
<pre><code>juntarArquivos(df_csv, df_xlsx, df_json, 'caminho/do/arquivo_combinado.csv')
</code></pre>

<h3>lerArquivos()</h3>

<p>Função principal que chama as ações a serem executadas, como a leitura de arquivos CSV, XLSX e JSON, a junção dos dados e a exibição dos primeiros registros.</p>

<p>Exemplo de Uso:</p>
<pre><code>lerArquivos()
</code></pre>

<h2>Uso do Projeto</h2>

<h3>Configuração do Ambiente</h3>

<p>Certifique-se de ter Python e a biblioteca <code>pandas</code> instalados. Você pode instalar o <code>pandas</code> utilizando o seguinte comando:</p>
<pre><code>pip install pandas
</code></pre>

<h3>Alterar o Caminho do Arquivo</h3>

<p>Atualize o caminho dos arquivos CSV, XLSX e JSON no código conforme necessário:</p>
<pre><code>caminho_arquivo_csv = r'caminho/do/arquivo.csv'
caminho_arquivo_xlsx = r'caminho/do/arquivo.xlsx'
caminho_arquivo_json = r'caminho/do/arquivo.json'
</code></pre>

<h3>Executar o Código</h3>

<p>Execute o código Python para ler e manipular os dados dos arquivos CSV, XLSX e JSON e gerar o arquivo combinado:</p>
<pre><code>python nome_do_arquivo.py
</code></pre>

<h3>Utilização no Power BI</h3>

<p>Após a execução, o arquivo <code>combinado.csv</code> será gerado na pasta <code>bases</code>. Importe este arquivo no Power BI para montar uma visão gerencial detalhada e gerar insights através de visualizações avançadas dos dados combinados.</p>

![visual_final](https://github.com/Clizan/cruzarDadosMedicos/assets/31556355/5d59626a-55e2-4a76-beb7-4f8538cf8169)

<h2>Futuras Implementações</h2>

<ul>
  <li><strong>Combinação de Mais Formatos:</strong> Implementar suporte para mais formatos de arquivos, como XML e SQL.</li>
  <li><strong>Análise Avançada de Dados:</strong> Incluir funcionalidades para análise estatística e preditiva dos dados.</li>
  <li><strong>Integração Contínua:</strong> Configurar integração contínua para automação de processos.</li>
</ul>

<h2>Contribuições</h2>

<p>Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias ou novas funcionalidades. Para contribuir, siga estes passos:</p>
<ol>
  <li>Fork o projeto</li>
  <li>Crie uma nova branch (<code>git checkout -b feature/nova-feature</code>)</li>
  <li>Commit suas mudanças (<code>git commit -am 'Adiciona nova feature'</code>)</li>
  <li>Push para a branch (<code>git push origin feature/nova-feature</code>)</li>
  <li>Crie um novo Pull Request</li>
</ol>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a <a href="https://opensource.org/licenses/MIT">Licença MIT</a>.</p>
