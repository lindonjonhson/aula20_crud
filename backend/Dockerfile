# FROM python:3.9
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app


# RUN pip install uvicorn

# CMD ["uvicorn", "--host", "0.0.0.0", "--port", "6000", "app:app"]

# CMD ['uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8000']
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"

# CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
