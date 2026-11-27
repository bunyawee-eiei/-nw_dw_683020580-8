select
    cast(id as integer) as shipper_id,
    nullif(trim(company), '') as shipper_name,
    nullif(trim(business_phone), '') as business_phone
from {{ source('raw', 'shippers') }}
