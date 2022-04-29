FROM python:3.10.4-buster as python
RUN apt-get update && apt-get install -y build-essential libffi-dev python-dev
COPY python /python
WORKDIR /python
RUN python -m pip install -r requirements.txt
RUN python main.py

FROM mysql/mysql-server:latest
COPY --from=python /python/queries /queries
COPY "init.sh" /docker-entrypoint-initdb.d/
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=bloodbank
ENV MYSQL_USER=umkc
ENV MYSQL_PASSWORD=umkc
EXPOSE 3306