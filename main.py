from PersistExt.py_func_op_extract import PyFuncOpExtract
import argparse
import re
import os
import sys

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
    elif args.detect and args.model:
        print(1)
    else:
        print("Invalid arguments, please provide path, version and target file path!")
        return


    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Tensorflow API or detect malicious Tensorflow models(i.e., h5 or saved_model).")

    group1 = parser.add_argument_group("Tensorflow API analysis group")
    group1.add_argument("-p", "--path", help="Tensorflow source code path")
    group1.add_argument("-v", "--version", help="Tensorflow version")
    group1.add_argument("-t", "--target", help="Target file path")
    
    group2 = parser.add_argument_group("Malicious model detection group")
    group2.add_argument("-d", "--detect", help="Model detection")
    group2.add_argument("-m", "--model", help="Tensorflow model path (i.e., h5 or saved_model)")

    args = parser.parse_args()
    
    # Ensure group1 or group2 parameters are provided as a full set
    if (args.path or args.version or args.target) and not (args.path and args.version and args.target):
        print("Error: Arguments -p, -v, -t must be used together.")
        sys.exit(1)
    elif (args.detect or args.model) and not (args.detect and args.model):
        print("Error: Arguments -d, -m must be used together.")
        sys.exit(1)
    
    main(args)