select count(*) from (
       select docid from Frequency WHERE term="transactions" 
       INTERSECT 
       select docid from Frequency WHERE term="world"
) x;

