CREATE TABLE marketing.visits
(
    visitid Int32,
    visitDateTime DateTime,
    URL String,
    duration Int32,
    clientID Int32,
    source String,
    UTMCampaign String,
    params String
)
ENGINE = MergeTree
ORDER BY visitDateTime;

select * from marketing.visits;


--match methodology
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
	from sberbank.visits_example
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
