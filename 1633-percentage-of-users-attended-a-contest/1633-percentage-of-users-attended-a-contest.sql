# Write your MySQL query statement below
select contest_id,round(
    count(user_id )*100.0 / (select COUNT(*) FROM Users),2
    ) as percentage
    from register
    group by contest_id
    ORDER BY percentage DESC, contest_id ASC;