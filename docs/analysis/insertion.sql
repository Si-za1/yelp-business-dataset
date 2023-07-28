-- user_inserted 
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

-- SELECT * FROM raw.business
-- LIMIT 10;




-- INSERT INTO dwh.fact_review (
--     review_id,
--     user_id  ,
--     business_id ,
--     stars,
--     date 
-- )

-- SELECT 
--     review_id,
--     user_id,
--     business_id,
--     stars::FLOAT AS stars,
--     date::TIMESTAMP AS date
 
-- FROM raw.review  ;
