from PersistExt.py_func_op_extract import PyFuncOpExtract
import argparse
import re
import os

pattern = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)' \
              r'(-[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?' \
              r'(\+[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?$'
              
def main(args):
    if args.path and args.version and args.target:
        path = args.path
        if not os.path.exists(path):
            print("Invalid path")
            return
        
        if re.match(pattern, args.version) is None:
            print("Invalid version format")
            return
        else:
            version = 2 if args.version.split(".")[0]=='2' else 1
        py_func_op_extract = PyFuncOpExtract(version, path)
        py_func_op_extract.analyze_tensorflow_source()
        py_func_op_extract.get_results(args.target)
    else:
        print("Invalid arguments, please provide path, version and target file path!")
        return


    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Tensorflow API or detect malicious Tensorflow models(i.e., h5 or saved_model).")

    # group = parser.add_mutually_exclusive_group()
    parser.add_argument("-p", "--path", help="Tensorflow source code path")
    parser.add_argument("-v", "--version", help="Tensorflow version")
    parser.add_argument("-t", "--target", help="Target file path")
    args = parser.parse_args()
    main(args)