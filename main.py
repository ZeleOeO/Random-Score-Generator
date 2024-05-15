import randing


random_num1 = randing.LinearCongruential(27, 17, 100)
# print(random_num1.get_next_seed())
random_num2 = randing.SquaredRandom(random_num1.get_next_seed(), 7)
num = random_num2.get_random_number()
print(f"Random num {num} type: {type(num)}")
