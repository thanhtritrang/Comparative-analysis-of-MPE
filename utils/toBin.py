import subprocess
import multiprocessing
import os
import time
import argparse
from utils.all import is_file_empty, get_list_files

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run enplex with multiple parameters in parallel")
    parser.add_argument("--app", type=str, required=True, help="Path to the application executable")
    parser.add_argument("--maxsecond", type=int, default=3600*24, help="Maximum execution time in seconds")
    parser.add_argument("--data_path", type=str, required=True, help="Path to the data directory")
    parser.add_argument("--max_processes", type=int, default=64, help="Maximum number of parallel processes")
    return parser.parse_args()

def run_tobin(param):
    print(param)
    output_file = f"output/{appName}_{param}"
    command = f"{app} {data_path}{param}" 
    os.makedirs("output", exist_ok=True)
    
    with open(output_file, "w") as out:
        process = subprocess.run(command, shell=True, stdout=out, stderr=subprocess.PIPE, text=True)
        
        if process.returncode != 0:
            print(f"Error running ToBin with {param}: {process.stderr}")

if __name__ == "__main__":
    args = parse_arguments()
    
    app = args.app
    maxsecond = args.maxsecond
    data_path = args.data_path
    MAX_PROCESSES = args.max_processes

    appName = os.path.basename(app)
    param_list = [f for f in os.listdir(data_path) if f.endswith(".txt")]
    
    with multiprocessing.Pool(processes=MAX_PROCESSES) as pool:
        pool.map(run_tobin, param_list)

    print("Complete all processes!")
