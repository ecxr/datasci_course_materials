select count(*) from (
       SELECT Frequency.docid AS TermCount FROM Frequency 
       GROUP BY Frequency.docid 
       HAVING SUM(Frequency.count) > 300
) x;
