FROM python:3.10

#ENV DJANGO_ENV=development

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN python manage.py migrate

# Собираем статические файлы (если необходимо)
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["./wait-for-it.sh", "db", "5432", "python", "manage.py", "runserver", "0.0.0.0:8000"]
