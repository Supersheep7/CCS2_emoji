import random

random.seed(42)

numbers = list(range(1, 95))

all_pairs = [(a-1, b-1) for a in numbers for b in numbers if a != b]

random_pairs = random.sample(all_pairs, 30)

print(random_pairs)

