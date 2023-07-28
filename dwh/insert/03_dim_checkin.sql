-- Insert data into the dim_checkin table
INSERT INTO dwh.dim_checkin (
    business_id,
    date
)
SELECT
    business_id,
    string_to_array(date, ',') as date
FROM raw.checkin;