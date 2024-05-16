from LinearCongruential import LinearCongruential as random

num = random.rand_int(seed=4, mod=9, multiplier=2, c=3)


i = 15
while i > 0:
    print(f"Random num: {num}")
    num = random.rand_int(seed=num, mod=9, multiplier=2, c=3)
    i -= 1
