FROM python:3.9 as base
RUN pip install poetry
WORKDIR /app
COPY poetry.lock pyproject.toml .
RUN poetry install
COPY todo_app todo_app

FROM base as development
ENTRYPOINT ["poetry","run","flask","run", "--host","0.0.0.0"]

FROM base as production
RUN poetry add gunicorn
ENTRYPOINT ["poetry","run","gunicorn","todo_app.app:create_app()", "-b","0.0.0.0:80"]

