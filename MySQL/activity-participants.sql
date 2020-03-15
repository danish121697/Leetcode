SELECT activity 
FROM   friends 
GROUP  BY activity 
HAVING Count(*) NOT IN (SELECT Max(counts) 
                        FROM   (SELECT Count(*) AS counts 
                                FROM   friends 
                                GROUP  BY activity ) a 
                        UNION ALL 
                        SELECT Min(counts) 
                        FROM   (SELECT Count(*) AS counts 
                                FROM   friends 
                                GROUP  BY activity ) b) 
