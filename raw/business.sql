DROP TABLE IF EXISTS raw.business;
CREATE TABLE raw.business (
    business_id VARCHAR,
    name VARCHAR,
    address VARCHAR,
    city VARCHAR,
    state VARCHAR,
    postal_code VARCHAR,
    latitude VARCHAR,
    longitude VARCHAR,
    stars VARCHAR,
    review_count VARCHAR,
    is_open VARCHAR,
    attributes JSON,
    categories VARCHAR,
    hours VARCHAR
)