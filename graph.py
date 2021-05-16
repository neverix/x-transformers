from matplotlib import pyplot as plt
import sys

for i in sys.argv[1:]:
 x = eval(open(f"loss-{i}.txt").read())
 plt.plot(x)
plt.show()
