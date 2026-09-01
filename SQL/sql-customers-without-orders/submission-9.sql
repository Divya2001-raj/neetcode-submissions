-- Write your query below
-- select c.name from customers c
-- left join orders o 
-- on c.id=o.customer_id 
-- where o.customer_id is null

select c.name from customers c 
where not exists (
    select 1 from orders o 
    where o.customer_id = c.id
)
