import csv
import parse_marco

base_path = "/path/to/TensorFlow_source_code"
# your tensorflow source code base path
def clean_line(line):
    # Remove spaces, tabs, backslashes, and newlines
    return line.replace(" ", "").replace("\t", "").replace("\\", "").replace("\n", "").replace("\r", "")

def read_file_section(file_path, start_line, start_char, end_line, end_char):
    try:
        output_line = ""
        with open(base_path + file_path, 'r') as file:
            lines = file.readlines()
            for line_number in range(start_line - 1, end_line):
                line = lines[line_number]
                if line_number == start_line - 1:
                    output_line += clean_line(line[start_char - 1:])
                elif line_number == end_line - 1:
                    output_line += clean_line(line[:end_char])
                else:
                    output_line += clean_line(line)
        return output_line
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None



def op_name_mapping(file_path):
    mapping_dict = {}
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                    input_string = row[0]
                    file_path, start_line, start_char, end_line, end_char = input_string.split(":")
                    start_line, start_char, end_line, end_char = int(start_line), int(start_char), int(end_line), int(end_char)
                    map_tuple = parse_marco.extract_macro_content(read_file_section(file_path, start_line, start_char, end_line, end_char))
                    
                    class_name = None
                    macro_name = None
                    if map_tuple != None:
                        class_name = map_tuple[0]
                        macro_name = map_tuple[1]
                    if class_name != None and macro_name != None:
                        if class_name not in mapping_dict:
                            mapping_dict[class_name] = [macro_name]
                        else:
                            if macro_name not in mapping_dict[class_name]:
                                mapping_dict[class_name].append(macro_name)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return mapping_dict

csv_file_path = './excel/result.csv'
# mapping_dict = op_name_mapping(csv_file_path)
# for class_name, macro_names in mapping_dict.items():
#     output_str = f"{class_name}:"
#     for macro_name in macro_names:
#         output_str += f"  {macro_name}"
#     # print(output_str)
