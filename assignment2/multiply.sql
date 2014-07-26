SELECT val FROM (
       SELECT a.row_num r, b.col_num c, SUM(a.value * b.value) AS val
       FROM a, b
       WHERE a.col_num = B.row_num
       GROUP BY a.row_num, b.col_num
       HAVING r=2 AND c=3
);