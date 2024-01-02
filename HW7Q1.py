import random
import matplotlib.pyplot as plt

def simulate():
    result = []
    for i in range(1000):
        X = random.uniform(7, 30)
        result.append(X)
    plt.hist(result, bins=12)
    plt.show()

simulate()