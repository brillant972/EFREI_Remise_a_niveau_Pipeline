import json
import datetime
import os
import shutil

def read_transactions(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def generate_json(transactions_generator):
    transactions = {}
    
    for line in transactions_generator :
        parts = line.split()
        if parts != [] :
            print(f"{parts}")
            name = parts[0]
            amount = int(parts[2].replace('€', ''))
        
        if name in transactions:
            transactions[name] += amount
        else:
            transactions[name] = amount
    
    for name, total in transactions.items():
        yield {"name": name, "total_sent": total} 

def save_result(path, transactions_generator, result_dir):
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    identifier = path.split('sample')[1].split('.')[0]
    file_name = f"result_sample{identifier}_{current_datetime}.json"
    
    result_path = os.path.join(result_dir, file_name)
    
    with open(result_path, 'w') as file:
        json.dump(list(transactions_generator), file, indent=4)

    return result_path

def process_files(source_dir: str = "source", result_dir: str = "result", archived_dir: str = "archived"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    source_dir = os.path.join(script_dir, source_dir)
    result_dir = os.path.join(script_dir, result_dir)
    archived_dir = os.path.join(script_dir, archived_dir)
    
    os.makedirs(result_dir, exist_ok=True)
    os.makedirs(archived_dir, exist_ok=True)
    
    for file_name in os.listdir(source_dir):
        if file_name.endswith('.txt'):
            file_path = os.path.join(source_dir, file_name)
            
            transactions_generator = read_transactions(file_path)
            json_generator = generate_json(transactions_generator)
            
            result_path = save_result(file_name, json_generator, result_dir)
            print(f"Fichier traité : {file_name}, résultat sauvegardé dans : {result_path}")
            
            archived_path = os.path.join(archived_dir, file_name)
            shutil.move(file_path, archived_path)
            print(f"Fichier déplacé dans le dossier archived : {archived_path}")

process_files()
