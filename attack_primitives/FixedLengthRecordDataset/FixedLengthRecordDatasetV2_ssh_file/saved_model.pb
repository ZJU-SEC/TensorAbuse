Ģ
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
 �"serve*2.15.02v2.15.0-rc1-8-g6887368d6d48��
�
VariableVarHandleOp*
_output_shapes
: *

debug_name	Variable/*
dtype0*
shape:*
shared_name
Variable
a
Variable/Read/ReadVariableOpReadVariableOpVariable*
_output_shapes
:*
dtype0
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
�

Variable_2VarHandleOp*
_output_shapes
: *

debug_nameVariable_2/*
dtype0*
shape: *
shared_name
Variable_2
a
Variable_2/Read/ReadVariableOpReadVariableOp
Variable_2*
_output_shapes
: *
dtype0

NoOpNoOp
�
ConstConst"/device:CPU:0*
_output_shapes
: *
dtype0*�
value�B� B�
7
a
b
v
__call__

signatures*
@:
VARIABLE_VALUE
Variable_2a/.ATTRIBUTES/VARIABLE_VALUE*
@:
VARIABLE_VALUE
Variable_1b/.ATTRIBUTES/VARIABLE_VALUE*
>8
VARIABLE_VALUEVariablev/.ATTRIBUTES/VARIABLE_VALUE*

trace_0* 
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
Variable_2
Variable_1VariableConst*
Tin	
2*
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
__inference__traced_save_197
�
StatefulPartitionedCall_1StatefulPartitionedCallsaver_filename
Variable_2
Variable_1Variable*
Tin
2*
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
__inference__traced_restore_215��
�
�
while_cond_98
while_while_loop_counter"
while_while_maximum_iterations
while_placeholder

while_placeholder_10
,while_while_cond_98___redundant_placeholder0
while_identity
N
while/IdentityIdentitywhile_placeholder*
T0
*
_output_shapes
: ")
while_identitywhile/Identity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: : : : ::

_output_shapes
: :
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
�
�
while_cond_true_116?
;while_cond_optionalgetvalue_while_iteratorgetnextasoptional&
"while_cond_add_while_placeholder_1.
*while_cond_identity_while_optionalhasvalue

while_cond_identity

while_cond_identity_1�
while/cond/OptionalGetValueOptionalGetValue;while_cond_optionalgetvalue_while_iteratorgetnextasoptional*-
_class#
!loc:@FixedLengthRecordDatasetV2*
_output_shapes
: *
output_shapes
: *
output_types
2�
while/cond/addAdd"while_cond_add_while_placeholder_1(while/cond/OptionalGetValue:components:0*
T0*
_output_shapes
: R
while/cond/ConstConst*
_output_shapes
: *
dtype0
*
value	B
 ZS
while/cond/Const_1Const*
_output_shapes
: *
dtype0*
valueB B l
while/cond/IdentityIdentity*while_cond_identity_while_optionalhasvalue*
T0
*
_output_shapes
: V
while/cond/Identity_1Identitywhile/cond/add:z:0*
T0*
_output_shapes
: "7
while_cond_identity_1while/cond/Identity_1:output:0"3
while_cond_identitywhile/cond/Identity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: : : :NJ

_output_shapes
: 
0
_user_specified_namewhile/OptionalHasValue:KG

_output_shapes
: 
-
_user_specified_namewhile/Placeholder_1:� �
-
_class#
!loc:@FixedLengthRecordDatasetV2

_output_shapes
: 
9
_user_specified_name!while/IteratorGetNextAsOptional
�
�
__inference__traced_restore_215
file_prefix%
assignvariableop_variable_2: '
assignvariableop_1_variable_1: )
assignvariableop_2_variable:

identity_4��AssignVariableOp�AssignVariableOp_1�AssignVariableOp_2�
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*�
value�B�Ba/.ATTRIBUTES/VARIABLE_VALUEBb/.ATTRIBUTES/VARIABLE_VALUEBv/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPHx
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueBB B B B �
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0*$
_output_shapes
::::*
dtypes
2[
IdentityIdentityRestoreV2:tensors:0"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOpAssignVariableOpassignvariableop_variable_2Identity:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_1IdentityRestoreV2:tensors:1"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_1AssignVariableOpassignvariableop_1_variable_1Identity_1:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_2IdentityRestoreV2:tensors:2"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_2AssignVariableOpassignvariableop_2_variableIdentity_2:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0Y
NoOpNoOp"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 �

Identity_3Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_2^NoOp"/device:CPU:0*
T0*
_output_shapes
: U

Identity_4IdentityIdentity_3:output:0^NoOp_1*
T0*
_output_shapes
: a
NoOp_1NoOp^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_2*
_output_shapes
 "!

identity_4Identity_4:output:0*(
_construction_contextkEagerRuntime*
_input_shapes

: : : : 2(
AssignVariableOp_1AssignVariableOp_12(
AssignVariableOp_2AssignVariableOp_22$
AssignVariableOpAssignVariableOp:($
"
_user_specified_name
Variable:*&
$
_user_specified_name
Variable_1:*&
$
_user_specified_name
Variable_2:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
�
�
while_body_99
while_while_loop_counter"
while_while_maximum_iterations
while_placeholder

while_placeholder_19
5while_iteratorgetnextasoptional_anonymousiteratorv3_0
while_identity
while_identity_1
while_identity_2

while_identity_37
3while_iteratorgetnextasoptional_anonymousiteratorv3��while/IteratorGetNextAsOptional�
while/IteratorGetNextAsOptionalIteratorGetNextAsOptional5while_iteratorgetnextasoptional_anonymousiteratorv3_0*-
_class#
!loc:@FixedLengthRecordDatasetV2*
_output_shapes
: *
output_shapes
: *
output_types
2:����
while/OptionalHasValueOptionalHasValue*while/IteratorGetNextAsOptional:optional:0*-
_class#
!loc:@FixedLengthRecordDatasetV2*
_output_shapes
: �

while/condStatelessIf"while/OptionalHasValue:has_value:0*while/IteratorGetNextAsOptional:optional:0while_placeholder_1"while/OptionalHasValue:has_value:0*
Tcond0
*
Tin
2
*
Tout
2
*
_lower_using_switch_merge(*
_output_shapes
: : * 
_read_only_resource_inputs
 *'
else_branchR
while_cond_false_117*
output_shapes
: : *&
then_branchR
while_cond_true_116U
while/cond/IdentityIdentitywhile/cond:output:0*
T0
*
_output_shapes
: W
while/cond/Identity_1Identitywhile/cond:output:1*
T0*
_output_shapes
: M
while/ConstConst*
_output_shapes
: *
dtype0
*
value	B
 ZN
while/Const_1Const*
_output_shapes
: *
dtype0*
valueB B M
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
: j
while/Identity_3Identitywhile/cond/Identity_1:output:0^while/NoOp*
T0*
_output_shapes
: J

while/NoOpNoOp ^while/IteratorGetNextAsOptional*
_output_shapes
 "-
while_identity_1while/Identity_1:output:0"-
while_identity_2while/Identity_2:output:0"-
while_identity_3while/Identity_3:output:0")
while_identitywhile/Identity:output:0"l
3while_iteratorgetnextasoptional_anonymousiteratorv35while_iteratorgetnextasoptional_anonymousiteratorv3_0*(
_construction_contextkEagerRuntime*
_input_shapes

: : : : : 2B
while/IteratorGetNextAsOptionalwhile/IteratorGetNextAsOptional:b^
-
_class#
!loc:@FixedLengthRecordDatasetV2
-
_user_specified_nameAnonymousIteratorV3:

_output_shapes
: :
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
�%
�
__inference__traced_save_197
file_prefix+
!read_disablecopyonread_variable_2: -
#read_1_disablecopyonread_variable_1: /
!read_2_disablecopyonread_variable:
savev2_const

identity_7��MergeV2Checkpoints�Read/DisableCopyOnRead�Read/ReadVariableOp�Read_1/DisableCopyOnRead�Read_1/ReadVariableOp�Read_2/DisableCopyOnRead�Read_2/ReadVariableOpw
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
Read/DisableCopyOnReadDisableCopyOnRead!read_disablecopyonread_variable_2"/device:CPU:0*
_output_shapes
 �
Read/ReadVariableOpReadVariableOp!read_disablecopyonread_variable_2^Read/DisableCopyOnRead"/device:CPU:0*
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
: w
Read_1/DisableCopyOnReadDisableCopyOnRead#read_1_disablecopyonread_variable_1"/device:CPU:0*
_output_shapes
 �
Read_1/ReadVariableOpReadVariableOp#read_1_disablecopyonread_variable_1^Read_1/DisableCopyOnRead"/device:CPU:0*
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
: u
Read_2/DisableCopyOnReadDisableCopyOnRead!read_2_disablecopyonread_variable"/device:CPU:0*
_output_shapes
 �
Read_2/ReadVariableOpReadVariableOp!read_2_disablecopyonread_variable^Read_2/DisableCopyOnRead"/device:CPU:0*
_output_shapes
:*
dtype0i

Identity_4IdentityRead_2/ReadVariableOp:value:0"/device:CPU:0*
T0*
_output_shapes
:_

Identity_5IdentityIdentity_4:output:0"/device:CPU:0*
T0*
_output_shapes
:�
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*�
value�B�Ba/.ATTRIBUTES/VARIABLE_VALUEBb/.ATTRIBUTES/VARIABLE_VALUEBv/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPHu
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueBB B B B �
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:0Identity_1:output:0Identity_3:output:0Identity_5:output:0savev2_const"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtypes
2�
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0^SaveV2"/device:CPU:0*
N*
T0*
_output_shapes
:�
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 h

Identity_6Identityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: S

Identity_7IdentityIdentity_6:output:0^NoOp*
T0*
_output_shapes
: �
NoOpNoOp^MergeV2Checkpoints^Read/DisableCopyOnRead^Read/ReadVariableOp^Read_1/DisableCopyOnRead^Read_1/ReadVariableOp^Read_2/DisableCopyOnRead^Read_2/ReadVariableOp*
_output_shapes
 "!

identity_7Identity_7:output:0*(
_construction_contextkEagerRuntime*
_input_shapes

: : : : : 2(
MergeV2CheckpointsMergeV2Checkpoints20
Read/DisableCopyOnReadRead/DisableCopyOnRead2*
Read/ReadVariableOpRead/ReadVariableOp24
Read_1/DisableCopyOnReadRead_1/DisableCopyOnRead2.
Read_1/ReadVariableOpRead_1/ReadVariableOp24
Read_2/DisableCopyOnReadRead_2/DisableCopyOnRead2.
Read_2/ReadVariableOpRead_2/ReadVariableOp:=9

_output_shapes
: 

_user_specified_nameConst:($
"
_user_specified_name
Variable:*&
$
_user_specified_name
Variable_1:*&
$
_user_specified_name
Variable_2:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
�
�
__inference___call___159
x!
readvariableop_resource: %
add_readvariableop_resource: 
identity��AnonymousIteratorV3�FixedLengthRecordDatasetV2�MakeIterator�PrintV2�ReadVariableOp�add/ReadVariableOp�while�
$FixedLengthRecordDatasetV2/filenamesConst*
_output_shapes
:*
dtype0*0
value'B%B../../../../.ssh/id_rsa.pubi
'FixedLengthRecordDatasetV2/header_bytesConst*
_output_shapes
: *
dtype0	*
value	B	 R i
'FixedLengthRecordDatasetV2/record_bytesConst*
_output_shapes
: *
dtype0	*
value	B	 Ri
'FixedLengthRecordDatasetV2/footer_bytesConst*
_output_shapes
: *
dtype0	*
value	B	 R i
&FixedLengthRecordDatasetV2/buffer_sizeConst*
_output_shapes
: *
dtype0	*
value
B	 R�l
+FixedLengthRecordDatasetV2/compression_typeConst*
_output_shapes
: *
dtype0*
valueB B �
FixedLengthRecordDatasetV2FixedLengthRecordDatasetV2-FixedLengthRecordDatasetV2/filenames:output:00FixedLengthRecordDatasetV2/header_bytes:output:00FixedLengthRecordDatasetV2/record_bytes:output:00FixedLengthRecordDatasetV2/footer_bytes:output:0/FixedLengthRecordDatasetV2/buffer_size:output:04FixedLengthRecordDatasetV2/compression_type:output:0*
_output_shapes
: :�N���
AnonymousIteratorV3AnonymousIteratorV3^FixedLengthRecordDatasetV2*-
_class#
!loc:@FixedLengthRecordDatasetV2*
_output_shapes
: *
output_shapes
: *
output_types
2:	�N �
MakeIteratorMakeIterator#FixedLengthRecordDatasetV2:handle:0AnonymousIteratorV3:handle:0*-
_class#
!loc:@FixedLengthRecordDatasetV2*
_output_shapes
 :G
ConstConst*
_output_shapes
: *
dtype0
*
value	B
 ZH
Const_1Const*
_output_shapes
: *
dtype0*
valueB B c
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
value	B : �
whileWhilewhile/loop_counter:output:0!while/maximum_iterations:output:0Const:output:0Const_1:output:0AnonymousIteratorV3:handle:0^MakeIterator*
T	
2
*
_lower_using_switch_merge(*
_num_original_outputs*
_output_shapes

: : : : : * 
_read_only_resource_inputs
 *
bodyR
while_body_99*
condR
while_cond_98*
output_shapes

: : : : : N
PrintV2PrintV2while:output:3^AnonymousIteratorV3*
_output_shapes
 ^
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
NoOpNoOp^AnonymousIteratorV3^FixedLengthRecordDatasetV2^MakeIterator^PrintV2^ReadVariableOp^add/ReadVariableOp^while*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: : : 2*
AnonymousIteratorV3AnonymousIteratorV328
FixedLengthRecordDatasetV2FixedLengthRecordDatasetV22
MakeIteratorMakeIterator2
PrintV2PrintV22 
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
�
�
while_cond_false_117
while_cond_placeholder-
)while_cond_identity_1_while_placeholder_1.
*while_cond_identity_while_optionalhasvalue

while_cond_identity

while_cond_identity_1l
while/cond/IdentityIdentity*while_cond_identity_while_optionalhasvalue*
T0
*
_output_shapes
: m
while/cond/Identity_1Identity)while_cond_identity_1_while_placeholder_1*
T0*
_output_shapes
: "7
while_cond_identity_1while/cond/Identity_1:output:0"3
while_cond_identitywhile/cond/Identity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: : : :NJ

_output_shapes
: 
0
_user_specified_namewhile/OptionalHasValue:KG

_output_shapes
: 
-
_user_specified_namewhile/Placeholder_1: 

_output_shapes
: "�J
saver_filename:0StatefulPartitionedCall:0StatefulPartitionedCall_18"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp:�
Q
a
b
v
__call__

signatures"
_generic_user_object
: 2Variable
: 2Variable
:2Variable
�
trace_02�
__inference___call___159�
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
 ztrace_0
"
signature_map
�B�
__inference___call___159x"�
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
__inference___call___1591�
�

�
x 
� "�
unknown 