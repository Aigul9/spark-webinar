# spark-webinar

Материалы к моему вебинару "Собираем витрину данных: от описания до результата"

[Запись тут](https://www.youtube.com/watch?v=ufR-__6_PqQ)

- [Webinar.pdf](https://github.com/Aigul9/spark-webinar/tree/main/Webinar.pdf) - презентация к вебинару
- [Methodology.md](https://github.com/Aigul9/spark-webinar/tree/main/Methodology.md) - методология для разработки витрины
- [webinar.ipynb](https://github.com/Aigul9/spark-webinar/blob/main/webinar.ipynb) - ноутбук со скриптами на Spark для сбора витрины и аналитики
- [Dashboards.md](https://github.com/Aigul9/spark-webinar/blob/main/Dashboard.md) - дэш на основе витрины
- [data](https://github.com/Aigul9/spark-webinar/tree/main/data) - папка для исходных данных
- [generation](https://github.com/Aigul9/spark-webinar/tree/main/generation) - python-скрипты для генерации этих данных
- [sql](https://github.com/Aigul9/spark-webinar/tree/main/sql) - sql-скрипты для методологии

## Техническая составляющая

### Подготовить:

- Docker Desktop
- Postgres
- Jupyter Notebook
- Metabase
- pgAdmin
- DBeaver

### Драйверы для бд

Postgres - https://jdbc.postgresql.org/download/

ClickHouse - https://mvnrepository.com/artifact/com.clickhouse/clickhouse-jdbc

### Запуск ClickHouse в Docker

docker run -d --name some-clickhouse-server -p 8123:8123 -p 9000:9000 -p 9009:9009 yandex/clickhouse-server

### Запуск локального Metabase

```
cd 'E:\Program Files\Metabase2'
java -jar metabase.jar
```

### Ссылки на локальные сервисы

Jupyter Notebook - http://localhost:8888/notebooks/jupyter-files/webinar.ipynb

Spark UI - http://host.docker.internal:4040/

Metabase - http://localhost:3000/dashboard/99-webinar

ClickHouse - http://localhost:8123
