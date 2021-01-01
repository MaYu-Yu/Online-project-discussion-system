select * from direction, project where direction.direction_id=project.id/*進專案之後會顯示所有跟這專案有關的面向*/
select * from opinion, direction where opinion.direction_id=direction.id/**/