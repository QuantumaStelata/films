  Сайт фильмов
  -----------
  ![Build Status](https://img.shields.io/badge/python-3.8.10-%2300dd1d)
  ![Build Status](https://img.shields.io/badge/django-3.2.8-%230000FF)
  ![Build Status](https://img.shields.io/badge/DRF-3.12.4-%23F00)
  
  
  
  **Запуск сервера**
  -----------
  Выполните все миграции и загрузите фикстуры:
  
    . ./migrate.sh
    python3 manage.py loaddata genres
    
  Запустите сервер:
  
    python3 manage.py runserver 127.0.0.1:8000
      
  В случае запуска на другом хосте/порту не забудьте изменить значение переменной HOST в файле films/settings.py
    
    ALLOWED_HOSTS = ['*']
    HOST = "http://127.0.0.1:8000"
    
  **API**
  -----------
  
    {
      "films": "http://127.0.0.1:8000/api/films",
      "actors": "http://127.0.0.1:8000/api/actors",
      "genres": "http://127.0.0.1:8000/api/genres",
      "ratings": "http://127.0.0.1:8000/api/ratings",
      "comments": "http://127.0.0.1:8000/api/comments"
    }
  
  API films возвращает список всех фильмов (доступен только GET-запрос)
  
  API actors возвращает список всех актеров (доступен только GET-запрос)
  
  API genres возвращает список всех жанров (доступен только GET-запрос)
  
  API ratings добавляет оценку фильма в БД (доступен только POST-запрос)
  
  API comments добавляет комментарий к фильму в БД (доступен только POST-запрос)
  
