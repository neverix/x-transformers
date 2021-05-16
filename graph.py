from matplotlib import pyplot as plt
import sys
import numpy as np

w = 56
for i in sys.argv[1:]:
 x = eval(open(f"loss-{i}.txt").read())
 x = [np.convolve(np.array(b), np.ones(w), 'valid') / w for b in zip(*x)] 
 for j, s in enumerate(x):
  #s = np.array(s)
  #s = np.convolve(s, np.ones(w), 'valid') / w
  plt.plot(s, label=i+'-'+str(j+1))
 plt.plot(np.mean(x, axis=0), label=i+' total')
plt.legend()
plt.show()
