# Three Line Plot
import random
from random import randint
from matplotlib import pyplot as plt

# The Data
list1 = [randint(1, 10) for x in range(20)]
list2 = [randint(1, 10) for x in range(20)]
list3 = [randint(1, 10) for x in range(20)]

# Colors the lines and changes how the lines look
plt.plot(list1, "rx-")
plt.plot(list2, "b.--")
plt.plot(list3, "go:")

# line plots title and labels
plt.title("Three Line Plot")
plt.xlabel("# of Numbers")
plt.ylabel("Numbers")

plt.show()