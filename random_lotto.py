import random

def get_random_numbers():
    # Określony zbiór cyfr
    digits = list(range(1, 50))

    # Generowanie tabeli losowych 6 cyfr
    random_table = random.sample(digits, k=6)

    sorted_table = sorted(random_table)

    return sorted_table