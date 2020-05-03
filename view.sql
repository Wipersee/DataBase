CREATE OR REPLACE VIEW region_sales AS
    SELECT company
    ,ROUND(sum(NA_sales)) AS NA_sales
    ,ROUND(sum(EU_sales)) AS EU_sales
    ,ROUND(sum(JP_sales)) AS JP_sales
    ,ROUND(sum(Other_sales)) AS Other_sales
    FROM game
    INNER JOIN companies using(company_id)
    INNER JOIN sales using(game_rank)
    GROUP BY company;
