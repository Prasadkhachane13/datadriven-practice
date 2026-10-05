SELECT
  pipe_name
FROM data_pipes
WHERE dur_secs IS NOT NULL
ORDER BY dur_secs DESC, start_at
LIMIT 1
