SELECT member_id, member_name, gender, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
from member_profile
where month(date_of_birth) = 3 and tlno is not null and gender = 'W'
order by member_id
