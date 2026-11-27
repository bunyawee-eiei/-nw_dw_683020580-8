select
    shipper_id,
    shipper_name,
    business_phone
from {{ ref('stg_shippers') }}
