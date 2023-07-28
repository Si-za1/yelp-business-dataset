DROP TABLE IF EXISTS dwh.fact_review CASCADE;
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

