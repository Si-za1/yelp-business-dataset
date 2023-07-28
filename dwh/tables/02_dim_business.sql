DROP TABLE IF EXISTS dwh.dim_business CASCADE;
CREATE TABLE dwh.dim_business (
    business_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    address VARCHAR,
    city VARCHAR,
    state VARCHAR,
    stars FLOAT,
    review_count INT,
    category TEXT[],
    hours TEXT[]
)

