select
    cast(id as integer) as supplier_id,
    nullif(trim(company), '') as company_name,
    nullif(trim(first_name), '') as contact_first_name,
    nullif(trim(last_name), '') as contact_last_name,
    nullif(trim(email_address), '') as email_address,
    nullif(trim(job_title), '') as job_title,
    nullif(trim(business_phone), '') as business_phone,
    nullif(trim(address), '') as address,
    nullif(trim(city), '') as city,
    nullif(trim(state_province), '') as state_province,
    nullif(trim(cast(zip_postal_code as varchar)), '') as postal_code,
    nullif(trim(country_region), '') as country
from {{ source('raw', 'suppliers') }}
