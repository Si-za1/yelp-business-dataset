INSERT INTO raw.review
VALUES 
(
  %(review_id)s,
  %(user_id)s,
  %(business_id)s,
  %(stars)s,
  %(date)s,
  %(text)s,
  %(useful)s,
  %(funny)s,
  %(cool)s
);