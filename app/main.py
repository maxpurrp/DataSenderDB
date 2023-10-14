from fastapi import FastAPI, Body
import requests
from .db import create_table, insert_data, get_last_record


app = FastAPI(title="FastAPI, Docker, and Traefik")
create_table()


class Item:
    id: int
    question: str
    answer: str
    time_created: str


def get_questions(count: int):
    bad_question = 0
    result = requests.get(f'https://jservice.io/api/random?count={count}')
    data = result.json()
    for elem in data:
        item = Item()
        item.id = elem['id']
        item.question = elem['question']
        item.answer = elem['answer']
        item.time_created = elem['category']['created_at']
        if not insert_data(item):
            bad_question += 1
    if bad_question:
        get_questions(bad_question)


@app.get("/")
async def main():
    return {'hello': 'world'}


@app.post('/transfer')
async def post_querry(data=Body()):
    try:
        count = data['questions_num']
        last_record = get_last_record()
        get_questions(count)
        return {'last record': last_record}
    except Exception as e:
        print(e)
