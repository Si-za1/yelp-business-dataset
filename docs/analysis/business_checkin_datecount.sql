SELECT
    business_id,
    COUNT(DISTINCT DATE(timestamp_date::timestamp)) AS total_dates
FROM
    raw.checkin,
    LATERAL unnest(string_to_array(date, ', ')) AS timestamp_date
GROUP BY
    business_id
LIMIT 5;
