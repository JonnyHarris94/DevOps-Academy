FROM python:3.9 as base
RUN pip install poetry
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry install
COPY todo_app todo_app
COPY test test
COPY entrypoint.sh entrypoint.sh

FROM base as development
ENTRYPOINT ["poetry","run","flask","run", "--host","0.0.0.0"]

# Docker Testing
FROM base as test
ENTRYPOINT ["poetry", "run", "pytest"]

FROM base as production
RUN poetry add gunicorn
ENTRYPOINT ["sh","./entrypoint.sh"]