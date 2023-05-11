SELECT i.rest_id, rest_name, food_type, favorites, address, round(avg(REVIEW_SCORE),2) as score
from rest_info i join rest_review r
on i.rest_id = r.rest_id 
group by rest_id
having address like '서울%'
order by score desc, favorites desc
