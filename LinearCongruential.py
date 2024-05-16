class LinearCongruential:
    def __init__(self):
        pass

    @staticmethod
    def rand_int(seed: int, multiplier: int, mod: int, c: int = 0):
        num = int((multiplier * seed + c) % mod)
        return num


class MiddleSquare:
    def __init__(self):
        # self.seed = seed
        # self.mod = mod
        pass

    @staticmethod
    def get_random_number(seed, mod):
        square = str(seed**2)
        if len(square) % 2 != 0:
            square = "0" + square
        mid = int(len(square) / 4)
        return int(square[mid: len(square) - mid]) % mod
