FROM postgres:14-alpine

COPY init.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_USER=yuniqua_admin
ENV POSTGRES_PASSWORD=root

EXPOSE 5432
