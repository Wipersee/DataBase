select realease_year, (sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales)) as SUMMARY_SALES
from game
inner join release_year using(year_id)
inner join sales using(game_rank)
GROUP BY realease_year;


select company
,ROUND(sum(NA_sales)/(sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales))*100,2)||'%' as NA_sales
,ROUND(sum(EU_sales)/(sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales))*100,2)||'%' as EU_sales
,ROUND(sum(JP_sales)/(sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales))*100,2)||'%' as JP_sales
,ROUND(sum(Other_sales)/(sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales))*100,2)||'%' as Other_sales
from game
inner join companies using(company_id)
inner join sales using(game_rank)
GROUP BY company;

select realease_year as YEAR_OF_REALES, count(name_of_game) as AMOUNT_OF_REALESES
from game
inner join release_year using(year_id)
group by realease_year;
