create table meal(id INT, meal_name VARCHAR(100));
create table drink(id INT, drink_name VARCHAR(100));

insert into meal values (1, "omelet"), (2, "fried egg"), (3, "sausage"), (4, "bacon");
insert into drink values (1, "orange juice"), (2, "tea"), (3, "coffee");

select * from drink;

select meal_name, drink_name
from meal
cross join drink