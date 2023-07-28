DROP table dwh.fact_review;

CREATE TABLE dwh.fact_review(
    review_id varchar primary key,
    business_id varchar references dwh.dim_business(business_id),
    user_id varchar references dwh.dim_users(user_id),
    stars float,
    useful int,
    funny int,
    cool int,
    date timestamp
)


INSERT INTO dwh.fact_review (
  review_id,
  business_id,
  user_id,
  stars,
  useful,
  funny,
  cool,
  date
)
SELECT
  review_id,
  business_id,
  user_id,
  stars::float,
  useful::int,
  funny::int,
  cool::int,
  date::timestamp
FROM raw.review
WHERE user_id IN (SELECT user_id FROM dwh.dim_users);