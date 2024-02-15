-- dumping a dump in database
-- display average temp by city
-- descending order
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
