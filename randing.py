class LinearCongruential:
    def __init__(self, seed: int, a: int, m: int, c: int = 0):
        self.seed = seed
        self.a = a
        self.m = m
        self.c = c

    def get_next_seed(self):
        return (self.a * self.seed + self.c) % self.m

    def get_random_number(self):
        return self.get_next_seed() / self.m


class SquaredRandom:
    def __init__(self, seed, mod):
        self.seed = seed
        self.mod = mod

    def get_random_number(self):
        square = str(self.seed**2)
        if len(square) % 2 != 0:
            square = "0" + square
        mid = int(len(square) / 4)
        return int(square[mid : len(square) - mid]) % self.mod
