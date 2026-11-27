select
    cast(id as integer) as product_id,
    nullif(trim(product_code), '') as product_code,
    nullif(trim(product_name), '') as product_name,
    nullif(trim(category), '') as category,
    cast(standard_cost as decimal(12, 2)) as standard_cost,
    cast(list_price as decimal(12, 2)) as list_price,
    cast(discontinued as boolean) as is_discontinued,
    nullif(trim(supplier_ids), '') as supplier_ids
from {{ source('raw', 'products') }}
