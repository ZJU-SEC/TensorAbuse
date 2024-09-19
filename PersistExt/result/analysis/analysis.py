import extract_c_code
import read_macro_csv
import read_op_xlsx
import json

c_mapping_list = extract_c_code.c_code_mapping_list(extract_c_code.xlsx_path)

op_mapping_dict = read_macro_csv.op_name_mapping(read_macro_csv.csv_file_path)

python_list = read_op_xlsx.python_code_list(path=read_op_xlsx.path)


def gen_c_python_mapping_list(c_mapping_list, op_mapping_dict, python_list):
    c_python_mapping_list = []
    for item in python_list:
        pattern_str = "_op_def_library._apply_op_helper("
        op_name_index = item.find(pattern_str) + len(pattern_str)
        # print("op_name_index = ", op_name_index)
        op_name_begin = item.find('"', op_name_index)
        # print("op_name_begin = ", op_name_begin)
        op_name_end = item.find('"', op_name_begin + 1)
        # print("op_name_end = ", op_name_end)
        op_name = item[op_name_begin + 1:op_name_end]

        # print("op_name = ", op_name)

        class_name = None
        for class_item, macro_names in op_mapping_dict.items():
            if op_name in macro_names:
                class_name = class_item
                break
        if class_name == None:
            continue

        select_c_code = None
        for c_tuple in c_mapping_list:
            if c_tuple[0] == class_name:
                select_c_code = c_tuple[1]
                break
        
        if select_c_code == None:
            continue
        
        json_tuple = {"Op name": op_name, "OpKernel class name": class_name, "Python code": item, "C++ code": select_c_code}
        if json_tuple not in c_python_mapping_list:
            c_python_mapping_list.append(json_tuple)
    
    return c_python_mapping_list

mapping_list = gen_c_python_mapping_list(c_mapping_list, op_mapping_dict, python_list)

json_data = json.dumps(mapping_list, ensure_ascii=False, indent=4)
with open('PersistExt_result.json', 'w', encoding='utf-8') as file:
    file.write(json_data)
