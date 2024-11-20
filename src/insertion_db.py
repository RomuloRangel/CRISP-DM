# Importaçãod dos modulos necessarios

import pandas as pd
import sqlite3






# Extração da base de dados
 
orders = pd.read_csv("../data/olist_orders_dataset.csv")
customers = pd.read_csv("../data/olist_customers_dataset.csv")
items = pd.read_csv("../data/olist_order_items_dataset.csv")




# Conectar ao SQLite e inserir dados
conn = sqlite3.connect('olist_crm.db')
orders.to_sql('orders', conn, if_exists='replace', index=False)
customers.to_sql('customers', conn, if_exists='replace', index=False)
items.to_sql('items', conn, if_exists='replace', index=False)
conn.close()
