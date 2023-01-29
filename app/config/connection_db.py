from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://airflow:airflow@postgres_db:5432/postgres")

con_db = engine.connect()
meta = MetaData()