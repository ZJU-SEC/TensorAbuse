malicious_op_list = [
    "ReadFile",
    "FixedLengthRecordDataset",
    "FixedLengthRecordDatasetV2",
    "CSVDataset",
    "CSVDatasetV2",
    "ExperimentalCSVDataset",
    "ImmutableConst",
    "InitializeTableFromTextFile",
    "InitializeTableFromTextFileV2",
    "WriteFile",
    "Save",
    "SaveSlices",
    "PrintV2",
    "MatchingFiles",
    "MatchingFilesDataset",
    "ExperimentalMatchingFilesDataset",
    "DebugIdentity",
    "DebugIdentityV2",
    "DebugIdentityV3",
    "DistributedSave",
    "RpcCall",
    "RpcClient",
    "RpcServer",
    "RpcServerRegister",
    "RegisterDataset",
    "RegisterDatasetV2",
    "DataServiceDataset",
    "DataServiceDatasetV2",
    "DataServiceDatasetV3",
    "DataServiceDatasetV4",
    "SqlDataset"
]

malicious_op_args = {
    "ReadFile":["filename"],
    
    "FixedLengthRecordDataset":["filenames"],
    "FixedLengthRecordDatasetV2":["filenames"],
    
    "CSVDataset":["filenames"],
    "CSVDatasetV2":["filenames"],
    "ExperimentalCSVDataset":["filenames"],
    
    "ImmutableConst":["memory_region_name"],
    
    "InitializeTableFromTextFile":["filename"],
    "InitializeTableFromTextFileV2":["filename"],
    
    "WriteFile":["filename"],
    
    "Save":["filename"],
    "SaveSlices":["filename"],
    
    "PrintV2": ["output_stream"],
    
    "MatchingFiles": ["pattern"],
    "MatchingFilesDataset": ["patterns"],
    "ExperimentalMatchingFilesDataset": ["patterns"],
    
    "DebugIdentity": ["debug_urls"],
    "DebugIdentityV2": ["debug_urls"],
    "DebugIdentityV3": ["debug_urls"],
    
    "DistributedSave": ["address"],
    "RpcCall": ["method_name"],
    "RpcClient": ["server_address"],
    "RpcServer": ["server_address"],
    "RpcServerRegister": ["method_name"],
    
    "RegisterDataset": ["address"],
    "RegisterDatasetV2": ["address"],
    
    "DataServiceDataset": ["address"],
    "DataServiceDatasetV2": ["address"],
    "DataServiceDatasetV3": ["address"],
    "DataServiceDatasetV4": ["address"],
    
    "SqlDataset": ["data_source_name"]
}

malicious_files = [
    "/etc/*", 
    "/boot/*", 
    "/lib/*", 
    "/var/*", 
    "/usr/*",
    "*/.bashrc",
    "*/.bash_profile",
    "*/.zshrc",
    "*/.ssh/authorized_keys",
    "*/tensorflow.py",
    "*.py"
]

safe_ips = [
    
]
