import cpp

from Class c
where 
  c.getABaseClass().getName() = "ReaderBase"
select c, c.getSimpleName() + "Op"