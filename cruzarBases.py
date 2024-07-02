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

def abrirArquivoXLSX(caminho_arquivo):
    """
    Esta função lê um arquivo XLSX do Excel e retorna um DataFrame.
    
    Args:
    caminho_arquivo (str): O caminho completo do arquivo XLSX.
    
    Returns:
    DataFrame: O DataFrame contendo os dados do arquivo XLSX.
    """
    lerArquivoXLSX = pd.read_excel(caminho_arquivo)
    return lerArquivoXLSX

def lerArquivos():
    """
    Função principal que chama as ações a serem executadas.
    """
    # Caminho completo do arquivo CSV
    caminhoArquivoCSV = r'C:\Users\clizanwillian\Desktop\Projetos\cruzarDadosMedicos\bases\csv.csv'
    
    # Chamar a função para abrir o arquivo CSV
    leituraArquivoCSVAberto = abrirArquivoCSV(caminhoArquivoCSV)
    
    # Exibir as primeiras linhas do DataFrame do CSV
    print("Primeiras linhas do arquivo CSV:")
    print(leituraArquivoCSVAberto.head())
    
    # Caminho completo do arquivo XLSX
    caminhoArquivoXlsx = r'C:\Users\clizanwillian\Desktop\Projetos\cruzarDadosMedicos\bases\PlanilhasExcel.xlsx'
    
    # Chamar a função para abrir o arquivo XLSX
    leituraArquivoXLSXAberto = abrirArquivoXLSX(caminhoArquivoXlsx)
    
    # Exibir as primeiras linhas do DataFrame do XLSX
    print("\nPrimeiras linhas do arquivo XLSX:")
    print(leituraArquivoXLSXAberto.head())

# Chamar a função principal
lerArquivos()
