FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY concert/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /app/

EXPOSE 8000
RUN python manage.py collectstatic --noinput

CMD sh -c "python concert/manage.py migrate && python concert/manage.py runserver 0.0.0.0:8000"