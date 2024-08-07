
SELECT a.id, a.name, SUM(jsonb_array_length(b.data->'list')) AS total_elements
FROM a
LEFT JOIN b ON a.id = b.a_id
GROUP BY a.id, a.name;
