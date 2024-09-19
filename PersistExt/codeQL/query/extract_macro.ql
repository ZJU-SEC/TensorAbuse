import cpp


from MacroInvocation mi
where mi.getMacroName() = "REGISTER_KERNEL_BUILDER"
select mi, mi.getActualLocation()