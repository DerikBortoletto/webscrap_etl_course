import pandas as pd
from bs4 import BeautifulSoup
import os

# Acessar as tableas e tratar

def transform_table_0(input_path, output_path):
    """Transforma a primeira tabela IFR(Fatalidade por faixa etária)."""
    with open(input_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table))[0]

    # Acessar as colunas da tabela e converter para csv
    df.columns = ['Age group', 'IFR']
    df.to_csv(output_path, index=False) 
    print(f'Tabela IFR transformada salva em {output_path}')

def transform_table_1(input_path, output_path):
    """Transforma a segunda tabela variants of concern."""
    with open(input_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table))[0]


        # Acessar as colunas da tabela e converter para csv
        df.columns = ['Name', 'Lineage', "Detected", "Countries", "Priority"]
        df.to_csv(output_path, index=False) 
        print(f'Tabela de variantes de preocupação transformada salva em {output_path}')

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_data_dir = os.path.join(base_dir, 'data', 'raw')
    processed_data_dir = os.path.join(base_dir, 'data', 'processed')
    os.makedirs(processed_data_dir, exist_ok=True)

    transform_table_0(
        input_path = os.path.join(raw_data_dir, 'table_0.html'),
        output_path = os.path.join(processed_data_dir, 'ifrs_data.csv')
    )

    transform_table_1(
        input_path = os.path.join(raw_data_dir, 'table_1.html'),
        output_path = os.path.join(processed_data_dir, 'variant_data.csv') 
    )