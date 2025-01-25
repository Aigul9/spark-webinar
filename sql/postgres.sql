create table costs(
    date date,
    campaign_id int,
    costs float,
    clicks int,
    views int
)

COPY costs
FROM 'E:\\EDesktop\\Webinar\\data\\campaign_data_postgres.csv'
DELIMITER ','
CSV Header;

select * from costs;

select
    date,
    campaign_id,
    round(sum(costs)::numeric, 2) as costs,
    sum(clicks) as clicks,
    sum(views) as views
from costs
group by date, campaign_id
order by date, campaign_id;
