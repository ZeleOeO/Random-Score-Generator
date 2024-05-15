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
    def __init__(self, seed):
        self.seed = seed

    def get_random_number(self):
        square = str(self.seed**2)
        print(square)
        if len(square) % 2 != 0:
            square = "0" + square
        print(square)
        mid = int(len(square) / 4)
        print("mid", mid, "len", len(square))
        return square[mid : len(square) - mid]


random1 = SquaredRandom(130000)
random2 = SquaredRandom(random1)
print(random1.get_random_number())
print(random2.get_random_number())
