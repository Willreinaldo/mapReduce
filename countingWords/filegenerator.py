import random

def generate_random_word(alphabet, min_size, max_size):
    size = random.randint(min_size, max_size)
    return ''.join(random.choice(alphabet) for _ in range(size))

def file_generator(split, n, alphabet, min_size, max_size):
    words = []
    for _ in range(n):
        words.append(generate_random_word(alphabet, min_size, max_size))

    # Dividindo o arquivo em várias partes
    files = [f"part_{i}.txt" for i in range(split)]
    for i, word in enumerate(words):
        file_name = files[i % split]
        with open(file_name, "a") as file:
            file.write(word + "\n")

file_generator(split=5, n=200, alphabet="aefw", min_size=3, max_size=5)