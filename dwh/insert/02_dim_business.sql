INSERT INTO dwh.dim_business(
    business_id,
    name,
    address,
    category,
    city,
    state,
    review_count,
    stars,
    hours
)
SELECT
    business_id,
    name,
    address,
    string_to_array(categories, ',') as category,
    city,
    state,
    review_count::integer,
    stars::float,
    string_to_array(hours, ',') as hours
FROM raw.business;
