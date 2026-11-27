select distinct
    cast(strftime(order_date, '%Y%m%d') as integer) as date_key,
    order_date as date_day,
    extract(year from order_date)::integer as year,
    extract(quarter from order_date)::integer as quarter,
    extract(month from order_date)::integer as month,
    extract(day from order_date)::integer as day
from {{ ref('stg_orders') }}
where order_date is not null
