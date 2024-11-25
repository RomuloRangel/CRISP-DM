
import pandas as pd
import sqlite3


# Nesta fase irei fazer as tranformações usando a Queries em SQL para trazer algumas metricas importantes para um CRM

conn = sqlite3.connect('olist_crm.db')

# Receita total por cliente
query_revenue = """
SELECT c.customer_unique_id, SUM(i.price) AS total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN items i ON o.order_id = i.order_id
GROUP BY c.customer_unique_id
"""
revenue_df = pd.read_sql_query(query_revenue, conn)

# Frequência de compra
query_frequency = """
SELECT c.customer_unique_id, COUNT(o.order_id) AS purchase_frequency
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_unique_id
"""
frequency_df = pd.read_sql_query(query_frequency, conn)

# Ticket Médio
query_avg_order_value = """
SELECT c.customer_unique_id, AVG(i.price) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN items i ON o.order_id = i.order_id
GROUP BY c.customer_unique_id
"""
avg_order_value_df = pd.read_sql_query(query_avg_order_value, conn)

# Recência
query_recency = """
SELECT c.customer_unique_id, MIN(DATE('now') - DATE(o.order_purchase_timestamp)) AS recency,
o.order_delivered_customer_date AS date

FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_unique_id
"""
recency_df = pd.read_sql_query(query_recency, conn)

conn.close()



# Juntar todas as métricas no mesmo DataFrame
crm_data = pd.merge(revenue_df, frequency_df, on='customer_unique_id', how='outer')
crm_data = pd.merge(crm_data, avg_order_value_df, on='customer_unique_id', how='outer')
crm_data = pd.merge(crm_data, recency_df, on='customer_unique_id', how='outer')

# Ajustar os nomes das colunas para melhorar o entendimento
crm_data.columns = ['customer_unique_id', 'total_revenue', 'purchase_frequency', 'avg_order_value', 'recency','date']

# Exportar para CSV
crm_data.to_csv('crm_data.csv', index=False)

print("Os dados consolidados foram exportados para 'crm_data.csv'.")

