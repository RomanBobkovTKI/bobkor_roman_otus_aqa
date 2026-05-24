## Запуск

1. `pip install -r requirement.txt`
1. `docker compose up -d`
1. `uvicorn app.main:app --reload`
1. `python -m app.seed`
1. `pytest`