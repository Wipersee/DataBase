select realease_year, (sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales)) as SUMMARY_SALES
from game
inner join release_year using(year_id)
inner join sales using(game_rank)
GROUP BY realease_year;

---
select sum(NA_sales) as SUMMARY_NA_sales, sum(EU_sales) as SUMMARY_EU_sales, sum(JP_sales) as SUMMARY_JP_sales, sum(Other_sales) as SUMMARY_Other_sales from
(select company
,ROUND(sum(NA_sales))as NA_sales
,ROUND(sum(EU_sales))as EU_sales
,ROUND(sum(JP_sales)) as JP_sales
,ROUND(sum(Other_sales)) as Other_sales
from game
inner join companies using(company_id)
inner join sales using(game_rank)
GROUP BY company);

select realease_year as YEAR_OF_REALES, count(name_of_game) as AMOUNT_OF_REALESES
from game
inner join release_year using(year_id)
group by realease_year;
