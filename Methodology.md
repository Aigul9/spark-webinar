# ТЗ на витрину marketing_datamart

Необходимо вывести в рамках витрины 3 таблицы:
- customer_detailed
- campaigns_agg
- dates_agg

## 1. Атрибутивный состав

### 1) Таблица customer_detailed

| №  | Название столбца | Тип данных    | Описание                                                   |
|----|------------------|---------------|------------------------------------------------------------|
| 1  | dt               | string        | Дата визита                                                |
| 2  | visit_id         | string        | Идентификатор визита                                       |
| 3  | client_id        | string        | Идентификатор клиента                                      |
| 4  | url              | string        | URL страницы                                               |
| 5  | duration         | integer       | Время на сайте в секундах                                  |
| 6  | source           | string        | Тип источника, с которого пользователь пришел на сайт      |
| 7  | utmcampaign      | string        | Название рекламной кампании                                |
| 8  | event_type       | string        | Тип события                                                |
| 9  | event_id         | integer       | Идентификатор события                                      |
| 10 | submit_id        | bigint        | Идентификатор заявки                                       |
| 11 | name             | string        | Имя клиента                                                |
| 12 | phone            | string        | Мобильный телефон                                          |
| 13 | phone_plus       | string        | Мобильный телефон со знаком +                              |
| 14 | phone_md5        | string        | Мобильный телефон, хешированный алгоритмом md5             |
| 15 | phone_plus_md5   | string        | Мобильный телефон со знаком +, хешированный алгоритмом md5 |
| 16 | deal_id          | bigint        | Идентификатор сделки                                       |
| 17 | deal_date        | string        | Дата сделки                                                |
| 18 | fio              | string        | ФИО клиента                                                |
| 19 | phone_deal       | string        | Мобильный телефон из таблицы со сделками                   |
| 20 | email            | string        | Электронная почта                                          |
| 21 | address          | string        | Адрес места жительства                                     |
| 22 | username         | string        | Имя пользователя из электронной почты                      |
| 23 | domain           | string        | Домен электронной почты                                    |
| 24 | campaign_name    | string        | Название рекламной кампании                                |
| 25 | costs            | decimal(19,2) | Расходы на рекламу                                         |
| 26 | clicks           | bigint        | Количество кликов                                          |
| 27 | views            | bigint        | Количество просмотров                                      |


### 2) Таблица campaigns_agg

| №  | Название столбца | Тип данных    | Описание                                   |
|----|------------------|---------------|--------------------------------------------|
| 1  | campaign_name    | string        | Название рекламной кампании                |
| 2  | unique_visits    | bigint        | Количество визитов                         |
| 3  | unique_clients   | bigint        | Количество уникальных клиентов             |
| 4  | unique_submits   | bigint        | Количество заявок                          |
| 5  | unique_deals     | bigint        | Количество сделок                          |
| 6  | total_costs      | decimal(19,2) | Общая сумма расходов на рекламу            |
| 7  | total_clicks     | bigint        | Общая сумма кликов                         |
| 8  | total_views      | bigint        | Общая сумма просмотров                     |
| 9  | total_duration   | bigint        | Общая продолжительность визитов в секундах |
| 10 | avg_deal_cost    | decimal(19,2) | Средняя сумма сделки                       |


### 3) Таблица dates_agg

| №  | Название столбца | Тип данных    | Описание                                   |
|----|------------------|---------------|--------------------------------------------|
| 1  | date             | string        | Дата по расходам                           |
| 2  | unique_visits    | bigint        | Количество визитов                         |
| 3  | unique_clients   | bigint        | Количество уникальных клиентов             |
| 4  | unique_submits   | bigint        | Количество заявок                          |
| 5  | unique_deals     | bigint        | Количество сделок                          |
| 6  | total_costs      | decimal(19,2) | Общая сумма расходов на рекламу            |
| 7  | total_clicks     | bigint        | Общая сумма кликов                         |
| 8  | total_views      | bigint        | Общая сумма просмотров                     |
| 9  | total_duration   | bigint        | Общая продолжительность визитов в секундах |
| 10 | avg_deal_cost    | decimal(19,2) | Средняя сумма сделки                       |



## 2. Источники

| № | Место хранения | Схема          | Таблица | Описание                                               |
|---|----------------|----------------|---------|--------------------------------------------------------|
| 1 | ClickHouse     | marketing      | visits  | Посещение пользователями нашего сайта                  |
| 2 | Postgres       | public         | costs   | Расходы на рекламу                                     |
| 3 | csv            | -              | -       | Словарик с сопоставлением рекламных кампаний           |
| 4 | HDFS           | website_events | submits | Заполненные формы на сайте для заявки/обратного звонка |
| 5 | HDFS           | system_events  | deals   | Заказанные дизайн-проекты                              |


## 3. Методология расчета

### visits (диалект ClickHouse)

```
with filtered_step1 as (
	select
		visitDateTime::date as dt,
		visitid,
		clientID,
		URL,
		duration,
		source,
		UTMCampaign,
		params,
		replaceRegexpAll(params, '\[|\]', '') as params_regex,
		splitByString(', ', replaceRegexpAll(params, '\[|\]', '')) as params_split
	from marketing.visits
	where visitDateTime >= '2024-01-01' and visitDateTime < '2025-01-28'
	and source in ('ad', 'direct')
	and (
		match(URL, '.*checkout.*') or
		match(URL, '.*add.*') or
		match(URL, '.*home.*') or
		match(URL, '.*contact.*') or
		match(URL, '.*top50.*') or
		match(URL, '.*customer-service.*') or
		match(URL, '.*wishlist.*') or
		match(URL, '.*sale.*') or
		match(URL, '.*best-sellers.*') or
		match(URL, '.*view.*') or
		match(URL, '.*discount.*') or
		match(URL, '.*featured.*') or
		match(URL, '.*new-arrivals.*') or
		match(URL, '.*settings.*') or
		match(URL, '.*return-policy.*') or
		match(URL, '.*edit.*') or
		match(URL, '.*delete.*') or
		match(URL, '.*reviews.*') or
		match(URL, '.*products.*') or
		match(URL, '.*about.*')
	)
),
filtered_step2 as (
	select *,
	replaceAll(params_split[1], '\'', '') as event_type,
	toInt32OrNull(params_split[2]) as event_id
	from filtered_step1
)
select
	dt,
	visitid,
	clientID,
	URL,
	duration,
	source,
	UTMCampaign,
	event_type,
	event_id
from filtered_step2
where event_type = 'submit';
```

### costs (диалект Postgres)

```
select
	date,
	campaign_id,
	round(sum(costs)::numeric, 2) as costs,
	sum(clicks) as clicks,
	sum(views) as views
from public.costs
group by date, campaign_id
order by date, campaign_id;
```

### submits (Spark SQL)

```
submits = spark.sql("""
    SELECT
        submit_id,
        name,
        CAST(phone AS STRING) AS phone,
        CONCAT('+', phone) AS phone_plus,
        MD5(CAST(phone AS STRING)) AS phone_md5,
        MD5(CONCAT('+', phone)) AS phone_plus_md5
    FROM website_events.submits
""")
```

### deals (pandas)

```
deals_pdf = spark.table('system_events.deals').toPandas()
deals_pdf[['username', 'domain']] = deals_pdf['email'].str.split('@', expand=True)
filtered_deals_pdf = deals_pdf[deals_pdf['domain'].isin(['example.com', 'example.org', 'example.net'])]
```

## 4. Логика сбора финальной витрины

Легенда:
- фиолетовый - источники
- бирюзовый - промежуточные таблицы
- бордовый - очищенные и подготовленные датафреймы
- синий - условия соединений
- зеленый - итоговые таблицы

![customer_detailed drawio (2)](https://github.com/user-attachments/assets/ace94611-8638-42bb-87d8-f0f5d67a984b)
