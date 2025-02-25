from tqdm import tqdm, trange
import csv
import os

bracket = ["(", ")", "{", "}", "[", "]", "\""]

def extract_compute_function(code_lines):
    ret = ""
    bracket_count = 0
    bracket_str = ""
    for line in code_lines:
        if line.strip().startswith("//"):
            continue
        if line.strip().startswith("/*"):
            while "*/" not in line:
                line = next(code_lines)
        ret += line
        for c in line:
            if c in bracket:
                bracket_str += c
        bracket_str=bracket_check(bracket_str)
        if bracket_str=="":
            return ret
    raise Exception("Matching bracket fail")

def bracket_check(bracket_str):
    stack = []
    iterator_bracket_str = iter(bracket_str)
    for c in iterator_bracket_str:
        if c in ["(", "{", "["]:
            stack.append(c)
        elif c == "\"":
            c = next(iterator_bracket_str)
            while c != "\"":
                c = next(iterator_bracket_str)
        else:
            if not stack:
                raise Exception("Bracket not match")
            if c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            else:
                raise Exception("Bracket not match")
    ret = ""
    for c in stack:
        ret += c
    return ret

def print_code_segment(file_path, code_line:int):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    code = extract_compute_function(lines[code_line-1:])

    return code


# print_code_segment("/tensorflow/core/kernels/mkl/mkl_avgpooling_op.cc", 48)
xlsx_path = './excel/result_op_codeql.xlsx'

def c_code_mapping_list(base_path, xlsx_path):
    import pandas as pd
    df = pd.read_excel('./PersistExt/excel/result_op_codeql.xlsx')

    c_mapping_list = []
    # extract 5th column
    column_class_name = df.iloc[:, 3]
    column_file_path = df.iloc[:, 4]
    column_line = df.iloc[:, 5]

    length = len(column_class_name)
    for i in range(0, length):
        file_path = column_file_path[i]
        class_name = column_class_name[i]
        line = int(column_line[i])
        try:
            code = print_code_segment(base_path + file_path, line)
            mapping_tuple = (class_name, code)
            if mapping_tuple not in c_mapping_list:
                c_mapping_list.append(mapping_tuple)
            # print(code)
        except:
            continue

    # print("length=", length)
    return c_mapping_list

