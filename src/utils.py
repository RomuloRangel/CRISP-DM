# Imports
import sqlite3



# Funcoes de Conexão

import sqlite3
import pandas as pd

def conexao_sqlite(name_table: str = 'nome_da_tabela', db: str = 'nome.db', data: pd.DataFrame = None):
    """
    Função para inserir um DataFrame em uma tabela de um banco SQLite.
    
    Parâmetros:
    - name_table (str): Nome da tabela no banco.
    - db (str): Nome do arquivo do banco de dados.
    - data (pd.DataFrame): DataFrame a ser inserido na tabela.
    
    OBS:
    - Especifique `name_table` como string.
    - Especifique `db` com o nome do arquivo do banco (ex.: "meubanco.db").
    - Passe um DataFrame no parâmetro `data` para carregá-lo no banco.
    """
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect(db)
        
        if data is not None:
            # Insere o DataFrame na tabela
            data.to_sql(name_table, conn, if_exists='replace', index=False)
            print('Tabela criada ou substituída com sucesso!')
        else:
            print("Nenhum DataFrame fornecido para inserção.")
        
        # Fecha a conexão
        conn.close()
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
