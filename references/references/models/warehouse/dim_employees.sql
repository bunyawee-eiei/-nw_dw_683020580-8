select
    employee_id,
    company_name,
    first_name,
    last_name,
    email_address,
    job_title,
    business_phone,
    address,
    city,
    state_province,
    postal_code,
    country
from {{ ref('stg_employees') }}
