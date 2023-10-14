from sqlalchemy import create_engine, text, insert
from .config import settings
from .models import metadata, question_table


engine = create_engine(
    url=settings.DATABASE_URL)


def create_table():
    metadata.create_all(engine)


def insert_data(item):
    try:
        with engine.connect() as conn:
            stmt = insert(question_table).values([
                item.id, item.question, item.answer, item.time_created,
            ])
            conn.execute(stmt)
            conn.commit()
            return True
    except Exception:
        return False


def get_last_record():
    try:
        with engine.connect() as conn:
            stmt = '''SELECT * FROM question'''
            res = conn.execute(text(stmt)).fetchall()
            if res:
                return list(res[-1])
            return 'No entries have been added yet'
    except Exception as e:
        print(e)
