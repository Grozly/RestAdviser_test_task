FROM tiangolo/uvicorn-gunicorn:python3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./app /code/app
COPY ./app/main.py /code/main.py
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]