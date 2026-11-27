select
    cast(id as integer) as order_id,
    cast(employee_id as integer) as employee_id,
    cast(customer_id as integer) as customer_id,
    try_strptime(
        nullif(trim(cast(order_date as varchar)), ''),
        '%m/%d/%Y %H:%M:%S'
    )::date as order_date,
    try_strptime(
        nullif(trim(cast(shipped_date as varchar)), ''),
        '%m/%d/%Y %H:%M:%S'
    )::date as shipped_date,
    cast(shipper_id as integer) as shipper_id,
    cast(shipping_fee as decimal(12, 2)) as shipping_fee,
    cast(taxes as decimal(12, 2)) as taxes,
    cast(status_id as integer) as status_id
from {{ source('raw', 'orders') }}
