import random


def shuffle_sequence(sequence: str) -> str:
    bases = list(sequence)
    random.shuffle(bases)
    return "".join(bases)
