select
    details.order_line_id,
    orders.order_id,
    orders.customer_id,
    orders.employee_id,
    orders.shipper_id,
    cast(strftime(orders.order_date, '%Y%m%d') as integer) as order_date_key,
    details.product_id,
    details.quantity,
    details.unit_price,
    coalesce(details.discount, 0) as discount,
    details.quantity * details.unit_price as gross_sales,
    details.quantity * details.unit_price
        * (1 - coalesce(details.discount, 0)) as net_sales
from {{ ref('stg_order_details') }} as details
inner join {{ ref('stg_orders') }} as orders
    on details.order_id = orders.order_id
