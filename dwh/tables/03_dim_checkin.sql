-- Drop the existing dim_checkin table if it exists
DROP TABLE IF EXISTS dwh.dim_checkin CASCADE;

-- Create the dim_checkin table with the correct schema
CREATE TABLE dwh.dim_checkin (
    business_id VARCHAR REFERENCES dwh.dim_business(business_id),
    date TEXT[]
);
