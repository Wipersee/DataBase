import cx_Oracle

def print_table(cur, request):
    names = []
    cur.execute(request) 
    for name in cur.description:
        names.append(name[0])
    print(" ; ".join(names))   
    for row in cur:
        print(row)
    print("\n\n")
my_conn = cx_Oracle.connect("hr/11@localhost:1521/orcl")
cursor = my_conn.cursor()


re1 = "select realease_year, (sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales)) as SUMMARY_SALES from game inner join release_year using(year_id) inner join sales using(game_rank) GROUP BY realease_year"
print("---------first query--------")
print_table(cursor, re1)


re2 ="""select company
,ROUND(sum(NA_sales)/(sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales))*100,2)||'%' as NA_sales
,ROUND(sum(EU_sales)/(sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales))*100,2)||'%' as EU_sales
,ROUND(sum(JP_sales)/(sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales))*100,2)||'%' as JP_sales
,ROUND(sum(Other_sales)/(sum(NA_sales)+sum(EU_sales)+sum(JP_sales)+sum(Other_sales))*100,2)||'%' as Other_sales
from game
inner join companies using(company_id)
inner join sales using(game_rank)
GROUP BY company"""
print("-------second query--------")
print_table(cursor, re2)



re3 = """
select realease_year as YEAR_OF_REALES, count(name_of_game) as AMOUNT_OF_REALESES
from game
inner join release_year using(year_id)
group by realease_year
"""
print("-------third query-------\n")
print_table(cursor, re3)

cursor.close()
