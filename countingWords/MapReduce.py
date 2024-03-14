import re
import threading

# Função Map
def map_function(file_name):
    word_counts = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = re.findall(r'\w+', line.lower())
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    with open(".temp.txt", "a") as temp_file:
        for word, count in word_counts.items():
            temp_file.write(f"{word} : \"{count}\"\n")

 # Função Reduce
processed_words = set()

def reduce_function(word):
    if word in processed_words:
        return
    processed_words.add(word)
    
    counts = []
    with open(".temp.txt", "r") as temp_file:
        for line in temp_file:
            if line.startswith(word):
                counts.append(int(line.split(":")[1].strip().strip('"')))
    total_count = sum(counts)
    with open("final_output.txt", "a") as final_file:
        final_file.write(f"{word} : {total_count}\n")
        
# Função para gerenciar threads
def process_files(file_names):
    threads = []
    for file_name in file_names:
        thread = threading.Thread(target=map_function, args=(file_name,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    with open(".temp.txt", "r") as temp_file:
        for line in temp_file:
            word = line.split(":")[0].strip()
            reduce_function(word)

# Lista de arquivos gerados pelo FileGenerator
file_names = ["part_0.txt", "part_1.txt", "part_2.txt", "part_3.txt", "part_4.txt"]

# Executando o sistema MapReduce
process_files(file_names)
