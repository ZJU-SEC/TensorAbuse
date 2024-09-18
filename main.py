from PersistExt.py_func_op_extract import PyFuncOpExtract
import argparse
import re
import os
import sys
from TensorDetect import model, scan
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
        
    elif args.model:
        path = args.model
        if not os.path.exists(path):
            print("Invalid path!")
            return

        mod = model.Model(path)
        if mod.model_type == model.ModelType.TF_H5:
            sc = scan.H5Scan(mod)
        elif mod.model_type == model.ModelType.TF_SM:
            sc = scan.SavedModelScan(mod)
        sc.scan()
        sc.print_issues()
            
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
    # group2.add_argument("-d", "--detect", help="Model detection", default=1)
    group2.add_argument("-m", "--model", help="Tensorflow model path (i.e., h5 or saved_model)")

    args = parser.parse_args()
    
    # Ensure group1 or group2 parameters are provided as a full set
    if (args.path or args.version or args.target) and not (args.path and args.version and args.target):
        print("Error: Arguments -p, -v, -t must be used together.")
        sys.exit(1)
    
    elif not (args.path and args.version and args.target) and not (args.model):
        print("Error: Arguments -m must be used.")
        sys.exit(1)
    
    main(args)