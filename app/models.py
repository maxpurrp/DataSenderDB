from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

question_table = Table(
    'question',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('question', String),
    Column('answer', String),
    Column('time_created', String)
)
