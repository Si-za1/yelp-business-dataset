DROP TABLE dwh.dim_businesslookup;
CREATE TABLE dwh.dim_businesslookup(
	business_num SERIAL PRIMARY KEY,
	business_id VARCHAR UNIQUE
)

INSERT INTO dwh.dim_businesslookup(
	business_id
)

SELECT 
	business_id 
FROM raw.business;


-- now working on the hours 


-- Step 1: Create the "business_hours_dim" table
TRUNCATE TABLE dwh.business_hours_dim;

CREATE TABLE dwh.business_hours_dim (
    business_id VARCHAR references dwh.dim_businesslookup(business_id),
    day VARCHAR(20),
    opening_time TIME,
    closing_time TIME,
   	PRIMARY KEY (business_id, day) -- Ensures uniqueness of combination (business_id, day)
    
);

-- Step 2: Extract and insert data into the "business_hours_dim" table
-- Step 2: Extract and insert data into the "business_hours_dim" table
INSERT INTO dwh.business_hours_dim (business_id,day, opening_time, closing_time)
SELECT
 business_id,
 -- Assuming there's a column named 'business_num' in the 'raw.business' table.
 TRIM(SUBSTRING(key, 1, LENGTH(key))) AS day,
    (LPAD(SPLIT_PART(value->>'start', ':', 1), 2, '0') || ':' ||
     LPAD(SPLIT_PART(value->>'start', ':', 2), 2, '0'))::TIME AS opening_time,
    (LPAD(SPLIT_PART(value->>'end', ':', 1), 2, '0') || ':' ||
     LPAD(SPLIT_PART(value->>'end', ':', 2), 2, '0'))::TIME AS closing_time
FROM raw.business,
     LATERAL jsonb_each_text(hours::jsonb) AS kv;

SELECT * 
FROM dwh.business_hours_dim
LIMIT 20;

-- Step 3: Optional - Index the "business_id" column for better query performance
CREATE INDEX idx_business_hours_dim_business_id ON business_hours_dim (business_id);
