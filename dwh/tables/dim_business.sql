DROP TABLE IF EXISTS dwh.dim_business;
CREATE TABLE dwh.dim_business (
    business_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    address VARCHAR,
    city VARCHAR,
    state VARCHAR,
    stars FLOAT,
    categories VARCHAR,
    hours DATE
)