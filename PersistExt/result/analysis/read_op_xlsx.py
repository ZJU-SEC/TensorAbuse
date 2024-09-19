import pandas as pd

path = './excel/python_code.xlsx'
def python_code_list(path):
    code_list = []
    df = pd.read_excel(path)

    # extract first column data
    column_python = df.iloc[:, 0]
    for value in column_python:
        code_list.append(value)

    return code_list

