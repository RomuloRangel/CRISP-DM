# Importaçãod dos modulos necessarios

import pandas as pd
from utils import conexao_sqlite






# Extração da base de dados
 
orders = pd.read_csv("../data/olist_orders_dataset.csv")
customers = pd.read_csv("../data/olist_customers_dataset.csv")
items = pd.read_csv("../data/olist_order_items_dataset.csv")

conexao_sqlite(name_table = 'orders',db = 'olist_crm',data=orders)
