 import cpp

 class OpKernelSubclass extends Class {
   OpKernelSubclass() {
     this.getABaseClass*().hasQualifiedName("tensorflow::OpKernel")
   }
 }

 from OpKernelSubclass s, MemberFunction f
 where 
    f.getDeclaringType() = s and 
    not f.isDeclaredVirtual() and 
    ( f.hasName("Compute") or 
      f.hasName("Compile") or
      f.hasName("ComputeAsync") or
      f.hasName("CreateResource") or
      f.hasName("MakeDataset") or
      f.hasName("Operate") or
      f.hasName("Computation") or
      f.hasName("DoCompute") or
      f.hasName("BuildReducer") or
      f.hasName("ComputeMatrix") or
      f.hasName("Combine") or
      f.hasName("ComputeWithReader") or
      f.hasName("Fill") or
      f.hasName("ComputeAsyncImpl") 
    ) 
 select f.getLocation(), s.getSimpleName(), f.getName()