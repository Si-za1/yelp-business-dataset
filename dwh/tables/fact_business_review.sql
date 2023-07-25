DROP TABLE IF EXISTS dwh.fact_review;
CREATE TABLE dwh.fact_review (
    review_id VARCHAR PRIMARY KEY,
    user_id  VARCHAR References dwh.dim_user(user_id),
    business_id VARCHAR References dwh.dim_business(business_id),
    stars FLOAT,
    date DATE
);