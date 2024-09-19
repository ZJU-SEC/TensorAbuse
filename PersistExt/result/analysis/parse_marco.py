import re

def extract_macro_content(input_string):
    # Regular expression pattern to match macro content
    pattern = r'Name\("([^"]+)"\).*?,\s*(\w+(?:::\w+)*)(?:<[^>]+>)?'

    name_index = input_string.find('Name("')
    if(name_index == -1):
        return None
    name_index_end = input_string.find('")', name_index)
    macro_name = input_string[name_index + 6 : name_index_end]

    class_index = input_string.rfind(',')
    # while input_string.find(">", class_index) != -1 and input_string.find("<", class_index) == -1:
    #     class_index = input_string.rfind(',', 0, class_index)
    end_index = input_string.rfind(')') - 1
    if input_string[input_string.rfind(')') - 1] == '>':
        num_rangle = 1
        num_langle = 0
        while num_rangle != num_langle:
            end_index -= 1
            if input_string[end_index] == '>':
                num_rangle += 1
            if input_string[end_index] == '<':
                num_langle += 1
        class_index = input_string.rfind(',', 0, end_index)
    else:
        end_index += 1



    class_name = input_string[class_index + 1 : end_index]
    if class_name.find("::") != -1:
        index = class_name.find("::")
        class_name = class_name[index + 2:]
    
    return (class_name, macro_name)

# Example usage
# input_string1 = 'REGISTER_KERNEL_BUILDER(Name("Sign").Device(DEVICE_DEFAULT).HostMemory("x").HostMemory("y").TypeConstraint<int32>("T"),UnaryOp<CPUDevice,functor::sign<int32>>)'
# input_string2 = 'REGISTER_KERNEL_BUILDER(Name("UnsortedSegmentJoin").Device(DEVICE_CPU).TypeConstraint<indices_type>("Tindices").TypeConstraint<num_segments_type>("Tnumsegments"),data::UnsortedSegmentJoinOp<a, data::<aaa>, data::<bbb>>)'

# print(extract_macro_content(input_string2))
# # print(extract_macro_content(input_string2))
