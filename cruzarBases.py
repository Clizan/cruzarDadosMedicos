import pandas as pd

def abrirArquivoCSV(caminho_arquivo):
    """
    Esta função lê um arquivo CSV e retorna um DataFrame.
    
    Args:
    caminho_arquivo (str): O caminho completo do arquivo CSV.
    
    Returns:
    DataFrame: O DataFrame contendo os dados do arquivo CSV.
    """
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

def abrirArquivoJSON(caminho_arquivo):
    """
    Esta função lê um arquivo JSON e retorna um DataFrame.
    
    Args:
    caminho_arquivo (str): O caminho completo do arquivo JSON.
    
    Returns:
    DataFrame: O DataFrame contendo os dados do arquivo JSON.
    """
    lerArquivoJSON = pd.read_json(caminho_arquivo)
    return lerArquivoJSON

def juntarArquivos(df1, df2, df3, caminho_saida):
    """
    Esta função junta três DataFrames e salva o resultado em um novo arquivo.
    
    Args:
    df1 (DataFrame): Primeiro DataFrame a ser juntado.
    df2 (DataFrame): Segundo DataFrame a ser juntado.
    df3 (DataFrame): Terceiro DataFrame a ser juntado.
    caminho_saida (str): O caminho completo do arquivo de saída.
    
    Returns:
    None
    """
    df_combinado = pd.concat([df1, df2, df3], ignore_index=True)
    df_combinado.to_csv(caminho_saida, index=False)
    print(f"Arquivos combinados e salvos em {caminho_saida}")

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
    
    # Caminho completo do arquivo JSON
    caminhoArquivoJSON = r'C:\Users\clizanwillian\Desktop\Projetos\cruzarDadosMedicos\bases\json.json'
    
    # Chamar a função para abrir o arquivo JSON
    leituraArquivoJSONAberto = abrirArquivoJSON(caminhoArquivoJSON)
    
    # Exibir as primeiras linhas do DataFrame do JSON
    print("\nPrimeiras linhas do arquivo JSON:")
    print(leituraArquivoJSONAberto.head())
    
    # Caminho do arquivo de saída combinado
    caminhoArquivoCombinado = r'C:\Users\clizanwillian\Desktop\Projetos\cruzarDadosMedicos\bases\combinado.csv'
    
    # Juntar os arquivos e salvar em um novo arquivo
    juntarArquivos(leituraArquivoCSVAberto, leituraArquivoXLSXAberto, leituraArquivoJSONAberto, caminhoArquivoCombinado)

# Chamar a função principal
lerArquivos()
