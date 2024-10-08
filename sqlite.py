import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data', conn, index_label='index_name')


c = conn.cursor()
c.execute('CREATE TABLE products (prooduct_id, product_name, price)')
conn.commit()

# PRA DELETAR E AS VEZES NAO PRECISA DE "conn.commit()"
c.execute('DROP TABLE products')
c.execute('DROP TABLE data')

c.execute('CREATE TABLE products ([prooduct_id] INTEGER PRIMARY KEY, [product_name] TEX, [price] INTEGER)')


#INSERT
c.execute('''INSERT INTO products (prooduct_id, product_name, price)
    VALUES
    (1, 'Computer', 800),
    (2, 'Printer', 200),
    (3, 'Tablet', 300)
''')
conn.commit()


df_data2 = df_data.iloc[::-2]
df_data2.to_sql('data', conn, if_exists='append')