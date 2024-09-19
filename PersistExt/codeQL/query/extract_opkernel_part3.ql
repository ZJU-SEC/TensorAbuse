import cpp

from Class c
where
  ( c.getABaseClass().getName() = "ConcatBaseOp" or
  c.getABaseClass().getName() = "GenericFftOp" or
  c.getABaseClass().getName() = "ScanOp" or
  c.getABaseClass().getName() = "BaseCandidateSamplerOp" or
  c.getABaseClass().getName() = "XlaArgMinMaxOp" 
  )
select c, c.getSimpleName()