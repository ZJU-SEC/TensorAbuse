��
��
^
AssignVariableOp
resource
value"dtype"
dtypetype"
validate_shapebool( �
8
Const
output"dtype"
valuetensor"
dtypetype
$
DisableCopyOnRead
resource�
.
Identity

input"T
output"T"	
Ttype
�
MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool("
allow_missing_filesbool( �

NoOp
M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
@
ReadVariableOp
resource
value"dtype"
dtypetype�
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0�
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0�
?
Select
	condition

t"T
e"T
output"T"	
Ttype
H
ShardedFilename
basename	
shard

num_shards
filename
�
StatefulPartitionedCall
args2Tin
output2Tout"
Tin
list(type)("
Tout
list(type)("	
ffunc"
configstring "
config_protostring "
executor_typestring ��
@
StaticRegexFullMatch	
input

output
"
patternstring
L

StringJoin
inputs*N

output"

Nint("
	separatorstring 
�
VarHandleOp
resource"
	containerstring "
shared_namestring "

debug_namestring "
dtypetype"
shapeshape"#
allowed_deviceslist(string)
 �"serve*2.15.02v2.15.0-rc1-8-g6887368d6d48�q

VariableVarHandleOp*
_output_shapes
: *

debug_name	Variable/*
dtype0*
shape: *
shared_name
Variable
]
Variable/Read/ReadVariableOpReadVariableOpVariable*
_output_shapes
: *
dtype0
�

Variable_1VarHandleOp*
_output_shapes
: *

debug_nameVariable_1/*
dtype0*
shape: *
shared_name
Variable_1
a
Variable_1/Read/ReadVariableOpReadVariableOp
Variable_1*
_output_shapes
: *
dtype0

NoOpNoOp
�
ConstConst"/device:CPU:0*
_output_shapes
: *
dtype0*�
value�B� B�
0
a
b
__call__

signatures*
@:
VARIABLE_VALUE
Variable_1a/.ATTRIBUTES/VARIABLE_VALUE*
>8
VARIABLE_VALUEVariableb/.ATTRIBUTES/VARIABLE_VALUE*

trace_0* 
* 
* 
O
saver_filenamePlaceholder*
_output_shapes
: *
dtype0*
shape: 
�
StatefulPartitionedCallStatefulPartitionedCallsaver_filename
Variable_1VariableConst*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8� *%
f R
__inference__traced_save_150
�
StatefulPartitionedCall_1StatefulPartitionedCallsaver_filename
Variable_1Variable*
Tin
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8� *(
f#R!
__inference__traced_restore_165�f
�
�
__inference___call___118
x!
readvariableop_resource: %
add_readvariableop_resource: 
identity��AnonymousIteratorV3�MakeIterator�MatchingFilesDataset�ReadVariableOp�add/ReadVariableOp�whiled
MatchingFilesDataset/patternsConst*
_output_shapes
: *
dtype0*
valueB B./*.py
MatchingFilesDatasetMatchingFilesDataset&MatchingFilesDataset/patterns:output:0*
_output_shapes
: :�N���
AnonymousIteratorV3AnonymousIteratorV3^MatchingFilesDataset*'
_class
loc:@MatchingFilesDataset*
_output_shapes
: *
output_shapes
: *
output_types
2:	�N �
MakeIteratorMakeIteratorMatchingFilesDataset:handle:0AnonymousIteratorV3:handle:0*'
_class
loc:@MatchingFilesDataset*
_output_shapes
 :G
ConstConst*
_output_shapes
: *
dtype0
*
value	B
 Zc
while/maximum_iterationsConst*
_output_shapes
: *
dtype0*
valueB :
���������T
while/loop_counterConst*
_output_shapes
: *
dtype0*
value	B : �
whileWhilewhile/loop_counter:output:0!while/maximum_iterations:output:0Const:output:0AnonymousIteratorV3:handle:0^MakeIterator*
T
2
*
_lower_using_switch_merge(*
_num_original_outputs*
_output_shapes

: : : : * 
_read_only_resource_inputs
 *
bodyR
while_body_71*
condR
while_cond_70*
output_shapes

: : : : ^
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes
: *
dtype0F
mulMulReadVariableOp:value:0x*
T0*
_output_shapes
: f
add/ReadVariableOpReadVariableOpadd_readvariableop_resource*
_output_shapes
: *
dtype0R
addAddV2mul:z:0add/ReadVariableOp:value:0*
T0*
_output_shapes
: E
IdentityIdentityadd:z:0^NoOp*
T0*
_output_shapes
: �
NoOpNoOp^AnonymousIteratorV3^MakeIterator^MatchingFilesDataset^ReadVariableOp^add/ReadVariableOp^while*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: : : 2*
AnonymousIteratorV3AnonymousIteratorV32
MakeIteratorMakeIterator2,
MatchingFilesDatasetMatchingFilesDataset2 
ReadVariableOpReadVariableOp2(
add/ReadVariableOpadd/ReadVariableOp2
whilewhile:($
"
_user_specified_name
resource:($
"
_user_specified_name
resource:9 5

_output_shapes
: 

_user_specified_namex
�
�
while_cond_70
while_while_loop_counter"
while_while_maximum_iterations
while_placeholder
0
,while_while_cond_70___redundant_placeholder0
while_identity
N
while/IdentityIdentitywhile_placeholder*
T0
*
_output_shapes
: ")
while_identitywhile/Identity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes

: : : ::

_output_shapes
: :PL

_output_shapes
: 
2
_user_specified_namewhile/maximum_iterations:J F

_output_shapes
: 
,
_user_specified_namewhile/loop_counter
�
�
while_body_71
while_while_loop_counter"
while_while_maximum_iterations
while_placeholder
9
5while_iteratorgetnextasoptional_anonymousiteratorv3_0
while_identity
while_identity_1
while_identity_2
7
3while_iteratorgetnextasoptional_anonymousiteratorv3��while/IteratorGetNextAsOptional�
while/cond�
while/IteratorGetNextAsOptionalIteratorGetNextAsOptional5while_iteratorgetnextasoptional_anonymousiteratorv3_0*'
_class
loc:@MatchingFilesDataset*
_output_shapes
: *
output_shapes
: *
output_types
2:����
while/OptionalHasValueOptionalHasValue*while/IteratorGetNextAsOptional:optional:0*'
_class
loc:@MatchingFilesDataset*
_output_shapes
: �

while/condIf"while/OptionalHasValue:has_value:0*while/IteratorGetNextAsOptional:optional:0"while/OptionalHasValue:has_value:0*
Tcond0
*
Tin
2
*
Tout
2
*
_lower_using_switch_merge(*
_output_shapes
: * 
_read_only_resource_inputs
 *&
else_branchR
while_cond_false_87*
output_shapes
: *%
then_branchR
while_cond_true_86U
while/cond/IdentityIdentitywhile/cond:output:0*
T0
*
_output_shapes
: M
while/ConstConst*
_output_shapes
: *
dtype0
*
value	B
 ZM
while/add/yConst*
_output_shapes
: *
dtype0*
value	B :c
	while/addAddV2while_while_loop_counterwhile/add/y:output:0*
T0*
_output_shapes
: W
while/IdentityIdentitywhile/add:z:0^while/NoOp*
T0*
_output_shapes
: j
while/Identity_1Identitywhile_while_maximum_iterations^while/NoOp*
T0*
_output_shapes
: h
while/Identity_2Identitywhile/cond/Identity:output:0^while/NoOp*
T0
*
_output_shapes
: W

while/NoOpNoOp ^while/IteratorGetNextAsOptional^while/cond*
_output_shapes
 "-
while_identity_1while/Identity_1:output:0"-
while_identity_2while/Identity_2:output:0")
while_identitywhile/Identity:output:0"l
3while_iteratorgetnextasoptional_anonymousiteratorv35while_iteratorgetnextasoptional_anonymousiteratorv3_0*(
_construction_contextkEagerRuntime*
_input_shapes

: : : : 2B
while/IteratorGetNextAsOptionalwhile/IteratorGetNextAsOptional2

while/cond
while/cond:\X
'
_class
loc:@MatchingFilesDataset
-
_user_specified_nameAnonymousIteratorV3:

_output_shapes
: :PL

_output_shapes
: 
2
_user_specified_namewhile/maximum_iterations:J F

_output_shapes
: 
,
_user_specified_namewhile/loop_counter
�
z
while_cond_false_87
while_cond_placeholder.
*while_cond_identity_while_optionalhasvalue

while_cond_identity
l
while/cond/IdentityIdentity*while_cond_identity_while_optionalhasvalue*
T0
*
_output_shapes
: "3
while_cond_identitywhile/cond/Identity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: : :NJ

_output_shapes
: 
0
_user_specified_namewhile/OptionalHasValue: 

_output_shapes
: 
�	
�
while_cond_true_86?
;while_cond_optionalgetvalue_while_iteratorgetnextasoptional.
*while_cond_identity_while_optionalhasvalue

while_cond_identity
��while/cond/PrintV2�
while/cond/OptionalGetValueOptionalGetValue;while_cond_optionalgetvalue_while_iteratorgetnextasoptional*'
_class
loc:@MatchingFilesDataset*
_output_shapes
: *
output_shapes
: *
output_types
2]
while/cond/PrintV2PrintV2(while/cond/OptionalGetValue:components:0*
_output_shapes
 R
while/cond/ConstConst*
_output_shapes
: *
dtype0
*
value	B
 Z~
while/cond/IdentityIdentity*while_cond_identity_while_optionalhasvalue^while/cond/NoOp*
T0
*
_output_shapes
: B
while/cond/NoOpNoOp^while/cond/PrintV2*
_output_shapes
 "3
while_cond_identitywhile/cond/Identity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: : 2(
while/cond/PrintV2while/cond/PrintV2:NJ

_output_shapes
: 
0
_user_specified_namewhile/OptionalHasValue:� |
'
_class
loc:@MatchingFilesDataset

_output_shapes
: 
9
_user_specified_name!while/IteratorGetNextAsOptional
�
�
__inference__traced_save_150
file_prefix+
!read_disablecopyonread_variable_1: +
!read_1_disablecopyonread_variable: 
savev2_const

identity_5��MergeV2Checkpoints�Read/DisableCopyOnRead�Read/ReadVariableOp�Read_1/DisableCopyOnRead�Read_1/ReadVariableOpw
StaticRegexFullMatchStaticRegexFullMatchfile_prefix"/device:CPU:**
_output_shapes
: *
pattern
^s3://.*Z
ConstConst"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B.parta
Const_1Const"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B
_temp/part�
SelectSelectStaticRegexFullMatch:output:0Const:output:0Const_1:output:0"/device:CPU:**
T0*
_output_shapes
: f

StringJoin
StringJoinfile_prefixSelect:output:0"/device:CPU:**
N*
_output_shapes
: L

num_shardsConst*
_output_shapes
: *
dtype0*
value	B :f
ShardedFilename/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B : �
ShardedFilenameShardedFilenameStringJoin:output:0ShardedFilename/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: s
Read/DisableCopyOnReadDisableCopyOnRead!read_disablecopyonread_variable_1"/device:CPU:0*
_output_shapes
 �
Read/ReadVariableOpReadVariableOp!read_disablecopyonread_variable_1^Read/DisableCopyOnRead"/device:CPU:0*
_output_shapes
: *
dtype0a
IdentityIdentityRead/ReadVariableOp:value:0"/device:CPU:0*
T0*
_output_shapes
: Y

Identity_1IdentityIdentity:output:0"/device:CPU:0*
T0*
_output_shapes
: u
Read_1/DisableCopyOnReadDisableCopyOnRead!read_1_disablecopyonread_variable"/device:CPU:0*
_output_shapes
 �
Read_1/ReadVariableOpReadVariableOp!read_1_disablecopyonread_variable^Read_1/DisableCopyOnRead"/device:CPU:0*
_output_shapes
: *
dtype0e

Identity_2IdentityRead_1/ReadVariableOp:value:0"/device:CPU:0*
T0*
_output_shapes
: [

Identity_3IdentityIdentity_2:output:0"/device:CPU:0*
T0*
_output_shapes
: �
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*m
valuedBbBa/.ATTRIBUTES/VARIABLE_VALUEBb/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPHs
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueBB B B �
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:0Identity_1:output:0Identity_3:output:0savev2_const"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtypes
2�
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0^SaveV2"/device:CPU:0*
N*
T0*
_output_shapes
:�
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 h

Identity_4Identityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: S

Identity_5IdentityIdentity_4:output:0^NoOp*
T0*
_output_shapes
: �
NoOpNoOp^MergeV2Checkpoints^Read/DisableCopyOnRead^Read/ReadVariableOp^Read_1/DisableCopyOnRead^Read_1/ReadVariableOp*
_output_shapes
 "!

identity_5Identity_5:output:0*(
_construction_contextkEagerRuntime*
_input_shapes

: : : : 2(
MergeV2CheckpointsMergeV2Checkpoints20
Read/DisableCopyOnReadRead/DisableCopyOnRead2*
Read/ReadVariableOpRead/ReadVariableOp24
Read_1/DisableCopyOnReadRead_1/DisableCopyOnRead2.
Read_1/ReadVariableOpRead_1/ReadVariableOp:=9

_output_shapes
: 

_user_specified_nameConst:($
"
_user_specified_name
Variable:*&
$
_user_specified_name
Variable_1:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
�
�
__inference__traced_restore_165
file_prefix%
assignvariableop_variable_1: %
assignvariableop_1_variable: 

identity_3��AssignVariableOp�AssignVariableOp_1�
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*m
valuedBbBa/.ATTRIBUTES/VARIABLE_VALUEBb/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPHv
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueBB B B �
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0* 
_output_shapes
:::*
dtypes
2[
IdentityIdentityRestoreV2:tensors:0"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOpAssignVariableOpassignvariableop_variable_1Identity:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_1IdentityRestoreV2:tensors:1"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_1AssignVariableOpassignvariableop_1_variableIdentity_1:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0Y
NoOpNoOp"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 �

Identity_2Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^NoOp"/device:CPU:0*
T0*
_output_shapes
: U

Identity_3IdentityIdentity_2:output:0^NoOp_1*
T0*
_output_shapes
: L
NoOp_1NoOp^AssignVariableOp^AssignVariableOp_1*
_output_shapes
 "!

identity_3Identity_3:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: : : 2(
AssignVariableOp_1AssignVariableOp_12$
AssignVariableOpAssignVariableOp:($
"
_user_specified_name
Variable:*&
$
_user_specified_name
Variable_1:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix"�J
saver_filename:0StatefulPartitionedCall:0StatefulPartitionedCall_18"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp:�
J
a
b
__call__

signatures"
_generic_user_object
: 2Variable
: 2Variable
�
trace_02�
__inference___call___118�
���
FullArgSpec
args�
jx
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 ztrace_0
"
signature_map
�B�
__inference___call___118x"�
���
FullArgSpec
args�
jx
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 M
__inference___call___1181�
�

�
x 
� "�
unknown 