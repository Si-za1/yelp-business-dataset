-- Drop the existing dim_checkin table if it exists
DROP TABLE IF EXISTS dwh.dim_checkin CASCADE;

-- Create the dim_checkin table with the correct schema
CREATE TABLE dwh.dim_checkin (
    business_id VARCHAR REFERENCES dwh.dim_business(business_id),
    date TEXT[]
);

-- Insert data into the dim_checkin table
INSERT INTO dwh.dim_checkin (
    business_id,
    date
)
SELECT
    business_id,
    string_to_array(date, ',') as date
FROM raw.checkin;


SELECT * FROM dwh.dim_users
LIMIT 2;



-- users
Insert into dwh.dim_users (
    user_id ,
    name ,
    review_count,
    average_stars 
)

SELECT 
	user_id AS user_id,
	name AS user_name,
	review_count::INT AS review_count,
	average_stars::FLOAT AS avg_stars
FROM raw.users;

SELECT * FROM dwh.fact_review 
LIMIT 5;

