DROP TABLE IF EXISTS dwh.dim_users;

CREATE TABLE dwh.dim_users (
    user_id varchar PRIMARY KEY,
    name VARCHAR,
    review_count INT,
    average_stars FLOAT
    )