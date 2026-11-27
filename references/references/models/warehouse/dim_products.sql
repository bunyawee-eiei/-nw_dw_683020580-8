select
    product_id,
    product_code,
    product_name,
    category,
    standard_cost,
    list_price,
    is_discontinued,
    supplier_ids
from {{ ref('stg_products') }}
