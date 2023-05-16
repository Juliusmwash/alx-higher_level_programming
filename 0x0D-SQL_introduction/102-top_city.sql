-- displays the top 3 of cities temperature during
-- July and August ordered by temperature (descending)
SELECT city, AVG(`value`) AS `avg_tmp`
FROM `temperatures`
WHERE `month` IN ('July', 'August')
GROUP BY `city`
ORDER BY `temperature` DESC
LIMIT 3;

