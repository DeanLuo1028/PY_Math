import random
def happen(p): return random.random() < p

probability = 0.5
happened_num = 0
no_happened_num = 0

for i in range(10000):
    if happen(probability): happened_num += 1
    else: no_happened_num += 1

print("Probability of happening:", probability)
print("Number of times happened:", happened_num)
print("Number of times not happened:", no_happened_num)