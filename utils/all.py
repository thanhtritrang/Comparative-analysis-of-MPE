import pandas as pd
import os

sz = {
'celegansneural': 297,
'jazz': 198,
'lastfm_asia_edges': 7624,
'ca-GrQc': 5241,
'wiki-Vote':7115,
'as-caida20071105':26475,
'p2p-Gnutella31':62586,
'email-EuAll':265214, 
'soc-Epinions1':75879,
'hollywood-2009':51140,
'com-dblp.ungraph':317080,
'road-belgium-osm':1441295,
'com-youtube.ungraph':1134890,
'twitter_combined':81306,
'amazon0505':410236,
'web-Google':875713,
'road_usa':4682832,
'soc-LiveJournal1':4847571,
'soc-orkut':2997166,
'facebook_combined':4039,
'karate_edges':77
}

kplexes = []

sz2 = {
'celegansneural': "(297,2345)",
'jazz': "(198,2742)",
'lastfm_asia_edges': "(7624, 27806)",
'ca-GrQc': "(5241,14484)",
'wiki-Vote':"(7115, 100762)",
'as-caida20071105':"(26475, 106762)",
'p2p-Gnutella31':"(62586, 147892)",
'email-EuAll':"(265214, 420045)", 
'soc-Epinions1':"(75879, 508837)",
'hollywood-2009':"(51140, 930414)",
'com-dblp.ungraph':"(317080, 1049866)",
'road-belgium-osm':"(1441295,1549970)",
'com-youtube.ungraph':"(1134890,2987624)",
'twitter_combined':"(81306,1768149)",
'amazon0505':"(410236, 3356824)",
'web-Google':"(875713, 5105039)",
'road_usa':"(4682832,25690335)",
'soc-LiveJournal1':"(4847571,68993773)",
'soc-orkut':"(2997166, 106349209)",
'facebook_combined':"(4039,88234)"
}

def is_file_empty(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path):
        content = open(file_path, 'r').readlines()
        if content[0].startswith("Timeout"):
            return 1
        for line in content:
            if "Killed" in line:
                return 1
        return 0
    return 1

def sort_by_time(filepath):
    df = pd.read_csv(filepath)
    df = df.sort_values(by='time', ascending=False)
    return df

def get_list_files(data_path, endswith=".txt"):
    files = [f for f in os.listdir(data_path) if f.endswith(endswith)]
    files = sorted(files, key=lambda f: os.path.getsize(os.path.join(data_path, f)))
    return files

def extract_info_textui(filepath):
    
    filename = os.path.basename(filepath)
    parts = filename.split('-')
    q = int(filename.split('-q')[1].split()[0])
    k = int(filename.split('-k')[1].split('.')[0])
    name = filename.split('-q')[0].strip().replace("text_ui_","")

    with open(filepath, "r") as f:
        lines = f.readlines()
    
    solutions_found = None
    running_time = None
    
    for line in lines:
        if ("Timeout" in line) or ("Error" in line):
            return name, k, q, "inf", -1

        if "Solutions found:" in line:
            solutions_found = int(line.split(":")[1].strip())
        if "Running time:" in line:
            running_time = float(line.split(":")[1].strip())
        if "Run time:" in line:
            running_time = float(line.split(":")[1].strip().replace("ms",""))/1000
    # results/output/chirop/text_ui/text_ui_wiki-Vote -q 100 -k 5.txt
    
    return name, k, q, solutions_found, running_time

def sort_store(data, path):
    
    df = pd.DataFrame(data, columns=["name", "k", "q", "k-plexes", "time"])
    df['size'] = df['name'].map(sz)
    df = df.sort_values(by=['size','name','k','q'], ascending=True)

    df.to_csv(path, index=False)

def textui_to_csv(path= "results/output/chirop/text_ui/"):
    files = get_list_files(path)
    data = []
    for f in files:
        data.append(extract_info_textui(path+f))
    sort_store(data, "results/csv/text_ui.csv")

def extract_info_sape(filepath):
    filename = os.path.basename(filepath)
    filename = filename.replace("_-k=","@-k=").strip()
    
    k = int(filename.split('-k=')[1].split()[0])
    minsize = int(filename.split('-minsize=')[1].split()[0])

    name = filename.split('@')[0].replace("sape_","")
    name = name.replace(".sape","")

    nb_models = "inf"
    running_time = -1

    with open(filepath, "r") as f:
        lines = f.readlines()
        
        for idx, line in enumerate(lines):
            if "nb models" in line:
                nb_models = int(lines[idx+2].split('|')[1].strip())
            if "Running time:" in line:
                running_time = float(line.split(":")[1].strip())
            if "OutOfMemoryException" in line:
                running_time = "-2"
                break
            if "Timeout" in line:
                running_time = "-1"
                break
    return name, k, minsize, nb_models, running_time

def sape_to_csv(path):
    files = get_list_files(path)
    data = []
    for f in files:
        print(f)
        data.append(extract_info_sape(path+f))
    sort_store(data, "results/csv/sape.csv")

def extract_info_plexnum(filepath):
    filename = os.path.basename(filepath)
    name = filename.split('PlexEnum_')[1].split('.bin')[0]
    k = int(filename.split('-k ')[1].split()[0])
    q = int(filename.split('-q ')[1].split('.')[0])

    with open(filepath, "r") as f:
        lines = f.readlines()
    
    solutions_found = "inf"
    running_time = -1

    for line in lines:
        if ("Timeout" in line):
            return name, k, q, "inf", -1
        if ("Segmentation fault" in line):
            return name, k, q, "inf", -2
        if "Number of" in line:
            solutions_found = int(line.split(":")[1].strip())
        elif "Running time: " in line:
            running_time = float(line.replace("Running time: ","").strip())
    
    return name, k, q, solutions_found, running_time

def plexnum_to_csv(path):
    files = get_list_files(path)
    data = []
    for f in files:
        print(f)
        data.append(extract_info_plexnum(path+f))
    sort_store(data, "results/csv/plexnum.csv")

def extract_info_listPlex(filepath):
    filename = os.path.basename(filepath)
    name = filename.split('listPlex_')[1].split('.bin')[0]
    k = int(filename.split('listPlex_')[1].split(' ')[1])
    q = int(filename.split('listPlex_')[1].split(' ')[2].split('.')[0])

    with open(filepath, "r") as f:
        lines = f.readlines()
    
    solutions_found = "inf"
    running_time = -1
    
    for line in lines:
        if ("Timeout" in line) and len(lines) == 1:
            return name, k, q, "inf", -1
        if ("Segmentation fault" in line):
            return name, k, q, "inf", -2
        if "-plex:" in line:
            solutions_found = int(line.split(":")[1].strip())
        elif "Running time" in line:
            running_time = float(line.replace("Running time","").replace(":","").strip())
    
    return name, k, q, solutions_found, running_time

def listPlex_to_csv(path):
    files = get_list_files(path)
    data = []
    for f in files:
        print(f)
        data.append(extract_info_listPlex(path+f))
    sort_store(data, "results/csv/listPlex.csv")

def extract_info_kplexenum(filepath):
    filename = os.path.basename(filepath)
    name = filename.split('kplexEnum_')[1].split('.bin')[0]
    k = int(filename.split('-k=')[1].split()[0])
    q = int(filename.split('-q=')[1].split()[0])

    with open(filepath, "r") as f:
        lines = f.readlines()
    
    solutions_found = "inf"
    running_time = -1
    
    for line in lines:
        if ("Timeout" in line) and len(lines) == 1:
            running_time = -1
        if ("Segmentation fault" in line):
            running_time = -2
        if "Number of plexes" in line:
            solutions_found = int(line.split(":")[1].strip())
        elif "Enum time: " in line:
            running_time = float(line.replace("Enum time: ","").replace("sec","").strip())
    
    return name, k, q, solutions_found, running_time

def kplexEnum_to_csv(path):
    files = get_list_files(path)
    data = []
    for f in files:
        print(f)
        data.append(extract_info_kplexenum(path+f))
    sort_store(data, "results/csv/kplexEnum.csv")

def extract_info_enplex(filepath):
    filename = os.path.basename(filepath)
    filename = filename.replace("_-k"," -k")
    name = filename.split('enplex_')[1].split(' ')[0]
    k = int(filename.split('-k ')[1].split()[0])
    q = int(filename.split('-l ')[1].split()[0])

    with open(filepath, "r") as f:
        lines = f.readlines()
    
    solutions_found = "inf"
    running_time = -1
 
    lines = [line.strip() for line in lines if line.strip()]
    for line in lines:
        if ("Timeout" in line) and len(lines) <= 2:
            return name, k, q, "inf", -1
        if ("Segmentation fault" in line):
            return name, k, q, "inf", -2
        if ("Killed" in line) and len(lines) == 1:
            return name, k, q, "inf", -3
        if "Number of " in line:
            solutions_found = int(line.split(":")[1].strip())
        elif "Running time: " in line:
            running_time = float(line.replace("Running time: ","").replace("sec","").strip())
    
    return name, k, q, solutions_found, running_time

def enplex_to_csv(path):
    files = get_list_files(path)
    data = []
    for f in files:
        print(f)
        if "2500" in f:
            continue
        data.append(extract_info_enplex(path+f))
    sort_store(data, "results/csv/enplex.csv")

def extract_info_gp(filepath):
    filename = os.path.basename(filepath)
    filename = filename.replace(".txt2","")
    filename = filename.replace("BinaryOptimizeWithPrunNot_","")
    name = filename.split('.sape_')[0]
    q = int(filename.split('.sape_')[1].split("_")[0])
    k = int(filename.split('.sape_')[1].split("_")[1])
    
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    solutions_found = "inf"
    running_time = -1
    
    lines = [line.strip() for line in lines if line.strip()]
    for line in lines:
        if "total_kplexNum: " in line:
            solutions_found = int(line.split(":")[1].strip())
        elif "time:" in line:
            running_time = float(line.split(":")[1].replace("s","").strip())
    
    return name, k, q, solutions_found, running_time

def gp_to_csv(path):
    files = get_list_files(path, ".txt2")
    data = []
    for f in files:
        if "BinaryOptimizeWithPrunNot" in f:
            print(f)
            data.append(extract_info_gp(path+f))
    sort_store(data, "results/csv/GP.csv")

def extract_info_bk(filepath):
    filename = os.path.basename(filepath)
    filename = filename.replace(".txt2","")
    filename = filename.replace("MyOptimize_","")
    name = filename.split('_')
    name = "_".join(name[:-2])
    q = int(filename.split('_')[-2])
    k = int(filename.split('_')[-1])
    
    lines = []
    if not "MyOptimize_jazz_10_5.txt2" in filepath:
        with open(filepath, "r") as f:
            lines = f.readlines()
    
    solutions_found = "inf"
    running_time = -1
    
    lines = [line.strip() for line in lines if line.strip()]
    for line in lines:
        if ("Timeout" in line) and len(lines) <= 2:
            return name, k, q, "inf", -1
        if ("Segmentation fault" in line):
            return name, k, q, "inf", -2
        if ("Killed" in line) and len(lines) == 1:
            return name, k, q, "inf", -3
        if "kplexNum:" in line:
            solutions_found = int(line.split(":")[1].strip())
        elif "Running time: " in line:
            running_time = float(line.replace("Running time: ","").replace("sec","").strip())
    
    return name, k, q, solutions_found, running_time

def bk_to_csv(path):
    files = get_list_files(path, ".txt2")
    data = []
    for f in files:
        if "MyOptimize" in f:
            print(f)
            data.append(extract_info_bk(path+f))
    sort_store(data, "results/csv/BK.csv")

def checK_correct_info(path):
    import numpy as np
    df = pd.read_csv(path)
    df = df[(df['time'] == -1.0)]
    df.to_csv("tmp.csv", index=False)
