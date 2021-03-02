FROM python:3.7

RUN python -m pip install --upgrade pip

COPY requirements .

RUN pip install -r requirements

WORKDIR /app

COPY app /app

EXPOSE 5000

CMD ["python", "app.py"]
