import subprocess
import multiprocessing
import os
import time
import argparse
from utils.all import is_file_empty, get_list_files

appName = ""
app = ""
extension = {
    "BinaryOptimizeWithPrunNot": ".txt",
    "enplex": ".bin",
    "kplexes": ".bin",
    "listPlex": ".txt",
    "PlexEnum": ".bin",
    "max_kplex": ".txt",
    "text_ui": ".nde"
}

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run alogrithms with multiple parameters in parallel")
    parser.add_argument("--app", type=str, required=True, help="Path to the application executable")
    parser.add_argument("--time", type=int, default=3600*24, help="Maximum execution time in seconds")
    parser.add_argument("--data_path", type=str, required=True, help="Path to the data directory")
    parser.add_argument("--k", type=str, default="2 3 4 5", help="Values of k separated by spaces")
    parser.add_argument("--q", type=str, default="10 20 30 50 100", help="Values of q separated by spaces")
    parser.add_argument("--max_processes", type=int, default=32, help="Maximum number of parallel processes")
    return parser.parse_args()

def get_list_files(data_path, endswith=".txt"):
    files = [f for f in os.listdir(data_path) if f.endswith(endswith)]
    files = sorted(files, key=lambda f: os.path.getsize(os.path.join(data_path, f)))
    return files

def runApp(param):
    name = param.split("/")[-1].replace(extension[appName], "")
    output_file = f"output/{appName}/{appName}_{name}_{param.split('/')[-1]}.txt"
    os.makedirs(f"output/{appName}/", exist_ok=True)
    command = f"{app} {param}" 

    if not is_file_empty(output_file):
        return

    with open(output_file, "w") as out:
        try:
            start_time = time.time()
            process = subprocess.run(
                command, 
                shell=True, 
                stdout=out, 
                stderr=subprocess.PIPE, 
                text=True, 
                timeout=maxsecond
            )
            end_time = time.time()
            out.write(f"\nRunning time: {end_time - start_time}\n")
            if process.returncode != 0:
                out.write(f"Error running {appName} with {param}: {process.stderr}")
        except subprocess.TimeoutExpired:
            out.write(f"Timeout expired for {appName} with {param} after {maxsecond} seconds")

def build_command(appName, file, k, m, maxsecond):
    if appName == "GP":
        return f"{file} output/{appName}/{appName}_{m}_{k} {m} {k}"
    elif appName == "enplex":
        return f"-k {k} -l {m} -d 1 -t {maxsecond} -f {file}"
    elif appName == "kplexes":
        return f"{file} -k={k} -q={m} -t=1"
    elif appName == "listPlex":
        return f"{file} {m} {k}"
    elif appName == "PlexEnum":
        return f"{file} -k {k} -q {m}"
    elif appName == "sape":
        return f"-k={k} -minsize={m} -verb=0 {file}"
    elif appName == "text_ui":
        return f"{file} -q {m} -k {k}"
    return ""
   
if __name__ == "__main__":
    args = parse_arguments()
    
    app = args.app
    maxsecond = args.time
    data_path = args.data_path
    kvalue = args.k.split()
    minsize = args.q.split()
    MAX_PROCESSES = args.max_processes

    appName = os.path.basename(app)
    files = get_list_files(data_path, extension[appName])
    
    param_list = [ build_command(appName, f, k, m, maxsecond) for f in files for k in kvalue for m in minsize]
    
    with multiprocessing.Pool(processes=MAX_PROCESSES) as pool:
        pool.map(runApp, param_list)

    print("Complete all processes!")
    # python script.py --app "algorithms/faplex-enplex/enplex" --time 86400 --data_path "datasets/txt/" --k "2 3 4 5" --q "10 20 30 50 100"
