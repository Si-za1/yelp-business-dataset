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

