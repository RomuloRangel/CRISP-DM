import pandas as pd
import sqlite3

orders = pd.read_csv("/data/olist_orders_dataset.csv")
customers = pd.read_csv("/data/olist_customers_dataset.csv")
items = pd.read_csv("/data/olist_order_items_dataset.csv")

sqlite3