FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r concert/requirements.txt


WORKDIR /app/concert

EXPOSE 8000

CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"