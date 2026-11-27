select
    cast(id as integer) as order_line_id,
    cast(order_id as integer) as order_id,
    cast(product_id as integer) as product_id,
    cast(quantity as integer) as quantity,
    cast(unit_price as decimal(12, 2)) as unit_price,
    cast(discount as decimal(8, 4)) as discount
from {{ source('raw', 'order_details') }}
