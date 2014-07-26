select a.row_num, b.col_num, sum(a.value*b.value) as similarity from
(select docid as row_num, term as col_num, count as value from frequency
UNION
SELECT 'q' as row_num, 'washington' as col_num, 1 as value
UNION
SELECT 'q' as row_num, 'taxes' as col_num, 1 as value
UNION
SELECT 'q' as row_num, 'treasury' as col_num, 1 as value
) a,
(select docid as col_num, term as row_num, count as value from frequency
UNION
SELECT 'q' as col_num, 'washington' as row_num, 1 as value
UNION
SELECT 'q' as col_num, 'taxes' as row_num, 1 as value
UNION
SELECT 'q' as col_num, 'treasury' as row_num, 1 as value
) b
 where a.col_num=b.row_num and b.col_num = 'q'
 group by a.row_num,b.col_num
order by similarity desc limit 1;