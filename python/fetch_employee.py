import pymysql
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:enter.me@localhost/inca_tech")

print(engine.table_names())

df = pd.read_sql_table("employee",engine)
print(df)

# sorting
print(df.sort_values(["first_name","last_name"],ascending=[1,0]))