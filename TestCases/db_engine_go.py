from sqlalchemy import create_engine, MetaData
import sqlite3

engine = create_engine('sqlite: D:/Develop/Python_source/RestApiTests/db.sqlite3', convert_unicode=True)
metadata = MetaData(bind=engine)

engine.execute("select * from pin")