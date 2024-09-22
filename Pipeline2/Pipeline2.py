import os
import shutil
import json
import datetime


def load_sample(file_name):
    with open(file_name, 'r', encoding='utf-8') as file: 
        content = file.read().strip().replace('\n', ',').replace(',,', ',') 
    return content

def generate_json(transactions_list):
    transactions = {}
    for line in transactions_list:
        parts = line.strip().split()
        name = parts[0]
        amount = int(parts[2].replace('€', ''))
        if name in transactions:
            transactions[name] += amount
        else:
            transactions[name] = amount
    
    result = [{"name": name, "total_sent": total} for name, total in transactions.items()]
    return json.dumps(result)

def save_result(path, result, result_dir):
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    identifier = path.split('sample')[1].split('.')[0]
    file_name = f"result_sample{identifier}_{current_datetime}.json"
    
    result_path = os.path.join(result_dir, file_name)
    
    with open(result_path, 'w') as file:
        json.dump(result, file, indent=4)

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
            
            content = load_sample(file_path).split(',')
            result = generate_json(content)
            
            result_path = save_result(file_name, result, result_dir)
            print(f"Fichier traité : {file_name}, résultat sauvegardé dans : {result_path}")
            
            archived_path = os.path.join(archived_dir, file_name)
            shutil.move(file_path, archived_path)
            print(f"Fichier déplacé dans le dossier archived : {archived_path}")

process_files()
