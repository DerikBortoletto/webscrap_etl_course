import sys
import os
import pandas as pd
import psycopg2

base_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.db_config import DB_CONFIG

# Carregar dados processados ifrs
def load_ifrs_data(csv_path):
    # Conexão com banco de dados
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Criar Tabela no database que receberá os dados ifrs
    create_table_query = """
        CREATE TABLE IF NOT EXISTS ifrs_data (
            age_group TEXT,
            ifr TEXT
        );   
    """
    # Executar a query de criação da tabela
    cursor.execute(create_table_query)
    conn.commit()

    # Iserir dados do CSV na tabela ifrs_data
    ifrs_df = pd.read_csv(csv_path)
    
    for index, row in ifrs_df.iterrows():
        cursor.execute("INSERT INTO ifrs_data (age_group, ifr) VALUES (%s, %s);", tuple(row))
        
    # Fechar conexão e comitar mudanças
    conn.commit()
    cursor.close()
    conn.close()
    print("Dados IFRS carregados com sucesso no banco de dados.")


# Carregar dados processados ifrs
def load_variant_data(csv_path):
    # Conexão com banco de dados
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Criar Tabela no database que receberá os dados ifrs
    create_table_query = """
        CREATE TABLE IF NOT EXISTS variant_data (
            name TEXT,
            lineage TEXT,
            detected TEXT,
            countries INTEGER,
            priority TEXT 
        );   
    """
    # Executar a query de criação da tabela
    cursor.execute(create_table_query)
    conn.commit()

    # Iserir dados do CSV na tabela ifrs_data
    variant_df = pd.read_csv(csv_path)
    
    for index, row in variant_df.iterrows():
        cursor.execute("INSERT INTO variant_data (name, lineage, detected, countries, priority) VALUES (%s, %s, %s, %s, %s);", tuple(row))
        
    # Fechar conexão e comitar mudanças
    conn.commit()
    cursor.close()
    conn.close()
    print("Dados variant carregados com sucesso no banco de dados.")

# Executando as funções de load
if __name__ == "__main__":
    processed_data_dir = os.path.join('data', 'processed')
    load_ifrs_data(csv_path = os.path.join(processed_data_dir, 'ifrs_data.csv'))
    load_variant_data(csv_path = os.path.join(processed_data_dir, 'variant_data.csv'))