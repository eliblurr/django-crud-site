FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY . /app

ARG ADMIN_EMAIL
ARG ADMIN_USERNAME
ARG ADMIN_PASSWORD

RUN python3 -m pip install -r /app/requirements.txt
EXPOSE 8080

RUN chmod +x /app/init.sh
RUN /app/init.sh

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]