-- displays the top 3 of cities temperature during
-- July and August ordered by temperature (descending)
SELECT city, AVG(`value`) AS `avg_tmp`
FROM `temperatures`
WHERE `month` IN (6, 7)
ORDER BY `temperature` DESC
LIMIT 3;

