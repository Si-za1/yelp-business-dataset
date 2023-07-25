DROP TABLE IF EXISTS dwh.dim_checkin;

CREATE TABLE dwh.dim_checkin (
    business_id VARCHAR REFERENCES dwh.dim_business(business_id),
    date TIMESTAMP
);