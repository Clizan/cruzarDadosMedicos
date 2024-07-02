import pandas as pd

def abrirArquivoCSV(caminho_arquivo):
    """
    Esta função lê um arquivo CSV e retorna um DataFrame.
    
    Args:
    caminho_arquivo (str): O caminho completo do arquivo CSV.
    
    Returns:
    DataFrame: O DataFrame contendo os dados do arquivo CSV.
    """
    # Leitura do arquivo CSV com a codificação 'latin1'
    lerArquivoCSV = pd.read_csv(caminho_arquivo, encoding='latin1')
    return lerArquivoCSV

def lerArquivos():
    """
    Função principal que chama as ações a serem executadas.
    """
    # Caminho completo do arquivo CSV
    caminho_arquivo_csv = r'C:\Users\clizanwillian\Desktop\Projetos\cruzarBases\bases\csv.csv'
    
    # Chamar a função para abrir o arquivo CSV
    leituraArquivoCSVAberto = abrirArquivoCSV(caminho_arquivo_csv)
    
    # Exibir as primeiras linhas do DataFrame
    print(leituraArquivoCSVAberto.head())

# Chamar a função principal
lerArquivos()
