import json
import random

START_PK = 1
MODEL = 'database.Genre'
FILE_FIXTURE = 'genres.json'


tpl = ('аниме', 'биографический', 'боевик', 'вестерн', 'военный', 'детектив',
        'детский', 'документальный', 'драма', 'исторический', 'кинокомикс', 'комедия',
        'концерт', 'короткометражный', 'криминал', 'мелодрама', 'мистика', 'музыка',
        'мультфильм', 'мюзикл', 'научный', 'нуар', 'приключения', 'реалити-шоу', 'семейный',
        'спорт', 'ток-шоу', 'триллер', 'ужасы', 'фантастика', 'фэнтези', 'эротика')

jsn = []

for pk, genre in enumerate(tpl, START_PK):
    row = {
        "model": MODEL,
        "pk": pk,
        "fields" : {
            "title": genre.capitalize(),
            "color": "#"+"".join([random.choice('0123456789ABCDEF') for _ in range(6)])
            }   
        }

    jsn.append(row)

with open(f'apps/database/fixtures/{FILE_FIXTURE}', 'w') as f:
    json.dump(jsn, f, ensure_ascii=False, indent=4)
