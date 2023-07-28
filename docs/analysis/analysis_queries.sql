-- highest rating business
SELECT business_id, name, stars
FROM dwh.dim_business
ORDER BY stars DESC
LIMIT 5;

-- TOP 10 users who have given most reviews 
SELECT *
FROM dwh.dim_users
ORDER BY review_count DESC, average_stars DESC
LIMIT 10;

-- repeated customers who have given more than one review 
SELECT user_id, COUNT(*) as num_reviews
FROM dwh.fact_review
GROUP BY user_id
HAVING COUNT(*) > 1
LIMIT 10;

-- business sucess and impact 
SELECT r.business_id, b.name, b.category, b.stars as business_stars,
       COUNT(r.review_id) as num_reviews_by_repeat_customers,
       AVG(r.stars) as average_rating_by_repeat_customers
FROM dwh.fact_review r
JOIN (
    SELECT user_id
    FROM dwh.fact_review
    GROUP BY user_id
    HAVING COUNT(*) > 1
) repeat_users ON r.user_id = repeat_users.user_id
JOIN dwh.dim_business b ON r.business_id = b.business_id
GROUP BY r.business_id, b.name, b.category, b.stars
ORDER BY num_reviews_by_repeat_customers DESC;


-- Busiest Business Categories:
SELECT b.category, COUNT(*) AS total_checkins
FROM dwh.dim_checkin c
JOIN dwh.dim_business b ON c.business_id = b.business_id
GROUP BY b.category
ORDER BY total_checkins DESC;


-- avg checkin per business 
SELECT AVG(average_checkins_per_day) AS average_checkins_per_business
FROM (
  SELECT c.business_id, b.name, COUNT(*) AS total_checkins,
         COUNT(*) / COUNT(DISTINCT date) AS average_checkins_per_day
  FROM dwh.dim_checkin c
  JOIN dwh.dim_business b ON c.business_id = b.business_id
  GROUP BY c.business_id, b.name
) subquery;

-- peak hour 
SELECT c.business_id, b.name, date, COUNT(*) AS checkins_on_date
FROM dwh.dim_checkin c
JOIN dwh.dim_business b ON c.business_id = b.business_id
GROUP BY c.business_id, b.name, date
ORDER BY checkins_on_date DESC;

-- peak time 
WITH checkin_data AS (
  SELECT c.business_id, b.name, date, COUNT(*) AS checkins_on_date
  FROM dwh.dim_checkin c
  JOIN dwh.dim_business b ON c.business_id = b.business_id
  GROUP BY c.business_id, b.name, date
)
SELECT business_id, name, date
FROM checkin_data
WHERE checkins_on_date = (
  SELECT MAX(checkins_on_date)
  FROM checkin_data
);


-- 

WITH checkin_data AS (
  SELECT c.business_id, b.name, date, COUNT(*) AS checkins_on_date
  FROM dwh.dim_checkin c
  JOIN dwh.dim_business b ON c.business_id = b.business_id
  GROUP BY c.business_id, b.name, date
)
SELECT 
  business_id, 
  name,
  UNNEST(date) AS checkin_date,
  SUBSTRING(UNNEST(date) FROM '\d{2}:\d{2}:\d{2}') AS extracted_time
FROM checkin_data;


-- max time 

WITH checkin_data AS (
  SELECT c.business_id, b.name, date, COUNT(*) AS checkins_on_date
  FROM dwh.dim_checkin c
  JOIN dwh.dim_business b ON c.business_id = b.business_id
  GROUP BY c.business_id, b.name, date
),
extracted_times AS (
  SELECT 
    business_id, 
    name,
    UNNEST(date) AS checkin_date,
    SUBSTRING(UNNEST(date) FROM '\d{2}:\d{2}:\d{2}') AS extracted_time
  FROM checkin_data
)
SELECT 
  business_id,
  name,
  extracted_time,
  COUNT(extracted_time) AS time_frequency
FROM extracted_times
GROUP BY business_id, name, extracted_time
ORDER BY time_frequency DESC
LIMIT 2;


-- for each business peak time 
WITH checkin_data AS (
  SELECT c.business_id, b.name, date, COUNT(*) AS checkins_on_date
  FROM dwh.dim_checkin c
  JOIN dwh.dim_business b ON c.business_id = b.business_id
  GROUP BY c.business_id, b.name, date
),
extracted_times AS (
  SELECT 
    business_id, 
    name,
    UNNEST(date) AS checkin_date,
    SUBSTRING(UNNEST(date) FROM '\d{2}:\d{2}:\d{2}') AS extracted_time
  FROM checkin_data
)
SELECT 
  business_id,
  name,
  extracted_time,
  COUNT(extracted_time) AS time_frequency
FROM extracted_times
GROUP BY business_id, name, extracted_time
ORDER BY business_id, time_frequency DESC;


-- peak time for top 5 business

WITH checkin_data AS (
  SELECT c.business_id, b.name, date, COUNT(*) AS checkins_on_date
  FROM dwh.dim_checkin c
  JOIN dwh.dim_business b ON c.business_id = b.business_id
  GROUP BY c.business_id, b.name, date
),
extracted_times AS (
  SELECT 
    business_id, 
    name,
    UNNEST(date) AS checkin_date,
    SUBSTRING(UNNEST(date) FROM '\d{2}:\d{2}:\d{2}') AS extracted_time
  FROM checkin_data
),
time_frequency_rank AS (
  SELECT
    business_id,
    name,
    extracted_time,
    COUNT(extracted_time) AS time_frequency,
    ROW_NUMBER() OVER (PARTITION BY business_id ORDER BY COUNT(extracted_time) DESC) AS rank
  FROM extracted_times
  GROUP BY business_id, name, extracted_time
)
SELECT 
  business_id,
  name,
  extracted_time,
  time_frequency
FROM time_frequency_rank
WHERE rank <= 5;


